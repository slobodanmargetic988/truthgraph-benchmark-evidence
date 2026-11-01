# OpenTelemetry: OFF, previous ON and files-only ON

Rates supplied by the owner: **$2/M uncached input, $0.10/M cached input, $10/M output**. Recorded cache-write tokens are zero. These are API-equivalent estimates; infrastructure is excluded. Cached input is included in input and reasoning in output, so neither subset is counted twice.

| Measure | Original OFF | Previous ON | Files-only ON |
| --- | ---: | ---: | ---: |
| Duration, seconds | 374.683 | 269.443 | 309.377 |
| Input | 1,358,312 | 1,914,876 | 1,275,292 |
| Cached input (subset) | 1,234,944 | 1,734,272 | 1,157,888 |
| Uncached input | 123,368 | 180,604 | 117,404 |
| Output (includes reasoning) | 12,176 | 10,620 | 11,005 |
| Reasoning (subset) | 4,670 | 3,471 | 3,709 |
| Total tokens (supplementary) | 1,370,488 | 1,925,496 | 1,286,297 |
| Static quality /10 |8.5|9.5|9.0|
| Uncached-input cost | $0.246736 | $0.361208 | $0.234808 |
| Cached-input cost | $0.123494 | $0.173427 | $0.115789 |
| Output cost | $0.121760 | $0.106200 | $0.110050 |
| **Total API-equivalent cost** | $0.491990 | $0.640835 | $0.460647 |

## Absolute and percentage changes

| Measure | Previous ON vs OFF | Files-only vs OFF | Files-only vs previous ON |
| --- | ---: | ---: | ---: |
| Duration, seconds | -105.240s (-28.09%) | -65.306s (-17.43%) | +39.934s (+14.82%) |
| Input | +556,564 (+40.97%) | -83,020 (-6.11%) | -639,584 (-33.40%) |
| Cached input (subset) | +499,328 (+40.43%) | -77,056 (-6.24%) | -576,384 (-33.23%) |
| Uncached input | +57,236 (+46.39%) | -5,964 (-4.83%) | -63,200 (-34.99%) |
| Output (includes reasoning) | -1,556 (-12.78%) | -1,171 (-9.62%) | +385 (+3.63%) |
| Reasoning (subset) | -1,199 (-25.67%) | -961 (-20.58%) | +238 (+6.86%) |
| Total tokens (supplementary) | +555,008 (+40.50%) | -84,191 (-6.14%) | -639,199 (-33.20%) |
| **Cost** | $+0.148845 (+30.25%) | $-0.031344 (-6.37%) | $-0.180188 (-28.12%) |

Previous ON reduced output, **increased input**, and cost 30.25% more than OFF at these prices. Files-only is 6.37% cheaper than OFF and 28.12% cheaper than previous ON. Against previous ON it saves $0.1840384 in input charges while adding $0.00385 in output charges, net $0.1801884 saved per run. It is 14.82% slower than previous ON, and 17.43% faster than OFF.

## Protocol and quality

Exactly one new files-only ON; one original OFF and one selected previous ON, with no baseline reruns. The previous ON was selected from four earlier Redu chats (one interrupted/resumed); other attempts remain diagnostic, not successes. All use gpt-6.1-sol/ultra/OpenAI, source pin `d306972ec1d91c7d01ec788e7e98e90535570a4c` and identical task questions. ON runtimes are 5443185→2ed2413, test-skill wrappers 2026.10.30.2→2026.11.01.1. The two ON CLI versions match; OFF uses its older recorded client. Same minimal Redu snapshot/hardware, but cache/load, preparation, selected queries and ranking outcomes differ. This is not a randomized or isolated causal comparison.

Previous ON used lexical fallback after an embedding timeout. Files-only completed hybrid retrieval and reranking. Three query calls used files-only and none requested full evidence, alongside one readiness call. Structured native payloads totaled 14,866 versus 77,968bytes, a reduction of 80.93%; that is not an isolated model-token attribution.

Current unblinded targeted static quality review is 9/10 versus previous 9.5/10 and original OFF 8.5/10. No material incorrect claim was found in sampled checks; all39 frozen evidence-file hashes matched. Files-only omits the Weaver telemetry definition checklist; explicit currencyCode query-parameter handling remains a shared gap. Evidence and review limitations are retained in quality-review.json.

## Raw-log findings and suggestions

Raw logs show 34 versus 91 local command records (batching differs), three nonzero commands in both sessions, no structured MCP errors and no exact duplicate whole shell commands. Some source ranges overlapped; files-only still read most checkout implementation code. Broad ownership discovery chose CHANGELOG.md and required independent source verification. Output rose 385 tokens (238 reasoning, 147 other output) and both ON sessions used 18 model responses. One run cannot isolate the source of the extra 39.934 seconds.

1. Use a returned exact canonical ownership subject rather than broad prose discovery.
2. Reuse focused ranges/discovered paths and avoid oversized batches or guessed build paths.
3. Include telemetry-schema definitions in navigation coverage.
4. Profile cold retrieval and evaluate speed/output variance only in a separately authorized experiment; no extra run was made for publication.
