# Spring PetClinic microservices: OFF, previous ON and files-only ON

Rates supplied by the owner: **$2/M uncached input, $0.10/M cached input, $10/M output**. Recorded cache-write tokens are zero. These are API-equivalent estimates; infrastructure is excluded. Cached input is included in input and reasoning in output, so neither subset is counted twice.

| Measure | Original OFF | Previous ON | Files-only ON |
| --- | ---: | ---: | ---: |
| Duration, seconds | 317.603 | 200.659 | 152.365 |
| Input | 986,953 | 988,494 | 553,675 |
| Cached input (subset) | 881,792 | 892,928 | 495,616 |
| Uncached input | 105,161 | 95,566 | 58,059 |
| Output (includes reasoning) | 10,258 | 9,506 | 7,769 |
| Reasoning (subset) | 3,874 | 2,645 | 2,377 |
| Total tokens (supplementary) | 997,211 | 998,000 | 561,444 |
| Static quality /10 | 9.0 | 9.0 | 9.0 |
| Uncached-input cost | $0.210322 | $0.191132 | $0.116118 |
| Cached-input cost | $0.088179 | $0.089293 | $0.049562 |
| Output cost | $0.102580 | $0.095060 | $0.077690 |
| **Total API-equivalent cost** | $0.401081 | $0.375485 | $0.243370 |

## Absolute and percentage changes

| Measure | Previous ON vs OFF | Files-only vs OFF | Files-only vs previous ON |
| --- | ---: | ---: | ---: |
| Duration, seconds | -116.944s (-36.82%) | -165.238s (-52.03%) | -48.294s (-24.07%) |
| Input | +1,541 (+0.16%) | -433,278 (-43.90%) | -434,819 (-43.99%) |
| Cached input (subset) | +11,136 (+1.26%) | -386,176 (-43.79%) | -397,312 (-44.50%) |
| Uncached input | -9,595 (-9.12%) | -47,102 (-44.79%) | -37,507 (-39.25%) |
| Output (includes reasoning) | -752 (-7.33%) | -2,489 (-24.26%) | -1,737 (-18.27%) |
| Reasoning (subset) | -1,229 (-31.72%) | -1,497 (-38.64%) | -268 (-10.13%) |
| Total tokens (supplementary) | +789 (+0.08%) | -435,767 (-43.70%) | -436,556 (-43.74%) |
| **Cost** | $-0.025596 (-6.38%) | $-0.157712 (-39.32%) | $-0.132115 (-35.19%) |

## Protocol

One new files-only run, declared before running, with no retries or outcome-based selection; the original OFF and previous ON were not rerun. All runs use gpt-6.1-sol, ultra effort, OpenAI, source pin `e8b747ab522721076cacb5cf688eb8a54ba8c5c9` and the same frozen task. Files-only backend `2ed2413` and test skill 2026.11.01.1 on the isolated Redu test VM; previous ON: Redu test VM, evidence-bearing responses (selected run, 30 Oct), backend 3ecddc8e95ff804dc5a8fad53d9516c65dd9d91c. Client versions: off 0.164.0-alpha.11.1, previous_on 0.166.0-alpha.5.1, files_only_on 0.166.0-alpha.5.1. Cache, load and preparation are uncontrolled. This is not a randomized or isolated causal comparison. Files-only mode is not yet deployed to production.

## Observations

- 4 native calls (previous ON: 7): 3 files-only requests and 0 full-evidence requests. Structured native payload 14,867 bytes versus 128,154 (not wire bytes or token attribution).

- Quality gaps shared with the OFF grade: the exact OwnerDetailsPage caller remains implicit, and the configured 10-second TimeLimiter is omitted.



Quality reviews are unblinded, targeted and source-based; they are not runtime proof. Full criteria are in quality-review.json.
