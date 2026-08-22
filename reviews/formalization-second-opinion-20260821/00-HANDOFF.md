# Second-opinion request: OVMG formal apparatus review

<!-- SUMMARY: Handoff package asking a second model to adjudicate a review of the OVMG paper's formal core (state theory, dynamics, Lean scaffold) · status: awaiting second opinion · updated: 2026-08-21 -->

## The task

You are being asked for an independent second opinion on a review of the formal
apparatus of Brett Reynolds, *Grammaticality de-idealized: The Operator-Value
Model of Grammaticality* (OVMG). The review is in `01-claude-review.md`
(findings) with recommendations at the end. Your job:

1. **Adjudicate each numbered finding** (9 findings, 3 recommendation tiers).
   For each: CONFIRM (with your own reasoning from the included sources, citing
   file and line), REFUTE (show why the review is wrong), or WEAKEN/STRENGTHEN
   (the finding is real but mis-weighted). Do not defer to the review; attempt
   refutation first.
2. **Report independent findings** the review missed, in the same areas:
   internal mathematical correctness, paper-to-Lean fidelity, the
   epistemic/ontic architecture, and alignment with the projectibility-first
   framework described in the brief.
3. **Judge the recommendations**: are the proposed fixes the right ones, are
   any harmful, and is the priority order right?

Ground every claim in the included files with line references. If you assert
that something is absent from a file (a definition, a bridging assumption, a
law), state the search you performed. Do not invent citations, theorems, or
paper content.

## What OVMG is (minimal orientation)

The paper de-idealizes grammaticality into a two-layer architecture:

- **State theory (paper section 3, `paper/section3.tex`)**: grammatical status is
  the population prevalence of a licensed assembly,
  S_t^theta(f,v,c) = P(exists A in A(f,v): def(A) and sat(A,c) and L_t(A,c) |
  theta_t, c), where def is hard typed-constraint compatibility, sat is
  saturation of obligatory dimensions, and L_t is speaker-level licensing of
  every constructional node in the assembly. The analyst's estimate is the
  posterior mean S-hat_t = E[S_t^theta | D_t] (abbreviated G_t). The subjective
  side is a bounded anomaly signal F in (-1, 0] and confidence read-outs:
  evidence confidence Phi^ev = nu/(nu+nu_0) in [0,1) and decision confidence
  Phi^dec = max{P(S>=tau|D), P(S<tau|D)}.
- **Dynamics (paper section 4, `paper/main.tex` lines ~749-1332)**: discounted
  Beta evidence filters per construction node, a normalized gated-softmax
  production model, log-likelihood-ratio omission evidence, a mean-field cubic
  for emergent bimodality, derived obligatoriness, winnerless cells,
  moribundity, actuation.
- **Lean scaffold (`formalization/`)**: a deliberately narrow Std-only
  structural sanity check of the section-3 core. It builds cleanly with the
  pinned toolchain (`lake build`, verified 2026-08-21).
- **v2 executable contract (`ovmg-tools/`)**: the reference implementation of
  the revised dynamics (not a fitted model). Included because one finding
  turns on whether inclusion states evolve anywhere in the system.

## The role of the brief

`context/projectibility-first-wtwss-codex-brief.md` is a working brief for a
*different* project (the book *Words That Won't Hold Still*). It reconstructs a
projectibility-first framework: begin with the projection to be licensed, keep
attribution unit distinct from explanatory bearer, state transport ranges,
treat mechanisms/maintenance/homeostasis as progressively stronger security
claims, and impose anti-vacuity discipline. The review was asked to assess the
OVMG formalization "in light of" this brief **without taking the brief as
gospel**. The same instruction applies to you: the brief is a recommendation
document, not adopted doctrine, and part of the review's content is claims
about where the brief should NOT be followed. Adjudicate those too.

## Context documents

- `context/formal-dynamics-revision-plan-2026-07-10.md`: the revision plan the
  current section 3-4 implements (state/estimate separation, variance
  decomposition, corrected discounting, LLR omissions, demoted derivation
  claims). Useful for judging whether the implementation matches the intent.
- `context/DECISIONS-excerpt-2026-06-09-to-07-10.md`: the project decision log
  for the relevant window, including the 2026-07-10 entries that motivated the
  current formal core ("This preserves conventional status without making it
  depend on the analyst's evidence state").

## Numerical checks already performed (re-check if you doubt them)

- Variance decomposition (section3.tex ~lines 310-322): for Beta(a,b) with
  C = a/(a+b), nu = a+b: Var(theta|D) = C(1-C)/(nu+1),
  E[theta(1-theta)|D] = C(1-C)nu/(nu+1), sum C(1-C). Confirmed.
- Cubic fixed point (main.tex eq. cubic-normal-form):
  C-double-dagger = (beta + chi*psi) / (alpha + 2*chi*psi). Confirmed.
- Decision threshold tau(c) = L_fa/(L_fa+L_fr) from asymmetric expected loss.
  Confirmed.
- Figure posterior-means trajectories: Beta(1,1) prior with per-step mass m
  gives mean 1/(2+mt); plotted values match exactly for m = 0.01 and m = 5,
  and the 95% CrI endpoints for Beta(1, 1.5) at t = 50 (0.0167, 0.9145) match
  the closed-form quantiles of 1-(1-x)^1.5. Confirmed.

## Manifest

```
00-HANDOFF.md                      this file
01-claude-review.md                the review under adjudication
paper/main.tex                     full paper source (section 4 dynamics at ~749-1332)
paper/section3.tex                 state theory (input by main.tex)
paper/main.pdf                     compiled paper (10 Jul build)
formalization/README.md            Lean scaffold scope statement
formalization/OVMG/Core.lean       the whole scaffold (214 lines)
formalization/OVMG.lean            root import
formalization/lakefile.toml        build config
formalization/lean-toolchain       pinned toolchain
context/projectibility-first-wtwss-codex-brief.md   the brief (do not take as gospel)
context/formal-dynamics-revision-plan-2026-07-10.md revision plan
context/DECISIONS-excerpt-2026-06-09-to-07-10.md    decision log excerpt
ovmg-tools/README.md               v2 model overview
ovmg-tools/quantitative-model-contract.md           v2 scope contract
ovmg-tools/js/revised-engine.mjs   v2 quantitative core
ovmg-tools/js/revised-sim.mjs      v2 occasion simulator
ovmg-tools/js/joint-likelihood.mjs toy joint likelihood
```

## Output format

A single report: (1) a table adjudicating findings 1-9 (verdict + one-line
basis each); (2) prose for anything you refute or re-weight, with line
references; (3) your independent findings, ranked; (4) verdict on the
recommendations and their ordering. Flag explicitly anything you could not
verify from the included files.
