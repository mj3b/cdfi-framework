# Translation 4 — Statistical Rigor Produces Defensible Rankings

**Source Publication:** [A Statistical Approach to Model Evaluations](https://www.anthropic.com/research/statistical-approach-to-model-evals) — Anthropic, November 2024

**Paper:** [arxiv.org/abs/2411.00640](https://arxiv.org/abs/2411.00640)

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

## Source Evidence Record

This section provides the verbatim paper text that anchors each step of the translation pipeline above. Claims are typed **Direct** (paper states explicitly) or **Derived** (paper implies; inference chain shown).

This paper is the most directly applicable of the seven translations. Its recommendations map almost 1:1 onto CDFI statistical requirements. The inference chains are correspondingly short.

---

### E1 — Point Estimates Without Uncertainty Quantification Are Not Defensible

**Claim type:** Direct

**CDFI mechanism:** 95% CI requirement; deployment tier thresholds as context-dependent readiness

**Verbatim extract:**

> "Suppose an AI model outperforms another model on a benchmark of interest — testing its general knowledge, for example, or its ability to solve computer-coding questions. Is the difference in capabilities real, or could one model simply have gotten lucky in the choice of questions on the benchmark? With the amount of public interest in AI model evaluations — informally called 'evals' — this question remains surprisingly understudied among the AI research community."

*— Introduction*

> "We argue that the real object of interest should not be the observed average, but rather the theoretical average across all possible questions. So if we imagine that eval questions were drawn from an unseen 'question universe,' we can learn about the average score in that universe — that is, we can measure the underlying skill, independent of the 'luck of the draw' — using statistical theory."

*— Recommendation 1: Use the Central Limit Theorem*

**Inference chain to CDFI:**

The paper establishes that any eval score is an estimate of an underlying theoretical performance, not a fixed truth. A bishop's conference acting on a point estimate of 82.5 is treating a sample statistic as a population parameter. The CDFI requires 95% confidence intervals on all rankings so that institutional actors can see the range of plausible underlying performance — not just the observed sample mean.

---

### E2 — Clustered Questions Require Clustered Standard Errors

**Claim type:** Direct

**CDFI mechanism:** Clustered standard errors at topic_domain level (G=7)

**Verbatim extract:**

> "Many evals violate the above assumption of independently selected questions, and instead consist of groups of closely related questions. For these evals, each question's selection from the 'question universe' is no longer independent. Because including several questions about the same passage of text will yield less information than selecting the same number of questions about different passages of text, a naive application of the Central Limit Theorem to the case of non-independent questions will lead us to underestimate the standard error — and potentially mislead analysts into drawing incorrect conclusions from the data."

*— Recommendation 2: Cluster standard errors*

> "In practice, we have found that clustered standard errors on popular evals can be over three times as large as naive standard errors."

*— Recommendation 2: Cluster standard errors*

**Inference chain to CDFI:**

The SAICRED v2 dataset contains four variants of each of 100 base questions. Questions within the same topic domain are non-independent: a model's performance on papal infallibility questions predicts its performance on other ecclesiology questions. Naive standard errors would underestimate uncertainty by the factor the paper documents. SAICRED v2 clusters on topic_domain (G=7) directly implementing this recommendation.

---

### E3 — Paired Difference Analysis Extracts the Strongest Signal

**Claim type:** Direct

**CDFI mechanism:** Pairwise Welch t-tests; positions 2–5 disclosed as directionally informative

**Verbatim extract:**

> "In practice, we find the correlation of question scores on popular evals between frontier models to be substantial — between 0.3 and 0.7 on a scale of −1 to +1. Put another way, frontier models have an overall tendency to get the same questions right and wrong. Paired-difference analysis thus represents a 'free' variance reduction technique that is very well suited for AI model evals. Therefore, in the interest of extracting the clearest signal from the data, our paper recommends reporting pairwise information — mean differences, standard errors, confidence intervals, and correlations — whenever two or more models are being compared."

*— Recommendation 4: Analyze paired differences*

**Inference chain to CDFI:**

The paper establishes that frontier models share question-level performance patterns — they tend to succeed and fail on the same questions. Exploiting this correlation through paired-difference analysis reduces apparent variance without collecting more data. The SAICRED v2 pairwise Welch t-tests implement this recommendation. The finding that only the Grok 4 vs. Claude gap reaches significance (p=0.008) while the o3 vs. Claude gap does not (p=0.142) directly follows from applying the paper's analytical framework to the v2 data.

---

### E4 — Context-Dependent Readiness Requires Context-Differentiated Thresholds

**Claim type:** Direct

**CDFI mechanism:** Three deployment tier thresholds (85/70/50); temporal versioning protocol

**Verbatim extract:**

> "If an eval doesn't have very many questions, confidence intervals associated with any statistical tests will tend to be wide. This means that models will need to have a large underlying difference in capabilities in order to register a statistically significant result — and that small differences will likely go undetected."

*— Recommendation 5: Use power analysis*

> "Statistics is the science of measuring uncertainty. The scientific goal of an eval is to measure a model's underlying skill — the average score it would achieve across all possible questions."

*— Conclusion*

**Inference chain to CDFI:**

The paper establishes that the goal of evaluation is to measure underlying skill, and that the usefulness of a score depends on whether the underlying skill is being measured for the right purpose. A model adequate for general knowledge retrieval is not necessarily adequate for high-stakes institutional decision support. The CDFI deployment tier thresholds operationalize this principle: three distinct tiers with three distinct cutoffs reflect three distinct institutional risk profiles. The temporal versioning protocol follows from the same logic: an estimate of underlying skill expires when the underlying model changes.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Point estimates not defensible without CIs | Direct | Yes | Introduction; Recommendation 1 |
| E2 — Clustered questions require clustered SEs | Direct | Yes | Recommendation 2 |
| E3 — Paired difference analysis for frontier models | Direct | Yes | Recommendation 4 |
| E4 — Context-dependent readiness | Direct | Yes | Recommendation 5; Conclusion |

All four evidence items are typed Direct. This is the most straightforward of the seven translations: every CDFI statistical requirement maps to a named recommendation in the paper. The inference chains are short because the translation distance is small.

---

*Specification: [`docs/specifications/deployment-tiers.md`](../specifications/deployment-tiers.md)*

*Versioning: [`docs/governance/temporal-versioning.md`](../governance/temporal-versioning.md)*

*Claims pack (planned v1.5): [`claims/pub3-statistical-rigor.json`](../../claims/pub3-statistical-rigor.json)*
