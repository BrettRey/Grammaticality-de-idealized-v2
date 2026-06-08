# Critique: dynamic-stratified-feedback-candidate

**Target:** `graphs/archive/dynamic-stratified-feedback-candidate.json`
**Family:** dynamic-stratified-feedback
**Pass:** fourth adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`needs washed` is the strongest attack. The candidate can model time-lagged feedback among
production, usage, entrenchment, licensing, ideology, correction, reported acceptability, and later
production. But it still has only one `community_licensing_t1` and one
`standard_language_ideology_t1`.

That hides the main contrast in the card: a form can be licensed in one regional community while
being condemned by a standard-language norm centre. Time indexing does not solve that problem if the
community parameter is not explicit.

`stigmatized robust vernacular` and `register-bound fragments` expose the same weakness. The graph
needs conditioning by community, speaker cues, genre, medium, and task frame, not just time.

## 2. Category Mistake

The candidate treats temporal indexing as enough contextualization. It is not.

Time slices answer "when?" but not:

- licensed for whom?
- in which genre?
- in which medium?
- under which task framing?
- attributed to which speaker identity?
- judged relative to which norm centre?

Without those axes, the graph can accidentally average over incompatible communities and then
recreate the standard-language ideology problem at a higher level.

## 3. Most Damaging Missing Node

`speaker_identity`.

Speaker cues are not optional for stigmatized robust vernacular cases. They can change reported
acceptability and grammaticality attribution while production and community licensing remain stable.

Secondary missing nodes:

- `social_indexical_value`
- `genre`
- `medium`
- `register_genre_appropriateness`
- `task_framing`

## 4. Most Suspicious Edge

`community_licensing_t1 -> production_probability_t2`.

The edge is plausible, but underspecified. Community licensing in which community predicts later
production by which speakers, in which genre and medium, under which monitoring conditions? Without
conditioning, the edge can wrongly predict that regional licensing should raise production in
standard-edited prose, or that standard condemnation should suppress production in local speech.

## 5. Minimal Mutation

Create a context-indexed dynamic mutation.

The mutation should add:

- explicit conditioning metadata for community, norm centre, genre, medium, task framing, and speaker
  identity;
- time-sliced nodes for `speaker_identity`, `social_indexical_value`, `genre`, `medium`,
  `register_genre_appropriateness`, and `task_framing`;
- edges from those context nodes into `reported_acceptability_t1` and
  `grammaticality_attribution_t1`;
- the same time-lagged feedback discipline as the dynamic candidate.

This tests whether the workbench can preserve temporal feedback without erasing community
heterogeneity.

## 6. Score-Readiness Judgment

`not ready`.

The candidate is a useful dynamic skeleton, but it should not receive a non-zero score while it lacks
explicit context conditioning. It would overpredict cross-context stability for forms whose whole
point is that licensing, production, and judgment diverge across communities and genres.
