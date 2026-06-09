# Forty-Second Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** Second held-out temporal/modal pressure test for `TEMP`.
**Change type:** Held-out evaluation, no graph mutation, no score movement.

## What Changed

Added phenomenon card:

- `phenomena/cards/backshifted-preterite-orientation-cgel.md`

Added evaluation:

- `evaluations/protocol-tests/temporal-anchor-heldout-backshifted-preterite-2026-06-09.json`

No ontology nodes and no graph edges were added.

## Evaluation Rationale

The modal-preterite card showed that `TEMP` cannot yet handle preterite form used for present or
future situation time under modal remoteness. The next question was whether that gap is only modal
remoteness or a broader orientation problem.

CGEL's backshifted-preterite discussion supplies the discriminator:

- `Jill said she had too many commitments` can report an original present-tense proposition;
- `If he knew she had too many commitments...` can embed backshift under a modally remote matrix
  clause while the embedded situation remains present;
- the backshifted preterite is not ordinary deictic past time and not modal remoteness.

## Result

`TEMP` partly survives again:

- it avoids treating tense/aspect form as a direct licensing cause;
- it routes tense/aspect cases through temporal-anchor fit;
- it keeps recoverability and reported acceptability away from licensing.

But the missing construct is now clearer. A modal-remoteness-only repair would be too narrow.
Backshift shows that the graph needs a temporal-orientation frame: a construct for whether the time
of orientation is deictic, matrix/report-supplied, modal-remote, narrative, or otherwise supplied by
the construction.

## Boundary

No promotion follows. `TEMP` remains unscored and has no `scoped_module` label.

The next mutation is now justified if the workbench continues the temporal lane: add a controlled
`temporal_orientation_frame` or equivalent node, route modal-preterite and backshifted-preterite
cards through it, and keep it distinct from `modal_temporal_inference_frame`.
