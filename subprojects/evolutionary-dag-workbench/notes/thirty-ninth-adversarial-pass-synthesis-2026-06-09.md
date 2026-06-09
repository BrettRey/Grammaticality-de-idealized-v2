# Thirty-Ninth Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** Repeated temporal-anchor pressure plus Brett's narrative-present and modal-perfect guard examples.
**Change type:** Graph mutation, protocol-bound evaluation, no score movement.

## What Changed

Added controlled ontology nodes:

- `tense_aspect_value`
- `temporal_anchor_expression`
- `temporal_anchor_fit`
- `current_relevance_relation`
- `continuative_interval_relation`
- `experiential_relevance_frame`
- `narrative_perspective_frame`
- `modal_temporal_inference_frame`

Added phenomenon card:

- `phenomena/cards/narrative-present-past-time-frame.md`
- `phenomena/cards/modal-perfect-by-now-inference.md`

Added graph:

- `graphs/archive/temporal-anchor-alignment-candidate.json`

Added evaluation:

- `evaluations/protocol-tests/temporal-anchor-alignment-2026-06-09.json`

## Mutation Rationale

`FRAME` partly survived three temporal cards but repeatedly lacked the same construct family:

- `perfect-definite-past-time`;
- `continuative-perfect-since-cgel`;
- `perfect-already-yesterday-cgel`.

The missing structure was not generic constructional frame fit. It was tense/aspect-specific
temporal anchoring: whether a tense/aspect value fits a definite past-time expression, a
continuative interval, current relevance, or an experiential frame.

Brett's narrative-present example added a guard against overfitting:

> So, I'm walking down the street one morning last year, and this guy waves to me.

That case shows that a past-time expression does not automatically exclude present-tense
morphology. A narrative perspective frame can license present-tense viewpoint inside a past story
world.

Brett's modal-perfect example added a second guard:

> I haven't heard for sure, but he will have arrived by now.

This case should not be analyzed as future tense in English. The useful construct is a modal
temporal inference frame: `will` plus perfect can present completion as inferable by the reference
time without collapsing modal force into tense/aspect value.

## Result

`temporal-anchor-alignment-candidate` survives the built-on temporal cards. It is not promoted:

- no held-out temporal card has tested it yet;
- no score movement is authorized;
- it is a narrow temporal-anchor module, not a general account.

The main boundary is now clear. `FRAME` remains the better module for broad question-answer and
construction-specific dependency licensing. `TEMP` is the candidate for temporal-anchor fit.
