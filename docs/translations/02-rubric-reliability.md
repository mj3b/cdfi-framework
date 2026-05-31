# Translation 2 — Rubric Reliability Requires a Publication Gate

**Source Publication:** [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) — Ganguli, Schiefer, Favaro, Clark, Anthropic, October 4, 2023

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

## Why Two Translations from One Paper

Translation 1 and Translation 2 address different architectural problems derived from the same paper.

Translation 1 extracts the domain-specificity finding: evaluation criteria must match the domain's own authority structure. This produces the four-column weighting matrix.

Translation 2 extracts the evaluator consistency finding: a rubric that independent evaluators apply differently is measuring subjectivity, not response quality. This produces the four-part certification protocol.

The two translations are not redundant. A rubric can be correctly designed for its domain (Translation 1 satisfied) and still be applied inconsistently by the judge (Translation 2 failing). The confidence calibration metric passed the domain-design test on its first design iteration. It failed the consistency test (kappa = 0.487) until the 2/3 score boundary was anchored with concrete examples. Both conditions must be satisfied before a score is defensible.

---

## Source Evidence Record

This section provides the verbatim paper text that anchors each step of the translation pipeline above. Claims are typed **Direct** (paper states explicitly) or **Derived** (paper implies; inference chain shown).

---

### E1 — Evaluator Consistency Is Not Automatic

**Claim type:** Direct

**CDFI mechanism:** Part 1 intra-rater consistency requirement; kappa threshold

**Verbatim extract:**

> "Human evaluations can vary significantly depending on the characteristics of the human evaluators. Key factors that may influence someone's assessment include their level of creativity, motivation, and ability to identify potential flaws or issues with the system being tested."

*— Section: Challenges — A/B tests with crowdworkers*

> "There is an inherent tension between helpfulness and harmlessness. A system could avoid harm simply by providing unhelpful responses like 'sorry, I can't help you with that'. What is the right balance between helpfulness and harmlessness? What numerical value indicates a model is sufficiently helpful and harmless? What high-level norms or values should we test for above and beyond helpfulness and harmlessness?"

*— Section: Challenges — A/B tests with crowdworkers*

**Inference chain to CDFI:**

The paper establishes that even human evaluators applying structured guidelines produce inconsistent results on open-ended quality judgments. The inference to automated judge certification: an automated judge applying a rubric at scale requires the same consistency verification — and the verification must be demonstrated, not assumed. Part 1 of the CDFI certification protocol (intra-rater consistency via Cohen's kappa) is that demonstration.

---

### E2 — Calibration Against Intent Must Be Verified, Not Assumed

**Claim type:** Direct

**CDFI mechanism:** Part 2 anchor calibration requirement; 98.3% accuracy result

**Verbatim extract:**

> "After implementing BBQ, our results showed that some of our models were achieving a bias score of 0, which made us feel optimistic that we had made progress on reducing biased model outputs. When we shared our results internally, one of the main BBQ developers (who works at Anthropic) asked if we had checked a simple control to verify whether our models were answering questions at all. We found that they weren't — our results were technically unbiased, but they were also completely useless."

*— Section: Challenges — BBQ*

> "All evaluations are subject to the failure mode where you overinterpret the quantitative score and delude yourself into thinking that you have made progress when you haven't."

*— Section: Challenges — BBQ*

**Inference chain to CDFI:**

The BBQ failure is a calibration failure: the measurement instrument was producing numbers that looked correct while measuring the wrong thing — and nobody knew until someone asked whether the models were answering at all. Part 2 of the CDFI certification (anchor calibration against expert-scored responses) exists specifically to catch this failure mode before scores enter publication. The first SAICRED v2 reliability run returned 79.9% anchor accuracy — meaning the judge was applying the rubric in a way that diverged from the authors' intent on approximately 1 in 5 responses. The fix (restructured anchor text format) brought calibration to 98.3%.

---

### E3 — Repeatability Requires Standardized Process

**Claim type:** Direct

**CDFI mechanism:** Seven-run certification history; publication gate architecture

**Verbatim extract:**

> "Red teaming AI systems is presently more art than science; red teamers attempt to elicit concerning behaviors by probing models, but this process is not yet standardized. A robust and repeatable process is critical to ensure that red teaming accurately reflects model capabilities and establishes a shared baseline on which different models can be meaningfully compared."

*— Section: Challenges — Red teaming for national security*

> "We were convinced that BBQ provides a good measurement of social biases only after implementing and comparing BBQ against several similar evaluations. This effort took us months."

*— Section: Challenges — BBQ*

**Inference chain to CDFI:**

The paper identifies "a robust and repeatable process" as the specific requirement for evaluations that can support comparative claims across models. The CDFI certification protocol is the operationalization of this requirement: a seven-run history with documented results, named failure modes, and specific fixes for each failure. The publication gate ensures that scores only enter comparative use after that repeatable process has cleared. The seven-run history in the STEP 7 pipeline above is not a sign of failure — it is the evidence that the process is robust.

---

### E4 — Third-Party Evaluation Requires Collaboration, Not Just Independence

**Claim type:** Direct

**CDFI mechanism:** Independent execution by Lead Engineer (Naveen) as certification requirement

**Verbatim extract:**

> "Providing full-time assistance diverted resources from internal evaluation efforts. When doing this audit, we realized that the relationship between auditors and those being audited poses challenges that must be navigated carefully. Auditors typically limit details shared with auditees to preserve evaluation integrity. However, without adequate information the evaluated party may struggle to address underlying issues when crafting technical evaluations."

*— Section: Preserving the objectivity of third-party audits*

> "After seeing the final audit report, we realized that we could have helped ARC be more successful in identifying concerning behavior if we had known more details about their (clever and well-designed) audit approach."

*— Section: Preserving the objectivity of third-party audits*

**Inference chain to CDFI:**

The paper identifies the tension between independence (needed for objectivity) and collaboration (needed to execute the evaluation correctly). The CDFI certification resolves this by separating roles clearly: the Evals Expert designed the protocol; Naveen Kumar Puppala executed it independently in a separate environment with proven quota and no interruptions. Independence is preserved at the execution level; the design documentation is fully shared so execution can be done correctly. This is the collaboration structure the paper recommends but could not implement with ARC.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Evaluator consistency not automatic | Direct | Yes | Crowdworkers section |
| E2 — Calibration against intent must be verified | Direct | Yes | BBQ section |
| E3 — Repeatability requires standardized process | Direct | Yes | Red teaming; BBQ sections |
| E4 — Independent execution with shared design | Direct | Yes | Third-party audits section |

All four evidence items are typed Direct. The inference chains from general evaluation principle to the specific CDFI certification architecture are Derived, but each derives from a Direct claim in the paper.

---

*Full protocol: [`docs/reliability/judge-reliability-protocol.md`](../reliability/judge-reliability-protocol.md)*

*Publication gates: [`docs/reliability/publication-gates.md`](../reliability/publication-gates.md)*

*Claims pack (planned v1.5): [`claims/pub1-rubric-reliability.json`](../../claims/pub1-rubric-reliability.json)*
