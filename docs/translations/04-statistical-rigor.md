# Translation 4: Statistical Rigor Produces Deployment Tier Thresholds

*From A Statistical Approach to Model Evaluations (Anthropic, 2024) to confidence intervals and deployment tiers*

**Research finding:** Point estimates without uncertainty quantification are not defensible for institutional reliance. Treating related prompts as statistically independent inflates apparent precision by up to 3x. Clustered standard errors and pre-registered power analysis are required for credible benchmark publication.

**The Catholic version of this problem:** A bishop's conference making deployment decisions based on "Model A scored 82.5 and Model B scored 81.8" needs to know whether that 0.7-point difference is statistically meaningful. In SAICRED v2, pairwise Welch t-tests with clustered standard errors (topic_domain, G=7) showed that positions 2 through 5 are not statistically distinguishable. Publishing those rankings without this disclosure overstates the precision of the benchmark.

**The mechanism:** Three outputs from this translation. First, 95% confidence intervals on all published CDFI scores. Second, the temporal versioning protocol: CDFI scores expire when a model receives a major version update, formalizing that the score is a measurement at a point in time, not a permanent property of the model. Third, the deployment tier thresholds (85 for formation, 70 for general information): the principle that readiness is context-dependent (a model adequate for low-stakes retrieval may be inadequate for high-stakes formation) drove the threshold design.

**SAICRED v2 data:** The o3-to-Claude gap of 7.0 points does not reach significance at p=0.142. The Grok 4-to-Claude gap does at p=0.008.

*Full specification: [`docs/specifications/deployment-tiers.md`](../specifications/deployment-tiers.md)*
