# Phenomenon Card: narrative present with past-time frame

**Stress test:** Past story time, present-tense viewpoint, and temporal-anchor fit.

## Description

A past-time expression can co-occur with present-tense morphology in a narrative-present frame:

- narrative present: `So, I'm walking down the street one morning last year, and this guy waves to me.`
- ordinary past narrative: `So, I was walking down the street one morning last year, and this guy waved to me.`
- non-narrative report: `*I am walking down the street one morning last year` under an ordinary
  current-event reading.

The contrast blocks a simple rule that present-tense forms cannot occur with past-time anchors. The
issue is whether the discourse supplies a narrative perspective frame that licenses present-tense
viewpoint inside a past story world.

## Source Pointers

- Source IDs: `brett-narrative-present-past-time`
- Related cards: [perfect-definite-past-time](perfect-definite-past-time.md),
  [perfect-already-yesterday-cgel](perfect-already-yesterday-cgel.md)

## Why It Matters

This card stress-tests the temporal-anchor graph against overgeneralization. A graph that bans
present morphology whenever a past-time expression is present will fail. The graph needs to
distinguish event-time anchoring from discourse viewpoint.

## Minimum Contrast Cells

- ordinary past narrative with past-time anchor;
- narrative present with past story-time anchor;
- non-narrative present with past-time anchor;
- present-tense current-event report with no past story-time anchor.

## Candidate Nodes

- tense_aspect_value
- temporal_anchor_expression
- temporal_anchor_fit
- narrative_perspective_frame
- constructional_frame_fit
- community_licensing
- semantic_pragmatic_recoverability
- reported_acceptability
- grammaticality_attribution

## Potential Construct Pressure

This card requires temporal-anchor machinery to include viewpoint or narrative perspective. A
tense/aspect graph that handles present perfect plus `yesterday` but cannot handle narrative present
has overfit the perfect-tense cards.

## Graph Failure Modes

- Treats all present forms with past-time expressions as unlicensed.
- Treats narrative vividness as mere semantic recoverability.
- Treats the past-time expression as payload with no effect on tense/aspect fit.
- Ignores the difference between event time and narrative viewpoint.

## Predicted Discriminators

- `TEMP` should survive only if it includes a narrative perspective frame or equivalent viewpoint
  construct.
- `FRAME` may partly survive as broad frame fit, but without a temporal-viewpoint construct it will
  only annotate the contrast.
- `PROC` should not explain the contrast as processing difficulty.
