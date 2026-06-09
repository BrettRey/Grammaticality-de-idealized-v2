# AGR COCA Partitive Agreement Targeted KWIC Pass

**Date:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Tranche:** `partitive-agreement-followup`
**Status:** Targeted KWIC filtering for selected non-zero cells; `lots of people are` remains
raw-unfiltered; no score movement.

## Question

Do the informative smaller cells from the partitive agreement follow-up survive KWIC filtering?

This pass targets:

- the only non-zero counter-direction cell, `lots of people is`;
- the moderate positive cells, `plenty of people are` and `the rest of the people are`.

The high-count `lots of people are` cell remains raw-unfiltered for now because it has 287 raw rows
and should be handled by either sampling or a dedicated full-coding pass.

## Retrieval

KWIC files:

- `data/agr-coca-projection/raw/partitive-agreement-followup/kwic/02-lots-of-people-is.json`
- `data/agr-coca-projection/raw/partitive-agreement-followup/kwic/03-plenty-of-people-are.json`
- `data/agr-coca-projection/raw/partitive-agreement-followup/kwic/05-the-rest-of-the-people-are.json`

Row-level coding:

- `data/agr-coca-projection/coded/partitive-agreement-targeted-kwic-coding.csv`

COCA returned one intermittent server-error page for `the rest of the people are`; retrying after a
longer delay succeeded.

## Results

| query | raw count | parsed KWIC rows | filtered target rows |
|---|---:|---:|---:|
| `lots of people is` | 5 | 5 | 0 |
| `plenty of people are` | 65 | 64 | 63 |
| `the rest of the people are` | 15 | 14 | 14 |

The `lots of people is` rows are not licensed singular target rows:

- four are non-subject rows where the query string is object/complement material inside a gerund or
  nominal frame;
- one is an apparent target-frame nonstandard/error row, retained as denominator-only evidence.

The `plenty of people are` cell has one malformed existential/relative row coded as
denominator-only. The `the rest of the people are` cell has one raw-list row absent from the saved
KWIC frame; the 14 parsed rows are target plural agreement rows.

## Interpretation

This targeted filter supports the partitive/QN people-frame direction without yet completing the
large `lots of people are` positive cell. Within the filtered subset, target plural rows are 77
(`plenty` + `rest`) and licensed target singular rows are 0.

No graph mutation or score movement follows. This is still measurement work inside the `AGR` COCA
vertical slice.
