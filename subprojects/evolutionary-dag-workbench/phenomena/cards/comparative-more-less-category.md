# Phenomenon Card: comparative more/less category pressure

**Stress test:** Category analysis vs grammatical licensing.

## Description

Comparative `more` and `less` create an analysis-sensitive case where category labels, syntactic
function, and licensing can be pulled apart. The important workbench question is not whether a
particular category analysis is right, but whether a graph mistakes analyst classification for a
speaker-facing grammaticality construct.

## Source Pointers

- Source IDs: `cgel-comparison`, `reynolds-more-less`

## Why It Matters

This card is a guard against category-label leakage. A graph can use category analysis as
evidence, but it should not turn "CGEL calls this X" or "a correction paper argues for Y" into a
licensed/unlicensed state by fiat.

## Minimum Contrast Cells

- comparative use in a scalar modifier environment;
- comparative use in a determiner-like nominal environment;
- metalinguistic category judgment by an analyst;
- ordinary speaker acceptability or production judgment with no category terminology.

## Candidate Nodes

- measurement_task
- task_framing
- constructional_analogy
- grammaticality_attribution
- reported_acceptability
- semantic_pragmatic_recoverability

## Graph Failure Modes

- Treats analyst category assignment as grammaticality attribution.
- Treats distributional category evidence as direct community licensing.
- Ignores task framing when respondents are asked to classify, not judge acceptability.
- Conflates syntactic function with lexical category.

## Predicted Discriminators

- A measurement-aware graph should predict different outputs for category tasks and acceptability
  tasks.
- A discovery-first graph should be allowed to revise category nodes only when contrast cells force
  that distinction.
