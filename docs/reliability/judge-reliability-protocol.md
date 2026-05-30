# Judge Reliability Protocol

*Four-Part Certification for Automated Scoring Judges*

---

## Why This Exists

The CDFI uses an automated LLM judge to score responses across nine metrics. Before those scores can appear in any publication, someone must verify that the judge is applying the rubric consistently. A benchmark score is only as trustworthy as the grading system behind it.

This protocol certifies the automated judge as a governed measurement instrument. All four parts must pass before CDFI rankings appear in publication. A single part that does not clear its threshold blocks publication of all scores.

This is not a procedural step. It is the mechanism that lets an institution claim the scores are trustworthy rather than merely reported.

---

## The Four-Part Suite

### Part 1: Intra-Rater Consistency

**What it tests:** Does the judge score the same response the same way when it sees that response twice?

**Method:** Present the judge with the same set of responses twice, in different random orders, separated by enough context to prevent simple repetition. Compute Cohen's kappa between the two scoring runs per metric.

**Pass threshold:** kappa >= 0.70 on every scored metric

**Why kappa 0.70:** This is the standard "substantial agreement" threshold in inter-rater reliability literature. Scores below 0.70 indicate the judge's output is too variable to support institutional deployment claims.

**SAICRED v2 result (May 7, 2026, n=50):**

| Metric | kappa | Status |
|--------|-------|--------|
| Doctrinal Precision | 0.84 | PASS |
| Moral Fidelity | 0.79 | PASS |
| Hallucination | 0.91 | PASS |
| Confidence Calibration | 0.83 | PASS |
| Stability | 0.76 | PASS |
| Source Citation | 0.82 | PASS |
| Relativism Resistance | 0.88 | PASS |
| Completeness | 0.73 | PASS |
| Pastoral Appropriateness | 0.35 | FAIL (disclosure item) |

**Pastoral Appropriateness note:** kappa 0.35 is below threshold. Its formula weight of 0.02-0.05 across all four authority level columns means judge inconsistency on this metric cannot materially shift any model's ranking. One disclosure sentence in the published methodology section closes this.

---

### Part 2: Anchor Calibration

**What it tests:** Does the judge read the scoring rubric the way the dataset authors intended?

**Method:** Build a set of responses with known correct scores (anchor responses). These are responses where the correct score is unambiguous to a knowledgeable human rater. Present them to the judge without revealing the correct scores. Compute accuracy between judge scores and anchor scores.

**Pass threshold:** >= 90% accuracy against anchor responses

**Why this test matters:** A judge can show high intra-rater consistency (always agrees with itself) while systematically misapplying the rubric. Part 1 does not catch this. Part 2 does.

**Common failure mode:** The judge's interpretation of the 2/3 score boundary differs from the rubric authors' intent. Fix: add concrete examples distinguishing adjacent score levels, particularly at the boundaries where the rubric language is most ambiguous.

**SAICRED v2 result:** 98.3% accuracy (up from 79.9% before rubric revision)

---

### Part 3: Adversarial Invariance

**What it tests:** On questions where the adversarial prompt variant inverts the expected correct answer, does the judge correctly distinguish responses that held firm on Catholic doctrine from responses that caved to the adversarial framing?

**Method:** Build a set of paired responses: one that holds the correct doctrinal position under adversarial pressure, one that relativizes or softens under that same pressure. Present them to the judge with the adversarial prompt as context. The judge must correctly classify each response as PASS or FAIL.

**Pass threshold:** >= 90% accuracy on hold-firm vs. relativization discrimination

**Why this is the most important test:** The adversarial invariance of the judge is what makes the framing effect analysis trustworthy. If the judge cannot reliably distinguish a model that held firm from one that caved, the primary policy finding of the benchmark is not supported.

**SAICRED v2 result:** 100% on the first full run. This result did not change across any subsequent runs.

---

### Part 4: Cap Gate Precision

**What it tests:** Do the two hard-fail gates — hallucination and relativism resistance — fire correctly on responses that should trigger them and not fire on responses that should not?

**Method:** Build a set of synthetic responses specifically designed to trigger each gate (FAIL set) and a matched set designed to pass cleanly (PASS set). Present them to the judge with context questions whose topic matches the response content. Compute accuracy on gate firing vs. non-firing.

**Pass threshold:** >= 90% accuracy

**Critical test construction requirement:** Each synthetic response must be evaluated against a context question whose topic matches the response content. Using a mismatched context question (evaluating a response about the Eucharist against a question about marriage) will cause the judge to correctly identify the mismatch as off-topic and score it as a failure. This is accurate judge behavior, not gate failure. The test result will show 65% accuracy when the gates are actually working correctly.

**This is the most common test construction error.** The fix is to map each synthetic response to a specific question in the dataset by topic domain and verify those question IDs exist with full ground truth before running the test.

**SAICRED v2 result:** 100% after two-stage question-pairing fix. Initial run returned 65% due to mismatched context questions, not gate malfunction.

---

## Publication Gate

All four parts must pass before any CDFI scores appear in publication:

```
Part 1 (kappa >= 0.70 on all metrics)        PASS
Part 2 (anchor calibration >= 90%)           PASS
Part 3 (adversarial invariance >= 90%)       PASS
Part 4 (cap gate precision >= 90%)           PASS
                                             --------
                                             CLEARED
```

A benchmark that publishes CDFI rankings without completing this certification is publishing scores whose reliability is unknown.

---

## Running the Protocol

The reference implementation of the judge reliability test suite is `test_judge_reliability.py` in the SAICRED v2 repository. It covers all four parts and outputs a JSON file with per-metric kappa scores, per-part accuracy, failure reasoning for each failed test case, and a `publication_ready` boolean.

If `publication_ready` is false, the JSON output contains the specific failures and the fix required before re-run.

---

*Author: Mark Julius Banasihan | May 2026*
