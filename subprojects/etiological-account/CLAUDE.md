# CLAUDE.md - Etiological Account

**Parent project:** `Grammaticality_de_idealized/` (OVMG)
**Status:** Skeleton
**Target:** TBD (theory journal)

## Overview

This is the etiological companion to the constitutive papers (OVMG main paper and "The asterisk de-idealized"). While those papers ask *what grammaticality is* (state theory), this paper asks *why C_t(u,c) trajectories settle where they do* (dynamics).

Two complementary modules:
1. **Opportunity-sensitive preemption** -- proximate mechanism for repertoire exclusion
2. **Coordination equilibria** -- game-theoretic explanation for why exclusion persists

The paper was announced as "in preparation" at the end of the asterisk paper (lines 666--670).

## Build

```bash
xelatex main.tex && biber main && xelatex main.tex
```

Uses parent project's `refs.bib` via symlink.

## Inheritance

This subproject inherits:
- Bibliography from parent project (`../../refs.bib`)
- House style from `../../../.house-style/` (via parent)
- Editorial conventions from parent `CLAUDE.md`

## Key Equations

- **Stability score:** $\widetilde{G}_t(u,c) = \mathsf{map}(u,c) \cdot K(u,c) \cdot C_t(u,c)$
- This paper focuses on **C_t** (repertoire status) and its dynamics

## Scope boundaries

This paper does NOT cover:
- What grammaticality IS (constitutive -- handled by main paper + asterisk)
- What operators ARE (handled by operator-stratum subproject)
- Metaphysical questions about grammaticality as a natural kind (Grammaticality_as_Kind_Miller)
- How operators acquire high functional load (CxG Chunking & Feature Selection)
- Emergence of grammar (Grammar_and_emergence with Nefdt -- NO LLMs)

## Semantic Macros

- `\term{}` -- technical terms (small caps)
- `\mention{}` -- linguistic forms (italics)
- `\enquote{}` -- quotations, scare quotes
- `\ungram{}` -- ungrammatical examples (*...)
- `\marg{}` -- marginal examples (?...)
- `\odd{}` -- semantically odd (#...)
