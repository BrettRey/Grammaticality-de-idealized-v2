# Fifteenth Adversarial Pass Synthesis

**Date:** 2026-06-08
**Trigger:** Run the held-out `prediction_tests` against enriched source-backed cards.

## Result

Some held-out prediction tests now have evidence statuses.

Six held-out CGEL cards were enriched with source-checked contrast examples and evidence notes:

- `case-in-coordination-cgel`
- `pronoun-personhood-proform-gender`
- `nonfinite-verbless-clause-boundaries-cgel`
- `negation-polarity-items-cgel`
- `unbounded-dependency-licensing-cgel`
- `fused-relative-constructions-cgel`

The two held-out CGEL evaluations now distinguish checked support from unresolved cells:

- `context-indexed-dynamic-feedback-heldout-cgel-2026-06-08`
  - `case-formal-correction-prediction`: `passed`
  - `pronoun-policy-framing-prediction`: `mixed`
  - `fragment-genre-prediction`: `passed`
  - `negation-standard-correction-prediction`: `mixed`
- `context-aware-operator-gap-heldout-cgel-2026-06-08`
  - `recoverable-unlicensed-gap-prediction`: `passed`
  - `transparent-rare-relative-prediction`: `inconclusive`

## Why This Matters

This is the first pass where the workbench does more than validate internal coherence. It checks
pre-registered prediction tests against source-backed contrast examples and records whether the
evidence supports, mixes, or fails to settle the prediction.

## Boundary

This still does not authorize numeric score movement. The evidence checked here is source-backed
contrast evidence, not corpus measurement or elicitation. It supports module boundaries and
projectibility bookkeeping, but not calibrated scores.

## Next Pressure Point

The unresolved cells point to the next data needs:

- policy/audience-design evidence for pronoun/personhood judgments;
- variety-specific evidence for dialectal negative patterns under standard correction;
- opportunity-threshold evidence for rare transparent relatives.
