# Pronoun Audience-Reference Response Validator

**Date:** 2026-06-09
**Target lane:** `data/audience-reference-projection/`
**Status:** Response-file validator added; no evidence-status change.

## Purpose

The audience/reference projection lane now has draft stimuli, response channels, a pilot packet,
and a response template. This pass adds a validator so future response files cannot silently drift
from the registered stimulus metadata or coding schema.

## Added Tool

`scripts/validate_audience_reference_responses.py`

The validator checks:

- required fields from `coding-schema.csv`;
- `item_id` resolution against `stimulus-register.csv`;
- metadata consistency for cell, referent status, pro-form pattern, audience/evaluator, norm
  centre, and speaker identity;
- allowed enum values where declared;
- 1-7 numeric bounds for confidence, feature-fit, and acceptability fields;
- expected item-by-channel rows;
- duplicate item/channel rows.

The empty template validates:

```bash
python3 scripts/validate_audience_reference_responses.py
```

Collected runs can be checked more strictly with:

```bash
python3 scripts/validate_audience_reference_responses.py path/to/responses.csv --require-responses
```

## Decision

No graph mutation.

No score movement.

No evidence label changes. The validator protects future data use; it does not supply data.
