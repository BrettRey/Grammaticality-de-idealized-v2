# Independent review brief: OVMG model and manuscript revision plan

Review `notes/model-and-manuscript-revision-plan-2026-08-22.md` as an
adversarial but constructive referee. The objective is a submission-ready paper
whose state theory remains ambitious while its population-dynamics claims say
exactly what the mathematics and simulations support.

The relevant current sources are:

- `main.tex` and its included `section3.tex`;
- the plan under review;
- the companion-tool `README.md`, `STATUS.md`, and
  `notes/quantitative-model-contract.md`; and
- the independent closed-loop follow-up audit.

The known computational findings are conditional: linear response stayed
interior at the calibrated negative-evidence scale; sufficiently steep logistic
and posterior-threshold responses separated regimes in some declared cells;
memory, opportunity, evidence calibration, and outside-option mass mattered;
finite-horizon perturbation return was observed in a passing threshold cell;
programmed repair is only a wiring check; and heterogeneous priors alone did not
make dispersion precede the normalized mean shift after opportunity loss.

Please answer these questions:

1. Does the plan repair the right layer of the model, or does it preserve a
   deeper conceptual or mathematical defect?
2. Is the proposed mean-field crossing/stability diagnostic correct at the
   stated level of closure? Identify any missing qualification.
3. Does the proposed smooth logistic response give an independently
   interpretable source of nonlinearity, or merely hide the desired result in a
   parameter? Recommend keep, revise, or omit.
4. Is retaining the cubic as a conditional normal form scientifically useful?
5. Does the plan calibrate the simulation, moribundity, repair, and stationary-
   distribution claims correctly?
6. From a projectibility-first perspective, which proposed manuscript changes
   are essential to prevent a trivial projection, post-hoc scope rescue, or an
   unsupported move from stability to maintenance/control?
7. Is the scope appropriate for this submission stage? Flag anything that is
   necessary now, anything that should be deferred, and anything that should be
   removed.
8. Rank the five most important changes to the plan.

Distinguish fatal objections, material revisions, and optional refinements.
Quote or cite source sections where useful. Do not edit files. End with one of:
`ACCEPT PLAN`, `ACCEPT WITH REVISIONS`, or `RETHINK PLAN`.
