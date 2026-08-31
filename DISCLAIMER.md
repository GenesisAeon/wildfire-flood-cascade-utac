# DISCLAIMER — Real, Multi-Mechanism Science, Deliberately Not Claimed As One System

> **Why no UTAC/CREP/AFET bridge:** not only because the cited literature
> already provides the necessary quantitative structure -- a deliberate
> choice. This project's highly speculative AFET/UTAC experiments must
> never stand in the way of climate/ecology topics being accessible and
> usable to people who don't work inside that construct and aren't
> looking for renormalization groups. Real, checkable science, without
> the burden of an unproven framework. See `PACKAGE_REGISTRY.md`'s "Why
> no UTAC/CREP/AFET bridge in the climate/ecology series" (2026-08-31) in
> the GenesisAeon workspace root for the full canonical note.

**Status: Real, independently verified science across 7 citations. NO
UTAC/CREP/AFET bridge, NO invented Gamma value.**

## Where this package came from

This is the richest single-conversation origin story in the P105-P121
climate/ecology series. Johann's opening observation was subjective:
fires seem to start earlier in the year now, and the traditional rainy
season then brings more precipitation. Over five separate messages he
proposed increasingly specific mechanisms -- smoke-aerosol invigoration,
warmer-SST moisture, forest/canopy-loss flood amplification, degraded
river-channel/floodplain capacity, and large-scale settlement-area
sealing -- each checked one at a time against real, current (2025/2026)
literature rather than built speculatively in advance.

Every citation was independently verified via WebSearch + WebFetch
against the publisher or press-release page (not a search-snippet
summary alone), 2026-08-31. `nature.com` (and the Communications Earth &
Environment / Nature Communications family specifically) consistently
redirects automated fetches to an `idp.nature.com` auth gate;
verification instead used PMC mirrors, phys.org/earth.com press
coverage, and cross-referencing 2+ independent sources for title/
author/DOI/finding agreement.

## Why the synthesis module is included on purpose

It would have been easy to present Johann's full combined causal chain
as if it were itself an established finding, since every individual
link in it is real. It is not: no single paper in the literature studies
"earlier fires -> smoke + SST intensify rain -> forest/channel/
settlement/glacier loss amplifies the resulting flood damage" as one
combined system for one region. `synthesis_hypothesis.py` exists
specifically to keep that distinction explicit and testable --
`is_combined_cascade_a_directly_studied_single_system()` returns
`False` while `component_mechanisms_independently_verified()` returns
`True`. This mirrors the same honesty-check convention used throughout
the P114-P120 series (see `coral-reef-utac`'s Walker et al. 2023
precedent), applied here at the level of a whole causal chain rather
than a single complicating citation.

## Why the fifth citation corrects the DOI from an earlier pass

`FAN_2026_CITATION`'s DOI was surfaced imprecisely in an initial broad
DeepResearch pass (2026-08-31, alongside `el-nino-amplification-utac`
P118, `marine-heatwave-utac` P119, `antarctic-ice-shelf-utac` P120) and
deliberately deferred rather than built on a shaky citation. A dedicated
follow-up research pass corrected it to `10.1029/2025GL121153` and
established the paper's real, regionally-divergent (not globally
uniform) finding before this package was built.

## What this is NOT

- **Not a claim that fire-season shift is globally uniform.**
  `is_shift_direction_uniform_globally()` returns `False` -- boreal/
  taiga shifts earlier, Mediterranean/desert shifts later, in the
  opposite direction.
- **Not a claim that flood-hazard drivers act independently of each
  other in every region.** Each mechanism is documented as a real,
  separately-attributed effect; this package does not claim they sum
  linearly or that all six operate simultaneously in any one place.
- **Not a claim that Kang et al. 2025's mechanism is soil
  hydrophobicity.** `is_mechanism_soil_hydrophobicity()` returns
  `False` -- the paper's own explicit finding is canopy/litter
  interception loss instead.
- **Not a re-derivation of glacier-buffer loss.**
  `glacier_buffer_cross_reference()` points to `glacier-buffer-utac`
  (P99, Huss & Hock 2018) rather than duplicating that citation here.
- **Not a UTAC/CREP/AFET-bridged package.** No Gamma value is assigned.

## References

- Fan, S., Tao, W., Zhang, Y., Shindell, D., Zhang, Y. (2026).
  "Regionally divergent shifts in global fire season timing under
  recent warming." *Geophysical Research Letters*.
  DOI: 10.1029/2025GL121153.
- Madakumbura, G.D., et al. (2025). "Advancing fire season onset across
  California ecoregions." *Science Advances*. DOI: 10.1126/sciadv.adt2041.
- Zhu, H., Zhao, H., Yang, S., et al. (2025). "Wildfire smoke aerosols
  invigorate precipitation across fire-impacted regions." *npj Climate
  and Atmospheric Science*, 8, 170. DOI: 10.1038/s41612-025-01047-3.
- Calvo-Sancho, C., Diaz-Fernandez, J., Gonzalez-Aleman, J.J., et al.
  (2026). "Anthropogenic warming intensified the October 2024 Valencia
  flash-flood rainfall." *Nature Communications*.
  DOI: 10.1038/s41467-026-68929-9.
- Kang, T-H., et al. (2025). "Interception reduction from deforestation
  and forest fire increases large-scale fluvial flooding risk."
  *Communications Earth & Environment*. DOI: 10.1038/s43247-025-02748-6.
- Hawker, L., Darby, S., Slater, L., et al. (2026). "River channel
  change can affect flood hazard and impact substantially."
  *Communications Earth & Environment*. DOI: 10.1038/s43247-026-03517-9.
- Azadgar, A., Benedini, A., Salata, S., Lacoere, P., Badach, J., Nyka,
  L. (2026). "Flood-sensitive land take (FSL) analysis: A new way to
  read how urban sealing shapes flood risk." *Journal of Environmental
  Management*. DOI: 10.1016/j.jenvman.2026.129513.

All verified via WebSearch + WebFetch (2026-08-31). Originating context:
a direct conversational sequence with Johann, following up on the
broader El Nino/climate DeepResearch pass that produced P118-P120.
