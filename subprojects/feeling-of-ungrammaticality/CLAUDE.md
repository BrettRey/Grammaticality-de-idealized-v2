# CLAUDE.md - The Feeling of Ungrammaticality

**Parent project:** `Grammaticality_de_idealized/` (OVMG)
**Status:** Seed
**Created:** 2026-01-29

## Overview

What *is* the feeling of ungrammaticality? The OVMG framework treats it as a detector/measurement channel distinct from grammatical status itself. This subproject develops that distinction.

## Position in the OVMG Family

| Subproject | Question |
|------------|----------|
| `operator-stratum/` | What operators ARE |
| `asterisk-de-idealized/` | What grammaticality IS |
| `etiological-account/` | WHY gaps emerge and persist |
| **This paper** | What the FEELING is |

## Core Claims (from parent framework)

The feeling of ungrammaticality is:
- A **metacognitive signal** triggered by instability or high repair cost
- **Not identical to grammatical status** - yields false positives (licit but feels bad) and false negatives (illicit but passes undetected)
- Modeled as **inverse conditioning** / **surprisal**: $-\log P(u \mid c)$

**Inputs to the detector:**
1. $\widetilde{G}_t$ (stability score)
2. Processing costs
3. Ideological filtering

## Potential Angles

1. **Psycholinguistic:** What *is* the detector? Neural correlates, time course, individual differences, relationship to error monitoring
2. **Methodological:** When can ratings be trusted as evidence about $G_t$? Systematic confounds, task effects, calibration
3. **Philosophical:** Is the feeling a perception, a judgment, an intuition? Relationship to other metacognitive feelings (tip-of-tongue, feeling of knowing)

## Key Phenomena to Explain

- **Satiation:** Some degraded structures improve with exposure; others don't
- **False positives:** Centre-embedding, garden paths - licit but feel terrible
- **False negatives:** Agreement attraction, unnoticed violations
- **Ideological overlay:** Forms feel worse when attributed to stigmatized groups
- **Task effects:** Different tasks yield different profiles for same items

## Connections

- **HPC book ch 5:** "Discrete from continuous" - philosophical foundation
- **asterisk-de-idealized §4.6:** Brief treatment of feeling vs status
- **Fanselow & Frisch (2021):** Key reference on dissociations
- **Gibson & Fedorenko (2026):** Processing costs and acceptability

## Build

```bash
# When main.tex exists:
xelatex main.tex && biber main && xelatex main.tex
```

Uses parent project's `refs.bib` via symlink (to be created).

## Inheritance

- Bibliography from grandparent (`../../../refs.bib`)
- House style from `../../../../.house-style/`
- Editorial conventions from parent `CLAUDE.md`
