# Phenomenon Card: nearest-noun agreement attraction

**Stress test:** Agreement-controller alignment vs nearest-attractor illusion.

## Description

Agreement can be perturbed by a nearby attractor noun whose number feature matches the verb more
than the structural controller does. A typical contrast is:

- `The key to the cabinets is on the table.`
- `The key to the cabinets are on the table.`

The second item can sound less bad on first pass because the nearest noun is plural, but rereading
or explicit correction usually restores the singular controller. The attraction effect is a
measurement and processing hazard, not evidence that the nearest noun has become the licensed
agreement controller in ordinary English.

## Source Pointers

- Source IDs: `brett-nearest-agreement-minimal-pair`
- Related cards: [agreement-attraction](agreement-attraction.md),
  [subject-verb-agreement-cgel](subject-verb-agreement-cgel.md)

## Why It Matters

The card forces graphs to distinguish the structural agreement controller from the nearest
retrieval attractor. A processing module can explain why the error sometimes feels acceptable; it
does not by itself explain the grammar of agreement-controller selection.

## Minimum Contrast Cells

- low-load controller agreement;
- plural-attractor first-pass judgment;
- reread or explicit correction of the same item;
- notional or collective agreement control case, kept separate from nearest-attractor illusion.

## Candidate Nodes

- processing_cost
- felt_naturalness_context
- measurement_task
- task_framing
- reported_acceptability
- community_licensing
- grammaticality_attribution

## Potential Construct Pressure

This card keeps pressure on a future agreement-specific construct such as agreement-feature
alignment, controller identification, or retrieval-attractor interference. The existing ontology
has pronoun feature alignment, but it should not be reused uncritically for all agreement cases.

## Graph Failure Modes

- Treats first-pass acceptability as licensing.
- Treats nearest noun agreement as the same as notional or collective agreement.
- Treats all agreement failures as operator-value failures without modelling retrieval or task
  timing.
- Ignores rereading, speeded judgment, or explicit correction as measurement conditions.

## Predicted Discriminators

- `PROC` should partly survive because it handles processing and naturalness perturbation.
- `OPG` should partly survive only as broad operator-value scaffolding.
- `TASK` may help separate speeded judgment from correctness-framed rereading.
- No current graph should claim a full agreement-controller account without a feature-alignment or
  retrieval-attractor construct.
