# Limitations Register

*CDFI Framework v1.5 | SAICRED v2 Reference Implementation*

*Author: Mark Julius Banasihan | May 2026*

---

> Limitations are documented here, not buried in appendices. A benchmark that conceals its constraints is not a credible benchmark. Every item below states the limitation, its scope, and the condition that closes it.

---

## Status Overview

| # | Limitation | Scope | Blocks Publication? | Status |
|---|-----------|-------|:-------------------:|--------|
| L1 | Authority level classification pending | All 400 v2 prompts | **Yes — final CDFI** | Open |
| L2 | Human theological review pending | All 21,599 metric scores | **Yes — full publication** | Open |
| L3 | Pastoral appropriateness kappa below threshold | 1 of 9 metrics | No (formula weight 0.02–0.05) | Disclosed |
| L4 | Stability scores hardcoded | All v2 stability scores | No (deferred to v2.1) | Open |
| L5 | Statistical significance of rank ordering | Positions 1–5 | No (interpretive constraint) | Disclosed |
| L6 | Temporal validity of scores | All v2 scores | No (versioning protocol) | Active |
| L7 | Security: prompt injection (judge), pipeline integrity, authority level signing | Attack surfaces disclosed | No — v1.6 remediation planned | Open |

---

## L1 — Authority Level Classification

**What the limitation is:**
All 400 SAICRED v2 prompts were scored using the `ordinary_magisterium` weight column because theological advisor classification of each prompt by doctrinal authority level had not been completed before the benchmark run. The four-column weighting matrix was not fully applied.

**What this means for the rankings:**
The current scores answer: *how do these models perform when every question is treated as ordinary magisterium?*

They do not yet answer: *how do these models perform when each question carries the weights appropriate to its actual doctrinal authority level?*

These are different measurements. The rankings will shift when the full matrix is applied. How much they shift is unknown until classification is complete.

**What the rankings can claim now:**
Directionally valid preliminary scores. The relative ordering is informative. No score should be cited as a final CDFI in publication.

**Closing condition:**
Theological advisors classify each of the 100 base questions by authority level. The pipeline reads `authority_level` at runtime — no schema changes required. Naveen can recompute all 2,400 CDFI scores in under 15 minutes using `python3 scoring_service.py --cdfi-only`.

**Disclosure language for publication:**
> *"All 400 prompts in SAICRED v2 were scored using the `ordinary_magisterium` weight column. Authority level classification by theological advisors is pending. Rankings are preliminary and will be revised once the full four-column weighting matrix is applied."*

---

## L2 — Human Theological Review

**What the limitation is:**
All 21,599 metric scores in SAICRED v2 were produced by Gemini 2.5 Flash without validation against human theological expert judgment.

**What the judge reliability certification covers:**
The four-part certification (all parts cleared May 11, 2026) verifies statistical consistency: the judge applies the rubric consistently across repeated runs, calibrates to the scoring anchors, and correctly identifies adversarial invariance and gate-triggering responses. It does not certify that the rubric itself, or the judge's application of it, correctly reflects Catholic theological standards.

**The gap:**
A judge can be perfectly consistent in applying a rubric that is theologically wrong on a specific class of questions. Human theological review catches this. Automated reliability testing does not.

**Closing condition:**
A representative sample of automated scores (methodology specified in SAICRED Addendum E) validated against human theological expert judgment. Owner: Filip Ponulak and theological advisors.

**Disclosure language for publication:**
> *"All metric scores were produced by an automated LLM judge (Gemini 2.5 Flash). None have been validated against human theological expert judgment. Human theological review per Addendum E is required before full publication."*

---

## L3 — Pastoral Appropriateness Kappa

**What the limitation is:**
The automated judge produced Cohen's kappa of 0.352 on the pastoral appropriateness metric in the Part 1 reliability run (May 7, 2026, n=50). This is below the 0.60 Critical metric threshold and below the 0.40 general flag threshold.

**Why it does not block publication:**
Pastoral appropriateness carries a formula weight of 0.02 (`defined_dogma`) to 0.05 (`legitimate_opinion`) across all four authority columns. At maximum weight, a 1-point judge inconsistency on this metric changes the CDFI by 1.0 point. That cannot materially shift any ranking. No model's deployment tier would change as a result of this metric's inconsistency.

**What it means:**
The pastoral appropriateness scores in v2 are less reliable than the other eight metrics. They should not be cited as precise standalone measurements.

**Disclosure language for publication:**
> *"Pastoral appropriateness produced a judge Cohen's kappa of 0.352, below the 0.60 publication threshold. Its formula weight of 0.02–0.05 means this inconsistency cannot materially affect any model's mean CDFI or deployment tier. Disclosed as a methodological limitation."*

---

## L4 — Stability Scores Hardcoded

**What the limitation is:**
All stability scores in SAICRED v2 were set to 3.0 (the midpoint of the 0–5 scale). Real stability scores require running each prompt through the model five times and computing variance across the five responses. This was deferred to v2.1.

**What this means for the rankings:**
Because every model received the same stability score on every prompt, stability did not differentiate any model's CDFI in v2. The column weight for stability (0.05 to 0.19 depending on authority level) applied uniformly. Models with genuine run-to-run instability were not penalized.

**Closing condition:**
Five-run evaluation per prompt implemented in v2.1. No change to the formula or schema required.

---

## L5 — Statistical Significance of Rank Ordering

**What the limitation is:**
Pairwise Welch t-tests with clustered standard errors (topic_domain, G=7) show that most rank-order gaps in v2 are not statistically significant at 95% confidence.

**Exact significance results from v2:**

| Comparison | Mean Difference | p-value | Significant at 95%? |
|------------|:--------------:|:-------:|:-------------------:|
| o3 vs. DeepSeek V4 | 1.6 pts | 0.201 | No |
| DeepSeek V4 vs. Gemini 3.1 Pro | 0.9 pts | 0.533 | No |
| Gemini 3.1 Pro vs. GPT-5.4 | 0.4 pts | 0.747 | No |
| GPT-5.4 vs. Grok 4 | 0.004 pts | 0.998 | No |
| Grok 4 vs. Claude Sonnet 4.6 | 4.1 pts | **0.008** | **Yes** |

**What this means for publications:**
The rank ordering of positions 1 through 5 should be presented as directionally informative, not as reliably separated performance. Only the Grok 4 vs. Claude Sonnet 4.6 gap reaches significance at this benchmark scale. o3's deployment tier (Formation and Catechesis) is defensible on the mean threshold crossing (85.0). Its separation from positions 2–5 on the mean is not statistically confirmed at this scale.

---

## L6 — Temporal Validity

**What the limitation is:**
CDFI scores are measurements of specific model versions at a point in time, not permanent properties of model names.

**v2 scores are tied to:**
- o3 as evaluated May 2026
- DeepSeek V4 as evaluated May 2026
- Gemini 3.1 Pro Preview as evaluated May 2026
- GPT-5.4 as evaluated May 2026
- Grok 4 as evaluated May 2026
- Claude Sonnet 4.6 as evaluated May 2026

**Closing condition per model:**
Major version update triggers re-evaluation per the temporal versioning protocol in `docs/governance/temporal-versioning.md`. Minor updates (system prompt changes, API changes that do not affect model weights) do not expire the score.

---

*This register should be cited in any publication using SAICRED v2 CDFI scores.*

*Last updated: May 2026 | CDFI Framework v1.5*

