# CLAUDE.md

This file provides guidance to Claude Code when working with this project.

## Project Overview

**Title:** Grammaticality De-idealized: The OVMG Model
**Author:** Brett Reynolds

This paper develops the Operator-Value Model of Grammaticality (OVMG), formalizing the distinction between objective grammaticality G(u) and subjective feeling of grammaticality F(u).

## Terminology Evolution

The model name has evolved as the theory sharpened:

| Version | Name | Why Changed |
|---------|------|-------------|
| MMMG | Multi-Modal Morphosyntactic Model of Grammaticality | Original |
| MVMG | Morphosyntactic-Value Model of Grammaticality | "Meaning" too narrow – value captures phonological/distributional regularities, is relational and contrastive (Saussure) |
| **OVMG** | Operator-Value Model of Grammaticality | "Morphosyntax" too narrow – other languages use tone, particles, word order; "operator" is channel-agnostic |

The **operator-stratum** subproject defines what operators are. The main paper uses operators as the unit of grammatical signaling.

Key equations:
- G(u) = C^t(u) · K(u) · map (objective: situational licensing × speaker knowledge × mapping)
- F(u) = -α(1-G(u)) - γL·L(u) - Pother(u) + η (subjective: includes processing costs, noise)

## Build System

```bash
# Full build (use XeLaTeX or LuaLaTeX, not pdfLaTeX)
xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex

# Lingbuzz preprint version
xelatex LingbuzzPreprint.tex && biber LingbuzzPreprint && xelatex LingbuzzPreprint.tex
```

## Key Files

- `main.tex` - Main document
- `LingbuzzPreprint.tex` - Lingbuzz submission version
- `refs.bib` - Bibliography
- `NOTES.md` - Working notes and external feedback
- `AGENTS.md` - Multi-agent coordination

## Cross-Project Connections

- **Grammar_and_emergence**: The OVMG's F(u)/G(u) distinction maps to emergence paper's commutativity question
- **Grammaticality_as_Kind_Miller**: Companion paper (metaphysics vs methodology framing)
- **Transparent_free_relatives**: TFRs as empirical test case for gradient grammaticality

## House Style

See portfolio-level `.house-style/` for LaTeX conventions and writing style.

## Editorial Approach (Lesson Learned)

**Don't do superficial find/replace for terminology changes.** When asked to change terminology throughout the document (e.g., "meaning" → "value"), read sections holistically and rewrite editorially. Piecemeal substitutions create awkward or incoherent prose. Step back, understand what the section is trying to say, and rewrite it properly with the new terminology integrated naturally.

## Multi-Agent Dispatch (MANDATORY)

Before dispatching multiple agents, ALWAYS ask Brett:
1. **Which model(s)?** Claude, Codex, Gemini, Copilot
2. **Redundant outputs?** Multiple models on same task for different perspectives?

See portfolio-level `CLAUDE.md` for CLI command patterns and full workflow.
