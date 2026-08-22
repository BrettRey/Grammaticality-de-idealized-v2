# ovmg-tools

Companion software for Brett Reynolds, *Grammaticality de-idealized: The
Operator-Value Model of Grammaticality* (OVMG).

## Model versions

The repository currently contains two intentionally separate artifacts.

1. **Legacy browser lab** (`lab/`, `js/engine.js`, `js/sim.js`). This is the
   2026-07-09 Tab 1 prototype. Its original fixtures reproduce the old Figure
   4 trajectories and its UI still needs a user-approved interpretability
   pass. It is retained for provenance, not as an implementation of the
   current manuscript's dynamics.
2. **Revised quantitative core** (`js/revised-engine.mjs`,
   `js/revised-sim.mjs`, `js/joint-likelihood.mjs`). This is the current-paper
   reference implementation.
   It keeps a fixed Beta baseline while discounting effective evidence, uses a
   normalized gated-choice model, and routes omissions by log likelihood ratio
   rather than the retired first-order omission mass.

The revised core is an executable model contract, not a fitted empirical
model. Its exact scope, including the required joint likelihood for fitting,
is in [notes/quantitative-model-contract.md](notes/quantitative-model-contract.md).

## Revised core

Per construction node `kappa` in conditioning state `c`, v2 stores a fixed
Beta prior and discounted effective evidence:

```text
a_t = a_0 + positiveEvidence_t
b_t = b_0 + negativeEvidence_t

positiveEvidence_(t+1) = delta_m * positiveEvidence_t + lambda_pos * e_t^+
negativeEvidence_(t+1) = delta_m * negativeEvidence_t + lambda_neg * e_t^-
```

The resulting posterior summaries are the mean `C`, concentration `nu`,
epistemic variance, and predictive between-speaker heterogeneity for the
single-node case, plus a threshold-sensitive decision-confidence read-out.
Evidence weights are generalized-Bayes effective counts and need calibration
before empirical fitting.

At each discrete opportunity, a speaker's inclusion vector gates a softmax over
candidate realizations plus an always-available outside option. Each candidate
is mapped to the construction nodes it requires, so a multi-node candidate is
available only when every required node is included. A non-target outcome contributes

```text
ell = log P(y | target unavailable) - log P(y | target available)
```

to the negative stream when `ell > 0`, or to the positive stream when
`ell < 0`, after niche recoverability weighting. This recovers the old
counterfactual-choice result only as a small-mass approximation.

The v2 tests cover:

- return to the stated prior in the absence of evidence;
- gated-choice normalization;
- exact omission log likelihood ratios;
- a bounded repair-channel helper;
- illustrative licensed, preempted, starved, and conditionally winnerless
  regimes; and
- latent-lect, multi-node assembly prevalence, including cases where the
  product of marginal node rates is demonstrably wrong.

## Layout

```text
js/engine.js                 Legacy v1 Beta engine
js/sim.js                    Legacy v1 lab simulation layer
js/revised-engine.mjs        Current-paper v2 quantitative core
js/revised-sim.mjs           Discrete occasion simulator for v2
js/joint-likelihood.mjs      Toy conditional joint-likelihood evaluator
lab/src/                     Legacy browser-lab source
tests/fixtures/              Legacy Figure 4 fixtures
tests/run-revised-model.mjs  V2 regression contract
tests/run-joint-likelihood.mjs  Joint-likelihood regression contract
notes/                       Project and quantitative-model notes
```

## Build and test

```bash
make test    # legacy provenance tests plus v2 model-contract tests
make lab     # rebuild the legacy lab only
```

Do not present the legacy lab as a visualization of the v2 model until it has
been explicitly migrated and its new behavior reviewed.

## License

MIT (see `LICENSE`).
