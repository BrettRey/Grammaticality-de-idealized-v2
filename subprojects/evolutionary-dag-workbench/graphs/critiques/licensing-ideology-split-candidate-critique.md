# Critique: licensing-ideology-split-candidate

**Target:** `graphs/archive/licensing-ideology-split-candidate.json`
**Family:** licensing-ideology-split
**Pass:** second adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`rare uncontroversial form` is the strongest attack. The candidate can explain why a stigmatized or
school-condemned form is rejected in some judgment contexts while remaining produced in a licensed
community. But it has no `usage_frequency`, `opportunity_mass`, `constructional_analogy`, or
`semantic_pragmatic_recoverability`, so it cannot distinguish:

- low token frequency because opportunities are rare;
- low production because a form is not community licensed;
- low acceptability because the task or genre is hostile;
- low confidence because the evidence is epistemically sparse.

`transparent free relatives` and `left-branch extraction` press the same weakness from a different
angle: the graph has no way to represent the difference between recoverable meaning and licensed
form.

## 2. Category Mistake

The candidate mostly avoids the first-pass collapse of ideology into licensing. Its new danger is
making `community_licensing` an unexplained oracle. The graph separates licensing from reported
acceptability and correction, but it does not say what evidence could move licensing up or down.

This is not a conflation, but it is an explanatory gap. A graph that says "community licensing
matters" without modeling how licensing is inferred risks becoming a relabeled target construct.

## 3. Most Damaging Missing Node

`opportunity_mass`.

Without it, the graph cannot decide whether absence or rarity is evidence against licensing. This
also weakens its handling of regional and register-bounded forms, because low observed frequency may
mean low opportunity rather than low licensing.

Secondary missing nodes:

- `usage_frequency`
- `constructional_analogy`
- `semantic_pragmatic_recoverability`
- `processing_cost`
- `social_indexical_value`
- `schooling_instructional_exposure`

## 4. Most Suspicious Edge

`editorial_correction_probability -> grammaticality_attribution`.

The edge is typed as evidential, which is better than treating correction as impossibility. But the
graph does not separate correction source, authority, genre, and institutional setting. That makes
the edge too easy to misread as "editors correct it, therefore it is less grammatical."

The safer version would route correction through `standard_language_ideology`, `genre`, and task or
institutional framing before allowing it to inform attribution.

## 5. Minimal Mutation

Add an evidence layer beneath `community_licensing`:

- `opportunity_mass`
- `usage_frequency`
- `constructional_analogy`
- `semantic_pragmatic_recoverability`

Then route:

- `opportunity_mass -> usage_frequency`
- `usage_frequency -> community_licensing` as evidential only;
- `opportunity_mass -> community_licensing` as evidential only;
- `semantic_pragmatic_recoverability -> reported_acceptability`, not directly to licensing;
- `constructional_analogy -> production_probability`.

This keeps the candidate's main strength, the ideology/licensing split, while preventing
`community_licensing` from floating free of measurable evidence.

## 6. Score-Readiness Judgment

`not ready`.

The candidate is a useful module for `needs washed`, stigmatized robust vernacular forms,
register-bound fragments, and frequent condemned forms. It should not receive a non-zero score as a
general representation until opportunity-normalized evidence and recoverability are added or
explicitly delegated to another module.
