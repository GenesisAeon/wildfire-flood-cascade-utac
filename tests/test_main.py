from __future__ import annotations

from wildfire_flood_cascade_utac import (
    AZADGAR_2026_CITATION,
    CALVO_SANCHO_2026_CITATION,
    CASCADE_LINKS,
    FAN_2026_CITATION,
    HAWKER_2026_CITATION,
    KANG_2025_CITATION,
    MADAKUMBURA_2025_CITATION,
    PACKAGE_ID,
    VALENCIA_ATTRIBUTION,
    ZHU_2025_CITATION,
    california_ecoregions_affected_fraction,
    california_onset_advance_range_days,
    california_study_period,
    cities_studied,
    combined_cascade_description,
    component_mechanisms_independently_verified,
    does_land_take_reduce_stormwater_retention_capacity,
    does_smoke_delay_precipitation_onset,
    event_name_and_date,
    exceeds_clausius_clapeyron_scaling,
    fire_season_shift_by_biome,
    flood_extent_underestimation_range_pct,
    flood_probability_increase_factor,
    glacier_buffer_cross_reference,
    hourly_rainfall_intensity_increase_pct_per_degc,
    index_names,
    is_channel_change_effect_comparable_to_climate_change,
    is_combined_cascade_a_directly_studied_single_system,
    is_effect_claimed_globally_uniform,
    is_mechanism_soil_hydrophobicity,
    is_shift_direction_uniform_globally,
    mechanism_breakdown_pct,
    mechanism_description,
    megafire_years_studied,
    number_of_cascade_links,
    population_exposure_underestimation_range_pct,
    post_megafire_flood_probability,
    pre_fire_flood_probability,
    regions_studied_count,
    streamflow_record_length_years,
    study_area_sq_miles,
    study_period,
)


def test_package_id() -> None:
    assert PACKAGE_ID == 121


def test_all_seven_citations_have_dois() -> None:
    assert FAN_2026_CITATION["doi"] == "10.1029/2025GL121153"
    assert MADAKUMBURA_2025_CITATION["doi"] == "10.1126/sciadv.adt2041"
    assert ZHU_2025_CITATION["doi"] == "10.1038/s41612-025-01047-3"
    assert CALVO_SANCHO_2026_CITATION["doi"] == "10.1038/s41467-026-68929-9"
    assert KANG_2025_CITATION["doi"] == "10.1038/s43247-025-02748-6"
    assert HAWKER_2026_CITATION["doi"] == "10.1038/s43247-026-03517-9"
    assert AZADGAR_2026_CITATION["doi"] == "10.1016/j.jenvman.2026.129513"


def test_fire_season_shift_is_regionally_divergent() -> None:
    shift = fire_season_shift_by_biome()
    assert shift["boreal_taiga"] != shift["mediterranean_desert"]
    assert is_shift_direction_uniform_globally() is False


def test_california_onset_advance() -> None:
    min_days, max_days = california_onset_advance_range_days()
    assert min_days == 6
    assert max_days == 46
    assert 0.0 < california_ecoregions_affected_fraction() < 1.0
    assert california_study_period() == (1992, 2020)


def test_smoke_aerosol_mechanism() -> None:
    assert regions_studied_count() == 5
    assert does_smoke_delay_precipitation_onset() is True
    assert is_effect_claimed_globally_uniform() is False
    assert "aerosol" in mechanism_description()


def test_sst_moisture_amplification() -> None:
    assert hourly_rainfall_intensity_increase_pct_per_degc() == 20.0
    assert exceeds_clausius_clapeyron_scaling() is True
    assert event_name_and_date() == "Valencia flash flood, October 2024"
    breakdown = mechanism_breakdown_pct()
    assert round(sum(breakdown.values()), 1) == 86.4
    assert breakdown["latent_heat_release"] == 29.5


def test_valencia_attribution_dataclass() -> None:
    assert VALENCIA_ATTRIBUTION.hourly_intensity_increase_pct_per_degc == 20.0
    assert VALENCIA_ATTRIBUTION.area_above_180mm_increase_pct == 55.0


def test_postfire_flood_risk() -> None:
    assert pre_fire_flood_probability() == 0.016
    assert post_megafire_flood_probability() == 0.127
    factor = flood_probability_increase_factor()
    assert 7.0 < factor < 8.5
    # The key honesty check: NOT soil hydrophobicity.
    assert is_mechanism_soil_hydrophobicity() is False
    assert megafire_years_studied() == (2003, 2007, 2009)
    assert streamflow_record_length_years() == 50


def test_channel_floodplain_degradation() -> None:
    extent_low, extent_high = flood_extent_underestimation_range_pct()
    assert extent_low == 9.0
    assert extent_high == 152.0
    exposure_low, exposure_high = population_exposure_underestimation_range_pct()
    assert exposure_low == 15.0
    assert exposure_high == 472.0
    assert is_channel_change_effect_comparable_to_climate_change() is True
    assert study_area_sq_miles() == 52000


def test_urban_sealing_amplification() -> None:
    assert len(cities_studied()) == 4
    assert study_period() == (2012, 2018)
    assert index_names() == ("WASI", "NWASI")
    assert does_land_take_reduce_stormwater_retention_capacity() is True


def test_synthesis_hypothesis_is_the_honesty_check() -> None:
    assert number_of_cascade_links() == len(CASCADE_LINKS) == 7
    assert "->" in combined_cascade_description()
    # The core honesty check: the full combined cascade is NOT itself a
    # directly-studied single finding, even though every link is real.
    assert is_combined_cascade_a_directly_studied_single_system() is False
    assert component_mechanisms_independently_verified() is True


def test_glacier_buffer_cross_reference_not_reinvented() -> None:
    ref = glacier_buffer_cross_reference()
    assert "glacier-buffer-utac" in ref
    assert "P99" in ref
    assert "Huss" in ref
