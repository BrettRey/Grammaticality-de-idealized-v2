# Fifth Adversarial Pass Synthesis

**Date:** 2026-06-07
**Inputs:** context-indexed dynamic feedback candidate, fifth critique, conditioning protocol

## Summary

The context-indexed dynamic candidate fixes the fourth-pass failure by making conditioning axes
explicit. But it creates the next methodological risk: overconditioning.

The workbench now needs to distinguish principled context specification from post hoc rescue.
That requires a protocol and a stricter linter, not another larger graph.

## What Survived

### 1. Context Indexing Is Necessary

The workbench should keep `conditioning_axes`. Cases like `needs washed`, stigmatized robust
vernaculars, register-bound fragments, and `between you and I` cannot be handled by a single
unconditioned community or judgment setting.

### 2. Context Indexing Is Not a License to Split Freely

Every conditioning axis creates a possible rescue move. The workbench must therefore require:

- pre-specified axes;
- contrast cells defined before interpretation;
- exploratory labels for newly discovered splits;
- explicit scope limits when a graph lacks the relevant module.

### 3. The Current Linter Is Halfway There

The linter now recognizes `conditioning_axes`, but it does not yet verify that an axis has a
corresponding node in the graph. That means a graph could declare `speaker_identity` as an axis while
containing no `speaker_identity` or `social_indexical_value` node.

This is exactly the kind of construct hygiene gap the project exists to close.

## Representation Decision

No new graph candidate yet.

The next natural move is tooling:

- document the conditioning operationalization protocol;
- make `scripts/lint_graph.py` check declared axes against corresponding graph nodes.

## Score Discipline

No candidate receives a non-zero score after this pass. The strongest current module is
`context-indexed-dynamic-feedback-candidate`, but it has not survived a protocol-bound test or an
operator-gap reintegration pass.
