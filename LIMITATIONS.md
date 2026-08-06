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
| L6 | Temporal validity of scores | All v2 scores | No (versioning protocol) | Standing |
| L7 | Security surface: judge prompt injection, pipeline integrity, authority level provenance | Three attack surfaces disclosed | No (v1.6 remediation planned) | Open |

**Status vocabulary.** *Open* means a closing condition exists and has not been met. *Disclosed* means the limitation will not close and is documented permanently. *Standing* means an ongoing protocol governs the item rather than a one-time fix.

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
Theological advisors classify each of the 100 base questions by authority level. The pipeline reads `authority_level` at runtime, so no schema changes are required. Naveen can recompute all 2,400 CDFI scores in under 15 minutes using `python3 scoring_service.py --cdfi-only`.

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

**Disclosure language for publication:**
> *"Stability scores in SAICRED v2 were fixed at 3.0 for all responses. Multi-run variance measurement is deferred to v2.1. Models with run-to-run instability are not penalized in v2 CDFI scores."*

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
The rank ordering of positions 1 through 5 should be presented as directionally informative, not as reliably separated performance. Only the Grok 4 vs. Claude Sonnet 4.6 gap reaches significance at this benchmark scale. o3's deployment tier (Formation and Catechesis) is defensible on the mean threshold crossing (85.0). Its separation from positions 2 through 5 on the mean is not statistically confirmed at this scale.

**Disclosure language for publication:**
> *"Pairwise Welch t-tests with clustered standard errors (G=7) confirm only one significant rank-order gap: Grok 4 vs. Claude Sonnet 4.6 (4.1 points, p=0.008). Positions 1 through 5 should be read as directionally informative rather than reliably separated."*

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

**Disclosure language for publication:**
> *"All CDFI scores reference the model versions evaluated in May 2026. Scores expire on major version update per the temporal versioning protocol. Any citation should include the evaluation date alongside the score."*

---

## L7 — Security Surface

**What the limitation is:**
The SAICRED v2 pipeline carries three unremediated attack surfaces. None were exploited in the v2 run. All three are disclosed because a benchmark that produces institutional deployment decisions should state what an adversary could change and what would go undetected if they did.

### L7a — Prompt injection against the judge

Gemini 2.5 Flash receives the model response as untrusted text inside the same context window that carries the scoring rubric. A response containing instruction-shaped content sits alongside the rubric with no delimiter isolation and no input sanitization. The v2 pipeline includes no test for whether the judge can be steered by content it is scoring.

**Why it did not affect v2:** All 2,400 responses came from six commercial models answering doctrinal questions under vendor default configurations. No response in the corpus was authored by a party with an incentive to manipulate its own score. The threat becomes live the first time SAICRED evaluates a model submitted by its own developer, which is the expected use case once the benchmark is published as a standard.

**Closing condition:** Delimiter isolation between response text and rubric instructions, plus a held-out injection test set scored as a fifth reliability part. Target: v1.6.

### L7b — Pipeline integrity

Score rows in `cdfi_scores_full.csv` carry no cryptographic binding to the prompt set version, model version strings, rubric version, or judge version that produced them. A modified CSV is indistinguishable from an authentic one by inspection. The scores are reproducible in principle because the pipeline is deterministic given the same inputs, and there is currently no record that fixes what those inputs were for a given run.

**Why it matters for institutional use:** A diocese citing a CDFI score in a deployment decision has no mechanism to verify that the score it received matches the score the pipeline produced.

**Closing condition:** Per-run content hash covering the four canonical CSVs, the rubric file, and the model version manifest, written to a signed run record. Target: v1.6.

### L7c — Authority level provenance

`authority_level` is a plain text field in `prompts_full.csv` that selects which CDFI weight column applies. Changing one prompt from `defined_dogma` to `legitimate_opinion` moves doctrinal precision weight from 0.30 to 0.15 and changes that prompt's CDFI. No record binds each assigned value to the theological advisor who assigned it or to the date of assignment.

**Interaction with L1:** This surface is dormant while L1 remains open, because every prompt currently defaults to `ordinary_magisterium` and the field carries no variation. It becomes live at the moment L1 closes. The classification pass that resolves L1 is also the point at which provenance should be captured, and capturing it retroactively costs more than capturing it during the pass.

**Closing condition:** Signed classification record naming the assigning advisor and date per prompt, produced during the L1 classification pass rather than after it. Target: v1.6.

**Disclosure language for publication:**
> *"SAICRED v2 discloses three unremediated security surfaces: the automated judge processes scored responses without delimiter isolation from rubric instructions, score records carry no cryptographic binding to the inputs that produced them, and authority level assignments carry no provenance record. None were exploited in the v2 run. Remediation is scheduled for CDFI Framework v1.6."*

---

*This register should be cited in any publication using SAICRED v2 CDFI scores.*

*Last updated: August 2026 | CDFI Framework v1.5*
