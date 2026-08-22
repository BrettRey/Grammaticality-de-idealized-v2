# Quantitative Model Contract

## Purpose

This note separates three things that should not be conflated:

1. the paper's structural state theory;
2. the executable discrete-occurrence model in `js/revised-*.mjs`;
3. the executable conditional joint likelihood in `js/joint-likelihood.mjs`; and
4. a future scalable inference implementation for empirical estimation.

The v2 simulator is a transparent toy generative process. It can test whether
a stated combination of priors, candidate utilities, opportunity structures,
and evidence rules produces a claimed qualitative regime. It does not prove
the theorem-adjacent stochastic claims in the paper, estimate parameters from
data, or identify a construction inventory.

## Implemented Discrete Model

For a community, situation, construction node, and speaker, let
`z[i,k,c]` be a binary inclusion state. The present implementation uses
independent Bernoulli draws with fixed rates `theta[k,c]`. This is a default
for tests, not a claim that constructional inclusions are independent within a
speaker. A latent lect can replace the independent draws when co-licensing is
substantive; the v2 simulator now implements that extension.

For a latent-lect population, draw `lect[i]` with mixture weights `pi[l]` and
then draw node inclusion conditionally:

```text
lect[i] ~ Categorical(pi)
z[i,k,c] ~ Bernoulli(theta[lect[i],k,c])
```

For an assembly requiring nodes `A`, its population prevalence is then

```text
S_A = sum_l pi[l] product_(k in A) theta[l,k,c]
```

not generally the product of marginal node rates. The simulator tests both
correlated and anti-correlated lect mixtures to make this non-identifiability
visible rather than leaving it as a prose caveat.

At an opportunity in niche `n`, candidate `x` is available only if the speaker
includes every construction node in its independently specified node set
`nodes[x]`:

```text
a[x,z] = product_(k in nodes[x]) z[k]
P(y = x | z, n, c) = a[x,z] exp(U[x]) /
  (exp(U[out]) + sum_j a[j,z] exp(U[j]))
```

The outside option is always available. The one-candidate/one-node mapping is
only a default for simple tests, not the general interpretation. For a
non-target outcome, the model
compares its probability when a target is counterfactually available and when
it is not:

```text
ell = log P(y | Z[target] = 0, n, c) -
      log P(y | Z[target] = 1, n, c)
```

Recoverability `r[i]` routes `r[i] max(ell, 0)` to effective negative
evidence and `r[i] max(-ell, 0)` to effective positive evidence. A target
token is direct positive evidence. This is an evidence rule for the learner's
state summary; it is not asserted to be literal conjugate Bayes updating.

Each node stores a fixed baseline prior plus discounted effective evidence:

```text
a[t+1] = a0 + delta_m (a[t] - a0) + lambda_pos e_plus[t]
b[t+1] = b0 + delta_m (b[t] - b0) + lambda_neg e_minus[t]
```

This guarantees return to the stated prior when evidence stops. The resulting
single-node summaries are:

```text
C       = a / (a + b)
nu      = a + b
U_epi   = C (1 - C) / (nu + 1)
U_het   = C (1 - C) nu / (nu + 1)
```

`U_epi` is posterior uncertainty about the population rate. `U_het` is the
predictive variability of a randomly sampled speaker under the simple
Bernoulli population model. Assembly-level prevalence needs a joint model of
the inclusion vector, not just marginal node rates. The latent-lect extension
is the current executable joint model; more flexible within-lect dependence
would require an additional multivariate inclusion layer.

## What the Regime Tests Establish

The v2 test suite is deliberately narrow.

- A licensed target has repeated direct evidence and becomes high mean, high
  concentration.
- A preempted target has frequent counterfactually informative competitor
  outcomes and becomes low mean, high concentration.
- A starved target with no opportunities remains at its prior, rather than
  being classified as excluded.
- A winnerless candidate is low mean and low concentration only when the
  model supplies a low analogical prior and the outside option is nearly
  uninformative. No-evidence alone does not derive exclusion.
- A lect mixture can leave each node's marginal rate at 0.5 while producing
  high, low, or zero assembly prevalence. A precisely known 50/50 population
  has high evidence concentration but low decision confidence at a 0.5
  membership threshold.

Those are executable consistency checks. They are not evidence that any real
language has the parameterization used in the tests.

## Fit-Ready Joint Likelihood

A quantitatively complete empirical model should have one likelihood over all
observed channels rather than treating each channel as an independent score.
One workable hierarchy is:

```text
lect[i] ~ Categorical(pi)
z[i,k,c] ~ Bernoulli(logit^-1(mu[k,c] + alpha[lect[i],k,c]))

y[i,o] ~ Categorical(gated_softmax(a(z[i,.,c[o]]), U[.,n[o],c[o]]))
repair[i,o] ~ Bernoulli(repair_link(mis_set[i,o], Delta[d], footing[i,o], D[i]))
rating[i,r] ~ OrderedLogit(readout_mean(F[i,r], Phi[i,r]), cutpoints)
confidence[i,r] ~ OrderedLogit(readout_confidence(Phi[i,r]), confidence_cutpoints)
c[i,o] ~ Categorical(pi_c)
cues[i,o] ~ p(cues | c[i,o])
```

`js/joint-likelihood.mjs` now evaluates this structure for known contexts and
for either known or exactly marginalized speaker lect/inclusion states. It
returns separate log components for lect, inclusion, context, cue, production,
repair, rating, and confidence. Exact marginalization costs `O(L * 2^K)` for a
speaker with `L` lects and `K` nodes, so it is deliberately limited to toy
models and regression checks. It establishes that the channels can be composed
without treating repair as two independent observations or treating `q(c|cue)`
as a generative distribution.

Here `lect[i]` is optional but solves the within-speaker dependence problem:
related constructional nodes can co-occur within a lect without pretending
that their marginal rates determine assembly prevalence. The status target is
then computed from the distribution of complete licensed assemblies across
the modeled inclusion vectors. The learner or analyst posterior estimates that
target; it is not the target itself.

The judgment likelihood must use the cue-integrated status estimate and the
two read-out channels from Section 3. Production, repair, ratings, confidence,
and cue data are then conditionally related through shared latent inclusion
states and utilities. Repair is counted once through its likelihood; it must
not also be independently added as a second observation of the same event.
The situation posterior `q(c | cues)` is derived from the situation prior and
the cue likelihood; it is not itself a generative sampling distribution.

For an empirical fit, the generalized-Bayes effective-count filter should be
treated as either a transparent emulator of the full state-space posterior or
as a tempered likelihood with a calibrated scale. It should not be presented
as ordinary conjugate inference on corpus tokens, omissions, and repairs.

## Identification Requirements

Before fitting a target contrast, fix independently:

1. the conditioning partition `c`, niche coding `n`, candidate set, and
   construction inventory;
2. the counterfactual utility or `rho-star` norm on data disjoint from the
   licensing corpus;
3. recoverability and ascription coding for omissions;
4. an update-divergence measure from comprehension/common-ground probes, not
   from the repair rate later regressed on it;
5. an effective-evidence scale, calibrated against repeated-sampling variance
   or held-out longitudinal data; and
6. which observations inform a learner state versus which are only measured
   outputs of the state.

These restrictions prevent the model from absorbing a result through a
post-hoc niche, candidate, conditioning, or evidence-weight choice.

## Implementation Sequence

1. Keep the v2 JavaScript regression model small and executable.
2. Completed: add a latent-lect simulator and a multi-node assembly
   calculation.
3. Pre-register one target contrast with independently normed candidate
   utilities and a fixed coding protocol.
4. Completed for toy models: implement and test a conditional joint-likelihood
   evaluator with exact latent-state marginalization.
5. Implement a scalable version in a probabilistic programming system such as
   Stan or PyMC, with posterior predictive checks for production, repair,
   ratings, and confidence.
6. Only then use fitted results to evaluate the dispersion, repair-control,
   and re-licensing predictions.
