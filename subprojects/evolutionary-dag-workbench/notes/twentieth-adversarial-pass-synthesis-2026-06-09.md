# Twentieth Adversarial Pass Synthesis: Legalese Against Processing

**Date:** 2026-06-09
**Input:** `legalese-center-embedding-gibson`
**Target graph:** `processing-naturalness-perturbation-candidate`
**Result:** no graph mutation; no numeric score movement.

## Trigger

The Gibson legalese card was deliberately ambiguous between three mechanisms:

- genre and institutional persistence;
- production and professional-setting stability;
- processing, comprehension, naturalness, and preference costs.

The eighteenth pass showed that `DYN` and `TASK` partly survive the card but lack direct processing
or comprehension machinery. Before inventing a genre-processing hybrid, the correct next move was to
test whether the processing side is already covered by `PROC`.

## Evaluation

The new protocol-bound evaluation is
`evaluations/protocol-tests/processing-naturalness-perturbation-gibson-legalese-2026-06-09.json`.

`PROC` partly survives:

- `processing_cost -> felt_naturalness_context -> reported_acceptability` captures the legalese
  preference/comprehension penalty.
- `semantic_pragmatic_recoverability -> felt_naturalness_context -> reported_acceptability`
  captures the plain-English paraphrase advantage.
- `task_framing -> grammaticality_attribution` keeps officialness, preference, comprehension, and
  grammaticality tasks apart.

The evaluation forbids treating processing cost or reported acceptability as causal routes into
community licensing.

## Decision

No genre-processing hybrid graph is justified yet.

The legalese card is better treated as a compositional discriminator:

- `DYN` covers genre/register and norm-centre pressure.
- `TASK` covers production-setting and judgment-setting separation.
- `PROC` covers processing, naturalness, comprehension, and preference perturbation.

This is a good result for the workbench: a complex card can require a module bundle without forcing
the invention of a new graph family.

## Remaining Pressure Point

Noisy-channel overacceptance remains unresolved. That card pressures `PROC` toward
`repair_neighbour_distance`; legalese does not.
