# Sixth Adversarial Pass Synthesis

**Date:** 2026-06-07
**Input:** external model evaluation of the packaged workbench

## Summary

The external evaluation confirmed that the shipped gates pass, then found three enforcement gaps
where the prose commitments were stronger than the tools:

1. `time_lagged` edges did not check forward time direction.
2. `conditioning_axes` required corresponding nodes but not directed edge paths.
3. `score_status.evaluation` checked file existence but not whether the evaluation targeted the
   graph being scored.

All three are valid critiques. They are implementation gaps, not conceptual objections, and the
right response is mechanical enforcement.

## Accepted Tooling Fixes

### 1. Time-Lag Direction

`time_lagged` edges should require both endpoints to be time-sliced and should require the target
slice to be later than the source slice. A backward edge such as `production_probability_t2 ->
opportunity_mass_t1` must fail.

### 2. Conditioning Axis Substance

A declared conditioning axis should not pass merely because its corresponding node exists. At least
one corresponding node must have a directed path to an outcome-like node. This prevents vestigial
metadata from satisfying the linter.

### 3. Evaluation Target Matching

`score_status.evaluation` must point to a JSON evaluation whose `target_graph` resolves to the graph
that cites it. Existence is not enough.

## Scoring Reassessment

The deeper critique is also accepted: the current graphs are unparameterized. Edges have type and
prose rationale, but no sign, magnitude, threshold, or functional form. Therefore numeric scores are
not measurements. They are hand-entered judgments linked to written reasoning.

The workbench should keep scoped-module labels and evaluation links, but it should not present
non-zero numeric scores as earned until there is at least one of:

- held-out protocol evaluation;
- parameterized edge semantics;
- empirical elicitation or corpus evidence;
- mechanized dimensions, such as computed complexity.

Current response: reset numeric scores to zero while retaining `scoped_module` labels for the two
modules that have exploratory protocol evaluations.

## Projectibility Gap

The evaluation also identified a framework-level gap: the current rubric emphasizes maintenance of
construct distinctions more than projectibility. Coverage over cards used to build the graphs is not
the same as predicting held-out contrasts.

This is a real next-stage requirement. Before any numeric score movement, the workbench should add
held-out protocol evaluations and a rubric/policy hook for projectibility.

## Next Action

Patch the three enforcement gaps, add negative fixtures for them, keep all numeric scores zero, and
move the next methodological task to held-out/projectibility evaluation.
