# Fourth Adversarial Pass Synthesis

**Date:** 2026-06-07
**Inputs:** dynamic stratified feedback candidate, fourth critique, regional/register phenomenon cards

## Summary

The dynamic candidate fixes one failure of the stratified candidate: it represents feedback legally
with time-sliced nodes and `time_lagged` edges. But it exposes the next failure. A time-indexed graph
can still be context-blind.

The strongest remaining problem is not acyclicity, and not even time. It is conditioning. A graph
must say which community, norm centre, genre, medium, task frame, and speaker cue its claims are
conditioned on.

## What Survived

### 1. Time Indexing Is Necessary

The dynamic candidate should remain in the archive. It gives the workbench a valid pattern for
feedback:

- production at one slice influences later usage;
- usage and opportunity inform later licensing;
- licensing, correction, entrenchment, and acceptability influence later production;
- usage, licensing, and correction contribute to later stabilization.

This is the right direction for diachronic phenomena.

### 2. Time Indexing Is Not Context Indexing

`needs washed`, stigmatized robust vernaculars, and register-bound fragments are not solved by a
single timeline. They require parallel or contrastive conditioning:

- regional community vs standard norm centre;
- local speech vs edited prose;
- naturalness task vs correctness task;
- speaker identified as in-group vs out-group;
- genre where a fragment is ordinary vs genre where it is marked.

The next representation should therefore make conditioning metadata explicit.

### 3. The JSON Format Can Carry More Than Edges

The user's earlier point still matters: this workbench is not limited to bare DAGs. The next
candidate can remain valid graph JSON while adding explicit conditioning metadata. That metadata
should not be treated as prose decoration; it should be a first-class part of the representation.

The current linter will not enforce that metadata yet. That is acceptable for this candidate, but it
creates a tooling task for a later pass.

## Representation Decision

Create:

`context-indexed-dynamic-feedback-candidate`

It should preserve the dynamic feedback skeleton while adding:

- `speaker_identity_t1`
- `social_indexical_value_t1`
- `genre_t1`
- `medium_t1`
- `register_genre_appropriateness_t1`
- `task_framing_t1`

It should also include top-level conditioning metadata that states which axes must be specified
before the graph is interpreted.

## Score Discipline

No existing scores should change. The dynamic candidate is useful but still too coarse. The new
context-indexed candidate should start with all-zero scores and receive no promotion until it is
attacked for overconditioning, complexity, and metadata/tooling drift.

## Next Action

Create `graphs/archive/context-indexed-dynamic-feedback-candidate.json`.

After that, the natural infrastructure task is to teach the linter to recognize and check
conditioning metadata. Otherwise the workbench will again rely on social discipline for one of its
central commitments.
