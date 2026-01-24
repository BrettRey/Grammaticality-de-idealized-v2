# STATUS.md - The Asterisk De-idealized

**Created:** 2026-01-24
**Last updated:** 2026-01-24
**Status:** Complete draft
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

- **Operator stratum**: Defines what operators ARE; this paper explains HOW their status is determined
- **LBE paper**: Provides the learning-theoretic Bayesian foundation for C_t trajectories
- **Varieties paper**: Elaborates the S/A/I conditioning structure for c

## Build

```bash
xelatex main.tex && biber main && xelatex main.tex
```

Uses parent project's refs.bib via symlink.
