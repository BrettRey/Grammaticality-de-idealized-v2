# Thirty-First Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** second held-out agreement projection check after the measure-NP override survived.

## New Held-Out Card

Added `fused-determiner-head-agreement-cgel`.

This card tests `any`, `none`, `either`, and `neither` as fused determiner-heads. It separates
non-count singular construal, plural-set construal, singular/plural variants, and formal-style
avoidance.

## Evaluation Result

Created `agreement-controller-override-heldout-scope-2026-06-09`.

The evaluation combines two held-out agreement subtypes:

- `measure-agreement-override-cgel`: survives.
- `fused-determiner-head-agreement-cgel`: survives.

Both survive without adding nodes or edges to `agreement-controller-override-candidate`.

## Scope Decision

`agreement-controller-override-candidate` now receives a `scoped_module` label through a
`scope-only` held-out evaluation. Numeric scores remain zero.

This is the right promotion level: the graph has build-card survival plus two held-out subtype
survivals, but it has not earned a score-change evaluation and has not been tested outside the CGEL
agreement domain.

## Boundary

The graph is an agreement module only. It should not absorb:

- category analysis for fused-head constructions (`CAT`);
- pronoun/pro-form personhood and audience design (`AUD`);
- diachronic or cohort stabilization (`DYN`);
- processing-only attraction effects (`PROC`).

## Next Move

Either pause agreement growth and return to temporal/catenative pressure, or test agreement against
a different source domain such as pronoun/person agreement or elicited attraction data before
considering numeric score movement.
