# Evaluation JSON Schema

Protocol-bound tests are stored as JSON so critique results are not only prose notes.

```json
{
  "id": "context-indexed-dynamic-feedback-2026-06-07",
  "target_graph": "graphs/archive/context-indexed-dynamic-feedback-candidate.json",
  "protocol": "notes/conditioning-operationalization-protocol-2026-06-07.md",
  "status": "exploratory",
  "held_out_from": [
    "Required when status is held-out; use phenomenon card IDs or evaluation IDs."
  ],
  "score_decision": "no-score-change",
  "activated_paths": [
    {
      "id": "ideology-to-acceptability",
      "phenomenon": "needs-washed",
      "contrast_cell": "regional-naturalness",
      "expected_path_reading": "indeterminate",
      "prediction": "Free text naming the expected path-level contrast.",
      "edges": [
        {
          "source": "standard_language_ideology_t1",
          "target": "reported_acceptability_t1",
          "type": "causal"
        }
      ]
    }
  ],
  "cards": [
    {
      "phenomenon": "needs-washed",
      "result": "survives_as_module",
      "expected_survival_pattern": "Free text.",
      "notes": "Free text.",
      "requirements": {
        "required_nodes": [
          "community_licensing_t1",
          "reported_acceptability_t1"
        ],
        "forbidden_nodes": [
          "operator_value_t1"
        ],
        "required_edges": [
          {
            "source": "community_licensing_t1",
            "target": "reported_acceptability_t1",
            "type": "measurement"
          }
        ],
        "forbidden_edges": [
          {
            "source": "reported_acceptability_t1",
            "target": "community_licensing_t1",
            "type": "causal"
          }
        ]
      },
      "contrast_cells": [
        {
          "id": "regional-naturalness",
          "axes": {
            "community": "Regional vernacular community.",
            "norm_centre": "Local norm centre.",
            "genre": "Informal interaction.",
            "medium": "Speech.",
            "task_framing": "Naturalness.",
            "speaker_identity": "Local in-group cue."
          }
        }
      ]
    }
  ]
}
```

## Required Top-Level Fields

- `id`
- `target_graph`
- `protocol`
- `status`
- `score_decision`
- `cards`

`activated_paths` is optional unless `score_decision` is `score-change-proposed`.

## Status Values

- `exploratory`
- `protocol-bound`
- `held-out`
- `archived`

Evaluations with `status` `held-out` must include a non-empty `held_out_from` list. Each item must
resolve to a phenomenon card ID or evaluation ID. This does not prove projectibility, but it prevents
the held-out label from being pure ceremony.

## Score Decisions

- `no-score-change`: records an evaluation without authorizing label or score movement.
- `scope-only`: authorizes a scoped/general label but no numeric score movement.
- `score-change-proposed`: authorizes numeric score movement; the target graph must be profiled by
  `edge_semantics_level`, and the evaluation must include `activated_paths`.

## Activated Paths

Activated paths make path-level prediction commitments explicit without requiring every graph edge
to be interpreted. Each activated path must include:

- `id`
- `phenomenon`
- `contrast_cell`
- `prediction`
- `edges`

The `phenomenon` must be one of the evaluation's cards. The `contrast_cell` must be present in that
card. Each edge reference must name `source`, `target`, and `type`, and must resolve to an edge in
the target graph. Consecutive edge references must form a directed path.

When `score_decision` is `score-change-proposed`, every activated edge must have a
`relation_profile` on the target graph edge and each path must include `expected_path_reading`.
For `no-score-change` and `scope-only` evaluations, activated paths and expected readings are allowed
as pre-registration scaffolding but do not authorize numeric scores.

Allowed path readings:

- `positive`: all traversed profiles are sign-propagating and multiply to a positive relation.
- `negative`: all traversed profiles are sign-propagating and multiply to a negative relation.
- `warranting`: all traversed profiles are evidential warrant profiles.
- `undercutting`: all traversed profiles are evidential undercut profiles.
- `component`: all traversed profiles are constitutive component profiles.
- `indeterminate`: at least one traversed profile is contextual, thresholded, or task-biased.
- `non_sign_propagating`: the path mixes profile families, such as component plus evidential plus
  causal edges.
- `unprofiled`: at least one traversed edge has no relation profile.

If `expected_path_reading` is present, the validator compares it with the reading computed from the
target graph's `relation_profile` values.

## Card Requirements

Each card may include a `requirements` object to make pass/fail criteria machine-checkable against
the target graph. Allowed keys:

- `required_nodes`
- `forbidden_nodes`
- `required_edges`
- `forbidden_edges`

Node values are exact target-graph node IDs. For time-sliced graphs, use the time-sliced ID such as
`community_licensing_t1`.

Edge values are objects with `source`, `target`, and `type`. Required edges must exist in the target
graph. Forbidden edges must not exist in the target graph. Requirements are evaluated per card, so a
single graph can survive one card while explicitly failing or going out of scope on another.

## Card Results

- `survives_as_module`
- `partly_survives`
- `fails`
- `fails_general_out_of_scope`
- `exploratory`

## Allowed Contrast-Cell Axes

- `community`
- `norm_centre`
- `genre`
- `medium`
- `task_framing`
- `speaker_identity`

Each contrast cell must include a non-empty `axes` object with all six axes listed above. Each axis
value must be a non-empty string. The validator checks that `target_graph`, `protocol`, and each
phenomenon card path exist.
