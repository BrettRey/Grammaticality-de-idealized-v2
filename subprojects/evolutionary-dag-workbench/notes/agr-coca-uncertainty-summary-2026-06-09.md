# AGR COCA Uncertainty Summary

**Date:** 2026-06-09
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Data table:** `data/agr-coca-projection/uncertainty-summary.csv`
**Status:** Analysis summary over existing audit data; no new COCA run, graph mutation, or score movement.

## Purpose

The surface-head baseline discriminator identified three clean pressure cells:

- animate `bunch`;
- `majority`;
- `the rest of the people`.

This summary asks how strong those cells look once uncertainty is made explicit. The measure is a
95% Wilson interval for the plural share among target agreement rows:

```text
plural target rows / (plural target rows + singular target rows)
```

This is not an opportunity-rate estimate, and it is not a licensing score. It is a compact
uncertainty check on the observed agreement direction among coded target rows.

## Results

| cell | plural | singular | plural share | 95% Wilson interval | interpretation |
|---|---:|---:|---:|---:|---|
| animate `bunch` | 71 | 1 | 0.986 | [0.925, 0.998] | strong directional result |
| `majority` exact rows | 105 | 0 | 1.000 | [0.965, 1.000] | tight directional result |
| `majority` audit-augmented | 142 | 0 | 1.000 | [0.974, 1.000] | tight audit-augmented result |
| `the rest of the people` | 14 | 0 | 1.000 | [0.785, 1.000] | clean but wide small cell |

## Interpretation

The strongest current discriminator is `majority`, not `bunch`. It is non-`bunch`, has 105 exact
target plural rows and 0 target singular rows, and the denominator false-omission audit adds 37
omitted plural opportunities with 0 omitted singular opportunities.

Animate `bunch` remains a strong discriminator against a simple surface-head-number baseline, but it
is less clean as a general agreement estimate because `bunch` is a known boundary item and because
the inanimate contrast is sparse.

`The rest of the people` is directionally useful but not a primary estimate. Its 14:0 result is
clean, but the lower Wilson bound is wide because the cell is small.

## Decision

The AGR COCA vertical slice now supports a narrower, defensible claim:

> In the checked English production cells, plural agreement is not a raw-query artifact and is not
> predicted by a simple surface-head-number baseline; the strongest current pressure comes from
> `majority` plus the denominator omission audit.

No numeric score movement follows. The result is still English-only, corpus-production-only, and
bounded by direct-query plus denominator-sample methods.

## Next Marginal Step

The next useful move is a compact write-up of the AGR vertical slice, not another data tranche. The
write-up should separate:

- representational result: `AGR` beats surface-head-only agreement in the checked cells;
- measurement result: KWIC filtering and omission audit reduce raw-query artifact risk;
- limitation: this is not yet projective score movement or cross-domain stability.
