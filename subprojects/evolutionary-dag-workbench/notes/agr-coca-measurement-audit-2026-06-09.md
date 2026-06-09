# AGR COCA Measurement Audit

**Date:** 2026-06-09
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Evaluation:** `evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`
**Audit lanes:** `false-positive-audit`; `false-omission-audit`
**Status:** Measurement audit completed for current AGR discriminator cells; no graph mutation and no score movement.

## Purpose

The AGR COCA vertical slice now has several passed directional cells. This audit asks a narrower
measurement question:

> Are those directional results artifacts of raw direct-string matching?

Two risks are separated:

- false positives: raw direct strings include non-target rows;
- false omissions: direct agreement strings miss agreement-bearing opportunities that would change
  the observed direction.

## False-Positive Pressure

File:

- `data/agr-coca-projection/false-positive-audit.csv`

Summary:

| audit | coded rows | target rows | denominator-only rows | excluded false positives | result |
|---|---:|---:|---:|---:|---|
| animate `bunch` exact rows | 77 | 72 | 0 | 5 | low false-positive pressure |
| inanimate `bunch` exact rows | 4 | 2 | 0 | 2 | sparse/high-noise |
| `majority` exact rows | 110 | 105 | 1 | 4 | low false-positive pressure |
| selected partitive/QN exact rows | 83 | 77 | 2 | 4 | low false-positive pressure |
| `lots of people are` bounded sample | 100 | 100 | 0 | 0 | no sample false-positive pressure |

The inanimate `bunch` cells remain sparse and noisy, as already recorded. The clean discriminator
cells are not raw-query artifacts.

## False-Omission Audit

Declaration:

- `notes/agr-coca-false-omission-denominator-sample-declaration-2026-06-09.md`

Raw and coded files:

- `data/agr-coca-projection/raw/false-omission-audit/kwic/01-the-majority-of-people.json`
- `data/agr-coca-projection/coded/majority-denominator-omission-sample-coding.csv`

COCA reported 1030 expected entries for `the majority of people`. The default KWIC frame exposed 98
rows, so the sample meets the declared 90-row denominator threshold.

| label | rows | interpretation |
|---|---:|---|
| `direct_captured_plural_agreement` | 11 | rows already captured by the direct `are/arent` route |
| `omitted_plural_agreement` | 37 | agreement-bearing plural rows missed by the registered `are/is` direct strings |
| `no_number_agreement_opportunity` | 17 | visible predicate has no number contrast for this audit |
| `not_subject_or_no_target_predicate` | 29 | phrase is not the auditable subject or lacks a target predicate |
| `unclear_or_non_target` | 4 | malformed, parenthetical, or too unclear |

The important result is directional:

- omitted plural agreement rows: 37
- omitted singular agreement rows: 0

The direct `are/is` strings therefore undercount `majority` agreement opportunities, but the
omission direction strengthens rather than reverses the plural-dominant result.

## Decision

The `majority` discriminator is now stronger as a measurement result:

- false positives are low in the exact rows;
- the denominator sample finds omitted agreement-bearing opportunities;
- those omitted opportunities are plural, not singular.

This supports the existing `majority-coca-portability` result and adds a new measurement-audit
prediction test. It does not license numeric score movement because the denominator sample is
bounded and limited to one discriminator cell.

## Next Marginal Step

The best next empirical step is not another nearby direct query. It is either:

- repeat this omission-audit design for animate `bunch`; or
- produce an uncertainty summary for the three clean discriminator cells.

The uncertainty summary is probably the better next step because it can be computed from the current
audit tables without another COCA run.
