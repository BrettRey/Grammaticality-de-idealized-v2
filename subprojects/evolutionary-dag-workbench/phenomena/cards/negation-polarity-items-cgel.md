# Phenomenon Card: negation and polarity items

**Stress test:** Polarity licensing, semantic transparency, and dialect/norm pressure.

## Description

Polarity-sensitive items separate meaning recovery from licensing. A hearer may recover the
intended negative or emphatic meaning even when the relevant polarity environment is missing,
contested, or treated differently across varieties.

## Source Pointers

- Source IDs: `cgel-negation-polarity`

## Why It Matters

The case tests whether graphs can represent operator licensing environments without reducing
negative meaning, polarity form, dialect licensing, and standard condemnation to the same node.

## Minimum Contrast Cells

- polarity item in a licensed negative or downward-entailing environment;
- polarity item outside a licensed environment but with recoverable intended meaning;
- negative concord or related dialectal pattern;
- standard-language correction of a dialect-licensed negative pattern.

## Source-Checked Contrast Examples

- Licensed NPI baseline: items such as negative-oriented `any` occur in negative, interrogative, or
  other non-affirmative contexts.
- Unlicensed-environment contrast: the same item can be unacceptable in a plain affirmative context
  even when a hearer can recover the intended meaning.
- Sense split: forms such as `any` can have a free-choice sense that is not the same polarity item,
  so form identity alone is not licensing.
- Idiom contrast: a phrase can retain negative meaning as an idiom even when the original polarity
  environment has changed.
- Standardness contrast: CGEL's multiple-negation section distinguishes Standard English multiple
  semantic negation from negative concord in non-standard dialects, with standard NPI alternatives
  for the non-standard concord examples.

## Source-Checked Evidence

Checked against `cgel-negation-polarity`, including the multiple-negation section. The source
strongly supports polarity licensing, the recoverability/licensing split, and the dialect/standard
negative-concord contrast. It supports the workbench's source-backed standard-correction cell, while
still leaving corpus distribution and social-evaluation strength for later empirical work.

## Candidate Nodes

- operator_value
- community_licensing
- standard_language_ideology
- semantic_pragmatic_recoverability
- reported_acceptability
- grammaticality_attribution
- metalinguistic_condemnation

## Graph Failure Modes

- Treats recoverable negative meaning as licensing.
- Treats standard condemnation as dialect-general non-licensing.
- Treats all polarity effects as semantic anomaly.
- Ignores the conditioning role of variety and task framing.

## Predicted Discriminators

- A context-indexed graph should predict divergence between local licensing and standard
  correction.
- An operator-gap graph should predict low licensing when a polarity item lacks the required
  environment even if the intended meaning is clear.
