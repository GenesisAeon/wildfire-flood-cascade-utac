"""Warmer SST -> more available atmospheric moisture -> heavier rain --
Calvo-Sancho et al. (2026), Nature Communications, Valencia October 2024
flash-flood attribution study.

Johann's own second proposed mechanism: earlier heat phases over the
local Atlantic and Mediterranean already mean more potential water
available for heavy-rain events, independent of the smoke mechanism.
This attribution study quantifies exactly that link for a real, recent,
extreme event.
"""

from __future__ import annotations

from dataclasses import dataclass

from .constants import (
    AREA_ABOVE_180MM_RAINFALL_INCREASE_PCT,
    CATCHMENT_RAINFALL_VOLUME_INCREASE_PCT,
    CLAUSIUS_CLAPEYRON_BASELINE_PCT_PER_DEGC,
    HOURLY_RAINFALL_INTENSITY_INCREASE_PCT_PER_DEGC,
    MECHANISM_BREAKDOWN_PCT,
    SIX_HOUR_RAINFALL_RATE_INCREASE_PCT,
)


@dataclass(frozen=True)
class ValenciaAttribution:
    """October 2024 Valencia flash-flood attribution numbers, vs. a
    pre-industrial counterfactual."""

    hourly_intensity_increase_pct_per_degc: float = HOURLY_RAINFALL_INTENSITY_INCREASE_PCT_PER_DEGC
    six_hour_rate_increase_pct: float = SIX_HOUR_RAINFALL_RATE_INCREASE_PCT
    area_above_180mm_increase_pct: float = AREA_ABOVE_180MM_RAINFALL_INCREASE_PCT
    catchment_volume_increase_pct: float = CATCHMENT_RAINFALL_VOLUME_INCREASE_PCT


VALENCIA_ATTRIBUTION = ValenciaAttribution()


def hourly_rainfall_intensity_increase_pct_per_degc() -> float:
    return HOURLY_RAINFALL_INTENSITY_INCREASE_PCT_PER_DEGC


def exceeds_clausius_clapeyron_scaling() -> bool:
    """Whether the observed intensification exceeds the ~7%/degC
    thermodynamic (Clausius-Clapeyron) baseline -- indicating dynamical
    amplification on top of simple moisture-holding-capacity increase,
    not merely a warmer-air-holds-more-water restatement."""
    return (
        HOURLY_RAINFALL_INTENSITY_INCREASE_PCT_PER_DEGC
        > CLAUSIUS_CLAPEYRON_BASELINE_PCT_PER_DEGC
    )


def mechanism_breakdown_pct() -> dict[str, float]:
    """Attributed contribution of each physical sub-mechanism, per
    Calvo-Sancho et al. 2026's model decomposition."""
    return dict(MECHANISM_BREAKDOWN_PCT)


def event_name_and_date() -> str:
    return "Valencia flash flood, October 2024"
