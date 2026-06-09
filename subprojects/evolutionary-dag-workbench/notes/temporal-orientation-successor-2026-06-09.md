# Temporal Orientation Successor

**Date:** 2026-06-09
**Target lane:** Temporal-anchor / tense-aspect alignment
**Status:** Successor graph added; no score or scoped label.

## Trigger

`temporal-anchor-alignment-candidate` partly survived two held-out temporal pressure tests:

- `modal-preterite-remoteness-cgel`
- `backshifted-preterite-orientation-cgel`

Both failures pointed to the same missing construct. The old graph separated tense/aspect value,
temporal anchor expression, temporal-anchor fit, narrative perspective, modal temporal inference,
recoverability, and licensing. It did not represent the source of temporal orientation: deictic
speech time, narrative viewpoint, matrix/reporting frame, modal remoteness, or reference-time
orientation.

## Mutation

Added ontology node:

- `temporal_orientation_frame`

Added successor graph:

- `graphs/archive/temporal-orientation-alignment-candidate.json`

Added protocol-bound no-score-change evaluation:

- `evaluations/protocol-tests/temporal-orientation-alignment-2026-06-09.json`

The successor graph adds paths from temporal orientation to temporal-anchor fit and constructional
frame fit. It also lets `narrative_perspective_frame` and `modal_temporal_inference_frame` feed
orientation without collapsing those narrower frames into the broader orientation construct.

## Boundary

This is a successor mutation, not held-out confirmation. The preterite cards exposed the gap and
therefore cannot authorize a scoped label or score movement for the mutated graph.

The successor graph remains unscored and has `score_status.kind: unscored`.

## Decision

Graph mutation: yes, as a successor candidate.

Score movement: no.

Scoped label: no.

Evidence labels: no upgrade. The next useful temporal step would be a fresh held-out temporal card
that was not used to motivate `temporal_orientation_frame`.
