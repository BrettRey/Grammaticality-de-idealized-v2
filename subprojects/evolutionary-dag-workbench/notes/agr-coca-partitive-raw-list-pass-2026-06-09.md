# AGR COCA Partitive Raw List Pass

**Date:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Tranche:** `partitive-calibration`
**Status:** Raw phrase-count denominator probe only; no KWIC filtering, no agreement outcome coding,
no score movement.

## Question

Do simple phrase-count probes reproduce the expected contrast between common bare/non-partitive QN
frames and rarer definite-partitive frames?

This tranche is not an agreement test. The registered queries do not include a following finite
verb, so they cannot directly code agreement realization. Their role is to check whether the
denominator side of the COCA lane can distinguish plausible QN subgroups before we design
agreement-bearing follow-up queries.

## Retrieval

Raw list queries were run for:

- `lots of people`
- `lots of the people`
- `plenty of people`
- `plenty of the people`
- `the rest of people`
- `the rest of the people`

Manifest:

- `data/agr-coca-projection/query-manifest-partitive-list.csv`

Raw outputs:

- `data/agr-coca-projection/raw/partitive-calibration/`

## Results

| query | raw phrase count |
|---|---:|
| `lots of people` | 3875 |
| `lots of the people` | 5 |
| `plenty of people` | 1563 |
| `plenty of the people` | 1 |
| `the rest of people` | 12 |
| `the rest of the people` | 272 |

COCA reports sampled high-frequency list outputs for `lots of people`, `plenty of people`, and
`the rest of the people`. The saved raw JSON files preserve the list output text and table data.

## Interpretation

The raw phrase counts reproduce the expected subgroup contrast:

- `lots of people` and `plenty of people` are common bare/non-partitive QN frames;
- `lots/plenty of the people` are rare as direct strings;
- `the rest of the people` is much more viable than `the rest of people`.

This is useful for denominator design, but it is not evidence about agreement direction. The next
usable step would be to register finite-verb follow-up cells, for example contrasting
`lots/plenty/rest` frames with `are/is/were/was`, and then KWIC-code the non-zero cells.

No graph mutation or score movement follows.
