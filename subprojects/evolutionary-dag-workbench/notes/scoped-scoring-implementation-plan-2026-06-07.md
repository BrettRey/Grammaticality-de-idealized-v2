# Scoped Scoring Implementation Plan
**Date:** 2026-06-07
## Goal
Allow a representation to receive a scoped-module score without implying that it is a general theory of grammaticality.
## Changes
1. Add a scoring policy note distinguishing:
  
  - `general_account`
    
  - `scoped_module`
    
  - `unscored`
    
2. Extend graph JSON with a `score_status` object. The object should make the scoring scope explicit before any non-zero score is allowed.
  
3. Update `lint_graph.py` so non-zero scores require:
  
  - `score_status.kind`;
    
  - `score_status.evaluation`;
    
  - the referenced evaluation file exists;
    
  - `score_status.kind` is `scoped_module` or `general_account`;
    
  - seeds still remain all-zero.
    
4. Update `score_graph.py` output so score scope and evaluation references are visible.
  
5. Add negative fixtures for:
  
  - non-zero score without `score_status`;
    
  - non-zero score with missing evaluation;
    
  - invalid score kind.
    
6. If the tooling is clean, assign conservative scoped-module scores only to:
  
  - `context-indexed-dynamic-feedback-candidate`
    
  - `context-aware-operator-gap-candidate`
    

No graph should receive a `general_account` score in this pass.
## Verification
Run:

```bash
python3 scripts/validate_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/lint_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/score_graph.py graphs/seeds/*.json graphs/archive/*.json
python3 scripts/validate_evaluation.py evaluations/protocol-tests/*.json
python3 scripts/run_fixture_tests.py
python3 -m py_compile scripts/validate_graph.py scripts/lint_graph.py scripts/score_graph.py scripts/validate_evaluation.py scripts/run_fixture_tests.py
```
