# AGR COCA Bunch-Inanimate KWIC Filter Pass

**Date:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Tranche:** `bunch-inanimate-confirmatory`

## Question

Does the `bunch` agreement profile change when the plural complement is inanimate rather than
animate?

This tranche was registered as a contrast to `bunch-animate-confirmatory`, where `a bunch of
people/kids` strongly favoured plural agreement after KWIC filtering.

## Retrieval

Raw list queries were run for:

- `a bunch of flowers is/are/was/were`
- `a bunch of things is/are/was/were`

Non-zero cells were KWIC-filtered with `scripts/fetch_coca_kwic_from_list.mjs`, using the same
list-result-click route as the animate tranche.

## Results

Raw list counts:

| query | raw count |
|---|---:|
| `a bunch of flowers is` | 2 |
| `a bunch of flowers are` | 0 |
| `a bunch of flowers was` | 0 |
| `a bunch of flowers were` | 0 |
| `a bunch of things is` | 1 |
| `a bunch of things are` | 0 |
| `a bunch of things was` | 0 |
| `a bunch of things were` | 1 |

KWIC-filtered target counts:

| agreement | filtered target rows |
|---|---:|
| plural present | 0 |
| plural past | 1 |
| singular present | 1 |
| singular past | 0 |

Aggregate filtered target rows:

| polarity | filtered target rows |
|---|---:|
| plural agreement | 1 |
| singular agreement | 1 |

Two of the three raw singular hits were non-subject false positives:

- `a bunch of flowers is`: one target singular row; one object-of-`destroying` false positive.
- `a bunch of things is`: one object-of-`juggle` false positive.

The row-level coding is in `data/agr-coca-projection/coded/bunch-inanimate-kwic-coding.csv`.

## Interpretation

This tranche is sparse and does not show the animate tranche's overwhelming plural profile. That is
useful: it suggests the animate `bunch` result is not simply an artifact of the query template.

It is not enough to estimate a stable inanimate agreement profile. Treat it as a contrastive
pressure point rather than a scored result. The next best corpus step is likely
`majority-minority-confirmatory`, because it tests whether `AGR` generalizes beyond `bunch` while
keeping plural-set complements central.
