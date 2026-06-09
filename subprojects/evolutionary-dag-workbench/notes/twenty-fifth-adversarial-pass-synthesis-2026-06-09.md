# Twenty-Fifth Adversarial Pass Synthesis: Meaning-Prior Reconstruction

**Date:** 2026-06-09
**Inputs:** `depth-charge-semantic-illusion-gibson`, `comparative-illusion-noisy-channel-gibson`
**Result:** new unscored candidate; no scoped-module label.

## Trigger

The twenty-fourth pass showed that `information-normalized-repair-candidate` remains too
surface-oriented for depth-charge semantic illusions. It can represent repair distance and target
information mass, but not the independent fact that a reconstructed intended meaning may be much
more plausible than the literal compositional meaning.

## Mutation

Two ontology nodes were added:

- `intended_meaning_plausibility`
- `literal_composition_coherence`

The new graph is `graphs/archive/meaning-prior-reconstruction-candidate.json`.

It separates:

- plausible intended meaning;
- literal compositional coherence;
- semantic-pragmatic recoverability;
- felt naturalness and reported acceptability;
- task-sensitive grammaticality attribution.

## Evaluation Result

The protocol-bound evaluation is
`evaluations/protocol-tests/meaning-prior-reconstruction-2026-06-09.json`.

Results:

- `depth-charge-semantic-illusion-gibson`: survives as a semantic noisy-channel module.
- `comparative-illusion-noisy-channel-gibson`: partly survives, because category/function analysis
  remains a `CAT` problem.

## Decision

Do not promote the candidate yet.

It has one clean semantic-illusion win and one partial comparative-illusion result. It should be
held as an unscored candidate until tested on more semantic-prior cards.
