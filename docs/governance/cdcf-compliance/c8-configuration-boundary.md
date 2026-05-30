# C8 — Governance, Maintenance, and Subsidiarity Compatibility

**CDCF Criterion Version:** v0.2 | Gate 2 — Required for Graduation to Active CDCF Project Status
**Criterion Text:** [catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria#criterion-8](https://catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria)

---

## Doctrinal and Canonical Grounding

*Antiqua et Nova* §42 (Dicastery for the Doctrine of the Faith, January 28, 2025) is explicit: the responsibility for managing technology wisely "pertains to every level of society, guided by the principle of subsidiarity." A project that functions only under conditions of centralized administration concentrates authority in ways that violate this principle and undermine the ecclesial structure the CDCF exists to serve.

The *Catechism of the Catholic Church* §1894 defines subsidiarity precisely: it is "a guarantee that each level of authority retains its proper duties and rights regarding the common good." Subsidiarity is not a delegation principle — moving decisions to the lowest available level. It is a guarantee that no larger entity absorbs the legitimate initiative and responsibility of smaller ones. In this framework's context, it means a diocese that wants to configure deployment tier thresholds for its own risk profile retains the right to do so, and the framework is architecturally designed to enable that without requiring the diocese to request permission or override safety mechanisms.

**Canon 627** grounds the governance process requirement: consequential authority is always tied to specific individuals operating within defined systems of consultation. The named maintainer requirement below operationalizes this canon at the project level.

---

## Ongoing Maintenance

**Named maintainer accepting public accountability:**

| Role | Named Person | Public Accountability |
|------|-------------|----------------------|
| Methodology author and primary maintainer | Mark Julius Banasihan | GitHub: github.com/mj3b | ORCID: 0009-0001-8121-2878 | DOI: 10.5281/zenodo.20464408 |
| Production pipeline maintainer | Naveen Kumar Puppala | GitHub: github.com/naveenp2708 |
| Theological and publication authority | Dr. Filip Ponulak | Catholic Digital Commons Foundation |

Public accountability means: any institution relying on this framework can identify these individuals by name, verify their credentials via ORCID and GitHub, and reach them through the contact information in the repository. The DOI provides a permanent, citable record of the methodology version they relied on.

**Version control process:**

CHANGELOG.md records every version with:
- Date and version number
- Files changed and rationale
- Reliability certification run history (SAICRED v2: seven runs, May 2026)
- Open gates and their status

Every architectural change to the scoring methodology requires a new version with a new Zenodo DOI. Score comparisons across versions are not valid without explicit version-alignment documentation.

**Community governance process:**

CONTRIBUTING.md defines three categories of accepted contribution:
1. Adaptations for other religious traditions (documented with authority level substitutions)
2. Corrections to methodology documentation (must trace to named source)
3. Engine improvements (test coverage, edge cases, formula documentation)

Changes to weights, gate logic, or tier thresholds require documented justification tracing to a named source or empirical finding. Undocumented changes to numerical parameters are not accepted.

---

## Vulnerability Response Process

Any identified security vulnerability, scoring logic error, or gate malfunction that could cause a Catholic institution to make a materially incorrect deployment decision follows this process:

```
SEVERITY 1 — Gate malfunction (either pass/fail gate not firing correctly)
  → Immediate: Issue filed on GitHub with label "gate-integrity"
  → Within 24 hours: Evals Expert assesses scope of affected scores
  → Within 72 hours: Corrected version committed; new DOI issued
  → Notification: All known institutional users notified via
    GitHub release notes and repository README banner
  → Disclosure: CHANGELOG.md documents the malfunction, affected
    version range, and correction

SEVERITY 2 — Scoring logic error (formula produces incorrect CDFI
             for a specific input combination)
  → Within 48 hours: Issue documented with reproducible example
  → Within 7 days: Corrected version committed; new DOI issued
  → Notification: GitHub release notes

SEVERITY 3 — Documentation error (text misrepresents behavior
             but implementation is correct)
  → Within 14 days: Corrected documentation committed
  → Notification: GitHub release notes
```

**Gate integrity is Severity 1 by definition.** Any confirmed malfunction in the hallucination gate or relativism resistance gate means deployed institutions may have authorized models based on scores that did not correctly apply the categorical failure architecture. That exposure requires immediate response.

---

## Subsidiarity-Compatible Configuration

The CDCF criterion requires that local configuration capacity be "architecturally genuine, requiring no override of the project's core accountability, safety, or governance design in order to function." This section states what is genuinely configurable, what is locked, and why the distinction preserves subsidiarity rather than limiting it.

### Locked Parameters

These parameters cannot be changed by a local deployer without producing a different scoring instrument that should not be called CDFI.

```
LOCKED 1: Cap gate values
  configs/threshold_gates.yaml
  hallucination.cap_value = 40
  relativism_resistance.cap_value = 40

  Why locked: Raising the cap would allow categorical failures —
  fabricated magisterial citations, defined doctrine treated as
  opinion — to contribute positively to a mean CDFI. That would
  undermine the gate architecture's entire purpose: ensuring
  categorical failures cannot be averaged away.

  Subsidiarity note: A diocese that wants a 60-point cap is
  building a different instrument. They may do so under Apache 2.0.
  They should not cite this framework's DOI for that instrument.

LOCKED 2: Gate firing conditions (binary logic)
  hallucination.fires_when = FAIL
  relativism_resistance.fires_when = FAIL

  Why locked: Converting either gate to a scored metric collapses
  the categorical/gradational distinction. The entire architecture
  depends on this boundary remaining binary.

LOCKED 3: Column sum constraint (all columns must sum to 1.00)
  configs/authority_matrix.json

  Why locked: The CDFI is a 0-100 scale only if weights sum to 1.00
  and metric scores are normalized by multiplying by 20. Deviation
  from 1.00 produces a number that is not a CDFI score and cannot
  be compared to any published threshold.
```

### Configurable Parameters

These parameters are designed to be adapted for local institutional context, different religious traditions, or different risk profiles. Local configuration of these parameters is the operational expression of subsidiarity.

```
CONFIGURABLE 1: Deployment tier thresholds
  configs/threshold_gates.yaml :: deployment_tiers
  Default: 85 (Formation) / 70 (General Information) / 50 (R&D)

  A diocese with access to additional validation data, a religious
  order with higher formation standards, or a tradition with
  different risk tolerance may set different thresholds with
  documented justification. The thresholds are the interface
  between the methodology and institutional discernment.

  Required: Document the new thresholds and the institutional
  reasoning. Scores cannot be compared to published CDFI tiers
  using different thresholds without explicit disclosure.

CONFIGURABLE 2: Authority level column weights
  configs/authority_matrix.json :: authority_levels

  The four-column structure (defined_dogma, ordinary_magisterium,
  theological_consensus, legitimate_opinion) reflects Catholic
  doctrinal authority. Another tradition substitutes its own
  authority structure here — the columns, their names, and their
  weights are all replaceable. See adapting-for-other-traditions.md.

  Required: All columns must still sum to 1.00. Document the
  tradition and authority levels before publication.

CONFIGURABLE 3: Default authority level
  configs/authority_matrix.json :: default_level
  Default: "ordinary_magisterium"

  A tradition with a different primary authority level for
  unclassified questions sets this to the appropriate default.

CONFIGURABLE 4: Judge reliability thresholds
  The kappa ≥ 0.60 and ≥ 90% accuracy thresholds are defaults.
  A higher-stakes deployment context may require stricter values.
  Document the institutional justification when raising them.
```

### The Subsidiarity Test

A diocese in rural Appalachia running a parish-level faith formation program has different institutional capacity than the USCCB's technology office. Both can run the CDFI Framework. The diocese configures the deployment tier thresholds to match its pastoral judgment and risk profile, runs the engine against its own evaluation data, and deploys a model within its context — without requesting permission from anyone, without overriding any gate, and without violating the framework's integrity.

That is architecturally genuine local configuration. It is what *Antiqua et Nova* §42 requires when it says the responsibility for managing technology wisely pertains to every level of society guided by subsidiarity.

---

## Canonical and Magisterial Citations

- Dicastery for the Doctrine of the Faith, *Antiqua et Nova*, §42, January 28, 2025. https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html

- *Catechism of the Catholic Church*, 2nd ed., §1894, Vatican City: Libreria Editrice Vaticana, 1997. https://www.vatican.va/archive/ENG0015/_INDEX.HTM

- *Code of Canon Law*, Canon 627, Vatican City: Libreria Editrice Vaticana, 1983. https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib2-cann460-572_en.html

---

*Configuration files: [configs/authority_matrix.json](../../../configs/authority_matrix.json)*

*Configuration files: [configs/threshold_gates.yaml](../../../configs/threshold_gates.yaml)*

*Adaptation guide: [docs/governance/adapting-for-other-traditions.md](../adapting-for-other-traditions.md)*

*Contributing: [CONTRIBUTING.md](../../../CONTRIBUTING.md)*
