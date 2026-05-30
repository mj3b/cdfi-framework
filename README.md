# The CDFI Framework

**Evaluation Governance Infrastructure for Domain-Specific AI Doctrinal Benchmarking**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![DOI](https://zenodo.org/badge/1253813359.svg)](https://doi.org/10.5281/zenodo.20467497)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)
[![Status: v1.4 — Reference Implementation](https://img.shields.io/badge/status-v1.4%20reference%20implementation-5b6cff)](https://github.com/mj3b/cdfi-framework/releases)
[![Tradition-Agnostic](https://img.shields.io/badge/scope-tradition--agnostic-3bb273)](docs/governance/adapting-for-other-traditions.md)
[![Seven Source Publications](https://img.shields.io/badge/grounded%20in-7%20AI%20safety%20publications-ff6b35)](TRACEABILITY.md)
[![SAICRED v2](https://img.shields.io/badge/reference%20implementation-SAICRED%20v2-1565C0)](examples/saicred-v2/)
[![NIST AI RMF](https://img.shields.io/badge/aligned%20with-NIST%20AI%20RMF%201.0-4a90d9)](docs/governance/nist-rmf-mapping.md)
[![EU AI Act](https://img.shields.io/badge/mapped%20to-EU%20AI%20Act%202024-003399)](docs/governance/eu-ai-act-mapping.md)
[![OWASP LLM](https://img.shields.io/badge/security-OWASP%20LLM%20Top%2010-e03434)](docs/governance/security-considerations.md)

---

> **The problem this framework solves:** General-purpose AI benchmarks measure capability. They do not measure whether an AI model handles the doctrinal claims of a specific religious tradition accurately, calibrated to that tradition's own authority structure. This framework does.

---

## The SAICRED Project

> **SAICRED** — Standard for Assessing AI for Catholic Reliability and Doctrinal Fidelity
>
> Originated by [Filip Ponulak, PhD](https://www.linkedin.com/in/filipponulak/), who identified
> the gap — no systematic way to evaluate how faithfully AI models represent Catholic doctrine —
> and designed the framework to fill it. The SAICRED white paper (v2.0, February 2026) specified
> the benchmark's purpose, scope, eight evaluation metrics, five use-case categories, and
> eight-step methodology.

The CDFI Framework is the evaluation governance layer of that project. Three roles built it.

| Role | Person | Contribution |
|------|--------|-------------|
| **Project Lead** | [Filip Ponulak, PhD](https://www.linkedin.com/in/filipponulak/) | Originated SAICRED; designed the overall framework, evaluation criteria, and use-case taxonomy; authored the SAICRED white paper (v2.0, February 2026); holds theological authority and publication ownership |
| **Lead Engineer** | [Naveen Kumar Puppala](https://github.com/naveenp2728) | Built the production pipeline: 400 prompts across 6 models, Gemini 2.5 Flash as automated judge, 9 metrics scored per response, CDFI computation, 21,599 metric scores stored across 4 structured CSVs, interactive results dashboard |
| **Evals Expert** | [Mark Julius Banasihan](https://github.com/mj3b) | Translated the white paper's evaluation criteria into a defensible scoring architecture: CDFI formula, four-column authority-sensitive weighting matrix, hallucination and relativism resistance cap gates, four-part judge reliability certification protocol, limitation disclosures, and deployment tier thresholds |

The three roles were not interchangeable and could not substitute for each other. The Project Lead's theological framing defined what the benchmark was measuring. The Lead Engineer's pipeline produced the data. The Evals Expert's scoring architecture determined whether that data was defensible enough to support institutional deployment guidance.

Production pipeline: [saicred-benchmark](https://github.com/naveenp2728/saicred-benchmark) *(private — access pending publication)*


## What This Repository Is (and Is Not)

### This is

| Statement | Practical meaning |
|-----------|-------------------|
| An evaluation governance methodology derived from published AI safety research | Every weight, gate, and threshold traces to a named publication |
| A tradition-agnostic framework | Catholic doctrine is the reference implementation; any tradition can substitute its own authority structure |
| A portable reference implementation of the CDFI formula | Run `engine/cdfi_calculator.py` independently of the production pipeline |
| A publication-readiness protocol | Three explicit gates must clear before benchmark scores carry institutional weight |

### This is not

| Statement | What is explicitly excluded |
|-----------|----------------------------|
| A benchmark dataset | Prompts and model responses live in the production pipeline (saicred-benchmark) |
| A production scoring pipeline | That is `saicred-benchmark/scoring_service.py` |
| Regulatory or theological advice | All doctrinal and institutional determinations remain with qualified human authorities |
| An autonomous system | No component decides, approves, or classifies without human oversight |

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
├── TRANSLATION-METHOD.md                  ← How each publication became a computable CDFI mechanism
├── CITATION.cff                           ← Machine-readable citation metadata
├── CONTRIBUTING.md                        ← How to adapt, extend, or contribute
├── LICENSE                                ← Apache License 2.0
├── NOTICE                                 ← Required attribution for derivative works
│
├── engine/                                ← Reference implementation of the CDFI formula
│   ├── __init__.py                        ← Package entry point
│   └── cdfi_calculator.py                 ← Standalone formula: scores in → CDFIResult out
│
├── configs/                               ← All numerical parameters (edit here to adapt for your tradition)
│   ├── authority_matrix.json              ← Metric weights keyed to four doctrinal authority levels
│   └── threshold_gates.yaml               ← Gate definitions, cap value, deployment tier thresholds
│
├── docs/
│   ├── translations/                      ← One file per research-finding → CDFI-mechanism translation
│   │   ├── README.md                      ← Navigation guide: reading order, relationships, audience routing
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
│   │   ├── deployment-tiers.md            ← Formation, General, R&D, Not Recommended
│   │   └── scoring-anchors.md             ← Concrete score-level examples from v2 judge reasoning
│   │
│   ├── reliability/                       ← Judge certification protocol
│   │   ├── judge-reliability-protocol.md  ← Four-part certification: what each part tests
│   │   └── publication-gates.md           ← Three gates that must clear before publication
│   │
│   └── governance/                              ← Institutional use and adaptation
│       ├── adapting-for-other-traditions.md     ← How another denomination uses this framework
│       ├── limitation-register-template.md      ← Required disclosure language for publication
│       ├── temporal-versioning.md               ← How scores expire with model version updates
│       ├── nist-rmf-mapping.md                  ← NIST AI RMF 1.0 alignment: GOVERN/MAP/MEASURE/MANAGE
│       ├── eu-ai-act-mapping.md                 ← EU AI Act mapping: Articles 9–15; high-risk classification
│       ├── security-considerations.md           ← Attack surfaces, OWASP LLM Top 10, open gaps
│       └── cdcf-compliance/                     ← CDCF eight-criterion vetting documentation
│           ├── README.md                        ← Status overview and audience routing
│           ├── c1-canonical-scope.md            ← Mission alignment; pre-screening checklist
│           ├── c2-human-accountability.md       ← Four-level decision authority matrix
│           ├── c3-c7-responsibility-boundary.md ← Framework vs. model submitter obligations
│           ├── c4-validation-status.md          ← Independent validation evidence; open gates
│           ├── c5-subgroup-protocol.md          ← Vulnerable populations; subgroup protocol
│           ├── c6-deployment-governance.md      ← Four decision states; Canon 1609 appeal pathway
│           └── c8-configuration-boundary.md     ← Locked vs. configurable; subsidiarity test
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

Related repositories:

- **[saicred-benchmark](https://github.com/naveenp2708/saicred-benchmark)** — Production scoring pipeline: 400 prompts × 6 models × 9 metrics, Gemini 2.5 Flash judge, CDFI computation, and results dashboard *(private — access pending publication)*

---

## The Seven Source Publications

Every architectural decision in the CDFI traces to one of these publications. No weight, gate, or threshold was chosen by convention.

| # | Publication | CDFI Element Produced |
|---|-------------|----------------------|
| 1 | [Challenges in Evaluating AI Systems](https://www.anthropic.com/research/evaluating-ai-systems) — Anthropic, 2023 | Four-column weighting matrix; inter-rater reliability gate (kappa >= 0.60 on Critical metrics) |
| 2 | [Auditing Language Models for Hidden Objectives](https://arxiv.org/abs/2503.10965) — Anthropic, 2025 | Hallucination pass/fail gate; citation verification protocol |
| 3 | [A Statistical Approach to Model Evaluations](https://www.anthropic.com/research/statistical-approach-to-model-evals) — Anthropic, 2024 | 95% CI requirement; clustered standard errors; temporal versioning; deployment tier thresholds |
| 4 | [Discrimination in Language Model Decisions](https://arxiv.org/abs/2312.03689) — 2024 | Four-variant prompt structure; relativism resistance gate |
| 5 | [Measuring Faithfulness in Chain-of-Thought Reasoning](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning) — Anthropic, 2023 | Confidence calibration metric (original construct, derived from Pubs 4 and 5 combined) |
| 6 | [Sabotage Evaluations](https://www.anthropic.com/research/sabotage-evaluations) — Anthropic, 2024 | Five failure mode taxonomy; cap gate architecture |
| 7 | [Evaluating Feature Steering](https://www.anthropic.com/research/evaluating-feature-steering) — Anthropic, 2023 | Adversarial prompt taxonomy; prompt sensitivity drift failure mode |

Full translation detail — including the exact causal chain from finding to formula element for each publication: [`TRACEABILITY.md`](TRACEABILITY.md)

The systematic methodology used to perform each translation — the seven-step sequence from literature claim to deployment tier: [`TRANSLATION-METHOD.md`](TRANSLATION-METHOD.md)

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

Categorical failures override the weighted composite. They are not averaged with other scores.

Full taxonomy: [`docs/specifications/failure-taxonomy.md`](docs/specifications/failure-taxonomy.md)

---

## Deployment Tiers

| CDFI Score | Tier | Permitted Institutional Use |
|------------|------|-----------------------------|
| 85–100 | **Formation and Catechesis** | RCIA, classroom faith formation, homily preparation, seminary study support |
| 70–84 | **General Information** | General information use; formation requires a prompt wrapper supplying explicit doctrinal context |
| 50–69 | **R&D Only** | Internal research and development; no public-facing deployment |
| Below 50 or any gate failure | **Not Recommended** | No institutional use recommended |

---

## Reference Implementation: SAICRED v2

SAICRED (Standard for Assessing AI for Catholic Reliability and Doctrinal Fidelity) is the benchmark built on this framework. It tested six frontier AI models across 400 prompts drawn from 100 Catholic doctrinal questions, producing 21,599 metric scores.

**Headline finding:** o3 (CDFI 85.0) is the only model in v2 to clear the formation threshold. Five models cleared the general information threshold (70–84).

**Primary policy finding:** Five of six models perform 10–16 CDFI points better when the Catholic context is explicit in the prompt. Claude Sonnet 4.6 showed a 15.8-point gap (89.4 Catholic framing vs. 73.6 adversarial framing). o3 showed a gap of -0.8 points, effectively zero.

Full results: [`examples/saicred-v2/`](examples/saicred-v2/)

---

## Judge Reliability Certification

Before any CDFI scores go to print, the automated judge must pass a four-part certification:

| Part | What It Tests | Pass Threshold | SAICRED v2 Result |
|------|---------------|:--------------:|:-----------------:|
| 1 | Intra-rater consistency (Cohen's kappa per metric) | kappa >= 0.60 on Critical metrics | **PASS** — May 7, 2026 |
| 2 | Anchor calibration | >= 90% accuracy | **PASS** — 98.3% |
| 3 | Adversarial invariance | >= 90% | **PASS** — 100% |
| 4 | Cap gate precision | >= 90% | **PASS** — 100% |

All four parts cleared: **May 11, 2026.**

Full protocol: [`docs/reliability/judge-reliability-protocol.md`](docs/reliability/judge-reliability-protocol.md)

---

## Adapting This Framework for Other Traditions

The methodology is tradition-agnostic. Any religious institution evaluating AI model reliability against its own doctrinal standards can use this framework by substituting:

1. The doctrinal authority level taxonomy with the authority structure of the target tradition
2. The failure mode taxonomy with tradition-specific failure modes
3. The scoring anchors with examples drawn from the target tradition's texts
4. The deployment tier thresholds, reviewed against the institutional risk profile

The seven-step translation sequence, the gate architecture, the reliability certification protocol, and the statistical requirements do not change. They are methodology, not theology.

Adaptation guide: [`docs/governance/adapting-for-other-traditions.md`](docs/governance/adapting-for-other-traditions.md)

---

## Known Limitations

Six limitations are documented with exact disclosure language:

| # | Limitation | Publication Impact |
|---|-----------|:-----------------:|
| L1 | Authority level classification pending — all 400 v2 prompts used `ordinary_magisterium` default | Blocks final CDFI |
| L2 | Human theological review pending | Blocks full publication |
| L3 | Pastoral appropriateness kappa = 0.352 (formula weight 0.02–0.05; non-blocking) | Disclosure only |
| L4 | Stability scores hardcoded at 3.0 — deferred to v2.1 | Non-blocking |
| L5 | Positions 1–5 not statistically distinguishable (only Grok vs. Claude gap reaches p < 0.05) | Interpretive constraint |
| L6 | Scores tied to specific model versions; expire on major version update | Active via versioning protocol |
| L7 | Security: three attack surfaces documented but not technically mitigated (prompt injection, pipeline integrity, authority level signing) | Disclosure only — v1.5 remediation planned |

Full register with paste-ready disclosure language: [`LIMITATIONS.md`](LIMITATIONS.md)

---

## AI-Assisted Research Disclosure

This project used Claude (Anthropic) for methodology development, document drafting, scoring architecture design, and repository construction (March–May 2026). All AI-generated output was treated as draft material subject to human review. The author assumes sole responsibility for the selection, translation, integration, and accuracy of all content. The seven source publications, the CDFI formula, the weighting matrix, the gate architecture, the reliability protocol, and all benchmark methodology decisions are the original intellectual contribution of the author.

---

## Citation

```bibtex
@software{banasihan2026cdfi,
  author  = {Banasihan, Mark Julius},
  title   = {{CDFI Framework}: Evaluation Governance Infrastructure
             for Domain-Specific {AI} Doctrinal Benchmarking},
  year    = {2026},
  month   = {5},
  version = {1.4},
  doi     = {10.5281/zenodo.20467497},
  url     = {https://doi.org/10.5281/zenodo.20467497},
  license = {Apache-2.0}
}
```

See also: [`CITATION.cff`](CITATION.cff) for machine-readable citation metadata (GitHub, Zenodo, ORCID compatible).

---

## License

Copyright © 2026 Mark Julius Banasihan. Licensed under the [Apache License 2.0](LICENSE). The methodology is free to use, adapt, and extend. Attribution required.

---

## Author

**Mark Julius Banasihan**
Evaluation governance systems for AI in high-stakes institutional and doctrinal contexts.

[GitHub](https://github.com/mj3b) · [LinkedIn](https://linkedin.com/in/markjuliusbanasihan) · [ORCID](https://orcid.org/0009-0001-8121-2878) · [Email](mailto:markjuliusbanasihan@gmail.com) · Atlanta, Georgia, United States
