# Changelog

*CDFI Framework — Version history and re-evaluation record*

---

> CDFI scores expire on major model version updates per the temporal versioning protocol ([`docs/governance/temporal-versioning.md`](docs/governance/temporal-versioning.md)). This changelog is the authoritative record of every evaluation run, methodology change, and score revision. It is a living document.

---

## Framework v1.0 — May 2026

**Initial release. Reference implementation of the CDFI methodology derived from seven Anthropic AI safety research publications.**

### What was established

- CDFI formula and four-column weighting matrix — [`docs/specifications/CDFI-formula.md`](docs/specifications/CDFI-formula.md)
- Five failure mode taxonomy — [`docs/specifications/failure-taxonomy.md`](docs/specifications/failure-taxonomy.md)
- Two pass/fail cap gates: hallucination and relativism resistance — [`configs/threshold_gates.yaml`](configs/threshold_gates.yaml)
- Four deployment tiers: Formation and Catechesis (85+), General Information (70–84), R&D Only (50–69), Not Recommended (below 50) — [`docs/specifications/deployment-tiers.md`](docs/specifications/deployment-tiers.md)
- Four-part judge reliability certification protocol — [`docs/reliability/judge-reliability-protocol.md`](docs/reliability/judge-reliability-protocol.md)
- Seven research-to-architecture translation documents — [`docs/translations/`](docs/translations/)
- Reference implementation of the CDFI formula — [`engine/cdfi_calculator.py`](engine/cdfi_calculator.py)
- Weighting matrix and gate configurations — [`configs/authority_matrix.json`](configs/authority_matrix.json)
- Complete traceability from source publications to formula elements — [`TRACEABILITY.md`](TRACEABILITY.md)
- Six disclosed limitations with exact language — [`LIMITATIONS.md`](LIMITATIONS.md)

### Reliability certification history

| Run | Date | Parts Tested | Result | Key Finding |
|-----|------|:------------:|--------|-------------|
| Run 1 | Apr 29, 2026 | 1, 2, 3, 4 | FAIL | Part 1 blocker: `confidence_calibration` kappa 0.487. Part 2: anchor accuracy 79.9%. Part 4: cap gate accuracy 65% |
| Run 2 | May 4, 2026 | 4 | FAIL | Part 4: 80% accuracy. Root cause: context question mismatch in test construction, not gate malfunction |
| Run 3 | May 6, 2026 | 1 | FAIL | Part 1 still failing; rubric revision in progress |
| Run 4 | May 6, 2026 | 1 | FAIL | Confidence calibration rubric revision continued |
| Run 5 | May 7, 2026 | 1 | **PASS** | `confidence_calibration` kappa improved to **0.831** after rubric revision with concrete score band examples. All Critical metrics cleared ≥ 0.60 |
| Run 6 | May 7, 2026 | 2 | **PASS** | Anchor calibration: **98.3%** accuracy (up from 79.9%) |
| Run 7 | May 11, 2026 | 4 | **PASS** | Cap gate precision: **100%** after two-stage question-pairing fix |

**Certification cleared: May 11, 2026. All four parts passing. `publication_ready: true`.**

Full protocol: [`docs/reliability/judge-reliability-protocol.md`](docs/reliability/judge-reliability-protocol.md)
Publication gates: [`docs/reliability/publication-gates.md`](docs/reliability/publication-gates.md)

### Final Part 1 kappa values (May 7, 2026, n=50)

| Metric | kappa | Status |
|--------|:-----:|--------|
| Hallucination | 1.000 | STRONG |
| Relativism Resistance | 0.846 | STRONG |
| Source Citation | 0.859 | STRONG |
| Confidence Calibration | 0.831 | STRONG |
| Completeness | 0.802 | STRONG |
| Doctrinal Precision | 0.644 | SUBSTANTIAL |
| Moral Fidelity | 0.636 | SUBSTANTIAL |
| Stability | — | Hardcoded (deferred to v2.1) |
| Pastoral Appropriateness | 0.352 | UNRELIABLE (disclosed — weight 0.02–0.05) |

---

## SAICRED v2 Benchmark Results — May 2026

**100 questions × 4 framings × 6 models = 2,400 responses. 21,599 metric scores.**

Full results: [`examples/saicred-v2/results-summary.md`](examples/saicred-v2/results-summary.md)
Primary policy finding: [`examples/saicred-v2/framing-effect-analysis.md`](examples/saicred-v2/framing-effect-analysis.md)

### Rankings (preliminary — authority level classification pending)

| Rank | Model | Mean CDFI | 95% CI (clustered) | Median | Cap Rate | Tier |
|:----:|-------|:---------:|:------------------:|:------:|:--------:|------|
| 1 | o3 | 85.0 | [83.0, 87.0] | 94.0 | 8.0% | **Formation and Catechesis** |
| 2 | DeepSeek V4 | 83.4 | [80.6, 86.2] | 91.6 | 12.5% | General Information |
| 3 | Gemini 3.1 Pro | 82.5 | [80.2, 84.8] | 91.6 | 14.5% | General Information |
| 4 | GPT-5.4 | 82.1 | [80.6, 83.7] | 84.4 | 8.0% | General Information |
| 5 | Grok 4 | 82.1 | [79.5, 84.7] | 94.0 | 15.3% | General Information |
| 6 | Claude Sonnet 4.6 | 78.0 | [76.1, 79.8] | 89.2 | 17.0% | General Information |

*95% CIs use clustered standard errors at topic_domain level (G=7). Only the Grok 4 vs. Claude Sonnet 4.6 gap reaches significance at 95% confidence (p=0.008).*

### Framing effect (mean CDFI by variant)

| Model | Neutral | Christian | Catholic | Adversarial | Gap (C − A) |
|-------|:-------:|:---------:|:--------:|:-----------:|:-----------:|
| o3 | 84.9 | 81.9 | 86.2 | 87.0 | **−0.8** |
| GPT-5.4 | 78.0 | 79.3 | 87.8 | 83.3 | +4.5 |
| Gemini 3.1 Pro | 79.5 | 78.2 | 90.3 | 82.0 | +8.3 |
| Grok 4 | 75.0 | 83.1 | 90.7 | 79.6 | +11.1 |
| DeepSeek V4 | 77.1 | 84.3 | 91.6 | 80.4 | +11.2 |
| Claude Sonnet 4.6 | 74.3 | 74.6 | 89.4 | 73.6 | **+15.8** |

### Cap event breakdown

| Model | Relativism only | Both gates | Hallucination only | Total | Rate |
|-------|:---------------:|:----------:|:-----------------:|:-----:|:----:|
| Claude Sonnet 4.6 | 42 | 20 | 7 | 69 | 17.3% |
| Grok 4 | 44 | 13 | 7 | 64 | 16.0% |
| Gemini 3.1 Pro | 36 | 15 | 7 | 58 | 14.5% |
| DeepSeek V4 | 27 | 12 | 11 | 50 | 12.5% |
| GPT-5.4 | 18 | 11 | 3 | 32 | 8.0% |
| o3 | 14 | 5 | 13 | 32 | 8.0% |
| **Total** | **181** | **76** | **48** | **305** | **12.7%** |

### Open publication gates at time of v1.0 release

| Gate | Document | Status |
|------|----------|--------|
| Judge reliability certification | [`docs/reliability/publication-gates.md`](docs/reliability/publication-gates.md) | **CLEARED — May 11, 2026** |
| Authority level classification (400 prompts) | [`docs/governance/cdcf-compliance/c4-validation-status.md`](docs/governance/cdcf-compliance/c4-validation-status.md) | Pending — theological advisors |
| Human theological review (21,599 scores) | [`docs/governance/cdcf-compliance/c4-validation-status.md`](docs/governance/cdcf-compliance/c4-validation-status.md) | Pending — Filip Ponulak + advisors |
| Stability scoring (5 runs/prompt) | [`docs/specifications/scoring-anchors.md`](docs/specifications/scoring-anchors.md) | Deferred to v2.1 |

---

## Framework v1.1 — May 2026

**Translation methodology documentation added.**

### What was added

| File | Description |
|------|-------------|
| [`TRANSLATION-METHOD.md`](TRANSLATION-METHOD.md) | Seven-step methodology document: how each source publication became a computable CDFI mechanism. Includes the full translation map table, the ninth metric's two-paper derivation as a flow diagram, and the empirical validation record |
| [`docs/translations/README.md`](docs/translations/README.md) | Navigation guide with audience routing table and relationship map to specifications, configs, and engine |
| [`docs/specifications/scoring-anchors.md`](docs/specifications/scoring-anchors.md) | Concrete score-level examples using real SAICRED v2 model responses and judge reasoning from `scores_full.csv`. Includes the Central Illustration: same question answered by Claude neutral framing (CDFI 40, gate fires), Claude catholic framing (CDFI 94, all 5s), and o3 adversarial framing (CDFI 94, framing-invariant) |

### What was corrected

| File | Correction |
|------|-----------|
| [`docs/translations/02-rubric-reliability.md`](docs/translations/02-rubric-reliability.md) | Kappa threshold corrected from 0.70 to 0.60, matching `KAPPA_BLOCKER` in `test_judge_reliability.py` |
| [`docs/translations/05-framing-sensitivity.md`](docs/translations/05-framing-sensitivity.md) | Claude framing gap corrected to 15.8, Catholic framing to 89.4, o3 gap to −0.8. All verified against `cdfi_scores_full.csv` |
| [`docs/translations/01-evaluation-criteria.md`](docs/translations/01-evaluation-criteria.md) through [`docs/translations/08-confidence-calibration.md`](docs/translations/08-confidence-calibration.md) | All eight translation files rebuilt with seven-step pipeline format |

---

## Framework v1.2 — May 2026

**CDCF compliance documentation added (first pass).**

### What was added

| File | Description |
|------|-------------|
| [`docs/governance/cdcf-compliance/README.md`](docs/governance/cdcf-compliance/README.md) | Status overview and audience routing for all eight criteria |
| [`docs/governance/cdcf-compliance/c1-canonical-scope.md`](docs/governance/cdcf-compliance/c1-canonical-scope.md) | Mission alignment and canonical scope |
| [`docs/governance/cdcf-compliance/c2-human-accountability.md`](docs/governance/cdcf-compliance/c2-human-accountability.md) | Four-level decision authority matrix |
| [`docs/governance/cdcf-compliance/c3-c7-responsibility-boundary.md`](docs/governance/cdcf-compliance/c3-c7-responsibility-boundary.md) | Framework vs. model submitter obligations |
| [`docs/governance/cdcf-compliance/c4-validation-status.md`](docs/governance/cdcf-compliance/c4-validation-status.md) | Independent validation evidence and open gates |
| [`docs/governance/cdcf-compliance/c5-subgroup-protocol.md`](docs/governance/cdcf-compliance/c5-subgroup-protocol.md) | Vulnerable populations and subgroup protocol |
| [`docs/governance/cdcf-compliance/c6-deployment-governance.md`](docs/governance/cdcf-compliance/c6-deployment-governance.md) | Four decision states; escalation conditions; appeal pathway |
| [`docs/governance/cdcf-compliance/c8-configuration-boundary.md`](docs/governance/cdcf-compliance/c8-configuration-boundary.md) | Locked vs. configurable parameters |

### What was extended

| File | Extension |
|------|-----------|
| [`docs/specifications/deployment-tiers.md`](docs/specifications/deployment-tiers.md) | C6 governance elements appended: decision authority, escalation, review triggers, appeal pathway |
| [`docs/reliability/publication-gates.md`](docs/reliability/publication-gates.md) | C4 cross-reference table appended: CDFI publication gates mapped to C4 validation columns |

---

## Framework v1.3 — May 2026

**CDCF compliance documentation pressure-tested and rebuilt against actual published criteria text.**

### What triggered this version

Systematic gap analysis against [CDCF Project Vetting Criteria v0.2](https://catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria) (published April 29, 2026) identified 24 deficiencies in the v1.2 compliance documents. Every deficiency traced to missing canonical citations, missing case studies, or missing exact requirements from the published criteria text.

### What was corrected — 24 gaps closed

| Criterion | Document | Gaps Closed |
|-----------|----------|------------|
| C1 | [`c1-canonical-scope.md`](docs/governance/cdcf-compliance/c1-canonical-scope.md) | Added spiritual direction to exclusion list; added [*Antiqua et Nova*](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html) and [Pope Leo XIV Nov 2025](https://www.vatican.va/content/leo-xiv/en/messages/pont-messages/2025/documents/20251103-messaggio-builders-aiforum.html) citations; added Father Justin case study; added universality evaluation question |
| C2 | [`c2-human-accountability.md`](docs/governance/cdcf-compliance/c2-human-accountability.md) | Added [Canon 627](https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib2-cann460-572_en.html) verbatim; added [Robodebt Royal Commission](https://robodebt.royalcommission.gov.au/) case; added Pope Francis quote; added committee-without-named-owner explicit failure condition |
| C3 | [`c3-c7-responsibility-boundary.md`](docs/governance/cdcf-compliance/c3-c7-responsibility-boundary.md) | Added inference-time data disclosure; added [COMPAS algorithm case study](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing); added *Antiqua et Nova* dignity/fraternity citation |
| C4 | [`c4-validation-status.md`](docs/governance/cdcf-compliance/c4-validation-status.md) | Added proportionality principle; added conditional graduation path with plan and timeline |
| C5 | [`c5-subgroup-protocol.md`](docs/governance/cdcf-compliance/c5-subgroup-protocol.md) | Added people with disabilities to population list; added [Pope Leo XIV Dec 2025](https://www.vatican.va/content/leo-xiv/en/speeches/2025/december/documents/20251205-conferenza.html) quote; added *Antiqua et Nova* magisterial definition of algorithmic bias |
| C6 | [`c6-deployment-governance.md`](docs/governance/cdcf-compliance/c6-deployment-governance.md) | Added [Canon 1609](https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib7-cann1501-1670_en.html) verbatim with explanation; added governance-as-code pattern; added four decision states (go/conditional-go/no-go/defer); added aspirational vs. required distinction |
| C7 | [`c3-c7-responsibility-boundary.md`](docs/governance/cdcf-compliance/c3-c7-responsibility-boundary.md) | Added 90-day deployment test; added five-category data compliance table (HIPAA/FERPA/Sacramental/Minors/Financial); added future model update terms in handoff clause |
| C8 | [`c8-configuration-boundary.md`](docs/governance/cdcf-compliance/c8-configuration-boundary.md) | Added three named maintainers with public verification paths; added three-severity vulnerability response process; added [*Antiqua et Nova* §42](https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html) and [CCC §1894](https://www.vatican.va/archive/ENG0015/_INDEX.HTM) verbatim |

### Other files updated in v1.3

| File | Change |
|------|--------|
| [`README.md`](README.md) | DOI badge corrected to `20464408`; bibtex version updated to 1.3; compliance folder added to directory tree |
| [`CITATION.cff`](CITATION.cff) | Version updated to 1.3 |
| [`LIMITATIONS.md`](LIMITATIONS.md) | Version header updated to v1.3 |

---

## Framework v1.4 — May 2026

**AI governance framework alignments and security documentation added.**

### What triggered this version

Three governance gaps identified through analysis of the [AI Alliance Trust & Safety User Guide](https://the-ai-alliance.github.io/trust-safety-user-guide/exploring/nist-risk-framework/) and the [LatticeFlow AI Atlas frameworks catalog](https://atlas.latticeflow.ai/frameworks/): no mapping to NIST AI RMF 1.0, no EU AI Act alignment documentation, and three undocumented security attack surfaces in the LLM-as-judge architecture.

### What was added

| File | Description |
|------|-------------|
| [`docs/governance/nist-rmf-mapping.md`](docs/governance/nist-rmf-mapping.md) | Alignment with [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) (January 2023) and [NIST AI 600-1 GenAI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf) (2024). All four functions covered: GOVERN, MAP, MEASURE, MANAGE. 24 sub-functions assessed. Maps CDCF criteria to NIST RMF functions for U.S. Catholic institutional reviewers |
| [`docs/governance/eu-ai-act-mapping.md`](docs/governance/eu-ai-act-mapping.md) | Alignment with [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) (EU AI Act). Articles 9–15 assessed. Articles 11, 13, 14 satisfied. Articles 9, 10, 12, 15 partially satisfied. Fundamental rights impact assessment and conformity assessment documented as open institutional obligations. August 2026 high-risk compliance deadline documented |
| [`docs/governance/security-considerations.md`](docs/governance/security-considerations.md) | Three attack surfaces mapped to [OWASP LLM Top 10 (2025)](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and [MITRE ATLAS](https://atlas.mitre.org/): judge prompt injection (LLM01), scoring pipeline integrity (LLM04/LLM08), authority level classification manipulation (LLM09). Current mitigations documented. Remediations planned for v1.5 |

### What was updated

| File | Change |
|------|--------|
| [`README.md`](README.md) | Status badge updated to v1.4; three new badges added (NIST AI RMF, EU AI Act, OWASP LLM); directory tree updated with three new governance docs; bibtex version updated to 1.4; L7 security limitation added |
| [`CITATION.cff`](CITATION.cff) | Version updated to 1.4 |
| [`LIMITATIONS.md`](LIMITATIONS.md) | Version header updated to v1.4; L7 (security attack surfaces) added |

### Frameworks catalog consulted for this release

| Framework | Source | Decision |
|-----------|--------|---------|
| [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework) | NIST, 2023 | Mapped — high relevance for U.S. Catholic institutional reviewers |
| [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | EU, 2024 | Mapped — mandatory for EU member state deployment |
| [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | OWASP, 2025 | Referenced in security document — high relevance for judge architecture |
| [MITRE ATLAS](https://atlas.mitre.org/) | MITRE, 2020–2026 | Referenced in security document |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) | ISO, 2023 | Deferred to v1.5 |
| [ISO/IEC 23894:2023](https://www.iso.org/standard/77304.html) | ISO, 2023 | Deferred to v1.5 |
| FINMA, NYC LL144, Colorado AI Act | Various | Not applicable — financial and employment contexts |
| Healthcare-specific frameworks | Various | Not applicable — no clinical use cases |

---

## Upcoming: SAICRED v2.1

**Planned additions:**

- Five-run stability scoring (removes hardcoded stability = 3.0) — see [`docs/specifications/scoring-anchors.md`](docs/specifications/scoring-anchors.md)
- Authority level classification applied — final CDFI scores replace preliminary scores
- Human theological review completed per [Addendum E](docs/governance/cdcf-compliance/c4-validation-status.md) — full publication weight achieved
- Updated rankings with complete four-column matrix applied — see [`configs/authority_matrix.json`](configs/authority_matrix.json)
- Non-English subgroup evaluation (Spanish priority) — see [`docs/governance/cdcf-compliance/c5-subgroup-protocol.md`](docs/governance/cdcf-compliance/c5-subgroup-protocol.md)

## Upcoming: Framework v1.5

**Planned additions:**

- [`docs/governance/iso-42001-mapping.md`](docs/governance/) — ISO/IEC 42001:2023 AI Management System Standard alignment
- Security remediations: Part 5 reliability certification (prompt injection resistance); SHA-256 hash verification of results files
- Authority level classification file cryptographic sign-off process

---

*Framework maintained by: [Mark Julius Banasihan](https://github.com/mj3b) | [ORCID: 0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)*

*SAICRED v2 pipeline maintained by: [Naveen Kumar Puppala](https://github.com/naveenp2708)*

*Theological and publication authority: Filip Ponulak, PhD and the Catholic Digital Commons Foundation*
