# Transparent-Relative Opportunity Measurement Design

**Date:** 2026-06-09
**Target mixed cell:** `transparent-rare-relative-prediction`
**Primary graph under test:** `context-aware-operator-gap-candidate`
**Purpose:** turn the rare transparent-relative data pointer into an operational measurement plan.

## Question

When does absence or rarity count against licensing for a transparent-relative-like construction?

The workbench needs to distinguish three cases:

- low raw frequency because the opportunity context is rare;
- probative absence after a checked opportunity denominator;
- attested but constrained licensing where genre, verb class, information structure, or competitor
  availability narrows the distribution.

## Source Lanes

### Lane A: Transparent Free Relatives

Local sources:

- `Transparent_free_relatives/two-kinds.tex`
- `Transparent_free_relatives/coca-data/README.md`
- `Transparent_free_relatives/coca-data/context-checks.txt`

Existing source facts:

- `call` plus adjective query: 619 raw COCA hits, with many genuine category-flexible transparent
  cases.
- `seem`/`appear` checked searches: zero genuine non-NP transparent cases across 474 examined
  results after context checks.
- The checked false positives split into pre-nominal modifiers inside NP nuclei and ordinary free
  relatives in NP function.

Operational variables:

- `verb_class`: attributional vs appearance/result-type;
- `raw_hit_count`;
- `checked_opportunity_count`;
- `genuine_transparent_count`;
- `false_positive_type`;
- `external_function`;
- `competitor_pattern_available`;
- `genre_or_register`.

### Lane B: Independent Relative `whose`

Local sources:

- `Independent_relative_whose_A_Bayesian_analysis_of_a_low-frequency_gap/main.tex`
- `Independent_relative_whose/items/all_items.csv`
- `Independent_relative_whose/items/README.md`

Existing source facts:

- The Bayesian note frames the contrast as high-opportunity absence vs low-opportunity uncertainty.
- The item table has 6 critical items crossed with `LicPlus`/`LicMinus`, 6 dependent-`whose`
  baselines, 12 good fillers, and 12 bad fillers.
- The design directly separates licensing context from the target string.

Operational variables:

- `licensing_context`: plus vs minus;
- `baseline_type`: dependent `whose`, simple genitive, or filler;
- `rating`;
- `speaker_variability`;
- `register_context`;
- `competitor_pattern_available`;
- `posterior_spread`.

## Measurement Rule

Do not compare raw rarity across constructions. Compare opportunity-normalized evidence:

```text
opportunity_normalized_attestation =
  genuine_transparent_count / checked_opportunity_count
```

and record the confidence state:

```text
if checked_opportunity_count is high and genuine_transparent_count is zero:
  absence is probative for that subtype
if checked_opportunity_count is low:
  absence remains weak evidence
if genuine_transparent_count is positive but restricted:
  licensing is scoped to the conditioning variables
```

This is not yet a universal threshold. It is a per-subtype evidence rule.

## Candidate Prediction

`OPG` should pass only if it predicts:

- raw frequency does not directly determine licensing;
- opportunity-normalized attestation can warrant licensing;
- high-opportunity checked absence can undercut licensing for a subtype;
- low-opportunity absence leaves uncertainty rather than categorical rejection;
- competitor availability strengthens preemption only inside a declared opportunity set.

`OPG` should fail if it predicts:

- any rare transparent construction is unlicensed by raw frequency alone;
- recoverability is sufficient for licensing;
- a single transparent-relative threshold applies before verb class, register, and competitor set
  are declared.

## Status

This design is ready for a data pass, but it is not itself a data pass. The current held-out
evaluation should remain `mixed` until at least one lane is run with checked denominators and
recorded outcomes.
