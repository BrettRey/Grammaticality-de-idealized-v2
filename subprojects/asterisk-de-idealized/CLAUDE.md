# CLAUDE.md - The Asterisk De-idealized

**Parent project:** `Grammaticality_de_idealized/` (MVMG)
**Status:** Complete draft
**Target:** Journal of Linguistics "Looking Back, Moving Forward"

## Overview

This is the MVMG framework presented for a general theoretical linguistics audience. It reviews the history of grammaticality theory and proposes the state-theoretic reconceptualisation as conditioned stability.

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
- **Membership:** $G_t(u,c) = \mathbb{I}[\widetilde{G}_t \geq \tau(c)]$

## Semantic Macros

- `\term{}` — technical terms (small caps)
- `\mention{}` — linguistic forms (italics)
- `\enquote{}` — quotations, scare quotes
- `\ungram{}` — ungrammatical examples (*...)
- `\marg{}` — marginal examples (?...)
- `\odd{}` — semantically odd (#...)

## House Style Notes

This document already uses `\enquote{}` correctly for scare quotes. The `\mention{}` macro is used for linguistic examples being mentioned, which is correct usage.
