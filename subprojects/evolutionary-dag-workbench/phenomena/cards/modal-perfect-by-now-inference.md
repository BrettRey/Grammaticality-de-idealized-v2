# Phenomenon Card: modal perfect with by-now inference

**Stress test:** Modal inference, perfect/anterior anchoring, and the absence of an English future tense.

## Description

English `will` can combine with the perfect to present an event as inferably complete by the
reference time:

- modal perfect inference: `I haven't heard for sure, but he will have arrived by now`;
- non-perfect prospective modal: `He will arrive by noon`;
- by-now completion without `will`: `He has probably arrived by now`;
- non-perfect `will` plus `by now` under the completed-by-now reading: `*He will arrive by now`.

The contrast is not a future-tense contrast. `Will` is a modal auxiliary, and the licensing question
concerns how modal inference, perfect/anterior meaning, and the `by now` reference-time anchor fit
together.

## Source Pointers

- Source IDs: `brett-modal-perfect-by-now`
- Related cards: [perfect-definite-past-time](perfect-definite-past-time.md),
  [perfect-already-yesterday-cgel](perfect-already-yesterday-cgel.md),
  [narrative-present-past-time-frame](narrative-present-past-time-frame.md)

## Why It Matters

This card prevents the temporal-anchor graph from becoming a tense-label graph. A graph that calls
`will have arrived by now` a future-tense case has already lost the needed distinction. The useful
construct is a modal temporal inference frame feeding temporal-anchor fit.

## Minimum Contrast Cells

- modal `will` plus perfect plus `by now` completion inference;
- present perfect or modal-probability paraphrase plus `by now`;
- `will` plus non-perfect verb with a prospective deadline such as `by noon`;
- non-perfect `will` plus `by now` under a completed-by-now reading.

## Candidate Nodes

- modal_temporal_inference_frame
- tense_aspect_value
- temporal_anchor_expression
- temporal_anchor_fit
- current_relevance_relation
- constructional_frame_fit
- community_licensing
- reported_acceptability
- grammaticality_attribution

## Potential Construct Pressure

This card adds a modal-inference path to the temporal-anchor graph. It does not justify a separate
future-tense construct for English.

## Graph Failure Modes

- Treats English `will` as future tense.
- Treats `by now` as equivalent to `yesterday`.
- Treats modal inference as reported certainty.
- Treats all `will` plus `by` expressions as the same prospective temporal frame.
- Collapses perfect/anterior anchoring with event-time location.

## Predicted Discriminators

- `TEMP` should survive only if it keeps modal inference distinct from tense/aspect value.
- `FRAME` may partly survive as broad frame fit, but it should not earn the modal/anterior contrast.
- `PROC` should not explain the contrast as processing difficulty.
