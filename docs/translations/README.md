# Translation Documents

**How Seven AI Safety Research Publications Became the CDFI**

*Mark Julius Banasihan | May 2026*

---

> These eight documents show the complete causal chain from each Anthropic AI safety research publication to the specific CDFI mechanism it produced. The translation methodology is documented in [`TRANSLATION-METHOD.md`](../../TRANSLATION-METHOD.md) at the root level.

---

## What a Translation Document Is

Each file in this folder answers one question: how did a specific research finding — written for general AI safety purposes — become a specific, computable, institution-grade scoring mechanism in the CDFI?

The answer has seven steps in every case. Each step takes the output of the previous step as its input:

```
Published Finding  →  Domain Risk  →  Failure Mode  →  Detection Method
                                                              ↓
Deployment Decision  ←  Judge Validation  ←  Scoring Rule
```

A finding that cannot complete all seven steps does not become a CDFI mechanism. This constraint is what makes the benchmark defensible rather than merely documented.

Each document also contains a **Source Evidence Record**: verbatim extracts from the source paper anchoring each step of the pipeline, with claim types marked as Direct (paper states explicitly) or Derived (paper implies; inference chain shown). Translation 8 marks its convergent claim as Original Construct, with an explicit disclosure that no source quote exists.

---

## The Eight Documents

### From Published Research (7 translations)

| File | Source Publication | CDFI Mechanism Produced |
|------|-------------------|------------------------|
| [01-evaluation-criteria.md](01-evaluation-criteria.md) | Challenges in Evaluating AI Systems (Anthropic, 2023) | Four-column authority-sensitive weighting matrix |
| [02-rubric-reliability.md](02-rubric-reliability.md) | Challenges in Evaluating AI Systems (Anthropic, 2023) | Four-part judge reliability certification; kappa ≥ 0.60 publication gate |
| [03-hallucination-gate.md](03-hallucination-gate.md) | Auditing Language Models for Hidden Objectives (Anthropic, 2025) | Hallucination pass/fail gate; `CAP_VALUE = 40` |
| [04-statistical-rigor.md](04-statistical-rigor.md) | A Statistical Approach to Model Evaluations (Anthropic, 2024) | 95% CI; clustered SE; deployment tier thresholds; temporal versioning |
| [05-framing-sensitivity.md](05-framing-sensitivity.md) | Discrimination in Language Model Decisions (Anthropic, 2023) | Four-variant prompt structure; relativism resistance gate |
| [06-adversarial-probing.md](06-adversarial-probing.md) | Evaluating Feature Steering (Anthropic, 2024) | Adversarial prompt variant; prompt sensitivity drift failure mode |
| [07-categorical-failures.md](07-categorical-failures.md) | Sabotage Evaluations (Anthropic, 2024) | Five failure mode taxonomy; cap gate architecture |

> *Publication 1 (Challenges in Evaluating AI Systems) produced two separate mechanisms — the weighting matrix and the reliability gate — that are architecturally distinct enough to warrant separate translation documents (01 and 02).*

---

### From Original Construction (1 document)

| File | Derived From | CDFI Mechanism Produced |
|------|-------------|------------------------|
| [08-confidence-calibration.md](08-confidence-calibration.md) | Publications 4 + 5 combined | Confidence calibration metric — ninth metric, original construct |

Translation 8 is structurally different from the others. No single paper provides the Step 1 claim. Publications 4 and 5 each provide half of a compound claim. The metric emerged from holding both findings in tension simultaneously. The SAICRED Implementation Guidelines document this explicitly: *"The rubric is an original construct derived from combining two findings."*

---

## How to Read These Documents

| Audience | Start Here |
|----------|-----------|
| **Researcher evaluating the methodology** | [`TRANSLATION-METHOD.md`](../../TRANSLATION-METHOD.md) — the seven-step sequence, then any individual translation to see it applied |
| **AI safety researcher verifying paper derivations** | The Source Evidence Record at the end of each translation document — verbatim extracts with section/page citations, Direct/Derived claim typing, and explicit inference chains for all Derived steps |
| **Building a benchmark for another tradition** | [`05-framing-sensitivity.md`](05-framing-sensitivity.md) and [`07-categorical-failures.md`](07-categorical-failures.md) — the two mechanisms most likely to require adaptation. Then [`docs/governance/adapting-for-other-traditions.md`](../governance/adapting-for-other-traditions.md) |
| **Peer reviewer checking v2 data claims** | All figures verified against `cdfi_scores_full.csv`, `scores_full.csv`, `pairwise_significance.csv`, `confidence_intervals.csv`. Exact outputs from Naveen Kumar Puppala's scoring pipeline — not rounded estimates |
| **Catholic institution making a deployment decision** | [`04-statistical-rigor.md`](04-statistical-rigor.md) for why rank-order positions 2–5 are directionally informative but not statistically reliable. [`05-framing-sensitivity.md`](05-framing-sensitivity.md) for the framing effect finding — the most practically actionable output of the benchmark |

---

## Relationship to Other Repository Documents

| Document | Relationship |
|----------|-------------|
| [`TRANSLATION-METHOD.md`](../../TRANSLATION-METHOD.md) | Defines the seven-step methodology these files apply |
| [`TRACEABILITY.md`](../../TRACEABILITY.md) | Summary table: all seven publications → mechanisms in one view |
| [`docs/specifications/`](../specifications/) | The full technical specifications the translations produced |
| [`configs/`](../../configs/) | The numerical parameters (weights, gates, tiers) the translations specified |
| [`engine/cdfi_calculator.py`](../../engine/cdfi_calculator.py) | The reference implementation of the scoring rules the translations defined |

---

*DOI: [10.5281/zenodo.20467497](https://doi.org/10.5281/zenodo.20467497)*

*ORCID: [0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)*
