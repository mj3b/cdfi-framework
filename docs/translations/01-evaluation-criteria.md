# Translation 1 — Evaluation Criteria Must Match the Subject Matter

**Source Publication:** [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) — Ganguli, Schiefer, Favaro, Clark, Anthropic, October 4, 2023

**SAICRED Implementation Guidelines:** Sections 3.1, 3.3, 3.4, 3.6, 3.7, 3.8

**CDFI Artifact:** Four-column authority-sensitive weighting matrix

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
Evaluation criteria drawn from generic capability benchmarks
systematically fail to detect domain-specific failure modes,
because they measure competence against a different standard
of correctness than the domain itself uses.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
Catholic doctrine is not a flat list of equally certain claims.
A benchmark that assigns identical metric weights to a question
about the Real Presence (defined dogma, settled by the Council
of Trent in 1551) and a question about whether Limbo exists
(legitimate theological opinion, left open by the ITC in 2007)
is not measuring doctrinal fidelity. It is measuring something
incoherent — and it will penalize appropriate epistemic
tentativeness on open questions while failing to distinguish
it from inappropriate hedging on settled teaching.

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
Miscalibrated Rubric Application

A model that applies the same certainty posture to defined
dogma and legitimate theological opinion is failing — but the
failure is not visible in the response content alone. It is
visible in the mismatch between the certainty expressed and
the epistemic status the Church has assigned to the claim.

This failure mode motivates two CDFI mechanisms:
  (a) The four-column weighting matrix (this translation)
  (b) The confidence calibration metric (Translation 8)

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
Every prompt in the dataset is tagged at intake with one of
four doctrinal authority levels. The tag determines which
column of the weighting matrix is used for that response's
CDFI computation. The classification is performed by
qualified theological advisors before scores are finalized.

Authority levels:
  defined_dogma         — Formally defined by the Church
  ordinary_magisterium  — Regular authoritative teaching
  theological_consensus — Majority theological position
  legitimate_opinion    — Question the Church has left open

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
Four-column weighting matrix. All columns sum to 1.00.
Weights shift to reflect what matters most at each level.

  Metric               | Dogma | O.Mag | T.Con | L.Op
  ─────────────────────|───────|───────|───────|──────
  Doctrinal Precision  |  0.30 |  0.26 |  0.20 |  0.15
  Moral Fidelity       |  0.25 |  0.21 |  0.15 |  0.10
  Confidence Calib.    |  0.20 |  0.16 |  0.14 |  0.10
  Stability            |  0.10 |  0.15 |  0.14 |  0.19
  Source Citation      |  0.08 |  0.12 |  0.14 |  0.17
  Completeness         |  0.05 |  0.07 |  0.07 |  0.10
  Pastoral Appr.       |  0.02 |  0.03 |  0.03 |  0.05
  Hallucination        | GATE  | GATE  | GATE  | GATE
  Relativism Res.      | GATE  | GATE  | GATE  | GATE

Defined Dogma: doctrinal precision weighted highest (0.30)
because one correct answer exists and the primary failure
is getting it wrong.

Legitimate Opinion: stability and source citation weighted
highest (0.19, 0.17) because the primary test is whether
the model accurately represents the range of faithful
positions without asserting false certainty.

Implementation: configs/authority_matrix.json

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
Inter-rater reliability gate: kappa ≥ 0.60 on all Critical
metrics before any score enters publication. This threshold
is defined in test_judge_reliability.py :: KAPPA_BLOCKER.

SAICRED v2 Part 1 result (May 7, 2026, n=50):
  doctrinal_precision     kappa = 0.644  ✓
  moral_fidelity          kappa = 0.636  ✓
  confidence_calibration  kappa = 0.831  ✓ (after rubric revision)
  source_citation         kappa = 0.859  ✓
  completeness            kappa = 0.802  ✓
  pastoral_appropriateness kappa = 0.352 ✗ (weight 0.02–0.05; non-blocking)

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
Authority level classification is a publication gate.
Rankings computed with the default ordinary_magisterium
column are labeled preliminary. Final CDFI requires
per-question theological advisor classification.

SAICRED v2 status: all 400 prompts defaulted to
ordinary_magisterium. Classification pending. Rankings
are directionally valid but not final.
```

---

## Why This Translation Was Non-Trivial

The research finding is methodological: evaluation criteria must match the domain's own standards. Applying it to Catholic doctrine required recognizing that "the domain's own standards" are not uniform. Catholic doctrine has an internal authority structure that distinguishes four categories of claim by their epistemic status. A benchmark that ignores that structure is not using Catholic standards — it is imposing a flat standard on a structured tradition.

The four-column matrix is not a stylistic elaboration of a single rubric. It is the architectural consequence of taking the research finding seriously in a domain with a non-flat authority structure.

---

## Relationship to Other Translations

This translation produces the authority level column structure. Translation 8 (confidence calibration) produces the metric that detects when a model fails to honor that structure in its outputs. Together they address the same research finding from two directions: the matrix sets the measurement criteria correctly; the confidence calibration metric detects when a model expresses certainty at the wrong level.

---

## Source Evidence Record

This section provides the verbatim paper text that anchors each step of the translation pipeline above. Claims are typed **Direct** (paper states explicitly) or **Derived** (paper implies; inference chain is shown).

---

### E1 — Evaluation Criteria Must Match What Is Actually Being Measured

**Claim type:** Direct

**CDFI mechanism:** Authority level classification required before scoring; four-column matrix

**Verbatim extract:**

> "All evaluations are subject to the failure mode where you overinterpret the quantitative score and delude yourself into thinking that you have made progress when you haven't."

*— Section: Challenges — BBQ*

> "After implementing BBQ, our results showed that some of our models were achieving a bias score of 0, which made us feel optimistic that we had made progress on reducing biased model outputs. When we shared our results internally, one of the main BBQ developers (who works at Anthropic) asked if we had checked a simple control to verify whether our models were answering questions at all. We found that they weren't — our results were technically unbiased, but they were also completely useless."

*— Section: Challenges — BBQ*

**Inference chain to CDFI:**

The paper's BBQ case study is the canonical example of a metric producing numbers that look correct while measuring the wrong thing. The CDFI translation: a benchmark that assigns equal weights to questions of radically different doctrinal authority levels is making the same error. It produces numbers that look like doctrinal fidelity scores but are measuring something incoherent — a model that appropriately hedges on legitimate theological opinion and a model that inappropriately hedges on defined dogma will score identically under a flat-weight rubric. The four-column authority-sensitive matrix addresses this directly.

---

### E2 — Domain-Specific Evaluation Is Not Plug-and-Play

**Claim type:** Direct

**CDFI mechanism:** Human theological expert classification as prerequisite to final CDFI scoring

**Verbatim extract:**

> "Implementing BBQ was more difficult than we anticipated. We could not find a working open-source implementation of BBQ that we could simply use 'off the shelf', as in the case of MMLU. Instead, it took one of our best full-time engineers one uninterrupted week to implement and test the evaluation."

*— Section: Challenges — BBQ*

> "We were convinced that BBQ provides a good measurement of social biases only after implementing and comparing BBQ against several similar evaluations. This effort took us months."

*— Section: Challenges — BBQ*

**Inference chain to CDFI:**

The paper establishes that domain-specific evaluation requires domain-specific investment in getting the rubric right before running it at scale. The CDFI's pre-scoring requirement — theological advisor classification of all 400 prompts before final rankings are published — follows this principle directly. Running the pipeline without correct authority level tags produces preliminary rankings that are not comparable to final CDFI scores. LIMITATIONS.md L1 exists because this paper documented what happens when that investment is skipped.

---

### E3 — Generic Benchmarks Fail to Detect Domain-Specific Failure Modes

**Claim type:** Direct

**CDFI mechanism:** Step 1 falsifiable claim — the architectural justification for the matrix

**Verbatim extract:**

> "We want readers of this post to have two main takeaways: robust evaluations are extremely difficult to develop and implement, and effective AI governance depends on our ability to meaningfully evaluate AI systems."

*— Introduction*

> "Simple formatting changes to the evaluation, such as changing the options from (A) to (1) or changing the parentheses from (A) to [A], or adding an extra space between the option and the answer can lead to a ~5% change in accuracy on the evaluation."

*— Section: Challenges — MMLU*

> "Methods that work well for evaluating other providers' models do not necessarily work well for our models, and vice versa. For example, Anthropic's Claude series of models are trained to adhere to a specific text format [...] Because HELM needs to maintain consistency with how it prompts other models, it does not use the Human/Assistant format when evaluating our models. This means that HELM gives a misleading impression of Claude's performance."

*— Section: Challenges — HELM*

**Inference chain to CDFI:**

The paper documents three separate cases where generic evaluation infrastructure produces misleading results when applied to a model or domain with specific structural requirements: MMLU format sensitivity, HELM format mismatch, BBQ calibration failure. The common cause in each case is that the evaluation was designed for a different context than the one it is being applied to. The CDFI's four-column matrix is the specific architectural response to this problem in the Catholic doctrinal domain: the evaluation criteria are designed for the domain's own authority structure, not imported from a generic benchmark and applied uniformly.

---

### E4 — Inter-Rater Reliability Is a Requirement, Not a Preference

**Claim type:** Direct

**CDFI mechanism:** kappa ≥ 0.60 publication gate

**Verbatim extract:**

> "Human evaluations can vary significantly depending on the characteristics of the human evaluators. Key factors that may influence someone's assessment include their level of creativity, motivation, and ability to identify potential flaws or issues with the system being tested."

*— Section: Challenges — A/B tests with crowdworkers*

> "Red teaming AI systems is presently more art than science; red teamers attempt to elicit concerning behaviors by probing models, but this process is not yet standardized. A robust and repeatable process is critical to ensure that red teaming accurately reflects model capabilities and establishes a shared baseline on which different models can be meaningfully compared."

*— Section: Challenges — Red teaming for national security*

**Inference chain to CDFI:**

The paper documents inter-rater inconsistency as a systematic problem across both human crowdworkers and expert red teamers. It identifies "a robust and repeatable process" as the requirement for evaluations that can "establish a shared baseline on which different models can be meaningfully compared." The CDFI's kappa threshold is the operationalization of that requirement for the automated judge: a score produced by a judge that cannot pass the consistency test is not part of a robust and repeatable process. It is part of the same problem the paper documents.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Metrics must measure what the domain requires | Direct | Yes | BBQ section |
| E2 — Domain-specific evaluation requires domain-specific investment | Direct | Yes | BBQ section |
| E3 — Generic benchmarks fail domain-specific contexts | Direct | Yes | Introduction; MMLU; HELM sections |
| E4 — Inter-rater reliability is a requirement | Direct | Yes | Crowdworkers; Red teaming sections |

All four evidence items are typed Direct. This is the most straightforwardly applicable of the seven source papers: the paper argues for evaluation rigor and domain-appropriate design; the CDFI operationalizes both. The inference chains from general evaluation principle to the specific Catholic authority-level architecture are Derived, but all derive from Direct claims.

---

*Full specification: [`docs/specifications/authority-levels.md`](../specifications/authority-levels.md)*

*Implementation: [`configs/authority_matrix.json`](../../configs/authority_matrix.json)*

*Claims pack (planned v1.5): [`claims/pub1-evaluation-criteria.json`](../../claims/pub1-evaluation-criteria.json)*

