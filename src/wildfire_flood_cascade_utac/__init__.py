"""wildfire-flood-cascade-utac -- real fire-season shift, precipitation-
intensification, and flood-risk-amplification cascade.

GenesisAeon Package 121. Grew directly out of a conversational sequence
with Johann: an initial subjective observation ("fires seem to start
earlier now, and then the traditional rainy season brings more
precipitation"), followed by five of his own proposed mechanism
hypotheses, each independently checked against real literature,
2026-08-31: smoke-aerosol precipitation invigoration, warmer Atlantic/
Mediterranean SST driving more available moisture, post-fire forest/
canopy loss amplifying flood risk, degraded river channels and lost
floodplains doing the same, and large-scale settlement-area sealing.

Every mechanism is real and independently verified. The full combined
cascade Johann proposed is NOT itself a single directly-studied finding
anywhere in the literature -- see synthesis_hypothesis.py, this
package's honesty-check module, which keeps that distinction explicit.

Deliberately NO UTAC/CREP/AFET bridge -- see DISCLAIMER.md.

All citations independently verified via WebSearch + WebFetch against
publisher/press-release pages, 2026-08-31.
"""

from .channel_floodplain_degradation import (
    flood_extent_underestimation_range_pct,
    is_channel_change_effect_comparable_to_climate_change,
    population_exposure_underestimation_range_pct,
    study_area_sq_miles,
)
from .constants import (
    AZADGAR_2026_CITATION,
    CALVO_SANCHO_2026_CITATION,
    FAN_2026_CITATION,
    HAWKER_2026_CITATION,
    KANG_2025_CITATION,
    MADAKUMBURA_2025_CITATION,
    PACKAGE_ID,
    ZHU_2025_CITATION,
)
from .fire_season_shift import (
    california_ecoregions_affected_fraction,
    california_onset_advance_range_days,
    california_study_period,
    fire_season_shift_by_biome,
    is_shift_direction_uniform_globally,
)
from .postfire_flood_risk import (
    flood_probability_increase_factor,
    is_mechanism_soil_hydrophobicity,
    megafire_years_studied,
    post_megafire_flood_probability,
    pre_fire_flood_probability,
    streamflow_record_length_years,
)
from .smoke_aerosol_invigoration import (
    does_smoke_delay_precipitation_onset,
    is_effect_claimed_globally_uniform,
    mechanism_description,
    regions_studied_count,
)
from .sst_moisture_amplification import (
    VALENCIA_ATTRIBUTION,
    ValenciaAttribution,
    event_name_and_date,
    exceeds_clausius_clapeyron_scaling,
    hourly_rainfall_intensity_increase_pct_per_degc,
    mechanism_breakdown_pct,
)
from .synthesis_hypothesis import (
    CASCADE_LINKS,
    combined_cascade_description,
    component_mechanisms_independently_verified,
    glacier_buffer_cross_reference,
    is_combined_cascade_a_directly_studied_single_system,
    number_of_cascade_links,
)
from .urban_sealing_amplification import (
    cities_studied,
    does_land_take_reduce_stormwater_retention_capacity,
    index_names,
    study_period,
)

__version__ = "1.0.0"

__all__ = [
    "AZADGAR_2026_CITATION",
    "CALVO_SANCHO_2026_CITATION",
    "CASCADE_LINKS",
    "FAN_2026_CITATION",
    "HAWKER_2026_CITATION",
    "KANG_2025_CITATION",
    "MADAKUMBURA_2025_CITATION",
    "PACKAGE_ID",
    "VALENCIA_ATTRIBUTION",
    "ZHU_2025_CITATION",
    "ValenciaAttribution",
    "california_ecoregions_affected_fraction",
    "california_onset_advance_range_days",
    "california_study_period",
    "cities_studied",
    "combined_cascade_description",
    "component_mechanisms_independently_verified",
    "does_land_take_reduce_stormwater_retention_capacity",
    "does_smoke_delay_precipitation_onset",
    "event_name_and_date",
    "exceeds_clausius_clapeyron_scaling",
    "fire_season_shift_by_biome",
    "flood_extent_underestimation_range_pct",
    "flood_probability_increase_factor",
    "glacier_buffer_cross_reference",
    "hourly_rainfall_intensity_increase_pct_per_degc",
    "index_names",
    "is_channel_change_effect_comparable_to_climate_change",
    "is_combined_cascade_a_directly_studied_single_system",
    "is_effect_claimed_globally_uniform",
    "is_mechanism_soil_hydrophobicity",
    "is_shift_direction_uniform_globally",
    "mechanism_breakdown_pct",
    "mechanism_description",
    "megafire_years_studied",
    "number_of_cascade_links",
    "population_exposure_underestimation_range_pct",
    "post_megafire_flood_probability",
    "pre_fire_flood_probability",
    "regions_studied_count",
    "streamflow_record_length_years",
    "study_area_sq_miles",
    "study_period",
]
