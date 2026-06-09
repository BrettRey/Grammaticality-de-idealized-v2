# Twenty-Sixth Adversarial Pass Synthesis: Local Operator-Contrast Cards

**Date:** 2026-06-09
**Input:** Brett local contrast examples:

- `I did it` / `I have done it` / `I did it yesterday` /
  `*I have done it yesterday`;
- nearest-noun agreement attraction;
- `know`/`believe`/`wonder` with `that` and `whether` complements.

## Added Cards

Created three local minimal-pair cards:

- `perfect-definite-past-adverbial`
- `nearest-noun-agreement-attraction`
- `attitude-complement-selection`

These are compact contrast cells, not source-backed evidence yet. Their job is to pressure the
graph inventory before broader CGEL, corpus, or elicitation sourcing.

## Evaluations

Added three protocol-bound no-score-change evaluations:

- `frame-specific-dependency-licensing-perfect-adverbial-2026-06-09`
- `processing-naturalness-perturbation-nearest-agreement-2026-06-09`
- `selection-collocation-split-attitude-complement-2026-06-09`

The activated paths validate and compute the intended path readings.

## Results

`perfect-definite-past-adverbial` partly survives `FRAME`.

`FRAME` separates constructional frame fit from semantic recoverability, so it blocks the bad
collapse: the present-perfect-plus-`yesterday` cell is transparent but not licensed in the target
English repertoire. The partial result matters because `constructional_frame_fit` is still broad.
The card exposes a possible temporal-anchor or tense/aspect value-alignment construct, but one card
is not enough to mutate the graph.

`nearest-noun-agreement-attraction` partly survives `PROC`.

`PROC` correctly routes the nearest-attractor effect through processing, felt naturalness, reported
acceptability, and task framing rather than through community licensing. It remains partial because
it cannot predict which feature configurations produce attraction: an agreement-controller,
feature-alignment, or retrieval-attractor construct is still missing.

`attitude-complement-selection` survives `SEL` as a scoped complement-selection case.

`SEL` already represents complement-type choice as argument-linking selection rather than payload
lexical choice or collocational rigidity. The card nevertheless exposes a possible future need for
a finer complement-type or selected-update-role construct if the workbench needs to predict why
`know`, `believe`, and `wonder` differ without hand-coded predicate classes.

## Decision

No graph mutation is justified yet.

The correct state is:

- record the cards;
- keep numeric scores at zero;
- treat `perfect-definite-past-adverbial` and `nearest-noun-agreement-attraction` as live pressure
  on finer constructs;
- treat `attitude-complement-selection` as new support for `SEL`'s scoped complement-selection
  boundary.

## Next Pressure Points

- Add more tense/aspect anchoring cards before deciding whether a temporal-anchor-fit node is
  warranted.
- Add more agreement-controller cards before introducing an agreement-specific feature-alignment
  or retrieval-attractor construct.
- Compare `SEL`, `FRAME`, and `UPT` on richer complement-type cards before deciding whether
  complement selection needs its own graph family.
