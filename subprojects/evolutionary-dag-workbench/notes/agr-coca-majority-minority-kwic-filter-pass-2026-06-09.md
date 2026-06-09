# AGR COCA Majority/Minority KWIC Filter Pass

**Date:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Tranche:** `majority-minority-confirmatory`

## Question

Does the `AGR` module generalize beyond `bunch` to majority/minority constructions with plural set
complements?

This tranche matters because the earlier COCA slices were all `bunch`-based. A successful result
here would support the broader agreement-controller module rather than a local `bunch` fact.

## Retrieval

Raw list queries were run for:

- `a majority of people are/is`
- `the majority of people are/is`
- `a minority of voters are/is`

Non-zero cells were KWIC-filtered with `scripts/fetch_coca_kwic_from_list.mjs`, using the same
list-result-click route as the `bunch` tranches.

## Results

Raw list counts:

| query | raw count |
|---|---:|
| `a majority of people are` | 7 |
| `a majority of people is` | 0 |
| `the majority of people are` | 99 |
| `the majority of people is` | 5 |
| `a minority of voters are` | 0 |
| `a minority of voters is` | 0 |

KWIC-filtered target counts:

| agreement | filtered target rows |
|---|---:|
| plural present | 105 |
| singular present | 0 |

The large `the majority of people are` cell has one retrieval wrinkle: COCA's list count was 99,
but the KWIC frame exposed 98 parsed rows. The missing row was absent from the saved KWIC frame
text rather than dropped by the parser.

The five raw `the majority of people is` rows did not yield target singular agreement:

- four were non-subject false positives (`the majority of people` inside a PP or object position);
- one was a likely nonstandard/error row (`the majority of people is agree`), coded as
  denominator-only rather than target singular agreement.

The row-level coding is in `data/agr-coca-projection/coded/majority-minority-kwic-coding.csv`.

## Interpretation

This tranche supports the broader `AGR` agreement-controller module beyond `bunch`: plural agreement
dominates for majority constructions with plural human complements, and raw singular hits vanish
under KWIC filtering.

The `minority` query pair was uninformative because both registered cells returned zero raw rows.
This means the tranche supports generalization to `majority`, not to the entire majority/minority
family.

No score movement follows. The evidence is stronger than the `bunch` tranches for cross-construction
portability, but the workbench still needs either a formal evaluation update or another registered
construction family before numeric projective credit should be considered.
