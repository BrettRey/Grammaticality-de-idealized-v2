# Eighth Adversarial Pass Synthesis: Audience and Reference Tracking

**Date:** 2026-06-08
**Mutation:** `audience-reference-tracking-candidate`
**Trigger:** `pronoun-personhood-proform-gender` remained only partly handled after the
task-separated feedback mutation.

## Pressure

The prior task-separated graph separated production setting from judgment setting, but it still had
no explicit representation of:

- reference-tracking success;
- pronoun/pro-form feature alignment;
- personhood ascription;
- audience design as a pressure on social-indexical value and reported judgment.

That made it possible to describe pronoun judgments, but not to preserve the card's main
distinction: ordinary reference-tracking/agreement problems differ from social, ethical,
ideological, or policy-framed disputes over pro-form choice.

## Mutation

Added controlled nodes:

- `reference_tracking_success`
- `pronoun_feature_alignment`
- `personhood_ascription`

Created `audience-reference-tracking-candidate`, a compact profiled graph that keeps separate:

- personhood ascription -> pronoun feature alignment;
- pronoun feature alignment -> reference tracking success;
- reference tracking success -> reported acceptability;
- pronoun feature alignment -> operator value -> community licensing;
- audience design and speaker identity -> social-indexical value -> reported acceptability;
- standard-language ideology -> condemnation -> attribution.

The graph explicitly blocks the dangerous shortcuts:

- reference tracking success -> community licensing;
- social-indexical value -> community licensing;
- personhood ascription -> grammaticality attribution.

## Evaluation

Added `evaluations/protocol-tests/audience-reference-tracking-2026-06-08.json`.

Results:

- `pronoun-personhood-proform-gender`: survives as a scoped pronoun/pro-form module.
- `singular-they`: partly survives; the graph supplies personhood/audience/reference structure but
  not diachronic stabilization.
- `stigmatized-robust-vernacular`: partly survives as a social-indexical judgment layer, not as a
  full vernacular-licensing account.

## Decision

No score movement. The graph is useful as a scoped module for pronoun/pro-form judgment channels. It
does not replace the dynamic-context module or the operator-gap module.

The next unresolved discriminator is the operator-gap distinction between collocational rigidity and
argument-linking selection.
