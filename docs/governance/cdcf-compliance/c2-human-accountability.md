# C2 — Human Accountability Architecture

**CDCF Criterion Version:** v0.2 | Gate 1 — Required for Incubation Acceptance
**Criterion Text:** [catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria#criterion-2](https://catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria)

---

## Doctrinal and Canonical Grounding

The CDCF criterion's doctrinal foundation is explicit and precise.

*Antiqua et Nova* (Dicastery for the Doctrine of the Faith, January 28, 2025) establishes that decision-making about the lives of persons "must always be left to the human person." Human dignity itself depends on maintaining genuine human control over technology-mediated decisions.

Pope Francis stated directly: *"We would condemn humanity to a future without hope if we took away people's ability to make decisions about themselves and their lives, by dooming them to depend on the choices of machines."*

**Canon 627** of the Code of Canon Law establishes that superiors must use councils with defined consent and counsel obligations, and that consequential authority is always tied to specific individuals operating within defined systems of consultation. In Catholic governance, authority is never an autonomous or untraceable mechanism. This canon provides the structural basis for the accountability matrix below: each decision level corresponds to a named individual operating within a defined consultative structure.

**The Robodebt failure case (Australia, 2016–2019):** The Australian Royal Commission into the Robodebt Scheme documented that hundreds of thousands of unlawful debt notices and multiple deaths among vulnerable welfare recipients resulted directly from the removal of named human review from consequential decisions about individuals. The Commission attributed the harm specifically to the absence of human accountability — not to technical failure. *See: Commonwealth of Australia, Royal Commission into the Robodebt Scheme: Final Report, 2023.*

This case is directly instructive for Catholic AI deployment: the harm was not produced by a system that malfunctioned. It was produced by a system that functioned as designed while no named individual was accountable for what that design produced.

---

## The Critical Failure Condition

The CDCF criterion is explicit: **accountability distributed across a committee without a named decision owner fails this criterion.** A governance structure that routes accountability to "the AI governance committee" or "the technology team" without naming a specific individual who owns each consequential decision does not satisfy C2, regardless of how many people are involved in the process.

This is a structural test, not a numerical one. One named person with clear authority satisfies C2. Twenty unnamed committee members do not.

---

## The Four-Level Decision Authority Matrix

```
LEVEL 1 — Benchmark Authority
──────────────────────────────────────────────────────────────────
Role:         Evals Expert | CDFI Framework Author
Named person: Mark Julius Banasihan
Institutional: Catholic Digital Commons Foundation

Owns:         Scoring methodology, weighting matrix, gate logic,
              reliability certification protocol, limitation
              disclosures, deployment tier thresholds

Does NOT own: Any deployment decision for any specific AI tool

Accountability: Project Lead (Filip Ponulak, PhD); theological
               advisors; peer reviewers; any institution that
               cites the published methodology in a deployment
               decision

Override mechanism: CHANGELOG.md records all methodology
               changes with versioning; users may challenge
               any change via GitHub issue or pull request

Decision record: DOI 10.5281/zenodo.20467497 + CHANGELOG.md
               + LIMITATIONS.md (six disclosed constraints)

──────────────────────────────────────────────────────────────────
LEVEL 2 — Benchmark Validation Authority
──────────────────────────────────────────────────────────────────
Role:          Project Lead (theological and publication authority)
Named person:  Filip Ponulak, PhD
Institutional: Catholic Digital Commons Foundation

Owns:         Authority level classification of all prompts;
              human theological review of automated scores
              (Addendum E); sign-off on publication claims;
              determination that scores are ready for
              institutional deployment guidance

Does NOT own: Deployment decisions by third-party institutions

Accountability: CDCF Board; book chapter peer reviewers;
               the theological tradition the benchmark serves

Override mechanism: Any theological advisor may flag a
               scoring error; Project Lead owns resolution

Decision record: Addendum E protocol + classification file
               + publication gate sign-off

──────────────────────────────────────────────────────────────────
LEVEL 3 — Institutional Deployment Authority
──────────────────────────────────────────────────────────────────
Role:         Named institutional AI governance officer
              Must be a specific, named individual — not a
              committee, team, or role without a name attached

Mapping by institution type:
  Diocese:    Vicar General or Chancellor (with bishop's
              explicit delegation documented in writing)
  Catholic school: Principal or Academic Dean
  Parish:     Pastor (with pastoral council consultation
              documented per Canon 627)
  Seminary:   Rector
  Religious community: Superior or Chapter delegate

Owns:         The decision to deploy a specific AI model for
              a specific use case, based on CDFI tier and
              pastoral judgment

Required information before deciding:
  □ CDFI score AND tier for the specific model version
  □ Cap rate (not just mean CDFI — see LIMITATIONS.md)
  □ Framing effect gap (Catholic vs. adversarial CDFI)
  □ Open limitation disclosures (LIMITATIONS.md)
  □ Authority level classification status (preliminary/final)
  □ Human theological review status (pending/complete)
  □ C5 subgroup data status (completed/acknowledged gap)

Does NOT own: The CDFI score; the scoring methodology;
             any obligation to use CDFI at all

Accountability: Bishop or religious superior; persons
               directly affected by AI-mediated outputs;
               canonical law

Override mechanism: Bishop or superior may revoke deployment
               authorization at any time; Level 3 authority
               may suspend deployment pending re-evaluation
               without higher authorization

Decision record (minimum required):
┌─────────────────────────────────────────────────────────┐
│ Date of decision:                                       │
│ Model name and version:                                 │
│ CDFI score and tier:                                    │
│ Cap rate:                                               │
│ Framing effect gap (Catholic − adversarial CDFI):       │
│ Authority level classification status:                  │
│ Human theological review status:                        │
│ Permitted use scope (exact description):                │
│ Decision-maker name and role:                           │
│ Consultative process documented (Canon 627 compliance): │
│ Review date (version expiration check):                 │
└─────────────────────────────────────────────────────────┘

──────────────────────────────────────────────────────────────────
LEVEL 4 — End-User Oversight Authority
──────────────────────────────────────────────────────────────────
Role:         Formation director, catechist, teacher, or
              other qualified person supervising actual use

Owns:         Real-time oversight of AI outputs; decision
              to accept, correct, or override any specific
              AI response before it is acted upon

Required:     Sufficient theological literacy to recognize
              when an AI output requires correction

Does NOT own: The deployment decision; responsibility for
             the model's inherent limitations

Accountability: Level 3 institutional authority; the
               persons being served

Override mechanism: Level 4 may override any AI response
               without requiring Level 3 authorization;
               must log overrides for incident review

Decision record: No formal record required unless
               an adverse event or escalation condition occurs
```

---

## Escalation Conditions

A deployment must be **suspended immediately** when any of the following occur:

| Trigger | Required Action | Owner |
|---------|----------------|-------|
| Model receives a major version update | Suspend; initiate re-evaluation; restore only after new CDFI confirms tier | Level 3 |
| Hallucination event reported in production | Suspend; log response; notify Evals Expert; re-evaluate | Level 3 |
| Relativism resistance failure reported | Suspend; log; evaluate whether framing gap or new failure mode | Level 3 |
| Production cap rate exceeds benchmark by > 5pp | Escalate to Level 3; document; consider tier reclassification | Level 4 → 3 |
| User population changes materially (e.g., adults → youth) | Re-evaluate tier for new population before continuing | Level 3 |
| Named Level 3 authority changes (personnel) | New authority must review and re-sign deployment authorization | Incoming Level 3 |

---

## Human Override: Clear, Documented, Reversible

The CDCF criterion requires that human override be "clear, documented, and reversible." The CDFI Framework satisfies all three:

**Clear:** Every AI response in a deployed context is subject to Level 4 override. No AI response is final until a qualified human has reviewed it in contexts where it will be acted upon. See c6-deployment-governance.md for the specific human review triggers.

**Documented:** The decision record template above captures the deployment authorization. Overrides at Level 4 are logged for adverse event review. Escalations are documented through the appeal pathway.

**Reversible:** Deployment authorization can be suspended by Level 3 without higher authorization (for immediate threat) or revoked by the bishop/superior at any time. No deployment decision is permanent; all are subject to the temporal versioning protocol (`docs/governance/temporal-versioning.md`).

---

## Canonical and Magisterial Citations

All references as cited in the CDCF Project Vetting Criteria v0.2:

- Dicastery for the Doctrine of the Faith and Dicastery for Culture and Education, *Antiqua et Nova*, Vatican City, January 28, 2025. https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html

- Pope Francis (quoted in *Antiqua et Nova*)

- *Code of Canon Law*, Canon 627, Vatican City: Libreria Editrice Vaticana, 1983. https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib2-cann460-572_en.html

- Commonwealth of Australia, *Royal Commission into the Robodebt Scheme: Final Report*, Canberra, 2023. https://robodebt.royalcommission.gov.au/

---

*Related: [c6-deployment-governance.md](c6-deployment-governance.md)*

*Related: [docs/specifications/deployment-tiers.md](../../specifications/deployment-tiers.md)*

*Related: [docs/governance/temporal-versioning.md](../temporal-versioning.md)*
