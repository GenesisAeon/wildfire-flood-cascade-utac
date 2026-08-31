"""Verified constants for the wildfire-season-shift / precipitation-
intensification / flood-risk-amplification cascade.

GenesisAeon Package 121. Grew out of Johann's own subjective observation
("fires seem to start earlier now, and then the traditional rainy season
brings more precipitation") followed by four of his own proposed
mechanism hypotheses, checked one at a time against real literature
across 2026-08-31: smoke-aerosol precipitation invigoration, warmer
Atlantic/Mediterranean SST driving more available moisture, forest/
canopy loss amplifying flood severity, degraded river channels/
floodplains losing natural flood capacity, and large-scale settlement-
area sealing (impervious surfaces) doing the same. Each was independently
verified via WebSearch + WebFetch against publisher or press-release
pages (not a search-snippet summary alone), 2026-08-31.

Deliberately NO UTAC/CREP/AFET bridge -- see DISCLAIMER.md and
PACKAGE_REGISTRY.md's "Why no UTAC/CREP/AFET bridge in the
climate/ecology series" note for why.

Deliberately NOT a claim that Johann's full combined causal chain has
been studied as a single system anywhere in the literature -- see
synthesis_hypothesis.py, this package's honesty-check module.
"""

PACKAGE_ID = 121

# =====================================================================
# Fan et al. (2026), Geophysical Research Letters -- fire-season timing
# shift, regionally divergent (NOT globally uniform)
# =====================================================================

FAN_2026_CITATION = {
    "authors": "Fan, S., Tao, W., Zhang, Y., Shindell, D., Zhang, Y.",
    "year": 2026,
    "title": "Regionally divergent shifts in global fire season timing under recent warming",
    "journal": "Geophysical Research Letters",
    "doi": "10.1029/2025GL121153",
    "verified": "2026-08-31, via a corrective follow-up DeepResearch pass "
    "after an initial pass returned a slightly wrong DOI",
}

# Key finding: fire-season timing shift is NOT globally uniform.
# Boreal/taiga: earlier onset (earlier snowmelt). Mediterranean/desert:
# delayed AND extended late season -- the OPPOSITE direction. Prairie/
# humid biomes: muted signal. This directly complicates a single global
# "fires start earlier now" reading.
FIRE_SEASON_SHIFT_BY_BIOME = {
    "boreal_taiga": "earlier onset (earlier snowmelt)",
    "mediterranean_desert": "delayed onset, extended late season",
    "prairie_humid": "muted / weak signal",
}

# =====================================================================
# Madakumbura et al. (2025), Science Advances -- California fire-season
# onset advance, a concrete regional confirmation within the divergent
# global picture above
# =====================================================================

MADAKUMBURA_2025_CITATION = {
    "authors": "Madakumbura, G.D., et al.",
    "year": 2025,
    "title": "Advancing fire season onset across California ecoregions",
    "journal": "Science Advances",
    "doi": "10.1126/sciadv.adt2041",
    "verified": "2026-08-31, cross-referenced across 2+ independent sources",
}

CALIFORNIA_ONSET_ADVANCE_MIN_DAYS = 6
CALIFORNIA_ONSET_ADVANCE_MAX_DAYS = 46
CALIFORNIA_ECOREGIONS_AFFECTED = 11
CALIFORNIA_ECOREGIONS_TOTAL = 13
CALIFORNIA_STUDY_PERIOD = (1992, 2020)

# =====================================================================
# Zhu et al. (2025), npj Climate and Atmospheric Science -- smoke-aerosol
# precipitation invigoration (Johann's 1st proposed mechanism)
# =====================================================================

ZHU_2025_CITATION = {
    "authors": "Zhu, H., Zhao, H., Yang, S., et al.",
    "year": 2025,
    "title": "Wildfire smoke aerosols invigorate precipitation across fire-impacted regions",
    "journal": "npj Climate and Atmospheric Science",
    "volume": 8,
    "article_number": 170,
    "doi": "10.1038/s41612-025-01047-3",
    "verified": "2026-08-31, cross-referenced via nature.com listing and a "
    "DOAJ index entry (direct nature.com fetch redirected to an auth gate)",
}

SMOKE_AEROSOL_REGIONS_STUDIED = 5

# =====================================================================
# Calvo-Sancho et al. (2026), Nature Communications -- warmer SST driving
# more available atmospheric moisture and heavier rain (Johann's 2nd
# proposed mechanism), Valencia October 2024 flash-flood attribution
# =====================================================================

CALVO_SANCHO_2026_CITATION = {
    "authors": "Calvo-Sancho, C., Diaz-Fernandez, J., Gonzalez-Aleman, J.J., et al.",
    "year": 2026,
    "title": "Anthropogenic warming intensified the October 2024 Valencia flash-flood rainfall",
    "journal": "Nature Communications",
    "doi": "10.1038/s41467-026-68929-9",
    "verified": "2026-08-31, via PMC mirror PMC12913788 (direct nature.com "
    "fetch redirected to an auth gate)",
}

# Attribution numbers vs. a pre-industrial counterfactual, exceeding
# simple Clausius-Clapeyron (~7%/degC) scaling:
HOURLY_RAINFALL_INTENSITY_INCREASE_PCT_PER_DEGC = 20.0
SIX_HOUR_RAINFALL_RATE_INCREASE_PCT = 21.0
AREA_ABOVE_180MM_RAINFALL_INCREASE_PCT = 55.0
CATCHMENT_RAINFALL_VOLUME_INCREASE_PCT = 19.0
CLAUSIUS_CLAPEYRON_BASELINE_PCT_PER_DEGC = 7.0

MECHANISM_BREAKDOWN_PCT = {
    "convective_updrafts": 11.9,
    "latent_heat_release": 29.5,
    "graupel": 32.4,
    "precipitation_efficiency": 12.6,
}

# =====================================================================
# Kang et al. (2025), Communications Earth & Environment -- post-fire
# flood-risk amplification via canopy/litter interception loss (Johann's
# 3rd proposed mechanism, forest-loss half)
# =====================================================================

KANG_2025_CITATION = {
    "authors": "Kang, T-H., et al.",
    "year": 2025,
    "title": (
        "Interception reduction from deforestation and forest fire "
        "increases large-scale fluvial flooding risk"
    ),
    "journal": "Communications Earth & Environment",
    "doi": "10.1038/s43247-025-02748-6",
    "verified": "2026-08-31, via phys.org press coverage (direct nature.com "
    "fetch redirected to an auth gate)",
}

# 50-year SE Australia streamflow record, 3 real megafires, El Nino/
# La Nina years excluded from the comparison set to isolate the fire
# effect specifically.
PRE_FIRE_FLOOD_PROBABILITY = 0.016  # ~1-in-64-year event
POST_MEGAFIRE_FLOOD_PROBABILITY = 0.127  # ~1-in-8-year event
MEGAFIRE_YEARS_STUDIED = (2003, 2007, 2009)
STREAMFLOW_RECORD_YEARS = 50

# =====================================================================
# Hawker et al. (2026), Communications Earth & Environment -- degraded/
# unmeasured river channel and floodplain capacity causes systematic
# flood-hazard underestimation (Johann's 4th proposed mechanism, "Auen
# und natuerliche Flussläufe" half)
# =====================================================================

HAWKER_2026_CITATION = {
    "authors": "Hawker, L., Darby, S., Slater, L., et al.",
    "year": 2026,
    "title": "River channel change can affect flood hazard and impact substantially",
    "journal": "Communications Earth & Environment",
    "doi": "10.1038/s43247-026-03517-9",
    "verified": "2026-08-31, via earth.com press coverage (direct "
    "nature.com fetch redirected to an auth gate)",
}

FLOOD_EXTENT_UNDERESTIMATION_RANGE_PCT = (9.0, 152.0)
POPULATION_EXPOSURE_UNDERESTIMATION_RANGE_PCT = (15.0, 472.0)
HAWKER_STUDY_AREA_SQ_MILES = 52000

# =====================================================================
# Azadgar et al. (2026), Journal of Environmental Management -- large-
# scale settlement-area sealing (impervious surfaces) reduces stormwater
# retention capacity (Johann's 5th proposed mechanism)
# =====================================================================

AZADGAR_2026_CITATION = {
    "authors": "Azadgar, A., Benedini, A., Salata, S., Lacoere, P., Badach, J., Nyka, L.",
    "year": 2026,
    "title": (
        "Flood-sensitive land take (FSL) analysis: A new way to read "
        "how urban sealing shapes flood risk"
    ),
    "journal": "Journal of Environmental Management",
    "doi": "10.1016/j.jenvman.2026.129513",
    "verified": "2026-08-31, cross-referenced across PubMed listing and "
    "ScienceDirect record for title/authors/journal/DOI agreement "
    "(both direct fetches blocked)",
}

SEALING_CITIES_STUDIED = ("Gdansk", "Milan", "Ghent", "Oslo")
SEALING_STUDY_PERIOD = (2012, 2018)
SEALING_INDEX_NAMES = ("WASI", "NWASI")

# =====================================================================
# Cross-reference: glacier-buffer loss (Johann's 3rd-message mechanism,
# glacier half) is already documented elsewhere in this ecosystem
# =====================================================================

GLACIER_BUFFER_CROSS_REFERENCE_PACKAGE = "glacier-buffer-utac"
GLACIER_BUFFER_CROSS_REFERENCE_PACKAGE_ID = 99
GLACIER_BUFFER_CROSS_REFERENCE_CITATION = "Huss & Hock (2018)"
