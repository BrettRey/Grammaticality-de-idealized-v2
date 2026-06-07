# Graph JSON Schema

Seed and archive graphs are stored as JSON. The local validator checks simple graph structure.
The linter also checks node IDs against `ontology/nodes.yaml`, `family`, `status`, and seed
score discipline.

```json
{
  "id": "usage-heavy-seed",
  "title": "Usage-heavy seed graph",
  "family": "usage-heavy",
  "status": "seed",
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
      "rationale": "Repeated exposure can change learned accessibility."
    }
  ],
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

## Dynamic Feedback

If a graph needs feedback, use explicit time slices or `time_lagged` edges. The validator excludes `time_lagged` edges from synchronic cycle checks.

Same-slice mutual dependence is not represented as reciprocal directed edges. If a graph claims
co-constitution within a single timescale, it should either explain the acyclic constitutive
direction it chooses or mark the move as a theoretical wager.

## Scoring

Seed graphs carry complete all-zero `scores` blocks. Non-zero scores should be added only after an
adversarial critique exists in `graphs/critiques/` or an equivalent review note is linked.
