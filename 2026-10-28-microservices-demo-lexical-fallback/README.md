# microservices-demo: selected faster WITH-skill run, with lexical fallback

**This is not a successful full-hybrid run.** Both requested hybrid searches exceeded the semantic retrieval deadline and fell back to lexical results. The task completed with the customer skill, lexical/indexed evidence and pinned local source. The owner selected this measured improvement for publication with that failure disclosed. A future hybrid-mode run must be a separate comparison; these raw files will not be replaced.

The original OFF baseline and the new ON run answer the same two read-only questions: checkout service flow/failures, and recommendation selection/frontend behavior, at commit `38e7348eb289eb5b87c0c6e8cb19ced0449dc389` of [GoogleCloudPlatform/microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo). Each ran in a fresh projectless Codex desktop chat. The ON prompt explicitly uses `truthgraph-context` version 2026.10.27.2 and native `truthgraph_customer`; OFF uses ordinary source tools. Exact prompts are in `prompts/`.

Both native logs record **gpt-6.1-sol / ultra / openai / CLI 0.164.0-alpha.11.1 / default service tier**. The original OFF ran on 27 October and ON on 28 October. Source pins and questions match; service/skill versions, order and cache/backend conditions were not controlled equally. These are single trials, not an average or a cost estimate.

| Whole-chat measure | Original OFF | WITH skill, lexical fallback | Change |
|---|---:|---:|---:|
| Total native tokens, including cached input |956,117|781,872|18.22% fewer|
| Uncached input tokens |87,010|78,322|9.99% fewer|
| Output tokens, including reasoning |13,555|10,814|20.22% fewer|
| Uncached input plus output |100,565|89,136|11.36% fewer|
| Elapsed |378.653s|307.729s|70.924s /18.73% faster|
| Model responses |12|11|1 fewer|
| Local command events |22|21|1 fewer|
| Native customer MCP calls |0|4|readiness, 2 searches, 1 context|

## What explains the measured difference

The ON run had one fewer model response and local command, and produced 2,741 fewer output tokens. Fewer responses can reduce repeated conversation input. The answer was shorter; OFF covered additional startup/non-default failure details. Both answers accurately covered the core questions in an independent review of 27 cited files and 60 ON / 67 OFF citation instances, with no established material ON quality gain.

Those are observed differences, not an isolated explanation of causality. Lexical discovery supplied candidate subjects, but **no vector-ranked hybrid result succeeded**. The graph bundle returned definitions and no CALLS edge, so local source remained necessary. Stochastic variation, answer length and cache/backend conditions can affect this single comparison. The numbers must not be described as proof of hybrid/vector superiority.

## Retrieval failures and coverage

Index status reported 2,489/2,489 ready memberships with zero pending/failed/missing. Nevertheless both semantic retrieval phases exceeded the 3,000 ms budget (reported 3,018 and 3,001 ms), causing lexical fallback. Fallback metadata also used different exclusion/capture fields; authoritative index readiness is preserved separately in the raw log. There were 30 excluded whole files and one separately recorded oversized PNG omission (4,721,773 bytes). The selected context was bounded/truncated, with omitted evidence. No failing request was replayed, scan started or backend repaired during the attempt. The agent still printed substantial tool descriptions/results; this was not perfect compliance with the skill's output-efficiency guidance.

## Reproduce the measurements

```sh
python3 verify.py
```

The standard-library verifier checks SHA-256, exact native prompt inputs after normal XML entity decoding, model/effort, whole-chat durations and final cumulative tokens against summed per-response usage. It also verifies that both hybrid requests actually fell back. `results.json` holds separate derived metadata. `logs/01-original-off.jsonl` is the unchanged first sealed baseline; `logs/02-with-skill-lexical-fallback.jsonl` is the entire new native log after stable completed reads. Neither file was trimmed, normalized, redacted or annotated. No screen recording exists for this automated pair.

Only this selected comparison is being added now. Other trials are outside this folder, so this is not a complete suite or representative success rate. The separate [original owner-run comparison](../2026-10-25-weeyugaweb-request-id/) has its own logs, agent-summary thread and recordings.
