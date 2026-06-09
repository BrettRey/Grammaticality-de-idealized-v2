# Pronoun Audience-Reference Response Fixtures

**Date:** 2026-06-09
**Target lane:** `data/audience-reference-projection/`
**Status:** Fixture coverage added; no evidence-status change.

## Purpose

The response validator now gates future audience/reference pilot or critic response files. This
pass adds fixture coverage so the validator is itself checked by `scripts/run_fixture_tests.py`.

## Added Checks

The fixture runner now checks that:

- the empty pilot response template validates;
- collected-response mode rejects empty `raw_response` cells;
- a deliberately bad response fixture catches 1-7 scale violations;
- the same fixture catches drift from registered stimulus metadata.

## Decision

No graph mutation.

No score movement.

No evidence label changes. The fixtures test the gate; they do not supply response data.
