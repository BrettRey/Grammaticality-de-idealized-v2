# Critique: opportunity-preemption-operator-gap-candidate

**Target:** `graphs/archive/opportunity-preemption-operator-gap-candidate.json`
**Family:** opportunity-preemption-operator-gap
**Pass:** second adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`needs washed` is the strongest attack. The candidate can model opportunity-normalized rarity,
recoverability, operator-value pressure, repair, production, and attribution. But it cannot represent
the crucial split between regional community licensing and standard-language ideology, because it
lacks:

- `standard_language_ideology`
- `metalinguistic_condemnation`
- `speaker_identity`
- `genre`
- `editorial_correction_probability`

`stigmatized robust vernacular` and `frequent condemned form` expose the same problem. The graph can
say that a form is licensed or not licensed, but it cannot explain why production remains robust
while reported acceptability, correction, and explicit attribution are hostile.

## 2. Category Mistake

The high-risk move is treating operator structure as too close to licensing. The edge
`operator_value -> community_licensing` is marked as constitutive and scoped to this candidate, which
is disciplined enough for a test. But it still risks encoding OVMG as the answer before the
workbench has earned it.

The graph should instead make operator value a subtype or module that can explain some licensing
failures, not the constitutive route into licensing in general.

## 3. Most Damaging Missing Node

`standard_language_ideology`.

Without it, the candidate cannot survive the cards where production, community licensing, and
correction diverge. It also cannot protect `reported_acceptability` from correctness-framing effects.

Secondary missing nodes:

- `metalinguistic_condemnation`
- `editorial_correction_probability`
- `speaker_identity`
- `genre`
- `task_framing`
- `register_genre_appropriateness`

## 4. Most Suspicious Edge

`operator_value -> community_licensing`.

The edge is useful for operator-gap cases such as left-branch extraction, but it becomes suspicious
as soon as the graph is used outside that family. It can turn "this account predicts operator-value
failure" into "licensing failure is constituted by operator-value failure."

That is exactly the theory-preservation move the first pass warned against.

## 5. Minimal Mutation

Add an ideology and context layer above the judgment proxies:

- `standard_language_ideology`
- `metalinguistic_condemnation`
- `editorial_correction_probability`
- `task_framing`
- `register_genre_appropriateness`

Then route:

- `standard_language_ideology -> metalinguistic_condemnation`
- `metalinguistic_condemnation -> editorial_correction_probability`
- `standard_language_ideology -> reported_acceptability`
- `task_framing -> reported_acceptability`
- `register_genre_appropriateness -> reported_acceptability`

Also weaken or re-scope `operator_value -> community_licensing`: it should be marked as a local
constitutive wager for operator-rich constructions, not a general licensing mechanism.

## 6. Score-Readiness Judgment

`not ready`.

The candidate is useful for left-branch extraction, transparent free relatives, and rare-form
preemption problems. It should not receive a non-zero general score until ideology, correction, and
context channels are added or the graph is explicitly narrowed to operator-gap cases.
