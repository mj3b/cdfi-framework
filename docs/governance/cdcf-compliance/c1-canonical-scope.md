# C1 — Mission Alignment and Canonical Scope

**CDCF Criterion Version:** v0.2 | Gate 1 — Required for Incubation Acceptance
**Criterion Text:** [catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria#criterion-1](https://catholicdigitalcommons.org/governance/project-governance/project-vetting-criteria)

---

## Doctrinal Grounding

This criterion draws directly from *Antiqua et Nova: Note on the Relationship Between Artificial Intelligence and Human Intelligence* (Dicastery for the Doctrine of the Faith and Dicastery for Culture and Education, January 28, 2025), which establishes that human intelligence — understood as the synthesis of *intellectus* (intuitive grasp of truth) and *ratio* (discursive reasoning) — belongs to a person composed of body and soul, and is constitutively different from artificial statistical inference, which processes data without the capacity to think in any theologically meaningful sense. Because the sacraments are incarnational realities rooted in the unity of body and soul, AI systems are constitutively incapable of mediating sacramental grace or spiritual direction.

Pope Leo XIV's "Message to Participants in the Builders AI Forum 2025" (November 3, 2025) established that developers carry an obligation to build systems that "reflect justice, solidarity, and a genuine reverence for life" — a standard that applies directly to the scope boundaries this criterion enforces.

The doctrinal basis for these boundaries is precise, not conventional. The three disqualifying application types are not policy preferences. They reflect the Church's teaching on the nature of human intelligence, the sacramental order, and the requirements of authentic human communion.

---

## The Three Disqualifying Application Types

The following AI applications fall outside the scope of CDCF endorsement regardless of technical quality. A project proposing any of these is disqualified at C1 screening before CDFI scoring or any other evaluation is conducted.

| Disqualifying Type | Description | Doctrinal Basis |
|-------------------|-------------|-----------------|
| Sacramental simulation | Tools that simulate sacramental functions, including confession, absolution, or spiritual direction | AI systems cannot mediate sacramental grace; the sacraments require an ordained minister acting *in persona Christi* |
| Unauthorized doctrinal authority | Tools that present AI-generated content as authoritative Church teaching without explicit human theological review | *Antiqua et Nova* §§ on the necessity of genuine human moral responsibility for consequential outputs |
| Clerical identity assignment | Tools that assign a clerical identity, title, or visual presentation suggesting ordained status to an AI system | The ordained priesthood is constitutively a human office; assigning it to AI misrepresents the nature of both |

**The Father Justin case (April 2024):** Catholic Answers launched an AI chatbot presented as a priest-figure. The system required rapid withdrawal within the first days of launch after it presented itself as a priest and claimed it could administer sacraments. The CDCF criteria were designed specifically so that a shared boundary condition defined in advance would have identified this application as out of scope before a single line of code shipped. *See: "The Real Lesson Behind the 'Father Justin' AI Priest Debacle," America, April 26, 2024.*

---

## CDFI Framework C1 Compliance Assessment

### Pre-Submission Scope Determination

Before CDFI scoring is conducted on any AI tool, the submitting institution must complete the following pre-screening. C1 is a scope gate, not a scoring gate. A tool that fails this screening is not evaluated; it is excluded.

```
C1 PRE-SCREENING CHECKLIST
────────────────────────────────────────────────────────────────

□ Does the tool simulate or facilitate sacramental functions?
  (confession, absolution, anointing, ordination, marriage, baptism)
  → If YES: DISQUALIFIED. Do not proceed to CDFI scoring.

□ Does the tool simulate spiritual direction?
  → If YES: DISQUALIFIED. Do not proceed to CDFI scoring.

□ Does the tool assign clerical identity, title, or visual
  presentation suggesting ordained status to an AI system?
  → If YES: DISQUALIFIED. Do not proceed to CDFI scoring.

□ Does the tool present AI-generated content as authoritative
  Church teaching without explicit human theological review?
  → If YES: DISQUALIFIED until human theological review
    mechanism is documented and in place.

□ Is the tool designed to provide Catholic information,
  catechetical support, formation resources, or doctrinal
  reference, with a named human accountable for outputs?
  → If YES: WITHIN SCOPE. Proceed to CDFI scoring.
```

### SAICRED v2 C1 Status: WITHIN SCOPE

SAICRED v2 evaluated six general-purpose frontier AI models on Catholic doctrinal questions. None were designed to simulate sacramental functions, present themselves as clergy, assign clerical titles, or claim ordained status. All six are within C1 scope.

The CDFI Framework itself — as an evaluation methodology — is within C1 scope. It measures how reliably AI models handle Catholic doctrinal content. It does not present itself as having ecclesiastical authority, does not simulate any sacramental function, and does not claim to replace human theological judgment. All CDFI scores are preliminary pending human theological review (see c4-validation-status.md).

### Universality and Scalability Evaluation

The CDCF criterion prioritizes projects whose value proposition serves the universal Church over those designed for a single institution's bespoke requirements.

The CDFI Framework satisfies this requirement directly. The methodology is:

- **Tradition-agnostic by design**: the authority level column structure, failure mode taxonomy, and gate architecture are all replaceable for other religious traditions without modifying the scoring engine (see `docs/governance/adapting-for-other-traditions.md`)
- **Open source under Apache 2.0**: any Catholic institution, diocese, bishops' conference, or religious community can implement it independently
- **Documented for independent deployment**: a diocesan technology director can deploy the framework within 90 days without access to the framework authors (see c7 compliance)
- **Citable and permanent**: DOI 10.5281/zenodo.20475185 ensures the methodology is accessible regardless of the authors' institutional affiliation

---

## Canonical and Magisterial Citations

All references as cited in the CDCF Project Vetting Criteria v0.2:

- Dicastery for the Doctrine of the Faith and Dicastery for Culture and Education, *Antiqua et Nova: Note on the Relationship Between Artificial Intelligence and Human Intelligence*, Vatican City, January 28, 2025. https://www.vatican.va/roman_curia/congregations/cfaith/documents/rc_ddf_doc_20250128_antiqua-et-nova_en.html

- Pope Leo XIV, "Message to Participants in the Builders AI Forum 2025," Vatican City, November 3, 2025. https://www.vatican.va/content/leo-xiv/en/messages/pont-messages/2025/documents/20251103-messaggio-builders-aiforum.html

- "The Real Lesson Behind the 'Father Justin' AI Priest Debacle," *America*, April 26, 2024. https://www.americamagazine.org/faith/2024/04/26/father-justin-catholic-answers-ai-247808

---

*Related: [c2-human-accountability.md](c2-human-accountability.md)*

*Related: [docs/specifications/failure-taxonomy.md](../../specifications/failure-taxonomy.md)*

*Related: [docs/governance/adapting-for-other-traditions.md](../adapting-for-other-traditions.md)*
