# Translation 1 — Evaluation Criteria Must Match the Subject Matter

**Source Publication:** [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) — Anthropic, 2023
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

*Full specification: [docs/specifications/authority-levels.md](../specifications/authority-levels.md)*
*Implementation: [configs/authority_matrix.json](../../configs/authority_matrix.json)*
