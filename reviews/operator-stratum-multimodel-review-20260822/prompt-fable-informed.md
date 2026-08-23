# Fable OVMG-informed consistency audit prompt

You are the architecture and consistency reviewer for two companion papers.
Read these files in full:

- `subprojects/operator-stratum/main.tex` (the target paper)
- `main.tex` and `section3.tex` (the repaired OVMG companion)

Do not read prior review outputs or plans, and do not edit files. The target
paper predates the companion's latest repairs. Determine what the target paper
must change, if anything, to remain theoretically consistent and independently
publishable.

The previous formalization audit taught us to test, not presuppose, the
following separations:

- world-side population status versus speaker evidence, analyst estimates, and
  judgment output;
- Bayesian evidence updating versus persistent speaker adoption/retention and
  population change;
- historical recruitment versus current stability, effective maintenance, and
  corrective control;
- a category's membership conditions versus the projections used to test it;
- exact constitutive claims versus empirical support hypotheses.

Treat these as questions, not supplied diagnoses. Recompute whether each issue
actually arises in the operator-stratum paper. Also look for problems outside
this list.

Required output:

1. One-paragraph reconstruction of the target paper's strongest defensible
   thesis.
2. A cross-paper consistency table with TARGET PASSAGE, COMPANION COMMITMENT,
   STATUS (consistent / stale terminology / substantive conflict / underspecified),
   and REQUIRED ACTION.
3. An ontic/epistemic and level-of-analysis audit.
4. A projectibility audit: state the source, target, bearer, scope, and tolerance
   of each main projection; say whether it is independent of operator-membership
   diagnosis and what warrant is presently offered.
5. A recruitment/maintenance/control audit. Identify the strongest world-side
   commitment actually supported and every stronger formulation that is claimed
   for free.
6. A reader-facing audit of title, abstract, and first two sections for a typical
   linguistics expert who has not read OVMG.
7. A ranked revision plan divided into MUST, SHOULD, and DEFER. Say explicitly
   whether simulation, formalization, or Lean would add evidential value here,
   or merely decorate a conceptual paper.

Use line or section references and short exact phrases. Distinguish defects from
open empirical questions. End with a verdict: SOUND AS FRAMED, REPAIRABLE
WITHOUT NEW THEORY, or REQUIRES THEORETICAL RECONSTRUCTION.
