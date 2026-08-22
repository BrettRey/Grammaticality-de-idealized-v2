# OVMG model and manuscript revision plan

<!-- Revised 2026-08-22 after independent Fable and Ox Alpha review and focused Ox adjudication. -->

## Decision

Prepare the paper as a defensible state theory with a deliberately conditional
dynamics module. Preserve the structural architecture, but repair the
evidence-state update before completing the learner-to-population bridge. The
current omission pseudo-count is not consistently typed as a posterior update
for the population rate it is said to estimate; bridge work built on it would
inherit that defect.

The target claim, conditional on that repair, is:

> OVMG specifies a projectible population licensing profile and a coherent
> micro-to-macro transition. Under an independently motivated adoption
> criterion and declared opportunity, observation, memory, and evidence-flow
> conditions, the composed transition can have separated attracting regions.
> Those conditions are hypotheses to estimate, not consequences of Beta
> updating alone.

The revision will replace the endpoint-pinned cubic as the explanatory device
with the fixed points and Jacobian of the composed mean-field map. The cubic may
remain, if useful, only as a clearly labelled large-concentration limiting
idealization. Concentration loss, not dispersion-leading decline, becomes the
robust moribundity prediction.

## Independent review and adjudication

Fable and Ox Alpha independently returned **ACCEPT WITH REVISIONS**. They agreed
that the state architecture is worth preserving, projectibility is structural,
Lean should remain frozen, repair simulations provide no maintenance or control
warrant, and the current emergence and moribundity language needs narrowing.

The first Ox review recommended retaining a qualified cubic and deriving a
logistic slope from threshold heterogeneity. Fable then identified a deeper
filter-consistency problem, distinguished slope-8 bistability from the 0.8
endpoint criterion, proposed concentration-derived posterior-threshold adoption,
and challenged the cubic's fixed endpoints. A focused Ox recomputation confirmed
those substantive findings. This plan adopts the following adjudication:

- repair or explicitly re-scope the evidence filter before revising the bridge;
- prefer a likelihood-consistent, moment-matched Beta approximation;
- make the full mean-field map and its Jacobian primary;
- use posterior-threshold adoption as the canonical candidate, while treating
  its criterion as an independently warranted substantive assumption;
- keep the logistic only as a reduced form tied to independently measured
  regularization;
- replace the cubic's explanatory role with a crossing analysis;
- put that analytic argument in the main text and the finite sweep in a short
  technical appendix; and
- make concentration loss the primary moribund precursor, with dispersion-
  leading decline retained only under named additional structures.

The preserved reviews are:

- reviews/model-manuscript-plan-fable-20260822.md;
- reviews/model-manuscript-plan-ox-alpha-20260822.md; and
- reviews/model-manuscript-plan-ox-alpha-adjudication-20260822.md.

## Goals and constraints

The revision should:

1. keep the constitutive distinctions among coverage, compatibility,
   saturation, licensing, and subjective read-out;
2. keep population status separate from speaker and analyst estimates;
3. make the evidence update consistent with the quantity it claims to estimate,
   or explicitly type it as a score rather than a posterior mean;
4. retain projectibility as the paper's organizing payoff;
5. make every population-dynamic conclusion conditional on a declared bridge;
6. preserve negative and criterion-sensitive computational results as scope
   information;
7. leave a clear empirical programme without claiming that its parameters have
   already been estimated; and
8. reach submission-ready proportionality without building a networked,
   shared-latent empirical model at this stage.

The Lean development remains frozen. It machine-checks structural properties of
the state architecture, but the live defects are model specification and claim
typing. The unique-crossing and moribund-ordering lemmas are definition-complete
but elementary enough that formalizing them would add little at this stage.

## Load-bearing assumptions and failure conditions

| Assumption | What would make it false | Consequence |
|---|---|---|
| The state architecture is independently useful. | Its profiles license no held-out predictions beyond the diagnostics used to assign them. | Recast the paper as a decomposition, or add genuinely non-trivial projection targets. |
| A likelihood-consistent bounded filter is available. | Moment matching fails against exact quadrature, remains materially biased, or destroys low-information outside-option behaviour. | Re-scope C as a score and publish its map to theta; if the projections then become uninterpretable, remove the dynamics claim. |
| A modest bridge completion is enough. | The claims require networks, shared latent judgments, or fitted social parameters to be intelligible. | Remove the emergence claim rather than sketching an unevaluable mechanism. |
| The adoption criterion is independently motivated. | q-kappa is chosen only because it produces the desired population separation. | Report separation as a phenomenological possibility, not an explanation. |
| The reduced crossing picture represents the full map. | Its fixed points or stability classifications disagree with the full map after filter repair. | Use only the full map and Jacobian. |
| Opportunity loss robustly lowers concentration. | The repaired baseline-preserving update does not yield that comparative static. | Correct the recurrence or withdraw the moribundity result. |
| Dispersion-leading decline needs additional structure. | A valid derivation shows that opportunity loss and prior heterogeneity suffice. | Restore the stronger prediction with its actual sufficient conditions. |

The strongest inversion remains visible throughout: a threshold model can
reproduce categoricality while explaining nothing if its threshold is selected
from the categorical outcome. Concentration-derived curvature removes a free
steepness parameter; it does not independently warrant the adoption criterion.

## Work plan

### 1. Establish the claim ledger and freeze the baseline

- Record the current manuscript and tool-repository revisions, pre-repair sweep
  hash, and passing test totals before editing.
- Classify each formal claim as a definition, exact identity, analytic
  consequence, modelling assumption, finite-horizon computational result,
  empirical projection, or open proof obligation.
- Name the bearer of every headline quantity: population rate, speaker belief,
  analyst estimate, evidence score, judgment read-out, or simulation state.
- Keep the legacy browser lab out of the evidential chain.
- Treat the current sweep as a diagnostic of the pre-repair process, not as a
  result ready for the manuscript.

Checkpoint: no abstract, prediction, or conclusion sentence is revised before
its bearer and evidential status exist in the ledger.

### 2. Repair the evidence update before bridge work

The present model observes target choice with probability proportional to
theta times rho-tilde-star. A non-target event therefore has a likelihood affine
in theta; raising one minus theta by an omission LLR is a different likelihood.
Under the present pseudo-count rule, a fully licensed population has a
stationary evidence-mean ceiling around 0.588 at the default negative weight and
0.738 at weight 0.5 in the declared base cell. That is incompatible with typing
C as a posterior mean of theta and defining the licensed region near one.

Preferred repair:

1. derive the exact one-event posterior for target and non-target observations;
2. retain the non-target posterior's two-component Beta-mixture form;
3. apply baseline-preserving discount before the new-window likelihood;
4. moment-match the resulting mixture back to a Beta by mean and variance;
5. derive the batched form, keeping per-speaker observation counts explicit;
6. compare the approximation with exact grid quadrature across broad prior,
   choice-probability, memory, opportunity, and population-rate ranges; and
7. verify that negligible counterfactual choice remains nearly uninformative,
   winnerless cells do not become preempted gaps, and posterior means recover
   known stationary population rates up to declared prior shrinkage.

The omission LLR remains useful as an event-informativeness identity. It should
not be inserted as a literal Beta failure count unless a separate
generalized-Bayes target and calibration are declared.

Fallback if moment matching fails: call C a generalized licensing score,
provide the score-to-theta mapping for every claim that uses it, state the
calibration target for any power weight, and rewrite the licensed, excluded,
unsettled, and heterogeneous regions in the correct units. This is less
attractive because the licensing-versus-selection factorization needs an
availability estimate.

Blocking checkpoint: do not revise the adoption response, regenerate the sweep,
or rewrite the manuscript until the repaired filter passes exact-posterior and
stationary-recovery tests, or the score fallback has been explicitly adopted.

### 3. Complete the bridge only to the level the argument needs

Retain the speaker transition:

\[
P(z_{i,t+1}=1)=(1-\lambda_i)z_{i,t}+
\lambda_i h_\kappa(C_{i,t},\nu_{i,t},\xi_{i,t},c).
\]

Make the deterministic mean-field state

\[
X_t=(\theta_t,a_t,b_t)
\]

or its equivalent theta/C/nu state, with a declared update map
from X-t to X-(t+1). Fixed points solve the stationary evidence equations
together with the inclusion equation. Local stability is determined by the
spectral radius of the full Jacobian:

\[
\rho(J_F)<1.
\]

This is the deterministic object of record.

Use the reduced response

\[
H(\theta)=E_i[
  h_\kappa(C_i^*(\theta),\nu_i^*(\theta),\xi_i,c)
]
\]

as a secondary equilibrium diagnostic. Crossings of H(theta) and the diagonal
locate candidate fixed points when the stationary evidence manifold is well
defined. A reduced multiplier such as

\[
\left|(1-\lambda)+\lambda H'(\theta^*)\right|<1
\]

may classify monotone one-dimensional reductions but must not supply return or
escape times when evidence is not a fast variable. Heterogeneous speakers,
latent lects, endogenous utilities, changing gates, and finite-population noise
remain explicit closure limits.

Use as the canonical candidate response

\[
h_\kappa(C,\nu;q_\kappa)
=P(\theta\geq q_\kappa\mid C,\nu).
\]

Interpret it as posterior sampling against an adoption criterion. Its curvature
is induced by concentration, hence by opportunity, observation, retention, and
evidence informativeness. The criterion q-kappa must be tied to independently
measured switching or coordination costs and fixed before the population outcome
is inspected.

Keep

\[
\sigma\!\left(\gamma_\kappa[C-q_\kappa]\right)
\]

only as a reduced form, with gamma-kappa estimated as regularization strength
in an independent learning task or derived from a declared distribution of
individual criteria. A free steepness knob is not explanatory.

Distinguish q-kappa, a causal adoption criterion inside the transition, from
tau(c), the judge's loss-sensitive read-out threshold. The latter remains
non-constitutive; the former is a substantive dynamics assumption.

Replace the cubic as the primary explanatory normal form with an
H(theta)-against-the-diagonal crossing figure and the full-map analysis. If the
cubic is retained at all, label it as an endpoint-absorbing,
large-concentration limit and do not use it as a source of warrant.

Checkpoint: a reader can identify which assumption supplies the criterion,
which observed quantities supply curvature, which approximation locates the
fixed points, and what would defeat each.

### 4. Regenerate and reinterpret the computational scope audit

After the filter repair, regenerate every closed-loop result. Do not assume that
the current grid's pass/fail pattern will survive.

The new audit should:

- calculate stationary evidence responses, fixed points, and the full Jacobian
  before interpreting stochastic trajectories;
- compare proportional, logistic reduced-form, and posterior-threshold
  responses without tuning any family to a preferred result;
- distinguish **bistability** from **endpoint concentration**;
- report attractor locations and separatrices, not only membership in low/high
  bins;
- retain the operational endpoint criterion and report its false negatives;
- separate mid-state initialization from inclusion-only perturbations that leave
  the slow evidence state unchanged;
- add evidence-side shocks if return-to-attractor language is retained;
- vary opportunity, observation, memory, outside-option mass, adoption rate,
  and independently interpretable response parameters;
- retain all failing cells; and
- omit the programmed repair comparison from the main evidential table. It may
  remain in the tools as a wiring check.

For the pre-repair process, record only the diagnostic lesson: slope 8 already
has two attracting fixed points near 0.027 and 0.703, while slope 16 is merely
the first tested value passing the declared 0.2/0.8 endpoint criterion. Retire
the phrase "calibrated negative-evidence scale" because no independent
calibration target fixed that weight.

Put the analytic map and crossing figure in the main text. Put the finite-
population grid, exact inputs, seeds, criteria, and hash in a short technical
appendix or companion supplement. Label the exercise an existence and scope
audit, not an empirical fit or stationary-distribution result.

Checkpoint: every simulation sentence remains true if "English grammar" is
replaced by "this declared finite-population process."

### 5. Recalibrate the moribundity claim

State three levels separately.

- **Direct consequence:** baseline-preserving discount makes reduced opportunity
  lower excess concentration. Zero evidence returns it to baseline; reduced but
  nonzero inflow yields partial loss.
- **Analytic ordering in the current prior-heterogeneity arm:** if

  \[
  C_{i,t}=w_t m_i+(1-w_t)C_E,
  \]

  normalized movement of between-speaker variance is strictly smaller than
  normalized movement of the mean because its weight is quadratic in w-t.
  Prior heterogeneity alone therefore makes dispersion lag, not lead.
- **Conditional research hypothesis:** dispersion can lead only when a faster
  heterogeneity source—cohort replacement, unequal network opportunity loss,
  heterogeneous retention, or a specified judgment mapping—makes individual
  divergence grow while the mean initially remains stable.

Promote falling evidence confidence, increasing test–retest instability, or
another independently operationalized measure of concentration loss as the
primary preregistrable precursor. The existing stress test measures dispersion
of speaker evidence means, not judgment dispersion, and must be described that
way.

Remove "corollary," "novel leading indicator," and the unqualified
"dispersion leads; means lag" from the abstract, dynamics section, predictions,
actuation discussion, and conclusion.

Checkpoint: concentration loss, mean movement, evidence-mean dispersion, and
judgment dispersion remain distinct bearers throughout.

### 6. Rebalance the manuscript around the revised contribution

Make targeted changes after Stages 2–5 settle the mathematics.

- **Abstract:** foreground the state architecture and non-trivial projections;
  describe separated regimes as conditional; make concentration loss the
  moribund precursor.
- **Introduction and roadmap:** say that the dynamics module supplies candidate
  sufficient conditions, not a generic derivation of categoricality.
- **Formal core:** preserve the ontic/epistemic separation, but correct the
  typing and interpretation of the evidence state wherever C is called an
  estimate of theta.
- **Dynamics:** insert the repaired update, full map, crossing diagnostic,
  canonical adoption response, and revised moribundity result. Replace or demote
  the cubic.
- **Predictions:** distinguish projections of the state architecture from
  hypotheses requiring the dynamics bridge. Give each a source, target bearer,
  population, conditions, timescale, tolerance, and failure result where a
  confirmatory design is proposed.
- **Repair:** keep stabilization, maintenance, and corrective control separate.
  The simulation contributes no new warrant for maintenance or control.
- **Limitations:** name criterion identification, effective evidence scale,
  network structure, shared-latent observation model, finite-population
  stationarity, and escape times as open work.
- **Conclusion:** claim an architecture plus testable conditional mechanisms,
  not a completed derivation of grammatical categoricality.

Correct local language that risks treating field-relative scope as truth:
different speakers can be correct relative to independently identified
conditioning states; post-hoc selection of a sympathetic state does not rescue a
failed projection.

Checkpoint: projectibility remains structural. The payoff is what the profile
licenses us to expect, while stability, causal order, maintenance, and control
retain separate warrants.

### 7. Keep larger improvements as an explicit sequel

Do not add these before the present submission unless the bounded repair shows
that the core argument cannot stand without them:

- networked exposure and speaker interaction;
- empirical estimation of adoption criteria, response regularization, evidence
  scales, and outside-option utilities;
- a genuinely shared-latent likelihood for production, repair, ratings, and
  confidence;
- cohort replacement and structured heterogeneity for moribund contrasts;
- stationary-distribution and escape-time analysis;
- belief-dependent evidence weighting as a possible additional source of
  nonlinear lock-in; or
- a new browser visualization.

These form the dynamics paper or empirical follow-up. The present paper should
state the interfaces they must satisfy.

### 8. Verification and stopping rule

After implementation and editing:

1. compare the repaired approximate posterior with exact quadrature and the
   stationary population rate across the declared test grid;
2. run all companion-tool regression tests;
3. regenerate the closed-loop sweep twice and record the new deterministic hash;
4. recompute fixed points and full-map Jacobians independently of the simulator;
5. build the paper with latexmk and check for undefined references;
6. run bibliography validation, house-style review, and a fresh
   projectibility-first audit;
7. confirm that the Lean files are unchanged and their existing build passes;
8. obtain one final adversarial review focused on filter typing, unconditional
   emergence, threshold circularity, moribund ordering, maintenance, and control;
   and
9. stop when every headline claim traces to a definition, derivation,
   computational result, cited evidence, or explicitly labelled hypothesis.

## Acceptance criteria

The revision is complete when:

- C is either a validated approximation to the posterior mean of theta or
  consistently labelled a score with an explicit map to theta;
- a fully licensed optional form can reach the model's licensed region under its
  declared observation process;
- no passage implies that Beta filtering alone generates bimodality;
- the adoption criterion and source of response curvature are separately stated
  and independently testable;
- the full mean-field map, not a fast-filter reduction, governs stability and
  return claims;
- the cubic has been replaced or consistently demoted to a limiting
  idealization;
- bistability is not conflated with passage of an endpoint-concentration cut;
- simulations are reported with their finite-horizon, criterion, and parameter
  scope;
- repair simulation remains outside the warrant for maintenance or control;
- concentration loss is separated from mean change, evidence-mean dispersion,
  and judgment dispersion;
- projective claims identify what is projected, for whom, under what conditions,
  and what failure would mean;
- no world-side upgrade from stability to causal order, maintenance, or control
  is made without separate evidence; and
- the paper, tools, and formalization records agree about what has and has not
  been established.

## Points for Roughdraft review

The plan recommends the likelihood-consistent moment-matched filter, with score
re-scoping only as a fallback. It also recommends replacing the cubic's
explanatory role, using posterior-threshold adoption as the canonical candidate,
placing the analytic crossing argument in the main text, and retaining the
finite grid in a technical appendix. Comments on those four commitments are the
most consequential at this checkpoint.
