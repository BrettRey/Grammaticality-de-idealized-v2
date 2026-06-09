# Agreement COCA Projection Protocol

**Date:** 2026-06-09
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Target module:** `AGR`
**Status:** protocol scaffold; no data run, no score movement.

## Decision

Use `AGR` as the first empirical vertical slice where a scoped workbench module is pushed beyond
card survival into a confirmatory corpus projection test.

The immediate precedent is the number-transparent quantified-NP work in
`Linguistic_transparency/paper/data/coca-pilot.md`: surface COCA query cells, KWIC filtering,
partitive/non-partitive contrasts, agreement-direction cells, and boundary cases such as `bunch`.

The stronger methodological precedent is the English left-branch extraction paper: make the
opportunity set explicit, manually validate candidates, estimate search error, and convert zero or
near-zero cells into uncertainty-bounded claims rather than impossibility claims.

## What This Improves

The Linguistic Transparency COCA pilot already does the important first pass:

- raw query cells are preserved;
- KWIC filtering separates genuine target cases from parse shifts, literal uses, modifiers, and
  non-target frames;
- several independent reflexes are checked: complement type, agreement direction, and boundary
  behaviour;
- counter-direction cells are treated as possible evidence only after inspection.

The workbench version should add five controls:

1. **Discovery/confirmation split.** Known CGEL members calibrate the query machinery. Boundary or
   candidate items test projection only if their target behaviour was not used to tune the graph or
   query definitions.
2. **Opportunity denominators.** Counts must be rates over relevant subject-position or complement
   frames, not raw string totals.
3. **Reproducible KWIC coding.** Every filtered cell needs raw rows, a coding label, and an
   exclusion reason.
4. **Uncertainty.** Use Wilson/Jeffreys intervals for proportions and upper bounds for zero cells.
5. **Search-error audit.** Sample raw positives and raw non-hits where possible to estimate false
   discovery and false omission pressure.

## Target Graph Commitments

The corpus run should test whether `AGR`'s internal distinctions project:

- `notional_agreement_basis -> agreement_controller_identification`;
- `agreement_controller_identification -> agreement_feature_alignment`;
- `agreement_override_pattern -> agreement_feature_alignment`;
- `agreement_feature_alignment -> community_licensing`;
- `retrieval_attractor_salience -> production_probability` as an error/processing channel, not as
  a licensing channel.

The core question is whether knowing the candidate expression's notional basis and constructional
subtype predicts agreement realization better than surface-head number alone.

## Discovery Set

Use known central cases only to calibrate query syntax and filtering:

- `a number of people`;
- `a lot of people`;
- `a lot of money`;
- `lots of people`;
- `lots of money`;
- `plenty of people`;
- `plenty of money`;
- `the rest of the people`;
- `the rest of the money`.

These can confirm that the wrapper, COCA search strings, KWIC exports, and coding labels reproduce
the already-known pilot pattern. They cannot earn projective credit.

## Confirmatory Targets

The first confirmatory tranche should target boundary or candidate cases:

- `bunch` with animate vs inanimate complements;
- `majority` and `minority` as borderline number-transparent/collective cases;
- `couple` sense split if queryable without excessive ambiguity;
- optionally `rest/remainder` fused-head or partitive variants if denominator cells can be defined
  independently.

The prediction should be registered before the relevant COCA cells are inspected.

## Prediction Shape

For each target, record:

- input diagnostics known before the run: candidate item, complement animacy/count profile,
  determiner frame, expected notional basis;
- predicted agreement realization: singular-dominant, plural-dominant, mixed/contextual, or
  uncertain;
- predicted contrast with a surface-head-only account;
- required opportunity denominator;
- exclusion labels that would invalidate raw hits.

## Data Artifacts

The run should write artifacts under `data/agr-coca-projection/`:

- `prediction-register.csv`: pre-run predictions and pass/fail thresholds;
- `query-plan.csv`: query families, denominators, and intended contrasts;
- `raw/`: raw COCA exports or copied KWIC batches;
- `coded/`: coded KWIC rows with labels and exclusion reasons;
- `summary.csv`: raw counts, filtered counts, denominators, intervals, and evidence status.

The initial template files are included now. Raw and coded data are intentionally absent until the
COCA run is actually performed.

## Pass/Fail Rules

`AGR` gains real projective pressure only if a registered confirmatory target behaves as predicted
on filtered data over an explicit denominator.

Pass examples:

- animate `bunch` shows plural agreement over relevant subject-position opportunities, while
  inanimate `bunch` does not show the same profile, or the failure is explicitly informative about
  `bunch` as a boundary case;
- `majority`/`minority` show mixed or context-conditioned agreement in the predicted direction,
  rather than collapsing to surface-head number;
- counter-direction raw hits mostly disappear under reproducible KWIC filtering.

Failure examples:

- surface-head number predicts agreement realization as well as the `AGR` node bundle;
- boundary targets require a construct not present in `AGR`;
- KWIC filtering depends on undocumented judgment calls;
- zero or sparse cells lack opportunity denominators and therefore cannot be interpreted.

## Score Discipline

No numeric score movement follows from creating this protocol.

If the run is completed and at least one confirmatory target passes, the next step is a
`held-out` or `protocol-bound` evaluation with `score_decision: score-change-proposed`. That
evaluation must cite the data artifacts, use activated paths from `AGR`, and state why the result is
projection rather than coverage.
