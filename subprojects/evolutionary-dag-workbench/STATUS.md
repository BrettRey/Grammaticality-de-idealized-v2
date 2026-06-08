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

The current strongest module is `context-indexed-dynamic-feedback-candidate`, but it is explicitly
not a general winner. It needs protocol-bound testing and later reintegration with operator-gap,
recoverability, constructional-analogy, and processing modules.

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
- protocol-bound evaluation schema and first evaluation in `evaluations/`

## Current Tooling Gates

Run these over seeds plus archive candidates:

```bash
python3 scripts/validate_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/lint_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/score_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/validate_evaluation.py evaluations/protocol-tests/*.json
```

The linter now checks:

- controlled node IDs, including time-sliced extensions;
- family/status conventions;
- complete score blocks where present;
- all-zero seed score discipline;
- `conditioning_axes` metadata for context-indexed graph families;
- declared conditioning axes against corresponding graph nodes.
- protocol-bound evaluations against target graph paths, protocol paths, phenomenon card IDs,
  allowed result labels, and contrast-cell axes.

## Next Actions

1. Build a context-aware operator-gap module rather than folding operator value into the dynamic
   context graph by default.
2. Add more protocol-bound evaluations, including one for operator-gap/recoverability cases.
3. Add tests or fixtures for negative linter/evaluation cases, especially malformed
   `conditioning_axes` and invalid contrast-cell axes.
4. Expand `phenomena/cards/` toward 40-100 cards only after the current representation classes stop
   shifting every pass.
5. Only after the construct inventory stabilizes, consider whether `pgmpy`, NOTEARS-style methods,
   or empirical causal discovery are useful.
