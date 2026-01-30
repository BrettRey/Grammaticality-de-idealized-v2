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

## Subprojects

| Subproject | Question | Status |
|------------|----------|--------|
| `operator-stratum/` | What operators ARE | LingBuzz (Jan 25) |
| `asterisk-de-idealized/` | What grammaticality IS | LingBuzz (Jan 28) |
| `etiological-account/` | WHY gaps emerge and persist | Draft |
| `feeling-of-ungrammaticality/` | What the FEELING is | Seed |

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
- **HPC book ch 5** ("Discrete from continuous"): Provides philosophical foundation for the G_t vs feeling-of-ungrammaticality distinction. The two-layer model (discrete grammaticality filtered through noise → gradient acceptability) is developed there with hyperreal formalization. Key claim: "The uncertainty is epistemic, not semantic: there is a fact of the matter about where the boundary falls; we just can't determine what it is." Satiation effects are evidence that the mapping is plastic, not that grammar rewrites during an experiment.

## House Style

See portfolio-level `.house-style/` for LaTeX conventions and writing style.

## Editorial Approach (Lessons Learned)

**Don't do superficial find/replace for terminology changes.** When asked to change terminology throughout the document (e.g., "meaning" → "value"), read sections holistically and rewrite editorially. Piecemeal substitutions create awkward or incoherent prose. Step back, understand what the section is trying to say, and rewrite it properly with the new terminology integrated naturally.

**Engage with the conceptual network, not just individual sources.** Brett's work is building a framework — a network of interconnected ideas across multiple papers. When citing a related paper (e.g., HPC book ch 5), don't just grep for quotable lines. Read the chapter to understand how the ideas connect, what conceptual architecture is being built, and where the current paper sits in that network. Mining sources for quotes without understanding the framework is incurious and misses the point.

## Multi-Agent Dispatch (MANDATORY)

Before dispatching multiple agents, ALWAYS ask Brett:
1. **Which model(s)?** Claude, Codex, Gemini, Copilot
2. **Redundant outputs?** Multiple models on same task for different perspectives?

See portfolio-level `CLAUDE.md` for CLI command patterns and full workflow.
