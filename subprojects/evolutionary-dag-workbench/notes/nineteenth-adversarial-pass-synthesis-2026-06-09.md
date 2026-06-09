# Nineteenth Adversarial Pass Synthesis: Frame-Specific Dependency Licensing

**Date:** 2026-06-09
**Inputs:** `frame-conditioned-duration-have`, `island-construction-variation-gibson`
**Result:** new scoped module; no numeric score movement.

## Trigger

The eighteenth pass left two adjacent pressure points:

- `frame-conditioned-duration-have` showed that broad recoverability is too coarse. `I have five
  years` is recoverable in both cells, but only the remaining-duration question supplies the frame
  in which the have-duration answer is licensed.
- `island-construction-variation-gibson` showed that global island/non-island labels are too coarse.
  The relevant dependency status varies with construction type, discourse role, and control
  comparison rather than with extraction topology alone.

`OPG` and `UPT` both partly survived these cards, but each represented the missing contrast too
broadly. `OPG` has operator value and recoverability; `UPT` has update-role configuration and
operator-repertoire membership. Neither had a narrow construct for constructional frame fit or for
construction-specific dependency licensing.

## Mutation

The pass added three controlled ontology nodes:

- `repair_neighbour_distance`
- `constructional_frame_fit`
- `construction_specific_dependency_licensing`

The new graph is `graphs/archive/frame-specific-dependency-licensing-candidate.json`.

It is deliberately narrow. It tests whether the next level of contrast should route through:

- `constructional_frame_fit` for question-answer and response-slot licensing;
- `construction_specific_dependency_licensing` for construction-conditioned dependency status;
- recoverability only as a reported-acceptability perturbation, not as a licensing shortcut.

## Evaluation Result

The protocol-bound evaluation is
`evaluations/protocol-tests/frame-specific-dependency-licensing-2026-06-09.json`.

Both cards survive as scoped-module tests:

- `frame-conditioned-duration-have`: survives as a frame-fit module.
- `island-construction-variation-gibson`: survives as a construction-specific dependency module.

The graph receives `score_status.kind: scoped_module` and keeps all numeric scores at zero.

## What This Does Not Solve

This is not a general dependency account. It does not replace:

- `OPG`'s opportunity-normalized attestation and preemption machinery;
- `UPT`'s broader uptake/repertoire boundary machinery;
- `PROC`'s processing-cost and naturalness-perturbation machinery;
- `DYN` or `TASK` for diachronic, institutional, or production/judgment divergence.

The new graph also does not yet answer whether construction-specific dependency licensing is
projectible beyond the first Gibson island card. It needs held-out dependency cards before any
numeric score movement would be defensible.

## Next Stress Tests

1. Add at least two more dependency cards that vary construction type independently of processing
   load and recoverability.
2. Test `FRAME` against `unbounded-dependency-licensing-cgel` and `left-branch-extraction` to see
   whether it complements or duplicates `OPG`.
3. Keep noisy-channel overacceptance separate for now; it pressures `repair_neighbour_distance`,
   not construction-specific dependency licensing.
4. Run `legalese-center-embedding-gibson` against `PROC` before inventing a genre-processing hybrid.
