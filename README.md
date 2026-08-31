# wildfire-flood-cascade-utac

GenesisAeon Package 121 — a real, seven-citation cascade: fire-season
timing shift (regionally divergent), two independent precipitation-
intensification mechanisms, and three independent flood-severity-
amplification mechanisms. **Deliberately has no UTAC/CREP/AFET bridge**
— see [DISCLAIMER.md](DISCLAIMER.md).

## Where this package came from

Johann's own subjective observation ("fires seem to start earlier now,
and the traditional rainy season then brings more precipitation")
followed by five of his own proposed mechanism hypotheses, raised one
message at a time and each independently checked against real
literature, 2026-08-31.

## What's real here

1. **Fan et al. (2026, *GRL*)** + **Madakumbura et al. (2025, *Science
   Advances*)** — fire-season timing shift is real but **regionally
   divergent**: boreal/taiga earlier, Mediterranean/desert later and
   extended, prairie/humid muted. California onset advanced 6-46 days
   across 11 of 13 ecoregions, 1992-2020.
2. **Zhu et al. (2025, *npj Climate and Atmospheric Science*)** — smoke
   aerosols act as cloud-condensation/ice-nucleating particles, delaying
   coalescence to higher altitude and intensifying latent-heat release,
   across 5 fire-impacted regions.
3. **Calvo-Sancho et al. (2026, *Nature Communications*)** — the October
   2024 Valencia flash flood: hourly rainfall intensity +20%/degC C
   (exceeding simple Clausius-Clapeyron ~7%/degC scaling), 6-hour rate
   +21%, area above 180mm rainfall +55%, vs. a pre-industrial
   counterfactual.
4. **Kang et al. (2025, *Communications Earth & Environment*)** — SE
   Australia, 3 real megafires, 50-year streamflow record: annual flood
   probability rose from ~1-in-64-years to ~1-in-8-years after a
   megafire, via canopy/litter interception loss (explicitly **not**
   soil hydrophobicity).
5. **Hawker et al. (2026, *Communications Earth & Environment*)** —
   standard channel-capacity assumptions underestimate flood extent by
   9-152% and population exposure by 15-472%, Mississippi basin; channel
   geometry change shifts flood risk by a magnitude comparable to
   climate change over the same period.
6. **Azadgar et al. (2026, *Journal of Environmental Management*)** —
   a real WASI/NWASI land-take framework across 4 European cities
   (Gdansk, Milan, Ghent, Oslo), 2012-2018: sealing measurably reduces
   stormwater retention capacity.

## Deliberately not one system

`is_combined_cascade_a_directly_studied_single_system()` returns
`False` — no single paper studies Johann's full combined causal chain
(earlier fires -> intensified precipitation -> amplified flood damage
via forest/channel/settlement/glacier factors) as one system for one
region. Every individual link is real and independently verified; the
combination is a plausible, mechanistically-grounded synthesis, not an
established finding. `glacier_buffer_cross_reference()` points to
`glacier-buffer-utac` (P99, Huss & Hock 2018) for the glacier-loss half
rather than re-deriving it here.

## Installation

```bash
pip install wildfire-flood-cascade-utac
```

## Quick start

```python
from wildfire_flood_cascade_utac import (
    is_shift_direction_uniform_globally,
    flood_probability_increase_factor,
    is_combined_cascade_a_directly_studied_single_system,
)

is_shift_direction_uniform_globally()  # False -- regionally divergent
flood_probability_increase_factor()  # ~7.9x, Kang et al. 2025
is_combined_cascade_a_directly_studied_single_system()  # False -- the honesty check
```

## License

Code: MIT. Documentation/data notes: see [DISCLAIMER.md](DISCLAIMER.md).

## Citation

See [CITATION.cff](CITATION.cff).
