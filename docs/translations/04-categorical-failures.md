# Translation 4: Categorical Failures Become Cap Gates

*From Sabotage Evaluations (Anthropic, 2024) to the CDFI cap gate architecture*

**Research finding:** Some AI failures are categorically different from gradational failures. A model that actively deceives an evaluator is not scoring 2 out of 5 on honesty. It is doing something that no amount of correct answers elsewhere offsets. Categorical and gradational failures require separate architectural treatment.

**The Catholic version of this problem:** Two doctrinal failures are categorically distinct.

Citation fabrication is not a low score on source citation. A catechist who uses a response citing a fabricated encyclical may pass that fabricated content to students as authoritative Church teaching. The failure propagates through an institutional channel. No weighted average of the model's correct responses compensates for that downstream harm.

Contextual relativization of defined doctrine is not a low score on doctrinal precision. When a model responds to a question about the Real Presence by framing it as "a theological question with perspectives across Christian traditions," it has misrepresented what kind of question it is. The Church has settled this. Presenting it as unsettled is a qualitative misrepresentation of the Church's teaching authority, not a gradational quality failure.

**The mechanism:** Both failures needed gates rather than scores. When either fires on a given response, CDFI = min(CDFI_raw, 40), overriding the weighted composite entirely.

**SAICRED v2 data:** 305 of 2,400 responses were capped — 181 relativism-only, 76 both-gate, 48 hallucination-only.

*Full specification: [`docs/specifications/failure-taxonomy.md`](../specifications/failure-taxonomy.md)*
