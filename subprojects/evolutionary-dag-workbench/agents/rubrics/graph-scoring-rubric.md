# Graph Scoring Rubric

Keep dimensions separate. A total score is useful only as a triage device.

## Positive Dimensions

`empirical_coverage`

How many phenomenon cards does the graph handle without ad hoc repair?

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

## Triage Formula

```text
score = empirical_coverage
      + counterexample_resilience
      + measurement_clarity
      + explanatory_payoff
      + cross_domain_stability
      - complexity_penalty
      - circularity_penalty
      - construct_confusion_penalty
```

Use the formula for sorting, not for final adjudication.
