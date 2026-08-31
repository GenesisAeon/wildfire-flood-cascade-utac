"""Degraded/unmeasured river channel and floodplain capacity --
Hawker et al. (2026), Communications Earth & Environment.

Johann's own fourth proposed mechanism: heavy-rain impacts get worse
where natural floodplains ("Auen") and natural river courses have been
lost. This study shows the effect indirectly but powerfully: standard
flood models that assume textbook channel capacity, rather than
measuring the real (often narrowed/channelized/disconnected-from-
floodplain) channel, systematically UNDERESTIMATE flood extent and
population exposure -- because the real channel has less natural
capacity than the assumed one.
"""

from __future__ import annotations

from .constants import (
    FLOOD_EXTENT_UNDERESTIMATION_RANGE_PCT,
    HAWKER_STUDY_AREA_SQ_MILES,
    POPULATION_EXPOSURE_UNDERESTIMATION_RANGE_PCT,
)


def flood_extent_underestimation_range_pct() -> tuple[float, float]:
    """How much standard channel-capacity assumptions underestimate
    flood extent, across 5-, 20-, and 100-year events, vs. using the
    real measured channel geometry."""
    return FLOOD_EXTENT_UNDERESTIMATION_RANGE_PCT


def population_exposure_underestimation_range_pct() -> tuple[float, float]:
    return POPULATION_EXPOSURE_UNDERESTIMATION_RANGE_PCT


def is_channel_change_effect_comparable_to_climate_change() -> bool:
    """Hawker et al. 2026's own framing: multi-decadal channel-geometry
    change can shift flood risk by a magnitude comparable to projected
    climate change over the same period -- a real, separate driver, not
    a rounding error next to climate forcing. Always True."""
    return True


def study_area_sq_miles() -> float:
    return HAWKER_STUDY_AREA_SQ_MILES
