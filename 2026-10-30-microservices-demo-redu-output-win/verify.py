#!/usr/bin/env python3
"""Offline checksum/control/usage verification. No network, credentials or model calls."""
from pathlib import Path
import hashlib
import html
import json
import re

HERE = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify_run(expected):
    data = (HERE / expected['file']).read_bytes()
    assert sha(data) == expected['sha256'] and len(data) == expected['bytes']
    rows = [json.loads(line) for line in data.splitlines()]
    meta = next(r['payload'] for r in rows if r['type'] == 'session_meta')
    assert meta['id'] == expected['thread_id']
    assert meta['cli_version'] == expected['cli_version']
    assert meta['model_provider'] == 'openai'
    turns = [r['payload'] for r in rows if r['type'] == 'turn_context']
    assert turns and {r['model'] for r in turns} == {'gpt-6.1-sol'}
    assert {r['effort'] for r in turns} == {'ultra'}
    records = [r['payload']['usage'] for r in rows if r['type'] == 'token_usage_record']
    cumulative = [r['payload']['info']['total_token_usage'] for r in rows
                  if r['type'] == 'event_msg' and r['payload'].get('type') == 'token_count'][-1]
    assert {k: sum(r.get(k, 0) for r in records) for k in cumulative} == cumulative
    completed = [r['payload'] for r in rows if r['type'] == 'event_msg'
                 and r['payload'].get('type') == 'task_complete']
    assert len(completed) == 1
    wrappers = [r['payload']['output'] for r in rows if r['type'] == 'response_item'
                and isinstance(r['payload'].get('output'), str)
                and r['payload']['output'].startswith('<codex_delegation>')]
    assert len(wrappers) == 1
    match = re.fullmatch(r'<codex_delegation>\s*<source_thread_id>[^<]+</source_thread_id>\s*<input>(.*)</input>\s*</codex_delegation>\s*', wrappers[0], re.S)
    assert match
    prompt = html.unescape(match[1]).encode()
    assert sha(prompt) == expected['prompt_sha256']
    assert prompt == (HERE / expected['prompt_file']).read_bytes()
    items, seen = [], set()
    for row in rows:
        p = row['payload']
        if row['type'] == 'event_msg' and p.get('type') == 'item_completed':
            item = p.get('item', {})
            if item.get('id') not in seen:
                seen.add(item.get('id'))
                items.append(item)
    commands = [i for i in items if i.get('type') == 'CommandExecution']
    mcp = [i for i in items if i.get('type') == 'McpToolCall']
    measured = {'usage': cumulative, 'duration_ms': completed[0]['duration_ms'],
                'model_responses': len(records), 'local_commands': len(commands),
                'native_mcp_calls': len(mcp),
                'nonzero_local_command_exits': sum(i.get('exit_code') not in (None, 0) for i in commands)}
    assert measured == expected['measured']
    searches = []
    if expected['condition'] == 'on':
        assert len(mcp) == 4 and all(i['server'] == 'truthgraph_test_customer' for i in mcp)
        assert all(i['status'] == 'completed' and not i.get('result', {}).get('isError') for i in mcp)
        def decoded(item):
            result = item['result']
            if isinstance(result.get('structuredContent'), dict):
                return result['structuredContent']
            return json.loads(next(c['text'] for c in result['content'] if c.get('type') == 'text'))
        values = [decoded(i) for i in mcp]
        assert any(v.get('context_capabilities', {}).get('version') == '2026.10.30.1' for v in values)
        status = next(decoded(i) for i in mcp if i['tool'] == 'truthgraph_index_status')
        assert status['indexed_revision'] == '38e7348eb289eb5b87c0c6e8cb19ced0449dc389'
        assert status['configured'] and status['capture_complete'] and status['complete']
        assert status['eligible_documents'] == status['embedded_documents']
        assert all(status[k] == 0 for k in ['pending_documents', 'failed_documents', 'missing_capture_files', 'missing_job_documents'])
        searches = [decoded(i)['discovery'] for i in mcp if i['tool'] == 'truthgraph_search']
        assert len(searches) == 1
        for discovery in searches:
            assert discovery['requested_mode'] == discovery['mode'] == 'hybrid'
            assert discovery['semantic_state'] == 'ready'
            assert discovery['reranking_status'] == 'not_requested'
        impacts = [v for v in values if v.get('workflow') == 'get_change_impact']
        assert len(impacts) == 1 and all(not v['impact']['impacted_entities'] for v in impacts)
    else:
        assert not mcp
    return measured, searches


def main():
    for line in (HERE / 'SHA256SUMS').read_text().splitlines():
        expected, name = line.split(None, 1)
        assert sha((HERE / name).read_bytes()) == expected, name
    results = json.loads((HERE / 'results.json').read_bytes())
    runs = {name: verify_run(value)[0] for name, value in results['runs'].items()}
    for metric, expected in results['comparison'].items():
        def value(run):
            if metric == 'elapsed_ms':
                return run['duration_ms']
            if metric == 'uncached_input_tokens':
                return run['usage']['input_tokens'] - run['usage']['cached_input_tokens']
            return run['usage'][metric]
        on, off = value(runs['on']), value(runs['off'])
        assert on == expected['on'] and off == expected['off']
        assert on - off == expected['difference']
        assert abs((on / off - 1) * 100 - expected['percent_change']) < 1e-9
    q = json.loads((HERE / 'quality-review.json').read_bytes())
    assert sum(x['score'] for x in q['criteria']) == q['score'] == 9.5
    assert q['original_OFF']['score'] == 9.5
    on_rows = [json.loads(line) for line in (HERE / results['runs']['on']['file']).read_bytes().splitlines()]
    answer = next(r['payload']['last_agent_message'] for r in on_rows if r['type'] == 'event_msg' and r['payload'].get('type') == 'task_complete')
    assert sha(answer.encode()) == q['answerSHA256'], 'Review/answer association'
    for name, run in runs.items():
        u = run['usage']
        print(f"{name}: {run['duration_ms']/1000:.3f}s; {run['model_responses']} responses; "
              f"{u['input_tokens']:,} input ({u['cached_input_tokens']:,} cached); "
              f"{u['input_tokens']-u['cached_input_tokens']:,} uncached; "
              f"{u['output_tokens']:,} output; {u['total_tokens']:,} total")
    print('One hybrid search reports semantic ready and reranking not_requested; graph impact has zero modeled dependents.')
    print('Selected output-token win: output/uncached input/time fall, cached input/total tokens rise. CLI and environment differ.')
    print('Owner cached-input evaluation weight is zero; that is not a universal-free-cache or verified-dollar-saving claim.')
    print('All exact hashes/prompts, native controls, usage sums and published differences verified offline.')


if __name__ == '__main__':
    main()
