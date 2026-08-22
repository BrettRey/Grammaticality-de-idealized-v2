# Formal claim ledger: model and manuscript repair

Date: 2026-08-22  
Status: repair complete; pre-repair baseline retained below

## Reproducible baseline

- Paper repository commit: `47d4c61d7eb22400652f3893331a0aaa89431dc7`
- Tool repository commit: `0e485f9fb80622361da091141398dff26c7592dd`
- Pre-repair closed-loop sweep SHA-256:
  `f548657ffe995cda1523b497d86d8eb1f2276da6aba4ad0463adb153695d7449`
- Pre-repair test result: 288/288 checks passed (27 fixture, 46 smoke,
  41 revised-model, 18 joint-likelihood, 156 closed-loop).
- Both repositories already contained user-owned changes and untracked files.
  Implementation must preserve them and must not treat the commits above as
  clean-tree snapshots.

## Post-repair verification

- Final closed-loop sweep SHA-256:
  54f359dab7d63fb05bb7acdc19067d8698f73e62d1402ba27e147043ec275963
- Two independent regenerations produced that identical hash.
- Post-repair test result: 316/316 checks passed (27 fixture, 46 smoke,
  57 revised-model, 18 conditional-shell, 168 closed-loop).
- The paper builds to 66 pages with no undefined citations or references.
- Lean builds with no sorry, admit, axiom, or unsafe declaration in
  formalization/OVMG.

## Claim classes

| Claim | Current status | Required support before manuscript use |
|---|---|---|
| The gated-choice model gives the probability of each observed outcome conditional on target availability. | Definition/exact calculation | Unit tests including the outside option. |
| A target token has likelihood proportional to the latent availability rate. | Exact under the stated observation model | Derivation and limiting-case tests. |
| A non-target outcome has likelihood affine in the latent availability rate. | Exact under the stated observation model | Derivation and tests against direct numerical integration. |
| The evidence state is a Beta approximation to the exact batch posterior. | Approximation | Exact mixture moments followed by documented moment matching; approximation-error diagnostics. |
| Evidence discounting acts once on accumulated evidence and preserves the stated baseline prior. | Update convention | Recurrence tests and no-evidence convergence test. |
| Posterior mean and concentration have their ordinary epistemic interpretations. | Licensed only after the filter repair | Calibration and limiting-case checks; no pseudo-count LLR update in the main simulator. |
| Posterior-threshold adoption is a candidate causal transition rule. | Model assumption, not empirical result | Independent threshold interpretation; comparison with alternatives. |
| A reduced fixed-point crossing locates candidate equilibria. | Diagnostic approximation | Agreement with the full deterministic map near fixed points. |
| Stability and return rates are properties of the full evidence-population map. | Model result once computed | Full Jacobian eigenvalues, not only a scalar reduced multiplier. |
| Bistability occurs for some stated parameter regions. | Simulation/model result | Regenerated sweeps and seeds under the repaired filter. |
| A particular response slope is a bifurcation threshold. | Not established | Do not claim unless a continuation analysis establishes it. |
| Concentration loss can precede mean movement during evidence withdrawal. | Robust model prediction under stated assumptions | Moribund-language simulation and analytic limiting cases. |
| Dispersion must rise before the mean moves. | Not robust | State only conditionally, with the extra heterogeneity mechanism named. |
| Repair observations identify latent licensing status. | Not established by the current wiring check | Keep outside the main warrant unless a shared latent likelihood is implemented. |
| The Lean development proves the empirical model. | False | Lean remains a structural consistency check for explicitly encoded definitions only. |
| Projectibility follows from stability alone. | False | Keep projectibility conditional on non-trivial projection targets and evidence. |

## Blocking dependency

The old update adds omission log-likelihood ratios to the Beta `b` parameter.
That is not the posterior update implied by the declared gated-choice likelihood:
for a non-target outcome, the likelihood is an affine function of the latent
availability rate, not a power of `(1 - theta)`. Consequently the old
`positiveEvidence`/`negativeEvidence` state is a generalized score, not a Beta
posterior over the population rate. All old balance thresholds, ceiling values,
and closed-loop sweeps are quarantined as pre-repair results until regenerated.

## Acceptance gates

1. Exact one-event and batch mixture moments agree with independent numerical
   integration to numerical tolerance.
2. Moment matching preserves the first two moments and returns a valid Beta
   state in limiting cases (`d = 0`, `d = 1`, target-only, no evidence).
3. Discounting preserves the baseline prior and is applied once per update.
4. The revised and closed-loop simulators use the likelihood-consistent update.
5. Full-map fixed points and Jacobian eigenvalues are reported for primary
   stability claims.
6. All sweeps are regenerated with seeds, parameter grids, and artifact hashes.
7. Manuscript wording distinguishes definition, approximation, simulation
   result, conditional prediction, and empirical claim.
8. Lean builds without `sorry`, `admit`, added axioms, or unsafe declarations;
   no new theorem is added unless it closes a named structural gap.

## Change record

- 2026-08-22: Ledger opened and pre-repair baseline frozen.
- 2026-08-22: Likelihood-consistent filter, population transition, full-map
  diagnostics, perturbation experiments, and manuscript calibration completed;
  all acceptance gates satisfied at the stated scope.
