# Spring Petclinic: selected output-token win on Redu

One selected historical comparison: **output -7.33%**, uncached input -9.12%, time -36.82%. The owner assigns cached input zero weight in their evaluation; that preference is not a universal free-cache statement or a measured dollar-cost claim. Total tokens are supplementary, and all adverse category changes remain below.

Both investigations use the exact source pin `e8b747ab522721076cacb5cf688eb8a54ba8c5c9` in [spring-petclinic-microservices](https://github.com/spring-petclinic/spring-petclinic-microservices/tree/e8b747ab522721076cacb5cf688eb8a54ba8c5c9), gpt-6.1-sol/ultra/OpenAI and identical task questions. Exact prompts are retained. ON uses only the isolated native `truthgraph_test_customer` at `https://truthgraph-test-6f8d2a10.redu.cloud/api/mcp`, runtime `3ecddc8e95ff804dc5a8fad53d9516c65dd9d91c`, snapshot generation `d99d4b50-488e-46af-97e8-c5f5dc821c29`. It has separate sandbox credentials and runs on one 2-vCPU/4-GiB Redu VM. Skill: Initial test wrapper; customer guidance2026.10.30.1. Readiness was checked before timing. This is not a production-customer performance measurement; client, skill/backend, cache/load, identity and hardware differences are uncontrolled. CLI versions are recorded per run in results.json.

| Measure | Original WITHOUT | Redu WITH | Absolute change | Change |
| --- | ---: | ---: | ---: | ---: |
| Input | 986,953 | 988,494 | +1,541 | +0.16% |
| Cached input, included above | 881,792 | 892,928 | +11,136 | +1.26% |
| Uncached input | 105,161 | 95,566 | -9,595 | -9.12% |
| Output, including reasoning | 10,258 | 9,506 | -752 | -7.33% |
| Reasoning, included in output | 3,874 | 2,645 | -1,229 | -31.72% |
| Total counted tokens | 997,211 | 998,000 | +789 | +0.08% |
| Elapsed seconds | 317.603 | 200.659 | -116.944 | -36.82% |

Cached input is a subset of input; reasoning is a subset of output. Non-reasoning output includes tool text and is not final-answer length. The original baseline was preserved, not rerun. This selected pair is not a representative success rate, randomized trial or product-wide causal finding. Other development attempts remain diagnostic, not successes.

## Retrieval and reviewed coverage

All 7 native test-customer calls completed without structured errors. Exact search mode/fallback/reranking phases, impact counts and ownership continuation limits are in results.json and the unchanged raw logs. The index matched the pinned source and reported complete eligible embeddings; that does not establish complete graph extraction. Local source verification remained necessary. Do not infer complete callers or runtime transport from partial ownership/impact.

New unblinded targeted static source review: **9.0/10**, original frozen OFF review **9/10**. No material incorrect claim was found in the sampled checks. Frozen source evidence hashes matched. Remaining rubric gaps: Browser helper and ChatBox correctly identified; exact OwnerDetailsPage.setup/useRequest caller remains implicit.; POST503 retry, fallback response and differences covered; configured10-second TimeLimiter omitted. This is not runtime correctness, exhaustive citation verification or executed propagation testing. Full review is separate in quality-review.json.

## Verify raw evidence

Run `python3 verify.py` offline. It checks every manifest entry, entire native log hashes, exact decoded prompts, model/effort/provider/client controls, cumulative versus per-response counters, completed task duration, command/MCP counts and actual retrieval metadata, quality-score arithmetic, and all absolute/percentage changes. It performs no network, model calls or application tests.

Both logs are the **whole unchanged native JSONL**. No trimming, reformatting, redaction, repair or annotation occurred. Source paths and native account/session/tool metadata remain. Known credential-pattern scans and their limits are in publication-audit.json. No database/source-graph dump, secret key, account password or test-client configuration is included. No recording exists for this automated comparison.
