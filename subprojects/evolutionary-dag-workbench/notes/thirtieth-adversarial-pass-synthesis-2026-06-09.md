# Thirtieth Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** first held-out projection check for `agreement-controller-override-candidate`.

## Held-Out Card

Added `measure-agreement-override-cgel`.

The card draws from the same broad CGEL agreement source pool but from a different subtype than the
cards used to build the agreement candidate. It tests formally plural measure NPs that license
singular agreement under single-measure construal.

## Evaluation Result

`measure-agreement-override-cgel` survives `agreement-controller-override-candidate` as a module.

The graph generalizes because the measure case can be routed through:

- notional basis -> controller identification;
- override pattern -> feature alignment;
- feature alignment -> community licensing;
- licensing -> lower repair pressure.

This is exactly the distinction the graph was built to preserve: surface plurality does not by
itself determine the controller, and a licensed singular override is not an attraction error.

## Guardrail

No score movement and no `scoped_module` label follow yet. This is one held-out card from the same
CGEL chapter, not a cross-source or cross-domain projection test. It is enough to show the agreement
candidate is not merely repeating the build cards; it is not enough to stabilize a scored module.

## Next Move

Add one more held-out agreement card from a different agreement domain, ideally one of:

- relative-clause agreement with `one of those people who...`;
- fused determiner-head agreement with `none`, `any`, `which`, `who`, or `what`;
- person agreement in cleft relatives.

If the candidate survives a second held-out subtype without adding nodes, then a `scope-only`
evaluation and `scoped_module` label become reasonable. Numeric scores should still wait.
