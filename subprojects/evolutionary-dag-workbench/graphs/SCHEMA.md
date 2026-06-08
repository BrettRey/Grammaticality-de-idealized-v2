# Graph JSON Schema

Seed and archive graphs are stored as JSON. The local validator checks simple graph structure,
duplicate edges, edge types, and time-lag discipline. The linter also checks node IDs against
`ontology/nodes.yaml`, relation profiles against `ontology/relation-profiles.yaml`, graph IDs
against filenames, `family`, `status`, and score discipline.

```json
{
  "id": "usage-heavy-seed",
  "title": "Usage-heavy seed graph",
  "family": "usage-heavy",
  "status": "seed",
  "edge_semantics_level": "topology_only",
  "nodes": [
    "usage_frequency",
    "entrenchment",
    "reported_acceptability"
  ],
  "edges": [
    {
      "source": "usage_frequency",
      "target": "entrenchment",
      "type": "causal",
      "relation_profile": "positive_monotone",
      "rationale": "Repeated exposure can change learned accessibility."
    }
  ],
  "conditioning_axes": {
    "community": "Required for context-indexed graphs.",
    "norm_centre": "Required for context-indexed graphs.",
    "genre": "Required for context-indexed graphs.",
    "medium": "Required for context-indexed graphs.",
    "task_framing": "Required for context-indexed graphs.",
    "speaker_identity": "Required for context-indexed graphs."
  },
  "scores": {
    "empirical_coverage": 0,
    "counterexample_resilience": 0,
    "measurement_clarity": 0,
    "explanatory_payoff": 0,
    "cross_domain_stability": 0,
    "complexity_penalty": 0,
    "circularity_penalty": 0,
    "construct_confusion_penalty": 0
  },
  "score_status": {
    "kind": "unscored",
    "evaluation": "evaluations/protocol-tests/example.json",
    "scope": "Free text describing whether the score is scoped or general."
  },
  "notes": "Free text."
}
```

## Required Fields

- `id`
- `title`
- `family`
- `status`
- `nodes`
- `edges`

`id` must match the JSON filename stem. For example,
`graphs/archive/context-aware-operator-gap-candidate.json` must use
`"id": "context-aware-operator-gap-candidate"`.

## Status Values

- `seed`
- `candidate`
- `archived`
- `rejected`
- `superseded`

`family` should be a lowercase hyphenated slug used for archive grouping.

## Allowed Edge Types

- `causal`
- `mediating`
- `measurement`
- `constitutive`
- `evidential`
- `time_lagged`

Edges are unique by `source`, `target`, and `type`. Repeating the same typed edge is invalid; if two
rationales seem necessary, merge them or introduce a distinct construct.

## Optional Relation Profiles

`relation_profile` is optional. When absent, the edge is an uncommitted topology claim: it says that
a relation is worth representing, not that the graph has pre-registered a sign or inference reading
for prediction.

Allowed profiles are defined in `ontology/relation-profiles.yaml`. If a profile is present, it must
be compatible with the edge's `type`.

Graph-level `edge_semantics_level` values:

- `topology_only`: default when the field is absent; profiles may be absent.
- `profiled`: the graph contains explicit relation profiles for the edges it is using as
  prediction commitments.

Profiled graphs must include at least one `relation_profile`. They do not need every edge profiled:
profiles accrete where protocol-bound evaluation needs an interpretable path. Evidential and
constitutive profiles express warrant or component relations, not signed causal propagation.

## Dynamic Feedback

If a graph needs feedback, use explicit time slices or `time_lagged` edges. The validator excludes `time_lagged` edges from synchronic cycle checks.
`time_lagged` edges must point forward in time: `_t` counts as time 0, `_t1` as time 1,
`_t2` as time 2, and so on. Backward or same-slice `time_lagged` edges are invalid.

For all typed edges, if both endpoints are time-sliced, the target time must not precede the source
time. Forward cross-time effects must use `time_lagged`; same-slice typed edges may use the other
edge types.

Same-slice mutual dependence is not represented as reciprocal directed edges. If a graph claims
co-constitution within a single timescale, it should either explain the acyclic constitutive
direction it chooses or mark the move as a theoretical wager.

## Conditioning Metadata

Graphs may include `conditioning_axes` when their claims depend on community, norm centre, genre,
medium, task framing, or speaker identity. This is required for graph families whose slug contains
`context-indexed`.

Allowed axes:

- `community`
- `norm_centre`
- `genre`
- `medium`
- `task_framing`
- `speaker_identity`

Each axis value must be a non-empty string explaining how that condition should be specified before
the graph is interpreted. Context-indexed graphs must include all six axes.

Declared axes must also be represented by graph nodes that are themselves outcome-like or have a
directed path to an outcome-like node. Time-sliced node IDs count by their base node. The linter
checks:

- `community` -> `community_licensing`
- `norm_centre` -> `standard_language_ideology`, `metalinguistic_condemnation`, or
  `editorial_correction_probability`
- `genre` -> `genre` or `register_genre_appropriateness`
- `medium` -> `medium`
- `task_framing` -> `task_framing`
- `speaker_identity` -> `speaker_identity` or `social_indexical_value`

## Scoring

Seed graphs carry complete all-zero `scores` blocks. Non-zero scores should be added only after an
adversarial critique exists in `graphs/critiques/` or an equivalent review note is linked.

Each score dimension must be numeric, not boolean, and must be between 0 and 5 inclusive.

Graphs with non-zero scores must include `score_status`.

Allowed `score_status.kind` values:

- `unscored`
- `scoped_module`
- `general_account`

`scoped_module` and `general_account` labels require `score_status.evaluation`. The evaluation must
target the labelled graph, have `status` set to `protocol-bound` or `held-out`, and have
`score_decision` set to `scope-only` or `score-change-proposed`.

Non-zero scores require `score_status.kind` to be `scoped_module` or `general_account`. They also
require `edge_semantics_level` set to `profiled` and the referenced evaluation to have
`score_decision` set to `score-change-proposed`. A scoped-module label or score must not be read as
a general-account score.
