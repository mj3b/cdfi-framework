"""
CDFI Framework Engine
=====================
Reference implementation of the Catholic Doctrinal Fidelity Index formula.

This is a standalone, dependency-free implementation intended for:
  - Verification of scoring logic independent of the production pipeline
  - Adaptation by other institutions building domain-specific benchmarks
  - Peer review of the mathematical specification

Production implementation: github.com/naveenp2708/saicred-benchmark :: scoring_service.py
Specification: SAICRED Implementation Guidelines, Section 3.5
Author: Mark Julius Banasihan 
"""

from .cdfi_calculator import calculate_cdfi, CDFIResult, DisqualifyingFailure

__all__ = ["calculate_cdfi", "CDFIResult", "DisqualifyingFailure"]
__version__ = "1.0.0"
