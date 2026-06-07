# Critique: ovmg-seed

**Target:** `graphs/seeds/ovmg-seed.json`
**Family:** operator-value-conditioned-stability
**Pass:** first adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`needs washed` is the most damaging first attack. The seed has `community_licensing`, which is
good, but it lacks standard-language ideology, speaker identity, register, and production probability.
That means it cannot represent the full contrast: a form can be licensed in one community, produced
there, condemned under standard-language ideology, and rejected under correctness framing.

The OVMG seed also risks being too operator-centered for expression-shape and normativity cases.
Left-branch extraction fits the operator-value story. Stigmatized robust vernacular and frequent
condemned forms require more social and measurement structure.

## 2. Category Mistake

The graph risks making `operator_value` a synonym for the grammar-relevant target. The forbidden
conflation file explicitly warns against using `operator_value` as a synonym for every form-meaning
relation. The seed does not go that far, but the constitutive edge into `grammaticality_attribution`
can make the hypothesis look protected by definition.

## 3. Most Damaging Missing Node

`standard_language_ideology`.

Without it, the graph cannot explain why an already licensed form can still be condemned, corrected,
or rejected in a standard-framed task.

Secondary missing nodes:

- `production_probability`
- `task_framing`
- `register_genre_appropriateness`
- `opportunity_mass`

## 4. Most Suspicious Edge

`operator_value -> grammaticality_attribution`.

The edge is labelled constitutive. That is exactly the high-risk move: it may encode the OVMG thesis
as a graph edge before the workbench has tested rival families. It should be marked as a theoretical
wager or replaced by a more explicit target such as an operator-state node distinct from attribution.

## 5. Minimal Mutation

Split the target:

- Keep `operator_value`.
- Add a separate target such as `community_licensing` or an explicitly defined operator-state node.
- Treat `grammaticality_attribution` as an attribution about that target, not the target itself.

Then add:

- `standard_language_ideology`
- `task_framing`
- `production_probability`
- `opportunity_mass`

This would let OVMG survive operator-gap cases without pretending that all grammaticality talk is
exhausted by operator value.

## 6. Score-Readiness Judgment

`partly ready`.

The OVMG seed is promising as a targeted operator-gap model. It is not ready as a general
grammaticality representation until the attribution target is split and ideology/production channels
are added.
