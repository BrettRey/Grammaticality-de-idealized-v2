# Phenomenon Card: non-finite and verbless clause boundaries

**Stress test:** Clause recognition, fragment licensing, genre, and medium.

## Description

Non-finite and verbless clauses create forms that can be fully interpretable and locally licensed
without looking like canonical finite sentences. Their status often depends on construction type,
genre, medium, and whether the task asks for a sentence, a message, a heading, or an utterance.

## Source Pointers

- Source IDs: `cgel-nonfinite-verbless`
- Related seed card: [register-bound-fragments](register-bound-fragments.md)

## Why It Matters

The case tests whether a graph can represent recognizability and genre licensing without treating
finite full clauses as the only grammatical target.

## Minimum Contrast Cells

- licensed non-finite clause in a larger construction;
- verbless clause or supplement with clear discourse role;
- headline, sign, list item, or message fragment;
- formal sentence-correction task.

## Source-Checked Contrast Examples

- Embedded non-finite baseline: infinitival, gerund-participial, and past-participial clauses occur
  as complements, modifiers, and supplements.
- Subjectless non-finite contrast: a non-finite clause can lack an overt subject while still being a
  clause, with interpretation recovered from matrix or discourse context.
- Hollow-clause contrast: a missing non-subject can be recoverable from the matrix clause without
  being an arbitrary ellipsis.
- Verbless-clause contrast: dependent or supplement clauses can have subject-predicate structure
  without a verbal predicate.
- Formal sentence-task contrast: asking whether a string is a canonical finite sentence should
  produce different judgments from asking whether it is licensed as a clause, supplement, heading,
  answer fragment, or message.

## Source-Checked Evidence

Checked against `cgel-nonfinite-verbless`. The source supports the prediction that finite-sentence
status is not a safe proxy for clause licensing, and that genre/task framing should affect
acceptability and grammaticality attribution.

## Candidate Nodes

- register_genre_appropriateness
- genre
- medium
- task_framing
- community_licensing
- grammaticality_attribution
- reported_acceptability
- semantic_pragmatic_recoverability

## Graph Failure Modes

- Treats all non-finite or verbless forms as fragments.
- Treats all fragments as ungrammatical.
- Ignores genre and medium conditioning.
- Uses finite-sentence status as a proxy for community licensing.

## Predicted Discriminators

- A context-indexed graph should predict strong task and medium effects.
- A syntax-only graph should fail if it cannot separate sentence-correction judgments from
  situated utterance licensing.
