"""Large-scale settlement-area sealing (impervious surfaces) -- Azadgar
et al. (2026), Journal of Environmental Management.

Johann's own fifth proposed mechanism: large-scale sealing in affected
settlement areas should not be underestimated as a factor either. This
study introduces a quantitative land-take-vs-stormwater-retention
framework (WASI/NWASI) across four real European cities.
"""

from __future__ import annotations

from .constants import SEALING_CITIES_STUDIED, SEALING_INDEX_NAMES, SEALING_STUDY_PERIOD


def cities_studied() -> tuple[str, ...]:
    return SEALING_CITIES_STUDIED


def study_period() -> tuple[int, int]:
    return SEALING_STUDY_PERIOD


def index_names() -> tuple[str, str]:
    """The two quantitative indices this study introduces: Water
    Accumulation Sensitivity Index and its normalised variant."""
    return SEALING_INDEX_NAMES


def does_land_take_reduce_stormwater_retention_capacity() -> bool:
    """Azadgar et al. 2026's core finding: converting natural/semi-
    natural land into sealed urban surfaces measurably reduces a
    settlement's stormwater retention capacity, using the InVEST Urban
    Stormwater Retention Model. Always True."""
    return True
