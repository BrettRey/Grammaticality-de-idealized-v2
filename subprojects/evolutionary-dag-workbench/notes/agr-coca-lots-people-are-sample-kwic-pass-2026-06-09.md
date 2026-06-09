# AGR COCA `lots of people are` Bounded KWIC Sample

**Date:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Parent decision memo:** `notes/agr-coca-vertical-slice-stock-memo-2026-06-09.md`
**Sample declaration:** `notes/agr-coca-lots-people-are-sample-declaration-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Tranche:** `partitive-agreement-followup`
**Status:** Bounded positive-cell KWIC sample passed; no score movement.

## Question

Was the high-count raw `lots of people are` cell mostly genuine plural agreement, or mostly COCA
query noise?

The stock memo fixed the decision boundary in advance: if the default KWIC route could provide at
least 100 rows and at least 90% were target plural agreement, the partitive/QN people-frame
prediction could move from `mixed` to `passed`, provided the counter-direction singular side
remained at 0 licensed target rows.

## Retrieval

Command:

```bash
node scripts/fetch_coca_kwic_from_list.mjs \
  --query 'lots of people are' \
  --output data/agr-coca-projection/raw/partitive-agreement-followup/kwic/01-lots-of-people-are.json \
  --allow-partial \
  --min-rows 100
```

COCA reported 281 expected KWIC entries for the clicked list result. The default KWIC frame exposed
100 rows before timeout, so the fetcher saved the pre-declared partial sample.

Raw and coded files:

- `data/agr-coca-projection/raw/partitive-agreement-followup/kwic/01-lots-of-people-are.json`
- `data/agr-coca-projection/coded/lots-people-are-sample-kwic-coding.csv`

## Results

| query | raw list count | expected KWIC entries | sampled KWIC rows | target plural rows |
|---|---:|---:|---:|---:|
| `lots of people are` | 287 | 281 | 100 | 100 |

All 100 sampled rows are coded `target_plural_agreement`. This is a bounded sample result, not a
full filtered count for all raw hits.

The counter-direction result from the targeted KWIC pass remains unchanged:

| query | raw list count | parsed KWIC rows | licensed target singular rows |
|---|---:|---:|---:|
| `lots of people is` | 5 | 5 | 0 |

## Interpretation

The pre-declared threshold is met: the sampled positive cell is 100/100 target plural agreement, and
the singular counter-direction cell still has 0 licensed target rows.

The `partitive-qn-coca-targeted-kwic` prediction should therefore move from `mixed` to `passed`.
This updates the evidence trail only. It does not authorize numeric score movement, because the
sample is bounded and the broader COCA lane remains a narrow English production vertical slice.
