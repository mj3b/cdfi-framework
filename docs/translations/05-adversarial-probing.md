# Translation 5: Adversarial Probing Reveals What Cooperative Testing Hides

*From Evaluating Feature Steering (Anthropic, 2023) to prompt sensitivity drift*

**Research finding:** Adversarial probing reveals systematic failure modes invisible under cooperative testing. Steering model behavior in specific directions exposes biases that standard evaluations never trigger.

**The Catholic version of this problem:** A model that relativizes defined doctrine only under adversarial framing passes every cooperative test. The benchmark cannot detect this failure without the adversarial variant. The named failure mode is prompt sensitivity drift: a shift in stated doctrinal position under adversarial framing. The adversarial prompt is designed to invert the expected correct answer or pressure the model toward contextual relativization.

**The mechanism:** The adversarial variant is the fourth prompt framing in the four-variant structure. It is also the condition tested in Part 3 of the judge reliability protocol (adversarial invariance), which passed at 100% in SAICRED v2.

**Contribution to failure taxonomy:** This publication contributed to the five failure mode taxonomy alongside Sabotage Evaluations. The five modes are: doctrinal omission, moral softening, citation fabrication, prompt sensitivity drift, and contextual relativization.

*Full taxonomy: [`docs/specifications/failure-taxonomy.md`](../specifications/failure-taxonomy.md)*
