# Critique: dynamic-feedback-seed

**Target:** `graphs/seeds/dynamic-feedback-seed.json`
**Family:** time-indexed-feedback
**Pass:** first adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`singular they` is the strongest attack. The seed represents a legal feedback loop over time:
production affects usage, usage affects entrenchment, entrenchment affects reported acceptability,
and reported acceptability feeds later production. But singular `they` also involves metalinguistic
condemnation, institutional change, standard-language ideology, and community licensing. Those
forces can move against usage or lag behind it.

The seed's feedback loop is therefore too thin. It models exposure dynamics, not norm dynamics.

## 2. Category Mistake

The graph risks treating feedback from reported acceptability to later production as if acceptance
were the main social mechanism. That is not illegal as a time-lagged relation, but it leaves out the
authority, correction, and register channels that often mediate whether reported acceptance matters.

## 3. Most Damaging Missing Node

`community_licensing`.

Without community licensing, the dynamic loop cannot distinguish "more familiar" from "licensed
in this community/register." It also cannot handle stigmatized robust vernacular forms, where
production and community licensing may remain high while reported acceptability under standard
framing is low.

Secondary missing nodes:

- `standard_language_ideology`
- `metalinguistic_condemnation`
- `opportunity_mass`
- `editorial_correction_probability`

## 4. Most Suspicious Edge

`entrenchment_t1 -> reported_acceptability_t1`.

The edge is plausible, but too much rests on it. Entrenchment can raise familiarity, speed, or felt
naturalness; reported acceptability depends on task framing, ideology, and register cues as well.
In this seed, the edge makes entrenchment look like a direct route to acceptance.

## 5. Minimal Mutation

Keep the time-indexed representation, but add a parallel norm loop:

- `community_licensing_t1`
- `standard_language_ideology_t1`
- `metalinguistic_condemnation_t1`
- `editorial_correction_probability_t1`

Then route reported acceptability through task and norm variables, not only entrenchment. Add
`opportunity_mass_t1` so rarity can be separated from lack of licensing.

This seed is also a candidate for a representation mutation: a dynamic model with multiple coupled
time-indexed processes may be a better fit than a single DAG-shaped file.

## 6. Score-Readiness Judgment

`partly ready`.

The seed demonstrates legal feedback, but it is not substantively ready until the feedback model
contains norm, licensing, and opportunity channels.
