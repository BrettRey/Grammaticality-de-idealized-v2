# Ox Alpha final refutation audit — recomputed findings

This is a normalized local record of the visible response, not a raw stdout
capture; equations were converted to plain text and the incorporated cleanup
items are identified explicitly.

Run: `stealth/ox-alpha`, high effort, 19,170 input tokens, 8,563 output tokens,
202.4 seconds, no fallback. The model received only the line-numbered excerpts
preserved in `input-final-repair-audit.txt`.

## Issue 1: rho-star / rho-tilde-star and the exact omission LLR — CLOSED

With

```text
D_0 = exp(U(outside)) + sum(non-target gated weights),
```

the gated softmax gives

```text
P(y | Z_x = 1) / P(y | Z_x = 0)
  = D_0 / (D_0 + exp(U(x)))
  = 1 - rho-tilde-star.
```

Hence `ell = -log(1-rho-tilde-star) >= 0`. Removing the positive omission
channel is a theorem of the fixed-utility, fixed-other-gates softmax. The stated
recovery conditions for the older `N * rho-star` approximation are jointly
sufficient: near-complete omission, reliable niche identification, negligible
outside mass, matched gates, and small target mass.

The audit noted two minor clarifications. First, multiple assemblies for one
surface candidate must be aggregated before the candidate-level softmax.
Second, outside-option evidence is small because the target's full-choice mass
is small, not merely because the outside option is fixed. Both clarifications
were incorporated after the run. A dangling positive-part notation was also
removed.

## Issue 2: ontic status versus estimates — CLOSED

`S_t^theta` is a function of the population state and prior population history;
`S-hat_t^(r)` integrates it under bearer `r`'s posterior. Bearer discipline now
holds at the audited sites: `G_t` and `g_(i,t)` are distinguished, the analyst
substitution is explicitly an estimation step, the filter/population split is
explicit, and the decision read-out uses the judge's own `g_(i,t)` against the
situation threshold.

The variance decomposition recomputes exactly:

```text
C(1-C)/(nu+1) + C(1-C)nu/(nu+1) = C(1-C).
```

The adoption kernel is a well-formed convex combination, and the empirical
prevalence / latent exchangeable-rate distinction supports the stated
`O_p(M^-1/2)` sampling remark separately from the nonlinear closure error.

## Issue 3: derived obligatoriness — CLOSED

- `R^0` is a realized, niche-specific population statistic rather than a status
  predicate.
- Pressure uses ungated full-choice norming and explicitly excludes saturation,
  obligatoriness, and outside-option choices.
- The recurrence defines every state. Entry makes the dimension obligatory;
  absent entry, a previous obligatory state persists unless release holds; all
  other cases are out.
- Entry and release cannot both hold because `pi_0 > pi_1` and
  `epsilon_1 > epsilon_0`.
- The stipulated base state and strict descent through `t-1` make the recursion
  well founded.
- The English progressive case can satisfy entry through low zero-marking rates
  in the ongoing-at-issue niche plus marked-competitor pressure, while the same
  simple-present nodes remain licensed in habitual niches. Saturation is
  downstream, so it does not collapse into licensing.

The audit's one scope note is that the derivation is relative to a stipulated
initial convention state; the manuscript now says this explicitly.

## Issue 4: cubic and frozen flow — CLOSED

The interior root

```text
theta-dagger = (beta + chi psi-bar) / (alpha + 2 chi psi-bar)
```

is algebraically correct. Its location in `(0,1)` matches attraction at both
endpoints, and the interior root is repelling when the bracket slope is
positive. The manuscript marks the cubic as stipulated rather than derived,
states the frozen-flow assumption, directs readers to recompute fixed points
for `psi(theta)`, includes the outside-option restriction, and leaves
convergence as a proof obligation.

## Verdict

All four audited defect clusters are closed.

**MATERIAL FORMAL COHERENCE: YES**
