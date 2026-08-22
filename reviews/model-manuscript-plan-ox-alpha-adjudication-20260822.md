# Ox Alpha adjudication of the Fable plan review

Ox Alpha independently recomputed the new Fable claims from
`revised-engine.mjs`, `closed-loop-sim.mjs`, and the declared sweep parameters.
It did not defer to either earlier review and made no project edits.

## Confirmed findings

### Evidence-filter ceiling

With

\[
p=P(\text{target}\mid\text{included})=
\frac{1}{2+e^{-4}}\approx0.4955,
\qquad
\ell=\log\frac{2+e^{-4}}{1+e^{-4}}\approx0.6841,
\]

the stationary pseudo-count mean under the base opportunities, observation
probability, and retention is

\[
C^*(\theta)=
\frac{1+Kp\theta}
{2+Kp\theta+K\lambda^-\ell(1-p\theta)},
\qquad K=180.
\]

The balance thresholds reproduce the sweep exactly:
$\theta^*=0.51442$ for $\lambda^-=0.5$ and $0.81987$ for $\lambda^-=1$.
At full licensing, the corresponding ceilings are approximately 0.738 and
0.588. The issue is a genuine typing/consistency defect: the exact non-target
likelihood is affine in $\theta$, whereas the pseudo-count update applies a
power of $(1-\theta)$. Generalized Bayes does not justify calling the resulting
quantity a posterior mean of $\theta$ under the declared observation model.

### Preferred bounded repair

Moment matching the exact one-event nonconjugate posterior back into the Beta
family is a sound, bounded repair worth placing in the plan. A batch of $m$
events has at most $m+1$ mixture components under fixed utilities. Required
implementation qualifications are:

- discount the existing state first, then form and match the posterior mixture;
- keep per-speaker observation counts explicit;
- replace the old analytic balance threshold with numerical root finding; and
- regenerate the complete sweep, since cells may change.

An explicit re-scope of $C$ as a generalized licensing score is an acceptable
fallback if the likelihood-consistent repair proves disproportionate, but it
would require rewriting the state regions and the map from score to population
rate.

### Slope-8 bifurcation

The current slope-8 logistic cell has mean-field fixed points near
0.027 / **0.582** / 0.703, with the middle point unstable. It is bistable even
though its upper attractor lies below the declared 0.8 endpoint cut. Slope 16 is
only the first value in the tested grid that passes the operational endpoint
criterion; it is not the first bifurcating slope.

### Canonical response

The posterior-threshold response should be preferred as the canonical candidate
because its effective curvature scales with posterior concentration, hence with
opportunity, observation, and memory, instead of a free logistic slope. Its
criterion $q_\kappa$ remains a categorical decision commitment and must be
motivated or estimated independently from switching or coordination costs. The
logistic can remain as a reduced form whose slope is interpreted through an
independent regularization measure.

### Normal form

The endpoint-pinned replicator cubic materially mismatches every
finite-steepness composed transition, whose attracting states are interior.
Replace its explanatory role with the full mean-field map and an
$H(\theta)$-versus-diagonal crossing analysis. Retain the cubic only as a
clearly labelled large-concentration limit, if useful at all.

### Moribundity

For the declared prior-heterogeneity process,

\[
C_{i,t}=w_t m_i+(1-w_t)C_E.
\]

Normalized variance movement is the normalized mean movement multiplied by a
factor strictly below one, so variance necessarily lags mean movement. Loss of
excess concentration precedes both by a wide margin. Concentration loss is the
robust preregistrable precursor; dispersion-leading decline requires additional
heterogeneity structure.

### Dynamic timescale

Direct iteration confirmed the slow-state issue. At the upper attractor, the
full map's dominant eigenvalue is about 0.969 for slope 16 and 0.995 for slope
8, whereas the reduced formula gives about 0.931 and 0.984. The full
mean-field map and Jacobian should be the deterministic object of record. The
one-dimensional crossing picture can locate and classify equilibria in the
tested monotone cases, but it should not be used for return-time claims.

## Required changes to the plan

1. Make evidence-filter repair or explicit re-scoping a blocking stage before
   the bridge revision.
2. Make the full mean-field map and Jacobian primary; use the crossing diagnostic
   as a qualified reduction.
3. Distinguish slope-8 bistability from slope-16 endpoint-criterion passage.
4. State the moribund variance lag analytically and promote concentration loss.
5. Demote and replace the cubic's explanatory role.
6. Make posterior-threshold adoption the canonical candidate, with independent
   identification of $q_\kappa$, and reconcile it with the non-constitutive
   read-out threshold $\tau(c)$.

No substantive Fable claim was refuted. Exact percentages and ceiling examples
should be tied to declared parameters, and the ordering results should be stated
analytically rather than through one numerical trajectory.

**Verdict: adopt Fable's ranked revisions, as amended. ACCEPT WITH REVISIONS.**
