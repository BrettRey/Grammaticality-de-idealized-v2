# AGR COCA Projection Data Lane

**Created:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`

This directory is reserved for a confirmatory COCA run testing the `AGR` module.

## Files

- `prediction-register.csv`: pre-run predictions and pass/fail thresholds.
- `query-plan.csv`: query cells, denominators, and expected patterns.
- `kwic-coding-schema.csv`: row-level labels for raw KWIC filtering.

Future run artifacts should use:

- `raw/` for raw COCA exports or pasted KWIC batches;
- `coded/` for row-level coded data;
- `summary.csv` for raw counts, filtered counts, denominators, intervals, and evidence statuses.

Do not treat raw COCA frequency as licensing. The lane measures production/attestation over
opportunity sets and uses KWIC filtering to distinguish genuine agreement realizations from query
noise.
