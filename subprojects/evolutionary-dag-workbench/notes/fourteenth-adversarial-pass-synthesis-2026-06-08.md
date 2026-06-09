# Fourteenth Adversarial Pass Synthesis

**Date:** 2026-06-08
**Trigger:** Run the workbench harder after all cards had at least one protocol-test evaluation.

## Result

Add a machine-readable `prediction_tests` layer.

The workbench already had activated paths and computed path readings, but those were still mostly
scaffolding. This pass adds explicit contrast-level prediction tests with pass/fail conditions and
an evidence status. Score-changing evaluations now require prediction tests, so numeric score
movement cannot rest on path existence alone.

## What Changed

- `evaluations/SCHEMA.md` now documents `prediction_tests`.
- `scripts/validate_evaluation.py` validates prediction tests.
- `scripts/summarize_evaluations.py` reports prediction-test counts and evidence status.
- Fixture tests now cover valid score-change prediction tests, unresolved prediction-test path
  references, and score-change evaluations that lack prediction tests.
- The two held-out CGEL evaluations now contain pre-registered prediction tests with
  `evidence_status: not-run`.

## Why This Matters

This is the first layer that makes projectibility operational rather than merely named. A held-out
evaluation can now say:

- which contrast cell is being predicted;
- which activated path or paths support the prediction;
- what would count as a pass;
- what would count as a failure;
- whether evidence has actually been checked.

That still does not make the workbench empirical. It does make the next empirical or source-backed
pass auditable.

## Boundary

All numeric scores remain zero. `prediction_tests` are commitments, not results. Evidence status
stays `not-run` until cards are enriched with examples, source pointers, or data checks.
