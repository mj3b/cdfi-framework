# NIST AI RMF 1.0 Mapping

## CDFI Framework Alignment with the National Institute of Standards and Technology AI Risk Management Framework

*Mark Julius Banasihan | May 2026*

**Framework:** [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework) (January 2023)
**Profile Applied:** [NIST AI 600-1 Generative AI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf) (2024)
**Relevance:** U.S. Catholic dioceses, universities, health systems, and charitable organizations operating under federal guidance or institutional risk management requirements.

---

> This document maps the CDFI Framework's existing architecture to the four NIST AI RMF functions. It identifies where the framework satisfies RMF requirements, where it partially satisfies them, and where gaps remain for v1.4 and beyond.

---

## The Four RMF Functions at a Glance

```
GOVERN  ──  Infuse risk management into culture, policy, and process
   │
   ├── MAP  ──  Understand contexts, risks, and their interdependencies
   │
   ├── MEASURE  ──  Quantify risks and evaluate their magnitude
   │
   └── MANAGE  ──  Respond to and recover from risk incidents
```

The functions are iterative, not sequential. GOVERN supports and is supported by MAP, MEASURE, and MANAGE continuously over the system's lifetime.

---

## GOVERN — Policies, Roles, and Organizational Accountability

The GOVERN function requires that AI risk management be embedded in organizational culture, with defined roles, policies, and accountability structures.

| RMF Sub-Function | CDFI Framework Element | Status |
|-----------------|----------------------|:------:|
| GOVERN 1.1 — Policies for AI risk management established | `configs/threshold_gates.yaml` machine-readable policy; `docs/governance/cdcf-compliance/` eight-criterion governance structure | **Satisfied** |
| GOVERN 1.2 — Accountability and responsibility defined | `docs/governance/cdcf-compliance/c2-human-accountability.md` four-level decision authority matrix; named maintainers in `c8-configuration-boundary.md` | **Satisfied** |
| GOVERN 1.3 — Organizational teams understand AI risk | `TRANSLATION-METHOD.md` seven-step methodology; `docs/translations/` eight documents; `docs/specifications/` | **Satisfied** |
| GOVERN 1.4 — Organizational risk tolerance established | Deployment tier thresholds (85/70/50) in `configs/threshold_gates.yaml`; C8 configurable for local risk tolerance | **Satisfied** |
| GOVERN 2.1 — AI risk intersects with other enterprise risk | CDCF compliance documentation connects AI scoring risk to canonical, theological, and institutional risk categories | **Partial** — no enterprise risk register integration |
| GOVERN 4.1 — Organizational teams committed to risk management | Apache 2.0 open governance; `CONTRIBUTING.md` defines accepted contributions and review requirements | **Satisfied** |
| GOVERN 5.1 — Policies for AI procurement and third-party risks | `docs/governance/cdcf-compliance/c3-c7-responsibility-boundary.md` handoff clause for model submitters | **Partial** — procurement policy template not provided |
| GOVERN 6.1 — Policies for AI deployment and monitoring | `docs/governance/cdcf-compliance/c6-deployment-governance.md` four decision states; escalation conditions; temporal versioning | **Satisfied** |

---

## MAP — Contextualize Risks and Their Interdependencies

The MAP function requires identifying the deployment context, affected populations, and the network of risks that emerge when AI systems operate in institutional settings.

| RMF Sub-Function | CDFI Framework Element | Status |
|-----------------|----------------------|:------:|
| MAP 1.1 — Context established for AI risk assessment | `docs/governance/cdcf-compliance/c1-canonical-scope.md` pre-screening checklist; C3 transparency documentation | **Satisfied** |
| MAP 1.5 — AI risk identified for specific deployment context | `docs/specifications/failure-taxonomy.md` five failure modes; `docs/specifications/deployment-tiers.md` tier-specific risk profiles | **Satisfied** |
| MAP 2.1 — Scientific findings reviewed for AI limitations | `TRACEABILITY.md` seven source publications; `LIMITATIONS.md` six disclosed constraints with exact language | **Satisfied** |
| MAP 2.2 — AI system characteristics examined | `docs/specifications/CDFI-formula.md`; `configs/authority_matrix.json`; `engine/cdfi_calculator.py` | **Satisfied** |
| MAP 3.5 — Risks of bias and discrimination evaluated | `docs/governance/cdcf-compliance/c5-subgroup-protocol.md` subgroup protocol; framing effect analysis documents English-language bias | **Partial** — subgroup evaluation not yet conducted (SAICRED v3) |
| MAP 5.1 — Likelihood and impact of risk assessed | `LIMITATIONS.md` impact assessment per limitation; `docs/reliability/publication-gates.md` publication blocking status | **Satisfied** |
| MAP 5.2 — Impact on persons and communities evaluated | `docs/governance/cdcf-compliance/c5-subgroup-protocol.md`; framing effect data quantifies differential impact | **Partial** — non-English communities not yet evaluated |

---

## MEASURE — Quantify and Evaluate AI Risks

The MEASURE function requires defining metrics, performing measurements, and evaluating results against defined thresholds.

| RMF Sub-Function | CDFI Framework Element | Status |
|-----------------|----------------------|:------:|
| MEASURE 1.1 — Metrics established for AI risk | Nine-metric scoring rubric; Cohen's kappa thresholds; deployment tier thresholds | **Satisfied** |
| MEASURE 2.1 — Test sets evaluated for fairness and bias | Four-variant prompt structure (neutral/Christian/Catholic/adversarial) detects framing-induced bias | **Partial** — demographic subgroup testing not yet conducted |
| MEASURE 2.2 — Evaluations against intended use | 400 prompts × 6 models × 9 metrics; SAICRED v2 evaluation against Catholic doctrinal use cases | **Satisfied** |
| MEASURE 2.5 — AI system to be evaluated for confabulation | Hallucination pass/fail gate; citation fabrication is categorical failure; 68 hallucination events detected in v2 | **Satisfied** |
| MEASURE 2.6 — AI system evaluated for dangerous recommendations | Relativism resistance gate catches doctrinal misrepresentation; 181 relativism failures detected in v2 | **Satisfied** |
| MEASURE 2.9 — Privacy risk evaluated | `docs/governance/cdcf-compliance/c3-c7-responsibility-boundary.md` data ingestion disclosure | **Partial** — no formal privacy impact assessment |
| MEASURE 2.10 — AI system consistency evaluated | Four-part judge reliability certification (all parts cleared May 11, 2026); kappa ≥ 0.60 on Critical metrics | **Satisfied** |
| MEASURE 2.13 — Effectiveness evaluated in deployment context | Framing effect analysis; cap rate by model; pairwise significance testing with clustered standard errors | **Satisfied** |
| MEASURE 4.1 — Risk metrics monitored in deployment | Temporal versioning protocol triggers re-evaluation on model version update | **Partial** — no automated monitoring; re-evaluation is manual |

---

## MANAGE — Respond to and Recover from Risk Incidents

The MANAGE function requires response plans, recovery procedures, and continuous improvement mechanisms.

| RMF Sub-Function | CDFI Framework Element | Status |
|-----------------|----------------------|:------:|
| MANAGE 1.1 — Risk responses prioritized | Deployment tier thresholds; mandatory suspension conditions in `c6-deployment-governance.md` | **Satisfied** |
| MANAGE 1.3 — Risk response plans established | Three-severity vulnerability response process in `c8-configuration-boundary.md`; escalation conditions with actions | **Satisfied** |
| MANAGE 2.2 — AI incidents documented | Appeal pathway produces written records; institutional governance log required | **Satisfied** |
| MANAGE 2.4 — Risk treatments implemented | Cap gate architecture overrides CDFI scores on categorical failures; deployment tier prevents out-of-tier use | **Satisfied** |
| MANAGE 3.1 — AI risk management reviewed | `CHANGELOG.md` version history; `docs/governance/temporal-versioning.md` re-evaluation triggers | **Satisfied** |
| MANAGE 4.1 — Lessons learned integrated | `CHANGELOG.md` documents root cause analysis for every reliability run failure and fix | **Satisfied** |

---

## NIST GenAI Profile — Risk Coverage

The NIST AI 600-1 GenAI Profile defines risks specific to or amplified by generative AI systems. The CDFI Framework addresses a subset directly relevant to Catholic doctrinal evaluation.

| GenAI Risk | CDFI Coverage | Status |
|-----------|--------------|:------:|
| Confabulation | Hallucination gate; citation verification; source citation metric | **Addressed** |
| Information Integrity | Relativism resistance gate; doctrinal precision metric; four-variant testing | **Addressed** |
| Value Chain and Component Integration | `c3-c7-responsibility-boundary.md` handoff clause; model submitter obligations | **Partial** |
| Toxicity, Bias, and Homogenization | Framing effect analysis; C5 subgroup protocol (pending execution) | **Partial** |
| Data Privacy | Data ingestion disclosure; no personal data at framework level | **Partial** |
| CBRN Information | Not applicable to Catholic doctrinal evaluation | N/A |
| Human-AI Configuration | Four-level accountability matrix; Level 4 real-time oversight requirement | **Addressed** |

---

## Summary: NIST RMF Coverage by Function

| Function | Sub-functions Satisfied | Partial | Open Gap |
|----------|:-----------------------:|:-------:|:--------:|
| GOVERN | 6 | 2 | 0 |
| MAP | 5 | 3 | 0 |
| MEASURE | 7 | 3 | 0 |
| MANAGE | 6 | 0 | 0 |
| **Total** | **24** | **8** | **0** |

No RMF sub-function is entirely unaddressed. All eight partial satisfactions trace to the same two root causes: subgroup evaluation not yet conducted (C5, addressed in v3) and monitoring automation not implemented (aspirational per C6).

---

## Relationship to CDCF Criteria

The NIST RMF and the CDCF Project Vetting Criteria are complementary, not redundant. The CDCF criteria operationalize Catholic institutional governance requirements with canonical grounding. The NIST RMF provides the secular institutional risk management framework that governs U.S. Catholic organizations operating under federal guidance.

| CDCF Criterion | Primary NIST RMF Function |
|---------------|--------------------------|
| C1 Mission Alignment | GOVERN 1.1, MAP 1.1 |
| C2 Human Accountability | GOVERN 1.2, MANAGE 2.2 |
| C3 Transparency | GOVERN 1.3, MAP 2.1 |
| C4 Independent Validation | MEASURE 2.10 |
| C5 Vulnerable Populations | MAP 3.5, MEASURE 2.1 |
| C6 Deployment Governance | GOVERN 6.1, MANAGE 1.3 |
| C7 Documentation | GOVERN 4.1, MANAGE 3.1 |
| C8 Subsidiarity | GOVERN 1.4 |

---

*NIST AI RMF 1.0:* https://www.nist.gov/itl/ai-risk-management-framework

*NIST AI 600-1 GenAI Profile:* https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf

*Related: [docs/governance/cdcf-compliance/README.md](cdcf-compliance/README.md)*

*Related: [docs/governance/eu-ai-act-mapping.md](eu-ai-act-mapping.md)*

*Related: [docs/governance/security-considerations.md](security-considerations.md)*
