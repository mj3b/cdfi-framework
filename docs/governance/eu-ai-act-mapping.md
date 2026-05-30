# EU AI Act Mapping

## CDFI Framework Alignment with the European Union Artificial Intelligence Act

*Mark Julius Banasihan | May 2026*

**Regulation:** [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) of the European Parliament and of the Council on Artificial Intelligence (EU AI Act), in force August 1, 2024. Phased application through 2027.
**Relevance:** Catholic schools, universities, parishes, dioceses, and charitable organizations operating in EU member states. Any Catholic institution deploying AI tools for educational or formation purposes in the EU likely operates under the high-risk classification.

---

> The EU AI Act introduces mandatory requirements for AI systems classified as high-risk. This document identifies where the CDFI Framework satisfies those requirements, where gaps remain, and what Catholic institutions in the EU must address before deploying any AI tool scored under this framework.

---

## Risk Classification: Where Catholic AI Tools Land

The EU AI Act classifies AI systems by risk level. The classification determines which obligations apply.

```
UNACCEPTABLE RISK  ──  Prohibited entirely (Article 5)
      │
HIGH RISK  ──────────  Mandatory requirements apply (Articles 8–15, Annex III)
      │
LIMITED RISK  ────────  Transparency obligations only (Article 50)
      │
MINIMAL RISK  ────────  No mandatory requirements (encouraged to follow voluntary codes)
```

**Catholic AI tools for education and formation: likely HIGH RISK**

[Annex III, Category 4](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#anx_III) of the EU AI Act lists high-risk AI systems in education and vocational training, including systems that:
- Determine access to or assignment in educational institutions
- Evaluate learning outcomes
- Assess the appropriate level of education for a person

A Catholic formation program that uses an AI tool to guide a person's faith journey, determine their readiness for sacraments, or assess doctrinal knowledge operates in this category. An AI tool used for general Catholic information retrieval may fall under Limited Risk. The classification depends on the specific use case, not the tool itself.

**Catholic institutions should determine their AI tool's classification before deployment.** The pre-screening checklist in [`docs/governance/cdcf-compliance/c1-canonical-scope.md`](cdcf-compliance/c1-canonical-scope.md) is the starting point. Tools that simulate sacramental functions are excluded from scope entirely; the EU AI Act's unacceptable risk category would apply independently.

---

## High-Risk AI System Requirements (Articles 8–15)

### Article 9 — Risk Management System

**Requirement:** A continuous, iterative risk management system identifying and analyzing known and reasonably foreseeable risks, and implementing appropriate risk management measures.

| CDFI Framework Element | Satisfies |
|----------------------|:---------:|
| [`LIMITATIONS.md`](../../LIMITATIONS.md) — six disclosed limitations with closing conditions | Partial |
| [`docs/reliability/publication-gates.md`](../reliability/publication-gates.md) — three publication gates | Partial |
| [`docs/governance/temporal-versioning.md`](temporal-versioning.md) — version expiration triggers | Partial |
| [`docs/governance/cdcf-compliance/c6-deployment-governance.md`](cdcf-compliance/c6-deployment-governance.md) — escalation conditions | Partial |

**Gap:** The CDFI Framework documents risk at the methodology level. A Catholic institution deploying an AI tool must implement Article 9 at the **deployment** level — a continuous risk management system covering the specific tool, the specific use case, and the specific affected population. The CDFI Framework provides inputs to that system; it does not constitute the system itself.

---

### Article 10 — Data and Data Governance

**Requirement:** Training, validation, and testing datasets must meet quality criteria, be examined for biases, and be relevant, representative, and free of errors.

| CDFI Framework Element | Satisfies |
|----------------------|:---------:|
| [`docs/governance/cdcf-compliance/c3-c7-responsibility-boundary.md`](cdcf-compliance/c3-c7-responsibility-boundary.md) — data ingestion disclosure | Partial |
| [`docs/governance/cdcf-compliance/c5-subgroup-protocol.md`](cdcf-compliance/c5-subgroup-protocol.md) — subgroup evaluation protocol | Partial |
| SAICRED v2 dataset: 100 questions × 4 variants, English only | Partial |

**Gap:** Article 10 applies to the AI models being evaluated, not to the evaluation methodology itself. Catholic institutions must verify that the AI tool they intend to deploy satisfies Article 10 data requirements independently of its CDFI score. The model submitter obligations in [`c3-c7-responsibility-boundary.md`](cdcf-compliance/c3-c7-responsibility-boundary.md) address this at the handoff clause level.

**CDFI-specific gap:** The SAICRED v2 evaluation dataset is in English only. For EU deployment, the dataset does not represent the linguistic diversity of Catholic populations in EU member states. Non-English subgroup evaluation (Spanish, Portuguese, French, German, Polish, Italian, and others) is required before CDFI scores can be cited as supporting Article 10 compliance for European Catholic AI deployment. See [`docs/governance/cdcf-compliance/c5-subgroup-protocol.md`](cdcf-compliance/c5-subgroup-protocol.md).

---

### Article 11 — Technical Documentation

**Requirement:** Technical documentation sufficient for conformity assessment before market placement, covering design specifications, capabilities, limitations, intended purpose, and risk management measures.

| CDFI Framework Element | Satisfies |
|----------------------|:---------:|
| [`TRACEABILITY.md`](../../TRACEABILITY.md) — every architectural decision traced to source | ✓ |
| [`docs/specifications/CDFI-formula.md`](../specifications/CDFI-formula.md) — complete formula specification | ✓ |
| [`configs/authority_matrix.json`](../../configs/authority_matrix.json) — all numerical parameters | ✓ |
| [`configs/threshold_gates.yaml`](../../configs/threshold_gates.yaml) — gate definitions and tier thresholds | ✓ |
| [`LIMITATIONS.md`](../../LIMITATIONS.md) — limitations with exact language | ✓ |
| [`docs/reliability/judge-reliability-protocol.md`](../reliability/judge-reliability-protocol.md) — certification evidence | ✓ |
| [`CHANGELOG.md`](../../CHANGELOG.md) — version history | ✓ |

**Status: Substantially Satisfied.** The CDFI Framework's documentation architecture was designed for exactly this purpose. A conformity assessor can trace every scoring decision to its source without access to the framework authors.

---

### Article 12 — Record-Keeping

**Requirement:** High-risk AI systems must automatically log events ("logging"), with logs retained for at least six months.

| CDFI Framework Element | Satisfies |
|----------------------|:---------:|
| [`CHANGELOG.md`](../../CHANGELOG.md) — methodology version history | Partial |
| [`docs/governance/cdcf-compliance/c2-human-accountability.md`](cdcf-compliance/c2-human-accountability.md) — decision record template | Partial |

**Gap:** The CDFI Framework does not implement automated logging of deployment events. A Catholic institution deploying a high-risk AI tool must implement Article 12 logging independently, using the institutional governance log specified in [`c2-human-accountability.md`](cdcf-compliance/c2-human-accountability.md) as a starting point. That log must be retained for a minimum of six months under Article 12.

---

### Article 13 — Transparency and Provision of Information to Deployers

**Requirement:** High-risk AI systems must be transparent enough for deployers to understand capabilities, limitations, intended purpose, and how to interpret outputs.

| CDFI Framework Element | Satisfies |
|----------------------|:---------:|
| [`docs/specifications/scoring-anchors.md`](../specifications/scoring-anchors.md) — concrete score-level examples | ✓ |
| [`docs/specifications/deployment-tiers.md`](../specifications/deployment-tiers.md) — permitted uses per tier | ✓ |
| [`docs/governance/cdcf-compliance/c3-c7-responsibility-boundary.md`](cdcf-compliance/c3-c7-responsibility-boundary.md) — operational boundaries | ✓ |
| [`examples/saicred-v2/framing-effect-analysis.md`](../../examples/saicred-v2/framing-effect-analysis.md) — framing gap disclosure | ✓ |
| [`LIMITATIONS.md`](../../LIMITATIONS.md) — limitations with disclosure language | ✓ |

**Status: Satisfied.** The deployment tier structure, scoring anchor documentation, and framing effect analysis collectively provide deployers with sufficient information to understand what CDFI scores mean and what they do not mean.

---

### Article 14 — Human Oversight

**Requirement:** High-risk AI systems must be designed to enable effective oversight by natural persons, including the ability to understand capabilities and limitations, intervene, and override.

| CDFI Framework Element | Satisfies |
|----------------------|:---------:|
| [`docs/governance/cdcf-compliance/c2-human-accountability.md`](cdcf-compliance/c2-human-accountability.md) — four-level oversight matrix | ✓ |
| [`docs/governance/cdcf-compliance/c6-deployment-governance.md`](cdcf-compliance/c6-deployment-governance.md) — human review triggers | ✓ |
| [`engine/cdfi_calculator.py`](../../engine/cdfi_calculator.py) — open source, fully inspectable | ✓ |
| Mandatory suspension conditions on gate failures | ✓ |
| Level 4 real-time override without requiring Level 3 authorization | ✓ |

**Status: Satisfied.** The four-level accountability matrix, Level 4 real-time override authority, and mandatory suspension conditions collectively satisfy Article 14's human oversight requirements.

---

### Article 15 — Accuracy, Robustness, and Cybersecurity

**Requirement:** High-risk AI systems must achieve appropriate accuracy levels, be resilient against errors, faults, and inconsistencies, and be protected against adversarial attacks or unauthorized attempts to alter performance.

| CDFI Framework Element | Satisfies |
|----------------------|:---------:|
| Four-part judge reliability certification (kappa ≥ 0.60 Critical metrics) — [`docs/reliability/judge-reliability-protocol.md`](../reliability/judge-reliability-protocol.md) | Partial |
| Hallucination and relativism resistance gates — [`configs/threshold_gates.yaml`](../../configs/threshold_gates.yaml) | Partial |
| [`docs/governance/security-considerations.md`](security-considerations.md) — attack surface documentation | Partial |
| Apache 2.0 open source — community audit of scoring logic — [`LICENSE`](../../LICENSE) | Partial |

**Gap:** Article 15 requires documented cybersecurity measures against adversarial manipulation. The CDFI Framework identifies three attack surfaces in [`docs/governance/security-considerations.md`](security-considerations.md) (judge prompt injection, scoring pipeline integrity, authority level manipulation) but does not implement automated protections against them. This is the primary Article 15 gap for v1.4.

---

## Fundamental Rights Impact Assessment — Open Gap

The EU AI Act requires deployers of high-risk AI systems to conduct a fundamental rights impact assessment before deployment. This is separate from, and in addition to, the Article 9 risk management system.

The CDFI Framework does not provide a fundamental rights impact assessment template. Catholic institutions deploying high-risk AI tools in the EU must conduct this assessment independently. The CDFI Framework's subgroup protocol ([`c5-subgroup-protocol.md`](cdcf-compliance/c5-subgroup-protocol.md)) is the methodological input to that assessment — it identifies populations at elevated risk and the evaluation protocol required — but the assessment itself is an institutional obligation under EU law.

**What a fundamental rights impact assessment for Catholic AI deployment would require:**

```
1. Identify the specific AI system and its intended use case
2. Identify the populations affected (with particular attention to
   the groups named in C5: elderly, disabled, non-English-speaking,
   communities in poverty, youth in formation programs)
3. Assess the nature and severity of potential impacts on:
   — Right to non-discrimination (Article 21, EU Charter)
   — Right to education (Article 14, EU Charter)
   — Freedom of religion and conscience (Article 10, EU Charter)
   — Right to dignity (Article 1, EU Charter)
4. Document mitigation measures
5. Consult with affected communities where feasible
6. Document the assessment with named institutional authority
```

---

## Conformity Assessment — Open Gap

For high-risk AI systems, the EU AI Act requires a conformity assessment before placing the system on the market or putting it into service. The CDFI score is one input to such an assessment, not the assessment itself.

**What constitutes a passing conformity assessment for the CDFI Framework layer:**

```
Required for conformity (CDFI Framework layer):
  □ All four judge reliability certification parts cleared
  □ Authority level classification complete (final CDFI, not preliminary)
  □ Human theological review complete (Addendum E)
  □ Article 11 technical documentation complete (satisfied — see above)
  □ Article 13 transparency documentation complete (satisfied — see above)
  □ Article 14 human oversight structure implemented (satisfied — see above)

Required for conformity (model submitter layer):
  □ Training data documentation (Article 10)
  □ Automated logging implementation (Article 12)
  □ Cybersecurity measures documented (Article 15)
  □ Fundamental rights impact assessment completed
```

---

## EU AI Act Application Timeline

| Date | Obligation |
|------|-----------|
| February 2025 | Prohibited AI practices ([Article 5](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#art_5)) apply |
| August 2025 | GPAI model obligations apply |
| **August 2026** | **High-risk AI system obligations apply — [Annex III](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#anx_III)** |
| August 2027 | High-risk systems already in service must comply |

Catholic institutions in the EU deploying formation and catechetical AI tools should be preparing for August 2026 compliance now. The CDFI Framework's governance documentation provides the methodology layer of that preparation.

---

## Summary: EU AI Act Coverage

| Article | Requirement | CDFI Status |
|---------|------------|:-----------:|
| [Art. 9](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#art_9) | Risk management system | Partial — methodology inputs provided; institutional system required |
| [Art. 10](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#art_10) | Data and data governance | Partial — model submitter obligation; English-only dataset gap |
| [Art. 11](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#art_11) | Technical documentation | **Satisfied** |
| [Art. 12](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#art_12) | Record-keeping and logging | Partial — decision record template provided; automated logging not implemented |
| [Art. 13](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#art_13) | Transparency | **Satisfied** |
| [Art. 14](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#art_14) | Human oversight | **Satisfied** |
| [Art. 15](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#art_15) | Accuracy, robustness, cybersecurity | Partial — reliability certification satisfies accuracy; cybersecurity gaps documented |
| [Annex III](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#anx_III) | Fundamental rights impact assessment | **Open gap** — institutional obligation, not framework obligation |
| [Annex III](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#anx_III) | Conformity assessment | **Open gap** — pending Addendum E completion and model submitter documentation |

---

*EU AI Act full text:* [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)

*EU AI Act high-risk classification:* [Annex III](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689#anx_III)

*EU Charter of Fundamental Rights:* [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12012P/TXT)

*Related: [docs/governance/nist-rmf-mapping.md](nist-rmf-mapping.md)*

*Related: [docs/governance/security-considerations.md](security-considerations.md)*

*Related: [docs/governance/cdcf-compliance/c5-subgroup-protocol.md](cdcf-compliance/c5-subgroup-protocol.md)*

*Related: [docs/governance/cdcf-compliance/c2-human-accountability.md](cdcf-compliance/c2-human-accountability.md)*

*Related: [docs/governance/cdcf-compliance/c4-validation-status.md](cdcf-compliance/c4-validation-status.md)*
