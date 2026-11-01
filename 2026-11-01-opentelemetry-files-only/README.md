# OpenTelemetry files-only comparison

Three whole native sessions: original WITHOUT TruthGraph, previous selected WITH evidence, and new files-only WITH TruthGraph. Exact prompts, counter/category costs, source-quality review, full unchanged JSONL and an offline verifier follow the repository format.

**API-equivalent cost:** $0.491990 OFF → $0.640835 previous ON → $0.460647 files-only, using owner-supplied gpt-6.1-sol rates. Files-only saves 28.12% versus previous ON, while output rises 3.63%, duration rises 14.82%, and targeted static quality is 9.0 versus 9.5/10. This is a selected individual comparison, not a product-wide or suite success-rate claim.

Read [ANALYSIS.md](ANALYSIS.md) for the side-by-side metrics, all absolute/percentage changes, category pricing, attempts, environment differences, raw-log findings and suggestions. Previous ON used lexical fallback; the new run completed hybrid retrieval. No recording exists for this automated comparison.

Run `python3 verify.py` offline to recompute whole-session counters, durations and category costs and verify all manifest hashes, exact prompts, model/effort controls and quality/answer association. It makes no network/model/application-test calls.

The three JSONLs in `logs/` are full byte-identical native captures. They retain native paths/account/session/tool metadata. No trimming, redaction, reformatting or repair occurred. No database dump, credentials or client secret configuration is included. Pattern screening and its limits are in publication-audit.json.
