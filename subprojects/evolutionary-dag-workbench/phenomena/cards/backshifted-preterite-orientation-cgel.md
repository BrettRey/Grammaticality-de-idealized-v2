# Phenomenon Card: backshifted preterite orientation

**Stress test:** Preterite form, matrix-oriented time, and non-deictic temporal orientation.

## Description

CGEL distinguishes ordinary preterite from backshifted preterite. In a report such as:

- original present: `I have too many commitments`;
- backshifted report: `Jill said she had too many commitments`;
- ordinary preterite: `She had too many commitments`;

the preterite form in the reported clause is not simply locating the situation before the current
deictic time. It is oriented to the matrix clause or reporting frame. CGEL also gives cases where
the matrix preterite is modal rather than temporal:

- `If he knew she had too many commitments, he would do something about it`;
- `I wish he realised that she had too many commitments`.

In these examples, the subordinate `had` can describe a present situation. It is backshifted, not
ordinary past time and not modal remoteness.

## Source Pointers

- Source IDs: `cgel-past-tense-uses`
- Local source: `/Users/brettreynolds/Documents/CGEL/out/028_6 Further uses of the past tenses 148.pdf`
- Related cards: [modal-preterite-remoteness-cgel](modal-preterite-remoteness-cgel.md),
  [modal-perfect-by-now-inference](modal-perfect-by-now-inference.md)

## Held-Out Status

This card was not used to build `temporal-anchor-alignment-candidate`. It is a second held-out
temporal/modal pressure test after `modal-preterite-remoteness-cgel`.

## Why It Matters

The card prevents the graph from repairing modal preterites with a narrow modal-remoteness node
only. Backshift shows a broader problem: tense/aspect form needs an orientation frame specifying
where the relevant time of orientation comes from.

## Minimum Contrast Cells

- ordinary preterite with deictic past-time orientation;
- reported present backshifted under a past reporting frame;
- backshift under a modally remote matrix clause with present situation time;
- non-backshifted present in a direct or current report;
- original preterite backshifted as preterite perfect.

## Candidate Nodes

- tense_aspect_value
- temporal_anchor_expression
- temporal_anchor_fit
- constructional_frame_fit
- semantic_pragmatic_recoverability
- community_licensing
- reported_acceptability
- grammaticality_attribution

## Potential Construct Pressure

This card suggests a broader temporal-orientation construct rather than a modal-remoteness-only
repair. The graph needs to represent whether tense/aspect form is interpreted deictically, by a
matrix/reporting frame, or by a modal-remote frame.

## Graph Failure Modes

- Treats every preterite form as deictic past time.
- Treats backshift as modal remoteness.
- Treats backshift as mere indirect-speech paraphrase with no tense/aspect licensing consequence.
- Collapses ordinary preterite and backshifted preterite because they can produce the same surface
  time relation in ordinary reports.
- Treats recoverability of the reported proposition as licensing the backshift pattern.

## Predicted Discriminators

- `TEMP` should partly survive by separating tense/aspect value from event time, but it should expose
  a missing temporal-orientation frame.
- `FRAME` may partly survive as broad reporting-frame fit.
- `PROC` should not explain the contrast as processing difficulty.
