# Ox Alpha post-restructure audit

You are reviewing a post-restructure version of Brett Reynolds,
*Grammaticality de-idealized*. The main paper has just been made deliberately
math-free for a typical linguistics expert. All equations, notation,
likelihoods, population dynamics, simulation specifications, and the Lean
correspondence have been moved to a standalone formal supplement.

This is an adversarial, refutation-first audit. Read all attached files. Treat
the TeX sources as source of truth; do not rely on earlier review verdicts.
Recompute any formal claim you challenge. Do not edit files.

## Questions

1. **Main/supplement boundary.** Is the main paper genuinely independent of
   mathematical notation while retaining the model's linguistic content,
   scope conditions, and falsifiers? Flag any main-paper claim that now
   overstates, understates, or misdescribes the formal supplement.

2. **Reader accessibility.** Would a typical expert linguist understand the
   reader-facing definitions of *public update*, operator contrast, coverage,
   compatibility, saturation, licensing, evidence concentration, population
   heterogeneity, and the four dynamics trajectories? Identify the three
   highest-friction passages, but distinguish genuine conceptual opacity from
   mere density.

3. **Level and category discipline.** Audit especially:
   - operator membership versus categorical licensing;
   - opportunity as a licensing/categoricality modulator rather than an
     operator-membership condition;
   - operator-value mis-setting versus value-intact exponent exclusion;
   - head-specific complementation such as *depend of* as constructional
     convention rather than necessarily an operator error;
   - a rich SBCG construction/sign versus the task-specific mathematical
     projection used by OVMG;
   - speaker inclusion, population rate, analyst estimate, and subjective
     read-out.

4. **Projectibility and causal strength.** Check that the main and supplement
   declare non-trivial projections beyond membership diagnostics, keep warrant
   separate from world-side pattern, and do not move freely from stability to
   causal order, maintenance, or corrective control. Repair must remain only a
   candidate controller absent intervention evidence.

5. **Formal coherence.** Recheck the outside-option normalization, current-window
   evidence recurrence, learner-to-population transition, ontic definition of
   obligatoriness versus analyst identification, and stated scope of the
   simulations. Look for any regression introduced by splitting the files.

6. **Lean meaningfulness.** Evaluate the theorem *statements*, not merely
   compilation. Do `OperatorStratum.lean` and `OperatorBridge.lean` establish
   non-vacuous structural distinctions worth reporting? Look for conclusions
   smuggled into arbitrary predicates, witnesses made trivial in a misleading
   way, mismatch with the manuscript, or unproved empirical content. The Lean
   artifact is intentionally not a formalization of the stochastic dynamics.

7. **Notation register.** Is `formal-notation.tex` sufficiently typed and
   complete to answer the reader's complaint that variables and constants were
   introduced without definition? List recurring symbols that remain undefined,
   mis-typed, or dangerously overloaded.

## Output

Give:

- a one-paragraph verdict on the restructuring;
- a table of findings with severity, exact file/line evidence, and proposed
  repair;
- explicit verdicts for **main-paper linguistic coherence**, **formal
  supplement coherence**, **Lean structural meaningfulness**, and
  **main--supplement--Lean correspondence**;
- a refutation ledger for the five previously fragile interfaces named in
  Question 5; and
- a prioritized repair list containing only changes that would materially
  improve the package.

Be willing to return “no material problem found” for an interface that survives
your attempts to break it. Do not recommend putting equations back into the
main paper merely because the supplement is long.
