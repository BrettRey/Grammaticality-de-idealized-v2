# Evolutionary DAG Workbench Placement

**Date:** 2026-06-07
**Question:** Should the grammaticality evolutionary DAG workbench live in an existing project, a new subproject, or a new top-level project?
**Status:** Implemented after Brett confirmation. Roughdraft timed out twice without a Done Reviewing signal or saved comments.

## Recommendation

Create it as a **new subproject inside `Grammaticality_de_idealized`**, tentatively:

`papers/Grammaticality_de_idealized/subprojects/evolutionary-dag-workbench/`

Implemented 2026-06-07.

Do not put it inside `Grammaticality_judgments_as_detectors`, `Grammaticality_as_Kind_Miller`, or any submitted subproject. Do not make it a new top-level paper repo yet.

The rationale is simple: the workbench should piggyback on the grammaticality ecology without inheriting any single model's commitments. The parent `Grammaticality_de_idealized` project is already a framework family with subprojects. This new work is another family member, but it needs an explicit non-commitment boundary:

> Earlier models are seeds, constraints, counterexample sources, and comparison baselines; they are not the ontology the workbench is required to vindicate.

## Why Not Existing Project Only?

The existing root OVMG project has live theoretical commitments: `G(u)`, `F(u)`, `map`, `K`, `C_t`, and the operator-value bridge. The new workbench is designed to test whether those commitments are stable against rival graph families. If it lives only as a root note, it will be too easy for future agents to treat the OVMG equations as the default answer.

The workbench needs its own `STATUS.md`, node ontology, graph schema, phenomenon cards, agent prompts, and scoring criteria. That is too much structure for a note, and too methodologically distinct from the current root paper.

## Why Not `Grammaticality_judgments_as_detectors`?

`Grammaticality_judgments_as_detectors` is already a paper-shaped project with a specific contribution: judgments as noisy detectors of a socially stabilized kind, aimed at a philosophy-of-psychology audience. It has a detector architecture, source-grounding obligations, and a paper argument.

The DAG workbench should use that project as a feeder:

- judgment channels;
- acceptability/grammaticality distinctions;
- channel-specific failure patterns;
- adversarial reviewer personas;
- phenomenon cards.

But the workbench is broader. It is not just about judgments as detectors. It asks what graph families survive when usage, processing, normativity, pedagogy, production, correction, community licensing, and theoretical attributions are all allowed to compete.

## Why Not `Grammaticality_as_Kind_Miller`?

That paper is under review at *Mind & Language* and has co-author/provenance constraints. It should not become the place where experimental machinery, mutating graphs, and speculative ontology revisions accumulate.

The DAG workbench can later inform a revision if needed, especially around the stability of grammaticality-as-kind claims. But it should not touch or depend on that submission while it is under review.

## Why Not A New Top-Level Project Now?

A top-level repo would make sense later if the workbench becomes one of these:

- a general tool for conceptual DAG exploration across categories;
- a publishable methods paper independent of grammaticality;
- a reusable library with code, schemas, and an archive that other projects consume;
- a public supplement or web app.

That is not the first move. At the start, the object domain is grammaticality, and the strongest local material lives in the OVMG family. Starting as a subproject keeps the gravitational center correct while preserving the option to graduate later.

## Discovery Assumptions

### Existence

- `Grammaticality_de_idealized` already has a subproject structure.
- Existing subprojects cover operator value, the asterisk/state theory, etiology, and felt ungrammaticality.
- `Grammaticality_judgments_as_detectors` already contains judgment-channel and detector material.
- `Grammaticality_as_Kind_Miller` is under review and should be protected from local speculative drift.

### Capability

- A subproject can hold schemas, cards, prompts, graph archives, and scoring scripts without forcing root OVMG source changes.
- Earlier DAGs and equations can be represented as seed graphs rather than treated as canonical.
- The workbench can start with lightweight JSON/YAML plus `networkx`/Mermaid/Graphviz before any `pgmpy` or NOTEARS-style empirical structure learning is relevant.

### Preference

- Brett wants to piggyback on prior grammaticality work but avoid recommitting to the models already built.
- The system should preserve rival graph families rather than converge prematurely on a single "best" graph.
- The project should support category-stability-and-inference work, not just HPC branding.

## Inversions

### What would make "new subproject" wrong?

If the workbench's primary contribution quickly becomes a general method for conceptual modelling across domains, not grammaticality, it should graduate to a new top-level project. The trigger would be using more non-grammaticality domains than grammaticality domains in the phenomenon-card archive.

If the workbench becomes a revision instrument for one submitted paper only, it should instead become a branch-local notes/methods folder in that paper. That would be true only if its outputs serve a single review response rather than a wider hypothesis-space map.

If the workbench becomes mainly an empirical causal-discovery tool over measured judgment data, it may need its own top-level computational project with environment management and data provenance rules.

### What does this recommendation assume but not state?

It assumes the workbench should study **the space of viable grammaticality explanations**, not merely automate Brett's existing theory. That means it has to allow graphs that demote or dissolve "grammaticality" as a single target.

It assumes the early deliverable is not a polished paper. The first deliverable should be a reusable corpus of phenomenon cards, node definitions, graph schemas, and a first archive of rival conceptual DAGs.

It assumes the method is useful even if it shows that the single-DAG ambition fails. A diverse archive of locally strong but incompatible graphs would itself be an important result.

## Initial Subproject Shape

Recommended scaffold:

```text
subprojects/evolutionary-dag-workbench/
  STATUS.md
  README.md
  DECISIONS.md
  ontology/
    nodes.yaml
    edge-types.yaml
    forbidden-conflations.md
  phenomena/
    cards/
    index.md
  graphs/
    seeds/
    archive/
    critiques/
  agents/
    prompts/
    rubrics/
  scripts/
    validate_graph.py
    score_graph.py
  notes/
    source-map.md
    pressure-test.md
```

The first three work products should be:

1. `ontology/nodes.yaml`: typed node inventory with definitions, measurement proxies, and forbidden conflations.
2. `phenomena/index.md`: 40-100 candidate phenomenon cards grouped by what they stress-test.
3. `graphs/seeds/`: seed graphs representing OVMG, detector, operator-stratum, usage-heavy, processing-heavy, and normativity-heavy starting points.

## Naming

Working title:

**Evolutionary DAG Workbench for Grammaticality**

Short directory name:

`evolutionary-dag-workbench`

Avoid naming it after OVMG, HPC, or "grammaticality as kind." The name should keep the search procedure visible and avoid implying that the existing model is the winner.
