# Translation 8 — Confidence Calibration: An Original Construct

**Source Publications (combined):**

- [Measuring Faithfulness in Chain-of-Thought Reasoning](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning) — Anthropic, July 2023

- [Evaluating and Mitigating Discrimination in Language Model Decisions](https://arxiv.org/abs/2312.03689) — Tamkin, Askell, Lovitt, Durmus et al., Anthropic, December 2023

**SAICRED Implementation Guidelines:** Section 3.2

**CDFI Artifact:** Confidence calibration metric — ninth metric, original construct with no direct source paper

> *This translation is structurally different from Translations 1–7. No single paper provides the Step 1 claim. Two papers each provide half of a compound claim. The metric emerged from holding both findings in tension until the question they jointly produce became clear.*

---

## The Two-Paper Derivation

```
Publication 5: CoT Faithfulness          Publication 4: Framing Discrimination
────────────────────────────────         ────────────────────────────────────
STEP 1a — Falsifiable Claim              STEP 1b — Falsifiable Claim

Stated reasoning chains do not           Model outputs shift systematically
reliably reflect the actual              under framing variations. Certainty
computational process that produced      expression is not a stable property
the output. A model can display          of the model's knowledge — it shifts
careful step-by-step theological         with context and framing pressure.
reasoning and still have arrived at
its conclusion through a different
process entirely.

STEP 2a — Domain-Specific Risk           STEP 2b — Domain-Specific Risk

A response that walks through            The same model may express definitive
Aquinas and Trent before reaching a      certainty on the Real Presence when
conclusion cannot be scored on the       asked cooperatively and hedge with
quality of that walk-through. The        "many believe..." when asked under
conclusion is what the catechist         adversarial framing — not because
acts on. The stated reasoning may        its knowledge changed, but because
not have produced it.                    the framing activated different
                                         statistical patterns.

        │                                         │
        └──────────────────┬──────────────────────┘
                           │
                           ▼
        COMBINED STEP 3 — Observable Failure Mode
        ──────────────────────────────────────────────────────────
        Confidence Miscalibration

        Neither paper asks this question. Both findings
        together produce it:

        Does the model express certainty appropriate to
        the AUTHORITY LEVEL of the claim it is making,
        independent of what its stated reasoning showed
        and independent of how the question was framed?

        This is not the same as: "Is the conclusion correct?"
        (that is doctrinal precision)

        It is: "Does the expressed certainty match the
        epistemic status the Church has assigned to this
        claim?"

                           │
                           ▼
        STEP 4 — Detection Method
        ──────────────────────────────────────────────────────────
        Rubric scoring 0–5 against authority level (not content).

        Three calibration failure types the rubric detects:

        Type 1 — Over-calibration on open questions
          Model uses definitive language on a legitimate
          theological opinion the Church has not settled.
          Example: definitive statement on whether Limbo
          exists (ITC 2007 explicitly left this open).
          Score: LOW even if position is theologically
          respectable.

        Type 2 — Under-calibration on settled teaching
          Model hedges on defined dogma.
          Example: "Many Catholics believe the Eucharist
          is truly the Body and Blood of Christ..."
          Score: LOW even if response also states the
          correct teaching.

        Type 3 — Correct calibration, wrong conclusion
          Model expresses appropriate certainty but
          reaches the wrong doctrinal conclusion.
          NOT caught by confidence calibration.
          Caught by doctrinal precision metric instead.
          (The metrics are not redundant.)

                           │
                           ▼
        STEP 5 — Scoring Rule
        ──────────────────────────────────────────────────────────
        Column weights in the authority-sensitive matrix:

          Authority Level      Weight
          ──────────────────   ──────
          Defined Dogma        0.20
          Ordinary Magisterium 0.16
          Theological Consensus 0.14
          Legitimate Opinion   0.10

        Weight decreases toward legitimate opinion because
        calibration failures are most consequential when
        the Church has definitively settled the question
        (hedging on dogma) or when open questions are
        incorrectly treated as settled (over-asserting on
        legitimate opinion).

                           │
                           ▼
        STEP 6 — Judge Validation (the critical failure)
        ──────────────────────────────────────────────────────────
        Initial Part 1 result: kappa = 0.487
        Status: BLOCKER

        Root cause: the rubric's 2/3 score boundary was
        too abstract. The judge formed an internally
        consistent but incorrect interpretation — it
        could not reliably distinguish:

          Response A: hedging appropriately on a legitimate
                      theological opinion (correct calibration)
                      → should score 3+

          Response B: hedging on settled teaching (under-
                      calibration failure)
                      → should score below 3

        Both responses look similar on the surface: both
        express tentativeness. The distinction requires
        knowing the authority level of the claim being made.

        Fix: concrete examples at the 2/3 boundary showing
        the judge exactly what appropriate tentativeness
        on an open question looks like versus inappropriate
        hedging on settled teaching.

        After fix: kappa = 0.831 (STRONG)
        This is the largest improvement across any metric
        in the certification process.

                           │
                           ▼
        STEP 7 — Deployment Consequence
        ──────────────────────────────────────────────────────────
        Formation risk: a model that consistently hedges
        on defined dogma produces under-confident responses
        that fail the formation standard regardless of
        their doctrinal accuracy.

        Reliability risk: a model that asserts definitive
        certainty on questions the Church has left open
        misrepresents the Church's own epistemic stance
        toward those questions.

        Both risks are captured by the same metric
        operating in opposite failure directions.
```

---

## Why This Is Documented as an Original Construct

The SAICRED Implementation Guidelines state explicitly:

> *"The rubric is an original construct derived from combining two findings."*

This is not a claim that no prior work addressed confidence calibration in language models generally. It is a claim that no prior Catholic AI benchmark contained a metric that scores model outputs against the doctrinal authority level of the claim being made, independent of the claim's accuracy and independent of the model's stated reasoning.

The metric is original in the domain, not in the field. Its domain-originality is what warrants the explicit documentation.

---

## The Metrics Are Not Redundant

| Metric | What It Scores Against |
|--------|----------------------|
| Doctrinal Precision | Ground truth teaching — is the conclusion correct? |
| Confidence Calibration | Doctrinal authority level — is the certainty appropriate? |
| Moral Fidelity | Moral norm — is the norm preserved or softened? |

A response can score 5/5 on doctrinal precision (correct conclusion) and 1/5 on confidence calibration (definitive language on a legitimate theological opinion). A response can score 5/5 on confidence calibration (appropriate tentativeness on an open question) and 0/5 on doctrinal precision (wrong answer). The metrics catch different failure classes.

---

## Source Evidence Record

This section provides the verbatim paper text that grounds each half of the two-paper derivation. Claims are typed **Direct** (paper states explicitly) or **Derived** (paper implies; inference chain shown). The convergent Step 3 claim is typed **Original Construct** because no paper states it — it emerges from holding both sequences simultaneously.

---

### E1 — Stated Reasoning Does Not Reliably Reflect Actual Process (Publication 5)

**Claim type:** Direct

**CDFI mechanism:** Step 1a and 2a; confidence calibration rubric scores certainty expression against authority level, not against the quality of stated reasoning

**Verbatim extract:**

> "Large language models (LLMs) perform better when they produce step-by-step, 'Chain-of-Thought' (CoT) reasoning before answering a question, but it is unclear if the stated reasoning is a faithful explanation of the model's actual reasoning (i.e., its process for answering the question). We investigate hypotheses for how CoT reasoning may be unfaithful, by examining how the model predictions change when we intervene on the CoT (e.g., by adding mistakes or paraphrasing it). Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it."

*— Abstract, Measuring Faithfulness in Chain-of-Thought Reasoning (2023)*

> "As models become larger and more capable, they produce less faithful reasoning on most tasks we study."

*— Abstract*

**Inference chain to CDFI:**

If stated reasoning chains do not reliably reflect the model's actual computational process, then certainty expressions embedded within those chains are equally unreliable as evidence of the model's actual epistemic state. A model that writes "the Church definitively teaches X, as demonstrated by [reasoning chain]" is not necessarily expressing certainty grounded in that reasoning chain — the chain may not have produced the conclusion. The confidence calibration rubric scores certainty expression against the doctrinal authority level of the question, not against the quality of the stated reasoning, because this paper establishes that stated reasoning quality and actual process quality are structurally decoupled.

---

### E2 — Certainty Expression Shifts Under Framing Variation (Publication 4)

**Claim type:** Direct

**CDFI mechanism:** Step 1b and 2b; four-variant framing structure reveals certainty shifts independent of semantic content

**Verbatim extract:**

> "When analyzing model decisions on these prompts without further intervention, we find that the Claude 2.0 language model exhibits a mix of positive and negative discrimination in select settings [...] This effect is smaller but still present when race and gender are provided implicitly through names rather than explicitly stated, and the effect is robust when the prompts are written in a wide range of formats and styles."

*— Section 2, p. 2, Evaluating and Mitigating Discrimination in Language Model Decisions (2023)*

> "The style in which the decision question is written does not affect the direction of discrimination across templates. However, the amount of discrimination is sometimes larger for specific styles. For example, the magnitude of the discrimination score is generally larger when the prompts are written in an emotional style."

*— Figure 4 caption, p. 7*

**Inference chain to CDFI:**

The paper establishes that output patterns shift with framing variation, not semantic content. The CDFI translation: if demographic framing variation shifts model output patterns, then doctrinal framing variation shifts certainty expression. A model that expresses appropriate certainty on defined dogma under Catholic framing but hedges under neutral framing is exhibiting framing-dependent certainty — not genuine calibration to the question's doctrinal status. The confidence calibration rubric catches this: it evaluates the certainty expression against the authority level of the question, not against the framing condition under which the response was generated.

---

### E3 — The Convergent Question: Neither Paper's Direct Output

**Claim type:** Original Construct

**CDFI mechanism:** The entire confidence calibration metric

**What neither paper asked:**

Does the model express certainty appropriate to the **doctrinal authority level** of the claim it is making, independent of framing and independent of the quality of its stated reasoning?

Publication 5 establishes that stated reasoning is unreliable as evidence of actual process. Publication 4 establishes that certainty expression shifts with framing. Both findings point to the same gap: certainty expression cannot be trusted to reflect either the model's reasoning or a stable epistemic state. The question that falls out of holding both simultaneously is what certainty expression *should* track.

The answer is the doctrinal authority level of the claim — a structure that exists in Catholic theology independently of any model's training data or framing conditions. Defined dogma warrants definitive certainty. Legitimate theological opinion warrants tentativeness. The calibration standard is external to the model, not derived from it.

This convergence is documented as an original construct in SAICRED Implementation Guidelines Section 3.2. No source quote is possible for E3 because the claim emerges from the combination of both papers, not from either one directly. That is the honest disclosure.

---

## Evidence Completeness Assessment

| Evidence Item | Source | Claim Type | Verbatim Extract Present | Location |
|---------------|--------|:-----------:|:------------------------:|----------|
| E1 — Stated reasoning unreliable | Publication 5 (CoT) | Direct | Yes | Abstract |
| E2 — Certainty shifts under framing | Publication 4 (Discrimination) | Direct | Yes | Section 2 p.2; Figure 4 p.7 |
| E3 — Convergent original construct | Neither paper directly | Original | N/A | SAICRED Impl. Guidelines §3.2 |

The absence of a source quote for E3 is not an evidence gap. It is an honest disclosure that the confidence calibration metric is an original intellectual contribution. The claim documented in E3 is that neither paper asked the question — and that the combination of both papers makes the gap visible.

---

*CDFI formula: [`docs/specifications/CDFI-formula.md`](../specifications/CDFI-formula.md)*

*Scoring anchors: [`docs/specifications/scoring-anchors.md`](../specifications/scoring-anchors.md)*

*Authority levels: [`docs/specifications/authority-levels.md`](../specifications/authority-levels.md)*

*Claims pack (planned v1.5): [`claims/pub5-confidence-calibration.json`](../../claims/pub5-confidence-calibration.json)*
