# AGR COCA Bunch-Animate KWIC Filter Pass

**Date:** 2026-06-09
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Tranche:** `bunch-animate-confirmatory`

## Question

Does the first registered COCA tranche support the `AGR` prediction that animate plural complements
in `a bunch of people/kids` favour plural agreement when the queried NP is actually the agreement
controller?

## Retrieval

The direct COCA KWIC form route was unreliable. The reproducible route is:

1. run a normal list query;
2. click the list-result phrase link that targets COCA's `x3` KWIC frame;
3. wait until parsed KWIC rows match the `ENTRIES:` count;
4. save the KWIC JSON and code rows against `kwic-coding-schema.csv`.

The repo-local helper for this route is:

```bash
node scripts/fetch_coca_kwic_from_list.mjs --query 'a bunch of people is' --output data/agr-coca-projection/raw/bunch-animate-confirmatory/kwic/01-a-bunch-of-people-is.json
```

## Results

Raw list counts:

| query | raw count |
|---|---:|
| `a bunch of people is` | 3 |
| `a bunch of people are` | 27 |
| `a bunch of people was` | 0 |
| `a bunch of people were` | 28 |
| `a bunch of kids is` | 3 |
| `a bunch of kids are` | 5 |
| `a bunch of kids was` | 0 |
| `a bunch of kids were` | 12 |

KWIC-filtered target counts:

| agreement | filtered target rows |
|---|---:|
| plural present | 31 |
| plural past | 40 |
| singular present | 1 |
| singular past | 0 |

Aggregate filtered target rows:

| polarity | filtered target rows |
|---|---:|
| plural agreement | 71 |
| singular agreement | 1 |

Five of six raw singular hits were non-subject false positives:

- `a bunch of people is`: all three rows were non-subject cases where `is` belonged to another
  controller (`reason`, `email`, or a gerund-clause subject).
- `a bunch of kids is`: two rows were non-subject cases; one row was a genuine target singular
  agreement row.

The row-level coding is in `data/agr-coca-projection/coded/bunch-animate-kwic-coding.csv`.

## Interpretation

This tranche supports the registered direction for animate plural complements: once KWIC-filtered,
plural agreement overwhelmingly dominates target singular agreement.

This is evidence for the `AGR` module's notional-agreement-basis path, not a general grammaticality
result and not a score movement. It is one narrow production/attestation slice. The next useful data
pressure is either:

- run `bunch-inanimate-confirmatory` to test whether animate/member construal is doing work, or
- run `majority-minority-confirmatory` to test whether the agreement-controller module generalizes
  beyond `bunch`.
