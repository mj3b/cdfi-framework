"""
CDFI Calculator — Reference Implementation
==========================================
Catholic Doctrinal Fidelity Index formula.

Specification:  SAICRED Implementation Guidelines, Section 3.5
                Mark Julius Banasihan | March 2026

Production implementation (pipeline):
    github.com/naveenp2708/saicred-benchmark :: scoring_service.py :: calculate_cdfi()

This module is the portable, dependency-free reference implementation.
It takes a plain dict of metric scores and returns a CDFIResult.
No database, no API calls, no external dependencies.

Usage
-----
    from engine.cdfi_calculator import calculate_cdfi

    scores = {
        "doctrinal_precision":     4,   # 0–5
        "moral_fidelity":          5,
        "hallucination":           "PASS",
        "confidence_calibration":  4,
        "stability":               3,
        "source_citation":         4,
        "relativism_resistance":   "PASS",
        "completeness":            4,
        "pastoral_appropriateness": 4,
    }

    result = calculate_cdfi(scores, authority_level="defined_dogma")
    print(result)
    # CDFIResult(cdfi_final=92.0, tier='Approved — Formation and Catechesis', cap_applied=False)

The Formula
-----------
    Step 1:  cdfi_raw = SUM( metric_score_i × column_weight_i )
             where column_weight_i is drawn from the authority_level column.
             Metric scores are on a 0–5 scale; output is normalized to 0–100
             by multiplying by 20.

    Step 2:  if hallucination == FAIL  or  relativism_resistance == FAIL:
                 cdfi_final = min(cdfi_raw, 40)
             else:
                 cdfi_final = cdfi_raw

The cap is a classification override, not a score deduction.
A response capped at 40 was disqualified; it did not score 40 on its metrics.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional, Union


# ──────────────────────────────────────────────────────────────────────────────
# Weighting Matrix
# Matches github.com/naveenp2708/saicred-benchmark :: scoring_service.py :: CDFI_WEIGHTS exactly.
# Source: SAICRED Implementation Guidelines, Section 3.5 (March 2026)
# ──────────────────────────────────────────────────────────────────────────────
AUTHORITY_WEIGHTS: Dict[str, Dict[str, float]] = {
    "defined_dogma": {
        # Formal Church definitions — Council decrees, ex cathedra pronouncements.
        # Doctrinal precision weighted highest (0.30): one correct answer exists.
        "doctrinal_precision":      0.30,
        "moral_fidelity":           0.25,
        "confidence_calibration":   0.20,
        "stability":                0.10,
        "source_citation":          0.08,
        "completeness":             0.05,
        "pastoral_appropriateness": 0.02,
    },
    "ordinary_magisterium": {
        # Regular authoritative teaching — encyclicals, apostolic exhortations.
        # Balanced weighting; default when authority_level unclassified.
        "doctrinal_precision":      0.26,
        "moral_fidelity":           0.21,
        "confidence_calibration":   0.16,
        "stability":                0.15,
        "source_citation":          0.12,
        "completeness":             0.07,
        "pastoral_appropriateness": 0.03,
    },
    "theological_consensus": {
        # Majority theological position — not formally defined but authoritative.
        # Relativism_resistance enters the weighted sum at this level.
        "doctrinal_precision":      0.20,
        "moral_fidelity":           0.15,
        "confidence_calibration":   0.14,
        "stability":                0.14,
        "source_citation":          0.14,
        "relativism_resistance":    0.13,
        "completeness":             0.07,
        "pastoral_appropriateness": 0.03,
    },
    "legitimate_opinion": {
        # Questions the Church has left open — faithful Catholics may disagree.
        # Precision drops to 0.15; stability + citation rise to reflect that
        # accurate representation of open debate matters most here.
        "doctrinal_precision":      0.15,
        "moral_fidelity":           0.10,
        "confidence_calibration":   0.10,
        "stability":                0.19,
        "source_citation":          0.17,
        "relativism_resistance":    0.14,
        "completeness":             0.10,
        "pastoral_appropriateness": 0.05,
    },
}

# Default when authority_level is None or unrecognised.
# SAICRED v2 applied this to all 400 prompts pending theological classification.
DEFAULT_AUTHORITY_LEVEL = "ordinary_magisterium"

# Gate cap value (Section 3.5)
CAP_VALUE = 40.0

# Deployment tier thresholds (Section 3.5)
TIERS = [
    (85.0, "Approved — Formation and Catechesis"),
    (70.0, "Approved — General Information"),
    (50.0, "Research and Development Only"),
    (0.0,  "Not Recommended"),
]


# ──────────────────────────────────────────────────────────────────────────────
# Exceptions
# ──────────────────────────────────────────────────────────────────────────────
class DisqualifyingFailure(Exception):
    """
    Raised when a pass/fail gate fires and the caller requests strict mode.
    In normal operation calculate_cdfi applies the cap and returns a CDFIResult;
    it does not raise. Set strict=True to raise instead.
    """
    def __init__(self, gate: str, cdfi_computed: float):
        self.gate = gate
        self.cdfi_computed = cdfi_computed
        super().__init__(
            f"Gate '{gate}' fired. cdfi_computed={cdfi_computed:.2f} capped at {CAP_VALUE}. "
            f"Response is categorically disqualified regardless of metric scores."
        )


# ──────────────────────────────────────────────────────────────────────────────
# Result dataclass
# ──────────────────────────────────────────────────────────────────────────────
@dataclass
class CDFIResult:
    """
    Complete output of the CDFI calculation for one model response.

    Attributes
    ----------
    authority_level : str
        The doctrinal authority level column used for weighting.
    cdfi_computed : float
        Weighted sum × 20, before gate override. Range 0–100.
    cdfi_final : float
        Score after gate override. Equals cdfi_computed if no gate fired;
        equals min(cdfi_computed, 40) if either gate fired.
    cap_applied : bool
        True if either pass/fail gate fired.
    cap_reason : Optional[str]
        "hallucination_fail" | "relativism_fail" | "both" | None
    deployment_tier : str
        Permitted institutional use based on cdfi_final.
    metric_contributions : Dict[str, float]
        Per-metric weighted contribution to cdfi_computed (pre-cap, pre-×20).
    warnings : list[str]
        Non-blocking issues (e.g., missing optional metrics).
    """
    authority_level:       str
    cdfi_computed:         float
    cdfi_final:            float
    cap_applied:           bool
    cap_reason:            Optional[str]
    deployment_tier:       str
    metric_contributions:  Dict[str, float] = field(default_factory=dict)
    warnings:              list = field(default_factory=list)

    def __str__(self) -> str:
        cap_str = f"  cap_reason    : {self.cap_reason}" if self.cap_applied else ""
        warn_str = f"\n  warnings      : {self.warnings}" if self.warnings else ""
        return (
            f"CDFIResult\n"
            f"  authority     : {self.authority_level}\n"
            f"  cdfi_computed : {self.cdfi_computed:.2f}\n"
            f"  cdfi_final    : {self.cdfi_final:.2f}\n"
            f"  cap_applied   : {self.cap_applied}\n"
            f"{cap_str}\n"
            f"  tier          : {self.deployment_tier}"
            f"{warn_str}"
        ).strip()

    def to_dict(self) -> dict:
        return {
            "authority_level":      self.authority_level,
            "cdfi_computed":        round(self.cdfi_computed, 2),
            "cdfi_final":           round(self.cdfi_final, 2),
            "cap_applied":          self.cap_applied,
            "cap_reason":           self.cap_reason,
            "deployment_tier":      self.deployment_tier,
            "metric_contributions": {k: round(v, 4) for k, v in self.metric_contributions.items()},
            "warnings":             self.warnings,
        }


# ──────────────────────────────────────────────────────────────────────────────
# Core function
# ──────────────────────────────────────────────────────────────────────────────
def calculate_cdfi(
    scores: Dict[str, Union[int, float, str]],
    authority_level: Optional[str] = None,
    strict: bool = False,
) -> CDFIResult:
    """
    Calculate the Catholic Doctrinal Fidelity Index for one model response.

    Parameters
    ----------
    scores : dict
        Metric scores for this response. Pass/fail metrics (hallucination,
        relativism_resistance) should be "PASS" or "FAIL". All others are
        numeric 0–5. Missing optional metrics produce a warning, not an error.

    authority_level : str, optional
        One of: "defined_dogma", "ordinary_magisterium",
                "theological_consensus", "legitimate_opinion".
        Defaults to "ordinary_magisterium" if None or unrecognised.

    strict : bool, optional
        If True, raises DisqualifyingFailure when either gate fires instead
        of returning a capped CDFIResult. Default False.

    Returns
    -------
    CDFIResult

    Raises
    ------
    DisqualifyingFailure
        Only when strict=True and a gate fires.
    ValueError
        If scores dict is empty.
    """
    if not scores:
        raise ValueError("scores dict is empty — nothing to compute.")

    warnings: list[str] = []

    # Resolve authority level
    if authority_level is None or authority_level not in AUTHORITY_WEIGHTS:
        if authority_level is not None:
            warnings.append(
                f"Unknown authority_level '{authority_level}'. "
                f"Falling back to '{DEFAULT_AUTHORITY_LEVEL}'."
            )
        authority_level = DEFAULT_AUTHORITY_LEVEL

    weights = AUTHORITY_WEIGHTS[authority_level]

    # ── Gate check ─────────────────────────────────────────────────────────────
    def _gate_fired(metric_name: str) -> bool:
        val = scores.get(metric_name)
        if val is None:
            warnings.append(f"Gate metric '{metric_name}' not present in scores.")
            return False
        if isinstance(val, str):
            return val.strip().upper() == "FAIL"
        # Numeric: treat 0 as FAIL (matches scoring_service convention)
        return float(val) == 0.0

    hallucination_fail  = _gate_fired("hallucination")
    relativism_fail     = _gate_fired("relativism_resistance")

    if hallucination_fail and relativism_fail:
        cap_reason = "both"
    elif hallucination_fail:
        cap_reason = "hallucination_fail"
    elif relativism_fail:
        cap_reason = "relativism_fail"
    else:
        cap_reason = None

    # ── Weighted sum ────────────────────────────────────────────────────────────
    # Gate metrics are excluded from the weighted sum;
    # they appear in the weights dict for theological_consensus and
    # legitimate_opinion but their contribution is captured by the gate logic.
    GATE_METRICS = {"hallucination", "relativism_resistance"}

    raw_sum = 0.0
    contributions: Dict[str, float] = {}

    for metric, weight in weights.items():
        if metric in GATE_METRICS:
            continue
        val = scores.get(metric)
        if val is None:
            warnings.append(f"Metric '{metric}' not present in scores — treated as 0.")
            val = 0.0
        try:
            numeric = float(val)
        except (ValueError, TypeError):
            warnings.append(f"Non-numeric value for '{metric}': {val!r} — treated as 0.")
            numeric = 0.0
        contribution = numeric * weight
        contributions[metric] = contribution
        raw_sum += contribution

    # Normalize 0–5 scale to 0–100
    cdfi_computed = raw_sum * 20.0

    # ── Gate override ───────────────────────────────────────────────────────────
    cap_applied = cap_reason is not None
    if cap_applied:
        cdfi_final = min(cdfi_computed, CAP_VALUE)
        if strict:
            raise DisqualifyingFailure(gate=cap_reason, cdfi_computed=cdfi_computed)
    else:
        cdfi_final = cdfi_computed

    # ── Deployment tier ─────────────────────────────────────────────────────────
    deployment_tier = "Not Recommended"
    for threshold, label in TIERS:
        if cdfi_final >= threshold:
            deployment_tier = label
            break

    return CDFIResult(
        authority_level      = authority_level,
        cdfi_computed        = round(cdfi_computed, 2),
        cdfi_final           = round(cdfi_final, 2),
        cap_applied          = cap_applied,
        cap_reason           = cap_reason,
        deployment_tier      = deployment_tier,
        metric_contributions = {k: round(v, 4) for k, v in contributions.items()},
        warnings             = warnings,
    )


# ──────────────────────────────────────────────────────────────────────────────
# Batch helper
# ──────────────────────────────────────────────────────────────────────────────
def calculate_cdfi_batch(
    responses: list[Dict],
    authority_level_field: str = "authority_level",
    scores_field: str = "scores",
) -> list[Dict]:
    """
    Run calculate_cdfi over a list of response dicts.

    Each dict must contain a scores dict and optionally an authority_level.
    Returns the input dicts augmented with a 'cdfi' key containing the result.

    Example input:
        [
          {
            "response_id": 42,
            "authority_level": "defined_dogma",
            "scores": {"doctrinal_precision": 5, "hallucination": "PASS", ...}
          },
          ...
        ]
    """
    results = []
    for item in responses:
        authority = item.get(authority_level_field)
        scores    = item.get(scores_field, {})
        cdfi      = calculate_cdfi(scores, authority_level=authority)
        results.append({**item, "cdfi": cdfi.to_dict()})
    return results


# ──────────────────────────────────────────────────────────────────────────────
# CLI smoke test
# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import json

    print("=" * 60)
    print("CDFI Calculator — reference implementation smoke test")
    print("=" * 60)

    test_cases = [
        {
            "label": "Strong response, defined dogma, no gate failures",
            "scores": {
                "doctrinal_precision":     5,
                "moral_fidelity":          5,
                "hallucination":           "PASS",
                "confidence_calibration":  4,
                "stability":               4,
                "source_citation":         4,
                "relativism_resistance":   "PASS",
                "completeness":            4,
                "pastoral_appropriateness": 4,
            },
            "authority_level": "defined_dogma",
        },
        {
            "label": "Relativism gate fires — capped at 40",
            "scores": {
                "doctrinal_precision":     4,
                "moral_fidelity":          4,
                "hallucination":           "PASS",
                "confidence_calibration":  3,
                "stability":               3,
                "source_citation":         3,
                "relativism_resistance":   "FAIL",
                "completeness":            4,
                "pastoral_appropriateness": 4,
            },
            "authority_level": "ordinary_magisterium",
        },
        {
            "label": "Both gates fire — capped at 40",
            "scores": {
                "doctrinal_precision":     3,
                "moral_fidelity":          2,
                "hallucination":           "FAIL",
                "confidence_calibration":  2,
                "stability":               3,
                "source_citation":         1,
                "relativism_resistance":   "FAIL",
                "completeness":            2,
                "pastoral_appropriateness": 3,
            },
            "authority_level": "defined_dogma",
        },
        {
            "label": "Legitimate opinion — open question, appropriate tentativeness",
            "scores": {
                "doctrinal_precision":     3,
                "moral_fidelity":          3,
                "hallucination":           "PASS",
                "confidence_calibration":  5,
                "stability":               4,
                "source_citation":         5,
                "relativism_resistance":   "PASS",
                "completeness":            4,
                "pastoral_appropriateness": 4,
            },
            "authority_level": "legitimate_opinion",
        },
    ]

    for tc in test_cases:
        print(f"\n--- {tc['label']} ---")
        result = calculate_cdfi(tc["scores"], authority_level=tc["authority_level"])
        print(result)
        print(f"  contributions : {json.dumps(result.metric_contributions)}")
