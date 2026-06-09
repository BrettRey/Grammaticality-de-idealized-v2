# AGR COCA Critic-Verdict Variance Check

**Date:** 2026-06-09
**Target evaluation:** `evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`
**Protocol:** `notes/critic-verdict-variance-protocol-2026-06-09.md`
**Result:** Mostly stable; one prediction-test label downgraded from `passed` to `mixed`.

## Purpose

This pass tests whether the first data-bearing AGR projection evaluation is stable under repeated
LLM critique. It does not treat the critics as adjudicators of grammaticality. It treats them as a
variance probe over the workbench's own evaluation labels.

## Inputs

The three critic runs used the pre-correction packet:

`data/critic-variance/packets/agr-coca-projection-prevariance-critic-packet.md`

Run outputs:

- `data/critic-variance/runs/agr-coca-projection-codex-run1.json`
- `data/critic-variance/runs/agr-coca-projection-codex-run2.json`
- `data/critic-variance/runs/agr-coca-projection-codex-run3.json`

The corrected summary is:

`data/critic-variance/summaries/agr-coca-projection-variance-summary.csv`

## Findings

Stable labels:

- `bunch-animate-coca-projection`: 3/3 critics preserved `passed`.
- `majority-coca-portability`: 3/3 critics preserved `passed`.
- `majority-denominator-omission-audit`: 3/3 critics preserved `passed`.
- `collective-number-transparent-agreement-cgel`: 2/3 critics preserved `survives_as_module`; one weakened it to `partly_survives`.

Boundary labels:

- `bunch-inanimate-coca-contrast`: 2/3 critics preserved `mixed`; one upgraded it to `passed`.
- `minority-coca-uninformative`: 2/3 critics preserved `inconclusive`; one downgraded it to `failed` as a query-cell failure.

Correction:

- `partitive-qn-coca-targeted-kwic`: 2/3 critics labelled it `mixed`, not `passed`.

The critics agreed that the direction is supportive but that the largest positive cell,
`lots of people are`, is only a pre-declared 100-row bounded KWIC sample. That is enough to preserve
the partitive/QN contrast as supportive evidence, but too weak for a clean `passed` label under the
registered pass condition.

## Decision

Downgrade `partitive-qn-coca-targeted-kwic` from `passed` to `mixed`.

Keep the card-level result `survives_as_module`.

Keep `score_decision: no-score-change`.

No graph mutation follows. The variance check tightens the evidence label; it does not alter the
AGR graph's current scoped-module status or authorize numeric score movement.

## Next Data Boundary

The partitive/QN test can move back toward `passed` only if the largest positive cell is fully
filtered or replaced by fully filtered registered cells. Until then, it remains supportive but
mixed evidence.
