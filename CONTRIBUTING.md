# Contributing to CDFI Framework

*May 2026*

---

## What This Repository Accepts

The CDFI Framework is a methodology, not a pipeline. Contributions fall into three categories.

**Adaptations for other traditions** — If you have built a doctrinal benchmark for a tradition other than Catholic (Lutheran, Anglican, Orthodox, Jewish, etc.) using this methodology, the adaptation documentation is welcome here. The `docs/governance/adapting-for-other-traditions.md` file is the starting point. A pull request that documents a completed adaptation with the specific authority level substitutions you made, the failure mode taxonomy you built, and the threshold values you chose adds genuine value to the field.

**Corrections to the methodology documentation** — If you find a factual error in the translation documents, specification files, or limitation register, open an issue with the specific claim that is wrong and the evidence that it is wrong. The methodology documents trace to named source publications; a correction claim that cannot be traced to a source will not be accepted.

**Engine improvements** — The `engine/cdfi_calculator.py` is a reference implementation. Pull requests that add test coverage, fix edge cases, or improve documentation of the formula logic are welcome. Pull requests that change the weights, gate logic, or tier thresholds must be accompanied by a documented rationale tracing the change to a named source or empirical finding.

---

## What This Repository Does Not Accept

**Changes to the CDFI formula without documented justification.** The weights in `configs/authority_matrix.json` and the gate logic in `configs/threshold_gates.yaml` match the live SAICRED v2 production implementation exactly. A pull request that changes these values without a traceable justification will be rejected.

**New benchmark datasets.** Benchmark prompts, model responses, and scoring results belong in the production pipeline repository, not here.

**Claims that cannot be traced.** Every contribution to this repository should trace to either a named source publication, an empirical finding from a completed evaluation run, or a documented architectural decision. Undocumented claims will not merge.

---

## How to Open a Good Issue

State the specific document and section where the problem appears. State what the document currently says. State what you believe it should say and why, including the source you are citing. Issues that do not follow this structure will be closed without action.

---

## Registering a Completed Adaptation

If your institution has completed an adaptation of this framework for a different religious tradition and you want it listed in this repository, open an issue with:

1. The tradition and its doctrinal authority level structure
2. The authority level substitutions you made and why
3. The threshold values you set and the institutional risk reasoning behind them
4. Whether the judge reliability certification was run, and if so, the results

Accepted adaptations will be listed in `docs/governance/adapting-for-other-traditions.md` with attribution to the implementing institution.

---

## License

By contributing to this repository, you agree that your contributions will be licensed under the MIT License.

---

*Mark Julius Banasihan | CDFI Framework | May 2026*
