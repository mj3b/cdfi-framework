# Changelog

*CDFI Framework — Version history and re-evaluation record*

---

> CDFI scores expire on major model version updates per the temporal versioning protocol (`docs/governance/temporal-versioning.md`). This changelog is the authoritative record of every evaluation run, methodology change, and score revision. It is a living document.

---

## Framework v1.0 — May 2026

**Initial release. Reference implementation of the CDFI methodology derived from seven Anthropic AI safety research publications.**

### What was established

- CDFI formula and four-column weighting matrix (Section 3.5 of SAICRED Implementation Guidelines)
- Five failure mode taxonomy: doctrinal omission, moral softening, citation fabrication, prompt sensitivity drift, contextual relativization
- Two pass/fail cap gates: hallucination and relativism resistance
- Four deployment tiers: Formation and Catechesis (85+), General Information (70–84), R&D Only (50–69), Not Recommended (below 50)
- Four-part judge reliability certification protocol
- Seven research-to-architecture translation documents

### Reliability certification history

| Run | Date | Parts Tested | Result | Key Finding |
|-----|------|:------------:|--------|-------------|
| Run 1 | Apr 29, 2026 | 1, 2, 3, 4 | FAIL | Part 1 blocker: `confidence_calibration` kappa 0.487. Part 2: anchor accuracy 79.9%. Part 4: cap gate accuracy 65% |
| Run 2 | May 4, 2026 | 4 | FAIL | Part 4: 80% accuracy. Root cause diagnosed: context question mismatch in test construction, not gate malfunction |
| Run 3 | May 6, 2026 | 1 | FAIL | Part 1 still failing; rubric revision in progress |
| Run 4 | May 6, 2026 | 1 | FAIL | Confidence calibration rubric revision continued |
| Run 5 | May 7, 2026 | 1 | **PASS** | `confidence_calibration` kappa improved to **0.831** after rubric revision with concrete score band examples. All Critical metrics cleared ≥ 0.60 |
| Run 6 | May 7, 2026 | 2 | **PASS** | Anchor calibration: **98.3%** accuracy (up from 79.9%) |
| Run 7 | May 11, 2026 | 4 | **PASS** | Cap gate precision: **100%** after two-stage question-pairing fix |

**Certification cleared: May 11, 2026. All four parts passing. `publication_ready: true`.**

### Final Part 1 kappa values (May 7, 2026, n=50)

| Metric | kappa | Status |
|--------|:-----:|--------|
| Hallucination | 1.000 | STRONG |
| Relativism Resistance | 0.846 | STRONG |
| Source Citation | 0.859 | STRONG |
| Confidence Calibration | 0.831 | STRONG |
| Completeness | 0.802 | STRONG |
| Doctrinal Precision | 0.644 | SUBSTANTIAL |
| Moral Fidelity | 0.636 | SUBSTANTIAL |
| Stability | — | Hardcoded (deferred to v2.1) |
| Pastoral Appropriateness | 0.352 | UNRELIABLE (disclosed — weight 0.02–0.05) |

---

## SAICRED v2 Benchmark Results — May 2026

**100 questions × 4 framings × 6 models = 2,400 responses. 21,599 metric scores.**

### Rankings (preliminary — authority level classification pending)

| Rank | Model | Mean CDFI | 95% CI (clustered) | Median | Cap Rate | Tier |
|:----:|-------|:---------:|:------------------:|:------:|:--------:|------|
| 1 | o3 | 85.0 | [83.0, 87.0] | 94.0 | 8.0% | **Formation and Catechesis** |
| 2 | DeepSeek V4 | 83.4 | [80.6, 86.2] | 91.6 | 12.5% | General Information |
| 3 | Gemini 3.1 Pro | 82.5 | [80.2, 84.8] | 91.6 | 14.5% | General Information |
| 4 | GPT-5.4 | 82.1 | [80.6, 83.7] | 84.4 | 8.0% | General Information |
| 5 | Grok 4 | 82.1 | [79.5, 84.7] | 94.0 | 15.3% | General Information |
| 6 | Claude Sonnet 4.6 | 78.0 | [76.1, 79.8] | 89.2 | 17.0% | General Information |

*95% CIs use clustered standard errors at topic_domain level (G=7). Only the Grok 4 vs. Claude Sonnet 4.6 gap reaches significance at 95% confidence (p=0.008).*

### Framing effect (mean CDFI by variant)

| Model | Neutral | Christian | Catholic | Adversarial | Gap (C − A) |
|-------|:-------:|:---------:|:--------:|:-----------:|:-----------:|
| o3 | 84.9 | 81.9 | 86.2 | 87.0 | **−0.8** |
| GPT-5.4 | 78.0 | 79.3 | 87.8 | 83.3 | +4.5 |
| Gemini 3.1 Pro | 79.5 | 78.2 | 90.3 | 82.0 | +8.3 |
| Grok 4 | 75.0 | 83.1 | 90.7 | 79.6 | +11.1 |
| DeepSeek V4 | 77.1 | 84.3 | 91.6 | 80.4 | +11.2 |
| Claude Sonnet 4.6 | 74.3 | 74.6 | 89.4 | 73.6 | **+15.8** |

### Cap event breakdown

| Model | Relativism only | Both gates | Hallucination only | Total | Rate |
|-------|:---------------:|:----------:|:-----------------:|:-----:|:----:|
| Claude Sonnet 4.6 | 42 | 20 | 7 | 69 | 17.3% |
| Grok 4 | 44 | 13 | 7 | 64 | 16.0% |
| Gemini 3.1 Pro | 36 | 15 | 7 | 58 | 14.5% |
| DeepSeek V4 | 27 | 12 | 11 | 50 | 12.5% |
| GPT-5.4 | 18 | 11 | 3 | 32 | 8.0% |
| o3 | 14 | 5 | 13 | 32 | 8.0% |
| **Total** | **181** | **76** | **48** | **305** | **12.7%** |

### Open publication gates at time of release

| Gate | Status |
|------|--------|
| Judge reliability certification | **CLEARED — May 11, 2026** |
| Authority level classification (400 prompts) | Pending — theological advisors |
| Human theological review (21,599 scores) | Pending — Filip Ponulak + advisors |
| Stability scoring (5 runs/prompt) | Deferred to v2.1 |

---

## Upcoming: SAICRED v2.1

**Planned additions:**

- Five-run stability scoring (removes hardcoded stability = 3.0)
- Authority level classification applied — final CDFI scores replace preliminary scores
- Human theological review completed — full publication weight achieved
- Updated rankings with complete four-column matrix applied

---

*Maintained by: Mark Julius Banasihan *

