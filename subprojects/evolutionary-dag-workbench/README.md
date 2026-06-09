# Evolutionary DAG Workbench for Grammaticality

This subproject maps rival hypotheses about the property cluster behind grammaticality. It uses the
existing grammaticality ecology as material without treating any existing model as settled.

The workbench generates, mutates, attacks, scores, and archives typed acyclic construct graphs.
These are conceptual DAGs in the weak graph-theoretic sense, not causal DAGs licensed for
d-separation or intervention claims. The goal is not to find "the DAG of grammaticality." The goal
is to discover graph families that survive adversarial cards and make better held-out predictions
than their predecessors.

See `DISCOVERY_RULES.md` for the standing rule that this is not a justification engine for OVMG,
the operator-stratum paper, detector models, usage-based accounts, processing accounts, or normative
accounts.

## Boundary

Earlier models are seeds, constraints, counterexample sources, and comparison baselines. They are not the ontology this workbench is required to vindicate.

This subproject may use material from:

- `../operator-stratum/`
- `../asterisk-de-idealized/`
- `../etiological-account/`
- `../feeling-of-ungrammaticality/`
- `../../../Grammaticality_judgments_as_detectors/`
- `../../../Grammaticality_as_Kind_Miller/` only as a protected submitted-paper reference point

Do not import claims from submitted or co-authored work as live commitments without checking that project's status file.

## First Deliverables

1. Build a typed node ontology with definitions, measurement proxies, and forbidden conflations.
2. Enrich the existing phenomenon cards with examples, data sources, contrast cells, and
   discriminators before expanding the card set.
3. Seed the archive with OVMG, detector, operator-value, usage-heavy, processing-heavy, and
   normativity-heavy graph families as starting points only.
4. Generate theory-neutral mutations from card failures, not from pressure to preserve a named
   theory.
5. Run adversarial and held-out evaluations before any numeric score movement.
6. Preserve diversity. A locally strong but incompatible graph is a result, not a failure.

## Working Structure

```text
ontology/        Node inventory, edge types, and conflation rules.
phenomena/       Phenomenon cards and card index.
graphs/          Graph schema, seed graphs, archive, and critique outputs.
agents/          Prompt templates and scoring rubrics.
scripts/         Local validation and scoring helpers.
notes/           Source map, pressure test, and planning notes.
evaluations/     Protocol-bound graph tests with machine-checkable contrast cells.
tests/           Positive and negative fixtures for validator behavior.
```

## Method Commitments

- Start with typed acyclic construct graphs, not automatic causal discovery.
- Keep constructs separate from measurement proxies.
- Reject non-time-indexed cycles.
- Represent feedback with time-indexed variables or `time_lagged` edges.
- Treat edge profiles as optional prediction commitments; absent profile means uncommitted.
- Start graph mutation from phenomenon-card failures rather than from theory alignment.
- Name new graph families by their mechanism or contrast, not by a source paper they resemble.
- Penalize theory-preserving moves that do not improve prediction or construct separation.
- Treat held-out projectibility as stronger evidence than coverage of cards used to build a graph.
- Keep seed scores at zero until an adversarial critique is recorded.
- Require `score_status`, a target-matched evaluation reference, and an authorizing evaluation
  status/decision before any graph receives a scoped/general label or non-zero score.
- Treat scoped-module labels as scoped evidence, not as general-account scores.
- Keep multiple scores visible instead of collapsing everything into one winner too early.
- Treat LLM agents as graph generators and critics, not as scholarly adjudicators.

## Minimal Local Commands

Validate the seed and archive graphs:

```bash
python3 scripts/validate_graph.py graphs/seeds/*.json graphs/archive/*.json
```

Lint the graphs against the ontology, relation-profile registry, scoring conventions, and
conditioning metadata rules:

```bash
python3 scripts/lint_graph.py graphs/seeds/*.json graphs/archive/*.json
```

Score graphs after they have a `scores` block:

```bash
python3 scripts/score_graph.py graphs/seeds/*.json graphs/archive/*.json
```

Validate protocol-bound evaluations:

```bash
python3 scripts/validate_evaluation.py evaluations/protocol-tests/*.json
```

Run positive and negative validator fixture tests:

```bash
python3 scripts/run_fixture_tests.py
```

## Worked Vertical Slice

The first data-bearing vertical slice is the AGR COCA projection lane:

- report: `notes/agr-coca-vertical-slice-report-2026-06-09.md`;
- ablation check: `notes/agr-coca-ablation-test-2026-06-09.md`;
- graph: `graphs/archive/agreement-controller-override-candidate.json`;
- evaluation: `evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`;
- data: `data/agr-coca-projection/`.

The current result is scoped: `AGR` beats a simple surface-head-number baseline in checked English
production cells, especially `majority`, but no numeric score movement or general-account claim
follows.

Run the AGR ablation/compression check with:

```bash
python3 scripts/run_agr_ablation.py --output data/agr-coca-projection/ablation-summary.csv
```
