# Twenty-Second Adversarial Pass Synthesis: Noisy-Channel Subtypes

**Date:** 2026-06-09
**Inputs:** four Gibson-backed noisy-channel subtype cards
**Target graph:** `repair-neighbour-reconstruction-candidate`
**Result:** candidate survives one subtype cleanly, partly survives three; no promotion.

## Trigger

`repair-neighbour-reconstruction-candidate` initially survived the omnibus
`noisy-channel-overacceptance-gibson` card, but a single broad card is too weak for scope promotion.
The next move was to split the source pressure into narrower cards.

## New Cards

Four cards were added:

- `missing-verb-phrase-illusion-gibson`
- `depth-charge-semantic-illusion-gibson`
- `comparative-illusion-noisy-channel-gibson`
- `edit-distance-acceptability-gibson`

They separate omitted-material repair, semantic illusion, comparative/category-sensitive illusion,
and edit-distance/length effects.

## Evaluation Result

The protocol-bound evaluation is
`evaluations/protocol-tests/repair-neighbour-reconstruction-gibson-subtypes-2026-06-09.json`.

Results:

- `missing-verb-phrase-illusion-gibson`: survives as a module. This is the clean case for
  `repair_neighbour_distance`.
- `depth-charge-semantic-illusion-gibson`: partly survives. The graph needs a meaning-prior or
  intended-meaning-plausibility construct.
- `comparative-illusion-noisy-channel-gibson`: partly survives. `CAT` remains needed for
  category/function-analysis tasks.
- `edit-distance-acceptability-gibson`: partly survives. The graph needs length or information-mass
  normalization.

## Decision

Do not promote `repair-neighbour-reconstruction-candidate` yet.

The candidate is no longer a one-card accident, but it is still too narrow. It has earned standing
as a useful candidate, not as a scoped module.

## Next Mutation Pressure

The strongest new construct pressure is not another generic processing node. It is a normalization
construct:

- target sentence length;
- target information mass;
- repair distance normalized by target information.

This should be tested with edit-distance/length cards before any new candidate receives a scoped
label.
