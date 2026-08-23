# Ox Alpha adjudication: catastrophe language and diagnostic simulation

## Role and independence

Act as an independent mathematical modeller and skeptical linguistics referee.
Recompute rather than deferring to either assessment below. Do not edit any
attached file. The decision is whether there is enough non-trivial predictive
content to justify a new simulation, a passage in the current formal
supplement, or eventually a separate paper.

The paper source and executable model are authoritative. In particular, the
full deterministic object is the discrete map on `(theta, a, b)` in
`formal-dynamics.tex` and `closed-loop-sim.mjs`; the scalar cubic is explicitly
only a large-concentration limiting sketch. The existing audit is attached so
that you do not accidentally rely on an already-identified diagnostic defect.

## Proposal to adjudicate

An external memo recommended rejecting Thom-style catastrophe classification
but retaining three ideas.

1. **Beta-shape boundary.** It claimed that rare niches drive the steady-state
   Beta shape parameters below one, producing endpoint-massed rather than merely
   wide posteriors. It gave
   `a* = lambdaPlus * meanSupport / (1 - deltaM)`, argued that concentration
   cannot distinguish `(0.4, 0.6)` from `(1.9, 0.1)`, and concluded that the
   paper's `(F, Phi)` read-out is blind to a generated regime boundary.
2. **Population cusp.** It argued that preemption gives positive feedback and
   hence a possible cusp with evidence/frequency asymmetry as one control and
   preemption strength as the other. It suggested that a one-dimensional cubic
   drift could license cusp identification, though irreversible dynamics may
   require a quasi-potential rather than a smooth potential.
3. **Diagnostic signatures.** It recommended testing critical slowing down
   (variance and lag-1 autocorrelation rising before a transition) and
   hysteresis under upward/downward preemption sweeps. It proposed interpreting
   distinct de-licensing and re-licensing thresholds as evidence of bistability,
   and fitting the R `cusp` package against logistic alternatives.

The memo's overall verdict was: pursue the bifurcation/signatures, leave Thom's
classification, add the Beta-shape result to the supplement, and consider a
future paper if the cusp survives numerical analysis.

## Codex's preliminary contrary assessment

Codex recommended no manuscript addition yet, but a bounded simulation. Its
main objections were:

1. The declared filter discounts toward a baseline:
   `a_tilde = a0 + deltaM * (a - a0)` and likewise for `b`. With the registered
   uniform baseline and no observations, a rare/quiet niche returns to
   `Beta(1,1)`, not a U-shaped Beta. The proposed steady state omitted the
   baseline. The numerical concentration example is also arithmetically wrong:
   the sums are 1 and 2. Moreover, the model retains posterior mean and
   concentration, and decision confidence uses posterior mass relative to a
   threshold. Therefore rarity does not establish the claimed hidden regime.
   (A separate question is whether moment projection can ever yield a shape
   parameter below one under non-quiet evidence, or loses important modality.)
2. Removing an earlier energy ontology is not itself a mathematical blocker:
   any smooth one-dimensional drift has an antiderivative. The real blocker is
   the absence of a demonstrated center-manifold reduction and cusp
   nondegeneracy/unfolding for the current three-dimensional discrete map.
3. The displayed scalar drift
   `theta_dot = theta(1-theta)(alpha theta-beta)` is not the cusp normal form.
   It retains fixed boundary branches and an interior branch that crosses them;
   a generic two-fold cusp has not been shown.
4. Critical slowing is conditional on approaching a loss of stability. The
   paper's robust moribund result, concentration loss when opportunity dries up,
   can occur without an eigenvalue approaching one. Thus slowing cannot yet be
   advertised as a sharper version of that prediction.
5. A hysteresis loop would support path dependence/multistability but would not
   uniquely identify a cusp. A valid test must separate genuine static
   hysteresis from finite-rate lag and from the explicitly stipulated entry and
   release hysteresis in the OBL rule.
6. Direct cusp regression on speaker-level licensing estimates may be
   misspecified for a bounded, dynamic, hierarchical model with measurement
   error. Model comparison alone would not validate the dynamical mechanism.

Codex nevertheless proposed a bounded diagnostic extension:

- continue the **full map**, not the scalar cubic, over independently meaningful
  control parameters;
- run quasi-static upward/downward sweeps at multiple rates and from multiple
  initial full states;
- perturb stable fixed points and measure full-state recovery and dominant
  eigenvalues;
- add noise only after deterministic structure is established, then test
  whether variance and lag-1 autocorrelation rise in the same approach;
- stop without manuscript change if no fold, robust rate-independent loop, or
  stability-loss signature appears.

## Questions

1. Which technical claims in the proposal and Codex response are correct,
   incorrect, or overstated under the attached equations and code? Show enough
   calculation to make the adjudication checkable.
2. Does the current model possess, or plausibly contain under a two-control
   continuation, saddle-node folds or a codimension-two cusp? Distinguish what
   is demonstrated, numerically searchable, and structurally impossible.
3. Is there a non-trivial projective payoff? State exactly what observing which
   source quantity would license expecting which held-out outcome, under what
   controls and timescale. Reject any projection that merely redescribes
   bistability or reuses its detection criterion.
4. Is a diagnostic simulation worth running now? If yes, give the **smallest
   adequate preregistered design** using the attached engine. Specify control
   parameters, grids or continuation method, initial states, sweep rates,
   perturbations, outcomes, failure conditions, and checks needed to distinguish
   static multistability from dynamic lag and stipulated OBL hysteresis.
5. Should stochastic critical-slowing diagnostics be included in the first run,
   or only after a deterministic loss of stability is found? Explain.
6. Give separate verdicts for: (a) add to the current main paper; (b) add to the
   formal supplement; (c) develop as a separate paper; (d) run the bounded
   simulation now.

## Required output

Lead with a short verdict. Then provide:

- a claim-by-claim adjudication table;
- the minimum simulation specification, if warranted;
- explicit stop/go criteria for manuscript action;
- the strongest justified world-side commitment and the non-trivial
  projection, if any;
- any code-level hazards in the attached engine that would invalidate the run.

Do not recommend catastrophe terminology unless the attached model earns more
than vocabulary and a phase portrait. Do not treat a formal or numerical result
as empirical evidence about language.
