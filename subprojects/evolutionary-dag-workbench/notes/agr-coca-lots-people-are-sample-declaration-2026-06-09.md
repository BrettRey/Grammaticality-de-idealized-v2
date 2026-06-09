# AGR COCA `lots of people are` Sample Declaration

**Date:** 2026-06-09
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Parent memo:** `notes/agr-coca-vertical-slice-stock-memo-2026-06-09.md`
**Cell:** `partitive-agreement-followup`
**Query:** `lots of people are`

## Decision

Use a bounded KWIC check for `lots of people are` rather than full manual coding unless COCA exposes
all 287 raw rows cleanly.

The bounded check is:

- the first/default KWIC page exposed by the normal list-result-click route;
- acceptable only if it contains at least 100 rows;
- coded with the existing `kwic-coding-schema.csv`;
- interpreted as a sample check on whether the 287 raw plural rows are mostly target plural
  agreement or mostly query noise.

## Interpretation Rule

If the bounded KWIC check contains at least 100 rows and at least 90% are target plural agreement,
then the `partitive-qn-coca-targeted-kwic` prediction may move from `mixed` to `passed`, provided
the existing counter-direction result remains unchanged:

- `lots of people is`: 0 licensed target singular rows.

If the bounded check contains fewer than 100 rows, or if target/noise coding is unstable, keep the
prediction `mixed`.

If the bounded check shows mostly non-target noise, mark the prediction `failed`.

No numeric score movement follows from this sample.
