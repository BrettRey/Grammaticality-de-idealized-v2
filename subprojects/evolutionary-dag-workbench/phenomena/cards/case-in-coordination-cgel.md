# Phenomenon Card: case in coordination

**Stress test:** Case form, coordination, hypercorrection, and standard ideology.

## Description

Coordinated pronouns create cases where production, correction, and explicit grammaticality
attribution can diverge. A form may be common enough in speech, strongly condemned in
schooling/editing contexts, and variably accepted depending on whether the task frames the issue
as case, coordination, naturalness, or correctness.

## Source Pointers

- Source IDs: `cgel-case`
- Related seed card: [between-you-and-I](between-you-and-I.md)

## Why It Matters

The case tests whether a graph can distinguish local production probability, standard-language
ideology, and community licensing without letting a correction norm define the target construct.

## Minimum Contrast Cells

- ordinary object-case pronoun outside coordination;
- coordinated pronoun in informal production;
- coordinated pronoun in formal correctness judgment;
- explicit school-rule or editor framing.

## Source-Checked Contrast Examples

- Non-coordinate baseline: a single pronoun in subject position contrasts with a single pronoun in
  object or prepositional-complement position.
- Coordination-sensitive standard pattern: a coordinated pronoun follows the case that would be
  expected if one pronoun replaced the whole coordination.
- Stigmatized production pattern: accusative pronouns appear in subject coordinations in informal
  or non-standard varieties.
- Frequent condemned pattern: final-coordinate nominatives appear in object or prepositional
  environments, with `between you and I` as the familiar usage-advice case.
- Formal correction frame: school or usage-manual framing treats some coordination patterns as
  errors even where CGEL treats the final-coordinate `I` pattern as broadly established.

## Source-Checked Evidence

Checked against `cgel-case`, especially the coordination subsection. The source supports the
prediction that coordination creates a production/correction split and that prescriptive correction
should not be treated as direct evidence of global non-licensing.

## Candidate Nodes

- standard_language_ideology
- schooling_instructional_exposure
- task_framing
- production_probability
- reported_acceptability
- grammaticality_attribution
- editorial_correction_probability
- community_licensing

## Graph Failure Modes

- Treats condemnation as evidence of non-licensing without conditioning on norm centre.
- Treats production frequency as sufficient for licensing.
- Fails to represent task-framing effects on reported acceptability.
- Collapses coordination-specific case pressure into a general pronoun-case rule.

## Predicted Discriminators

- A dynamic/context graph should predict production-correction dissociation across norm centres.
- An operator-gap graph should pass only if it can identify the relevant operator or form-selection
  contrast, rather than treating all case correction as operator value.
