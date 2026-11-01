# Online Boutique (microservices-demo): OFF, previous ON and files-only ON

Rates supplied by the owner: **$2/M uncached input, $0.10/M cached input, $10/M output**. Recorded cache-write tokens are zero. These are API-equivalent estimates; infrastructure is excluded. Cached input is included in input and reasoning in output, so neither subset is counted twice.

| Measure | Original OFF | Previous ON | Files-only ON |
| --- | ---: | ---: | ---: |
| Duration, seconds | 342.937 | 261.751 | 237.721 |
| Input | 962,651 | 1,107,086 | 674,555 |
| Cached input (subset) | 852,608 | 1,006,336 | 611,840 |
| Uncached input | 110,043 | 100,750 | 62,715 |
| Output (includes reasoning) | 9,767 | 8,387 | 7,818 |
| Reasoning (subset) | 4,613 | 2,694 | 3,102 |
| Total tokens (supplementary) | 972,418 | 1,115,473 | 682,373 |
| Static quality /10 | 9.5 | 9.5 | 9.5 |
| Uncached-input cost | $0.220086 | $0.201500 | $0.125430 |
| Cached-input cost | $0.085261 | $0.100634 | $0.061184 |
| Output cost | $0.097670 | $0.083870 | $0.078180 |
| **Total API-equivalent cost** | $0.403017 | $0.386004 | $0.264794 |

## Absolute and percentage changes

| Measure | Previous ON vs OFF | Files-only vs OFF | Files-only vs previous ON |
| --- | ---: | ---: | ---: |
| Duration, seconds | -81.186s (-23.67%) | -105.216s (-30.68%) | -24.030s (-9.18%) |
| Input | +144,435 (+15.00%) | -288,096 (-29.93%) | -432,531 (-39.07%) |
| Cached input (subset) | +153,728 (+18.03%) | -240,768 (-28.24%) | -394,496 (-39.20%) |
| Uncached input | -9,293 (-8.44%) | -47,328 (-43.01%) | -38,035 (-37.75%) |
| Output (includes reasoning) | -1,380 (-14.13%) | -1,949 (-19.95%) | -569 (-6.78%) |
| Reasoning (subset) | -1,919 (-41.60%) | -1,511 (-32.76%) | +408 (+15.14%) |
| Total tokens (supplementary) | +143,055 (+14.71%) | -290,045 (-29.83%) | -433,100 (-38.83%) |
| **Cost** | $-0.017013 (-4.22%) | $-0.138223 (-34.30%) | $-0.121210 (-31.40%) |

## Protocol

One new files-only run, declared before running, with no retries or outcome-based selection; the original OFF and previous ON were not rerun. All runs use gpt-6.1-sol, ultra effort, OpenAI, source pin `38e7348eb289eb5b87c0c6e8cb19ced0449dc389` and the same frozen task. Files-only backend `2ed2413` and test skill 2026.11.01.1 on the isolated Redu test VM; previous ON: Redu test VM, evidence-bearing responses (selected run, 30 Oct), backend 3ecddc8. Client versions: off 0.164.0-alpha.11.1, previous_on 0.165.0-alpha.1.2, files_only_on 0.166.0-alpha.5.1. Cache, load and preparation are uncontrolled. This is not a randomized or isolated causal comparison. Files-only mode is not yet deployed to production.

## Observations

- 4 native calls: 3 files-only requests and 0 full-evidence requests. Structured native payload 15,052 bytes versus 59,238 for the previous ON (not wire bytes or token attribution).

- Quality gap: proposes downstream metadata and logging but omits the serialized payment-request versus shipping-log contrast and the payment-data exposure caution.



Quality reviews are unblinded, targeted and source-based; they are not runtime proof. Full criteria are in quality-review.json.
