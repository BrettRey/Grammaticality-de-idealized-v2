# Scoped Module Compression Audit

**Date:** 2026-06-09
**Trigger:** Claude/GPT-Pro criticism that the workbench had no rejection, merge, or stopping
pressure.
**Status:** First compression audit; no label changes, graph mutations, or score movement.

## Method

Ran:

```bash
python3 scripts/audit_module_overlap.py
```

The script strips time indices (`_t`, `_t1`, `_t2`) and computes pairwise node-overlap among graphs
whose `score_status.kind` is `scoped_module`. It also lists nodes distinctive to each scoped module.

This is only a first compression screen. Shared generic nodes such as `community_licensing`,
`reported_acceptability`, `grammaticality_attribution`, and `task_framing` do not by themselves
justify merger. A module becomes merge/kill vulnerable when its distinctive nodes are not doing
activated-path work in its authorizing evaluations.

## Scoped Modules

| Module | Nodes | Edges | Distinctive nodes |
| --- | ---: | ---: | --- |
| `AGR` | 14 | 15 | `agreement_controller_identification`, `agreement_feature_alignment`, `agreement_override_pattern`, `notional_agreement_basis`, `retrieval_attractor_salience` |
| `ART` | 17 | 19 | `audience_design`, `judgment_task_setting`, `personhood_ascription`, `pronoun_feature_alignment`, `reference_tracking_success` |
| `OPG` | 22 | 28 | `competitor_availability`, `constructional_analogy`, `opportunity_normalized_attestation`, `preemption_strength` |
| `DYN` | 20 | 31 | `diachronic_stabilization`, `editorial_correction_probability`, `entrenchment` |
| `FDL` | 12 | 15 | `construction_specific_dependency_licensing`, `constructional_frame_fit`, `constructional_function` |
| `PNP` | 8 | 9 | `felt_naturalness_context`, `measurement_task` |
| `UOB` | 17 | 20 | `repertoire_closedness`, `token_innovability` |

## Highest Overlap Pairs

| Pair | Jaccard | Compression read |
| --- | ---: | --- |
| `OPG` / `DYN` | 0.56 | Do not merge yet. Shared licensing/context nodes hide different mechanisms: opportunity/preemption vs time-lagged stabilization and institutional correction. Pressure test: can `DYN` handle opportunity-normalized absence without importing `preemption_strength`? |
| `OPG` / `UOB` | 0.50 | Keep separate unless boundary cards stop using `repertoire_closedness` and `token_innovability`. `OPG` explains gaps and repair pressure; `UOB` explains operator-stratum membership boundaries. |
| `ART` / `DYN` | 0.48 | Do not merge. `ART` is pronoun/pro-form and audience/reference specific; `DYN` is general diachronic/context feedback. Merge only if audience/reference cards can be handled without `pronoun_feature_alignment`, `personhood_ascription`, and `reference_tracking_success`. |
| `FDL` / `UOB` | 0.45 | Live merger candidate, but not yet justified. Both use operator/repertoire/update nodes. Difference: `FDL` tracks construction-specific frame fit; `UOB` tracks repertoire closedness and token innovability. |
| `ART` / `OPG` | 0.44 | Keep separate. Overlap is mostly context and attribution infrastructure; distinctive reference-tracking nodes protect `ART`. |

## Immediate Compression Conclusions

1. **No scoped module should be merged or killed on node overlap alone.** Every scoped module has at
   least two distinctive nodes, and the distinctive nodes are not merely naming variants of the
   shared construct core.
2. **`FDL` / `UOB` is the best merger test.** A future fused/dependency or interjection-style card
   should ask whether constructional frame fit and repertoire closedness are separable mechanisms
   or one boundary-licensing module.
3. **`OPG` / `DYN` is the best overfitting guard.** Their high overlap makes them look mergeable, but
   the mechanisms differ. The kill test is whether dynamic feedback can handle opportunity-normalized
   absence and competitor preemption without importing `OPG`'s distinctive nodes.
4. **`PNP` is small but protected.** Its distinctive contribution is not licensing, but perturbation:
   `felt_naturalness_context` and `measurement_task`. It should stay scoped only while evaluations
   continue to distinguish low acceptability from licensing failure.
5. **`AGR` is structurally isolated enough to deserve the first empirical lane.** The COCA protocol
   is not just another agreement card; it is the first chance to test whether the module's distinctive
   controller/override nodes project.

## Provisional Compression Rule

A scoped module becomes merge/kill vulnerable when all three conditions hold:

1. its distinctive nodes are absent from activated paths in its authorizing evaluation;
2. another scoped module can satisfy the same required/forbidden nodes and activated-path readings
   with fewer distinctive constructs;
3. the candidate merger survives at least one held-out card without adding a new distinctive node.

Until those conditions hold, module diversity is preserved but marked as provisional rather than
treated as cumulative confirmation.
