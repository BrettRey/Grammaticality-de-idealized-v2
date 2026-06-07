# Critique: usage-heavy-seed

**Target:** `graphs/seeds/usage-heavy-seed.json`
**Family:** usage-heavy
**Pass:** first adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`frequent condemned form` is the strongest attack. The seed can model usage frequency, opportunity
mass, entrenchment, production probability, and reported acceptability. But it cannot represent a
form that is frequent in production while still being condemned in usage guides, classrooms, or
editing contexts.

`needs washed` also hurts the graph: regional licensing and standard-language rejection can diverge
even when usage patterns are stable.

## 2. Category Mistake

The graph risks converting entrenchment into acceptance. It correctly separates raw frequency from
opportunity mass, but the path `usage_frequency -> entrenchment -> reported_acceptability` has no
ideology, register, correction, or speaker-cue channel. That makes familiarity too close to reported
acceptability.

## 3. Most Damaging Missing Node

`standard_language_ideology`.

Without it, the graph cannot explain frequent condemned forms or production/judgment splits under
correctness framing.

Secondary missing nodes:

- `community_licensing`
- `metalinguistic_condemnation`
- `editorial_correction_probability`
- `task_framing`

## 4. Most Suspicious Edge

`entrenchment -> reported_acceptability`.

Entrenchment can influence ease, familiarity, and production, but reported acceptability is filtered
through task framing, ideology, and register. This edge needs mediators or competing causes.

## 5. Minimal Mutation

Add a norm and licensing layer:

- `community_licensing`
- `standard_language_ideology`
- `metalinguistic_condemnation`
- `task_framing`

Then route:

- `entrenchment -> production_probability`
- `community_licensing -> reported_acceptability`
- `standard_language_ideology -> reported_acceptability`
- `standard_language_ideology -> metalinguistic_condemnation`

This mutation would let the seed preserve its strength on rare licensed forms while surviving
frequent condemned forms.

## 6. Score-Readiness Judgment

`partly ready`.

The seed has the best opportunity/frequency hygiene of the archive, but it is not score-ready until
frequency, licensing, ideology, and judgment are all separated.
