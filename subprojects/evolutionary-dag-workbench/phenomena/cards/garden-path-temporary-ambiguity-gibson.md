# Phenomenon Card: garden-path temporary ambiguity

**Stress test:** Illusion of ungrammaticality under strong temporary ambiguity.

## Description

Garden-path sentences can be grammatical while sounding unacceptable because an early, locally
preferred parse becomes incompatible with later material. The felt failure comes from reanalysis and
confusion, not from a missing licensed form-value relation.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`
- Related cards: [grammatical-but-hard](grammatical-but-hard.md),
  [agreement-attraction](agreement-attraction.md)

## Why It Matters

The case tests whether a graph keeps detector output separate from the target construct. Low
acceptability and high confusion can arise when the parser commits to a locally attractive
interpretation even though the final structure is licensed.

## Minimum Contrast Cells

- locally biased continuation that confirms the initial parse;
- garden-path continuation requiring reanalysis;
- disambiguated version with the same final dependency pattern;
- judgment task after first reading versus after explanation or rereading.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive` section 2.2.9. The source treats these as grammatical
sentences whose acceptability is depressed by temporary ambiguity and parser commitments.

## Candidate Nodes

- processing_cost
- reported_acceptability
- felt_naturalness_context
- measurement_task
- semantic_pragmatic_recoverability
- grammaticality_attribution

## Graph Failure Modes

- Treats the initial feeling of failure as evidence of non-licensing.
- Fails to distinguish first-pass detector response from post-reanalysis attribution.
- Collapses temporary ambiguity into semantic-pragmatic incoherence.
- Predicts stable rejection even after disambiguation or explanation.

## Predicted Discriminators

- `PROC` should survive by routing the effect through processing cost, recoverability, task, and
  attribution.
- `OPG` should fail if it explains garden-path rejection as an operator gap.
- `TASK` may partly survive only where the task timing or explanation changes the judgment.
