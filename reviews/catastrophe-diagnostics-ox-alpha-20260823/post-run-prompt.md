# Ox Alpha post-run refutation audit

Audit the attached bifurcation implementation and generated JSON against the
attached engine. Do not edit files. This is a second, post-result lane: try to
refute the result rather than reconciling it with your earlier adjudication.

Your pre-run review correctly rejected the proposed rare-niche U-shaped Beta
regime and reproduced the one-control fold. It reported the cusp as unresolved
after a coarse adoption-threshold probe. The local implementation subsequently
found a candidate at approximately
`(theta, inflow, q) = (0.370957, 0.479156, 0.552048)` by solving
`R = R_theta = R_theta_theta = 0` for the stationary reduced residual. It
reports:

- cubic derivative about `-7.2843`;
- two-control unfolding determinant about `2.3345`;
- full-map eigenvalue moduli `1.000000, 0.961496, 0.883699`;
- one distinct fixed point at the cusp, three inside a nearby wedge, and one
  outside;
- five-start stationary evidence agreement below `1e-8`;
- deterministic spectral radius and pulse-recovery time rising toward the
  `q=.5` fold;
- two-control directional jumps converging toward two static folds as the
  number of iterations per control value rises;
- failure of the preregistered stochastic monotonicity criterion because all
  24 trajectories escape at `1.02 x` fold distance and only four pre-escape
  segments remain valid;
- no variance clamp in any checked cell and deterministic third-moment error
  below `7.4e-5`;
- one-sided boundary mass on dense negative-evidence branches (`min a=.9314`)
  but no checked state with both Beta shapes below one.

Please check, in order:

1. Whether the numerical derivative formulas, Newton systems, control
   transformation, cusp nondegeneracy determinant, and full-Jacobian test are
   correct for a codimension-two cusp of this discrete map.
2. Whether the one-versus-three fixed-point comparison and static-fold
   hysteresis cycle are independent evidence or artifacts of the root locator,
   finite differences, or the chosen local coordinates.
3. Whether the two controls (effective evidence inflow and independently
   supplied adoption threshold) constitute a legitimate unfolding in the
   model, and what their empirical identification would require.
4. Whether the stochastic result is correctly classified as a failed general
   early-warning criterion rather than either positive confirmation or a
   refutation of deterministic slowing.
5. Whether the one-shape-below-one finding corrects your earlier scan without
   rehabilitating the original rare-niche/U-shape proposal.
6. Whether any manuscript claim is now warranted. Distinguish main paper,
   formal supplement, separate paper, local bifurcation terminology, and Thom
   catastrophe terminology.

Return a short verdict, a ranked defect list, independent numerical spot checks,
and an explicit `CUSP RESULT: CONFIRMED / NOT CONFIRMED / INDETERMINATE` line.
