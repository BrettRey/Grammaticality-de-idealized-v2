# Phenomenon Card: dependency-locality alternations

**Stress test:** Licensed alternatives with different processing and production profiles.

## Description

Some alternations preserve licensing and broad meaning while changing dependency length. Gibson's
examples include particle placement, dative ordering, subject/object length asymmetries, and
quotation order. The shorter-dependency variant is often easier and more probable, but the
longer-dependency variant is not thereby unlicensed.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`
- Related cards: [grammatical-but-hard](grammatical-but-hard.md),
  [center-embedding](center-embedding.md)

## Why It Matters

The case separates grammatical licensing from locality-driven production probability and felt
naturalness. It also tests whether a processing module can predict comparative preferences without
turning awkwardness into grammatical failure.

## Minimum Contrast Cells

- short-dependent-before-long-dependent order in a head-initial construction;
- long-dependent-before-short-dependent order with the same broad semantic payload;
- short/short or local/local baseline where the alternation is not strongly differentiated;
- head-final or cross-linguistic comparison where the locality preference reverses or changes.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive`, especially chapters 4 and 5. The source supports the
claim that dependency length affects production and processing preferences, while also warning that
dependency locality is a compressed approximation rather than a complete processing theory.

## Candidate Nodes

- processing_cost
- production_probability
- reported_acceptability
- felt_naturalness_context
- semantic_pragmatic_recoverability
- measurement_task

## Graph Failure Modes

- Treats lower naturalness as licensing failure.
- Treats equal licensing as enough to predict equal production probability.
- Ignores cross-linguistic/head-direction conditioning on locality preferences.
- Treats dependency length as the whole mechanism rather than a useful predictor.

## Predicted Discriminators

- `PROC` should predict lower felt naturalness and acceptability for high-locality-cost variants
  without lowering licensing.
- `DYN` should not explain the preference only through community licensing or ideology.
- `OPG` should remain out of scope unless an alternation involves an actual dependency-licensing
  gap.
