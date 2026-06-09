# Phenomenon Card: coordination agreement resolution

**Stress test:** Agreement controller choice, override patterns, and proximity advice.

## Description

CGEL treats agreement with coordinated subjects as more structured than a simple nearest-noun rule.
And-coordinations normally take plural agreement, but singular agreement is licensed when the
coordination is construed as a single unit, when two descriptions identify one participant, or when
distributive determiners such as `each` or `every` set up a singular agreement pattern:

- `Mary and John are here`;
- `Eggs and bacon is my favourite breakfast`;
- `Our chef and chauffeur has decided to emigrate` under the one-person reading;
- `Each dog and each cat has to be registered`.

Or-coordination adds another pressure point. A pair of singular coordinates selects singular
agreement, but mixed-number cases are unstable enough that CGEL notes awkwardness and avoidance
strategies rather than a clean proximity rule. Supplements and corrections can also determine the
agreement target:

- `Mary or John is sure to go`;
- `Mary or the twins` plus a finite verb creates a difficult mixed-number choice;
- `His proposal, or rather the ramifications of it, are going to have a serious effect`;
- `Her eyes, or rather the visible one, was pale blue`.

## Source Pointers

- Source IDs: `cgel-subject-verb-agreement`
- Local source: `/Users/brettreynolds/Documents/CGEL/out/058_18 Subjectverb agreement 499.pdf`
- Related cards: [subject-verb-agreement-cgel](subject-verb-agreement-cgel.md),
  [proximity-agreement-error-cgel](proximity-agreement-error-cgel.md),
  [collective-number-transparent-agreement-cgel](collective-number-transparent-agreement-cgel.md),
  [nearest-noun-agreement-attraction](nearest-noun-agreement-attraction.md)

## Why It Matters

This card forces agreement to split into at least three mechanisms: controller identification,
licensed override, and processing or production attraction. A broad operator-value graph can say
that agreement is grammar-relevant, and a processing graph can handle nearest-attractor errors, but
neither predicts the licensed singular/plural choices across coordination.

## Minimum Contrast Cells

- ordinary and-coordination with plural agreement;
- unit-construal and-coordination with singular agreement;
- one-participant role coordination with singular agreement;
- distributive `each`/`every` coordination with singular agreement;
- mixed-number or-coordination with avoidance/proximity pressure;
- supplement or correction where the correcting phrase controls agreement.

## Candidate Nodes

- agreement_controller_identification
- agreement_feature_alignment
- agreement_override_pattern
- notional_agreement_basis
- retrieval_attractor_salience
- community_licensing
- reported_acceptability
- repair_reformulation_pressure
- grammaticality_attribution

## Potential Construct Pressure

This card is strong pressure for an agreement-controller/override graph. It is not enough to add a
single agreement node: the graph must keep controller choice, licensed override, and attraction
pressure separate.

## Graph Failure Modes

- Treats all coordination agreement as nearest-noun proximity.
- Treats all singular agreement with coordination as error.
- Treats all agreement variation as community ideology or reported acceptability.
- Collapses unit construal, one-participant identity, distributive coordination, mixed-number
  or-coordination, and correction/supplement agreement into one rule.

## Predicted Discriminators

- `OPG` should partly survive only as broad grammar-relevance scaffolding.
- `PROC` should partly survive only for attraction and unstable mixed-number judgments.
- A new agreement-controller graph should survive as a narrow module if it keeps controller,
  override, and attractor constructs separate.
