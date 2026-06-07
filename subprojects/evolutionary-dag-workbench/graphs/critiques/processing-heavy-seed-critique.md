# Critique: processing-heavy-seed

**Target:** `graphs/seeds/processing-heavy-seed.json`
**Family:** processing-heavy
**Pass:** first adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`needs washed` is the strongest attack. The processing-heavy seed can explain why something feels
awkward, natural, easy, or hard under a task. It cannot explain a regionally licensed form that is
systematic and usable while being condemned under standard-language ideology.

`frequent condemned form` and stigmatized robust vernacular forms produce the same failure. The
seed has no social, licensing, production, or normative structure.

## 2. Category Mistake

The seed risks turning felt naturalness into the whole target. It does distinguish
`felt_naturalness_context` from `reported_acceptability`, but it has no `community_licensing` or
`grammaticality_attribution` node. As a result, low acceptability remains too close to low naturalness.

## 3. Most Damaging Missing Node

`community_licensing`.

Without it, the graph cannot say that a form is licensed despite being hard, stigmatized, rare, or
task-disfavored.

Secondary missing nodes:

- `grammaticality_attribution`
- `standard_language_ideology`
- `production_probability`
- `register_genre_appropriateness`

## 4. Most Suspicious Edge

`felt_naturalness_context -> reported_acceptability`.

The edge is labelled measurement, but reported acceptability is not merely a measurement of felt
naturalness. It is also affected by task wording, ideology, register, speaker cueing, and theoretical
or metalinguistic attribution.

## 5. Minimal Mutation

Keep the processing channel, but subordinate it to a broader measurement model:

- Add `community_licensing`.
- Add `grammaticality_attribution`.
- Add `standard_language_ideology`.
- Add `register_genre_appropriateness`.

Then represent processing as one perturbing channel into reported acceptability and felt naturalness,
not as the whole explanation.

## 6. Score-Readiness Judgment

`not ready`.

The seed is useful as a processing module. As a general representation, it fails too many social,
normative, and licensing cards.
