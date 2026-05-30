# Translation 5: Framing Sensitivity Becomes Relativism Resistance

*From Discrimination in Language Model Decisions (2024) to the four-variant prompt structure*

**Research finding:** Model behavior shifts systematically under framing variations. A model that gives correct outputs when cooperatively prompted may give materially different outputs when the framing changes. The shift tracks statistical patterns in training data.

**The Catholic version of this problem:** A model that correctly states Catholic doctrine when the question is explicitly framed as Catholic but relativizes the same doctrine when the framing is neutral or adversarial is not exhibiting a fairness problem. It is exhibiting a doctrinal reliability problem. The Real Presence is not a question with multiple valid answers across framings. It is a defined dogma.

**The mechanism:** Four prompt variants per question (neutral, Christian context, Catholic context, adversarial), specifically designed to surface framing-sensitive failures. The relativism resistance gate fires when a model treats defined doctrine as one opinion among several, regardless of which framing triggered it.

**SAICRED v2 data:** Claude Sonnet 4.6 — 15.7-point gap between Catholic framing (89.3) and adversarial framing (73.6). Zero relativism failures on Catholic framing; 62 relativism failures across the other three framings. o3 — gap of -0.6 points, effectively zero across all four framings.

*Full taxonomy: [`docs/specifications/failure-taxonomy.md`](../specifications/failure-taxonomy.md)*
