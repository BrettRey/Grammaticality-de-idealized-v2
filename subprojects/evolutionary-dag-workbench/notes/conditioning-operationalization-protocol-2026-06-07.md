# Conditioning Operationalization Protocol

**Date:** 2026-06-07
**Purpose:** prevent context indexing from becoming a rescue parameter.

## Rule 1. Specify Axes Before Interpreting Evidence

For any context-indexed graph, specify these axes before interpreting production, judgment,
correction, or corpus evidence:

- `community`
- `norm_centre`
- `genre`
- `medium`
- `task_framing`
- `speaker_identity`

Do not add or split an axis after seeing a surprising result unless the split is marked as exploratory.

## Rule 2. Run Contrast Cells, Not Global Averages

For each phenomenon, define minimally informative contrast cells. Do not average across cells when
the phenomenon is defined by cross-context divergence.

Examples:

- `needs washed`: regional vernacular speech/community context vs standard-edited prose/norm-centre
  context.
- `stigmatized robust vernacular`: in-group speaker cue vs standard-evaluator cue, with naturalness
  and correctness task framings separated.
- `register-bound fragments`: headline, sign, conversation, and formal-prose cells separated by
  genre and medium.
- `singular they`: historical time slices separated from current institutional norm-centres.
- `between you and I`: production context separated from correctness-framed judgment context.

## Rule 3. Mark Exploratory Splits

If a new context split is discovered during analysis, keep it, but label it exploratory. It cannot be
used as the basis for a non-zero score until a later pass tests it against held-out phenomenon cards
or newly specified evidence.

## Rule 4. Keep Modules Scoped

The context-indexed dynamic candidate is a module for diachronic and context-conditioned licensing,
production, ideology, correction, and judgment. It is not a replacement for:

- operator-gap modules;
- processing modules;
- recoverability modules;
- opportunity/preemption modules.

When a graph lacks a module needed for a phenomenon, record that as a scope limit rather than adding
post hoc context axes.

## Rule 5. Failure Conditions

A context-indexed graph fails the protocol if:

- it treats standard-language norms as the whole community;
- it treats a task effect as transparent access to grammar;
- it explains every counterexample by adding a new context split after the fact;
- it aggregates over cells whose separation is part of the phenomenon;
- it declares a conditioning axis but has no corresponding node or edge path in the graph.

## Tooling Implication

The linter should check that declared `conditioning_axes` are not metadata-only. Each declared axis
should be represented by at least one corresponding node:

- `community` -> `community_licensing`
- `norm_centre` -> `standard_language_ideology`, `metalinguistic_condemnation`, or
  `editorial_correction_probability`
- `genre` -> `genre` or `register_genre_appropriateness`
- `medium` -> `medium`
- `task_framing` -> `task_framing`
- `speaker_identity` -> `speaker_identity` or `social_indexical_value`
