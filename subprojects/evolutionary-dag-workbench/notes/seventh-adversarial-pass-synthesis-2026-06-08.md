# Seventh Adversarial Pass Synthesis: Task-Separated Feedback

**Date:** 2026-06-08
**Mutation:** `context-indexed-task-separated-feedback-candidate`
**Trigger:** held-out `case-in-coordination-cgel` and older `between-you-and-I` pressure.

## Pressure

The prior `context-indexed-dynamic-feedback-candidate` could represent standard ideology,
correction, reported acceptability, attribution, and production. Its weak point was task
discipline: unmonitored production, elicited production, correctness judgment, editing, and grammar
testing were all routed through `task_framing` or left implicit.

That made the graph vulnerable to a familiar collapse:

- production probability in an ordinary setting;
- reported acceptability in a judgment task;
- correction in a school or editing task;
- grammaticality attribution under correctness framing.

Those are related, but they are not the same measurement channel.

## Mutation

Added controlled nodes:

- `production_task_setting`
- `judgment_task_setting`

Created `context-indexed-task-separated-feedback-candidate`, a compact profiled graph that keeps:

- production task setting -> production probability -> later usage;
- schooling exposure -> standard ideology -> condemnation -> correction -> attribution;
- judgment task setting -> task framing -> acceptability/attribution;
- correction pressure -> later monitored production.

The graph retains community licensing as a separate construct and explicitly forbids routing
standard ideology into community licensing.

## Evaluation

Added `evaluations/protocol-tests/context-indexed-task-separated-feedback-2026-06-08.json`.

Results:

- `case-in-coordination-cgel`: survives as a production/judgment divergence module.
- `between-you-and-I`: survives as the same divergence module.
- `pronoun-personhood-proform-gender`: partly survives; the graph still lacks audience-design and
  reference-tracking structure.

## Decision

No score movement. The graph is a useful scoped mutation, not a new general account and not yet a
replacement for the broader dynamic-context module.

The next mutation should come from one of two remaining failures:

- add audience-design/reference-tracking structure for pronoun and pro-form cases;
- split collocational rigidity from argument-linking selection in the operator-gap module.
