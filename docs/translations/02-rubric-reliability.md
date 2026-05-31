# Translation 2 — Inter-Rater Reliability Is a Publication Gate, Not a Quality Preference

**Source Publication:** [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) — Anthropic, October 2023

**SAICRED Implementation Guidelines:** Section 3.6

**CDFI Artifacts Produced:** Cohen's kappa ≥ 0.60 publication gate; four-part certification protocol structure; Part 1 (intra-rater consistency) requirement

---

> **How to read this document.** Translation 1 drew the weighting matrix architecture from this
> same paper. This document draws the separate contribution: the reliability certification
> protocol and the kappa threshold that must clear before any scores enter publication.
> Both translations come from Publication 1. They are separated because they address different
> architectural problems.

---

## Why This Paper (Second Translation)

The paper documents the human evaluator case explicitly: crowdworker evaluations "can vary
significantly depending on the characteristics of the human evaluators." The inference to
automated judge evaluation is one step: if human raters with explicit instructions produce
inconsistent results, an automated judge applying a rubric without calibration will produce
inconsistent results at scale and no one will notice. The reliability certification protocol
is the mechanism that catches this before publication.

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
A rubric is only as good as the consistency with which it is applied.
If two independent evaluations of the same response produce different
scores, the rubric is measuring evaluator subjectivity rather than
response quality. Consistency is a necessary (not sufficient) condition
for a rubric to be a valid measurement instrument.

Claim type: DERIVED
The paper establishes this through the crowdworker case and the BBQ
calibration failure. The inference to automated judge certification
is one step from the paper's demonstrated principle.

See Source Evidence Record: E1, E2.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
SAICRED v2 uses Gemini 2.5 Flash as the automated judge for 21,599
metric scores across 6 models. If the judge applies rubrics
inconsistently, the CDFI rankings reflect judge noise as much as model
behavior. Publishing those rankings without certification would produce
the Catholic institutional equivalent of Anthropic's BBQ zero-bias
result: numbers that look like findings but are measuring the wrong
thing.

Claim type: DERIVED

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
Judge inconsistency failure: the same response receives materially
different scores on repeated evaluation. Detectable by Cohen's kappa —
agreement between two independent scoring runs on the same response set.

Anchor miscalibration failure: the judge applies rubric levels in ways
that diverge from the authors' intent. Detectable by comparing judge
scores to expert-scored anchor responses.

Claim type: DIRECT (failure characterization) / DERIVED (CDFI application)

See Source Evidence Record: E1.

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
Part 1 — Intra-rater consistency:
  Score the same set of 50 responses twice under identical conditions.
  Compute Cohen's kappa per metric.
  Threshold: kappa ≥ 0.60 on all Critical metrics before publication.

Part 2 — Anchor calibration:
  Score a set of responses with known expert-assigned scores.
  Compare judge scores to expert scores.
  Threshold: ≥ 90% accuracy before publication.

Both parts are publication gates. Parts 3 and 4 test separate properties.

Claim type: DIRECT (design rationale) / DERIVED (implementation)

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
Publication gate (docs/reliability/publication-gates.md):

  All four parts of the judge reliability certification must pass before
  any CDFI scores appear in publication. A score produced by an
  uncertified judge is preliminary data, not a CDFI result.

  The kappa threshold is 0.60, not 0.70. This was a deliberate choice
  calibrated against what is achievable for subjective theological
  metrics versus a higher standard applied in other domains.
  confidence_calibration's initial kappa of 0.487 blocked publication
  and required rubric revision before clearing at 0.831.

Claim type: DERIVED (threshold calibration)

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
This step is self-referential for Translation 2: the certification
protocol IS the mechanism. The validation loop closes when all four
parts pass.

SAICRED v2 certification history:
  Run 1  Apr 29, 2026  FAIL  confidence_calibration kappa = 0.487
  Run 5  May 7,  2026  PASS  kappa = 0.831 after rubric revision
  Run 6  May 7,  2026  PASS  anchor calibration 98.3%
  Run 7  May 11, 2026  PASS  cap gate precision 100%

  All four parts cleared: May 11, 2026

The confidence_calibration failure was a rubric problem, not a metric
design problem. The 2/3 score boundary was too abstract. Adding concrete
examples distinguishing appropriate tentativeness on open questions from
inappropriate hedging on settled teaching moved kappa from 0.487 to
0.831. This is the BBQ calibration failure in miniature: the rubric was
producing numbers that looked like scores but were measuring something
other than what was intended.

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
Pastoral appropriateness kappa = 0.352 (below threshold).
This is LIMITATIONS.md L3:

  Pastoral appropriateness is not a publication blocker because its
  weight in the CDFI formula is 0.02 to 0.05 across all authority
  columns. Judge inconsistency on this metric has negligible impact
  on rankings. The limitation is disclosed, not suppressed.

  If pastoral appropriateness weight were raised to match the weight
  of doctrinal precision, the kappa failure would require resolution
  before publication. The disclosure standard is proportionate to the
  metric's influence on the index.
```

---

## Source Evidence Record

---

### E1 — Human Evaluator Consistency Is Not Automatic

**Claim type:** Direct

**CDFI mechanism:** Intra-rater consistency certification requirement

**Verbatim extract:**

> "Human evaluations can vary significantly depending on the characteristics of the human
> evaluators. Key factors that may influence someone's assessment include their level of
> creativity, motivation, and ability to identify potential flaws or issues with the system
> being tested."

*— Section: Challenges — A/B tests with crowdworkers*

> "There is an inherent tension between helpfulness and harmlessness. A system could avoid
> harm simply by providing unhelpful responses like 'sorry, I can't help you with that'.
> What is the right balance between helpfulness and harmlessness? What numerical value
> indicates a model is sufficiently helpful and harmless?"

*— Section: Challenges — A/B tests with crowdworkers*

**Inference chain to CDFI:**

The paper establishes that even human evaluators with structured guidelines produce
inconsistent results on open-ended quality judgments. The inference to automated judge
certification: if human evaluators require calibration protocols, an automated judge applying
a structured rubric at scale requires the same — and the calibration must be verified, not
assumed. Part 1 of the CDFI certification protocol (intra-rater consistency) is that
verification.

---

### E2 — Calibration Must Be Verified Against Intent, Not Assumed

**Claim type:** Direct

**CDFI mechanism:** Part 2 anchor calibration requirement

**Verbatim extract:**

> "All evaluations are subject to the failure mode where you overinterpret the quantitative
> score and delude yourself into thinking that you have made progress when you haven't."

*— Section: Challenges — BBQ*

> "We were convinced that BBQ provides a good measurement of social biases only after
> implementing and comparing BBQ against several similar evaluations. This effort took us
> months."

*— Section: Challenges — BBQ*

**Inference chain to CDFI:**

The paper's lesson is that calibration confidence must be earned through comparison against
known-correct results, not assumed from implementation completeness. Part 2 of the CDFI
certification (anchor calibration against expert-scored responses) operationalizes this
lesson: the judge's interpretation of the rubric is verified against a reference standard
before scores enter publication.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Human evaluator consistency not automatic | Direct | Yes | Crowdworker section |
| E2 — Calibration must be verified against intent | Direct | Yes | BBQ section |

---

*Reliability protocol: [`docs/reliability/judge-reliability-protocol.md`](../reliability/judge-reliability-protocol.md)*

*Publication gates: [`docs/reliability/publication-gates.md`](../reliability/publication-gates.md)*

*Claims pack (planned v1.5): [`claims/pub1-rubric-reliability.json`](../../claims/pub1-rubric-reliability.json)*
