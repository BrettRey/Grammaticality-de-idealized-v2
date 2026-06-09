# Twenty-First Adversarial Pass Synthesis: Repair-Neighbour Reconstruction

**Date:** 2026-06-09
**Input:** `noisy-channel-overacceptance-gibson`
**Result:** new unscored candidate; no scoped-module label; no numeric score movement.

## Trigger

`PROC` partly survived noisy-channel overacceptance by routing inflated acceptability through:

- semantic-pragmatic recoverability;
- felt naturalness;
- task-sensitive attribution.

That was not enough. The Gibson card distinguishes strings with a close intended repair from
equally defective strings without a plausible nearby repair. General recoverability is too broad for
that contrast.

## Mutation

The new graph is `graphs/archive/repair-neighbour-reconstruction-candidate.json`.

It introduces `repair_neighbour_distance` as a separate construct and tests three claims:

- greater repair-neighbour distance lowers recovery of the intended form;
- greater repair-neighbour distance lowers felt naturalness and reported acceptability;
- literal-analysis framing can reverse first-pass overacceptance without treating acceptability as
  licensing.

## Evaluation Result

The protocol-bound evaluation is
`evaluations/protocol-tests/repair-neighbour-reconstruction-2026-06-09.json`.

`repair-neighbour-reconstruction-candidate` survives the noisy-channel card as a module, but it
remains `unscored`. A one-card success is not enough for a `scoped_module` label.

## Boundary

This candidate is not a general processing account. `PROC` remains the better broader module for
garden paths, dependency locality, legalese comprehension, center embedding, and hard-but-licensed
cases. The new candidate is a narrower reconstruction module for cases where the distance to an
intended repair neighbour is the operative contrast.

## Next Stress Tests

1. Build separate cards for comparative illusions, missing-verb materials, and duplicated/missing
   function-word cases.
2. Test whether repair-neighbour distance predicts overacceptance independently of sentence length.
3. Test whether `CAT` is needed when the noisy-channel case also perturbs category assignment.
