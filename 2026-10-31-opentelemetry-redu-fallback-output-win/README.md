# OpenTelemetry demo (lexical fallback): selected output-token win on Redu

**Fallback-assisted result:** the requested hybrid search exceeded its query-embedding budget and returned lexical candidates. This is not evidence of a successful hybrid/vector run. The timeout, fallback and other retrieval limitations remain in the unchanged native log and results.json.

One selected historical comparison: **output -12.78%**, uncached input +46.39%, time -28.09%. The owner assigns cached input zero weight in their evaluation; that preference is not a universal free-cache statement or a measured dollar-cost claim. Total tokens are supplementary, and all adverse category changes remain below.

Both investigations use the exact source pin `d306972ec1d91c7d01ec788e7e98e90535570a4c` in [opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo/tree/d306972ec1d91c7d01ec788e7e98e90535570a4c), gpt-6.1-sol/ultra/OpenAI and identical task questions. Exact prompts are retained. ON uses only the isolated native `truthgraph_test_customer` at `https://truthgraph-test-6f8d2a10.redu.cloud/api/mcp`, runtime `544318527289b532226a0ff9f1641107b34b2b77`, snapshot generation `d99d4b50-488e-46af-97e8-c5f5dc821c29`. It has separate sandbox credentials and runs on one 2-vCPU/4-GiB Redu VM. Skill: 2026.10.30.2. Task-relevant readiness and ownership query before timed run; direct read-only stored-evidence integrity check. Earlier versioned ownership qualification also warmed graph data; baseline preparation/cache/load uncontrolled. This is not a production-customer performance measurement; client, skill/backend, cache/load, identity and hardware differences are uncontrolled. CLI versions are recorded per run in results.json.

| Measure | Original WITHOUT | Redu WITH | Absolute change | Change |
| --- | ---: | ---: | ---: | ---: |
| Input | 1,358,312 | 1,914,876 | +556,564 | +40.97% |
| Cached input, included above | 1,234,944 | 1,734,272 | +499,328 | +40.43% |
| Uncached input | 123,368 | 180,604 | +57,236 | +46.39% |
| Output, including reasoning | 12,176 | 10,620 | -1,556 | -12.78% |
| Reasoning, included in output | 4,670 | 3,471 | -1,199 | -25.67% |
| Total counted tokens | 1,370,488 | 1,925,496 | +555,008 | +40.50% |
| Elapsed seconds | 374.683 | 269.443 | -105.240 | -28.09% |

Cached input is a subset of input; reasoning is a subset of output. Non-reasoning output includes tool text and is not final-answer length. The original baseline was preserved, not rerun. This selected pair is not a representative success rate, randomized trial or product-wide causal finding. Other development attempts remain diagnostic, not successes.

## Retrieval and reviewed coverage

All 5 native test-customer calls completed without structured errors. Exact search mode/fallback/reranking phases, impact counts and ownership continuation limits are in results.json and the unchanged raw logs. The index matched the pinned source and reported complete eligible embeddings; that does not establish complete graph extraction. Local source verification remained necessary. Do not infer complete callers or runtime transport from partial ownership/impact.

New unblinded targeted static source review: **9.5/10**, original frozen OFF review **8.5/10**. No material incorrect claim was found in the sampled checks. Frozen source evidence hashes matched. Remaining rubric gaps: Actual browser/native surfaces and shared tool callers covered; explicit currencyCode removal into query parameters omitted. This is not runtime correctness, exhaustive citation verification or executed propagation testing. Full review is separate in quality-review.json.

## Verify raw evidence

Run `python3 verify.py` offline. It checks every manifest entry, entire native log hashes, exact decoded prompts, model/effort/provider/client controls, cumulative versus per-response counters, completed task duration, command/MCP counts and actual retrieval metadata, quality-score arithmetic, and all absolute/percentage changes. It performs no network, model calls or application tests.

Both logs are the **whole unchanged native JSONL**. No trimming, reformatting, redaction, repair or annotation occurred. Source paths and native account/session/tool metadata remain. Known credential-pattern scans and their limits are in publication-audit.json. No database/source-graph dump, secret key, account password or test-client configuration is included. No recording exists for this automated comparison.

This Redu development cycle contained 4 ON chats, including an interrupted/resumed attempt. Only this selected version is included here; the earlier non-winning logs remain unchanged privately. Older development attempts also exist. This is not a complete suite or representative success-rate claim.
