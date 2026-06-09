# Phenomenon Card: measure agreement override

**Stress test:** Plural measure NPs, singular construal, and held-out agreement projection.

## Description

CGEL treats some formally plural measure NPs as licensing singular agreement when the NP is construed
as a single measure of time, money, distance, or a similar quantity:

- `That ten days we spent in Florida was fantastic`;
- `Twenty dollars seems a ridiculous amount to pay to go to the movies`;
- `Five miles is rather more than I want to walk this afternoon`.

This is the opposite direction from collective plural override. A formally plural expression can be
respecified as singular because the relevant controller is a single measure, not a set of individual
days, dollars, or miles.

## Source Pointers

- Source IDs: `cgel-subject-verb-agreement`
- Local source: `/Users/brettreynolds/Documents/CGEL/out/058_18 Subjectverb agreement 499.pdf`
- Related cards: [collective-number-transparent-agreement-cgel](collective-number-transparent-agreement-cgel.md),
  [coordination-agreement-resolution-cgel](coordination-agreement-resolution-cgel.md),
  [subject-verb-agreement-cgel](subject-verb-agreement-cgel.md)

## Held-Out Status

This card was not used to build `agreement-controller-override-candidate`. It is a first projection
test for whether the candidate's `agreement_override_pattern` and `notional_agreement_basis`
constructs generalize beyond collective nouns, number-transparent expressions, coordination, and
nearest-attractor errors.

## Why It Matters

The card tests whether the agreement graph can predict an override direction that was not among the
build cards. If the graph simply memorized "collective plural" or "coordination singular", it should
fail here. If it really separates notional basis, controller identification, override pattern, and
feature alignment, it should survive.

## Minimum Contrast Cells

- formally plural measure NP construed as a single measure with singular agreement;
- formally plural NP construed as individual plural items with plural agreement;
- measure NP plus singular predicative complement where singular agreement is obligatory;
- distance or amount expression where singular override is optional but preferred.

## Candidate Nodes

- agreement_controller_identification
- agreement_feature_alignment
- agreement_override_pattern
- notional_agreement_basis
- community_licensing
- repair_reformulation_pressure
- reported_acceptability
- grammaticality_attribution

## Potential Construct Pressure

This is a held-out test of the agreement-controller graph, not a reason to grow it immediately. A
pass supports the claim that `agreement_override_pattern` is more than a name for the build cards.
A failure would mean the graph needs a finer distinction between measure respecification and other
override patterns.

## Graph Failure Modes

- Treats plural measure singular agreement as a processing or proximity error.
- Treats measure override as the same pattern as collective plural override.
- Treats the head noun's surface plurality as the only controller.
- Treats singular agreement as a usage-guide preference rather than licensed agreement in the
  relevant construction.

## Predicted Discriminators

- `AGR` should survive if controller identification and notional basis are doing real work.
- `OPG` should remain partial because broad operator value cannot identify the measure controller.
- `PROC` should fail as a licensing account because the contrast is not a nearest-attractor error.
