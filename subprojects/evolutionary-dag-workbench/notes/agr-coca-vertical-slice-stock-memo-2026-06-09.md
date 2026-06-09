# AGR COCA Vertical Slice Stock Memo

**Date:** 2026-06-09
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Evaluation:** `evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`

## Purpose

Fix the decision boundary for the current `AGR` COCA vertical slice so the next data move is
selection pressure rather than accumulation.

## Current Evidence State

The COCA lane is now usable as a measurement workflow. Raw list counts are treated as discovery or
triage only; KWIC-filtered target rows are the evidential unit.

The relevant live rival is now construction-specific listing, not simple surface-head number. The
surface-head comparison remains a sanity baseline, but it no longer fixes the decision boundary for
projective credit.

Completed calibration:

- Known-QN calibration reproduces expected directions: `a number of people` gives 98 target plural
  rows; `a lot of money is` gives 42 target singular rows; `a lot of money are` gives 0 licensed
  target plural rows.
- This supports the KWIC-coding method, not `AGR` projective credit.

Completed projection-supporting tranches:

- Animate `bunch`: 71 target plural rows vs. 1 target singular row. Status: `passed`.
- Inanimate `bunch`: 1 target plural row vs. 1 target singular row. Status: `mixed` because sparse.
- Majority: 105 target plural rows vs. 0 target singular rows. Status: `passed`.
- Minority: zero raw rows in registered direct strings. Status: `inconclusive`.
- Partitive/QN people frames: targeted KWIC subset gives 77 target plural rows vs. 0 licensed target
  singular rows. Status: `mixed` because `lots of people are` remains raw-unfiltered at 287 rows.

## Decision Boundary

The partitive/QN people-frame test can move from `mixed` to `passed` only if `lots of people are`
receives a bounded KWIC check.

Minimum acceptable bounded check:

- Either fully KWIC-code `lots of people are`, or code a pre-declared sample of at least 100 rows if
  full coding is disproportionate.
- The sampled/full set must show that the raw plural cell is mostly target plural agreement rather
  than query noise.
- The existing counter-direction result must remain: `lots of people is` has 0 licensed target
  singular rows, with any malformed row retained as denominator-only nonstandard/error evidence.

Upgrade condition:

- Mark the partitive/QN prediction `passed` if the bounded `lots of people are` check shows target
  plural rows strongly dominate and the licensed singular side remains zero or negligible.

Hold condition:

- Keep the partitive/QN prediction `mixed` if `lots of people are` is not checked, if the sample is
  too small or ad hoc, or if target/noise coding is unstable.

Failure condition:

- Mark the partitive/QN prediction `failed` only if the checked plural cell is mostly non-target
  noise or if licensed singular agreement appears at comparable density in the counter-direction
  cells.

## Score Boundary

No numeric score movement is licensed by the current COCA lane.

Even if the partitive/QN prediction moves to `passed`, the result should update the evidence trail,
not `projective_power`, unless a held-out or pre-registered projection threshold is added in advance.

The current warranted claim is narrower:

> `AGR` has a working corpus measurement lane and multiple supportive English production tranches,
> but no numeric projective credit yet, and it has not beaten construction-specific listing.

## Next Action

Run a bounded KWIC check for `lots of people are`:

1. Prefer full KWIC coding if COCA exposes all rows reliably.
2. If full coding is too costly, pre-declare a 100-row sample from the saved KWIC/list path and code
   only that sample.
3. Update `summary.csv`, the partitive KWIC note, and the COCA projection evaluation accordingly.

After the construction-listing rival was registered, the better marginal move is the
low-frequency-QN discriminator in `notes/agr-construction-listing-rival-protocol-2026-06-09.md`.
The `lots of people are` full-filter remains useful measurement cleanup, but it does not answer the
stronger rival.
