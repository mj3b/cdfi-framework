# Translation 1 — Domain-Specific Evaluation Criteria Require Domain-Specific Rubrics

**Source Publication:** [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) — Anthropic, October 2023

**SAICRED Implementation Guidelines:** Sections 3.1, 3.4, 3.6

**CDFI Artifacts Produced:** Four-column authority-sensitive weighting matrix; inter-rater reliability publication gate (kappa ≥ 0.60); human expert calibration requirement

---

> **How to read this document.** The Translation Pipeline shows the seven-step sequence that
> converted this paper's findings into computable CDFI mechanisms. The Source Evidence Record
> provides verbatim paper text anchoring each claim. Claims are typed **Direct** (paper states
> explicitly) or **Derived** (paper implies; inference chain is shown).

---

## Why This Paper

This is not a paper about doctrinal evaluation. It is a practitioner account of what goes wrong when
evaluation systems are built without domain grounding. Anthropic's engineers discovered that MMLU
formatting changes produce ~5% accuracy swings, that BBQ bias scores can show zero bias when the
model is not answering questions at all, and that BIG-bench is so unwieldy that major labs abandon
it. The paper's contribution to CDFI is not any specific finding. It is the diagnosis: evaluation
criteria drawn from generic frameworks systematically fail to detect domain-specific failure modes.
That diagnosis is why the CDFI has four authority columns instead of one.

---

## Translation Pipeline

```
STEP 1 — Falsifiable Claim
─────────────────────────────────────────────────────────────────────
Evaluation criteria drawn from generic benchmarks systematically fail
to detect domain-specific failure modes. A rubric designed for general
knowledge tasks will measure something coherent in that context and
something incoherent in a domain with a structured authority hierarchy.

Claim type: DERIVED
The paper does not state this in domain-general terms. It demonstrates
the failure empirically through four case studies (MMLU, BBQ, BIG-bench,
HELM) and concludes that "robust evaluations are extremely difficult to
develop and implement." The inference that authority-level sensitivity
requires domain-specific rubric architecture is the CDFI translation.

See Source Evidence Record: E1, E2, E3.

          ↓

STEP 2 — Domain-Specific Risk
─────────────────────────────────────────────────────────────────────
Catholic doctrine is not a flat list of equally certain claims. The Real
Presence is defined dogma. Whether Limbo exists is a legitimate
theological opinion. A scoring instrument that applies the same weights
to both is measuring something incoherent — exactly the failure the
paper documents in MMLU applying the same accuracy metric across
57 tasks of vastly different structure.

Claim type: DERIVED
The Catholic authority hierarchy is an original translation. The paper's
BBQ case study (zero bias when the model is not answering) is the
structural analogy: measuring the wrong thing with consistency is worse
than measuring nothing, because it produces false confidence.

See Source Evidence Record: E2.

          ↓

STEP 3 — Observable Failure Mode
─────────────────────────────────────────────────────────────────────
Doctrinal Omission (gradational): a response accurate as far as it goes
but missing elements required by the authority level of the question.
Miscalibrated Rubric Application: a judge applying a rubric designed for
one authority level to a question at a different authority level.

The second failure mode is upstream of scoring. It produces systematic
measurement error before any metric is applied.

Claim type: DERIVED

          ↓

STEP 4 — Detection Method
─────────────────────────────────────────────────────────────────────
Four-column weighting matrix keyed to doctrinal authority level:

  Column 1: Defined Dogma          (doctrinal precision weight: 0.30)
  Column 2: Ordinary Magisterium   (doctrinal precision weight: 0.26)
  Column 3: Theological Consensus  (doctrinal precision weight: 0.20)
  Column 4: Legitimate Opinion     (doctrinal precision weight: 0.15)

Each question is tagged with its authority level before scoring. The
judge applies the column matching the question's tag. Different weights
reflect what matters most at each authority level.

Claim type: DERIVED
The four-column architecture is a CDFI original. The paper established
that domain-specific structure matters; the Catholic authority taxonomy
is the domain-specific structure.

See Source Evidence Record: E3.

          ↓

STEP 5 — Scoring Rule
─────────────────────────────────────────────────────────────────────
Column weights in configs/authority_matrix.json.
All columns sum to 1.00.

Authority level tag required at intake before scoring proceeds (Section
3.1 of SAICRED Implementation Guidelines). All 400 SAICRED v2 prompts
defaulted to ordinary_magisterium pending theological advisor
classification — the reason v2 rankings are preliminary.

          ↓

STEP 6 — Judge Validation
─────────────────────────────────────────────────────────────────────
Part 2 — Anchor calibration:
  The judge is tested against a set of expert-scored responses to verify
  it reads the rubric as the authors intended, not as it interprets it.

  The paper's BBQ finding drove this requirement directly: zero bias when
  the model is not answering is a calibration failure the authors only
  caught because one developer asked whether models were answering at all.
  Calibration testing catches the equivalent failure in the judge.

  SAICRED v2 result: 98.3% accuracy (Parts 2 cleared May 7, 2026).

Claim type: DIRECT (design logic) / DERIVED (implementation)

See Source Evidence Record: E2.

          ↓

STEP 7 — Deployment Consequence
─────────────────────────────────────────────────────────────────────
Authority level classification is a publication gate (LIMITATIONS.md L1):

  All 400 SAICRED v2 prompts used ordinary_magisterium default.
  Final CDFI requires theological advisors to classify each prompt.
  Rankings are valid but preliminary until classification is complete.

  Pipeline reads authority_level at runtime. No code changes required
  when classification is applied. Rankings will shift. Magnitude unknown
  until classification is done.
```

---

## Source Evidence Record

---

### E1 — Generic Evaluation Criteria Fail Domain-Specific Contexts

**Claim type:** Direct

**CDFI mechanism:** Authority-level sensitivity in rubric design

**Verbatim extract:**

> "We have found four minor but important challenges with MMLU that are relevant to other
> multiple-choice evaluations: [...] Simple formatting changes to the evaluation, such as
> changing the options from (A) to (1) or changing the parentheses from (A) to [A], or adding
> an extra space between the option and the answer can lead to a ~5% change in accuracy on
> the evaluation."

*— Section: Challenges — MMLU*

> "We want readers of this post to have two main takeaways: robust evaluations are extremely
> difficult to develop and implement, and effective AI governance depends on our ability to
> meaningfully evaluate AI systems."

*— Introduction*

**Inference chain to CDFI:**

If simple formatting changes produce 5% accuracy swings in a general benchmark, a benchmark
applied across questions of radically different doctrinal authority levels — without adjusting
weights — will produce accuracy measurements that reflect rubric mismatch as much as model
behavior. The four-column CDFI weighting matrix addresses this by making the authority level
explicit and structuring scoring accordingly.

---

### E2 — Zero Score May Mean Wrong Measurement, Not Good Performance

**Claim type:** Direct

**CDFI mechanism:** Part 2 anchor calibration requirement

**Verbatim extract:**

> "After implementing BBQ, our results showed that some of our models were achieving a bias
> score of 0, which made us feel optimistic that we had made progress on reducing biased model
> outputs. When we shared our results internally, one of the main BBQ developers (who works at
> Anthropic) asked if we had checked a simple control to verify whether our models were answering
> questions at all. We found that they weren't — our results were technically unbiased, but they
> were also completely useless."

*— Section: Challenges — BBQ*

> "All evaluations are subject to the failure mode where you overinterpret the quantitative
> score and delude yourself into thinking that you have made progress when you haven't."

*— Section: Challenges — BBQ*

**Inference chain to CDFI:**

The BBQ failure is a calibration failure: the measurement instrument was producing numbers
that looked correct but were measuring the wrong thing. Part 2 of the CDFI judge certification
(anchor calibration) exists specifically to catch this failure mode — verifying that the judge's
rubric interpretation matches the authors' intent before any scores enter the benchmark.

---

### E3 — Domain-Specific Evaluations Require Domain-Specific Implementation Effort

**Claim type:** Direct

**CDFI mechanism:** Human expert calibration; authority level classification requirement

**Verbatim extract:**

> "Implementing BBQ was more difficult than we anticipated. We could not find a working
> open-source implementation of BBQ that we could simply use 'off the shelf' [...] it took
> one of our best full-time engineers one uninterrupted week to implement and test the
> evaluation."

*— Section: Challenges — BBQ*

> "Determining which tasks were most important and representative would have required running
> all 204 tasks, validating results, and extensively analyzing output — a substantial research
> undertaking, even for an organization with significant engineering resources."

*— Section: Challenges — BIG-bench*

**Inference chain to CDFI:**

The paper establishes that serious domain-specific evaluation requires serious investment in
getting the rubric right before running it at scale. The CDFI's pre-scoring requirement —
theological advisor classification of all prompts before final rankings are published — follows
this principle. Running the pipeline without correct authority level tags produces numbers that
look like CDFI scores but are not comparable to final CDFI scores. The preliminary/final
distinction in LIMITATIONS.md L1 exists because this paper documented exactly what happens
when that investment is skipped.

---

## Evidence Completeness Assessment

| Evidence Item | Claim Type | Verbatim Extract Present | Location Verified |
|---------------|:-----------:|:------------------------:|:-----------------:|
| E1 — Generic criteria fail domain-specific contexts | Direct | Yes | MMLU section |
| E2 — Zero score may mean wrong measurement | Direct | Yes | BBQ section |
| E3 — Domain-specific effort required | Direct | Yes | BBQ, BIG-bench sections |

---

*Weighting matrix: [`configs/authority_matrix.json`](../../configs/authority_matrix.json)*

*Authority levels: [`docs/specifications/authority-levels.md`](../specifications/authority-levels.md)*

*Claims pack (planned v1.5): [`claims/pub1-evaluation-criteria.json`](../../claims/pub1-evaluation-criteria.json)*

