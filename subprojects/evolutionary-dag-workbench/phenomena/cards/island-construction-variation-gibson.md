# Phenomenon Card: island construction variation

**Stress test:** Island effects that vary by construction and discourse role.

## Description

Some long-distance dependencies are unacceptable in one construction but much better in another.
Gibson's discussion of subject islands contrasts wh-question extractions with relative-clause
extractions and treats construction meaning and discourse function as central to the pattern.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`
- Related cards: [unbounded-dependency-licensing-cgel](unbounded-dependency-licensing-cgel.md),
  [left-branch-extraction](left-branch-extraction.md)

## Why It Matters

The case prevents an operator-gap graph from treating all island effects as one uniform syntactic
ban. It forces a representation of construction-specific dependency licensing, discourse function,
and controlled comparison against non-extraction baselines.

## Minimum Contrast Cells

- wh-question extraction from a subject versus object configuration;
- relative-clause extraction from a comparable subject versus object configuration;
- no-extraction controls for each construction;
- exclamative or other construction with a different locality or discourse profile.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive` section 8.4. The source argues that island acceptability
varies across constructions and that a two-by-two interaction is needed before calling a contrast an
island effect.

## Candidate Nodes

- operator_value
- update_role_configuration
- argument_linking_selection
- semantic_pragmatic_recoverability
- opportunity_mass
- competitor_availability
- preemption_strength
- community_licensing
- reported_acceptability
- measurement_task

## Potential Construct Pressure

This card may require a construction-specific dependency-licensing construct if `operator_value` and
`argument_linking_selection` remain too coarse.

## Graph Failure Modes

- Treats all extraction failures as one island mechanism.
- Ignores construction type, discourse role, or no-extraction controls.
- Treats a main effect of construction difficulty as an island interaction.
- Equates recoverability with licensing.

## Predicted Discriminators

- `OPG` should partly survive only if it can index opportunity and preemption to the construction.
- `UPT` may be needed where construction-specific update role explains the contrast.
- `PROC` should not be allowed to explain the island pattern only with raw difficulty.
