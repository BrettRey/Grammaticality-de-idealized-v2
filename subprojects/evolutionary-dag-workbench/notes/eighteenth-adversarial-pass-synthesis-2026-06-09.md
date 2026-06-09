# Eighteenth Adversarial Pass Synthesis

**Date:** 2026-06-09
**Input:** Gibson-backed cards plus `frame-conditioned-duration-have`
**Question:** do the new cards force graph mutation?

## Result

Not yet. They do force sharper module boundaries.

Five no-score-change protocol evaluations were added:

- `processing-naturalness-perturbation-gibson-2026-06-09`
- `context-aware-operator-gap-frame-island-2026-06-09`
- `uptake-operator-boundary-frame-island-2026-06-09`
- `context-indexed-dynamic-feedback-gibson-legalese-2026-06-09`
- `context-indexed-task-separated-feedback-gibson-legalese-2026-06-09`

## Findings

`PROC` survives `dependency-locality-alternations-gibson` and
`garden-path-temporary-ambiguity-gibson`. These are clean processing/naturalness cases:
processing cost can lower felt naturalness and reported acceptability without lowering licensing.

`PROC` only partly survives `noisy-channel-overacceptance-gibson`. Recoverability is present, but
the card likely needs a more specific construct: distance to a plausible intended form or repair
neighbour.

`UPT` survives `frame-conditioned-duration-have`. The contrast between `How old are you?` / `I have
five years` and `How long do you have left?` / `I have five years` is a compact update-role/frame-fit
test. `OPG` partly survives because it separates recoverability from licensing, but `operator_value`
is too coarse for the question-answer frame distinction.

`OPG` and `UPT` both partly survive `island-construction-variation-gibson`. `OPG` has opportunity,
preemption, recoverability, licensing, and repair pressure. `UPT` has construction-specific
update-role machinery. Neither alone yet represents construction-specific dependency licensing.

`DYN` and `TASK` both partly survive `legalese-center-embedding-gibson`. They represent genre,
production, judgment, and norm-centre channels, but not the processing/comprehension burden Gibson
foregrounds.

## Pressure Points

1. `intended_form_distance` or `repair_neighbour_distance` for noisy-channel overacceptance.
2. `constructional_frame_fit` for cases like `I have five years` if broad update-role vocabulary
   proves too coarse.
3. `construction_specific_dependency_licensing` for island variation if `OPG` plus `UPT` cannot
   predict construction-by-construction contrasts.
4. A possible legalese hybrid only if `PROC`, `DYN`, and `TASK` cannot be composed at evaluation
   time.

## Decision

No new graph yet. The next mutation should be driven by one of the pressure points above after a
second card forces the same missing construct.
