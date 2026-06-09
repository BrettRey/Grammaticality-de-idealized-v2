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

## Running the registered query plan

Use the repository runner to expand `query-plan.csv` into auditable calls to the shared
English-Corpora.org wrapper:

```bash
python3 scripts/run_agr_coca_queries.py
```

That prints the planned commands without running them. To write a command manifest:

```bash
python3 scripts/run_agr_coca_queries.py --manifest data/agr-coca-projection/query-manifest.csv
```

To execute live COCA queries after the wrapper session is authenticated:

```bash
python3 scripts/run_agr_coca_queries.py --run
```

The runner checks wrapper authentication before live execution and stops rather than producing
partial data from an expired session.

Do not treat raw COCA frequency as licensing. The lane measures production/attestation over
opportunity sets and uses KWIC filtering to distinguish genuine agreement realizations from query
noise.
