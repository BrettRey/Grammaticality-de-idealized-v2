# Critique: normativity-heavy-seed

**Target:** `graphs/seeds/normativity-heavy-seed.json`
**Family:** normativity-heavy
**Pass:** first adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`needs washed` is the strongest attack. The seed can represent standard-language ideology,
condemnation, correction, and judgment shifts. But `needs washed` is robustly licensed in some
regional communities while being condemned elsewhere. A normativity-only graph has no way to
represent the local licensed repertoire that survives the condemnation.

Stigmatized robust vernacular forms create the same failure. The graph has institutional rejection
but no community licensing.

## 2. Category Mistake

The graph risks treating institutional correction as evidence for grammatical failure. The edge is
labelled evidential, which helps, but the absence of `community_licensing` means the correction
channel has no competing licensing channel to be evidence against.

## 3. Most Damaging Missing Node

`community_licensing`.

Without it, the graph cannot distinguish "condemned by a standard-language institution" from
"unlicensed in the relevant speech community."

Secondary missing nodes:

- `production_probability`
- `speaker_identity`
- `genre`
- `social_indexical_value`

## 4. Most Suspicious Edge

`editorial_correction_probability -> grammaticality_attribution`.

As an evidential edge, it is defensible. As the only path into attribution, it overweights correction
and underweights production, community-specific licensing, and speaker/register conditioning.

## 5. Minimal Mutation

Add a licensing track beside the ideology track:

- `community_licensing`
- `production_probability`
- `speaker_identity`
- `genre`

Then add edges that allow:

- `community_licensing -> production_probability`
- `speaker_identity -> reported_acceptability`
- `genre -> reported_acceptability`
- `standard_language_ideology -> metalinguistic_condemnation`

The graph becomes harder to kill once condemnation and licensing can diverge instead of being
forced into one normative chain.

## 6. Score-Readiness Judgment

`not ready`.

The seed is useful as a normativity module, but as a full representation it fails precisely where the
workbench needs construct hygiene: standardness is not community licensing.
