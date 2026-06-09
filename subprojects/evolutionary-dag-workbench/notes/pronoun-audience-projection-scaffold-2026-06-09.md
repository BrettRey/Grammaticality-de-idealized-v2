# Pronoun Audience-Reference Projection Scaffold

**Date:** 2026-06-09
**Target graph:** `graphs/archive/audience-reference-tracking-candidate.json`
**Target evaluation:** `evaluations/protocol-tests/audience-reference-tracking-2026-06-08.json`
**Status:** Data-ready scaffold; no evidence-status change.

## Purpose

The unresolved `AUD` cell is `audience-policy-framing-prediction`. Existing source work supports
pro-form feature alignment, personhood ascription, reference-chain coherence, and the need to keep
reference success separate from licensing. What is still missing is channel-specific data showing
whether audience, evaluator, institution, or policy framing shifts reported acceptability,
grammaticality attribution, social sanction, or norm orientation while reference tracking remains
stable.

## Added Files

`data/audience-reference-projection/` now contains:

- `README.md`
- `stimulus-register.csv`
- `response-channel-schema.csv`
- `prediction-register.csv`
- `coding-schema.csv`

The register turns the existing task design into concrete draft items across five cells:

- low-stakes reference baseline;
- stable reference with policy/audience frame;
- reference-failure control;
- personhood reclassification;
- chain-coherence pressure.

## Decision

No graph mutation.

No score movement.

The evaluation remains unchanged: `audience-policy-framing-prediction` stays `mixed` until response
data are collected or supplied.

## Next Boundary

The next useful step is a small pilot or structured critic run using the stimulus register. The
minimum useful output is row-level channel data keyed to `coding-schema.csv`, not a single global
acceptability verdict.
