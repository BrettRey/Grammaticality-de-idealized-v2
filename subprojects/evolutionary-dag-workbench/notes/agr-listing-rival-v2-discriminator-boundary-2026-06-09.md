# AGR/List V2 Discriminator Boundary

**Date:** 2026-06-09
**Target module:** `graphs/archive/agreement-controller-override-candidate.json`
**Rival:** `graphs/archive/agreement-construction-listing-baseline-candidate.json`
**Data lane:** `data/agr-coca-projection/`
**Status:** Redesign registered after the first direct-string tranche returned all zero cells.

## Reason For The Redesign

The first low-frequency QN tranche was methodologically right but operationally too narrow:

- `a smattering of critics are/is`;
- `a gaggle of tourists are/is`;
- `a tranche of voters are/is`.

All six direct COCA list queries returned no matching records. That result is not evidence for
`AGR` and not evidence for construction-specific listing. It is a sparse-query failure.

## Live Rival

The real rival is not surface-head number. It is construction-specific listing:

> each lexical or constructional frame has a learned agreement preference, and no separate
> controller-identification, notional-basis, or licensed-override machinery is needed.

Known cells such as `majority of people`, `a bunch of people`, and `a number of people` can be
accommodated by listing after their distributions are known. The discriminator has to test
generalization before local item preferences are available.

## V2 Design

V2 separates two phases.

### Phase 1: Denominator-Only Scout

Run only phrase-level list queries, without finite agreement:

- `a smattering of people`;
- `a smattering of voters`;
- `a smattering of critics`;
- `a sprinkling of people`;
- `a sprinkling of voters`;
- `a sprinkling of critics`;
- `a scattering of people`;
- `a scattering of voters`;
- `a scattering of critics`;
- `a gaggle of people`;
- `a gaggle of tourists`;
- `a gaggle of voters`;
- `a tranche of people`;
- `a tranche of voters`;
- `a tranche of critics`.

These rows are discovery-only. They may be used to decide whether a frame has enough denominator
mass for follow-up, but they cannot be used to decide AGR/LIST evidence.

Use:

```bash
python3 scripts/run_agr_coca_queries.py --cell low-frequency-qn-scout --type list --run
python3 scripts/select_agr_listing_v2_candidates.py \
  --cell low-frequency-qn-scout \
  --output data/agr-coca-projection/low-frequency-qn-v2-candidates.csv
```

Default eligibility is 3-200 raw phrase hits. Below that, the agreement follow-up is likely too
sparse; above that, construction-specific listing can plausibly claim an already-central stored
frame.

### Phase 2: Frozen Finite-Agreement Follow-Up

Only after the eligible item list is written should the finite-agreement follow-up be registered.
For each eligible frame, register paired `are/is` and, where appropriate, `were/was` strings before
inspecting agreement rows.

The follow-up is the first phase that can count as AGR/LIST evidence.

## First Live Attempt

A first live attempt to run the denominator scout on 2026-06-09 failed on the first phrase,
`a smattering of people`, with an English-Corpora.org server-error response. No raw artifact was
written and no candidate list was generated. A follow-up wrapper status probe reported the COCA
browser profile as unauthenticated. This is an operational COCA/session state, not an evidence
label.

## Pass/Fail Boundary

`AGR` gains pressure against listing only if the frozen v2 follow-up shows a shared plural or
context-conditioned profile across several eligible low-frequency frames, where the pattern follows
notional/controller diagnostics better than item-specific listing.

The construction-listing baseline remains live if:

- the scout finds no eligible frames;
- the finite-agreement rows remain too sparse;
- each eligible frame behaves idiosyncratically;
- the result can only be described by adding post-hoc local preferences; or
- the data show surface-head fallback rather than notional/controller generalization.

No graph mutation, evidence-status upgrade, scoped label, `projective_power`, or numeric score
movement follows from the denominator scout alone.
