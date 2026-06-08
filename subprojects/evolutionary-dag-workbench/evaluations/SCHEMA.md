# Evaluation JSON Schema

Protocol-bound tests are stored as JSON so critique results are not only prose notes.

```json
{
  "id": "context-indexed-dynamic-feedback-2026-06-07",
  "target_graph": "graphs/archive/context-indexed-dynamic-feedback-candidate.json",
  "protocol": "notes/conditioning-operationalization-protocol-2026-06-07.md",
  "status": "exploratory",
  "score_decision": "no-score-change",
  "cards": [
    {
      "phenomenon": "needs-washed",
      "result": "survives_as_module",
      "expected_survival_pattern": "Free text.",
      "notes": "Free text.",
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

## Status Values

- `exploratory`
- `protocol-bound`
- `held-out`
- `archived`

## Score Decisions

- `no-score-change`: records an evaluation without authorizing label or score movement.
- `scope-only`: authorizes a scoped/general label but no numeric score movement.
- `score-change-proposed`: authorizes numeric score movement; the target graph must be profiled by
  `edge_semantics_level`.

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
