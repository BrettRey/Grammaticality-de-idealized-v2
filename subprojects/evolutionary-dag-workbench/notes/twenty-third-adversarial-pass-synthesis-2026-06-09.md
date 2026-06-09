# Twenty-Third Adversarial Pass Synthesis: Information-Normalized Repair

**Date:** 2026-06-09
**Inputs:** `edit-distance-acceptability-gibson`, `missing-verb-phrase-illusion-gibson`
**Result:** new unscored successor candidate; no scoped-module label.

## Trigger

The twenty-second pass showed that `repair-neighbour-reconstruction-candidate` has the right raw
repair-distance construct but cannot represent Gibson's rational-inference pattern: the same number
of edits can have different acceptability effects depending on the length or information content of
the intended target.

## Mutation

Two ontology nodes were added:

- `target_information_mass`
- `information_normalized_repair_distance`

The new graph is `graphs/archive/information-normalized-repair-candidate.json`.

The graph distinguishes:

- raw distance to a repair neighbour;
- target sentence length or information mass;
- normalized repair distance;
- felt naturalness and reported acceptability effects;
- task-sensitive grammaticality attribution.

## Evaluation Result

The protocol-bound evaluation is
`evaluations/protocol-tests/information-normalized-repair-2026-06-09.json`.

The candidate survives:

- `edit-distance-acceptability-gibson`, because it predicts both raw-distance penalty and
  information-mass cushioning;
- `missing-verb-phrase-illusion-gibson`, because it preserves the close-repair reconstruction path.

It remains unscored and does not receive a `scoped_module` label. The graph has not yet been tested
against depth-charge semantic illusions or comparative/category-sensitive noisy-channel cases.

## Boundary

This mutation improves `RNR`; it does not replace `PROC`, `CAT`, or a future meaning-prior module.

The key result is narrower: noisy-channel overacceptance now has a candidate path from raw repair
distance plus target information mass to reported acceptability, without promoting acceptability to
community licensing.
