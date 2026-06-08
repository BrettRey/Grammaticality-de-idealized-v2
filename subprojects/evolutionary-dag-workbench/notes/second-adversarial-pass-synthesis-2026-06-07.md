# Second Adversarial Pass Synthesis

**Date:** 2026-06-07
**Inputs:** two first-round candidate representations, second critique files, twelve phenomenon cards

## Summary

The two first-round candidates improve on the seed representations, but neither is ready for a
non-zero general score.

`licensing-ideology-split-candidate` is the stronger module for stigmatized, condemned,
regionally licensed, and register-bound cases. It protects `community_licensing` from
`standard_language_ideology`, `metalinguistic_condemnation`, correction, and
`reported_acceptability`.

`opportunity-preemption-operator-gap-candidate` is the stronger module for rare forms,
preemption, transparent free relatives, and left-branch extraction. It protects frequency from
licensing and recoverability from grammaticality.

Their failures are complementary. The first lacks an evidence layer under `community_licensing`.
The second lacks an ideology/context layer over judgment and correction. The next mutation should
therefore be a stratified representation, not a simple winner-take-all graph.

## What Survived

### 1. Community Licensing Must Remain Central But Not Oracular

Both candidate critiques confirm that `community_licensing` is necessary. But the
licensing/ideology graph shows a new risk: if licensing has no evidential inputs, it becomes a
renamed target rather than an explanatory construct.

The next representation needs opportunity-normalized evidence below licensing:

- `opportunity_mass`
- `usage_frequency`
- `constructional_analogy`
- `operator_value`

These should not collapse into licensing. They should function as evidence or scoped constitutive
components.

### 2. Ideology Must Remain Outside Licensing

The opportunity/operator candidate fails the cards where production and condemnation diverge:

- `needs-washed`
- `stigmatized-robust-vernacular`
- `frequent-condemned-form`
- `between-you-and-I`

The next representation needs a separate ideology/context channel:

- `standard_language_ideology`
- `metalinguistic_condemnation`
- `editorial_correction_probability`
- `schooling_instructional_exposure`
- `task_framing`
- `genre`
- `register_genre_appropriateness`
- `speaker_identity`

This channel should affect judgment, correction, and attribution without being treated as the
grammar-state itself.

### 3. Operator Value Should Be Scoped, Not Globalized

The second candidate's most dangerous edge is `operator_value -> community_licensing`. It is useful
for operator-rich constructions, but it can preserve OVMG by assumption if treated as a general
licensing mechanism.

The next representation should keep `operator_value`, but only as a local constitutive wager for
operator-gap cases. Its rationale must say that non-operator cases can be licensed or rejected for
other reasons.

### 4. Judgment Is a Proxy Channel With Multiple Perturbations

`reported_acceptability` should receive pressure from at least four sources:

- `community_licensing`
- `standard_language_ideology`
- `task_framing`
- `processing_cost`

Recoverability should also matter, but only as a response and comprehension channel. It should not
feed directly into licensing.

### 5. Production Needs Two Kinds of Support

`production_probability` should not be caused by licensing alone. Candidate forms may be produced
because they are community licensed, but also because analogical pressure makes them available or
tempting.

The next representation should therefore include:

- `community_licensing -> production_probability`
- `constructional_analogy -> production_probability`

This keeps open the possibility of innovative production without premature community licensing.

## Representation Decision

The next candidate should be:

`stratified-licensing-measurement-candidate`

It should have three explicit layers:

1. Evidence and structure layer: opportunity, frequency, analogy, operator value.
2. Licensing and production layer: community licensing, production probability, repair pressure.
3. Measurement and ideology layer: acceptability, correction, attribution, ideology, task framing,
   register, speaker cues, and processing.

This is still representable as a DAG-shaped JSON file, but it should be treated as a typed module
assembly rather than as the final hypothesis space. The point of the next candidate is to test
whether the workbench can keep construct hygiene while combining the two strongest first-round
survivors.

## Score Discipline

No existing seed or first-round candidate score should change after this pass. The critiques justify
candidate mutation, not promotion.

The new candidate should also start at zero. Its first useful score can only follow an adversarial
critique that tests whether the larger graph has become an overfitted omnibus.

## Next Action

Create `graphs/archive/stratified-licensing-measurement-candidate.json`.

The candidate should explicitly avoid three moves:

- treating `operator_value` as the definition of licensing;
- treating `standard_language_ideology` as the definition of licensing;
- treating `reported_acceptability` or correction as direct access to grammar.
