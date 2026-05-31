# Translation 4 — Point Estimates Without Uncertainty Quantification Are Not Defensible

**Source Publication:** [A Statistical Approach to Model Evaluations](https://www.anthropic.com/research/statistical-approach-to-model-evals) — Anthropic, November 2024

**Paper:** [arxiv.org/abs/2411.00640](https://arxiv.org/abs/2411.00640)

**SAICRED Implementation Guidelines:** Sections 3.4, 3.5, 3.8

**CDFI Artifacts Produced:** 95% confidence interval requirement; clustered standard errors (G=7, topic domain); deployment tier thresholds (85/70/50); temporal versioning protocol

---

> **How to read this document.** This paper is the most technically direct of the seven
> translations. Its recommendations map almost 1:1 onto CDFI statistical requirements.
> Claim types are marked but most are Direct rather than Derived.

---

## Why This Paper

The paper asks a specific question: when a model outperforms another on a benchmark, is the
difference real or could it reflect the specific question set chosen? It derives recommendations
for confidence intervals, clustered standard errors, paired-difference analysis, and power
analysis. The CDFI's statistical architecture follows these recommendations precisely. The
most consequential finding for the SAICRED v2 publication: pairwise significance tests with
clustered standard errors show that only the Grok 4 vs. Claude Sonnet 4.6 gap reaches
statistical significance. The rank ordering of positions 1 through 5 is directionally
informative but not statistically distinguished.

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
A benchmark ranking without confidence intervals cannot distinguish
between a real performance difference and sampling variation from the
specific questions chosen. Institutions that rely on point-estimate
rankings to make deployment decisions may be relying on noise.

Claim type: DIRECT
The paper states this explicitly in its opening paragraph and all
five recommendations follow from this premise.

See Source Evidence Record: E1.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
A Catholic diocese choosing between two AI models based on CDFI
rankings is making a deployment decision. If the 2.9-point gap
between DeepSeek V4 (83.4) and Gemini 3.1 Pro (82.5) is within
the confidence interval, reporting it as a ranked difference
misrepresents the evidence.

The SAICRED v2 finding: only the Grok 4 vs. Claude Sonnet 4.6 gap
reaches significance at 95% confidence (p=0.008). The 7.0-point gap
between o3 and Claude does not (p=0.142). A publication that presents
ranks 1–5 as reliably differentiated would be making claims the data
do not support.

Claim type: DERIVED
The diocese harm scenario is an original translation. The statistical
principle is direct.

See Source Evidence Record: E1, E3.

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
Overstated ranking precision: presenting point-estimate rankings as
reliable performance separations when the differences are within
confidence intervals. Not a model failure mode — an evaluation
reporting failure mode.

Claim type: DERIVED

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
95% confidence intervals using clustered standard errors:

  Clustering variable: topic_domain (G=7)
  Questions within the same domain are non-independent.
  Naive standard errors underestimate uncertainty.
  SAICRED v2 uses G=7 clusters matching the seven topic domains.

Pairwise Welch t-tests with clustered SEs:
  Tests whether any two models' CDFI distributions are
  statistically distinguishable, accounting for the shared
  question set.

Claim type: DIRECT

See Source Evidence Record: E2.

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
Deployment tier thresholds (configs/threshold_gates.yaml):
  85+:      Formation and Catechesis
  70–84:    General Information
  50–69:    R&D Only
  Below 50: Not Recommended

Derived from the paper's principle that readiness thresholds are
context-dependent: a model adequate for low-stakes information
retrieval may be inadequate for high-stakes formation. The specific
values were proposed by the Evaluation Expert, reviewed against the
SAICRED white paper's theological criteria, and accepted into the
Implementation Guidelines.

Temporal versioning protocol (docs/governance/temporal-versioning.md):
  A model's CDFI score is tied to a specific model version.
  Major version updates trigger re-evaluation. Scores expire.

This requirement derives from the paper's framing of eval scores as
estimates of "theoretical means across all possible questions" —
an estimate that changes when the underlying model changes.

Claim type: DIRECT (statistical principle) / DERIVED (threshold values)

See Source Evidence Record: E1, E3.

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
The statistical architecture does not add a certification part.
It constrains how certification results are reported:
  kappa values must include confidence intervals.
  Threshold comparisons must be significance-tested, not point-compared.

In practice, the four-part certification reports absolute kappa values
against fixed thresholds. The deeper statistical discipline appears
in how benchmark scores (not certification scores) are reported.

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
SAICRED v2 pairwise significance results:

  Pair                        Gap      p-value    Significant at 95%?
  ──────────────────────────  ──────   ────────   ──────────────────
  Grok 4 vs. Claude           4.1      0.008      YES
  o3 vs. Claude               7.0      0.142      NO
  DeepSeek V4 vs. Claude      5.4      0.071      NO
  Gemini 3.1 Pro vs. Claude   4.5      0.094      NO
  GPT-5.4 vs. Claude          4.1      0.108      NO

  Publication position: ranks 1–5 are directionally informative,
  not reliably separated. o3 is the only model cleared for formation
  use. The gap between positions 2–6 should not be presented as
  a reliable performance ranking.
```

---

## Source Evidence Record

---

### E1 — Point Estimates Without Uncertainty Quantification Are Not Defensible

**Claim type:** Direct

**CDFI mechanism:** 95% CI requirement; temporal versioning

**Verbatim extract:**

> "Suppose an AI model outperforms another model on a benchmark of interest — testing its
> general knowledge, for example, or its ability to solve computer-coding questions. Is the
> difference in capabilities real, or could one model simply have gotten lucky in the choice
> of questions on the benchmark? With the amount of public interest in AI model evaluations
> — informally called 'evals' — this question remains surprisingly understudied among the
> AI research community."

*— Introduction*

> "We argue that the real object of interest should not be the observed average, but rather
> the theoretical average across all possible questions."

*— Recommendation 1 (Use the Central Limit Theorem)*

**Inference chain to CDFI:**

The paper establishes that any eval score is an estimate of an underlying theoretical
performance, not a fixed truth. The CDFI adopts this framing directly: CDFI scores are
estimates with confidence intervals, not point measurements. The temporal versioning
protocol follows from the same logic: if the underlying model changes, the estimate
expires.

---

### E2 — Clustered Standard Errors Are Required When Questions Are Non-Independent

**Claim type:** Direct

**CDFI mechanism:** Clustered standard errors (G=7, topic domain)

**Verbatim extract:**

> "Many evals violate the above assumption of independently selected questions, and instead
> consist of groups of closely related questions. For these evals, each question's selection
> from the 'question universe' is no longer independent. Because including several questions
> about the same passage of text will yield less information than selecting the same number
> of questions about different passages of text, a naive application of the Central Limit
> Theorem to the case of non-independent questions will lead us to underestimate the
> standard error — and potentially mislead analysts into drawing incorrect conclusions from
> the data."

*— Recommendation 2 (Cluster standard errors)*

> "In practice, we have found that clustered standard errors on popular evals can be over
> three times as large as naive standard errors."

*— Recommendation 2 (Cluster standard errors)*

**Inference chain to CDFI:**

SAICRED v2 groups 100 questions into 7 topic domains. Questions within the same domain
are non-independent — a model's performance on papal infallibility questions is correlated
with its performance on other ecclesiology questions. Naive standard errors would
underestimate uncertainty by the factor the paper documents. SAICRED v2 uses G=7
clustering on topic domain to address this directly.

---

### E3 — Statistical Power Analysis Determines Whether a Difference Is Detectable

**Claim type:** Direct

**CDFI mechanism:** Disclosure that ranks 2–5 are directionally informative only

**Verbatim extract:**

> "If an eval doesn't have very many questions, confidence intervals associated with any
> statistical tests will tend to be wide. This means that models will need to have a large
> underlying difference in capabilities in order to register a statistically significant
> result — and that small differences will likely go undetected."

*— Recommendation 5 (Use power analysis)*

> "Therefore, in the interest of extracting the clearest signal from the data, our paper
> recommends reporting pairwise information — mean differences, standard errors, confidence
> intervals, and correlations — whenever two or more models are being compared."

*— Recommendation 4 (Analyze paired differences)*

**Inference chain to CDFI:**

SAICRED v2 has 400 prompts per model. The paper's power analysis framework implies that
small differences between frontier models may not be detectable at this sample size. The
pairwise significance test results confirm this: only one of five possible pairings reaches
95% confidence. The correct publication position is to present the ranking as directional,
not as a reliable performance separation, which is exactly what the SAICRED v2 findings
document.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Point estimates not defensible | Direct | Yes | Introduction, Recommendation 1 |
| E2 — Clustered SEs required | Direct | Yes | Recommendation 2 |
| E3 — Power analysis determines detectability | Direct | Yes | Recommendations 4, 5 |

---

*CDFI formula: [`docs/specifications/CDFI-formula.md`](../specifications/CDFI-formula.md)*

*Deployment tiers: [`docs/specifications/deployment-tiers.md`](../specifications/deployment-tiers.md)*

*Temporal versioning: [`docs/governance/temporal-versioning.md`](../governance/temporal-versioning.md)*

*Claims pack (planned v1.5): [`claims/pub3-statistical-rigor.json`](../../claims/pub3-statistical-rigor.json)*
