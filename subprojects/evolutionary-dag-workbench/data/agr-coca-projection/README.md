# AGR COCA Projection Data Lane

**Created:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`

This directory is reserved for a confirmatory COCA run testing the `AGR` module.

## Files

- `prediction-register.csv`: pre-run predictions and pass/fail thresholds.
- `query-plan.csv`: query cells, denominators, and expected patterns.
- `kwic-coding-schema.csv`: row-level labels for raw KWIC filtering.
- `summary.csv`: raw and filtered summaries as they accumulate.
- `coded/bunch-animate-kwic-coding.csv`: row-level coding for the animate `bunch` tranche.
- `coded/bunch-inanimate-kwic-coding.csv`: row-level coding for the inanimate `bunch` tranche.
- `coded/majority-minority-kwic-coding.csv`: row-level coding for the majority/minority tranche.
- `coded/known-qn-kwic-coding.csv`: row-level coding for the known number-transparent QN
  calibration tranche.

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
python3 scripts/run_agr_coca_queries.py --cell bunch-animate-confirmatory --run --type list
```

The runner defaults to a delay between searches to respect English-Corpora.org's rate limit. Use
`--preflight-status` only when the wrapper's status probe is known to match the current site state;
otherwise `ecorg query` will use configured private credentials and fail if authentication is not
available.

Current completed tranche:

- `bunch-animate-confirmatory`, list-result counts plus KWIC filtering via result-row clicks.
- `bunch-inanimate-confirmatory`, list-result counts plus KWIC filtering via result-row clicks.
- `majority-minority-confirmatory`, list-result counts plus KWIC filtering via result-row clicks.
- `known-qn-calibration`, list-result counts plus KWIC filtering via result-row clicks.
- `partitive-calibration`, raw phrase-count denominator probe only.
- `partitive-agreement-followup`, raw finite-agreement list counts only.

The filtered target counts for the animate tranche are 71 plural agreement rows and 1 singular
agreement row across `a bunch of people/kids` with `are/were/is/was`. Five of six raw singular
hits were non-subject false positives.

The filtered target counts for the inanimate tranche are 1 plural agreement row and 1 singular
agreement row across `a bunch of flowers/things` with `are/were/is/was`. The inanimate cells are
sparse rather than plural-dominant, which is useful as a contrast with the animate tranche but not
by itself a general agreement result.

The filtered target counts for the majority/minority tranche are 105 plural agreement rows and 0
singular agreement rows across `a/the majority of people` and `a minority of voters`. The
`minority` query pair returned zero raw rows; the positive evidence comes from `majority`.

The known-QN calibration tranche reproduces expected directions after KWIC filtering: `a number of
people` yields 98 filtered plural target rows across `are/were` after excluding two grammar-example
rows, while `a lot of money is` yields 42 filtered singular target rows and `a lot of money are`
yields 0 licensed plural target rows. One `a lot of money are` row was retained as
denominator-only nonstandard/error evidence, not as licensed plural agreement.

The partitive calibration tranche is raw phrase-count only. It confirms that `lots of people` and
`plenty of people` are high-frequency bare/non-partitive frames, `lots/plenty of the people` are
rare as direct strings, and `the rest of the people` greatly outnumbers `the rest of people`. It
does not code agreement because the registered strings do not include finite verbs.

The partitive agreement follow-up adds present-tense finite agreement strings for the usable people
frames. Raw counts are plural-dominant (`lots/plenty/rest of people are` totals 367) with only one
non-zero singular counter-cell (`lots of people is`, 5). These are raw list counts only; the small
counter-cell and moderate positive cells need KWIC filtering before target-row claims.

Do not treat raw COCA frequency as licensing. The lane measures production/attestation over
opportunity sets and uses KWIC filtering to distinguish genuine agreement realizations from query
noise.
