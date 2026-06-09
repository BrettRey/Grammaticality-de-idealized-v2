# Phenomenon Card: noisy-channel overacceptance

**Stress test:** Illusion of grammaticality and rational reconstruction.

## Description

Some strings with local errors, missing material, or incoherent literal meanings are judged better
than their formal status would predict because comprehenders infer a nearby intended sentence.
Examples include missing-verb materials, duplicated or missing determiners, depth-charge sentences,
and comparative illusions.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`
- Related cards: [comparative-more-less-category](comparative-more-less-category.md),
  [grammatical-but-hard](grammatical-but-hard.md)

## Why It Matters

The case tests the opposite side of garden paths: acceptability can be too high, not too low. A
graph that treats reported acceptability as licensing will falsely promote strings whose apparent
goodness comes from noisy-channel repair.

## Minimum Contrast Cells

- formally intact baseline;
- one-error or missing-material string with a close intended repair;
- equally unlicensed string without a plausible nearby repair;
- long versus short strings with the same number of errors.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive` sections 2.1.3, 2.2.10, and 10.4-10.5. The source supports
the claim that acceptability can rise when a problematic string has a highly recoverable intended
neighbour, especially in longer or more complex materials.

## Candidate Nodes

- semantic_pragmatic_recoverability
- reported_acceptability
- grammaticality_attribution
- processing_cost
- measurement_task
- repair_reformulation_pressure

## Potential Construct Pressure

Repeated use of this card may require a node for distance to a recoverable intended form, rather
than routing all noisy-channel effects through `semantic_pragmatic_recoverability`.

## Graph Failure Modes

- Treats high acceptability as evidence for community licensing.
- Fails to model correction-to-nearest-neighbour effects.
- Treats all unlicensed strings as equally unacceptable.
- Ignores sentence length and task timing in acceptability.

## Predicted Discriminators

- `PROC` should survive if it can represent high reported acceptability despite low licensing.
- `CAT` is relevant for comparative illusions only when the error changes category attribution.
- `DYN` and `OPG` should not promote the string merely because the reported judgment is high.
