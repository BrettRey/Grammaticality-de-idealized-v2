# AGR COCA Partitive Agreement Raw List Pass

**Date:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Tranche:** `partitive-agreement-followup`
**Status:** Raw finite-agreement list counts only; no KWIC filtering yet; no score movement.

## Question

Do finite present-agreement strings in partitive/QN people frames show the expected plural direction
before KWIC filtering?

This follow-up was registered after the phrase-count partitive calibration showed that the original
`partitive-calibration` queries were useful denominator probes but not agreement-outcome tests.

## Retrieval

Raw list queries were run for:

- `lots of people are`
- `lots of people is`
- `plenty of people are`
- `plenty of people is`
- `the rest of the people are`
- `the rest of the people is`

Manifest:

- `data/agr-coca-projection/query-manifest-partitive-agreement-list.csv`

Raw outputs:

- `data/agr-coca-projection/raw/partitive-agreement-followup/`

## Raw Counts

| query | agreement cell | raw count |
|---|---|---:|
| `lots of people are` | plural present | 287 |
| `lots of people is` | singular present | 5 |
| `plenty of people are` | plural present | 65 |
| `plenty of people is` | singular present | 0 |
| `the rest of the people are` | plural present | 15 |
| `the rest of the people is` | singular present | 0 |

Aggregate raw plural: 367.
Aggregate raw singular: 5.

## Interpretation

The raw list layer supports the expected plural direction for plural-people complements, but this is
not yet a target-row result. The next useful move is targeted KWIC filtering:

1. KWIC-filter `lots of people is`, because it is the only non-zero counter-direction cell and has
   just five rows.
2. KWIC-filter `plenty of people are` and `the rest of the people are`, because they are moderate
   positive cells.
3. Decide whether to fully KWIC-filter or sample `lots of people are`, whose raw count is 287.

No graph mutation or score movement follows from the raw counts alone.
