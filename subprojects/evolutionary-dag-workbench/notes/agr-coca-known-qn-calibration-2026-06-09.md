# AGR COCA Known-QN Calibration Pass

**Date:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Tranche:** `known-qn-calibration`

## Question

Can the COCA/KWIC workflow reproduce known agreement directions for central
number-transparent QN cases while also catching predictable direct-query false positives?

This is a method-calibration tranche, not a projection tranche. It should increase confidence that
the row-coding protocol can distinguish target agreement rows from query noise, but it does not
authorize score movement.

## Retrieval

Raw list queries were run for:

- `a number of people are`
- `a number of people were`
- `a lot of money is`
- `a lot of money are`

All four non-zero cells were KWIC-filtered with `scripts/fetch_coca_kwic_from_list.mjs`, using the
same list-result-click route as the earlier `AGR` COCA tranches.

COCA returned intermittent server-error pages on the `a lot of money` cells. Retrying after a
longer delay succeeded. The saved KWIC frames expose the full raw-list row counts, though the header
line reports the number of texts for some cells rather than the raw list count.

## Results

Raw list counts:

| query | raw count |
|---|---:|
| `a number of people are` | 52 |
| `a number of people were` | 48 |
| `a lot of money is` | 60 |
| `a lot of money are` | 12 |

KWIC-filtered target counts:

| calibration cell | filtered target rows |
|---|---:|
| `a number of people` + plural agreement | 98 |
| `a lot of money` + singular agreement | 42 |
| `a lot of money` + plural agreement | 0 |

The `a number of people` cells had two grammar-instruction/metalinguistic rows, both excluded from
production evidence.

The `a lot of money is` cell had 18 non-subject false positives, mostly gerund, infinitival, object,
PP-contained, or larger-subject configurations where `is` was not agreement with `a lot of money`.

The `a lot of money are` cell had:

- 9 parse-shift rows where the agreement controller was `people` or another higher controller;
- 2 non-subject rows where the query string was inside an object or larger subject;
- 1 apparent target-frame nonstandard/error row, retained as denominator-only evidence.

The row-level coding is in `data/agr-coca-projection/coded/known-qn-kwic-coding.csv`.

## Interpretation

The calibration pass supports the measurement workflow. It reproduces the expected contrast between
plural agreement with `a number of people` and singular agreement with `a lot of money`, while
showing why raw direct-query counts cannot be used without KWIC filtering.

The most important practical lesson is that counter-direction raw hits are not automatically
counterevidence. In this tranche, `a lot of money are` has 12 raw hits but no licensed plural target
rows after filtering. That validates the current row-coding distinction among target agreement,
parse-shift noise, non-subject noise, metalinguistic examples, and denominator-only nonstandard
errors.

No score movement follows. This tranche calibrates the COCA data lane; it does not add a held-out
projection result for `AGR`.
