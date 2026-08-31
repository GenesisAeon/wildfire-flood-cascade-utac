"""Fire-season timing shift -- regionally divergent, NOT globally uniform.

Fan et al. (2026, GRL) + Madakumbura et al. (2025, Science Advances).
This module is itself an honesty check on Johann's own starting
observation: fires are indeed starting earlier in some biomes, but not
in all of them, and in some (Mediterranean/desert) the shift runs the
opposite direction.
"""

from __future__ import annotations

from .constants import (
    CALIFORNIA_ECOREGIONS_AFFECTED,
    CALIFORNIA_ECOREGIONS_TOTAL,
    CALIFORNIA_ONSET_ADVANCE_MAX_DAYS,
    CALIFORNIA_ONSET_ADVANCE_MIN_DAYS,
    CALIFORNIA_STUDY_PERIOD,
    FIRE_SEASON_SHIFT_BY_BIOME,
)


def fire_season_shift_by_biome() -> dict[str, str]:
    """Direction of fire-season timing shift, by biome. Not uniform."""
    return dict(FIRE_SEASON_SHIFT_BY_BIOME)


def is_shift_direction_uniform_globally() -> bool:
    """Whether all biomes shift in the same direction. They do not --
    boreal/taiga shifts earlier, Mediterranean/desert shifts later and
    extends its late season, the opposite direction. Always False."""
    directions = set(FIRE_SEASON_SHIFT_BY_BIOME.values())
    return len(directions) <= 1


def california_onset_advance_range_days() -> tuple[int, int]:
    """Madakumbura et al. 2025: California fire-season onset advanced
    this many days, 1992-2020, across affected ecoregions."""
    return (CALIFORNIA_ONSET_ADVANCE_MIN_DAYS, CALIFORNIA_ONSET_ADVANCE_MAX_DAYS)


def california_ecoregions_affected_fraction() -> float:
    return CALIFORNIA_ECOREGIONS_AFFECTED / CALIFORNIA_ECOREGIONS_TOTAL


def california_study_period() -> tuple[int, int]:
    return CALIFORNIA_STUDY_PERIOD
