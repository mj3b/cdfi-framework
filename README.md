# CDFI Framework
### A Methodology for Domain-Specific AI Doctrinal Evaluation

**Catholic Doctrinal Fidelity Index — Evaluation Governance Infrastructure**

*Author: Mark Julius Banasihan*

*May 2026*

---

> **The problem this framework solves:** General-purpose AI benchmarks measure capability. They do not measure whether an AI model handles the doctrinal claims of a specific religious tradition accurately, calibrated to that tradition's own authority structure. This framework does.

---

## What This Is

The CDFI Framework is a reusable evaluation governance methodology for building domain-specific AI doctrinal benchmarks. It was derived from seven frontier AI safety research publications and translated into a scoring architecture purpose-built for Catholic doctrinal evaluation. SAICRED v2 is the reference implementation.

The framework is the first of its kind: a published, version-controlled methodology that any religious institution or denomination can adapt to evaluate AI models against its own doctrinal standards.

**It is not a benchmark.** It is the methodology that makes a benchmark defensible.

---

## The Core Sequence

Every benchmark built on this framework follows seven steps in order. Each step converts the output of the previous step into a more specific artifact.

```
Literature Claim
      ↓
Risk Mechanism
      ↓
Observable Failure Mode
      ↓
Metric or Gate
      ↓
Scoring Rule
      ↓
Reliability Test
      ↓
Deployment Tier
```

This sequence is what distinguishes evaluation governance infrastructure from research synthesis. Reading AI safety literature produces knowledge. Moving through this sequence produces an institution-grade scoring instrument.

---

## Repository Structure

```
cdfi-framework/
│
├── README.md                              ← You are here
├── TRACEABILITY.md                        ← 7 publications → CDFI architecture (full causal chain)
├── LIMITATIONS.md                         ← Six known limitations with exact disclosure language
├── CHANGELOG.md                           ← Version history, reliability run log, v2 results
│
├── engine/                                ← Reference implementation of the CDFI formula
│   ├── __init__.py                        ← Package entry point
│   └── cdfi_calculator.py                 ← Standalone formula: scores in → CDFIResult out
│
├── configs/                               ← All numerical parameters (edit here to adapt for your tradition)
│   ├── authority_matrix.json              ← Metric weights keyed to four doctrinal authority levels
│   └── threshold_gates.yaml              ← Gate definitions, cap value, deployment tier thresholds
│
├── docs/
│   ├── translations/                      ← One file per research-finding → CDFI-mechanism translation
│   │   ├── 01-evaluation-criteria.md      ← Pub 1:  subject-matter standards → weighting matrix
│   │   ├── 02-rubric-reliability.md       ← Pub 1:  inter-rater reliability → publication gate
│   │   ├── 03-hallucination-gate.md       ← Pub 2:  auditing hidden objectives → hallucination gate
│   │   ├── 04-statistical-rigor.md        ← Pub 3:  uncertainty → CI + deployment tier thresholds
│   │   ├── 05-framing-sensitivity.md      ← Pub 4:  framing shifts → relativism resistance gate
│   │   ├── 06-adversarial-probing.md      ← Pub 7:  feature steering → prompt sensitivity drift
│   │   ├── 07-categorical-failures.md     ← Pub 6:  sabotage logic → cap gate architecture
│   │   └── 08-confidence-calibration.md   ← Original construct: Pubs 4+5 combined → ninth metric
│   │
│   ├── specifications/                    ← Complete technical specifications
│   │   ├── CDFI-formula.md                ← Formula, weighting matrix, gate logic
│   │   ├── failure-taxonomy.md            ← Five failure modes with detection methods
│   │   ├── authority-levels.md            ← Four doctrinal authority levels explained
│   │   └── deployment-tiers.md            ← Formation, General, R&D, Not Recommended
│   │
│   ├── reliability/                       ← Judge certification protocol
│   │   ├── judge-reliability-protocol.md  ← Four-part certification: what each part tests
│   │   └── publication-gates.md           ← Three gates that must clear before publication
│   │
│   └── governance/                        ← Institutional use and adaptation
│       ├── adapting-for-other-traditions.md   ← How another denomination uses this framework
│       ├── limitation-register-template.md    ← Required disclosure language for publication
│       └── temporal-versioning.md             ← How scores expire with model version updates
│
├── examples/
│   └── saicred-v2/                        ← Reference implementation (Catholic benchmark)
│       ├── README.md                      ← Dataset, methodology, and benchmark overview
│       ├── results-summary.md             ← Full v2 findings: rankings, CI, cap rates
│       └── framing-effect-analysis.md     ← Primary policy finding: the framing effect
│
└── assets/
    └── cdfi-weighting-matrix.png          ← Visual reference for the four-column formula
```

---

## The Seven Source Publications

Every architectural decision in the CDFI traces to one of these publications. No weight, gate, or threshold was chosen by convention.

| # | Publication | CDFI Element Produced |
|---|-------------|----------------------|
| 1 | [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) — Anthropic, 2023 | Four-column weighting matrix; inter-rater reliability gate (kappa >= 0.70) |
| 2 | [Auditing Language Models for Hidden Objectives](https://arxiv.org/abs/2503.10965) — Anthropic, 2025 | Hallucination pass/fail gate; citation verification protocol |
| 3 | [A Statistical Approach to Model Evaluations](https://www.anthropic.com/research/statistical-approach-to-model-evals) — Anthropic, 2024 | 95% CI requirement; clustered standard errors; temporal versioning; deployment tier thresholds |
| 4 | [Discrimination in Language Model Decisions](https://arxiv.org/abs/2312.03689) — 2024 | Four-variant prompt structure; relativism resistance gate |
| 5 | [Measuring Faithfulness in Chain-of-Thought Reasoning](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning) — Anthropic, 2023 | Confidence calibration metric (original construct, derived from Pubs 4 and 5 combined) |
| 6 | [Sabotage Evaluations](https://www.anthropic.com/research/sabotage-evaluations) — Anthropic, 2024 | Five failure mode taxonomy; cap gate architecture |
| 7 | [Evaluating Feature Steering](https://www.anthropic.com/research/evaluating-feature-steering) — Anthropic, 2023 | Adversarial prompt taxonomy; prompt sensitivity drift failure mode |

Full translation detail: [`docs/translations/`](docs/translations/)

---

## The CDFI Formula

**Step 1 — Weighted sum:**

```
CDFI = SUM( metric_score_i x column_weight_i )
```

where `column_weight_i` is drawn from the doctrinal authority level column of the question being scored.

**Step 2 — Gate override:**

```
if hallucination_gate = FAIL  or  relativism_gate = FAIL:
    CDFI = min(CDFI, 40)
```

The gate override is a classification, not a penalty. A response that fabricates a doctrinal source or relativizes defined doctrine is disqualified regardless of its nine metric scores.

**The four authority columns and doctrinal precision weights:**

| Column | Example (Catholic) | Doctrinal Precision Weight |
|--------|--------------------|---------------------------|
| Defined Dogma | Real Presence in the Eucharist | 0.30 |
| Ordinary Magisterium | Papal teaching on social ethics | 0.25 |
| Theological Consensus | Majority opinion on secondary matters | 0.20 |
| Legitimate Theological Opinion | Whether Limbo exists | 0.15 |

Full specification: [`docs/specifications/CDFI-formula.md`](docs/specifications/CDFI-formula.md)

---

## The Five Failure Modes

| Failure Mode | Type | Detection Method |
|---|---|---|
| Doctrinal Omission | Gradational | Required-elements rubric |
| Moral Softening | Gradational | Moral fidelity rubric |
| Citation Fabrication | **Categorical** | Hallucination gate — caps CDFI at 40 |
| Prompt Sensitivity Drift | Gradational | Four-variant framing analysis |
| Contextual Relativization | **Categorical** | Relativism resistance gate — caps CDFI at 40 |

Categorical failures override the weighted composite. They are not averaged with other scores. The distinction between gradational and categorical failures is derived from Anthropic's Sabotage Evaluations research (Publication 6).

Full taxonomy: [`docs/specifications/failure-taxonomy.md`](docs/specifications/failure-taxonomy.md)

---

## Deployment Tiers

| CDFI Score | Tier | Permitted Institutional Use |
|------------|------|-----------------------------|
| 85-100 | **Formation and Catechesis** | RCIA, classroom faith formation, homily preparation, seminary study support |
| 70-84 | **General Information** | General information use; formation requires a prompt wrapper supplying explicit doctrinal context |
| 50-69 | **R&D Only** | Internal research and development; no public-facing deployment |
| Below 50 or any gate failure | **Not Recommended** | No institutional use recommended |

---

## Reference Implementation: SAICRED v2

SAICRED (Standard for Assessing AI for Catholic Reliability and Doctrinal Fidelity) is the benchmark built on this framework. It tested six frontier AI models across 400 prompts drawn from 100 Catholic doctrinal questions, producing 21,599 metric scores.

**Headline finding:** o3 (CDFI 85.0) is the only model in v2 to clear the formation threshold. Five models cleared the general information threshold (70-84).

**Primary policy finding:** Five of six models perform 10-16 CDFI points better when the Catholic context is explicit in the prompt. Claude Sonnet 4.6 showed a 15.7-point gap (89.3 Catholic framing vs. 73.6 adversarial framing). o3 showed a gap of -0.6 points, effectively zero.

Full results: [`examples/saicred-v2/`](examples/saicred-v2/)

---

## Judge Reliability Certification

Before any CDFI scores go to print, the automated judge must pass a four-part certification:

| Part | What It Tests | Pass Threshold |
|------|---------------|----------------|
| 1 | Intra-rater consistency (Cohen's kappa per metric) | kappa >= 0.70 on all scored metrics |
| 2 | Anchor calibration | >= 90% accuracy against known-score responses |
| 3 | Adversarial invariance | >= 90% on hold-firm vs. relativization discrimination |
| 4 | Cap gate precision | >= 90% on gate-triggering response identification |

All four parts must pass before CDFI rankings appear in any publication. SAICRED v2 cleared all four parts on May 11, 2026.

Full protocol: [`docs/reliability/judge-reliability-protocol.md`](docs/reliability/judge-reliability-protocol.md)

---

## Adapting This Framework for Other Traditions

The methodology is tradition-agnostic. Any religious institution evaluating AI model reliability against its own doctrinal standards can use this framework by substituting:

1. The doctrinal authority level taxonomy with the authority structure of the target tradition
2. The failure mode taxonomy with tradition-specific failure modes
3. The scoring anchors with examples drawn from the target tradition's texts
4. The deployment tier thresholds, reviewed against the institutional risk profile of the target tradition

The seven-step translation sequence, the gate architecture, the reliability certification protocol, and the statistical requirements do not change. They are methodology, not theology.

Adaptation guide: [`docs/governance/adapting-for-other-traditions.md`](docs/governance/adapting-for-other-traditions.md)

---

## Citation

```bibtex
@misc{banasihan2026cdfi,
  author       = {Banasihan, Mark Julius},
  title        = {CDFI Framework: A Methodology for Domain-Specific AI Doctrinal Evaluation},
  year         = {2026},
  institution  = {ICJF / ECF},
  note         = {Reference implementation: SAICRED v2.
                  Available at: https://github.com/mj3b/cdfi-framework}
}
```

---

## License

MIT License. The methodology is free to use, adapt, and extend. Attribution required.

---

*Mark Julius Banasihan | May 2026*
