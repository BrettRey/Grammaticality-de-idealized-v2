# CLAUDE.md

This file provides guidance to Claude Code when working with this project.

## Project Overview

**Title:** Grammaticality De-idealized: The MMMG Model
**Author:** Brett Reynolds

This paper develops the Morphosyntactic-Meaning Model of Grammaticality (MMMG), formalizing the distinction between objective grammaticality G(u) and subjective feeling of grammaticality F(u).

Key equations:
- G(u) = C^t(u) · K(u) · map (objective: community licensing × speaker knowledge × mapping)
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

- **Grammar_and_emergence**: The MMMG's F(u)/G(u) distinction maps to emergence paper's commutativity question
- **Grammaticality_as_Kind_Miller**: Companion paper (metaphysics vs methodology framing)
- **Transparent_free_relatives**: TFRs as empirical test case for gradient grammaticality

## House Style

See portfolio-level `.house-style/` for LaTeX conventions and writing style.

## Multi-Agent Dispatch (MANDATORY)

Before dispatching multiple agents, ALWAYS ask Brett:
1. **Which model(s)?** Claude, Codex, Gemini, Copilot
2. **Redundant outputs?** Multiple models on same task for different perspectives?

See portfolio-level `CLAUDE.md` for CLI command patterns and full workflow.
