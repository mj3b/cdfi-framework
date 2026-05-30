# Translation 8 — Confidence Calibration: An Original Construct

**Source Publications:** [Measuring Faithfulness in Chain-of-Thought Reasoning](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning) (Anthropic, 2023) + [Discrimination in Language Model Decisions](https://arxiv.org/abs/2312.03689) (2024)
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

          Authority Level     Weight
          ─────────────────   ──────
          Defined Dogma       0.20
          Ordinary Magisterium 0.16
          Theological Consensus 0.14
          Legitimate Opinion  0.10

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

*SAICRED Implementation Guidelines, Section 3.2 (original rubric)*
*Authority levels: [docs/specifications/authority-levels.md](../specifications/authority-levels.md)*
