# Scoped Scoring Policy

**Date:** 2026-06-07

## Purpose

The workbench now has scoped modules that survive some protocol-bound tests without being general
accounts of grammaticality. Scores must make that scope visible.

## Score Kinds

`unscored`

Use when a graph has not earned any non-zero score. This is the default when `score_status` is absent.

`scoped_module`

Use when a graph has survived a protocol-bound evaluation only relative to a declared module scope,
such as dynamic/context feedback or operator-gap analysis.

`general_account`

Use only when a graph is being scored as a general account across the workbench's phenomenon space.
No graph currently qualifies.

## Rule

Any graph with a `scoped_module` or `general_account` label should include:

- `score_status.kind`
- `score_status.evaluation`

`score_status.evaluation` must point to an existing protocol-bound evaluation whose `target_graph`
matches the graph being labelled.

Any graph with a non-zero `scores` block must include `score_status.kind` as `scoped_module` or
`general_account`, and the evaluation target must match. Non-zero numeric scores should wait for a
held-out or parameterized test.

Seed graphs remain all-zero regardless of score status.

## Current Decision

The current pass permits `scoped_module` labels for:

- `context-indexed-dynamic-feedback-candidate`
- `context-aware-operator-gap-candidate`

Their numeric scores remain zero. No graph receives a `general_account` score.
