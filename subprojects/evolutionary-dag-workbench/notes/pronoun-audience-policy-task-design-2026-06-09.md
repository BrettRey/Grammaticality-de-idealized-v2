# Pronoun Audience-Policy Task Design

**Date:** 2026-06-09
**Target mixed cells:** `audience-policy-framing-prediction`;
`pronoun-policy-framing-prediction`
**Primary graph under test:** `audience-reference-tracking-candidate`
**Comparison graph:** `context-indexed-dynamic-feedback-candidate`
**Purpose:** turn the pronoun/pro-form audience-policy pointer into an operational measurement
design.

## Question

Can audience, evaluator, or institutional framing shift reported acceptability, grammaticality
attribution, social sanction, or respect judgments while reference tracking remains constant?

The unresolved cell is not whether pro-form choice has personhood and reference-tracking structure.
The existing sources already support that. The unresolved cell is whether the audience-policy path
does measurable work independently of reference success and direct licensing.

## Source Lanes

### Lane A: CGEL Pronoun Sections

Local sources:

- `/Users/brettreynolds/Documents/CGEL/out/158_2 The personal pronouns.pdf`
- `/Users/brettreynolds/Documents/CGEL/out/057_17 Gender and pronounantecedent agreement 484.pdf`

Existing source facts:

- pronoun/pro-form choice is not reducible to formal antecedent matching;
- gender and personhood compatibility can depend on construed designatum, not only antecedent form;
- pronoun reference and agreement-like compatibility are separable from social evaluation.

Lane A supplies construct and contrast pressure. It does not by itself supply an audience-policy
measurement task.

### Lane B: Local Personhood/Pro-Forms Materials

Local sources:

- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Personhood_and_proforms/personhood+pro-forms.docx`
- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Personhood_and_proforms/reviews/`

Existing source facts:

- pro-form selection is designatum-sensitive;
- personal and non-personal pro-forms can become incoherent when mixed inside a single reference
  chain;
- dialect, identity, and reallocation questions are live reviewer pressure points.

Lane B supplies personhood, chain-coherence, dialect, and identity pressure. It does not yet supply
a controlled audience-policy dataset.

## Minimum Task Structure

Use paired items in which the target string is held constant while the frame changes. Each item
should be measured through separate prompts rather than one global acceptability question.

Core manipulations:

- `referent_status`: known human, unknown human, personified non-human, de-personified human,
  institution or collective;
- `pro_form_pattern`: feature-aligned, reference-recoverable but socially marked, chain-switched,
  ambiguous, or policy-specified;
- `audience_or_evaluator`: ordinary interlocutor, descriptive linguist, teacher/editor,
  institution/policy officer, target community member;
- `norm_centre`: descriptive usage, school-standard, institutional policy, community-local norm;
- `task_prompt`: reference resolution, naturalness, correctness, respect/social sanction,
  policy compliance, grammaticality attribution;
- `speaker_identity`: unmarked speaker, learner, institutional representative, in-group speaker,
  out-group speaker.

## Response Channels

Collect the channels separately:

| Channel | Workbench construct | Example response target |
|---|---|---|
| Reference identification | `reference_tracking_success` | Who does the pronoun refer to? How confident are you? |
| Feature/personhood fit | `pronoun_feature_alignment`, `personhood_ascription` | Does the pro-form fit the described referent? |
| Acceptability/naturalness | `reported_acceptability`, `felt_naturalness_context` | How acceptable or natural is this in the stated context? |
| Attribution | `grammaticality_attribution` | Is this a grammar error, a style issue, a respect issue, or none of these? |
| Social sanction | `metalinguistic_condemnation`, `social_indexical_value` | Would you correct, challenge, or avoid the form? Why? |
| Norm orientation | `standard_language_ideology`, `audience_design` | Which rule, audience, or institution are you orienting to? |

## Minimum Contrast Cells

### Cell 1: Low-Stakes Reference Baseline

The context supplies a clear antecedent and no policy or identity frame. The task asks for reference
resolution before any judgment prompt.

Expected result:

- feature alignment improves reference tracking and reported acceptability;
- audience/policy variables should have little independent effect;
- reference success should not directly entail community licensing.

### Cell 2: Stable Reference With Policy Frame

The target string and reference relation are held constant, but the evaluator/audience is varied
between ordinary interlocutor, school-standard correction, and institutional policy frame.

Expected result:

- reference tracking remains stable;
- reported acceptability, grammaticality attribution, social sanction, or respect/policy judgment
  shifts by audience or norm centre;
- social-indexical value and ideology mediate the shift rather than direct licensing.

### Cell 3: Reference-Failure Control

The pro-form makes reference genuinely unstable or ambiguous, independent of policy frame.

Expected result:

- reference tracking drops across audiences;
- audience or policy may change sanction, but should not rescue the reference path;
- this distinguishes reference failure from social disagreement about a recoverable pro-form.

### Cell 4: Personhood Reclassification

The same designatum is framed as personal, non-personal, institutional, intimate, or object-like.

Expected result:

- personhood ascription shifts pronoun feature alignment;
- the shift may affect reference success and acceptability;
- personhood ascription should not directly entail grammaticality attribution.

### Cell 5: Chain-Coherence Pressure

The same discourse chain either maintains one pro-form analysis or switches between personal and
non-personal construals without an explicit reclassification cue.

Expected result:

- unexplained chain switches should lower coherence and acceptability;
- explicit reclassification should improve acceptability without making the effect a simple
  antecedent-agreement rule.

## Candidate Prediction

`AUD` should pass only if it predicts:

- reference tracking can remain stable while audience/policy framing shifts acceptability,
  attribution, or social sanction;
- personhood ascription changes feature alignment without directly becoming grammaticality
  attribution;
- social-indexical value does not directly become community licensing;
- reference success does not directly become community licensing.

`AUD` should fail if it predicts:

- policy framing changes reference tracking without a feature or ambiguity manipulation;
- social sanction is treated as direct evidence of non-licensing;
- reference success is sufficient for licensing;
- all audience effects collapse into standard-language ideology.

`DYN` should partly survive if ideology and social-indexical value shift attribution, but it should
remain incomplete when reference tracking, personhood ascription, or pronoun feature alignment is
the measured channel.

## Status

This is a task design, not a data pass. The relevant prediction tests should remain `mixed` until a
dataset or elicitation run records channel-specific outcomes. No graph mutation or numeric score
movement follows.

## Data Scaffold

The design has been converted into data-ready files in `data/audience-reference-projection/`.
Those files define draft stimuli, response channels, prediction rows, and row-level coding fields.
They do not contain participant data and do not change any evidence labels.
