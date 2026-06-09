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

## Source-Checked Contrast Examples

- Pro-form baseline: a pronoun or other pro-form can stand in for an antecedent of a matching or
  recoverable category, but the category match is not always simple.
- Person-form distinction: a 3rd-person form can be used for speaker or addressee reference in
  special contexts, showing that person feature and discourse reference are distinct.
- Gender compatibility: a pronoun can encode a property not encoded by the antecedent, so agreement
  is often compatibility rather than complete feature identity.
- Personification contrast: non-human referents such as countries, ships, cars, and animals can
  receive different pronouns depending on construal, empathy, or social stance.
- De-personhood contrast: `it` with a human baby can be licensed in some contexts but can also carry
  a dehumanizing or affectively marked value.
- Designatum contrast: the local personhood/pro-forms paper treats English pro-form gender as
  driven by how a discourse entity is conceptualized, not by antecedent form alone.
- Chain-coherence contrast: personal and non-personal pro-forms are disfavoured when mixed inside a
  single reference chain unless the discourse independently reclassifies the designatum.

## Source-Checked Evidence

Checked against `cgel-pronouns` and the CGEL gender/agreement section. The source supports the
separation among reference tracking, grammatical form, gender/personhood compatibility, and
social-indexical value. Checked against `reynolds-personhood-proforms`; the local paper strengthens
the designatum, personhood, and reference-chain evidence. The policy/audience-design part of the
card still needs task-specific audience evidence before it can count as fully passed.

## Data Pointers

- `reynolds-personhood-proforms` supplies the strongest local evidence for designatum-driven
  pro-form selection, personal/non-personal chain coherence, and personification or
  de-personification effects.
- The Journal of Linguistics reviewer notes in `Personhood_and_proforms/reviews/` are useful stress
  sources for dialect-sensitive gender/pro-form systems, social identity, and reallocation of
  pronoun patterns.
- The unresolved prediction cell is narrower: it needs a task design that varies audience,
  institution, policy framing, speaker/referent identity, and judgment prompt while separately
  measuring reference success, reported acceptability, grammaticality attribution, and social
  sanction.
- Treat policy or respect judgments as data for `audience_design`, `social_indexical_value`,
  `standard_language_ideology`, and `grammaticality_attribution`; do not treat them as direct
  evidence that `reference_tracking_success` or `community_licensing` changed.

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
