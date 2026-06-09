# Evolutionary DAG Workbench - Status

**Parent:** `Grammaticality_de_idealized`
**Created:** 2026-06-07
**Stage:** Active adversarial iteration
**Public state:** Private working subproject; no public claims or submission state.

## Current State

The subproject is now active as a discovery-first workbench for exploring rival conceptual
representations about grammaticality. The existing OVMG, detector, operator-stratum, usage-based,
processing-based, and normativity-based models are treated as seed graph families, not as
conclusions or targets to vindicate.

Fifteen adversarial passes/synthesis steps have been run. All numeric scores remain zero. Four
current modules have `scoped_module` labels tied to protocol-bound evaluations. The original
scope-only evaluations now include card-level requirements and activated paths. Both held-out CGEL
evaluations also include card-level requirements and activated paths without authorizing score
movement. The agreement and center-embedding cards have now been converted into protocol-bound
evaluations against the operator-gap, dynamic/context, and task-separated modules. Their repeated
processing/naturalness gap justified a scoped `processing-naturalness-perturbation-candidate`.
The clause-type/interjection pair has now exposed a distinct uptake/operator boundary gap, which
justified a scoped `uptake-operator-boundary-candidate`.
The frequent-condemned-form pass did not justify a new graph: `DYN` and `TASK` cover the relevant
production/condemnation/attribution split, while `CAT` is out of scope.
The fused-head NP pass also did not justify a new graph: `OPG` covers the core constructional
support/recoverability split, while `CAT` and `SEL` partly cover category/function and
selection-adjacent dimensions only.
The held-out CGEL evaluations now include machine-readable `prediction_tests` with pass/fail
conditions; score-change evaluations now require prediction tests.
Six held-out CGEL cards have source-checked contrast examples, and the held-out prediction tests
now record checked evidence statuses: three `passed`, two `mixed`, and one `inconclusive`.
No graph has a `general_account` score. The current scoring schema includes `projective_power` and
`theory_preservation_penalty` so held-out prediction and anti-alignment discipline are visible.

## Current Candidate Stack

- `licensing-ideology-split-candidate`
- `opportunity-preemption-operator-gap-candidate`
- `stratified-licensing-measurement-candidate`
- `dynamic-stratified-feedback-candidate`
- `context-indexed-dynamic-feedback-candidate`
- `context-aware-operator-gap-candidate`
- `category-measurement-discipline-candidate`
- `context-indexed-task-separated-feedback-candidate`
- `audience-reference-tracking-candidate`
- `selection-collocation-split-candidate`
- `processing-naturalness-perturbation-candidate`
- `uptake-operator-boundary-candidate`

The current strongest modules are scoped, not general winners:

- `context-indexed-dynamic-feedback-candidate` for diachronic/context-conditioned licensing,
  production, ideology, correction, and judgment. This graph is now profiled only on activated
  evaluation paths.
- `context-aware-operator-gap-candidate` for operator-gap, opportunity, recoverability, analogy, and
  repair-pressure cases. This graph uses derived evidential constructs for opportunity-normalized
  attestation and preemption strength.
- `category-measurement-discipline-candidate` for category-analysis and measurement-task
  divergence. It is unscored and has no scoped-module label.
- `context-indexed-task-separated-feedback-candidate` for separating unmonitored or elicited
  production settings from correctness-framed judgment settings. It is unscored and has no
  scoped-module label.
- `audience-reference-tracking-candidate` for pronoun/pro-form reference tracking, personhood
  ascription, audience design, and social-indexical judgment channels. It is unscored and has no
  scoped-module label.
- `selection-collocation-split-candidate` for distinguishing payload preposition choice,
  collocational rigidity, and argument-linking selection. It is unscored and has no scoped-module
  label.
- `processing-naturalness-perturbation-candidate` for processing cost, recoverability, felt
  naturalness, measurement-task effects, reported acceptability, and attribution perturbations. It
  is a scoped module, not a licensing account.
- `uptake-operator-boundary-candidate` for update-role configuration, repertoire closedness, token
  innovability, operator-repertoire membership, stance, genre fit, repair, and attribution. It is a
  scoped module for clause-type/interjection boundaries, not a general operator-gap account.

`context-indexed-dynamic-feedback-candidate`, `context-aware-operator-gap-candidate`, and
`processing-naturalness-perturbation-candidate`, and `uptake-operator-boundary-candidate` currently
have protocol-bound `scope-only` evaluations and `scoped_module` labels. No graph has earned a
non-zero numeric score or a
`general_account` label.

## Live Boundary Rule

Earlier models are allowed to seed, constrain, and challenge the search. They are not the ontology
the search is required to vindicate. A graph earns standing by improving contrast-cell prediction,
construct separation, or held-out projectibility, not by fitting a prior paper.

## Scaffolded Components

- `ontology/nodes.yaml`
- `ontology/edge-types.yaml`
- `ontology/relation-profiles.yaml`
- `ontology/forbidden-conflations.md`
- `phenomena/index.md`
- source-backed CGEL/local-correction card tranche in `phenomena/cards/`
- `DISCOVERY_RULES.md`
- initial phenomenon cards in `phenomena/cards/`
- graph schema and seed graphs in `graphs/`
- graph-agent template and scoring rubric in `agents/`
- stdlib validation, linting, and scoring scripts in `scripts/`
- evaluation summary utility in `scripts/summarize_evaluations.py`
- source map and pressure test in `notes/`
- CGEL/local correction source registry in `notes/cgel-source-registry.md`
- conditioning protocol in `notes/conditioning-operationalization-protocol-2026-06-07.md`
- scoped scoring policy in `notes/scoped-scoring-policy-2026-06-07.md`
- task-separated feedback synthesis in `notes/seventh-adversarial-pass-synthesis-2026-06-08.md`
- audience/reference-tracking synthesis in `notes/eighth-adversarial-pass-synthesis-2026-06-08.md`
- selection/collocation synthesis in `notes/ninth-adversarial-pass-synthesis-2026-06-08.md`
- processing/naturalness synthesis in `notes/tenth-adversarial-pass-synthesis-2026-06-08.md`
- uptake/operator boundary synthesis in `notes/eleventh-adversarial-pass-synthesis-2026-06-08.md`
- frequent-condemned-form synthesis in `notes/twelfth-adversarial-pass-synthesis-2026-06-08.md`
- fused-head NP synthesis in `notes/thirteenth-adversarial-pass-synthesis-2026-06-08.md`
- prediction-test synthesis in `notes/fourteenth-adversarial-pass-synthesis-2026-06-08.md`
- source-backed prediction evidence synthesis in
  `notes/fifteenth-adversarial-pass-synthesis-2026-06-08.md`
- coverage/discriminator matrix in `notes/coverage-discriminator-matrix-2026-06-08.md`
- protocol-bound evaluation schema and exploratory evaluations in `evaluations/`
- held-out CGEL/local-correction evaluations in `evaluations/protocol-tests/`
- agreement, center-embedding, uptake-boundary, frequent-condemned-form, and fused-head evaluations in
  `evaluations/protocol-tests/`
- positive and negative validator fixtures in `tests/fixtures/`

## Current Tooling Gates

Run these over seeds plus archive candidates:

```bash
python3 scripts/validate_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/lint_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/score_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/validate_evaluation.py evaluations/protocol-tests/*.json
python3 scripts/run_fixture_tests.py
```

For a compact view of evaluation state:

```bash
python3 scripts/summarize_evaluations.py evaluations/protocol-tests/*.json
```

The linter now checks:

- controlled node IDs, including time-sliced extensions;
- relation profiles against the controlled registry and edge-type compatibility;
- profiled graphs have at least one profiled edge;
- graph IDs against filename stems;
- family/status conventions;
- complete score blocks where present;
- score values in the 0-5 range;
- discovery-specific score dimensions for held-out projectibility and theory-preservation penalty;
- all-zero seed score discipline;
- `score_status` metadata for non-zero scores;
- required evaluation references for scoped/general labels;
- evaluation references whose `target_graph` matches the labelled graph;
- scoped/general labels only when the referenced evaluation authorizes scope recognition;
- `general_account` labels only when the referenced evaluation is held-out and proposes score
  movement;
- non-zero scores only when the referenced evaluation authorizes score movement;
- held-out evaluation references resolve `held_out_from` items to cards or evaluations;
- non-zero scores only on graphs with `edge_semantics_level: profiled`;
- `conditioning_axes` metadata for context-indexed graph families;
- declared conditioning axes against corresponding graph nodes;
- conditioning-axis nodes that are outcome-like or have directed paths to outcome-like nodes.

The graph validator checks:

- allowed edge types;
- edge endpoint membership;
- duplicate typed edges;
- acyclicity of non-`time_lagged` edges;
- forward direction for `time_lagged` edges;
- no backward cross-time edges and no forward cross-time effects except `time_lagged`.

The evaluation validator checks:

- protocol-bound evaluations against target graph paths, protocol paths, phenomenon card IDs,
  allowed result labels, and complete six-axis contrast cells.
- card-level requirements for required/forbidden target-graph nodes and edges.
- held-out evaluations include non-empty `held_out_from` provenance resolved to cards or
  evaluations.
- activated paths, when present, resolve to target-graph edges and continue as directed paths.
- `score-change-proposed` evaluations target graphs whose `edge_semantics_level` is `profiled`.
- `score-change-proposed` evaluations include activated paths whose edges have relation profiles.
- activated paths with `expected_path_reading` match the path reading computed from relation
  profiles; score-change paths require an expected reading.
- prediction tests, when present, resolve to a phenomenon card, contrast cell, and activated path
  or paths from the same evaluation.
- `score-change-proposed` evaluations include prediction tests with explicit pass/fail conditions.

The fixture runner checks positive and negative cases for both graph linting and evaluation
validation.

## Next Actions

1. Add data pointers for the unresolved prediction-test cells: pronoun policy/audience design,
   dialectal negative correction, and rare transparent-relative opportunity thresholds.
2. Test whether `OPG`, `CAT`, and `SEL` stay complementary on richer fused-construction cards before
   adding any fused-head-specific graph.
3. Calibrate scoped-module score magnitudes after at least one held-out or parameterized evaluation
   pass.
4. Expand `phenomena/cards/` toward 40-100 cards only after the current representation classes stop
   shifting every pass.
5. Only after the construct inventory stabilizes, consider whether `pgmpy`, NOTEARS-style methods,
   or empirical causal discovery are useful.
