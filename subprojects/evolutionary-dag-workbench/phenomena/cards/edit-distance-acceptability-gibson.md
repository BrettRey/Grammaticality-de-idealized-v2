# Phenomenon Card: edit-distance and sentence-length acceptability

**Stress test:** Repair distance must be normalized by target information or length.

## Description

Noisy-channel acceptability is not determined only by whether a string is defective. Acceptability
varies with the distance from the presented string to a plausible intended sentence and with how
much material the intended sentence contains. A small number of edits can be tolerated more readily
in longer, information-rich sentences than in short ones.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`
- Related cards: [noisy-channel-overacceptance-gibson](noisy-channel-overacceptance-gibson.md),
  [missing-verb-phrase-illusion-gibson](missing-verb-phrase-illusion-gibson.md)

## Why It Matters

This card tests whether `repair_neighbour_distance` is enough. If distance is not normalized by the
size or information content of the intended sentence, the graph will mispredict cases where the same
number of edits has different acceptability effects at different lengths.

## Minimum Contrast Cells

- intact sentences of different lengths;
- one- or two-edit strings at short, medium, and long lengths;
- high-edit strings with no plausible close repair;
- rating task separated from literal grammaticality or proofreading task.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive` section 10.4. The source describes a rational-inference
model in which acceptability depends on the intended sentence and the number of errors normalized by
sentence length or information amount, and reports cross-language patterns consistent with that
approach.

## Candidate Nodes

- repair_neighbour_distance
- semantic_pragmatic_recoverability
- reported_acceptability
- felt_naturalness_context
- measurement_task
- grammaticality_attribution

## Graph Failure Modes

- Treats edit count as sufficient without target length or information mass.
- Treats all one-error strings as equally acceptable.
- Promotes high acceptability to licensing.
- Fails to separate rating tasks from literal grammaticality attribution.

## Predicted Discriminators

- `RNR` should partly survive but should be pressured toward a length- or information-normalized
  repair-distance construct.
- `PROC` should partly survive on naturalness and reported acceptability, but not on the
  distance-normalization mechanism.
