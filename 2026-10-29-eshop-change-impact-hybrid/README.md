# eShop change impact: faster, fewer total tokens, higher uncached input

This selected WITH-TruthGraph attempt finished **103.738 seconds / 29.83% faster** and used **10.70% fewer total counted tokens** than its original OFF baseline. **Uncached input increased 13.44% and output increased 0.64%**. The total-token reduction mostly concerns cached input; this is not a dollar-cost saving claim. Targeted static-source quality scores match at 9.5/10.

The owner selected this pair because its elapsed time and total tokens improved. Other current cases did not all reduce total tokens and are not included here. This folder is one selected observation, not a complete suite, representative success rate, average or randomized repeated trial.

## Task and conditions

Both chats investigate adding an optional nullable `checkout_reference` across checkout request construction, commands, domain persistence, lifecycle events, read/status responses and notifications, while preserving identity, duplicate handling and compatibility. The task asks for a change-impact plan, source citations, tests to add and explicit evidence gaps; it does not implement a change or execute tests. Exact prompts are in `prompts/`.

Both use commit `913acea66708a59595351174cee9b29f37179d29` of [dotnet/eShop](https://github.com/dotnet/eShop/tree/913acea66708a59595351174cee9b29f37179d29), **gpt-6.1-sol / ultra / OpenAI**, and fresh projectless desktop chats. The same source pin and task are preserved; ON includes the TruthGraph usage instruction. ON uses installed skill **2026.10.29.3** and native customer MCP **`truthgraph_customer`**. Its backend source is `7f26eea5e8f54586a4531b3df2df52ef5b4d34f6` and customer generation `afa23ce0-bf9a-4071-bc58-7c561324de9e`.

**The desktop CLI differs:** original OFF records `0.164.0-alpha.11.1`; ON records `0.165.0-alpha.1.2`. Both ran on 29 October 2026, hours apart. Launch configuration used the default service tier, but the native turn context does not explicitly record a tier. Backend/skill versions, earlier task-informed development, cache state and live load were not equal controlled conditions. This pair cannot isolate TruthGraph's causal contribution.

| Whole-chat measure | Original OFF | WITH skill | Change |
|---|---:|---:|---:|
| Input tokens | 2,112,651 | 1,885,246 | -10.76% |
| Cached input, included above | 1,997,056 | 1,754,112 | -12.17% |
| Uncached input | 115,595 | 131,134 | +13.44% |
| Output, including reasoning | 11,479 | 11,552 | +0.64% |
| Reasoning, included in output | 3,527 | 3,377 | -4.25% |
| Total tokens | 2,124,130 | 1,896,798 | -10.70% |
| Elapsed seconds | 347.718 | 243.980 | -29.83% |
| Model responses | 22 | 18 | 4 fewer |
| Local command events | 36 | 33 | 3 fewer |
| Nonzero local command exits | 0 | 2 | retained in full logs |
| Native MCP calls | 0 | 6 | status, 2 searches, 3 contexts |

Cached input is already included in input; reasoning is already included in output. The verifier checks final cumulative usage against summed per-response usage. Local reranker compute is outside Codex token counters. No recording exists for this automated pair.

## What the raw workflow shows

ON has 17 orchestration executions and one final model response; OFF has 21 and one final response. ON batches more underlying actions into fewer model cycles. Its average prompt is larger, and its final input context is 159,466 tokens versus OFF's 144,425. The smaller sum of input tokens therefore does not mean smaller prompts or less fresh information: cached input falls by 242,944 while uncached input rises by 15,539.

Two hybrid searches aid navigation. Both chats still inspect substantial pinned source for actual forwarding, persistence, event and notification paths. The graph contexts confirm no impacted entities for the two requested symbols; ownership returns one definition edge. This is not proof that the graph supplied the complete dependency chain. ON also prints full tool metadata, and two local command failures remain visible. No failing action was replaced with another benchmark attempt.

These are workflow observations and arithmetic, not an isolated causal explanation. Different batching, stopping decisions, client versions and uncontrolled conditions can affect one comparison.

## Retrieval and answer limits

Both search responses are intact structured native results reporting hybrid mode, semantic ready, six phases OK and completed reranking, with bounded candidate truncation. No search fallback or structured MCP error is reported. Index status matches the exact pin and reports configured/capture-complete/complete, eligible equals embedded, and zero pending/failed/missing-capture/missing-job documents. Ownership is bounded and reports `complete_change_impact=false`; local source checking remains necessary.

The post-timed review is targeted, unblinded and static, using the unchanged frozen rubric and 34 matched source-reference hashes. Both original OFF and new ON score 9.5/10; no material factual error was found in checked ON claims. Both lose half-credit for missing concrete existing command/idempotency test citations. No material quality improvement or runtime correctness proof is established. `quality-review.json` contains the selected pair's derived review separately from raw logs.

## Verify the evidence

```sh
python3 verify.py
```

This standard-library verifier makes no network or model calls. It checks all SHA-256 hashes, exact native prompts after normal XML entity decoding, model/effort/provider and per-run CLI versions, whole-chat duration, response/command/MCP counts, usage totals, search phase outcomes and published differences.

`logs/01-original-off.jsonl` is the unchanged original sealed baseline. `logs/02-with-skill-hybrid.jsonl` is the entire completed native ON capture. Both are byte-identical to their private source snapshots; nothing was trimmed, normalized, redacted, repaired or annotated. Analysis and publication notes are separate files. Native local paths, platform/account/session identifiers, generic tool metadata and historical command-approval prefixes remain in those complete logs. Known credential-pattern scans found zero matches; the scope review found no concrete secret or private third-party source/message blocker. Pattern screening is not a proof that every possible secret format is absent.
