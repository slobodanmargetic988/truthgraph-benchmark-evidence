#!/usr/bin/env python3
"""Recompute the 25 October 2026 comparison from the raw Codex session logs.

Standard library only. Run from this folder:  python3 verify.py
Reads logs/*.jsonl exactly as Codex wrote them and prints, per run: model, effort,
wall-clock duration, token totals, tool calls and TruthGraph calls, then the
paired difference between the two investigation runs.
"""
import glob, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = {
    '01a17372-0953-7aa1-8fb9-ca58efd98f74': 'with TruthGraph',
    '01a17378-fbf8-7da3-899f-12448bc85709': 'without TruthGraph',
}
LABELS = {**RUNS,
    '01a17381-9dde-7f50-a8ed-d237770f3703': 'Codex summary of the two runs',
    '01a17383-a155-7df2-8ec2-101f823bb417': 'sub-agent spawned by the summary thread',
}


def read(path):
    run = {'calls': 0, 'tg_calls': 0, 'prompt': None}
    for line in open(path, encoding='utf-8'):
        o = json.loads(line)
        p = o.get('payload') or {}
        kind, sub = o.get('type'), p.get('type')
        if kind == 'session_meta' and 'id' not in run:
            run['id'] = p.get('id')
        elif kind == 'turn_context':
            run['model'], run['effort'] = p.get('model'), p.get('effort')
        elif kind == 'event_msg' and sub == 'token_count' and p.get('info'):
            run['usage'] = p['info']['total_token_usage']
        elif kind == 'event_msg' and sub == 'task_complete':
            run['duration_ms'] = p.get('duration_ms')
        elif kind == 'response_item' and sub in ('custom_tool_call', 'function_call'):
            run['calls'] += 1
            if 'truthgraph' in json.dumps(p.get('input') or p.get('arguments') or '').lower():
                run['tg_calls'] += 1
        elif kind == 'response_item' and sub == 'message' and p.get('role') == 'user' and run['prompt'] is None:
            text = ' '.join(c.get('text', '') for c in p.get('content', []))
            if 'read-only investigation' in text or 'Examine these two threads' in text:
                run['prompt'] = text.split('\n')[0][:160]
    return run


runs = {}
for path in sorted(glob.glob(os.path.join(HERE, 'logs', '*.jsonl'))):
    r = read(path)
    runs[r['id']] = r
    u = r.get('usage', {})
    print(f"{os.path.basename(path)}\n  thread {r['id']}  {LABELS.get(r['id'], 'other')}")
    print(f"  model {r.get('model')} / effort {r.get('effort')}")
    print(f"  first prompt line: {r['prompt']!r}")
    print(f"  duration {r.get('duration_ms', 0) / 1000:.1f}s  tool calls {r['calls']}  calls mentioning truthgraph {r['tg_calls']}")
    print(f"  tokens: input {u.get('input_tokens'):,} (cached {u.get('cached_input_tokens'):,}, uncached {u.get('input_tokens', 0) - u.get('cached_input_tokens', 0):,})"
          f"  output {u.get('output_tokens'):,} (reasoning {u.get('reasoning_output_tokens'):,})  total {u.get('total_tokens'):,}\n")

on, off = (runs[k] for k in RUNS)
uo, uf = on['usage'], off['usage']


def change(a, b):
    return f"{a:,} vs {b:,}  ({(a - b) / b:+.1%})"


print('With TruthGraph vs without, same task, same model and effort:')
print('  total tokens    ', change(uo['total_tokens'], uf['total_tokens']))
print('  input tokens    ', change(uo['input_tokens'], uf['input_tokens']))
print('  uncached input  ', change(uo['input_tokens'] - uo['cached_input_tokens'], uf['input_tokens'] - uf['cached_input_tokens']))
print('  output tokens   ', change(uo['output_tokens'], uf['output_tokens']))
print('  duration        ', f"{on['duration_ms'] / 1000:.1f}s vs {off['duration_ms'] / 1000:.1f}s  ({(off['duration_ms'] - on['duration_ms']) / 1000:.1f}s faster)")
