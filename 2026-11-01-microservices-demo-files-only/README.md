# Online Boutique (microservices-demo): files-only comparison

Three whole native sessions: the original run WITHOUT TruthGraph, the previous run WITH evidence-bearing TruthGraph responses, and a new files-only run WITH TruthGraph. Exact prompts, cost categories, the source-quality review, full unchanged JSONL and an offline verifier follow the repository format.

**API-equivalent cost $0.4030 OFF → $0.3860 previous ON → $0.2648 files-only (-34.30% versus OFF). Duration -30.68%, output -19.95%, uncached input -43.01% versus OFF; static quality 9.5 OFF → 9.5 files-only.** One predeclared run, not a suite success rate or product-wide claim.

Read [ANALYSIS.md](ANALYSIS.md) for side-by-side metrics, all absolute and percentage changes, category pricing, environment differences and raw-log observations. No recording exists for this automated comparison.

Run `python3 verify.py` offline to recompute whole-session counters, durations and category costs, and to verify manifest hashes, exact prompts, model/effort controls and quality/answer association. It makes no network, model or application-test calls.

The three JSONLs in `logs/` are full byte-identical native captures. They retain native paths/account/session/tool metadata. No trimming, redaction, reformatting or repair occurred. No database dump, credentials or client secret configuration is included. Pattern screening and its limits are in publication-audit.json.
