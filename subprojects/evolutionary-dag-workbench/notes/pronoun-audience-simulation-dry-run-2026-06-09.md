# Pronoun Audience-Reference Simulation Dry Run

**Date:** 2026-06-09
**Target lane:** `data/audience-reference-projection/`
**Status:** Simulation-only dry run added; no evidence-status change.

## Purpose

The audience/reference lane now has enough machinery to accept response rows. This pass exercises
that machinery with deterministic simulation-only rows so the pipeline can be checked before any
participant, corpus, or independent critic data are used.

## Added Tool And Artifacts

- `scripts/simulate_audience_reference_responses.py`
- `data/audience-reference-projection/simulations/structured-critic-simulation-2026-06-09.csv`
- `data/audience-reference-projection/simulations/structured-critic-simulation-2026-06-09-summary.md`

Every generated row is marked:

```text
counts_as_prediction_evidence=no
```

The generated CSV validates under `--require-responses`. The summary is produced with
`--include-non-evidence`, so it reports the simulated channel pattern without making the rows
evidence-usable.

The fixture runner checks that the simulation validates, that the default summary excludes its
non-evidence rows, and that `--include-non-evidence` includes all 66 rows for pipeline QA.

## Design Correction

The dry run exposed that `cell_id` alone is too coarse for prediction summaries: several predictions
share the same broad cell. `prediction-register.csv` now includes `item_ids`, and the summarizer
uses those item sets when grouping response rows under each prediction.

## Decision

No graph mutation.

No score movement.

No evidence label changes. The simulation is a pipeline check, not a source of empirical evidence.
