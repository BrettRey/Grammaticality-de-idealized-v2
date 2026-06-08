# Evolutionary DAG Workbench for Grammaticality

This subproject maps rival hypotheses about the property cluster behind grammaticality. It uses the existing grammaticality ecology as material without treating any existing model as settled.

The workbench generates, mutates, attacks, scores, and archives conceptual DAGs. The goal is not to find "the DAG of grammaticality." The goal is to map the hypothesis space and preserve strong but different graph families.

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
2. Build 40-100 phenomenon cards that stress-test rival graph families.
3. Seed the archive with OVMG, detector, operator-value, usage-heavy, processing-heavy, and normativity-heavy graph families.
4. Run adversarial critiques before scoring any graph as strong.
5. Preserve diversity. A locally strong but incompatible graph is a result, not a failure.

## Working Structure

```text
ontology/        Node inventory, edge types, and conflation rules.
phenomena/       Phenomenon cards and card index.
graphs/          Graph schema, seed graphs, archive, and critique outputs.
agents/          Prompt templates and scoring rubrics.
scripts/         Local validation and scoring helpers.
notes/           Source map, pressure test, and planning notes.
```

## Method Commitments

- Start with conceptual DAGs, not automatic causal discovery.
- Keep constructs separate from measurement proxies.
- Reject non-time-indexed cycles.
- Represent feedback with time-indexed variables or `time_lagged` edges.
- Keep seed scores at zero until an adversarial critique is recorded.
- Keep multiple scores visible instead of collapsing everything into one winner too early.
- Treat LLM agents as graph generators and critics, not as scholarly adjudicators.

## Minimal Local Commands

Validate the seed and archive graphs:

```bash
python3 scripts/validate_graph.py graphs/seeds/*.json graphs/archive/*.json
```

Lint the graphs against the ontology, scoring conventions, and conditioning metadata rules:

```bash
python3 scripts/lint_graph.py graphs/seeds/*.json graphs/archive/*.json
```

Score graphs after they have a `scores` block:

```bash
python3 scripts/score_graph.py graphs/seeds/*.json graphs/archive/*.json
```
