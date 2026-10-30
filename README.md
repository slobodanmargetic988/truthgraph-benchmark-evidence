# TruthGraph benchmark evidence

Raw, unedited evidence behind performance claims made about [TruthGraph](https://truthgraph.weeyuga.com). These are selected individual comparisons, not a complete benchmark suite. Each folder is one comparison. It holds the agent session logs exactly as the agent wrote them, a standard-library script that recomputes the numbers, and SHA-256 hashes of every file. Where recordings exist, they are attached to the release with the same name as the folder; automated comparisons explicitly state when there is no recording.

| Folder | What it shows |
| --- | --- |
| [`2026-10-25-weeyugaweb-request-id`](2026-10-25-weeyugaweb-request-id/) | One planning task on a private codebase, Codex with and without TruthGraph: 28.9% fewer total tokens, 51 s faster. One run each; read the caveats. |
| [`2026-10-28-microservices-demo-lexical-fallback`](2026-10-28-microservices-demo-lexical-fallback/) | Selected public-repository case: 18.22% fewer total tokens, 70.924 s faster, **both semantic searches failed and used lexical fallback**. Not hybrid/vector performance proof. |
| [`2026-10-29-eshop-change-impact-hybrid`](2026-10-29-eshop-change-impact-hybrid/) | Selected eShop change-impact case: 10.70% fewer total tokens and 103.738 s faster; **uncached input +13.44%, output +0.64%**, equal targeted quality scores. Two hybrid searches completed; CLI versions differ. No cost-saving or isolated causal claim. |

The logs come straight from the agent. Nothing has been trimmed, redacted or reformatted.
