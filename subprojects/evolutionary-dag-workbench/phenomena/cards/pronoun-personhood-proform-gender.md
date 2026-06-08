# Phenomenon Card: pronoun personhood and pro-form gender

**Stress test:** Reference tracking, personhood, agreement, and social-indexical value.

## Description

Pronoun choice can encode reference tracking, personhood, animacy, gender, institutional policy,
and stance. Some mismatches are agreement or reference-tracking problems; others are social,
ethical, or ideological conflicts over how an entity is to be classified or addressed.

## Source Pointers

- Source IDs: `cgel-pronouns`, `reynolds-personhood-proforms`
- Related seed card: [singular-they](singular-they.md)

## Why It Matters

This card tests whether a graph can distinguish grammatical agreement and reference tracking from
social-indexical value and ideological correction, without denying that they can interact.

## Minimum Contrast Cells

- ordinary pronoun-antecedent agreement in a low-stakes reference task;
- singular `they` with known or unknown antecedent;
- personified or de-personified non-human referent;
- policy- or ideology-framed pronoun judgment.

## Candidate Nodes

- operator_value
- social_indexical_value
- speaker_identity
- audience_design
- community_licensing
- standard_language_ideology
- reported_acceptability
- grammaticality_attribution

## Graph Failure Modes

- Collapses personhood classification into agreement morphology.
- Treats social sanction as grammatical non-licensing.
- Treats reference success as sufficient for licensing.
- Ignores audience design and speaker/ascription effects.

## Predicted Discriminators

- A context graph should predict judgment shifts under policy, audience, and identity framing.
- An operator graph should preserve the reference-tracking role of pronouns without turning every
  social-indexical dispute into operator mismatch.
