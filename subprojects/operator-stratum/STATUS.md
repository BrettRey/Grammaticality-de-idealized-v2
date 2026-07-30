---
slug: operator-stratum
kind: paper
title: 'Why clause structure is judged like tense and agreement: public-update operators and grammaticality'
stage: complete
external: rejected
blocked_on:
- venue-decision
updated: 2026-06-26
source:
- STATUS.md
- DECISIONS.md
- publications.html
path: papers/retarget/grammaticality-de-idealized/subprojects/operator-stratum
venue: Functions of Language
external_id: FOL-26063
preprints:
- lingbuzz/009706
next_action: Choose a better-fit venue and retarget; do not revise on theoretical grounds unless the next
  venue requires reframing
notes: 'A subproject of grammaticality-de-idealized with its own STATUS.md, DECISIONS.md, main.tex and
  submission package; registered separately 2026-07-30 so its desk rejection survives into the registry
  rather than sitting in a note on the parent block. The parent block (batch-06) covers the main OVMG
  paper only. `source` paths are relative to the subproject.

  Its own STATUS.md header: "**Status:** Desk rejected by *Functions of Language* for scope/fit; retargeting
  needed... **LingBuzz:** Uploaded 2026-01-25... **Journal submission:** Submitted to *Functions of Language*
  2026-06-02; rejected 2026-06-26 as outside the journal''s scope." Article ID FOL-26063, decision signed
  by Wout Van Praet, Managing Editor. Scope/fit desk rejection only, no referee report.

  external: rejected with a live preprint, following the schema''s rule and the bresnan-dative precedent;
  the LingBuzz ID is lingbuzz/009706, from publications.html ("Why clause structure is judged like tense
  and agreement: public-update operators and grammaticality. Preprint. LingBuzz"), and the title there
  matches the submitted title exactly. stage: complete, since rejection does not change stage and this
  manuscript was packaged and sent. blocked_on: [venue-decision], from its own DECISIONS.md: "Treat the
  Functions of Language rejection as a venue-fit signal... No referee report or substantive criticism
  was provided, so the manuscript should be retargeted rather than revised on theoretical grounds."

  A sibling remains unregistered: subprojects/asterisk-de-idealized, which the parent STATUS.md records
  as a third LingBuzz subproject preprint in the OVMG family (lingbuzz/009713 per publications.html, "De-idealizing
  the asterisk: Grammaticality as conditioned stability"). It has a public preprint but no venue event,
  so it fell outside the four Brett authorised. Candidate for the same treatment.

  '
---

# STATUS.md - The Operator Stratum

**Created:** 2026-01-24
**Last updated:** 2026-06-26
**Status:** Desk rejected by *Functions of Language* for scope/fit; retargeting needed
**LingBuzz:** Uploaded 2026-01-25
**Journal submission:** Submitted to *Functions of Language* 2026-06-02; rejected 2026-06-26 as outside the journal's scope.
**Parent project:** Grammaticality_de_idealized (MVMG)

### 2026-06-26 Functions of Language Decision
- Article ID: FOL-26063.
- Submitted title: "Why clause structure is judged like tense and agreement: public-update operators and grammaticality"
- Decision: rejected by *Functions of Language* as outside the journal's scope.
- Editor/signatory: Wout Van Praet, Managing Editor.
- Triage: scope/fit desk rejection only; no substantive referee criticism was provided.
- Next action: choose a better-fit venue and retarget. Do not treat this as evidence against the argument unless the next venue requires reframing.

### 2026-06-02 Submission Notes
- Submitted as: "Why clause structure is judged like tense and agreement: public-update operators and grammaticality"
- Target journal: *Functions of Language*
- Anonymous package prepared in `submission/fol-anonymous/`
- Copy-paste submission metadata retained in `submission/fol-submission-copy-paste.md`
- Outcome: rejected for scope/fit on 2026-06-26.

### 2026-06-02 Evening Shutdown Notes
- Main submission-prep commit pushed: `c584972 Prepare FoL anonymous submission package`.
- Submission-status tracking commit pushed: `65ba5c0 Record FoL submission status`.
- Website publications/CV update pushed separately: `c51a1ce Update operator stratum submission status`.
- Central bibliography status update pushed separately: `.house-style` commit `467a560 Update operator stratum bibliography status`.
- Anonymous package includes PDF, DOCX, and LaTeX source ZIP; identity scans found no author-identifying strings in the anonymous PDF or DOCX.
- Remaining local caveat: `NOTES-cohn-multimodal.md` is still untracked in this subproject and was intentionally left out of the FoL package.

### 2026-01-26 Session Notes
- Revised per Geoff Pullum feedback on title/abstract opacity
- New title: "Why clause structure is judged like tense and agreement: a coordination account of grammaticality"
- Leavened 8 dense passages (concrete examples before abstractions throughout)
- Key pattern: introduce what something *does* before naming it
- `Reynolds_Clause_Structure_Grammaticality.pdf` ready for LingBuzz

## Summary

Argues that grammaticality judgments target a specific kind of value: **operator value**. Form-value relations belong to the operator stratum when they:
1. Conventionally contribute to public update (commitments, roles, scope)
2. Are part of a stable, closed-paradigm repertoire

## Core Argument

- Clause structure behaves "like grammar" because it IS a system of operators (clause typing, argument linking, dependency management, reference tracking)
- Tense/number behave like grammar WHERE they are grammaticalised as operators
- Accent/lexical choice are different because they contribute indexical/conceptual value that is negotiable, not publicly accountable in the same way
- BUT: phonology and lexicon CAN enter the operator stratum when grammaticalised (tone, question intonation, sign-language nonmanuals)

## Connection to MVMG

This paper develops what MVMG calls "value" in its formal model:
- MVMG's `C_t` (licensing) = entrenchment in the operator stratum
- MVMG's `map` (structural viability) = whether something can be an operator at all
- MVMG's `K` (interpretive coherence) = whether operator values cohere

The operator stratum paper explains WHY some form-value relations get policed as grammar: they function as public coordination infrastructure.

## Connection to Bayesian family

- **LBE paper**: Opportunity frequency + preemption dynamics → explains how operator gaps stabilize
- **Varieties paper**: S/A/I conditioning → explains how operator repertoires vary by situation/ascription/identification
- **This paper**: Defines what operators ARE and why they're special

## Diagnostics Proposed

1. Paradigmatic closure (small enumerable sets)
2. Broad scope (clause-wide consequences)
3. High opportunity mass (strong preemption)
4. Repair sensitivity ("you can't say that" vs style negotiation)
5. ERP dissociation (P600 vs N400 profiles)

## Predictions

1. Repair asymmetries (operator vs indexical mismatches)
2. Satiation asymmetries (high-opportunity gaps resist satiation)
3. Phonological operators behave like morphosyntax
4. Processing signatures track operator failure, not module boundaries

## Build

```bash
xelatex main.tex && biber main && xelatex main.tex
```

Uses EB Garamond font, self-contained refs.bib via filecontents.
