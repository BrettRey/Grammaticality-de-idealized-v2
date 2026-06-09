# Phenomenon Card: modal preterite remoteness

**Stress test:** Preterite form, non-past time reference, and modal remoteness.

## Description

CGEL distinguishes ordinary temporal uses of the preterite from modal-preterite uses where the
preterite marks remoteness rather than past time:

- present-time modal preterite: `I wish he was here`;
- present-time non-remote counterpart: `I'm glad he is here`;
- future-time modal preterite: `I'd rather you went tomorrow`;
- future-time non-remote counterpart: `I bet you go tomorrow`;
- remote conditional: `If he was here, he'd be upstairs`;
- open conditional: `If he is here, he'll be upstairs`.

In these contrasts, the time of the subordinate situation can be present or future. The preterite
form is doing modal work: it marks remoteness, preference, counterfactual orientation, or reduced
likelihood under the relevant construction.

## Source Pointers

- Source IDs: `cgel-past-tense-uses`
- Local source: `/Users/brettreynolds/Documents/CGEL/out/028_6 Further uses of the past tenses 148.pdf`
- Related cards: [modal-perfect-by-now-inference](modal-perfect-by-now-inference.md),
  [narrative-present-past-time-frame](narrative-present-past-time-frame.md),
  [perfect-definite-past-time](perfect-definite-past-time.md)

## Held-Out Status

This card was not used to build `temporal-anchor-alignment-candidate`. It is a held-out test of
whether `TEMP` can project beyond perfect/narrative/modal-perfect anchor cases.

## Why It Matters

The card blocks an event-time reading of tense morphology. A graph that treats every preterite as
past-time anchoring fails immediately. The issue is the interaction between tense/aspect form,
constructional modal frame, and temporal-anchor fit.

## Minimum Contrast Cells

- present-time modal preterite in `wish`;
- present-time non-remote present in `glad`;
- future-time modal preterite in `rather` or remote conditional;
- future-time open conditional with present tense;
- past-time remote conditional requiring preterite perfect.

## Candidate Nodes

- tense_aspect_value
- temporal_anchor_expression
- temporal_anchor_fit
- constructional_frame_fit
- operator_value
- semantic_pragmatic_recoverability
- community_licensing
- reported_acceptability
- grammaticality_attribution

## Potential Construct Pressure

This card probably needs a modal-remoteness or remote-conditional frame construct if the workbench
wants TEMP to handle it directly. The current `modal_temporal_inference_frame` is about modal
inference with perfect/anterior anchoring, not modal preterite remoteness.

## Graph Failure Modes

- Treats preterite form as always locating the situation in past time.
- Treats modal remoteness as the same thing as modal inference.
- Treats present-time and future-time modal preterites as tense errors.
- Collapses open and remote conditionals.
- Treats recoverability of the intended proposition as licensing the tense/modality contrast.

## Predicted Discriminators

- `TEMP` should partly survive by separating tense/aspect value from event time and temporal-anchor
  expression, but it should expose a missing modal-remoteness frame.
- `FRAME` may partly survive as broad constructional frame fit.
- `PROC` should not explain the contrast as processing difficulty.
