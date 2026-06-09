# Twenty-Fourth Adversarial Pass Synthesis: INR Boundary Test

**Date:** 2026-06-09
**Inputs:** `depth-charge-semantic-illusion-gibson`, `comparative-illusion-noisy-channel-gibson`
**Target graph:** `information-normalized-repair-candidate`
**Result:** partial survival; no graph mutation.

## Trigger

`information-normalized-repair-candidate` survived edit-distance/length and missing-verb cases. The
next question was whether normalization also handles the harder noisy-channel cases:

- semantic illusion, where the plausible repair is meaning-level rather than merely string-level;
- comparative illusion, where category/function analysis can diverge from first-pass reconstruction.

## Evaluation

The protocol-bound evaluation is
`evaluations/protocol-tests/information-normalized-repair-depth-comparative-2026-06-09.json`.

Results:

- `depth-charge-semantic-illusion-gibson`: partly survives. INR captures reconstruction-mediated
  acceptability but lacks a meaning-prior or intended-meaning-plausibility construct.
- `comparative-illusion-noisy-channel-gibson`: partly survives. INR captures the repair channel,
  but `CAT` remains needed for category/function analysis.

## Decision

Do not promote INR.

The candidate is stronger than RNR for edit-distance/length effects, but it remains a repair-distance
module. It should not absorb semantic-prior or category-analysis machinery.

## Next Pressure

Two separate future paths are now clearer:

- a meaning-prior candidate for depth-charge and related semantic illusions;
- a CAT/RNR or CAT/INR evaluation for comparative illusions where category analysis and
  noisy-channel repair interact.
