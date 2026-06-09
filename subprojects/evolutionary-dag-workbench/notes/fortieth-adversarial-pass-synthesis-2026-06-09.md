# Fortieth Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** Brett's number construal/realization prompt.
**Change type:** Consolidated protocol-bound evaluation, no graph mutation, no score movement.

## What Changed

Added evaluation:

- `evaluations/protocol-tests/agreement-number-construal-realization-2026-06-09.json`

No ontology nodes and no graph edges were added.

## Evaluation Rationale

Brett's prompt named a real pressure point:

> number construal/realization under different factors including coordination and collective nouns

The workbench already had the relevant card bundle:

- `collective-number-transparent-agreement-cgel`;
- `coordination-agreement-resolution-cgel`;
- `measure-agreement-override-cgel`;
- `fused-determiner-head-agreement-cgel`;
- `proximity-agreement-error-cgel`.

The question was whether this bundle forces a new number-construal construct or whether
`agreement-controller-override-candidate` already has the needed separation.

## Result

`AGR` survives the consolidated number-realization pass without mutation:

- `notional_agreement_basis` handles unit, member, single-measure, plural-set, and related construal
  evidence;
- `agreement_controller_identification` handles which expression or construction supplies the
  controller;
- `agreement_override_pattern` handles licensed departures from simple surface-head matching;
- `agreement_feature_alignment` handles the realized agreement relation;
- `retrieval_attractor_salience` remains the processing/error route and is forbidden from licensing.

This confirms that number construal is not a reason to add a free-standing `number_construal`
node yet. The current graph is doing the needed work by routing construal through controller
identification and alignment.

## Boundary

No score movement follows. This pass mostly consolidates built-on and already-held-out agreement
evidence. It strengthens confidence that `AGR` is not merely memorizing coordination or collective
noun cases, but it does not supply a new projective data source.

The next agreement move should wait for a genuinely different domain or data source. Otherwise the
better marginal work is a held-out temporal/modal test for `TEMP`, a pronoun/audience task, or the
independent-relative-`whose` human judgment lane.
