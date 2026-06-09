# Phenomenon Card: comparative illusion as noisy-channel repair

**Stress test:** Category-sensitive illusion with a plausible intended comparative.

## Description

Comparative illusions can receive surprisingly high acceptability because readers infer a plausible
intended comparative relation even when the literal string does not compose correctly. The case sits
between noisy-channel reconstruction and category/function analysis.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`, `reynolds-more-less`
- Related cards: [comparative-more-less-category](comparative-more-less-category.md),
  [noisy-channel-overacceptance-gibson](noisy-channel-overacceptance-gibson.md)

## Why It Matters

The card tests whether repair-neighbour distance and category-measurement discipline stay
separable. A graph should not use the fact that a plausible comparative was intended to settle the
literal string's category or licensing status.

## Minimum Contrast Cells

- comparative illusion with a plausible intended relation;
- literal category/function analysis of the presented string;
- repaired comparative paraphrase;
- ordinary comparative construction with no illusion.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive` section 2.2.10 and Brett's `more`/`less` correction paper.
Gibson treats comparative illusions as noisy-channel cases; the correction work makes them useful
for testing category-analysis leakage.

## Candidate Nodes

- repair_neighbour_distance
- semantic_pragmatic_recoverability
- analyst_category_assignment
- measurement_task
- reported_acceptability
- grammaticality_attribution

## Graph Failure Modes

- Treats the repaired comparative interpretation as literal-string licensing.
- Treats analyst category assignment as grammaticality attribution.
- Routes high acceptability directly into community licensing.
- Ignores the difference between category-analysis and first-pass interpretation tasks.

## Predicted Discriminators

- `RNR` should partly survive by modelling the repair-neighbour channel.
- `CAT` should be needed when the task is category/function analysis.
- A graph that conflates acceptability, category, and licensing should fail.
