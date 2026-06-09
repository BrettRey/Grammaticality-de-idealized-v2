# Critic Verdict Variance Protocol

**Date:** 2026-06-09
**Status:** Variance harness for LLM critic passes; no score movement.

## Purpose

This protocol tests whether graph-survival verdicts are stable under repeated independent critique.
It addresses a specific failure mode: an evaluation can look disciplined while the survival label is
really just one critic run's judgment.

The protocol does not make LLMs scholarly adjudicators. It treats them as noisy critics whose
variance must be logged before their verdicts can be trusted as pressure on the graph ecology.

## Unit

One variance check targets one existing evaluation JSON.

The packet must include:

- the target evaluation;
- the target graph;
- the phenomenon cards referenced by the evaluation;
- any data notes needed to interpret evidence statuses;
- an explicit JSON response shape.

## Run Rule

Run at least three independent critic passes before drawing a variance conclusion.

Allowed independence sources:

- different models;
- same model in fresh non-resumed sessions;
- different critic stances declared in the run metadata;
- separate external evaluators.

Do not count an assistant's own prose summary as an independent run unless it is recorded as such
and marked `self_generated`.

## Logged Fields

Each critic output should record:

- `critic_id`;
- `target_evaluation`;
- `overall_score_decision`;
- `overall_stability`;
- per-prediction-test `evidence_status`;
- per-card `result`;
- `strongest_instability`;
- `score_movement_allowed`;
- `minimal_change`.

## Interpretation

A verdict is stable only if:

- all or nearly all critics preserve the same card result labels;
- prediction-test evidence statuses do not flip between `passed` and `failed`;
- disagreement is localized to `mixed`, `inconclusive`, or boundary cells;
- no critic identifies a missing construct that would invalidate the evaluation's required paths.

A single variance check is not projective evidence. It is an uncertainty audit over the workbench's
internal evaluation layer.

## First Registered Target

The first packet targets:

`evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`

This is a deliberately conservative first target because it has a concrete data trail and should be
more stable than a purely conceptual survival label. If it shows high variance, the evaluation layer
is noisier than expected.
