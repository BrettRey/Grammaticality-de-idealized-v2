# Protocol-Bound Test: context-indexed-dynamic-feedback-candidate

**Date:** 2026-06-07
**Target:** `graphs/archive/context-indexed-dynamic-feedback-candidate.json`
**Protocol:** `notes/conditioning-operationalization-protocol-2026-06-07.md`

## Test Setup

This test uses pre-specified contrast cells. A split counts only if it is named before the candidate
is evaluated against the card.

The candidate is tested as a dynamic/context module, not as a general account. It is allowed to
handle licensing, ideology, correction, production, reported acceptability, attribution, and
diachronic stabilization. It is not allowed to claim operator-gap, recoverability, constructional
analogy, or processing coverage unless those modules are present.

## Card 1. `needs washed`

### Contrast Cells

- Regional vernacular community, local speech or informal writing, naturalness framing.
- Standard norm centre, edited prose or school task, correctness framing.

### Expected Survival Pattern

The candidate should predict stable or elevated `production_probability` and
`community_licensing` in the regional cell, while allowing higher `metalinguistic_condemnation`,
`editorial_correction_probability`, lower `reported_acceptability`, or hostile
`grammaticality_attribution` in the standard cell.

### Result

Survives as a module.

The conditioning axes make the right contrast available. The graph no longer has to choose between
"licensed" and "condemned" globally. The remaining weakness is that the JSON does not instantiate
the two cells; it only says the axes must be specified.

## Card 2. `stigmatized robust vernacular`

### Contrast Cells

- In-group or locally licensed speaker cue, naturalness framing.
- Out-group or standard-evaluator cue, correctness framing.

### Expected Survival Pattern

The candidate should let `speaker_identity_t1 -> social_indexical_value_t1` change
`reported_acceptability_t1` without changing `community_licensing_t1` directly.

### Result

Survives as a module.

The graph represents speaker-cue and indexical effects separately from licensing. This is a real
improvement over the first-round candidates. The remaining weakness is that the graph does not yet
separate evaluator identity from speaker identity.

## Card 3. `register-bound fragments`

### Contrast Cells

- Headline, sign, conversational answer, or message fragment.
- Formal edited prose or grammar-test full-sentence task.

### Expected Survival Pattern

The candidate should route genre and medium through `register_genre_appropriateness_t1` and then to
`reported_acceptability_t1`, without globally marking fragments as unlicensed.

### Result

Survives as a module.

The `genre_t1`, `medium_t1`, and `register_genre_appropriateness_t1` path is exactly the needed
split. The graph still needs a way to represent cases where fragment status is licensed by the
genre but still receives explicit grammaticality condemnation under task framing.

## Card 4. `singular they`

### Contrast Cells

- Earlier time slice with longstanding production and hostile usage-guide norm centre.
- Later time slice with institutional acceptance and broader public licensing.

### Expected Survival Pattern

The candidate should represent production and usage at earlier slices feeding later usage,
licensing, stabilization, ideology, and production without treating recent institutional acceptance
as creation from nothing.

### Result

Partly survives.

The dynamic skeleton is appropriate. It represents lagged feedback and avoids treating older
condemnation as proof of impossibility. But it still lacks a clear way to represent multiple norm
centres changing at different rates, and it has no explicit cohort or institutional-adoption node.

## Card 5. `between you and I`

### Contrast Cells

- Production context without explicit correctness framing.
- Correctness-framed judgment or school/editing task.

### Expected Survival Pattern

The candidate should allow production probability and reported acceptability to diverge under
`task_framing_t1`, `standard_language_ideology_t1`, and correction pressure.

### Result

Partly survives.

The graph has the right high-level channels, but it lacks `schooling_instructional_exposure` and
does not explicitly separate production task from judgment task. It can represent the divergence,
but not yet the learned hypercorrection pathway.

## Card 6. `left-branch extraction`

### Contrast Cells

- Semantically recoverable but structurally/operator-suspect extraction.
- Available paraphrase or preempting alternative in comparable discourse context.

### Expected Survival Pattern

The candidate should fail or mark the phenomenon out of scope unless it includes an operator-gap or
recoverability module.

### Result

Fails as a general account, correctly out of scope as a module.

This is a useful failure. It confirms that the context-indexed dynamic graph should not be promoted
as the workbench's default representation. A separate context-aware operator-gap candidate is still
needed.

## Score Judgment

No score changes.

The candidate is stronger than the earlier candidates as a dynamic/context module, but the test is
not enough to justify a non-zero score. Reasons:

- the contrast cells are specified in prose, not instantiated as graph data;
- the candidate has not been tested against held-out phenomenon cards;
- the graph has no signed edge semantics;
- operator-gap and processing cards remain out of scope;
- some conditioning distinctions, such as evaluator identity and institution type, are still absent.

## Next Action

Build a context-aware operator-gap candidate, or add a small evaluation format that can store
protocol-bound contrast-cell tests as data rather than prose.
