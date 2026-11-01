#!/usr/bin/env python3
"""Offline whole-session, prompt, usage, cost and manifest verification."""
from pathlib import Path
from decimal import Decimal
import hashlib,html,json,re

HERE=Path(__file__).resolve().parent
sha=lambda data:hashlib.sha256(data).hexdigest()

def extract(raw):
    rows=[json.loads(line) for line in raw.splitlines()]
    meta=next(r['payload'] for r in rows if r['type']=='session_meta')
    contexts=[r['payload'] for r in rows if r['type']=='turn_context']
    usage=[r['payload']['info']['total_token_usage'] for r in rows if r['type']=='event_msg' and r['payload'].get('type')=='token_count'][-1]
    records=[r['payload']['usage'] for r in rows if r['type']=='token_usage_record']
    assert {k:sum(r.get(k,0) for r in records) for k in usage}==usage
    complete=[r['payload'] for r in rows if r['type']=='event_msg' and r['payload'].get('type')=='task_complete']
    assert len(complete)==1
    assert not any(r['type']=='event_msg' and r['payload'].get('type') in ['turn_aborted','task_failed','turn_failed'] for r in rows)
    wrappers=[r['payload']['output'] for r in rows if r['type']=='response_item' and isinstance(r['payload'].get('output'),str) and r['payload']['output'].startswith('<codex_delegation>')]
    assert len(wrappers)==1
    match=re.fullmatch(r'<codex_delegation>\s*<source_thread_id>[^<]+</source_thread_id>\s*<input>(.*)</input>\s*</codex_delegation>\s*',wrappers[0],re.S)
    assert match
    prompt=html.unescape(match[1]);answer=complete[0]['last_agent_message']
    items=[];seen=set()
    for r in rows:
        p=r['payload'];item=p.get('item',{})
        if r['type']=='event_msg' and p.get('type')=='item_completed' and item.get('id') not in seen:
            items.append(item);seen.add(item.get('id'))
    commands=[i for i in items if i.get('type')=='CommandExecution']
    native=[]
    for i in items:
        if i.get('type')!='McpToolCall':continue
        result=i.get('result',{});v=result.get('structuredContent')
        if v is None:v=json.loads(next(c['text'] for c in result['content'] if c.get('type')=='text'))
        native.append({'server':i['server'],'tool':i['tool'],'arguments':i.get('arguments',{}),'status':i['status'],'isError':result.get('isError',False),
          'discovery':v.get('discovery'),'presentation_view':v.get('presentation',{}).get('view'),'coverage':v.get('coverage'),'indexed_revision':v.get('indexed_revision'),
          'structured_payload_bytes':len(json.dumps(v,separators=(',',':'),ensure_ascii=False).encode())})
    return {'thread_id':meta['id'],'cli_version':meta['cli_version'],'provider':meta['model_provider'],
      'models':sorted({c['model'] for c in contexts}),'efforts':sorted({c['effort'] for c in contexts}),
      'usage':usage,'duration_ms':complete[0]['duration_ms'],'model_responses':len(records),'local_commands':len(commands),
      'nonzero_commands':sum(i.get('exit_code') not in (0,None) for i in commands),'native_calls':native,
      'prompt':prompt,'answer':answer,'answer_sha256':sha(answer.encode())}

def metrics(run):
    u=run['usage']
    return {**{k:u[k] for k in ['input_tokens','cached_input_tokens','output_tokens','reasoning_output_tokens','total_tokens']},
      'uncached_input_tokens':u['input_tokens']-u['cached_input_tokens'],'duration_ms':run['duration_ms']}

def costs(run,rates):
    u=run['usage'];million=Decimal(1000000)
    assert u.get('cache_write_input_tokens')==0,'Cache-write attribution would require its own applicable rate.'
    out={'uncached_input':Decimal(u['input_tokens']-u['cached_input_tokens'])*Decimal(rates['uncached_input'])/million,
      'cached_input':Decimal(u['cached_input_tokens'])*Decimal(rates['cached_input'])/million,
      'output':Decimal(u['output_tokens'])*Decimal(rates['output'])/million}
    return {**out,'total':sum(out.values())}

def compare(before,after):
    a,b=metrics(before),metrics(after)
    return {k:{'baseline':a[k],'new':b[k],'difference':b[k]-a[k],'percent_change':(b[k]/a[k]-1)*100} for k in a}

def main():
    for line in (HERE/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split(None,1);assert sha((HERE/name).read_bytes())==digest,name
    result=json.loads((HERE/'results.json').read_text());quality=json.loads((HERE/'quality-review.json').read_text());runs={}
    for name,expected in result['runs'].items():
        raw=(HERE/expected['file']).read_bytes();assert sha(raw)==expected['sha256'] and len(raw)==expected['bytes']
        actual=extract(raw);prompt=actual.pop('prompt');answer=actual.pop('answer')
        assert prompt.encode()==(HERE/expected['prompt_file']).read_bytes() and sha(prompt.encode())==expected['prompt_sha256']
        assert actual==expected['measured'],name
        assert actual['models']==[result['controls']['model']] and actual['efforts']==[result['controls']['effort']] and actual['provider']=='openai'
        assert result['source']['commit'] in prompt
        assert actual['answer_sha256']==quality[name]['answerSHA256']
        assert not actual['native_calls'] if name=='off' else all(not c['isError'] and c['status']=='completed' for c in actual['native_calls'])
        assert {k:str(v) for k,v in costs(actual,result['pricing']['usd_per_million_tokens']).items()}==expected['estimated_cost_usd']
        runs[name]=actual
    for name,c in result['comparisons'].items():
        before,after=runs[c['baseline_run']],runs[c['new_run']]
        assert compare(before,after)==c['metrics'],name
        a=costs(before,result['pricing']['usd_per_million_tokens'])['total'];b=costs(after,result['pricing']['usd_per_million_tokens'])['total']
        assert str(b-a)==c['cost_difference_usd'] and str((b/a-1)*100)==c['cost_percent_change'],name
    for name,q in quality.items():
        if q.get('criteria'):assert sum(c['score'] for c in q['criteria'])==q['score'],name
    for name,r in runs.items():print(name,metrics(r),'estimated USD',result['runs'][name]['estimated_cost_usd']['total'])
    print('Whole native logs, prompts, controls, counter sums, cost categories, comparisons and quality/answer association verified offline.')

if __name__=='__main__':main()
