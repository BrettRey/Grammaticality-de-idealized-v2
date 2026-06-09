# Phenomenon Card: legalese center embedding

**Stress test:** Genre-stabilized complexity without licensing failure.

## Description

Legal prose contains unusually high rates of center embedding and long dependency distances. Plain
English paraphrases can preserve propositional content while reducing processing cost. The complex
form persists because it is genre-stabilized and official-sounding, not because readers find it
clearer or more acceptable.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`
- Related cards: [center-embedding](center-embedding.md),
  [register-bound-fragments](register-bound-fragments.md)

## Why It Matters

The case forces a three-way separation among licensing, processing burden, and genre/register
pressure. It also tests whether high production probability in a professional genre can coexist
with low comprehension and low preference.

## Minimum Contrast Cells

- legalese version with center embedding and long dependencies;
- plain-English paraphrase with the same propositional content;
- lawyer versus lay-reader comprehension and preference tasks;
- officialness or genre-fit judgment separated from comprehension.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive` chapter 6. The source reports that legalese has unusually
high center-embedding rates, that plain-English versions improve comprehension/recall, and that
lawyers as well as laypeople prefer the plain versions despite legalese persistence.

## Candidate Nodes

- genre
- register_genre_appropriateness
- processing_cost
- production_probability
- reported_acceptability
- felt_naturalness_context
- audience_design
- standard_language_ideology
- measurement_task

## Graph Failure Modes

- Treats high genre frequency as high felt naturalness.
- Treats low comprehension as ungrammaticality.
- Treats legal genre fit as ordinary community licensing.
- Ignores audience differences between officialness, comprehension, and preference tasks.

## Predicted Discriminators

- `PROC` should capture processing and comprehension burden.
- `DYN` or `TASK` should be needed for genre persistence, professional production, and task-framing
  effects.
- A graph that equates production probability, acceptability, and licensing should fail.
