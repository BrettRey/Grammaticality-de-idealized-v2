# STATUS.md - The Asterisk De-idealized

**Created:** 2026-01-24
**Last updated:** 2026-01-26
**Status:** Complete draft (18 pages)
**Parent project:** Grammaticality_de_idealized (MVMG)
**Target:** Journal of Linguistics "Looking Back, Moving Forward" section

## Summary

A retrospective/prospective article reconceptualising grammaticality as **conditioned stability** of form--value relations. Reviews 20th-century theory (well-formedness, processing, usage, norms) and diagnoses why the competence--performance--usage triangulation hasn't resolved the impasse.

## Core Argument

The asterisk has been used to mark four different things:
1. Structural crash (map = 0)
2. Interpretive incoherence (K ≈ 0)
3. Community non-licensing (C_t ≈ 0)
4. Feeling of anomaly (processing/ideology)

The MVMG decomposition (G = map · K · C_t) separates these and restores empirical vulnerability.

## Key Examples

- `*Can the have running` — structural crash
- `Colorless green ideas...` — map=1, K low but recoverable
- `*I've finished it yesterday` — map=1, K≈0 (temporal conflict)
- `?a friend of whose` — map=1, K high, C_t uncertain (low opportunity)
- `The bread the baker...` — map=1, K high, C_t high, but processing cost
- `*I have 25 years` — map=1, K high, C_t≈0 (preemption)
- `*Which did you buy car?` — LBE: map=1, K high, C_t≈0

## Connection to MVMG

This paper IS the MVMG presented for a general theoretical linguistics audience. It:
- Introduces the state theory formally (equations 1-2)
- Distinguishes grammaticality from feeling of anomaly
- Motivates the research agenda: operationalising c, measuring opportunity, etc.

## Connection to Other Papers

- **Operator stratum** (now cited): Defines what operators ARE; this paper explains HOW their status is determined
- **LBE paper** (now cited): Provides the learning-theoretic Bayesian foundation for C_t trajectories
- **Varieties paper**: Elaborates the S/A/I conditioning structure for c
- **HPC book ch 5** (now cited): Provides philosophical foundation for ontology/epistemology distinction; two-layer model (grammaticality → noise → acceptability)

## Build

```bash
xelatex main.tex && biber main && xelatex main.tex
```

Uses parent project's refs.bib via symlink.

## Session Log

### 2026-01-26

Imported insights from polished operator-stratum paper while maintaining distinct focus:

**Added paragraphs:**
- Three-stratum infrastructure model (expression-shape / operator / payload)
- Information-theoretic perspective (operators as protocol headers, entropy reduction)
- Repair asymmetry predictions (operator vs payload mismatches)
- Forward-reference to operator hypothesis in §8 (future research)

**Citations added:**
- Shannon 1948, Cover & Thomas 2006 (information theory)
- reynolds2026operators, reynolds2026lbe (LingBuzz preprints)
- Fixed sprouse2016 → sprouse2013

**Distinctiveness preserved:**
- Asterisk paper: state theory (what grammaticality IS) — formal equations, falsification conditions, opportunity methodology
- Operator paper: domain theory (what gets policed AS grammar) — typological predictions, cross-linguistic scope

### 2026-01-26 (continued session)

**House style completion:**
- Oxford spelling throughout (-ize)
- All \paragraph{} removed, converted to prose transitions
- Contractions, throat-clearers, hackneyed connectives cleaned

**Conceptual refinements:**
- Added Saussurian "value" footnote (what a form conventionally contributes)
- Clarified four-vs-three distinction at §3 opening
- Removed redundant §2 ending (now covered by §3)
- Added epistemic accessibility clause with HPC book ch 5 connection

**Citation audit (per external review):**
- Fixed: Pullum 2009 URL, Shannon 1948 (both parts), Grodner & Gibson pages, Sprouse LaTeX artefact, McCawley pages
- Added: Snyder 2000/2022 (satiation), Huddleston & Pullum 2002 (present perfect), Wagers 2009 (agreement attraction)
- Added: reynolds2025hpcbook (3 locations: footnote at ontology/epistemology distinction, §4.6 two-layer model, satiation line)

**Cross-paper architecture revealed:**
- HPC book ch 5 provides philosophical foundation for G_t vs feeling distinction
- Two-layer model: discrete grammaticality filtered through noise = gradient acceptability
- Satiation as evidence the mapping is plastic (not grammar rewriting)
