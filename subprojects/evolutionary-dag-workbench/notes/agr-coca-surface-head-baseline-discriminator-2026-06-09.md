# AGR COCA Surface-Head Baseline Discriminator

**Date:** 2026-06-09
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Evaluation:** `evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`
**Data table:** `data/agr-coca-projection/baseline-discriminator.csv`
**Status:** Discriminator memo; no graph mutation and no score movement.

## Purpose

The AGR COCA lane now has enough filtered/sampled evidence to say what it discriminates against.
The relevant baseline is a simple surface-head-number account:

> Agreement tracks the number of the surface head noun in the agreement-bearing subject phrase.

`AGR` predicts a different pattern when controller identification, notional basis, and licensed
override determine agreement alignment.

## Clean Discriminator Cells

| cell | surface-head baseline | AGR expectation | observed evidence | result |
|---|---|---|---:|---|
| animate `bunch` | singular from `bunch` | plural under animate-member construal | 71 plural vs. 1 singular | baseline disconfirmed |
| `majority` + people | singular from `majority` | plural under plural-set controller construal | 105 plural vs. 0 singular | baseline disconfirmed |
| `the rest of the people` | singular from `rest` | plural available from people-set controller | 14 plural vs. 0 singular | baseline disconfirmed, small cell |

These are the current high-value pressure points. They are better discriminators than raw frequency
or general plural-complement counts because the surface head and observed agreement direction come
apart.

## Supportive But Less Clean Cells

`lots/plenty of people` supports the broader people-frame direction, especially after the bounded
`lots of people are` sample and the zero licensed `lots of people is` counter-cell. But it is not as
clean a surface-head-number discriminator, because the quantity-head status differs across `lots`
and `plenty`.

The inanimate `bunch` cells are also not a baseline kill: the filtered evidence is 1 plural row and
1 singular row. Their value is contrastive. They show that the animate result is not simply a generic
`bunch` query-template effect, but they do not estimate a stable inanimate profile.

## Decision

This pass should not move numeric scores. It does, however, sharpen the COCA vertical slice:

- `AGR` now has three explicit cells where a simple surface-head baseline predicts the wrong dominant
  direction.
- The strongest portability discriminator is `majority`, because it is non-`bunch` and has a clean
  105:0 filtered direction.
- The next empirical improvement should be an uncertainty/denominator pass, not another nearby
  plural-complement query.

## Stronger Rival Added Later

This memo is now superseded as the main discriminator boundary. Surface-head number is a useful
sanity baseline, but the live rival is construction-specific listing:

> known QN and collective frames have local learned agreement preferences.

That rival is now represented by
`graphs/archive/agreement-construction-listing-baseline-candidate.json` and
`evaluations/protocol-tests/agreement-construction-listing-baseline-rival-2026-06-09.json`. The next
AGR data move should pressure that rival with the registered low-frequency QN tranche, not continue
to accumulate wins against surface-head number.

## Next Marginal Step

Run the planned `false-positive-audit` / `false-omission-audit` validation lane, or define a compact
uncertainty summary for the existing discriminator cells. That would convert the current
directional evidence into a more defensible projection report without requiring score movement.
