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
