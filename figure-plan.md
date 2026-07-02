# Figure plan — grammaticality-de-idealized (OVMG)

**Status (2026-07-02): BUILT #1, #2, #3, #5, #7. Skipped #4 (redundant w/ Fig
`posterior-means`), #6 (decision tree already legible as a table), #8 (companion
duplication), #9 (housekeeping). Fig `posterior-means` provenance fixed
(`simulate_dynamics.py` regenerated to emit the plotted coords + bands). Paper
now has 6 figures + the trident. All compile clean at 52 pp.**

Generated 2026-07-02. Menu to trim, not a build order. Build survivors with
`.house-style/plot_style.py` (data) or TikZ/forest (conceptual), then
`/check-chart-style` each.

## Existing

- **Fig. `posterior-means`** (licensing posteriors, rare vs stable-gap, 95% CrI
  bands). Rebuilt 2026-07-01. KEEP. **Provenance flag:** `simulate_dynamics.py`
  and `simulation_data.dat` are now stale — they hold the old 0.1-decay rare
  curve and no credible bands, while the figure's coordinates were recomputed
  by hand (Beta(1,1), per-step mass 0.01 / 5, Wilson-style quantile bands). Fix
  before submission: regenerate the script to emit the plotted values, or the
  figure isn't reproducible from the repo.
- **Fig. `impossible trident`** (borrowed line drawing, Scott-Phillips section).
  Low value; illustrates a rival's analogy, not OVMG. Raster `.jpg` in a vector
  doc is a house-style smell. KEEP-OR-CUT with the relevance-theory subsection.

## Menu

| # | Fig | Kind | Makes clearer | Type | Source | Keep |
|---|-----|------|---------------|------|--------|------|
| 1 | Profile → projection spine | conceptual | the paper's thesis: (map, K, C_t) form a profile whose partial observation licenses projections, with support graded | left-to-right schematic; inputs → licensing posterior → projections (repair, transmission fidelity, satiation, change), support-ladder annotated | conceptual | **must** |
| 2 | Licensing-state space (mean × concentration) | conceptual | the payoff of the posterior-state revision: profiles differ in a 2nd dimension the mean-product G̃ can't encode | 2-D region diagram; x = posterior mean, y = concentration; place grammatical / stable-gap / community-novel (*whose*) / defective-cell regions | conceptual | **must** |
| 3 | Discrete-status → gradient-feeling channel | conceptual | the G/F two-layer claim (Table 2 as a picture): thresholded G_t filtered through R_i, D_i, noise → F | schematic with a noise/cost channel; ties to HPC-book "discrete from continuous" | conceptual | nice |
| 4 | Emergent bimodality of C_t | data (simulated) | the "emergent categoricality" headline: node-level licensing piles up near 0 and 1, few in the middle | density/histogram over many simulated construction nodes | `DATA NEEDED` — extend `simulate_dynamics.py` to many nodes; illustrative, not empirical | nice |
| 5 | Threshold-reality test (RD) | conceptual | the new falsification test (Lazzaro): community response jumps at τ(c) if G_t is real, is smooth if it's bookkeeping | two-panel schematic, discontinuous vs smooth response over G̃; mark τ(c) | conceptual | nice |
| 6 | Diagnostic decision tree | conceptual | the "at a glance" routing, currently an in-text arrow-table | TikZ flowchart: no analysis→nonsense; clash→K-fail; rare→novel; preempted→stable gap; split→defective; high cost→transient; else grammatical | conceptual (upgrade of existing table) | nice |
| 7 | AGR agreement projection (COCA) | **data** | that C_t is measurable by corpus-rate-per-opportunity: notional plural dominates for *a bunch of* + animate plural etc., with real intervals | forest / dot-with-CI, plural-share by cell family | `subprojects/evolutionary-dag-workbench/data/agr-coca-projection/uncertainty-summary.csv` (real, KWIC-filtered, Wilson 95%) | stretch |
| 8 | LBE opportunity funnel | **data** | the flagship stable-gap: 86,098 det–head arcs → 1,228 fronting opps → 0 genuine LBE | funnel/bar | real, but **belongs to companion** `english-lbc-functionalist` (`figures/fig_opportunity_funnel.pdf`); import risks self-duplication | stretch |
| 9 | Levels-of-explanation map | conceptual | which OVMG quantity lives at which level (corpus-distributional C_t, cognitive Λ_i, processing R_i, institutional D_i) | labelled column schematic | conceptual | stretch |

## Notes for trimming

- **#1 and #2 are the two that most repay building.** #1 makes the
  projectibility-first framing visible (right now the thesis is stated but never
  drawn); #2 is the spatial form of the exact argument the review board said the
  formalism was missing (mean vs concentration). They pair with the existing
  trajectory figure: Fig `posterior-means` shows the motion, #2 shows the
  endpoint state space.
- **#7 is the only genuinely empirical candidate that's ready.** The data is
  real and already collected. Cost: it lives in a subproject and the main text
  touches agreement only glancingly, so it needs a paragraph of motivation to
  earn a place, or it stays a subproject asset. Worth it only if you want one
  real-data anchor in an otherwise formal paper.
- **#4 and #8 both risk redundancy or duplication** — #4 with Fig
  `posterior-means`, #8 with the companion LBE paper. Keep at most one.
- Everything here complies with house doctrine (no truncated axes, ≤5 series,
  no dual-y). Data plots would use `plot_style.py`; conceptual ones TikZ/forest
  (upright brackets, en-dashes).

**Trim prompt:** which of #1–#9 to keep? My recommendation: build #1 and #2
(must), decide #3/#5 as a pair (both make a stated-but-undrawn claim visible),
and take #7 only if you want a real-data anchor. Regenerate
`simulate_dynamics.py` regardless, to fix Fig `posterior-means` provenance.
