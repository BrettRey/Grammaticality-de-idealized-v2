# AGR COCA Vertical Slice Report

**Date:** 2026-06-09
**Graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Evaluation:** `evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`
**Data directory:** `data/agr-coca-projection/`
**Status:** Worked vertical slice; no numeric score movement.

## One-Sentence Result

The `AGR` module beats a simple surface-head-number baseline in the checked English production
cells, with the strongest pressure from `majority`: 105:0 exact plural agreement rows, 142:0 after a
bounded denominator omission audit, and no detected omitted singular-agreement competitors.

## What Was Being Tested

The target graph separates five agreement constructs:

- `agreement_controller_identification`;
- `agreement_feature_alignment`;
- `agreement_override_pattern`;
- `notional_agreement_basis`;
- `retrieval_attractor_salience`.

The corpus vertical slice asks whether production evidence in COCA supports that separation better
than a simpler baseline:

> Agreement tracks the number of the surface head noun in the agreement-bearing subject phrase.

The test is deliberately narrow. It is about English corpus production in selected number-transparent
agreement cells. It is not a general grammaticality account and it is not a licensing score.

## Method

The lane used a staged procedure:

1. Register query cells and expected directions in `query-plan.csv` and `prediction-register.csv`.
2. Treat raw COCA list counts as triage only.
3. Use KWIC filtering to code target agreement rows separately from false positives, denominator-only
   nonstandard/error rows, and non-target rows.
4. Add a bounded positive-cell sample for the high-count `lots of people are` row set.
5. Add a false-positive audit across already coded exact-query rows.
6. Add a bounded false-omission denominator sample for `the majority of people`.
7. Report Wilson intervals for plural share among coded target agreement rows.

This improves on a raw-frequency corpus pass by separating discovery, filtering, denominator risk,
and uncertainty.

## Main Discriminator

The cleanest discriminator is `majority`, not `bunch`.

| cell | surface-head baseline | AGR expectation | evidence | result |
|---|---|---|---:|---|
| `a/the majority of people` | singular from `majority` | plural under plural-set controller construal | 105:0 exact; 142:0 audit-augmented | baseline disconfirmed |

The exact query rows already disconfirm the surface-head baseline. The denominator omission audit
then checks whether direct `are/is` queries missed enough singular opportunities to reverse the
result. They did not. In a bounded 98-row `the majority of people` denominator sample, omitted
agreement-bearing opportunities were 37 plural and 0 singular.

## Other Discriminator Cells

| cell | evidence | interpretation |
|---|---:|---|
| animate `bunch` | 71 plural vs. 1 singular | strong baseline pressure, but `bunch` is a known boundary item |
| `the rest of the people` | 14 plural vs. 0 singular | clean direction, small cell |
| inanimate `bunch` | 1 plural vs. 1 singular | contrastive/sparse, not an estimate |
| `lots/plenty of people` | 163 plural vs. 0 licensed singular in checked/sample rows | supportive portability evidence, less clean as a surface-head diagnostic |

The result is therefore not "all plural complements take plural agreement." It is narrower:
controller identification and notional basis matter in cells where the surface head alone predicts
the wrong dominant direction.

## Measurement Audit

False-positive pressure is low in the clean cells:

| audit | target rows | excluded false positives | result |
|---|---:|---:|---|
| animate `bunch` exact rows | 72 | 5 | low false-positive pressure |
| `majority` exact rows | 105 | 4 | low false-positive pressure |
| selected partitive/QN exact rows | 77 | 4 | low false-positive pressure |
| `lots of people are` bounded sample | 100 | 0 | no false-positive pressure in sample |

False omission was checked for the strongest non-`bunch` discriminator:

| denominator sample | omitted plural | omitted singular | result |
|---|---:|---:|---|
| `the majority of people` | 37 | 0 | omission strengthens the plural direction |

## Uncertainty Summary

| cell | plural | singular | plural share | 95% Wilson interval |
|---|---:|---:|---:|---:|
| animate `bunch` | 71 | 1 | 0.986 | [0.925, 0.998] |
| `majority` exact rows | 105 | 0 | 1.000 | [0.965, 1.000] |
| `majority` audit-augmented | 142 | 0 | 1.000 | [0.974, 1.000] |
| `the rest of the people` | 14 | 0 | 1.000 | [0.785, 1.000] |

This makes the evidence hierarchy explicit: `majority` is the strongest cell, animate `bunch` is
strong but constructionally special, and `rest` is directionally clean but small.

## What This Licenses

The current warranted claim is:

> In the checked English production cells, plural agreement is not a raw-query artifact and is not
> predicted by a simple surface-head-number baseline; the strongest current pressure comes from
> `majority` plus the denominator omission audit.

The slice supports the workbench method because the graph did work a flat baseline could not do:
it identified where controller identification and notional basis should matter, separated production
from licensing, and forced measurement audits before any score movement.

## What This Does Not License

This does not show that `AGR` is a general account of grammaticality.

It also does not authorize numeric scores because:

- the evidence is English-only;
- the evidence is corpus-production-only;
- only one denominator omission audit has been run;
- no cross-domain stability test has been passed;
- no sealed held-out tranche was reserved before the AGR lane began.

The result is a publishable pilot slice for the workbench method, not a claim that the best graph of
grammaticality has been found.

## Next Decision Boundary

The next step should be a write-up or compression test, not another nearby COCA query.

For a methods/pilot paper, use this report as the worked example.

For discovery pressure, run the next unit of work as an ablation:

- remove `notional_agreement_basis`;
- merge `agreement_controller_identification` into `agreement_feature_alignment`;
- remove `production_probability`;
- ask which prediction/evaluation claims break.

That would convert the AGR vertical slice from evidence for a graph into evidence about which parts
of the graph are load-bearing.
