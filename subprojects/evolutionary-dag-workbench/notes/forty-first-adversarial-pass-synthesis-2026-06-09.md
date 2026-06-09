# Forty-First Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** Held-out temporal/modal test for `TEMP`.
**Change type:** Held-out evaluation, no graph mutation, no score movement.

## What Changed

Added phenomenon card:

- `phenomena/cards/modal-preterite-remoteness-cgel.md`

Added evaluation:

- `evaluations/protocol-tests/temporal-anchor-heldout-modal-preterite-2026-06-09.json`

No ontology nodes and no graph edges were added.

## Evaluation Rationale

`TEMP` was built from perfect, narrative-present, and modal-perfect-by-now cases. It needed a
held-out test before any scoped label. CGEL's modal-preterite contrasts are the right next pressure:

- `I wish he was here` uses preterite form for a present-time situation;
- `I'd rather you went tomorrow` uses preterite form for a future-time situation;
- remote conditionals contrast with open conditionals without a simple event-time difference.

These cases test whether the graph keeps tense/aspect form separate from event time and whether it
has enough modal-frame machinery.

## Result

`TEMP` partly survives:

- it separates `tense_aspect_value` from `temporal_anchor_expression`;
- it routes temporal fit through `temporal_anchor_fit`;
- it keeps recoverability and reported acceptability out of licensing;
- it therefore avoids the worst error: treating every preterite as simple past-time anchoring.

But it lacks a modal-remoteness or remote-conditional frame construct. The existing
`modal_temporal_inference_frame` is not the right node: it was introduced for modal auxiliary plus
perfect/anterior inference, not modal preterite remoteness.

## Boundary

No promotion follows. `TEMP` remains unscored and has no `scoped_module` label.

One held-out partial survival is not enough to mutate immediately. A second held-out modal or
conditional card would justify adding a `modal_remoteness_frame` or equivalent construct. Until
then, the result is pressure, not repair.
