# Graph Scoring Rubric

Keep dimensions separate. A total score is useful only as a triage device.

## Score Scope

Scores are scoped. A graph can be labelled as a `scoped_module` without being scored as a
`general_account`.

Scoped and general labels require `score_status.kind` and `score_status.evaluation` in the graph
JSON. The referenced evaluation must target the labelled graph, use `status` `protocol-bound` or
`held-out`, and use `score_decision` `scope-only` or `score-change-proposed`.

Non-zero scores additionally require `score_decision` `score-change-proposed`. No graph should
receive a `general_account` score unless it has survived protocol-bound held-out tests across the
workbench's phenomenon space.

Score movement also requires `edge_semantics_level` `profiled`. Absent edge profiles mean the graph
has not committed an interpretable prediction path for numeric comparison.

Each dimension is scored from 0 to 5 inclusive. Do not treat a one-point difference as meaningful
until held-out or parameterized evaluations make the scale comparable across graphs.

Current numeric scores are placeholders. Treat scoped-module labels and evaluation links as the
auditable result until held-out or parameterized tests make numeric comparison meaningful.

## Positive Dimensions

`empirical_coverage`

How many phenomenon cards does the graph handle without ad hoc repair?

`projective_power`

What held-out contrast cell does the graph forecast before seeing the result? This dimension should
carry more weight than coverage once held-out evaluations exist, because coverage of cards used to
build a graph demonstrates maintenance, not projectibility.

`counterexample_resilience`

How well does the graph survive adversarial cards: rare licensed forms, frequent condemned forms, stigmatized robust forms, processing illusions, and register-bound forms?

`measurement_clarity`

Does the graph distinguish constructs from proxies and specify what each observation measures?

`explanatory_payoff`

Does the graph explain why the pattern occurs, not just classify it?

`cross_domain_stability`

Does the graph preserve useful structure across usage, processing, normativity, pedagogy, corpus distribution, and diachrony?

## Penalties

`complexity_penalty`

Too many nodes or edges relative to explanatory gain.

`circularity_penalty`

Outcome variable used as its own cause; graph smuggles in the answer.

`construct_confusion_penalty`

Acceptability-as-grammaticality, frequency-as-licensing, correction-as-impossibility, or similar conflation.

`theory_preservation_penalty`

The graph preserves a named theory, paper, or familiar account by assumption rather than improving
contrast-cell prediction, construct separation, or held-out projectibility.

## Triage Formula

```text
score = empirical_coverage
      + projective_power
      + counterexample_resilience
      + measurement_clarity
      + explanatory_payoff
      + cross_domain_stability
      - complexity_penalty
      - circularity_penalty
      - construct_confusion_penalty
      - theory_preservation_penalty
```

Use the formula for sorting, not for final adjudication.
