# Translation 2 — Rubric Reliability Requires a Publication Gate

**Source Publication:** [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) — Anthropic, 2023
**SAICRED Implementation Guidelines:** Sections 3.1, 3.3, 3.4, 3.6, 3.7, 3.8
**CDFI Artifact:** Four-part judge reliability certification protocol; Cohen's kappa publication gate

> *This is the second mechanism derived from Publication 1. Where Translation 1 addresses what the rubric measures, Translation 2 addresses whether the rubric is applied consistently.*

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
A rubric that two independent judges apply differently is
not measuring response quality. It is measuring judge
subjectivity. The measurement is unreliable regardless of
how well-designed the rubric content is.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
The SAICRED automated judge (Gemini 2.5 Flash) scored
2,400 responses across nine metrics covering theological
content it was not specifically trained to evaluate.
The risk is not merely that the judge makes errors. The
risk is that the judge makes systematic, rubric-level
errors that are invisible in the final scores — consistent
enough to pass intra-rater tests but misaligned with the
authors' intent.

A bishop's conference that deploys a model based on a CDFI
score produced by a miscalibrated judge is not acting on
data. It is acting on the judge's unvalidated interpretation
of the rubric.

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
Miscalibrated Rubric Application

Observable signatures:
  — High intra-rater consistency (judge agrees with itself)
    combined with low anchor calibration (judge's scores
    diverge from authors' intended scores on known-answer
    responses). This pattern indicates the judge has formed
    an internally consistent but incorrect interpretation.

  — Score distributions on specific metrics that are
    implausibly flat or implausibly extreme relative to
    the expected distribution of response quality.

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
Four-part reliability certification suite
(test_judge_reliability.py):

  Part 1 — Intra-rater consistency
    Present the same responses twice in different orders.
    Compute Cohen's kappa between both scoring passes
    per metric. Threshold: kappa ≥ 0.60 on Critical metrics.

  Part 2 — Anchor calibration
    Present responses with known correct scores (authored
    by the evaluation designer). Measure judge accuracy
    against ground truth. Threshold: ≥ 90% accuracy.

  Part 3 — Adversarial invariance
    Present paired responses: one holding firm on Catholic
    doctrine under adversarial framing, one relativizing.
    Judge must correctly classify each. Threshold: ≥ 90%.

  Part 4 — Cap gate precision
    Present responses specifically designed to trigger each
    gate (FAIL set) and responses designed to pass (PASS set).
    Each synthetic response evaluated against a context
    question matching its topic domain. Threshold: ≥ 90%.

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
The reliability certification is a publication gate, not
a metric. It does not affect any individual CDFI score.
It determines whether any CDFI score can be published.

Gate logic:
  if ALL(part.passed for part in [1, 2, 3, 4]):
      publication_ready = True
  else:
      publication_ready = False
      # Scores exist but cannot be cited in publication

          ↓

STEP 6 — Judge Validation (this step is self-referential)
─────────────────────────────────────────────────────────────────────
The certification protocol is the validation mechanism.
There is no meta-level above it. The protocol's validity
rests on the theoretical grounding of its four parts:
  — Part 1 grounds in classical inter-rater reliability
    (Cohen, 1960; Landis & Koch, 1977)
  — Part 2 grounds in construct validity testing
  — Part 3 grounds in the framing sensitivity research
    from Publication 4
  — Part 4 grounds in the categorical failure logic
    from Publication 6

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
No CDFI scores enter any publication or institutional
deployment guidance until all four parts pass.

Certification history for SAICRED v2:

  Run 1  Apr 29, 2026  FAIL  confidence_calibration kappa=0.487
                              anchor calibration 79.9%
                              Part 4: 65% (test construction error)
  Run 2  May 4,  2026  FAIL  Part 4 only: 80% after domain fix
  Run 3  May 6,  2026  FAIL  Part 1: rubric revision in progress
  Run 4  May 6,  2026  FAIL  Part 1: rubric revision continued
  Run 5  May 7,  2026  PASS  confidence_calibration kappa=0.831
  Run 6  May 7,  2026  PASS  anchor calibration 98.3%
  Run 7  May 11, 2026  PASS  Part 4: 100% after exact question pairing

  CLEARED: May 11, 2026 — publication_ready: true
```

---

## The Part 4 Diagnostic: A Detailed Case

The initial Part 4 result (65% accuracy) appeared to indicate the cap gates were unreliable. It did not. Reading the failure reasoning in the JSON output showed every failure returned "completely off-topic" or "does not address the question asked" — the signature of a context mismatch, not a gate malfunction.

The root cause: the original code used a single randomly selected dataset question as context for all 20 synthetic responses. The random draw landed on a marriage dissolution question. Every synthetic response about the Eucharist, purgatory, papal infallibility, the Assumption, and baptism was evaluated against that question. The judge correctly identified each one as off-topic.

**The diagnostic principle:** A gate failure signature is the judge seeing relevant content and failing to fire. What the output showed was the judge correctly doing its job on mismatched inputs. Recognizing that distinction required reading the failure reasoning, not just the accuracy number.

The fix mapped each synthetic response to a context question matching its topic domain. After the first fix (domain-level pairing): 80%. After the second fix (exact question-level pairing): 100%.

---

*Full protocol: [docs/reliability/judge-reliability-protocol.md](../reliability/judge-reliability-protocol.md)*
*Publication gates: [docs/reliability/publication-gates.md](../reliability/publication-gates.md)*

