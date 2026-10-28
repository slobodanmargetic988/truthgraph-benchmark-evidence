# One task, with and without TruthGraph (25 October 2026)

Raw evidence for the "28.9% fewer tokens, 51 seconds faster" result. Everything here is unedited: the Codex session logs exactly as Codex wrote them, and the screen recordings of all three threads as they ran.

## What was run

Two Codex desktop threads ran the same read-only investigation of the founder's WeeyugaWeb repository at commit `6db98fe250a0663fc1f3ca970199ae6ac63cd8bc`. The task was to plan an optional `request_id` for the cluster chat API: find the entry points, the models to change, the callers, the forwarding layers that could drop it, logging, and the tests. Both threads used the same model and effort: `gpt-6.1-sol`, effort `ultra`.

| Thread | Mode | Started (UTC) | Recording |
| --- | --- | --- | --- |
| `01a17372-0953-7aa1-8fb9-ca58efd98f74` | With TruthGraph: the prompt asks for the `truthgraph-context` skill and the TruthGraph MCP | 14:23:36 | [Full ON recording](https://github.com/slobodanmargetic988/truthgraph-benchmark-evidence/releases/download/2026-10-25-weeyugaweb-request-id/1-with-truthgraph_screen-recording-2026-10-25-15.23.33.mov) |
| `01a17378-fbf8-7da3-899f-12448bc85709` | Without TruthGraph: the prompt allows file reads, text search and Git only | 14:32:14 | [Full OFF recording](https://github.com/slobodanmargetic988/truthgraph-benchmark-evidence/releases/download/2026-10-25-weeyugaweb-request-id/2-without-truthgraph_screen-recording-2026-10-25-15.32.12.mov) |
| `01a17381-9dde-7f50-a8ed-d237770f3703` | A third Codex thread asked to measure the two runs, so the totals are the agent's own reading of the logs | 14:42:02 | [Summary recording](https://github.com/slobodanmargetic988/truthgraph-benchmark-evidence/releases/download/2026-10-25-weeyugaweb-request-id/3-codex-summary_screen-recording-2026-10-25-15.42.04.mov) |
| `01a17383-a155-7df2-8ec2-101f823bb417` | A sub-agent the third thread started to double-check one run | 14:42:48 | (inside recording 3) |

## Results

From `python3 verify.py`, which recomputes everything from the logs using only the Python standard library:

| | With TruthGraph | Without | Change |
| --- | ---: | ---: | ---: |
| Total tokens | 3,178,299 | 4,469,228 | −28.9% |
| Input tokens | 3,165,558 | 4,454,940 | −28.9% |
| of which uncached | 157,302 | 191,644 | −17.9% |
| Output tokens (incl. reasoning) | 12,741 | 14,288 | −10.8% |
| Task duration | 424.1 s | 475.5 s | 51.4 s faster |
| Tool calls | 25 | 31 | |

## Read this before quoting the numbers

- **One task, one run each.** This shows what happened once on one codebase. It is not an average.
- **Most of the saving is cached input.** Codex resends the conversation on every step, and most of that is served from the provider's cache. The uncached input fell 17.9% and output fell 10.8%. Because cached tokens are billed at a lower rate, the cost change is smaller than 28.9%.
- **The prompts differ in their tool instruction.** The task text is identical. The "with" prompt adds an instruction to use TruthGraph, and the "without" prompt adds an instruction not to. In the "without" run TruthGraph was excluded by that instruction, not by configuration. The log shows zero TruthGraph calls in that run.
- **The with-TruthGraph run went first**, 9 minutes before the other. Order and cache warmth were not controlled; the causal effect of order/cache conditions is not established.
- **The repository is private.** Outsiders can check the logs and recordings against each other, but cannot rerun this exact task. A public-repository benchmark is being prepared separately.
- **Later settings records remain included.** The ON/OFF whole logs each retain two post-task `thread_settings_applied` records (25 and 27 October); the summary retains one (27 October). No additional user/task turns were found. Existing public copies exactly match the current whole native originals; they were not replaced or cleaned.

## Verify

The recordings are too large for git. On GitHub they are attached to the release [`2026-10-25-weeyugaweb-request-id`](https://github.com/slobodanmargetic988/truthgraph-benchmark-evidence/releases/tag/2026-10-25-weeyugaweb-request-id). Download them into `videos/` before checking hashes:

```bash
gh release download 2026-10-25-weeyugaweb-request-id -R slobodanmargetic988/truthgraph-benchmark-evidence -D videos
shasum -a 256 -c SHA256SUMS
python3 verify.py
```

`SHA256SUMS` fixes the content of every file here. Each log's `session_meta` line carries its thread ID and the Codex version, and every event has a timestamp. You can match the timestamps to the "Working for …" timers and the session IDs in the status panel visible in the recordings.

## Publication and workflow audit — 28 October 2026

All three owner-specified raw logs were already present, along with the summary sub-agent log. The three Desktop recordings were already GitHub release assets. Their GitHub SHA-256 digests/sizes match both the existing checksum manifest and the Desktop originals; no replacement or duplicate upload was needed. The ON/OFF clips cover their complete task intervals; the summary recording starts about 2 seconds after that task began and covers completion. See [publication-audit-20261028.json](publication-audit-20261028.json).

This older ON run used the **operator `truthgraph` MCP**, not the customer `/api/mcp` hybrid/vector pipeline. It made 10 native operator calls, including one failed lookup; other lookups were bounded/truncated. Those failures remain in the raw. It had 23 local command events / 26 model responses, versus 36 / 32 in OFF: observed less work consistent with reduced repeated context, not a controlled causal or quality claim. The third thread and its sub-agent contain the agents' own measurements/conclusions; preserving them does not turn every conclusion into a verified fact.

Nine sampled video frames passed known-secret OCR checks, and three middle frames visibly matched the corresponding Codex chats. This was a bounded sample review, not an exhaustive privacy certification of every video frame. Raw logs and recordings remain unmodified.
