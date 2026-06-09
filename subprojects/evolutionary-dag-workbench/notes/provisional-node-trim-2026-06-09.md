# Provisional Node Trim

**Date:** 2026-06-09
**Trigger:** `notes/scoped-module-load-bearing-audit-2026-06-09.md`
**Graphs changed:**

- `graphs/archive/audience-reference-tracking-candidate.json`
- `graphs/archive/context-indexed-dynamic-feedback-candidate.json`

## Decision

Trim two distinctive nodes that were absent from their scoped module's authorizing evaluation:

- `judgment_task_setting_t1` from `audience-reference-tracking-candidate`;
- `entrenchment_t1` from `context-indexed-dynamic-feedback-candidate`.

## Rationale

Both nodes were plausible earlier-stage commitments, but neither was load-bearing in the current
authorizing evaluation:

- neither appeared in required nodes;
- neither appeared in required or forbidden edge endpoints;
- neither appeared in activated paths;
- neither appeared in the module's scoped `score_status.scope`.

Keeping them would have made the modules look more expressive than their current evaluations
justify. Removing them applies the workbench's compression discipline without changing any scope
label or numeric score.

## Effect

The regenerated `data/module-compression/authorizing-load-bearing.csv` now contains no
`not_authorized` distinctive nodes.

The trim does not decide that `judgment_task_setting` or `entrenchment` are bad constructs in
general. It only says that these scoped modules have not earned those constructs yet. A future graph
can reintroduce either node if a card or evaluation makes it load-bearing.
