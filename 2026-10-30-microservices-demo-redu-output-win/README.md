# Microservices-demo on Redu: selected output-token win

The owner selected this single WITH-TruthGraph attempt because **output tokens fell 14.13%, uncached input fell 8.44%, and elapsed time fell 23.67%** against the original WITHOUT baseline. **Cached input rose 18.03%, total input rose 15.00%, and total counted tokens rose 14.71%.** This is an output-token win under the owner's evaluation preference, not a total-token win.

The owner assigns cached input zero weight in that evaluation. That preference is not a claim that cached input is universally free or that provider dollar cost was measured. With applicable rates Pi/Pc/Po per million uncached/cached/output tokens, the cost difference would be `(-9293*Pi + 153728*Pc - 1380*Po) / 1000000`. Applicable billing was not verified. Reasoning is already included in output, and cached input is already included in input; neither is added again.

This is one selected historical comparison, not a complete suite, representative win rate, average, randomized trial or product-wide causal result. Other development attempts exist and are not reclassified as successes. The eShop case remains separately published; OpenTelemetry and Petclinic have their own selected-case folders in this repository. No recording exists for this automated pair.

## Task and exact conditions

The task investigates an optional caller-supplied `checkout_reference` through checkout entry points, rebuilt requests/contracts, synchronous/asynchronous boundaries, side effects, errors, confirmation, telemetry and compatibility tests. It asks for a read-only plan, not an implementation or application test execution. Exact native prompts are in `prompts/`.

Both conditions use public [GoogleCloudPlatform/microservices-demo at 38e7348eb289eb5b87c0c6e8cb19ced0449dc389](https://github.com/GoogleCloudPlatform/microservices-demo/tree/38e7348eb289eb5b87c0c6e8cb19ced0449dc389), **gpt-6.1-sol / ultra / OpenAI**, fresh projectless desktop chats and the same task questions. ON adds the test skill/customer-MCP instructions. Original OFF ran on 29 October with CLI `0.164.0-alpha.11.1`; ON ran on 30 October with CLI `0.165.0-alpha.1.2`.

ON uses `truthgraph-test-context`, customer guidance **2026.10.30.1**, native **truthgraph_test_customer** at `https://truthgraph-test-6f8d2a10.redu.cloud/api/mcp`, runtime `3ecddc8`, and generation `d99d4b50-488e-46af-97e8-c5f5dc821c29`. This is a **Redu test snapshot**, not a production-customer performance measurement. It runs on one 2-vCPU/4-GiB m1.medium VM with query encoding limited to two threads. Authorized benchmark graph/source/embedding fixtures were cloned into isolated test storage with a separate sandbox account and credentials. Generic hybrid qualification occurred before the final service restart, with no task-specific warm query. Hardware, workload, cache state, skill/backend/client versions and earlier task-informed development are uncontrolled differences; this pair cannot isolate TruthGraph's causal contribution. The configured service tier was default but is not independently recorded in native turn context.

## Whole-chat results

| Measure | Original WITHOUT | Redu WITH | Absolute change | Change |
| --- | ---: | ---: | ---: | ---: |
| Input | 962,651 | 1,107,086 | +144,435 | +15.00% |
| Cached input, included above | 852,608 | 1,006,336 | +153,728 | +18.03% |
| Uncached input | 110,043 | 100,750 | -9,293 | -8.44% |
| Output, including reasoning | 9,767 | 8,387 | -1,380 | -14.13% |
| Reasoning, included in output | 4,613 | 2,694 | -1,919 | -41.60% |
| Total counted tokens | 972,418 | 1,115,473 | +143,055 | +14.71% |
| Elapsed seconds | 342.937 | 261.751 | -81.186 | -23.67% |
| Model responses | 12 | 13 | +1 | +8.33% |

Counters are whole-chat native measurements; non-reasoning output includes tool-call text and is not equivalent to final-answer length. Local server inference is outside Codex token counts. The original OFF baseline was preserved, not rerun or replaced.

## Retrieval, answer coverage and remaining gaps

All four ON customer calls completed without structured errors: readiness, one hybrid search, impact and ownership. Readiness matches the exact source pin and reports **4,917 / 4,917 eligible chunks embedded**, complete capture and zero pending/failed/missing-capture/missing-job documents, with 30 excluded files. The search reports hybrid/semantic-ready, but reranking is **not_requested** for this particular query. Three of four discovery hits are generated/copied stubs. A different query's completed reranking is not evidence that this run reranked. Source and excluded/omitted data limitations remain visible in the raw logs.

Symbol impact returned zero modeled dependents although pinned source confirms a frontend caller. Ownership is bounded and does not establish complete change impact. The answer traced substantive implementation boundaries through local source; this is not proof that the graph supplied the complete dependency chain. Full tool catalogues, duplicated readiness representation, clipped combined/generated-code output and overlapping source reads remain visible. Errors or inefficiencies inside the selected run were not removed or replaced with another attempt.

An unblinded targeted static review against the unchanged ten-criterion rubric scores ON **9.5/10**, matching the previously recorded OFF score. The missing half point concerns the concrete contrast between serialized payment-request logging and generic shipping logs, including payment-data exposure caution. Minor precision gaps include not stating explicitly that order-ID allocation precedes preparation and not naming HTTP 422/500 status codes. No material factual error was found in checked claims; no application tests or runtime correctness checks were performed. Review details are separate in `quality-review.json`.

## Deferred opportunities — not implemented by this archive

1. Improve source-backed frontend → RPC → concrete implementation navigation so impact returns the actual caller.
2. Standardize descriptive discovery queries, then exact canonical lookups; report the ranking path actually used.
3. Discover needed tool names/schema and emit one bounded decoded representation, rather than full catalogues/wrappers.
4. Read symbol-bound source ranges once; budget combined output and generated declarations to avoid clipping/recovery reads.
5. Continue ownership only when it resolves missing task facts, retaining honest incompleteness flags.
6. Profile readiness/database/transport before changing the encoder, VM size or rebuilding embeddings.

These are future opportunities, not fixes or extra benchmark attempts made for publication.

## Verify the unchanged evidence

Run `python3 verify.py`. The standard-library verifier performs no network or model calls. It checks every SHA-256 manifest entry, exact decoded native prompts, model/effort/provider/CLI controls, cumulative versus per-response usage, elapsed milliseconds, executed command/MCP counts, retrieval identity/readiness/search metadata and all absolute/percentage deltas.

`logs/01-original-off.jsonl` and `logs/02-with-test-skill-hybrid.jsonl` are the **entire native captures**, byte-identical to the preserved private source snapshots. Nothing was trimmed, reformatted, redacted, repaired or annotated. Analysis and publication notes are separate files. Native local paths, account/session/tool metadata and endpoint identifiers remain. Known credential-pattern scans found no matches, with their limitations recorded in `publication-audit.json`; this is not proof that every possible secret format is absent. No database dump, source-graph dump, account password, provider/API key or test-client configuration was added.
