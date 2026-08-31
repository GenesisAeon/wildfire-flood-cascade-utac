"""Post-fire flood-risk amplification via canopy/litter interception
loss -- Kang et al. (2025), Communications Earth & Environment.

Johann's own third proposed mechanism (forest-loss half): heavy-rain
events cause much worse regional impacts because of forest loss. This
is one of the best-established real findings in this package -- a
50-year SE Australia streamflow record across three real megafires
(2003, 2007, 2009), with El Nino/La Nina years excluded from the
comparison set specifically to isolate the fire effect.
"""

from __future__ import annotations

from .constants import (
    MEGAFIRE_YEARS_STUDIED,
    POST_MEGAFIRE_FLOOD_PROBABILITY,
    PRE_FIRE_FLOOD_PROBABILITY,
    STREAMFLOW_RECORD_YEARS,
)


def pre_fire_flood_probability() -> float:
    """Annual flood probability before a megafire -- roughly a 1-in-64-year event."""
    return PRE_FIRE_FLOOD_PROBABILITY


def post_megafire_flood_probability() -> float:
    """Annual flood probability after a megafire -- roughly a 1-in-8-year event."""
    return POST_MEGAFIRE_FLOOD_PROBABILITY


def flood_probability_increase_factor() -> float:
    return POST_MEGAFIRE_FLOOD_PROBABILITY / PRE_FIRE_FLOOD_PROBABILITY


def is_mechanism_soil_hydrophobicity() -> bool:
    """Kang et al. 2025's own explicit finding: canopy and leaf-litter
    interception loss is the primary factor, NOT fire-induced soil
    hydrophobicity (a commonly assumed but here explicitly ruled-out
    mechanism). Always False -- the honesty check inside this module."""
    return False


def megafire_years_studied() -> tuple[int, ...]:
    return MEGAFIRE_YEARS_STUDIED


def streamflow_record_length_years() -> int:
    return STREAMFLOW_RECORD_YEARS
