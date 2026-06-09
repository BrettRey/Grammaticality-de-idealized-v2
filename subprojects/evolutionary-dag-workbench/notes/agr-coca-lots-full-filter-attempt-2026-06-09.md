# AGR COCA `lots of people are` Full-Filter Attempt

**Date:** 2026-06-09
**Target cell:** `partitive-qn-coca-targeted-kwic`
**Status:** Tooling improved; full filtering not completed; no evidence-label upgrade.

## Purpose

The critic-verdict variance pass downgraded the partitive/QN people-frame prediction from `passed`
to `mixed` because the largest positive cell, `lots of people are`, was only a pre-declared
100-row KWIC sample. This pass tests whether the full cell can be retrieved and filtered.

## Tooling Change

`scripts/fetch_coca_kwic_from_list.mjs` now has an `--all-pages` option. The option follows COCA
KWIC page links from the clicked list-result frame and combines rows across pages when the site
exposes paginated results.

Intended command:

```bash
node scripts/fetch_coca_kwic_from_list.mjs \
  --query 'lots of people are' \
  --all-pages \
  --output data/agr-coca-projection/raw/partitive-agreement-followup/kwic/01-lots-of-people-are-all-pages.json
```

## Live Attempts

The higher-hit direct attempt failed:

```bash
node scripts/fetch_coca_kwic_from_list.mjs \
  --query 'lots of people are' \
  --hits 500 \
  --output data/agr-coca-projection/raw/partitive-agreement-followup/kwic/01-lots-of-people-are-full.json
```

Result: COCA returned a server-error page.

A frame-inspection probe showed that the normal `lots of people are` KWIC page exposes pagination
links (`p=1`, `p=2`) after a successful list-result click, so full retrieval is likely feasible
through pagination rather than by increasing `--hits`.

The first `--all-pages` retrieval attempt did not complete: the KWIC frame timed out before
parseable rows were available. A subsequent small-cell test also returned a COCA server-error page.
That looks like live site/session/rate behavior, not a new evidential result.

## Decision

Do not upgrade the partitive/QN evidence label.

Keep `partitive-qn-coca-targeted-kwic` at `mixed`.

No graph mutation or score movement follows.

## Next Boundary

Retry the `--all-pages` command after the COCA session/rate state clears. If it retrieves all
visible pages, create a row-level coding file for the combined rows and then reconsider whether the
partitive/QN test can move from `mixed` to `passed`.
