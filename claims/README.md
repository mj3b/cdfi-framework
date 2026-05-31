# `claims/` — Machine-Readable Evidence Packs

**CDFI Framework v1.4** | DOI: [10.5281/zenodo.20475185](https://doi.org/10.5281/zenodo.20475185)

---

This folder contains eight JSON files — one per Anthropic AI safety research publication used to build the CDFI. Each file is a structured evidence pack: the verbatim paper extracts, inference chains, claim types, and computable artifacts that together prove how a published research finding became a specific CDFI mechanism.

These files are machine-readable companions to the markdown translation documents in [`docs/translations/`](../docs/translations/). Every claim in a JSON file corresponds directly to a named evidence item (`E1`–`E4`) in its paired markdown document. A researcher who wants to understand the derivation reads the markdown. A tool that wants to audit the derivation reads the JSON.

---

## File Index

| JSON File | Publication | Translation Doc | CDFI Mechanism Produced |
|-----------|-------------|-----------------|------------------------|
| [`pub1-evaluation-criteria.json`](pub1-evaluation-criteria.json) | Challenges in Evaluating AI Systems (Anthropic, 2023) | [`01-evaluation-criteria.md`](../docs/translations/01-evaluation-criteria.md) | Four-column authority-sensitive weighting matrix |
| [`pub1-rubric-reliability.json`](pub1-rubric-reliability.json) | Challenges in Evaluating AI Systems (Anthropic, 2023) | [`02-rubric-reliability.md`](../docs/translations/02-rubric-reliability.md) | Four-part judge reliability certification; kappa ≥ 0.60 publication gate |
| [`pub2-hallucination-gate.json`](pub2-hallucination-gate.json) | Auditing Language Models for Hidden Objectives (Anthropic, 2025) | [`03-hallucination-gate.md`](../docs/translations/03-hallucination-gate.md) | Hallucination pass/fail gate; `CAP_VALUE = 40` |
| [`pub3-statistical-rigor.json`](pub3-statistical-rigor.json) | A Statistical Approach to Model Evaluations (Anthropic, 2024) | [`04-statistical-rigor.md`](../docs/translations/04-statistical-rigor.md) | 95% CI; clustered SE (G=7); deployment tier thresholds; temporal versioning |
| [`pub4-framing-sensitivity.json`](pub4-framing-sensitivity.json) | Discrimination in Language Model Decisions (Anthropic, 2023) | [`05-framing-sensitivity.md`](../docs/translations/05-framing-sensitivity.md) | Four-variant prompt structure; relativism resistance gate |
| [`pub5-confidence-calibration.json`](pub5-confidence-calibration.json) | CoT Faithfulness (2023) + Discrimination (2023) | [`08-confidence-calibration.md`](../docs/translations/08-confidence-calibration.md) | Confidence calibration metric — ninth metric, original construct |
| [`pub6-categorical-failures.json`](pub6-categorical-failures.json) | Sabotage Evaluations (Anthropic, 2024) | [`07-categorical-failures.md`](../docs/translations/07-categorical-failures.md) | Five failure mode taxonomy; cap gate architecture |
| [`pub7-adversarial-probing.json`](pub7-adversarial-probing.json) | Evaluating Feature Steering (Anthropic, 2024) | [`06-adversarial-probing.md`](../docs/translations/06-adversarial-probing.md) | Adversarial prompt variant; prompt sensitivity drift failure mode |

> **Note on numbering.** JSON file names track the source publication (`pub1`–`pub7`). Translation document names track the order in which mechanisms appear in the CDFI scoring sequence (`01`–`08`). Publication 1 produced two translations (01 and 02). Publication 4 appears in both `pub4-framing-sensitivity.json` and `pub5-confidence-calibration.json` because it is one of two papers that jointly produced the ninth metric. The table above maps between both numbering systems.

---

## Why Two Files from Publication 1

Publication 1 (*Challenges in Evaluating AI Systems*) produced two architecturally distinct mechanisms. `pub1-evaluation-criteria.json` covers the domain-specificity finding: evaluation criteria must match the domain's own authority structure, which produces the four-column weighting matrix. `pub1-rubric-reliability.json` covers the evaluator consistency finding: a rubric applied differently by independent judges is measuring judge subjectivity rather than response quality, which produces the four-part certification protocol.

A rubric can satisfy the first condition (correctly designed for its domain) while failing the second (applied inconsistently by the judge). The confidence calibration metric passed the domain-design test on its first iteration and failed the consistency test (kappa = 0.487) until the 2/3 score boundary was anchored with concrete examples. Both conditions must hold independently before any score is defensible.

---

## Why One File Covers Two Publications

`pub5-confidence-calibration.json` draws from two papers because no single paper produces the Step 1 claim for the confidence calibration metric. Publication 5 (CoT Faithfulness) establishes that stated reasoning chains do not reliably reflect the model's actual process. Publication 4 (Framing Discrimination) establishes that certainty expression shifts with framing variation. Neither paper asks the question that falls out of holding both simultaneously: does the model express certainty appropriate to the *doctrinal authority level* of the claim it is making, independent of framing and independent of stated reasoning quality? That question is an original construct, documented as such in SAICRED Implementation Guidelines Section 3.2. The file carries an explicit `Original Construct` claim type for E3, with an empty `verbatim_extracts` array and a `verbatim_extract_absence_explanation` field. The absence is intentional and honest.

---

## Relationship to Applied AI Research Translator

This folder was designed with reference to the [applied-ai-research-translator](https://github.com/mj3b/applied-ai-research-translator) — a governed system for translating applied AI research into auditable, decision-ready artifacts. That repo established the foundational concept this folder operationalizes: research findings should produce machine-readable claims with verbatim evidence, typed by how directly the paper supports them, traceable to specific computable artifacts.

The CDFI claims folder is not a direct implementation of the translator. It is a tailored adaptation for a different use case — benchmark methodology traceability rather than production deployment decisions. The table below documents exactly what was adopted, what was changed, and what was not used.

| Element | Translator Repo | CDFI `claims/` Folder | Why the Change |
|---------|----------------|----------------------|----------------|
| Core concept | Machine-readable claims packs with verbatim extracts | Adopted directly | The use case is identical at this level |
| Claim typing | Direct / Derived | Direct / Derived / **Original Construct** added | The CDFI's ninth metric is a domain-original intellectual contribution — the translator processes existing findings, not new ones |
| Deployment artifact field | Maps claim to a production system component | Renamed `cdfi_element_produced`; typed with 20 specific `type` values | CDFI artifacts are gate constants, column weights, certification parts, and scoring rules — not production system components |
| Translation step mapping | Translator's pipeline steps | `translation_step` maps to the seven-step CDFI methodology pipeline | Different pipeline, same structural concept |
| Single-paper assumption | One file per publication | Two files from Publication 1; one file spanning two publications | The CDFI's architecture required these exceptions; the schema accommodates them explicitly |
| Cross-file references | Not present — translator processes papers independently | Added in three files to model inter-paper dependencies | The CDFI architecture has real dependencies: pub6 depends on pub2 and pub4; pub5 draws from pub4 |
| Evidence completeness block | Not present in translator schema | Added as `evidence_completeness` | Required to handle the Original Construct case honestly — `all_claims_have_verbatim_extracts: false` is a valid and documented state |
| Runloop / governed execution | Automated loop with human gate | Not adopted | CDFI scoring runs require human judgment throughout; an automated loop would misrepresent the governance model |
| `packs/` folder convention | Translation outputs stored in `packs/` | Renamed to `claims/` | Signals the specific function — these are evidence packs for methodology traceability, not full translation packs for deployment decisions |

The `cdfi_element_produced` field is the most substantial adaptation. The translator's equivalent field names a production system component — a model, an API, a deployment configuration. The CDFI version names a computable benchmark artifact: a column weight value, a gate constant, a certification part threshold, a scoring rule. The 20 `type` values in this folder's schema (documented in the Schema Reference section below) emerged from mapping each paper claim to the specific artifact it produced in the CDFI architecture. None of the translator's existing type values transferred without modification.

---

## Schema Reference

Every JSON file in this folder follows the same top-level structure.

```
{
  "schema_version":            string  — currently "1.0"
  "cdfi_framework_version":    string  — currently "1.4"
  "doi":                       string  — Zenodo DOI for this framework version
  "translation_document":      string  — path to paired markdown file
  "source_publication":        object  — bibliographic record (or "source_publications" array for pub5)
  "translation_note":          string  — why the paper connection is or is not obvious
  "cdfi_mechanism_produced":   object  — the artifact this translation produced
  ...mechanism-specific data blocks...
  "claims":                    array   — the evidence items (see below)
  "evidence_completeness":     object  — audit summary
}
```

### The `claims` Array

Each element in `claims` represents one evidence item from the paired markdown document.

```
{
  "claim_id":              string  — matches E1, E2, E3, E4 in the markdown
  "claim_type":            string  — "Direct", "Derived", or "Original Construct"
  "translation_step":      int     — which of the seven pipeline steps this anchors (1-7)
  "claim_summary":         string  — one-sentence description of the claim
  "verbatim_extracts":     array   — one or more objects with "text" and "location" fields
  "inference_chain":       string  — how the paper finding translates to the CDFI mechanism
  "cdfi_element_produced": object  — the specific artifact this claim produced (see below)
}
```

### Claim Types

| Type | Meaning | Verbatim Extract | Inference Chain |
|------|---------|:----------------:|:---------------:|
| `Direct` | Paper states the claim explicitly | Required | Shown (may be short) |
| `Derived` | Paper implies the claim; reasoning required | Required | Required and explicit |
| `Original Construct` | No paper states the claim — emerges from combining findings | Empty array | `convergence_logic` field instead |

### The `cdfi_element_produced` Field

This is the bridge between the research claim and the computable CDFI artifact. Its `type` field distinguishes what kind of artifact was produced:

| `type` value | What it means | Example |
|---|---|---|
| `weighting_matrix_architecture` | A column or weight in `configs/authority_matrix.json` | E3 in pub1-evaluation-criteria |
| `publication_prerequisite` | A required step before final scores can be computed | E2 in pub1-evaluation-criteria |
| `publication_gate` | A threshold that must clear before scores enter publication | E4 in pub1-evaluation-criteria |
| `certification_part` | One of the four parts of `test_judge_reliability.py` | E1 in pub1-rubric-reliability |
| `execution_protocol` | The independence/collaboration structure of certification execution | E4 in pub1-rubric-reliability |
| `gate_architecture_justification` | The structural argument for why a gate is binary rather than scored | E1 in pub2-hallucination-gate |
| `gate_scope` | Which prompt variants the gate applies to | E2 in pub2-hallucination-gate |
| `cap_gate_override` | The `CAP_VALUE = 40` override logic | E4 in pub2-hallucination-gate |
| `statistical_requirement` | A statistical method required in the scoring pipeline | E1–E3 in pub3-statistical-rigor |
| `deployment_tiers_and_versioning` | The 85/70/50 thresholds and temporal versioning protocol | E4 in pub3-statistical-rigor |
| `prompt_structure` | The four-variant prompt design | E1 in pub4-framing-sensitivity |
| `adversarial_variant_design_rationale` | Why the adversarial variant is designed as it is | E2 in pub4-framing-sensitivity |
| `prompt_playbooks_rationale` | The empirical basis for the Prompt Playbooks deliverable | E3 in pub4-framing-sensitivity |
| `failure_mode_definition` | A named failure mode in Section 3.3 of the Implementation Guidelines | E2 in pub7-adversarial-probing |
| `adversarial_variant_requirement` | Why the adversarial variant is architecturally required | E1 in pub7-adversarial-probing |
| `analysis_scope_requirement` | Why analysis must span all seven topic domains | E4 in pub7-adversarial-probing |
| `failure_taxonomy_architecture` | The categorical/gradational distinction across all five failure modes | E1 in pub6-categorical-failures |
| `cap_gate_design_principle` | The conservative binary design principle for both gates | E2 in pub6-categorical-failures |
| `gate_vs_metric_distinction` | Why gates assess occurrence rather than severity | E3 in pub6-categorical-failures |
| `metric_design_principle` | A principle governing how a rubric metric is scored | E1, E2 in pub5-confidence-calibration |
| `original_metric` | A metric with no direct source paper — original construct | E3 in pub5-confidence-calibration |

---

## Cross-File References

Several files reference other files in this folder. These references model the dependency structure of the CDFI architecture.

```
pub6-categorical-failures.json
  ├── E1 → cross_references.citation_fabrication_gate → pub2-hallucination-gate.json
  ├── E1 → cross_references.relativization_gate       → pub4-framing-sensitivity.json
  └── E4 → diagnostic_detail_reference                → pub1-rubric-reliability.json

pub7-adversarial-probing.json
  └── E2 → escalation                                 → pub4-framing-sensitivity.json

pub5-confidence-calibration.json
  ├── E1 → source_publication_id                      → pub5 (CoT Faithfulness)
  └── E2 → source_publication_id                      → pub4 (Framing Discrimination)
```

The full dependency graph — which publications produced which mechanisms, and which mechanisms depend on others — is documented in [`TRACEABILITY.md`](../TRACEABILITY.md) at the repository root.

---

## Mechanism-Specific Data Blocks

Several files carry top-level blocks with empirical data from the SAICRED v2 benchmark run. These blocks sit alongside `claims` rather than inside any individual claim, because they represent the mechanism's empirical record as a whole.

| File | Top-Level Data Block | Contents |
|------|---------------------|----------|
| `pub1-rubric-reliability.json` | `certification_history` | Seven-run certification history with dates, results, and blockers |
| `pub2-hallucination-gate.json` | `saicred_v2_gate_results` | Hallucination gate event counts and rates by model |
| `pub3-statistical-rigor.json` | `saicred_v2_statistical_results` | Pairwise significance table; GPT-5.4 rounding artifact |
| `pub4-framing-sensitivity.json` | `saicred_v2_framing_results` | Framing gap by model; Claude relativism failure breakdown |
| `pub5-confidence-calibration.json` | `judge_reliability` | Kappa history for confidence calibration metric |
| `pub6-categorical-failures.json` | `saicred_v2_cap_results` | Cap event counts and rates by model and gate type |

---

## Validation Notes

Tools that validate this folder should treat the following as correct behavior, not errors:

**`pub1-evaluation-criteria.json` and `pub1-rubric-reliability.json` share a `source_publication`** with identical bibliographic data. This is intentional — both files derive from the same paper. The distinction is in what each file's `cdfi_mechanism_produced` names as the artifact.

**`pub5-confidence-calibration.json` uses `source_publications` (plural array)** rather than `source_publication` (singular object). Both schemas are valid. A tool that requires singular source publication should treat this file as an exception and consult the `translation_note` field for the rationale.

**`pub5-confidence-calibration.json` has `all_claims_have_verbatim_extracts: false`** in `evidence_completeness`. This is correct. E3 is an `Original Construct` claim with an empty `verbatim_extracts` array. The absence is documented in `verbatim_extract_absence_explanation`. Automated validators should be configured to treat `Original Construct` claims as exempt from the verbatim extract requirement.

---

## Relationship to Other Repository Documents

| Document | Relationship to This Folder |
|----------|---------------------------|
| [`docs/translations/`](../docs/translations/) | Paired markdown documents — human-readable companions to each JSON file |
| [`TRANSLATION-METHOD.md`](../TRANSLATION-METHOD.md) | Defines the seven-step pipeline that each claim's `translation_step` field references |
| [`TRACEABILITY.md`](../TRACEABILITY.md) | Summary table: all publications → all mechanisms in one view |
| [`configs/authority_matrix.json`](../configs/authority_matrix.json) | The weight values produced by `pub1-evaluation-criteria.json` and `pub5-confidence-calibration.json` |
| [`configs/threshold_gates.yaml`](../configs/threshold_gates.yaml) | The gate constants produced by `pub2-hallucination-gate.json`, `pub4-framing-sensitivity.json`, and `pub6-categorical-failures.json` |
| [`engine/cdfi_calculator.py`](../engine/cdfi_calculator.py) | The reference implementation of all scoring rules produced by this folder |
| [`test_judge_reliability.py`](../test_judge_reliability.py) | The certification suite produced by `pub1-rubric-reliability.json` |

---

*Mark Julius Banasihan | May 2026*

*DOI: [10.5281/zenodo.20475185](https://doi.org/10.5281/zenodo.20475185) | ORCID: [0009-0001-8121-2878](https://orcid.org/0009-0001-8121-2878)*
