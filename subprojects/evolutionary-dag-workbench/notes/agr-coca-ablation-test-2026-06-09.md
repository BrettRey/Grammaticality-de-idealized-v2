# AGR COCA Ablation Test

**Date:** 2026-06-09
**Graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Runner:** `scripts/run_agr_ablation.py`
**Summary data:** `data/agr-coca-projection/ablation-summary.csv`
**Status:** Compression check; no graph mutation and no numeric score movement.

## Question

The AGR vertical slice showed that the module beats a simple surface-head-number baseline in
checked COCA production cells. This ablation asks a different question:

> Which AGR constructs are load-bearing for the existing COCA and held-out evaluations?

The test creates temporary graph variants, repoints the existing AGR evaluations at each variant,
and records whether graph validation and evaluation validation survive. The invalid variants are
not archived as candidates.

## Ablations

The runner tests five graph changes:

- remove `notional_agreement_basis`;
- merge `agreement_controller_identification` into `agreement_feature_alignment`;
- remove `production_probability`;
- remove `retrieval_attractor_salience`;
- remove `agreement_override_pattern`.

The evaluations are:

- `agreement-controller-override-coca-projection-2026-06-09`;
- `agreement-controller-override-heldout-scope-2026-06-09`;
- `agreement-controller-override-heldout-measure-2026-06-09`.

## Results

| ablation | COCA projection | held-out scope | held-out measure | interpretation |
|---|---|---|---|---|
| baseline | passes | passes | passes | sanity check |
| drop `notional_agreement_basis` | fails | fails | fails | load-bearing across the AGR module |
| merge controller into alignment | fails | fails | fails | the controller/alignment split is load-bearing |
| drop `production_probability` | fails | passes | passes | production bridge is load-bearing for the COCA vertical slice, not for the older scope tests |
| drop `retrieval_attractor_salience` | fails | passes | passes | retrieval-attractor salience is load-bearing for the COCA/attraction-facing evaluation layer only |
| drop `agreement_override_pattern` | passes | fails | fails | override pattern is load-bearing for held-out agreement scope, not for the current COCA cells |

All ablated graphs remain graph-valid. Failures are evaluation failures: required nodes, required
edges, or activated paths disappear.

## Decision

Do not compress AGR right now.

The current module is not obviously overbuilt relative to the tests it has actually faced. The
ablation instead separates two kinds of load-bearing structure:

- core agreement-scope structure: `notional_agreement_basis`, `agreement_controller_identification`,
  `agreement_feature_alignment`, and `agreement_override_pattern`;
- COCA vertical-slice structure: `production_probability` and `retrieval_attractor_salience`.

This is useful because it keeps the pilot corpus lane from being mistaken for the whole agreement
module. `production_probability` is needed when the graph is asked to make corpus-production
claims. `agreement_override_pattern` is needed when the graph is asked to handle held-out agreement
override cases. Neither result authorizes numeric score movement.

## Next Marginal Move

Do not add more nearby AGR cards immediately. The next higher-value pressure is either:

1. a critic-verdict variance check on one existing evaluation, to estimate how noisy the survival
   labels are; or
2. a second compression pass over the more suspicious overlap pairs, especially `FDL`/`UOB` and
   `OPG`/`DYN`.

Held-out cards become urgent only when a graph is being considered for projective score movement or
a broader scope claim. AGR is not there yet.
