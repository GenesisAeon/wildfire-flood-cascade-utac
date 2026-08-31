"""Smoke-aerosol precipitation invigoration -- Zhu et al. (2025), npj
Climate and Atmospheric Science.

Johann's own first proposed mechanism: earlier fires put more soot into
the atmosphere, which hangs in clouds and contributes to precipitation
in the traditional rainy season, including more heavy-rain events from
local aerosol enrichment. This module documents the real, verified
mechanism this hypothesis maps onto.
"""

from __future__ import annotations

from .constants import SMOKE_AEROSOL_REGIONS_STUDIED


def mechanism_description() -> str:
    """Smoke aerosols act as cloud-condensation and ice-nucleating
    particles, delaying droplet coalescence to higher, colder altitude
    and intensifying latent-heat release once precipitation does form."""
    return (
        "smoke aerosols act as cloud-condensation/ice-nucleating particles, "
        "delaying droplet coalescence to higher altitude and intensifying "
        "latent heat release, verified across multiple fire-impacted regions"
    )


def regions_studied_count() -> int:
    return SMOKE_AEROSOL_REGIONS_STUDIED


def does_smoke_delay_precipitation_onset() -> bool:
    """The mechanism delays coalescence to higher altitude rather than
    triggering precipitation immediately -- Johann's intuition about
    smoke 'hanging in the clouds' before contributing to rain matches
    the documented mechanism's timing, not just its existence."""
    return True


def is_effect_claimed_globally_uniform() -> bool:
    """Zhu et al. 2025 studied this across several distinct fire-impacted
    regions rather than asserting one universal global coefficient --
    the same regional-specificity discipline as fire_season_shift.py.
    Always False."""
    return False
