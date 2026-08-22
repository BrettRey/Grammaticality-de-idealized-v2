# Fable review: OVMG model and manuscript revision plan

The reviewer read the plan, the full manuscript, the companion-tool model
contract, code, sweep results, prior audits, and project records. It deliberately
did not read the Ox Alpha plan review. It made no file edits. Equations and
numerical claims below were independently recomputed by Fable in the homogeneous
mean-field closure using the sweep's declared base parameters.

## Summary

The plan's direction is right: defend the state theory, make every population-
dynamic claim conditional on a declared bridge, keep failing cells, narrow
moribundity, and freeze Lean. It nevertheless preserves a deeper problem in the
evidence filter and understates several analytic consequences of the declared
model.

Fable's principal findings were:

1. The omission-LLR pseudo-count update is not a consistent estimator of the
   population licensing rate it is said to estimate. At full population
   licensing the posterior mean has a ceiling well below one under the declared
   choice process.
2. The proposed mean-field crossing equation correctly classifies fixed points,
   but the one-dimensional return-rate formula is inaccurate because the
   evidence filter is a slow state variable.
3. The logistic slope-16 result is partly an endpoint-criterion artifact. The
   slope-8 cell is already bistable, with an upper attractor near 0.70, but fails
   the declared 0.8 cut.
4. The posterior-threshold response has a more principled interpretation than
   the plan allowed: its steepness is induced by posterior concentration, so it
   connects nonlinearity to opportunity, exposure, and memory.
5. The replicator cubic pins fixed points at zero and one, while every finite-
   steepness composed transition has interior attractors. It should be retired
   as the explanatory normal form or explicitly demoted to a large-concentration
   limit.
6. Under the declared prior-heterogeneity moribundity process, dispersion of
   evidence means analytically lags the mean at every normalized fraction.
   Concentration loss, not dispersion, is the derived leading indicator.

Verdict: **ACCEPT WITH REVISIONS**.

## 1. The evidence-filter ceiling

The manuscript adds a target token to the Beta positive count and adds a
non-target event's omission LLR
$\ell=-\log(1-\widetilde\rho^\star)$ to the negative count. In the homogeneous
stationary closure this yields

\[
C^*(\theta)=
\frac{a^0+K\widetilde\rho^\star\theta}
{\nu_0+K\widetilde\rho^\star\theta+
 \lambda^-L(1-\widetilde\rho^\star\theta)},
\]

where

\[
K=\frac{\lambda^+Np_{\rm obs}}{1-\delta_m},
\qquad
L=\frac{Np_{\rm obs}\ell}{1-\delta_m}.
\]

At $\theta=1$ and large effective evidence,

\[
C^*(1)\longrightarrow
\frac{\widetilde\rho^\star}
{\widetilde\rho^\star+lambda^-\ell(1-\widetilde\rho^\star)}.
\]

For $\lambda^-=1$, this is approximately 0.513 at
$\widetilde\rho^\star=0.1$, 0.591 at 0.5, and 0.796 at 0.9. The reason is that a
competitor token from a producer who includes the target is evidence about that
producer's inclusion, but adding its LLR as a negative Beta pseudo-count treats
it as if it were a Bernoulli failure of the population rate.

The sweep's analytic evidence-balance threshold is the $\theta$ at which this
distorted evidence mean equals 0.5. Calling $\lambda^-=0.5$ a calibrated scale
is therefore misleading unless a calibration target has been independently
declared.

This matters because the formal core calls $C$ a posterior mean of the
population rate and defines the licensed region near one. Under the current
filter, a fully licensed but optional candidate cannot reach that region unless
negative evidence is nearly suppressed.

Fable proposed two remedies:

- **Preferred:** use the exact nonconjugate one-step posterior and approximate
  it within the Beta family by moment matching. For a non-target event the
  posterior is a two-component mixture of
  $\operatorname{Beta}(a+1,b)$ and $\operatorname{Beta}(a,b+1)$, with weights
  determined by the target's counterfactual choice probability and the current
  belief. This preserves low information from a negligible outside-option
  comparison without treating the LLR as a literal failure count.
- **Cheaper:** explicitly re-scope $C$ as a generalized licensing score, provide
  the map between that score and $\theta$, and rewrite all status regions and
  adoption thresholds in score units.

Fable recommended the first route because the manuscript's licensing-versus-
selection factorization requires an estimate of population availability, not an
arbitrary score. It characterized this defect as fatal to the plan as written
but curable within its intended scope.

## 2. Mean-field diagnostic

For the full deterministic closure, fixed points solve the stationary evidence
equations together with $H(\theta)=\theta$. Fable recomputed the following
current-filter crossings and compared them with the finite sweep:

| Cell | Predicted fixed points | Observed low/high tails |
|---|---|---|
| mean, $\lambda^-=0.5$ | one crossing near 0.473 | 0.421 / 0.487 |
| logistic slope 8 | 0.027 / **0.582** / 0.703 | 0.025 / 0.710 |
| logistic slope 16 | 0.0004 / **0.524** / 0.975 | 0.000 / 0.970 |
| logistic slope 32 | 0 / **0.518** / 0.9995 | 0.000 / 0.999 |
| posterior threshold, $\lambda^-=0.5$ | 0 / **0.518** / 1 | 0 / 1 |

Bold entries are unstable. The crossing analysis explains the sweep more
directly than the endpoint criterion.

The plan's reduced stability multiplier

\[
|(1-\lambda)+\lambda H'(\theta^*)|<1
\]

is valid only when the evidence state is slaved to $\theta$. In the actual base
parameters, the filter's memory timescale is about 25 steps while inclusion
updates on a timescale of 12.5 steps. Numerical linearization of the full
$(\theta,a,b)$ map agreed on stability classification but not return rates. At
the slope-16 upper attractor, the full dominant eigenvalue was about 0.970,
versus 0.932 from the reduced formula; at the slope-8 upper attractor, about
0.996 versus 0.988.

The exact deterministic object should therefore be the full mean-field map and
its Jacobian. The one-dimensional crossing picture can locate equilibria and,
in the tested monotone cases, classify them, but it should not supply return or
escape times.

Other required qualifications:

- $C_i(\theta)$ and $\nu_i(\theta)$ are stationary filter responses whose
  values depend on opportunity, observation, retention, evidence weights,
  counterfactual choice, and omission informativeness;
- averaging a steep response over heterogeneous speakers is not the same as
  applying it to average evidence;
- utilities, other gates, omission informativeness, and repair terms are frozen
  in the one-dimensional closure;
- finite-population attractors are metastable;
- finite-steepness responses generally make boundary attractors interior; and
- a latent-lect model requires a per-lect closure or an explicit approximation.

## 3. Source of nonlinearity

The drafted logistic hides the result in its free slope unless that slope is
measured independently. Fable recommended making the posterior-threshold family
canonical instead:

\[
h(C,\nu;q)=P(\theta\ge q\mid\mathcal D).
\]

This can be interpreted as posterior sampling over an independently motivated
adoption criterion. Its effective steepness near $q$ grows with
$\sqrt{\nu^*}$, while

\[
\nu^*=\nu_0+\frac{\text{evidence inflow}}{1-\delta_m}.
\]

The condition for separated regimes therefore becomes a condition on
opportunity, observation, memory, and adoption costs--quantities already present
in the theory--rather than on an unconstrained slope knob. The adoption
criterion $q_\kappa$ must still be fixed from coordination or switching costs
independently of the population outcome.

The logistic can remain as a reduced form, with its slope interpreted as
regularization strength and estimated in an independent learning task. The
manuscript must distinguish the causal adoption criterion $q_\kappa$ inside the
population transition from the judge's read-out threshold $\tau(c)$, which does
no constitutive work.

## 4. Cubic normal form

The current replicator cubic multiplies its drift by $\theta(1-\theta)$, thereby
making zero and one exact fixed points. The composed finite-steepness transition
has interior attractors instead. Fable recommended replacing the cubic as the
explanatory normal form with the $H(\theta)$-against-the-diagonal crossing
analysis, optionally using a cusp normal form locally near the fold. The
replicator cubic could remain only as a clearly labelled high-concentration
limit or historical comparison.

## 5. Scope-audit corrections

- The linear response has one crossing under the declared closure; present this
  as an analytic result rather than a grid observation.
- Slope 8 is already bistable. It fails the declared endpoint criterion because
  its upper attractor is near 0.70, below the 0.8 cut. Preserve the criterion and
  call slope 16 only the first passing value in that operational grid.
- Opportunity, memory, and outside-option effects follow through the stationary
  evidence mean and concentration. The analytic balance should carry the
  explanation, with the finite sweep as confirmation.
- The inclusion-only perturbation retains the slow evidence state at its old
  attractor. It checks the return of the fast inclusion state, not response to
  an evidence-side perturbation. The middle-state arms are the more relevant
  basin test; evidence shocks remain untested.
- The repair intervention flips an outcome against a baseline already driven
  downward by the default evidence weight. It remains a wiring check and need
  not appear in the main manuscript.

## 6. Moribundity

With zero new evidence after the opportunity drop, speaker means can be written
in the form

\[
C_{i,t}=w_t m_i+(1-w_t)C_E.
\]

Normalized mean movement is proportional to $w_t$, whereas normalized
between-speaker variance movement from heterogeneous priors is proportional to
$w_t^2$. Since $0<w_t<1$, variance lags mean movement at every normalized
fraction. The sweep's ordering is therefore an analytic consequence of the
declared prior-heterogeneity process.

Concentration loss occurs sooner than either. Fable's recomputation found that
after 25 post-drop steps, roughly 64% of the excess concentration had vanished
while the mean had moved only about 1.4% of its eventual distance. The robust
leading indicator should therefore be reduced evidence confidence, greater
test--retest instability, or another operational measure of falling
concentration. Dispersion-leading decline remains possible only under additional
faster heterogeneity, such as cohort replacement, unequal opportunity loss
across networks, or heterogeneous retention.

## 7. Scope and ranked changes

Necessary now:

1. add an evidence-filter repair or explicit score re-scope;
2. make the full mean-field map and its fixed points primary, with the reduced
   crossing diagnostic carefully qualified;
3. use a posterior-threshold response with concentration-derived steepness as
   the canonical candidate and treat the logistic as a reduced form;
4. correct the slope-8 interpretation and promote analytic results over the
   operational grid;
5. reformulate moribundity around concentration loss;
6. retire or demote the endpoint-pinned cubic;
7. reconcile $q_\kappa$ with the non-constitutive read-out threshold $\tau(c)$;
   and
8. rebalance the abstract, introduction, predictions, limitations, and
   conclusion accordingly.

Defer networks, empirical fitting, a shared-latent likelihood, cohort modelling,
stationary distributions, escape times, browser migration, and further Lean.

Fable's answers to the three plan decisions were:

1. Make posterior-threshold adoption canonical because its steepness is derived
   from concentration; keep the logistic only as a reduced form.
2. Put the analytic crossing argument in the main text and the finite grid in a
   short appendix.
3. Retain moribundity as a concentration-first prediction; retain
   dispersion-leading only as a conditional hypothesis with the needed
   structures named.

**ACCEPT WITH REVISIONS**
