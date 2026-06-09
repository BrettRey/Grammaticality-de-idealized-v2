# Twenty-Eighth Adversarial Pass Synthesis: CGEL Discriminator Pack

**Date:** 2026-06-09
**Input sources:** targeted CGEL extracts for perfect tense, catenative complement forms, and
subject-verb agreement.

## Added Cards

Created four source-backed CGEL cards:

- `continuative-perfect-since-cgel`
- `catenative-complement-form-selection-cgel`
- `proximity-agreement-error-cgel`
- `collective-number-transparent-agreement-cgel`

These cards target the same pressure zones exposed by the local examples, but now with source-backed
contrast cells.

## Evaluations

Added four protocol-bound no-score-change evaluations:

- `frame-specific-dependency-licensing-continuative-perfect-2026-06-09`
- `selection-collocation-split-catenative-complement-2026-06-09`
- `processing-naturalness-perturbation-proximity-agreement-2026-06-09`
- `context-aware-operator-gap-agreement-overrides-2026-06-09`

All activated paths validate and compute the intended readings.

## Results

`continuative-perfect-since-cgel` partly survives `FRAME`.

`FRAME` keeps frame fit separate from recoverability, but the second tense/aspect card makes the
temporal-anchor pressure stronger. The repeated partial survival suggests that a temporal-anchor or
tense/aspect-alignment construct may soon be justified.

`catenative-complement-form-selection-cgel` partly survives `SEL`.

`SEL` has the selection/collocation split, but it does not yet distinguish same-meaning complement
alternation, meaning-shifting complement alternation, and unlicensed complement-form substitution.
The `allowed doing` card and this CGEL catenative card are now a coherent complement-selection
pressure set.

`proximity-agreement-error-cgel` partly survives `PROC`.

`PROC` handles the processing and task-framing channel, but still lacks agreement-controller and
retrieval-attractor machinery. This source-backs the local nearest-noun agreement card.

`collective-number-transparent-agreement-cgel` partly survives `OPG`.

`OPG` can say agreement is operator-relevant, and it keeps processing perturbation separate, but it
cannot distinguish simple agreement, licensed overrides, number-transparent constructions, and
proximity errors.

## Decision

No graph mutation yet, but the pressure is now more organized.

Three future constructs are plausible if the next card or two repeats the same gaps:

- temporal-anchor or tense/aspect-alignment construct;
- catenative/complement-form subtype construct;
- agreement-controller plus override/retrieval-attractor construct.

## Next Move

Do not add a general hybrid graph. Add one more targeted card in each pressure zone, then mutate
only where the same partial-survival gap repeats across at least two source-backed cards and one
local card.
