# Scoped Module Load-Bearing Audit

**Date:** 2026-06-09
**Runner:** `scripts/audit_authorizing_load_bearing.py`
**Summary data:** `data/module-compression/authorizing-load-bearing.csv`
**Status:** Compression screen; followed by a provisional-node trim; no merge, kill, or score
movement.

## Question

The first compression audit used node overlap to identify suspicious pairs. This follow-up asks a
stricter question:

> Are each scoped module's distinctive nodes actually used by its authorizing evaluation?

The runner computes distinctive nodes for every `scoped_module`, then checks whether each one appears
in the authorizing evaluation as a required node, required/forbidden edge endpoint, or activated-path
endpoint.

## Result

The suspected merger pairs are mostly protected.

| Pair or module | Result | Interpretation |
|---|---|---|
| `FDL` / `UOB` | no merger | `FDL`'s distinctive `constructional_frame_fit`, `constructional_function`, and `construction_specific_dependency_licensing` are all activated-path nodes; `UOB`'s `token_innovability` is an activated-path node and `repertoire_closedness` is required by the authorizing evaluation. |
| `OPG` / `DYN` | no merger | `OPG`'s distinctive nodes are all required, and three are activated-path nodes; `DYN` retains distinctive diachronic/correction nodes in activated paths, so it cannot be reduced to `OPG`. |
| `AGR` | protected | The core controller/alignment/override/notional nodes are activated-path nodes; `retrieval_attractor_salience` is protected by required-edge machinery rather than the held-out scope paths. |
| `PNP` | protected | `felt_naturalness_context` is activated-path load-bearing; `measurement_task` is protected through requirements. |

The initial run exposed two vulnerabilities:

| Module | Vulnerable node | Why it is vulnerable |
|---|---|---|
| `ART` | `judgment_task_setting` | Present in the graph but absent from the authorizing evaluation's requirements and activated paths. |
| `DYN` | `entrenchment` | Present in the graph but absent from the authorizing evaluation's requirements and activated paths. |

Those two nodes were subsequently trimmed in `notes/provisional-node-trim-2026-06-09.md`. The
current `authorizing-load-bearing.csv` is regenerated after the trim and contains no
`not_authorized` distinctive nodes.

## Decision

Do not merge `FDL` with `UOB`, and do not merge `OPG` with `DYN` on the current evidence.

The next compression rule is:

> A distinctive node that is absent from its authorizing evaluation should be treated as provisional
> until a later evaluation uses it or a trim pass removes it.

The low-cost trim has already been applied to `ART.judgment_task_setting` and `DYN.entrenchment`.
The next compression pass should therefore target a substantive merger/kill test, not another
distinctive-node bookkeeping pass.
