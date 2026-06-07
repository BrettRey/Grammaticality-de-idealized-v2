# First Adversarial Pass Plan
**Date:** 2026-06-07
**Scope:** `evolutionary-dag-workbench`
## Goal
Put the scaffold to work by running the first adversarial critique pass over all six seed
representations. This is not a scoring pass. Seed scores remain zero until critique artifacts
exist and the workbench has a defensible basis for assigning non-zero values.

## Representation Boundary

The current seed files are graph-shaped JSON because that is the first representation layer. This
does not mean the hypothesis space is limited to DAGs. A valid critique may conclude that a seed
should mutate into a non-DAG representation, a time-indexed dynamic model, a family-resemblance
map, a bipartite construct/proxy map, or another structured hypothesis format.
## Inputs
- Six seed representations in `graphs/seeds/`
  
- Twelve phenomenon cards in `phenomena/cards/`
  
- `agents/prompts/adversarial-counterexample-agent.md`
  
- `agents/rubrics/graph-scoring-rubric.md`
  
- `ontology/forbidden-conflations.md`
  
## Outputs
1. One critique file per seed representation in `graphs/critiques/`:
  
  - `detector-seed-critique.md`
    
  - `dynamic-feedback-seed-critique.md`
    
  - `normativity-heavy-seed-critique.md`
    
  - `ovmg-seed-critique.md`
    
  - `processing-heavy-seed-critique.md`
    
  - `usage-heavy-seed-critique.md`
    
2. One synthesis note:
  
  - `notes/first-adversarial-pass-synthesis-2026-06-07.md`
    
## Critique Template
Each critique should answer:

1. Strongest counterexample.
  
2. Category mistake, if any.
  
3. Most damaging missing node.
  
4. Most suspicious edge.
  
5. Minimal mutation that would make the representation harder to kill.
  
6. Score-readiness judgment: `not ready`, `partly ready`, or `ready after mutation`.
  
## Guardrails
- Do not promote OVMG, detector, or any familiar family by default.
  
- Do not use `reported_acceptability` as grammaticality.
  
- Do not use raw `usage_frequency` as community licensing.
  
- Do not treat correction or condemnation as grammatical impossibility.
  
- Do not add non-zero seed scores in this pass.
  
- If a representation survives only by adding missing constructs, mark that as a mutation, not as current strength.
- If DAG structure itself is the problem, say so directly and name the better representation class.
  
## Work Order
1. Run `validate_graph.py`, `lint_graph.py`, and `score_graph.py` on seeds before writing critiques.
  
2. Read each seed graph and the most relevant phenomenon cards.
  
3. Write six critique files.
  
4. Write the synthesis note comparing failure modes and likely mutation families.
  
5. Run validation/lint/scoring again to confirm graph data was not accidentally changed.
  
## Success Condition
The workbench has a first critique layer that makes the seed archive less biased: every seed
representation has a recorded attack, and the synthesis identifies which mutations or representation
classes are worth trying next.
