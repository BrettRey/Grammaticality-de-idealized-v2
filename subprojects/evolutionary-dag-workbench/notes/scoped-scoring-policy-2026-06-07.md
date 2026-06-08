# Scoped Scoring Policy

**Date:** 2026-06-07

## Purpose

The workbench now has scoped modules that survive some protocol-bound tests without being general
accounts of grammaticality. Scores must make that scope visible.

## Score Kinds

`unscored`

Use when a graph has not earned any non-zero score. This is the default when `score_status` is absent.

`scoped_module`

Use when a graph has earned a non-zero score only relative to a declared module scope, such as
dynamic/context feedback or operator-gap analysis.

`general_account`

Use only when a graph is being scored as a general account across the workbench's phenomenon space.
No graph currently qualifies.

## Rule

Any graph with a non-zero `scores` block must include:

- `score_status.kind`
- `score_status.evaluation`

`score_status.kind` must be `scoped_module` or `general_account`, and `score_status.evaluation` must
point to an existing protocol-bound evaluation or equivalent review file.

Seed graphs remain all-zero regardless of score status.

## Current Decision

The current pass permits conservative `scoped_module` scores for:

- `context-indexed-dynamic-feedback-candidate`
- `context-aware-operator-gap-candidate`

No graph receives a `general_account` score.
