# Phenomenon Card: fused determiner-head agreement

**Stress test:** Fused determiner-heads, quantifier construal, and formal-style pressure.

## Description

CGEL treats fused determiner-heads such as `any`, `none`, `either`, and `neither` as showing
agreement patterns that depend on construal and style. When `any` or `none` is construed as
non-count singular, singular agreement is natural:

- `Has any of the money been recovered?`
- `None of the food was contaminated.`

When `none` quantifies over a plural set, both plural and singular verbs are possible:

- `None of them were very serious.`
- `None of them was very serious.`

CGEL also notes that with `either` and `neither` as fused determiner-heads, singular agreement is the
default, while plural agreement is found but likely to be avoided in formal style.

## Source Pointers

- Source IDs: `cgel-subject-verb-agreement`
- Local source: `/Users/brettreynolds/Documents/CGEL/out/058_18 Subjectverb agreement 499.pdf`
- Related cards: [measure-agreement-override-cgel](measure-agreement-override-cgel.md),
  [coordination-agreement-resolution-cgel](coordination-agreement-resolution-cgel.md),
  [fused-head-nps-cgel](fused-head-nps-cgel.md)

## Held-Out Status

This card was not used to build `agreement-controller-override-candidate`. It is a second held-out
agreement subtype, testing whether the graph handles quantifier/fused-head construal and formal-
style pressure without adding new nodes.

## Why It Matters

The card tests whether the agreement graph can separate:

- the controller selected by a fused determiner-head construction;
- singular versus plural construal of the quantified set;
- formal-style pressure against some plural variants;
- reported acceptability and grammaticality attribution.

If the graph survives, it has evidence that `agreement_controller_identification`,
`notional_agreement_basis`, and `agreement_override_pattern` are doing work beyond measure NPs and
coordination.

## Minimum Contrast Cells

- `any` or `none` with non-count singular construal and singular agreement;
- `none` over a plural set with plural agreement;
- `none` over a plural set with singular agreement;
- `either`/`neither` fused determiner-heads with singular default;
- formal-style avoidance of plural variants.

## Candidate Nodes

- agreement_controller_identification
- agreement_feature_alignment
- agreement_override_pattern
- notional_agreement_basis
- standard_language_ideology
- metalinguistic_condemnation
- community_licensing
- reported_acceptability
- grammaticality_attribution

## Potential Construct Pressure

This is a held-out scope test for the agreement graph. A pass supports scoped-module status. A
failure would indicate that fused determiner-head agreement requires a separate category/function
or fused-head construct rather than only agreement-controller machinery.

## Graph Failure Modes

- Treats `none were` and `none was` as the same agreement status under all framings.
- Treats formal-style avoidance as licensing failure.
- Treats fused determiner-head agreement as nearest-NP attraction.
- Requires a surface head-noun controller where the construction supplies a fused head.

## Predicted Discriminators

- `AGR` should survive if fused-head controller identification and notional basis are enough.
- `CAT` may be needed for category analysis, but not for the agreement licensing contrast itself.
- `PROC` should fail as a licensing account.
