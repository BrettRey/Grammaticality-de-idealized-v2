# Independent review: OVMG model and manuscript revision plan

Reviewed against `notes/model-and-manuscript-revision-plan-2026-08-22.md`,
`main.tex` (including `section3.tex`), the companion OVMG tools, and the
closed-loop follow-up audit. No files were edited by the reviewer.

## 1. Right layer repaired?

Yes, with one caveat. The plan correctly locates the defect at the
learner-to-population bridge and at claim calibration, not in the state
architecture. The formal core survives scrutiny: status/estimate separation,
the variance decomposition, the LLR omission rule, and constrained reassignment
are sound, and the plan leaves them intact. The prior defect was that the cubic
was presented as if the Beta filter entailed it; the manuscript now concedes it
is stipulated, and the plan builds the honest bridge diagnostic instead. That
is the right layer.

The caveat: the plan's own failure-condition table names the residual conceptual
risk correctly but does not fully discharge it. Even with the mean-field
diagnostic added, the emergence claim stands or falls on whether the
nonlinearity in $h_\kappa$ has a source outside the phenomenon it explains. The
plan flags this but its remedy, the independently interpreted logistic, is only
partially adequate. The deepest defect is converted into an explicit open
problem rather than solved. That is acceptable at this stage provided the
manuscript says exactly that.

## 2. Mean-field crossing/stability diagnostic

The algebra is correct at the stated closure level. Under homogeneous speakers
with common $\lambda$, independent observation, and $\bar\lambda$ read as that
common value, the expected-prevalence map is
$\theta_{t+1}=(1-\lambda)\theta_t+\lambda H(\theta_t)$; the fixed point satisfies
$H(\theta)=\theta$ and local stability requires
$|(1-\lambda)+\lambda H'(\theta^*)|<1$. Three crossings of the diagonal with
alternating stability do support two attracting regions flanking an unstable
interior state. This matches the composition implemented in the closed-loop
simulator.

Missing qualifications, in order of importance:

1. **Endogenous evidence flow.** $H(\theta)=E_i[h_\kappa(C_i(\theta),\dots)]$
   correctly treats each $C_i$ as a function of $\theta$, but the stability
   condition is correct only if $H'$ includes the derivative of the evidence
   flow with respect to $\theta$. That dependence is what makes separation
   possible. If the diagnostic is evaluated with the evidence map frozen at a
   reference regime, it inherits the cubic's frozen-flow caveat and must say so.
2. **Concentration slaving.** Because $h_\kappa$ takes $\nu_{i,t}$ as well as
   $C$, a one-dimensional map in $\theta$ is valid only if $\nu$ equilibrates
   faster than $\theta$ or is treated as a slaved variable.
3. **Homogeneous closure limits.** With heterogeneous $\lambda_i$ or dispersion
   in $C_i$, the linearization gains Jensen/covariance terms; a steep $h$ makes
   the average-of-$h$ versus $h$-of-average gap material. The manuscript should
   point forward to that limitation.
4. **Deterministic versus stochastic.** Map stability does not imply basin
   retention at finite population size. The plan's finite-horizon labelling
   handles this and should remain.

## 3. The smooth logistic response

Recommendation: **REVISE**, not keep as drafted, and not omit.

As proposed, $\sigma(\gamma_\kappa[C-q_\kappa])$ risks hiding the result in
$\gamma$: the sweep's first passing value was slope 16, at which the smooth
response is nearly a step. If $\gamma$ is free, the plan's own inversion warning
applies verbatim.

A genuine rescue is available. A shallow population-level response is what
threshold heterogeneity predicts; a steep one requires aligned thresholds
across speakers, and that alignment itself demands explanation. Thus
$\gamma_\kappa$ is independently interpretable only if it is derived rather
than supplied: write it as the reduced form of a stated within-population
distribution of individual thresholds $q_i$, with steepness determined by
$\operatorname{Var}(q_i)$ relative to the range of $C$, and require the threshold
and switching/coordination costs to be estimated from data disjoint from the
outcome. On that reading the logistic earns its place as a canonical candidate.
Without that derivation, omit it and state only the crossing/stability
conditions. The slope-16 result should be reported as near-threshold behaviour.

## 4. Cubic as conditional normal form

The cubic remains useful. It supplies the paper's vocabulary of separatrix,
actuation-as-crossing, S-curves, and the operator/style parameter statement. It
should be retained only if it is consistently labelled a conditional normal
form, is never used as empirical warrant, and carries its frozen-flow and
outside-option caveats into every later use. The plan's tripwire--retire it if
its sign structure fails to match the composed transition in any declared
regime--is appropriate.

## 5. Calibration of downstream claims

- **Simulation:** the proposed scope audit is accurate but should include the
  analytic expected-evidence-flow balance threshold. That explains why cells
  pass or fail rather than merely recording their outcome.
- **Moribundity:** the two-level split is right, but the direct comparative
  static should say that no opportunity returns concentration to baseline,
  whereas falling but nonzero opportunity yields partial loss. The stress test
  measured dispersion of speaker evidence means, while the retained hypothesis
  concerns judgment dispersion. The manuscript must carry that caveat.
- **Repair:** wiring check only, with no maintenance or control warrant. This is
  correctly calibrated.
- **Stationarity:** correctly retained as an open proof obligation and deferred.

## 6. Projectibility-first essentials

The essential changes are:

1. create the claim ledger with named bearers before revising prose;
2. separate projections of the state architecture from hypotheses requiring the
   dynamics bridge;
3. retain the firewall among stability, maintenance, and control; and
4. make field-relative scope depend on independently identified conditioning
   states, not a post-hoc sympathetic choice of $c$.

No proposed change creates a trivial projection or unsupported world-side
upgrade as written; the risk lies in execution drift, which the checkpoints
address.

## 7. Scope at this submission stage

The scope is appropriate. Necessary now are the ledger, bridge diagnostic,
scope-audit table, moribundity recalibration, headline-prose rebalancing, and
verification. Networks, the shared-latent likelihood, stationarity, cohort
replacement, empirical estimation of $h_\kappa$, and browser migration should
remain deferred. If space is tight, the candidate logistic can move to an
appendix while the crossing/stability conditions remain in the main text.

## 8. Five changes to the plan, ranked

1. Qualify the mean-field diagnostic by stating whether $H'$ includes endogenous
   evidence-flow dependence and by stating the concentration-slaving condition.
2. Derive rather than supply logistic steepness through a within-population
   threshold distribution and independently measurable costs.
3. Add the analytic evidence-balance threshold to a compact main-text scope
   audit.
4. Close the moribundity measurement gap by distinguishing evidence-mean
   dispersion from judgment dispersion.
5. Make the ledger strictly upstream of every abstract, prediction, or
   conclusion edit.

## Classification

- **Fatal objections:** none.
- **Material revisions:** items 1, 2, and 4 above, plus an exact statement of the
  opportunity/concentration comparative static.
- **Optional refinements:** analytic-balance row in the audit table; appendix
  fallback for the logistic; cosmetic cleanup in the companion tests; tighter
  wording for the repair wiring check against a collapsing baseline.

On the plan's three decisions: keep the logistic only in the derived-steepness
form; put a compact scope-audit box in the main text; retain the conditional
moribundity hypothesis as a registered, structure-specifying hypothesis while
keeping concentration loss as the sole direct model consequence.

**ACCEPT WITH REVISIONS**
