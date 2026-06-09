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
- `prediction-register.csv`: pre-run predictions, item memberships, pass/fail thresholds, and
  active paths.
- `coding-schema.csv`: row-level coding fields for future responses.
- `pilot-packet.md`: participant/critic-facing pilot packet generated from the register.
- `pilot-response-template.csv`: row-level response template generated from the register.
- `simulations/`: simulation-only response dry runs; not evidence.

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

## Build the Pilot Packet

Regenerate the pilot packet and response template with:

```bash
python3 scripts/build_audience_reference_pilot_packet.py \
  --run-id audience-reference-pilot-template
```

The packet is intentionally participant-facing: it omits hidden predictions and expected-reference
metadata. Use `prediction-register.csv` separately when evaluating the collected rows.

Validate a response file with:

```bash
python3 scripts/validate_audience_reference_responses.py \
  data/audience-reference-projection/pilot-response-template.csv
```

Add `--require-responses` when checking a collected run rather than an empty template.

Summarize a validated response file with:

```bash
python3 scripts/summarize_audience_reference_responses.py \
  path/to/responses.csv \
  --output path/to/summary.md
```

The summary is descriptive. It does not decide prediction-test outcomes or update evidence labels.

For simulation-only rows marked `counts_as_prediction_evidence=no`, add `--include-non-evidence`
to check the pipeline without treating the rows as evidence.

Generate the current simulation dry run with:

```bash
python3 scripts/simulate_audience_reference_responses.py
```
