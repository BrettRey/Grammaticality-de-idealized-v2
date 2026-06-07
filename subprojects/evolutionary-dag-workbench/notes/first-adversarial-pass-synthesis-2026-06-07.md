# First Adversarial Pass Synthesis

**Date:** 2026-06-07
**Inputs:** six seed representations, twelve phenomenon cards, first critique files

## Summary

The first adversarial pass did its job: no seed representation is ready for non-zero scoring as a
general account. Three are useful modules (`detector`, `usage-heavy`, `processing-heavy`), one is a
useful dynamic skeleton (`dynamic-feedback`), one is a useful normativity module
(`normativity-heavy`), and one is a useful operator-gap model (`ovmg`). None should be treated as
the workbench's preferred hypothesis.

The strongest recurrent failure is not acyclicity. It is missing cross-channel structure: production,
judgment, correction, community licensing, ideology, register, and processing are repeatedly forced
through too few nodes.

## Recurrent Failure Modes

### 1. Production and Judgment Are Still Too Often Collapsed

The detector, normativity, processing, and OVMG seeds cannot adequately explain cases where
production stays stable while reported acceptability or grammaticality attribution shifts.

Stress cards:

- `between-you-and-I`
- `frequent-condemned-form`
- `needs-washed`
- `stigmatized-robust-vernacular`

Most important missing node across these cases: `production_probability`.

### 2. Community Licensing Needs Its Own Track

The normativity and processing seeds fail because they lack `community_licensing`. The usage seed
also needs it, because usage and entrenchment are not licensing by themselves.

Stress cards:

- `needs-washed`
- `stigmatized-robust-vernacular`
- `rare-uncontroversial-form`
- `transparent-free-relatives`

This validates the ontology's decision to keep community licensing separate from reported
acceptability, standard-language ideology, and raw frequency.

### 3. Ideology and Correction Cannot Stand In for Grammar

The normativity seed is useful but dangerous. It models schooling, ideology, condemnation, and
correction, but without community licensing it risks making institutional correction look like
grammatical impossibility.

Needed mutation family: an ideology/licensing two-track model.

### 4. Processing Is a Channel, Not the Target

The processing-heavy seed is useful for agreement attraction, center embedding, and grammatical
but hard cases. It fails as soon as the phenomenon depends on region, standardness, production, or
community licensing.

Needed mutation family: processing-as-measurement-perturbation, not processing-as-grammar.

### 5. Opportunity Mass Is Necessary But Not Sufficient

The usage-heavy seed handles rare licensed forms better than the other seeds because it includes
`opportunity_mass`. But it cannot handle frequent condemned forms without ideology and correction.
It also needs `community_licensing` to prevent entrenchment from becoming acceptance.

Needed mutation family: opportunity/preemption plus licensing/ideology split.

### 6. OVMG Must Not Win by Definition

The OVMG seed has a plausible route through operator-gap cases, especially left-branch extraction.
Its high-risk edge is `operator_value -> grammaticality_attribution`, because that can encode the
preferred theory as a constitutive graph edge before the workbench has earned it.

Needed mutation family: split operator state from grammaticality attribution. Treat OVMG as one
targeted module, not as the default total graph.

## Representation Lesson

The user's Roughdraft comment was right: this workbench should not be limited to DAGs.

The JSON graph format is useful as a first discipline because it forces explicit nodes, edges, and
construct separations. But several live hypotheses may need different representation classes:

- time-indexed dynamic models for usage/norm feedback;
- two-track or multi-channel measurement models for production, judgment, and correction;
- family-resemblance maps if "grammaticality" fragments across practices;
- bipartite construct/proxy maps for measurement hygiene;
- typed module assemblies where processing, normativity, operator value, and usage are modules
  rather than a single acyclic graph.

The next workbench stage should therefore allow "representation mutation" as a legitimate output,
not only edge and node mutation inside DAG-shaped JSON.

## Most Promising Mutation Families

### A. Licensing-Ideology Split

Combine:

- `community_licensing`
- `standard_language_ideology`
- `metalinguistic_condemnation`
- `speaker_identity`
- `genre`
- `reported_acceptability`
- `production_probability`

Purpose: handle `needs washed`, stigmatized robust vernacular forms, and frequent condemned forms.

### B. Measurement-Explicit Detector Plus Production

Combine detector architecture with:

- `production_probability`
- `schooling_instructional_exposure`
- `register_genre_appropriateness`
- `task_framing`

Purpose: handle judgment/production splits such as `between you and I`.

### C. Opportunity-Preemption Operator Gap

Combine:

- `operator_value`
- `opportunity_mass`
- `community_licensing`
- `semantic_pragmatic_recoverability`
- `repair_reformulation_pressure`
- `reported_acceptability`

Purpose: handle left-branch extraction and transparent free relatives without treating
recoverability as licensing.

### D. Dynamic Usage-Norm Feedback

Use a time-indexed representation rather than a simple DAG:

- production at time t
- usage frequency and opportunity mass at time t+1
- community licensing at time t+1
- ideology/correction at time t+1
- production and attribution at time t+2

Purpose: handle singular `they` and other diachronic stabilization cases.

## Score Discipline

No seed scores should change after this pass. The critiques establish that all seed scores correctly
remain zero pending mutation. The first non-zero scores should attach to mutated candidates or to
seeds after a second pass explicitly scopes them as modules rather than total accounts.

## Next Action

Create two candidate mutations:

1. `licensing-ideology-split-candidate`
2. `opportunity-preemption-operator-gap-candidate`

These would test the two most important survival paths without prematurely promoting OVMG,
detector, usage, or normativity as the default answer.
