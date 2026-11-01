# eShop: OFF, previous ON and files-only ON

Rates supplied by the owner: **$2/M uncached input, $0.10/M cached input, $10/M output**. Recorded cache-write tokens are zero. These are API-equivalent estimates; infrastructure is excluded. Cached input is included in input and reasoning in output, so neither subset is counted twice.

| Measure | Original OFF | Previous ON | Files-only ON |
| --- | ---: | ---: | ---: |
| Duration, seconds | 347.718 | 243.980 | 455.455 |
| Input | 2,112,651 | 1,885,246 | 1,353,470 |
| Cached input (subset) | 1,997,056 | 1,754,112 | 1,255,936 |
| Uncached input | 115,595 | 131,134 | 97,534 |
| Output (includes reasoning) | 11,479 | 11,552 | 16,414 |
| Reasoning (subset) | 3,527 | 3,377 | 8,686 |
| Total tokens (supplementary) | 2,124,130 | 1,896,798 | 1,369,884 |
| Static quality /10 | 9.5 | 9.5 | 9.5 |
| Uncached-input cost | $0.231190 | $0.262268 | $0.195068 |
| Cached-input cost | $0.199706 | $0.175411 | $0.125594 |
| Output cost | $0.114790 | $0.115520 | $0.164140 |
| **Total API-equivalent cost** | $0.545686 | $0.553199 | $0.484802 |

## Absolute and percentage changes

| Measure | Previous ON vs OFF | Files-only vs OFF | Files-only vs previous ON |
| --- | ---: | ---: | ---: |
| Duration, seconds | -103.738s (-29.83%) | +107.737s (+30.98%) | +211.475s (+86.68%) |
| Input | -227,405 (-10.76%) | -759,181 (-35.93%) | -531,776 (-28.21%) |
| Cached input (subset) | -242,944 (-12.17%) | -741,120 (-37.11%) | -498,176 (-28.40%) |
| Uncached input | +15,539 (+13.44%) | -18,061 (-15.62%) | -33,600 (-25.62%) |
| Output (includes reasoning) | +73 (+0.64%) | +4,935 (+42.99%) | +4,862 (+42.09%) |
| Reasoning (subset) | -150 (-4.25%) | +5,159 (+146.27%) | +5,309 (+157.21%) |
| Total tokens (supplementary) | -227,332 (-10.70%) | -754,246 (-35.51%) | -526,914 (-27.78%) |
| **Cost** | $+0.007514 (+1.38%) | $-0.060884 (-11.16%) | $-0.068398 (-12.36%) |

## Protocol

One new files-only run, declared before running, with no retries or outcome-based selection; the original OFF and previous ON were not rerun. All runs use gpt-6.1-sol, ultra effort, OpenAI, source pin `913acea66708a59595351174cee9b29f37179d29` and the same frozen task. Files-only backend `2ed2413` and test skill 2026.11.01.1 on the isolated Redu test VM; previous ON: Hosted production service, 29 Oct, backend historical production deployment (exact revision not recorded). Client versions: off 0.164.0-alpha.11.1, previous_on 0.165.0-alpha.1.2, files_only_on 0.166.0-alpha.5.1. Cache, load and preparation are uncontrolled. This is not a randomized or isolated causal comparison. Files-only mode is not yet deployed to production.

## Observations

- **Regression: duration +30.98% and output +42.99% versus OFF.** Reasoning output rose 5,309 tokens, more than the entire output increase; non-reasoning output fell 447. Final answers are similar length (723 versus 684 words).

- The unchanged JSONL shows overlapping EventBusRabbitMQ and event-handler reads across batches, an impact root on the CreateOrderCommandHandler class before its Handle method, an API lookup that returned nearby subjects, and one guessed serializer-context path. All native calls completed without structured errors; initial hybrid search phases completed (lexical/readiness/embedding/vector/ranking/reranking 937/1039/843/1906/1015/1166 ms).

- Cost still falls 11.16% versus OFF because input falls 35.93% (uncached 15.62%, cached 37.11%). The separate contributions of extra reasoning and repeated source checking to the extra time are unmeasured.

- Fixture: 9,249 embedded chunks reused from the authorized restored snapshot; source-omission inventory unknown. The previous ON ran on the hosted production service with a different client and backend.



Quality reviews are unblinded, targeted and source-based; they are not runtime proof. Full criteria are in quality-review.json.
