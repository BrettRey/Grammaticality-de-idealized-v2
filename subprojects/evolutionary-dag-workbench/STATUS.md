# Evolutionary DAG Workbench - Status

**Parent:** `Grammaticality_de_idealized`
**Created:** 2026-06-07
**Stage:** Active adversarial iteration
**Public state:** Private working subproject; no public claims or submission state.

## Current State

The subproject is now active as a non-commitment workbench for exploring rival conceptual
representations about grammaticality. The existing OVMG, detector, operator-stratum, usage-based,
processing-based, and normativity-based models are treated as seed graph families, not as
conclusions.

Five adversarial passes have been run. Scores remain all-zero across seeds and candidates.

## Current Candidate Stack

- `licensing-ideology-split-candidate`
- `opportunity-preemption-operator-gap-candidate`
- `stratified-licensing-measurement-candidate`
- `dynamic-stratified-feedback-candidate`
- `context-indexed-dynamic-feedback-candidate`
- `context-aware-operator-gap-candidate`

The current strongest modules are scoped, not general winners:

- `context-indexed-dynamic-feedback-candidate` for diachronic/context-conditioned licensing,
  production, ideology, correction, and judgment.
- `context-aware-operator-gap-candidate` for operator-gap, opportunity, recoverability, analogy, and
  repair-pressure cases.

Both have protocol-bound exploratory evaluations. Neither has earned non-zero scores.

## Live Boundary Rule

Earlier models are allowed to seed, constrain, and challenge the search. They are not the ontology the search is required to vindicate.

## Scaffolded Components

- `ontology/nodes.yaml`
- `ontology/edge-types.yaml`
- `ontology/forbidden-conflations.md`
- `phenomena/index.md`
- initial phenomenon cards in `phenomena/cards/`
- graph schema and seed graphs in `graphs/`
- graph-agent template and scoring rubric in `agents/`
- stdlib validation, linting, and scoring scripts in `scripts/`
- source map and pressure test in `notes/`
- conditioning protocol in `notes/conditioning-operationalization-protocol-2026-06-07.md`
- protocol-bound evaluation schema and exploratory evaluations in `evaluations/`
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

The linter now checks:

- controlled node IDs, including time-sliced extensions;
- family/status conventions;
- complete score blocks where present;
- all-zero seed score discipline;
- `conditioning_axes` metadata for context-indexed graph families;
- declared conditioning axes against corresponding graph nodes.

The evaluation validator checks:

- protocol-bound evaluations against target graph paths, protocol paths, phenomenon card IDs,
  allowed result labels, and contrast-cell axes.

The fixture runner checks positive and negative cases for both graph linting and evaluation
validation.

## Next Actions

1. Decide whether scoped module scores should be possible, separate from general-account scores.
2. Add a processing-specific context module or keep processing as a perturbation layer only.
3. Expand `phenomena/cards/` toward 40-100 cards only after the current representation classes stop
   shifting every pass.
4. Only after the construct inventory stabilizes, consider whether `pgmpy`, NOTEARS-style methods,
   or empirical causal discovery are useful.
