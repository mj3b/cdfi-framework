# C3 and C7 — Responsibility Boundary

## Transparency of Scope and Operation / Documentation and Data Stewardship

**CDCF Criterion Version:** v0.2 | C3: Gate 1 | C7: Gate 2
**Criterion Text:** [catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria](https://catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria)

---

## Doctrinal Grounding

*Antiqua et Nova* (Dicastery for the Doctrine of the Faith, January 28, 2025) establishes that "the inherent dignity of each human being and the fraternity that binds us together" must serve as the "indisputable criteria for evaluating new technologies before they are employed." Evaluation requires information. A project whose operation cannot be independently described cannot be evaluated against those criteria.

The COMPAS criminal sentencing algorithm documented what happens when transparency requirements are absent: risk scores found to be nearly twice as likely to falsely flag Black defendants as high risk compared to white defendants, before institutional accountability mechanisms were engaged. *See: Julia Angwin et al., "Machine Bias," ProPublica, May 23, 2016.* The absence of transparency documentation is not a neutral condition. It is an enabling condition for undetected harm.

---

## The Boundary

The CDFI Framework evaluates AI models. It does not train them, does not manage the data they were trained on, and does not operate the inference-time systems that produce the responses it scores. This creates a responsibility boundary. A CDCF reviewer or adopting institution must know which transparency requirements land on the framework and which land on the submitter of the underlying AI model.

---

## C3: What the CDFI Framework Discloses

### What the project does

The CDFI Framework produces a scored assessment of how reliably an AI model handles the doctrinal claims of a specific religious tradition across nine metrics, four framing conditions, and multiple doctrinal authority levels. The output is the Catholic Doctrinal Fidelity Index: a weighted composite score on a 0-100 scale with a pass/fail gate architecture.

Full specification: [`docs/specifications/CDFI-formula.md`](../../specifications/CDFI-formula.md)

### What data it ingests

**At scoring time (inference):** The CDFI scoring engine ingests a dict of nine metric scores (0-5 each) plus an authority level tag for the question being scored. No personal data. No user data. No model response text is stored by the framework — only the scores the automated judge assigns to that response.

**At evaluation time (pipeline):** The production pipeline (Naveen Kumar Puppala, `github.com/naveenp2708/saicred-benchmark`) ingests model API responses to 400 prompts drawn from 100 Catholic doctrinal questions. Those prompts are the SAICRED v2 dataset. No personal data from Catholic institution users is ingested at any point.

**What the CDFI Framework does not ingest:** Training data of evaluated models; user queries in production deployment; personal information of Catholic institution members.

### Who is affected by its outputs

Primary: Catholic institutions making deployment decisions about AI tools. The CDFI tier assignment (Formation and Catechesis, General Information, R&D Only, Not Recommended) directly informs whether a diocese, school, or parish authorizes or prohibits specific AI use cases. See [`docs/specifications/deployment-tiers.md`](../../specifications/deployment-tiers.md).

Secondary: Catholics who use AI tools in contexts where deployment decisions were informed by CDFI scores.

### What decisions it informs or makes

**Informs (requires named human authority):**
- Deployment tier assignment for a specific AI model version
- Publication of CDFI rankings
- Institutional authorization decisions (see [`c2-human-accountability.md`](c2-human-accountability.md) Level 3)

**Makes autonomously (no human required per response):**
- Pass/fail gate override logic in [`engine/cdfi_calculator.py`](../../../engine/cdfi_calculator.py) — when either gate fires, CDFI_final = min(CDFI_computed, 40). This is the only autonomous decision in the framework, and it caps a score, not a person's access to anything.
- Deployment tier assignment from score (threshold lookup, no judgment)

### Operational boundaries

The CDFI Framework does not:
- Make deployment decisions
- Approve or prohibit any AI product
- Validate model responses as theologically correct (pending human theological review — see [`c4-validation-status.md`](c4-validation-status.md))
- Operate in any production Catholic institution context (it is a methodology framework, not a deployed tool)

### Independent technical reviewer documentation

A technical reviewer without access to the framework authors can assess the framework's actual behavior from:

| Document | What it enables |
|----------|----------------|
| [`docs/specifications/CDFI-formula.md`](../../specifications/CDFI-formula.md) | Reproduce the scoring formula exactly |
| [`configs/authority_matrix.json`](../../../configs/authority_matrix.json) | Inspect all metric weights |
| [`configs/threshold_gates.yaml`](../../../configs/threshold_gates.yaml) | Inspect all gate definitions and tier thresholds |
| [`engine/cdfi_calculator.py`](../../../engine/cdfi_calculator.py) | Run the reference implementation against any score input |
| [`TRACEABILITY.md`](../../../TRACEABILITY.md) | Trace every architectural decision to its source publication |
| [`LIMITATIONS.md`](../../../LIMITATIONS.md) | Identify all known constraints with exact disclosure language |
| [`docs/reliability/judge-reliability-protocol.md`](../../reliability/judge-reliability-protocol.md) | Reproduce the reliability certification protocol |

### AI Extension: Training data sources and distributional limitations

The CDFI Framework does not train AI models. Training data disclosure for evaluated models belongs to the model submitter (see "What the Model Submitter Owns" below).

**Known distributional limitation of the CDFI Framework itself:** The 100 SAICRED v2 questions are in English, authored by a single domain expert (Dr. Filip Ponulak), and cover seven topic domains weighted by Catholic formation priorities. Performance on this dataset does not predict performance on non-English questions, questions from different cultural contexts, or questions outside these seven domains. See [`c5-subgroup-protocol.md`](c5-subgroup-protocol.md).

### AI Extension: Independent audits

Four-part judge reliability certification (all parts cleared May 11, 2026). See [`docs/reliability/judge-reliability-protocol.md`](../../reliability/judge-reliability-protocol.md) and [`c4-validation-status.md`](c4-validation-status.md).

### AI Extension: Autonomous vs. human-review decisions

Stated above under "What decisions it informs or makes."

---

## C7: The Deployment Test

**The 90-day test:** Could the director of technology at a diocesan schools office, working with their team and without access to the framework authors, deploy this framework responsibly within 90 days?

**Answer: Yes.** The evidence:
- [`README.md`](../../../README.md) provides complete deployment instructions
- [`engine/cdfi_calculator.py`](../../../engine/cdfi_calculator.py) runs as a standalone Python module with no external dependencies
- [`configs/`](../../../configs/) files are human-readable JSON/YAML requiring no special tooling to modify
- [`docs/governance/adapting-for-other-traditions.md`](../adapting-for-other-traditions.md) guides adaptation without author involvement
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) defines the correction and adaptation process
- DOI 10.5281/zenodo.20464408 ensures permanent access regardless of author availability

---

## C7: Data Stewardship by Data Type

The CDFI Framework handles none of the five regulated data categories below directly. The table clarifies which requirements apply to projects that build on this framework.

| Data Type | CDCF Compliance Requirement | CDFI Framework Status | Model Submitter Obligation |
|-----------|---------------------------|----------------------|---------------------------|
| Health information | HIPAA compliance; data minimization documented | Not applicable — no health data ingested | If model is deployed in Catholic health system, submitter must document HIPAA compliance |
| Student records | FERPA compliance; retention/deletion procedures | Not applicable — no student data ingested | If model is deployed in Catholic schools, submitter must document FERPA compliance |
| Sacramental data | Diocesan governance policies; access controls documented | Not applicable — no sacramental data ingested | If model processes sacramental records, diocesan data governance policies apply |
| Data pertaining to minors | Enhanced protections; explicit consent; breach response | Not applicable at framework level | If model is used in youth formation contexts, submitter must document enhanced protections |
| Financial information | Applicable state/federal law; audit trail | Not applicable — no financial data ingested | If model processes financial data, applicable law and audit requirements apply |

---

## What the Model Submitter Owns

Any CDCF project submission that uses the CDFI Framework as part of its validation must address the following — not in this document, but in the submission materials for the specific AI model or product:

```
Model Submitter C3/C7 Obligations
────────────────────────────────────────────────────────────────

Training data sources and distributional limitations
  → Which training data sources are relevant to Catholic
    doctrinal content?
  → What is the known representation of Catholic magisterial
    documents in training data vs. general Christian or
    secular content?

Training data from Catholic institutions
  → Was any data from Catholic institutions (parish records,
    catechetical materials, diocesan publications) used in training?
  → Under what terms was it used?
  → Do institutions retain rights to request data removal?

Future model update terms
  → Under what terms may Catholic institution data be used
    in future model updates?
  → What is the process for notifying deploying institutions
    when training data terms change?

Version notification commitment
  → The submitter must commit to notifying deploying institutions
    of major version updates within 30 days of release,
    to trigger the CDFI temporal versioning protocol
```

**The Handoff Clause**

Any CDCF project submission using CDFI Framework scores must include a signed statement from the model developer confirming:

1. Training data sources relevant to Catholic doctrinal content have been disclosed to the submitting institution
2. The developer will notify the deploying institution of major version updates within 30 days of release
3. No Catholic institutional data was used in training without explicit institutional consent

The CDFI Framework cannot verify these statements. That verification belongs to the CDCF review process.

---

## Canonical and Magisterial Citations

- Dicastery for the Doctrine of the Faith, *Antiqua et Nova*, January 28, 2025. https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html

- Julia Angwin, Jeff Larson, Surya Mattu, and Lauren Kirchner, "Machine Bias," *ProPublica*, May 23, 2016. https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

---

*Related: [c1-canonical-scope.md](c1-canonical-scope.md)*

*Related: [c2-human-accountability.md](c2-human-accountability.md)*

*Related: [c4-validation-status.md](c4-validation-status.md)*

*Related: [c5-subgroup-protocol.md](c5-subgroup-protocol.md)*

*Related: [c6-deployment-governance.md](c6-deployment-governance.md)*

*Related: [c8-configuration-boundary.md](c8-configuration-boundary.md)*

*Related: [LIMITATIONS.md](../../../LIMITATIONS.md)*

*Related: [TRACEABILITY.md](../../../TRACEABILITY.md)*
