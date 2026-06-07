# Forbidden Conflations

These are lint targets for graph agents and human review. A graph may violate them deliberately only if it marks the move as a theoretical wager.

## Core Distinctions

- Do not use `reported_acceptability` as a synonym for grammaticality.
- Do not use `grammaticality_attribution` as a synonym for the thing attributed.
- Do not use `usage_frequency` as a synonym for `entrenchment`.
- Do not use `usage_frequency` as a synonym for `community_licensing`.
- Do not use `standard_language_ideology` as a synonym for community licensing.
- Do not use `processing_cost` as a synonym for ungrammaticality.
- Do not use `semantic_pragmatic_recoverability` as a synonym for grammaticality.
- Do not use `operator_value` as a synonym for every form-meaning relation.
- Do not use `social_indexical_value` as a synonym for register fit.
- Do not use `measurement_task` as a synonym for the target construct.

## DAG-Specific Checks

- If a graph contains feedback, it needs time slices or `time_lagged` edges.
- If a graph treats correction as evidence of ungrammaticality, it must separate correction source, correction context, and correction authority.
- If a graph treats corpus frequency as evidence, it must say whether opportunity mass has been controlled.
- If a graph treats speaker judgment as evidence, it must say which channel perturbations are active.
- If a graph contains a node called "grammaticality," it must define whether this is attribution, theoretical posit, community licensing, operator-state, or another construct.
- If a graph treats two constructs as mutually co-constitutive within one time slice, it must not encode that as a same-slice directed cycle. Choose and justify an acyclic constitutive direction, time-slice the dependence, or mark the acyclic representation as a theoretical wager.
