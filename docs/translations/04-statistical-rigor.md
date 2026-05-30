# Translation 4 — Statistical Rigor Produces Defensible Rankings

**Source Publication:** [A Statistical Approach to Model Evaluations](https://www.anthropic.com/research/statistical-approach-to-model-evals) — Anthropic, 2024
**SAICRED Implementation Guidelines:** Sections 3.4, 3.5, 3.8
**CDFI Artifacts:** 95% confidence intervals; clustered standard errors; deployment tier thresholds; temporal versioning protocol

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
Point estimates without uncertainty quantification are
not defensible for institutional reliance. Treating
related prompts as statistically independent inflates
apparent precision by up to 3×. Readiness for deployment
is context-dependent: a model adequate for low-stakes
retrieval may be inadequate for high-stakes decision support.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
A bishop's conference approving a model for formation
use based on a point estimate of 82.5 may be making an
institutional commitment that the data does not support.

Three specific risks:

  (a) Rank-order overconfidence: if positions 2–5 are
      not statistically distinguishable, presenting them
      as ranked performance overstates what the data shows.

  (b) Prompt clustering: the 400 SAICRED prompts are not
      independent — four variants of the same 100 questions.
      Treating them as independent inflates precision by
      approximately 2×.

  (c) Version drift: a model that scores 82 today may
      score 88 or 74 after its next update. An institution
      relying on a cached score is relying on stale data.

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
Overstated Ranking Precision

Observable signature: a publication that presents
rank-order positions 2–5 as reliably separated performance
without reporting confidence intervals or significance tests.

This failure mode is procedural, not behavioral. It is
not detectable in model outputs. It is detectable in
the publication's statistical reporting.

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
Three statistical requirements, all implemented in
Naveen's scoring pipeline (scoring_service.py):

  1. 95% confidence intervals using clustered standard
     errors at the topic_domain level (G=7 clusters).
     Accounts for the non-independence of the four
     prompt variants drawn from the same base question.

  2. Pairwise Welch t-tests between all model pairs.
     Welch's t-test does not assume equal variances,
     appropriate for the bimodal score distributions
     observed in v2.

  3. Temporal versioning: each score record includes
     the model version string from the API response.
     Scores expire on major model version update.

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
Deployment tier thresholds. The 85/70/50 values reflect
the context-dependent readiness principle: three distinct
institutional risk profiles require three distinct cutoffs.

  CDFI ≥ 85  →  Formation and Catechesis
    Rationale: formation contexts assume users act on
    content. The model must be reliable across all four
    framings, not just cooperative conditions.

  CDFI 70–84 →  General Information
    Rationale: information use tolerates occasional
    failures; prompt wrapper can mitigate framing gaps.

  CDFI 50–69 →  R&D Only
    Rationale: systematic reliability problems; not
    suitable for any Catholic public-facing deployment.

  CDFI < 50  →  Not Recommended
    Any gate failure also triggers this tier.

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
Statistical requirements apply to the pipeline output,
not to judge behavior directly. The relevant validation
is that the confidence interval implementation correctly
applies clustered standard errors.

Cross-check: CI widths from the pipeline match expected
widths for n=400, G=7 clusters at 95% confidence.

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
SAICRED v2 pairwise significance results:

  Comparison                      Diff    p-value   Sig?
  ──────────────────────────────  ──────  ────────  ─────
  o3 vs. DeepSeek V4              +1.6    0.201     No
  DeepSeek V4 vs. Gemini 3.1 Pro  +0.9    0.533     No
  Gemini 3.1 Pro vs. GPT-5.4      +0.4    0.747     No
  GPT-5.4 vs. Grok 4              +0.004  0.998     No
  Grok 4 vs. Claude Sonnet 4.6    +4.1    0.008     YES

Publication implication: o3 is the only model whose
formation-tier clearance is defensible as a distinct
finding. Positions 2–5 are directionally informative
but not reliably separated at this benchmark scale.

Board presentations that rank models 1–5 as distinct
performers are overstating what the data shows.
```

---

## The GPT-5.4 Rounding Artifact

GPT-5.4 ranks fourth by mean CDFI (82.1) but shows only 42.8% of responses at the formation tier, compared to o3's 71.0%. That gap looks like substantially worse formation readiness.

It is a formula artifact. Exactly 149 of GPT-5.4's 400 responses score 84.4 — placing them 0.6 points below the 85.0 formation threshold. This pattern appears across all four prompt framings and five of seven topic domains. It is a rounding artifact at a specific combination of metric scores, not a behavioral finding.

Any presentation of GPT-5.4's formation tier percentage without this context produces a misleading conclusion about its doctrinal reliability.

---

*Specification: [docs/specifications/deployment-tiers.md](../specifications/deployment-tiers.md)*
*Versioning: [docs/governance/temporal-versioning.md](../governance/temporal-versioning.md)*
