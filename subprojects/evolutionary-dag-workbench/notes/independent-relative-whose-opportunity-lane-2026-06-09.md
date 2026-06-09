# Independent Relative `whose` Opportunity Lane

**Date:** 2026-06-09
**Target evaluation cell:** `transparent-rare-relative-prediction`
**Primary graph under test:** `context-aware-operator-gap-candidate`
**Source lane:** Lane B, independent relative `whose`

## Question

Does the independent relative `whose` material support the workbench's low-opportunity discipline:
absence or rarity should yield uncertainty until a licensing context, contrast set, and measurement
task are declared?

## Sources Checked

Local source files and packages:

- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Independent_relative_whose/items/README.md`
- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Independent_relative_whose/items/all_items.csv`
- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Independent_relative_whose/docs/experiment/whose-experiment-README.md`
- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Independent_relative_whose/docs/experiment/POWER-ANALYSIS.md`
- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Independent_relative_whose/expected_parrot_package/`
- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Independent_relative_whose/results/simulation_results_*.csv`

## What The Lane Provides

The source pool provides an experiment-ready low-opportunity design rather than an observed human
result.

The compact item table records:

- 36 total items per participant;
- 6 critical independent-`whose` items crossed by `LicPlus`/`LicMinus`;
- 6 dependent-`whose` baseline items;
- 12 acceptable fillers and 12 unacceptable fillers;
- 6 Latin-square lists, with each participant seeing 3 `LicPlus` and 3 `LicMinus` critical items.

The fuller experiment documentation records a broader design:

- 32 critical items from 8 lexical sets crossed by `REF` and `LIC`;
- `REF`: identity-of-sense vs identity-of-reference;
- `LIC`: licensing vs non-licensing context;
- 4 environments, with one syntactically marked environment treated as exploratory;
- planned 7-point acceptability ratings, baselines, fillers, and follow-up cloze task.

## Simulation Summary

The local package includes LLM/simulation outputs. They are useful feasibility checks, not
substitutes for human evidence.

| Source file | Critical `LicPlus` mean | Critical `LicMinus` mean | Difference | Interpretation |
|---|---:|---:|---:|---|
| `simulation_results_llm.csv` | 2.667 | 2.010 | +0.657 | A model-sensitive licensing-context effect; aligns with the package summary. |
| `simulation_results_codex.csv` | 2.353 | 2.353 | 0.000 | No licensing-context sensitivity. |
| `simulation_results_gemini.csv` | 2.346 | 2.288 | +0.059 | No meaningful licensing-context sensitivity. |
| `simulation_results.csv` | 5.350 | 4.526 | +0.824 | Design-stage simulated effect, not independent evidence. |

The power-analysis note treats the `LIC` effect as the primary hypothesis and reports the design as
well powered for that effect at about 100 participants. `REF` and `REF` by `LIC` effects are marked
as exploratory.

## Workbench Interpretation

This lane supports `OPG`'s discipline at the design level:

- raw rarity is not treated as non-licensing;
- licensing context is explicitly manipulated rather than inferred after the fact;
- dependent-`whose` baselines separate the target construction from ordinary `whose`;
- LLM disagreement is treated as measurement-channel evidence, not as a verdict about licensing;
- low-opportunity uncertainty remains unresolved until human or corpus evidence exists.

This lane does not add a new passed human-evidence cell. The existing `OPG` prediction remains
passed because Lane A supplied checked opportunity evidence. Lane B adds a ready measurement route
and a warning against treating simulation output as direct grammatical evidence.

## Graph Consequence

No graph mutation follows. `context-aware-operator-gap-candidate` already has the needed constructs:

- `opportunity_mass`
- `opportunity_normalized_attestation`
- `competitor_availability`
- `preemption_strength`
- `community_licensing`
- `semantic_pragmatic_recoverability`
- `reported_acceptability`
- `measurement_task`

No score movement follows. A future pass could update the evaluation only after human judgment data
or an agreed corpus denominator has been recorded.
