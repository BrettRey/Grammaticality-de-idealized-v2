The JSON tail confirms: stochastic criterion fails at ratio 1.02 (24/24 escape, 4 valid replicates), medians non-monotone, `stochasticResultPasses: false`, `hysteresisRateConverges: true`. Now I'll run independent numerical spot checks in a scratch script outside the repo (no project files touched).All spot checks reproduce to machine precision. One more independent check on the full-map Jacobian eigenvalues:## Post-run refutation audit

### Independent spot checks (all recomputed from scratch, importing the engine read-only)

| Claim | My recomputation | Verdict |
|---|---|---|
| `R = R' = R'' ≈ 0` at `(0.370957, 0.479156, 0.552048)` | `R = 3.0e-11`, `R' = -1.1e-10`, `R'' = 2.5e-8` | reproduced |
| Cubic term ≈ `-7.2843` | -7.2883 / **-7.2843** / -7.2836 at h = 5e-4/1e-3/2e-3 | stable across steps |
| Unfolding det ≈ `2.3345` | 2.33448087 from my own mixed differences | reproduced exactly |
| Full-map multipliers `1.000000, .9615, .8837` | each reported λ satisfies `det(J − λI) ≈ 0` (≤ 3e-16); trace matches λ-sum to 8e-14; one +1 multiplier, two strictly inside | eigenvalues genuine |
| Fold at q=.5 | `R = 3e-12`, `R' = 1.7e-11`, `R'' = 3.04 ≠ 0` | genuine fold |
| 1-vs-3 fixed points | grid sizes 240/720/1200 all give n=3 inside (`0.253, 0.370, 0.505`), n=1 outside (`0.230`) | robust, not a locator artifact |
| Static folds on cross-section | residuals ≤ 2.3e-10, `dR/dθ ≤ 4e-12`, local splitting coefficient = 0.02 to machine precision | genuine saddle-node pair |

Formulas are correct: central second/third differences are the standard stencils; the determinant `R_u·R_θq − R_q·R_θu` is the right transversality condition for the unfolding; `R=R_θ=R_θθ=0, R_θθθ≠0` with a +1 multiplier and two transverse stable multipliers is the correct codimension-two cusp characterization for a discrete map.

### Ranked defect list

1. **Stochastic cell is doubly compromised** (run-cited but understated): at ratio 1.02 only 4/24 segments survive (selection bias), *and* the surviving medians are non-monotone (detrended variance falls from 1.77e-3 at 1.1 to 1.23e-3 at 1.02; lag-1 falls 0.9854 → 0.9792). The failure is not merely "too many escapes"; the preregistered monotonicity fails on its own terms among survivors.
2. **Control confound in the stochastic audit**: `observationProbability` is scaled with inflow (`ratio × 0.6`, capped at 1), coupling the inflow control to observation thinning rather than varying them independently.
3. **No step-sensitivity audit for the unfolding mixed partials** (unlike `derivativeStepAudit` for θ derivatives); steps are fixed at 2e-4/1e-3.
4. **Hysteresis jump detection is fragile**: largest adjacent θ-difference is dominated by dynamic lag at low iteration counts (jump size 8e-4 at k=20); convergence rests entirely on the k=5000 row.
5. Minor: `cusp-center` count of 1 depends on the arbitrary 0.01 grouping tolerance; the residual cache key (`toPrecision(15)`) could in principle collide (practically negligible here).

### Question-by-question

1. Correct (defect 3 aside).
2. Independent evidence; my grid sweep and fold-residual checks rule out locator/finite-difference artifacts. Local coordinates are ordinary; nothing suspicious.
3. Formally a legitimate local unfolding (det ≠ 0, both controls enter through distinct mechanisms: evidence power vs. posterior-threshold response). Empirical identification would require independently measuring effective exposure (opportunity frequency × observation rate) and the community adoption threshold as separable quantities; that work has not been done, so the result remains a property of the declared model.
4. Correctly classified. It is a failed general early-warning criterion, neither positive confirmation nor refutation of deterministic slowing; deterministic slowing itself has independent support (spectral radius rises monotonically 0.9648 → 0.9956 toward the q=.5 fold).
5. Yes. `min a = 0.9314` on dense negative-evidence branches gives one-sided boundary mass, never both shapes below 1. This corrects the coarse scan without rehabilitating the rare-niche/U-shape proposal; moment-matching still pins both shapes from mean and concentration.
6. Warranted claims: local bifurcation and static-hysteresis language for the formal supplement or a separate methods paper, scoped to the expected-window closure under declared parameters. Not warranted: any main-paper empirical claim about language, Thom catastrophe terminology (no gradient structure, no global unfolding proof), and the scalar cubic should stay retired.

**CUSP RESULT: CONFIRMED** (as a local, model-internal bifurcation result; empirically unidentifiable until defect-level measurement of the two controls exists)

No project files were edited; scratch script lives in `/var/folders/tq/7kfdnyd52zz82t095tvgbljc0000gp/T/opencode/cusp-audit.mjs`.