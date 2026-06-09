# AGR COCA Bunch-Animate Raw List Pass

**Date:** 2026-06-09
**Target module:** `AGR`
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Protocol:** `notes/agreement-coca-projection-protocol-2026-06-09.md`
**Cell:** `bunch-animate-confirmatory`
**Status:** Raw list-count tranche only; no KWIC filtering, no denominator estimate, no score movement.

## Run

The English-Corpora.org credentials were available through the private wrapper env file, but the
stored browser profile was not enough by itself. The shared `ecorg` wrapper needed a small repair
because English-Corpora's current form script failed under automation and could return stale result
frames. After the wrapper repair, the `bunch-animate-confirmatory` list tranche ran with a delay
between searches.

Manifest:

- `data/agr-coca-projection/query-manifest-bunch-animate-list.csv`

Raw outputs:

- `data/agr-coca-projection/raw/bunch-animate-confirmatory/`

Summary:

- `data/agr-coca-projection/summary.csv`

## Raw Counts

| Query | Agreement cell | Raw count |
| --- | --- | ---: |
| `a bunch of people is` | singular present | 3 |
| `a bunch of people are` | plural present | 27 |
| `a bunch of people was` | singular past | 0 |
| `a bunch of people were` | plural past | 28 |
| `a bunch of kids is` | singular present | 3 |
| `a bunch of kids are` | plural present | 5 |
| `a bunch of kids was` | singular past | 0 |
| `a bunch of kids were` | plural past | 12 |

Aggregate raw plural: 72.
Aggregate raw singular: 6.

Raw plural share: 72 / 78 = 92.3%.

## Interpretation

This is the first live data-bearing tranche for the workbench. It supports the direction registered
for `agr-bunch-animate`: animate plural complements in `a bunch of people/kids` favour plural
agreement in raw COCA list counts.

The result is not yet a scored projective result. The singular raw hits need KWIC filtering, because
earlier QN work showed that counter-direction surface strings often include parse shifts,
non-target heads, quotations, or other non-target uses. The next evidence step is therefore:

1. obtain KWIC rows for the six non-zero cells, or a manageable sample if the wrapper remains
   list-first;
2. code rows using `data/agr-coca-projection/kwic-coding-schema.csv`;
3. separate genuine target agreement from query artifacts;
4. only then update the evaluation layer.

## Workbench Consequence

`AGR` remains a scoped module with all numeric scores at zero. This tranche supplies raw production
pressure for the COCA projection lane, not licensing by itself.
