"""This package's honesty-check module.

Johann's own combined causal chain, built up across five separate
messages: fires start earlier -> smoke aerosols + warmer-SST moisture
both intensify precipitation, including heavy-rain events, in the old
traditional rainy season -> that heavier rain then does disproportionate
damage because of forest/canopy loss from the same fires, degraded
river channels and lost floodplains, large-scale settlement-area
sealing, and (regionally) glacier-buffer loss.

Every individual link in that chain is backed by a real, independently
verified paper in this package (or, for glacier-buffer loss, in
glacier-buffer-utac, P99). NO single study in the literature ties all
of these links together as one combined causal system for a specific
region -- this module exists specifically to keep that distinction
explicit rather than implying the full cascade itself has been directly
studied and confirmed.
"""

from __future__ import annotations

from .constants import (
    GLACIER_BUFFER_CROSS_REFERENCE_CITATION,
    GLACIER_BUFFER_CROSS_REFERENCE_PACKAGE,
    GLACIER_BUFFER_CROSS_REFERENCE_PACKAGE_ID,
)

CASCADE_LINKS = (
    "earlier fire-season onset (regionally divergent, not global)",
    "smoke-aerosol precipitation invigoration",
    "warmer SST -> more available moisture -> heavier rain",
    "post-fire canopy/litter interception loss -> higher flood risk",
    "degraded river channel / lost floodplain capacity",
    "large-scale settlement-area sealing",
    "glacier-buffer loss (regional, cross-referenced, not re-derived here)",
)


def combined_cascade_description() -> str:
    return " -> ".join(CASCADE_LINKS)


def is_combined_cascade_a_directly_studied_single_system() -> bool:
    """Whether any single paper in this package studies the full
    combined causal chain as one system for one region. It does not --
    each paper studies one link. Always False."""
    return False


def component_mechanisms_independently_verified() -> bool:
    """Whether each individual link is backed by a real, independently
    verified citation (six in this package plus a cross-reference to
    glacier-buffer-utac). Always True -- distinguishes 'not yet studied
    as a combined system' from 'not real at all'."""
    return True


def number_of_cascade_links() -> int:
    return len(CASCADE_LINKS)


def glacier_buffer_cross_reference() -> str:
    return (
        f"{GLACIER_BUFFER_CROSS_REFERENCE_PACKAGE} "
        f"(GenesisAeon P{GLACIER_BUFFER_CROSS_REFERENCE_PACKAGE_ID}, "
        f"{GLACIER_BUFFER_CROSS_REFERENCE_CITATION}) documents glacier "
        "peak-water/buffer loss as a regional flood-severity amplifier "
        "-- not re-derived in this package."
    )
