---
slug: operator-stratum
kind: paper
title: 'Why clause structure is judged like tense and agreement: public-update operators and grammaticality'
stage: complete
external: rejected
blocked_on:
- venue-decision
updated: 2026-08-22
source:
- STATUS.md
- DECISIONS.md
- publications.html
path: papers/retarget/grammaticality-de-idealized/subprojects/operator-stratum
venue: Functions of Language
external_id: FOL-26063
preprints:
- lingbuzz/009706
next_action: Choose a better-fit venue and retarget from the theoretically revised manuscript; preserve
  the four-way licensing/operator/value/exponent distinction
notes: 'A subproject of grammaticality-de-idealized with its own STATUS.md, DECISIONS.md, operator-stratum.tex and
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
**Last updated:** 2026-08-22
**Status:** Desk rejected by *Functions of Language* for scope/fit; theoretically revised; retargeting needed
**LingBuzz:** Uploaded 2026-01-25
**Journal submission:** Submitted to *Functions of Language* 2026-06-02; rejected 2026-06-26 as outside the journal's scope.
**Parent project:** Grammaticality_de_idealized (OVMG)

### 2026-08-22 Theoretical and clarity revision
- Ox Alpha and Claude Fable independently reviewed the manuscript, followed by an Ox Alpha level/category audit.
- Operator membership now has two conditions only: a closed paradigm and a paradigm-level public-update role. Opportunity count modulates evidence concentration and categoricality; it does not define membership.
- Constructional licensing, operator membership, value selection, and exponent licensing are treated as intersecting dimensions rather than exclusive strata.
- *Le hiver* is analyzed as a value-intact operator-exponent error; *depend of* as a head-specific complement-construction error. Categorical correction no longer diagnoses operator membership or a grammar/style binary.
- Historical recruitment is a diachronic support hypothesis rather than a synchronic membership condition. Population persistence requires adoption and retention, not learner updating alone.
- The principal tests now concern repair locus, paradigm-level contribution despite token redundancy, and cross-substance operator profiles. Satiation and opportunity effects are entrenchment corollaries rather than operator diagnostics.
- `latexmk -xelatex operator-stratum.tex` builds the revised manuscript with no missing citations or references.

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
2. Are part of a small, closed conventional paradigm

## Core Argument

- Clause structure belongs to the operator stratum where it packages clause type, argument linking, dependency scope, or reference tracking.
- Categorical grammaticality is broader: community-specific constructions can be licensed or excluded without an operator contrast.
- Tense and number qualify where languages grammaticalize them as closed paradigms with a public-update role.
- Accent and lexical choice usually contribute indexical or conceptual value, but phonological, lexical, and gestural material can realize operator values.

## Connection to OVMG

This paper develops the boundary around what OVMG calls an operator value:
- `map` asks whether an assembly covers the form--value pair; it does not diagnose operator membership.
- `K` asks whether grammatically encoded operator contributions unify.
- `C_t` tracks constructional licensing more broadly, including categorical non-operator conventions.
- The repair module distinguishes update-oriented repair from correction of an exponent or construction.

The operator paper explains why some grammatical contrasts configure public update while leaving grammaticality as a whole broader than the operator stratum.

## Connection to Bayesian family

- **LBE paper**: Opportunity frequency + preemption dynamics explain a constructional gap; operator membership remains an independent question
- **Varieties paper**: S/A/I conditioning → explains how operator repertoires vary by situation/ascription/identification
- **This paper**: Defines operator membership and its narrower response predictions

## Diagnostics Proposed

1. Paradigmatic closure (small enumerable sets)
2. Paradigm-level public-update contribution, tested independently through comprehension or uptake probes
3. Opportunity count and competitor strength as modulators of licensing concentration
4. Repair locus: update value, exponent, construction, or social stance
5. Cross-substance comparison with opportunity and frequency matched

## Predictions

1. Repair targets follow the error locus
2. Paradigm-level update contribution survives locally redundant tokens
3. Tonal, prosodic, gestural, and segmental operator values share matched response profiles
4. A closed, dense contrast with near-zero public-update contribution falsifies the boundary if it produces the same update-confusion profile as an operator

## Build

```bash
latexmk -xelatex operator-stratum.tex
```

Uses EB Garamond font, self-contained refs.bib via filecontents.
