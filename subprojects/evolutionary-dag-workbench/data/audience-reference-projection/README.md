# Audience Reference Projection Lane

**Created:** 2026-06-09
**Protocol/design:** `notes/pronoun-audience-policy-task-design-2026-06-09.md`
**Target graph:** `graphs/archive/audience-reference-tracking-candidate.json`
**Target evaluation:** `evaluations/protocol-tests/audience-reference-tracking-2026-06-08.json`

This directory scaffolds a data-ready task for the unresolved audience/policy pronoun cell. It does
not contain participant data.

## Files

- `stimulus-register.csv`: draft item frames and manipulations.
- `response-channel-schema.csv`: response channels mapped to workbench constructs.
- `prediction-register.csv`: pre-run predictions, pass/fail thresholds, and active paths.
- `coding-schema.csv`: row-level coding fields for future responses.

## Current Status

The existing source lanes support pro-form feature alignment, reference tracking, personhood
ascription, and chain coherence. The unresolved question is whether audience, evaluator, policy, or
institutional framing shifts reported acceptability, grammaticality attribution, social sanction, or
respect/policy judgment while reference tracking remains constant.

No evidence label changes follow from this scaffold. The relevant prediction test remains `mixed`
until response data are collected or supplied.

## Minimal Run Boundary

A useful first run needs at least:

- one low-stakes reference baseline;
- one stable-reference policy/audience manipulation;
- one reference-failure control;
- one personhood-reclassification item;
- one chain-coherence item;
- separate response prompts for reference identification, feature/personhood fit, acceptability,
  attribution, social sanction, and norm orientation.

Do not collapse these channels into a single acceptability score.
