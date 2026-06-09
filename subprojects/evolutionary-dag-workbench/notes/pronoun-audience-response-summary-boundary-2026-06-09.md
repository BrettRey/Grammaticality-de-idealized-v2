# Pronoun Audience-Reference Response Summary Boundary

**Date:** 2026-06-09
**Target lane:** `data/audience-reference-projection/`
**Status:** Descriptive response summarizer added; no evidence-status change.

## Purpose

The audience/reference lane now has a packet, response template, validator, and fixture coverage.
This pass adds a descriptive summarizer for future collected rows.

## Added Tool

`scripts/summarize_audience_reference_responses.py`

The script validates the response CSV first, then reports usable coded rows by registered prediction
cell and response channel. It summarizes 1-7 numeric fields and categorical labels but does not
assign pass/fail outcomes.

The fixture runner now checks that the summarizer runs on the empty template and refuses an invalid
response file before producing a summary.

Rows are treated as usable only when they contain a raw or coded response, are not explicitly marked
`counts_as_prediction_evidence=no`, and have no non-blank exclusion reason.

## Decision Boundary

The summary is an analysis aid, not an evaluation artifact. Evidence labels still require an
explicit update to the relevant protocol evaluation after inspecting the summary against the
pre-registered prediction register.

No graph mutation.

No score movement.

No evidence label changes.
