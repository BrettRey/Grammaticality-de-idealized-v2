# Critique: context-indexed-dynamic-feedback-candidate

**Target:** `graphs/archive/context-indexed-dynamic-feedback-candidate.json`
**Family:** context-indexed-dynamic-feedback
**Pass:** fifth adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`left-branch extraction` is the strongest attack from outside the candidate's core domain. The graph
is now good at diachronic and context-conditioned norm/licensing conflicts, but it dropped the
operator-gap machinery that made the opportunity-preemption candidate useful:

- `operator_value`
- `semantic_pragmatic_recoverability`
- `constructional_analogy`
- `repair_reformulation_pressure`

That is acceptable if the graph is explicitly a dynamic context module. It is not acceptable if the
graph is treated as the new general winner.

The more general counterexample is overconditioning: for any failed prediction, the model can say
the community, norm centre, genre, medium, task frame, or speaker cue was underspecified. That can
be true, but if the relevant axes are chosen after the result is known, the representation becomes
too elastic.

## 2. Category Mistake

The candidate risks treating conditioning metadata as operationalization. It is not. A graph can
list required axes and still give no rule for:

- how axis values are chosen;
- which contrasts are pre-registered;
- when two contexts count as different enough to split;
- when an apparent context split is an ad hoc rescue;
- how evidence aggregates across context cells.

Metadata is a necessary representation move, but it needs a protocol.

## 3. Most Damaging Missing Node

`operator_value`, if the graph is used as a general model.

If the graph is scoped as a context/dynamic module, the most damaging missing element is not a node
but a procedure: a pre-specified conditioning protocol.

Secondary missing nodes for a general account:

- `semantic_pragmatic_recoverability`
- `constructional_analogy`
- `processing_cost`
- `repair_reformulation_pressure`

## 4. Most Suspicious Edge

`task_framing_t1 -> grammaticality_attribution_t1`.

The edge is plausible, but it can also make explicit grammaticality attribution look like a mere
task artifact. The safer reading is that task framing changes which evidential channel is foregrounded
in attribution, not that attribution is fully caused by the prompt.

This edge needs pressure from the protocol: task framing must be specified before judgment data are
interpreted, not inferred afterward to explain the result.

## 5. Minimal Mutation

Do not create another larger graph yet.

Instead:

- add an operational conditioning protocol;
- make the linter check that declared conditioning axes have corresponding graph nodes;
- keep the context-indexed dynamic candidate as a module, not a winner;
- return to operator-gap cases later with a parallel context-aware operator module.

## 6. Score-Readiness Judgment

`not ready`.

The candidate is the strongest dynamic/context module so far, but it should not receive a non-zero
general score. Its next test is whether it can survive pre-specified context contrasts without using
conditioning as a rescue parameter.
