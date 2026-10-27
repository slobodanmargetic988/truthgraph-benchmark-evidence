# One task, with and without TruthGraph (25 October 2026)

Raw evidence for the "28.9% fewer tokens, 51 seconds faster" result. Everything here is unedited: the Codex session logs exactly as Codex wrote them, and the screen recordings of all three threads as they ran.

## What was run

Two Codex desktop threads ran the same read-only investigation of the founder's WeeyugaWeb repository at commit `6db98fe250a0663fc1f3ca970199ae6ac63cd8bc`. The task was to plan an optional `request_id` for the cluster chat API: find the entry points, the models to change, the callers, the forwarding layers that could drop it, logging, and the tests. Both threads used the same model and effort: `gpt-6.1-sol`, effort `ultra`.

| Thread | Mode | Started (UTC) | Recording |
| --- | --- | --- | --- |
| `01a17372-0953-7aa1-8fb9-ca58efd98f74` | With TruthGraph: the prompt asks for the `truthgraph-context` skill and the TruthGraph MCP | 14:23:36 | `videos/1-with-truthgraph_…mov` |
| `01a17378-fbf8-7da3-899f-12448bc85709` | Without TruthGraph: the prompt allows file reads, text search and Git only | 14:32:14 | `videos/2-without-truthgraph_…mov` |
| `01a17381-9dde-7f50-a8ed-d237770f3703` | A third Codex thread asked to measure the two runs, so the totals are the agent's own reading of the logs | 14:42:02 | `videos/3-codex-summary_…mov` |
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
- **The with-TruthGraph run went first**, 9 minutes before the other. Run order doesn't change token counts. Any provider-side caching shared between threads could only have helped the second run, which was the one without TruthGraph.
- **The repository is private.** Outsiders can check the logs and recordings against each other, but cannot rerun this exact task. A public-repository benchmark is being prepared separately.
- **The logs were reopened on 27 October.** Opening a thread in the Codex app appends one `thread_settings_applied` line, dated 27 October, to its log. Nothing else was added.

## Verify

The recordings are too large for git. On GitHub they are attached to the release [`2026-10-25-weeyugaweb-request-id`](https://github.com/slobodanmargetic988/truthgraph-benchmark-evidence/releases/tag/2026-10-25-weeyugaweb-request-id). Download them into `videos/` before checking hashes:

```bash
gh release download 2026-10-25-weeyugaweb-request-id -R slobodanmargetic988/truthgraph-benchmark-evidence -D videos
shasum -a 256 -c SHA256SUMS
python3 verify.py
```

`SHA256SUMS` fixes the content of every file here. Each log's `session_meta` line carries its thread ID and the Codex version, and every event has a timestamp. You can match the timestamps to the "Working for …" timers and the session IDs in the status panel visible in the recordings.
