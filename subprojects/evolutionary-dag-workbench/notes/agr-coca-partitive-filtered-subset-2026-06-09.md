# AGR COCA Partitive/QN Fully Filtered Subset

**Date:** 2026-06-09
**Evaluation:** `evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`
**Status:** Narrow passed prediction test added; broad partitive/QN test remains `mixed`.

## Purpose

The critic-verdict variance pass correctly blocked a clean `passed` label for the broad
partitive/QN people-frame test because the largest positive cell, `lots of people are`, is only a
100-row bounded KWIC sample.

This note records a narrower result that does not depend on that sampled positive cell.

This is a post-variance evaluation refinement. It was not present in the packet used for the three
critic-verdict variance runs.

## Evidence

Fully filtered registered cells:

| query | status | target rows |
|---|---|---:|
| `plenty of people are` | KWIC filtered | 63 plural |
| `the rest of the people are` | KWIC filtered | 14 plural |
| `plenty of people is` | raw zero | 0 singular |
| `the rest of the people is` | raw zero | 0 singular |
| `lots of people is` | KWIC filtered | 0 licensed singular |

The narrower subset is therefore 77 filtered plural target rows and 0 licensed singular target rows,
without using the sample-coded `lots of people are` positive cell.

## Evaluation Change

Add `partitive-qn-fully-filtered-subset` as a separate `passed` prediction test.

Keep `partitive-qn-coca-targeted-kwic` as `mixed`.

The distinction is deliberate:

- the broad partitive/QN cell is supportive but mixed because its largest positive row source is
  sampled;
- the smaller fully filtered subset cleanly supports the predicted direction but does not license
  the broader claim by itself.

## Decision

No graph mutation.

No score movement.

The next data boundary remains the same: retrieve and code all visible pages for
`lots of people are`, or replace the broad partitive/QN test with enough fully filtered registered
subcells that no sampled high-count cell is doing load-bearing work.
