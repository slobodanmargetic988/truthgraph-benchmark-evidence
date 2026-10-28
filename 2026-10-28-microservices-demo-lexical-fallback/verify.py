#!/usr/bin/env python3
"""Verify unchanged raw files and recompute this selected single comparison.

Standard library only; no network, model calls, source checkout or credentials.
"""
from pathlib import Path
import hashlib
import html
import json
import re

HERE = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_manifest():
    for line in (HERE / 'SHA256SUMS').read_text().splitlines():
        expected, name = line.split(None, 1)
        assert digest((HERE / name).read_bytes()) == expected, name


def read_run(expected):
    data = (HERE / expected['file']).read_bytes()
    assert digest(data) == expected['sha256']
    rows = [json.loads(line) for line in data.splitlines()]
    meta = next(r['payload'] for r in rows if r['type'] == 'session_meta')
    assert meta['id'] == expected['thread_id']
    turns = [r['payload'] for r in rows if r['type'] == 'turn_context']
    assert {r['model'] for r in turns} == {'gpt-6.1-sol'}
    assert {r['effort'] for r in turns} == {'ultra'}
    assert meta['model_provider'] == 'openai'
    totals = [r['payload']['info']['total_token_usage'] for r in rows
              if r['type'] == 'event_msg' and r['payload'].get('type') == 'token_count']
    usage = totals[-1]
    records = [r['payload']['usage'] for r in rows if r['type'] == 'token_usage_record']
    assert {k: sum(r.get(k, 0) for r in records) for k in usage} == usage
    completed = [r['payload'] for r in rows if r['type'] == 'event_msg'
                 and r['payload'].get('type') == 'task_complete']
    assert len(completed) == 1
    wrappers = [r['payload']['output'] for r in rows if r['type'] == 'response_item'
                and isinstance(r['payload'].get('output'), str)
                and r['payload']['output'].startswith('<codex_delegation>')]
    assert len(wrappers) == 1
    match = re.fullmatch(r'<codex_delegation>\s*<source_thread_id>[^<]+</source_thread_id>\s*<input>(.*)</input>\s*</codex_delegation>\s*', wrappers[0], re.S)
    assert match
    # The app XML-escapes arrows such as -> in its transport envelope.
    # Decode that transport once; do not trim or normalize prompt contents.
    prompt = html.unescape(match[1]).encode()
    assert digest(prompt) == expected['prompt_sha256']
    assert prompt == (HERE / expected['prompt_file']).read_bytes()
    items = [r['payload'].get('item', {}) for r in rows
             if r['type'] == 'event_msg' and r['payload'].get('type') == 'item_completed']
    commands = [i for i in items if i.get('type') == 'CommandExecution']
    mcp = [i for i in items if i.get('type') == 'McpToolCall']
    discovery = []
    for item in mcp:
        result = item.get('result', {})
        value = result.get('structuredContent')
        if not isinstance(value, dict):
            value = next((json.loads(c['text']) for c in result.get('content', [])
                          if c.get('type') == 'text'), {})
        if value.get('discovery', {}).get('requested_mode') == 'hybrid':
            discovery.append(value['discovery'])
    measured = {'usage': usage, 'duration_ms': completed[0]['duration_ms'],
                'model_responses': len(records), 'local_commands': len(commands),
                'native_mcp_calls': len(mcp)}
    assert measured == expected['measured']
    if expected['condition'] == 'on':
        assert all(i['server'] == 'truthgraph_customer' for i in mcp)
        assert len(discovery) == 2 and all(d['mode'] == 'lexical' for d in discovery)
        assert all(any(p['phase'] == 'semantic_retrieval' and p['outcome'] == 'failed'
                       and p.get('error_code') == 'deadline_exceeded'
                       for p in d['phases']) for d in discovery)
    else:
        assert not mcp
    return measured


def main():
    check_manifest()
    results = json.loads((HERE / 'results.json').read_text())
    runs = {name: read_run(value) for name, value in results['runs'].items()}
    for name, run in runs.items():
        u = run['usage']
        print(f"{name}: {u['total_tokens']:,} total tokens; "
              f"{u['input_tokens'] - u['cached_input_tokens']:,} uncached input; "
              f"{u['output_tokens']:,} output; {run['duration_ms']/1000:.3f}s; "
              f"{run['model_responses']} model responses; {run['local_commands']} local commands")
    on, off = runs['on'], runs['off']
    print(f"Total tokens: {(on['usage']['total_tokens']/off['usage']['total_tokens']-1)*100:+.2f}%")
    print(f"Elapsed: {(on['duration_ms']/off['duration_ms']-1)*100:+.2f}%")
    print('Hybrid requested: 2; full hybrid successes: 0; lexical fallbacks after semantic deadlines: 2')
    print('All checksums, exact prompts, native controls and cumulative/per-response usage checks passed.')


if __name__ == '__main__':
    main()
