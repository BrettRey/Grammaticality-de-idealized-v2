# Phenomenon Card: depth-charge semantic illusion

**Stress test:** Plausible global interpretation despite incoherent literal composition.

## Description

Depth-charge sentences and related semantic illusions can feel meaningful even when their literal
composition is incoherent or contradictory. The reader supplies a plausible intended meaning or
nearby semantic repair, sometimes without noticing that the literal interpretation is defective.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`
- Related cards: [noisy-channel-overacceptance-gibson](noisy-channel-overacceptance-gibson.md),
  [comparative-illusion-noisy-channel-gibson](comparative-illusion-noisy-channel-gibson.md)

## Why It Matters

This card is a harder test for repair-neighbour modelling than missing-material cases. The issue is
not only edit distance to an intended string, but also the plausibility and availability of a
nearby intended meaning. A graph that has only syntactic repair distance may overfit missing-word
cases and fail semantic illusions.

## Minimum Contrast Cells

- depth-charge item with plausible global interpretation;
- literal-composition task that exposes the incoherence;
- semantically matched control without the illusion;
- context manipulation that makes the intended repair more or less plausible.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive` section 2.2.10 and chapter 10. The source groups
depth-charge materials with noisy-channel and good-enough interpretation cases where readers infer
an intended meaning that differs from the literal composition.

## Candidate Nodes

- repair_neighbour_distance
- semantic_pragmatic_recoverability
- felt_naturalness_context
- reported_acceptability
- task_framing
- grammaticality_attribution

## Graph Failure Modes

- Treats semantic illusion as grammatical licensing.
- Treats all repair-neighbour effects as surface edit-distance effects.
- Ignores meaning-prior or plausibility pressure.
- Fails to predict a task shift under literal-composition framing.

## Predicted Discriminators

- `RNR` should partly survive by separating reconstruction from licensing.
- A future graph may need a meaning-prior or intended-meaning-plausibility node.
- `PROC` should partly survive on felt naturalness and reported acceptability, but not on the
  neighbour-selection mechanism.
