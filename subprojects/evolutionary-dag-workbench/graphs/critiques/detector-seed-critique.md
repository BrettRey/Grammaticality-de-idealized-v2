# Critique: detector-seed

**Target:** `graphs/seeds/detector-seed.json`
**Family:** detector
**Pass:** first adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`between you and I` is the sharpest initial attack. The graph can represent task framing,
standard-language ideology, and reported acceptability, so it can explain why a correctness-framed
judgment shifts. But it has no production side. The phenomenon requires a dissociation between
what speakers produce in casual contexts, what they report under a task, and what they attribute as
"correct" under schooling pressure.

`needs washed` and stigmatized robust vernacular forms create the same pressure in another form:
the detector graph can model a biased judgment channel, but it cannot represent a stable licensed
community repertoire that coexists with standard-language rejection.

## 2. Category Mistake

The seed mostly avoids the obvious mistake of treating reported acceptability as transparent access
to grammar. Its weakness is subtler: `reported_acceptability -> grammaticality_attribution` risks
making the detector output the privileged route into attribution without an explicit attribution
process, authority source, or community-indexing layer.

## 3. Most Damaging Missing Node

`production_probability`.

Without production probability, the graph cannot handle production/judgment dissociations. It can
say why a response changes in a judgment task, but not why production can remain stable while
reported acceptability or grammaticality attribution shifts.

Secondary missing nodes:

- `schooling_instructional_exposure`
- `register_genre_appropriateness`
- `speaker_identity`

## 4. Most Suspicious Edge

`reported_acceptability -> grammaticality_attribution`.

The edge is labelled evidential, which is better than causal or constitutive. Still, by making judgment
reports the only downstream evidence for attribution, the graph underweights correction authority,
production evidence, community licensing, and register conditioning.

## 5. Minimal Mutation

Add a production and authority channel:

- `production_probability`
- `schooling_instructional_exposure`
- `register_genre_appropriateness`

Then add edges:

- `community_licensing -> production_probability`
- `standard_language_ideology -> grammaticality_attribution`
- `schooling_instructional_exposure -> standard_language_ideology`
- `register_genre_appropriateness -> reported_acceptability`

This would make the detector model harder to kill because judgment reports would become one
fallible measurement channel among several, not the whole evidential path.

## 6. Score-Readiness Judgment

`partly ready`.

The detector seed has good measurement instincts, but it is not ready for non-zero scoring until it
can represent production/judgment dissociation and community-indexed licensing.
