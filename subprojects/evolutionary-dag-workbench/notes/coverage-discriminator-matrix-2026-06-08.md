# Coverage and Discriminator Matrix

**Date:** 2026-06-08
**Purpose:** summarize what the evaluated modules currently cover, where they partly survive, and
where they are explicitly out of scope.

No row below authorizes numeric score movement. The matrix is a decision aid for the next evaluation
round.

## Legend

- `S`: survives as a scoped module for this card.
- `P`: partly survives; useful structure is present but a named construct or mechanism is missing.
- `O`: fails as a general account or is explicitly out of scope.
- `.`: not yet evaluated against this module.

Module abbreviations:

- `DYN`: `context-indexed-dynamic-feedback-candidate`
- `OPG`: `context-aware-operator-gap-candidate`
- `CAT`: `category-measurement-discipline-candidate`
- `TASK`: `context-indexed-task-separated-feedback-candidate`
- `AUD`: `audience-reference-tracking-candidate`
- `SEL`: `selection-collocation-split-candidate`
- `PROC`: `processing-naturalness-perturbation-candidate`
- `UPT`: `uptake-operator-boundary-candidate`

## Matrix

| Phenomenon card | DYN | OPG | CAT | TASK | AUD | SEL | PROC | UPT |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `needs-washed` | S | . | . | . | . | . | . | . |
| `stigmatized-robust-vernacular` | S | . | . | . | P | . | . | . |
| `register-bound-fragments` | S | . | . | . | . | . | . | . |
| `singular-they` | P | . | . | . | P | . | . | . |
| `between-you-and-I` | P | . | . | S | . | . | . | . |
| `subject-verb-agreement-cgel` | P | P | . | P | . | . | . | . |
| `agreement-attraction` | O | P | . | O | . | . | P | . |
| `center-embedding` | O | P | . | O | . | . | S | . |
| `clause-type-force-cgel` | . | P | . | . | . | . | . | S |
| `interjection-boundary-source-card` | . | O | . | . | . | . | . | S |
| `frequent-condemned-form` | S | . | O | S | . | . | . | . |
| `left-branch-extraction` | O | P | . | . | . | . | . | . |
| `case-in-coordination-cgel` | P | . | . | S | . | . | . | . |
| `pronoun-personhood-proform-gender` | P | . | . | P | S | . | . | . |
| `nonfinite-verbless-clause-boundaries-cgel` | S | . | . | . | . | . | . | . |
| `negation-polarity-items-cgel` | O | . | . | . | . | . | . | . |
| `unbounded-dependency-licensing-cgel` | . | S | . | . | . | O | . | . |
| `fused-relative-constructions-cgel` | . | P | . | . | . | . | . | . |
| `fused-head-nps-cgel` | . | S | P | . | . | P | . | . |
| `preposition-category-selection-cgel` | . | P | . | . | . | S | . | . |
| `comparative-more-less-category` | . | O | S | . | . | P | . | . |
| `numerative-category-pressure` | . | . | P | . | . | . | . | . |
| `transparent-free-relatives` | . | P | . | . | . | . | . | . |
| `rare-uncontroversial-form` | . | S | . | . | . | . | . | . |
| `grammatical-but-hard` | . | P | . | . | . | . | S | . |

## Current Module Boundaries

`DYN` is the best module for context-indexed licensing, ideology, correction, production, reported
acceptability, attribution, register, and diachronic feedback. It should not absorb operator-gap
cases, polarity licensing, reference-tracking structure, or task/channel distinctions unless those
paths are explicitly added.

`OPG` is the best broad operator-gap module for recoverability, opportunity-normalized attestation,
preemption, repair pressure, and rare/transparent forms. It overreaches on preposition selection
unless the `SEL` split is added, and it is not a category-measurement account.

`CAT` is the category/measurement module. It handles category-assignment and function/classification
tasks without treating category labels as grammaticality. It is not a licensing, production, or
operator-gap module.

`TASK` is the production/judgment divergence module. It handles cases where unmonitored production,
school-correctness judgment, editing/correction, and later monitored production must be kept apart.
It is not a pronoun/reference module.

`AUD` is the pronoun/pro-form reference and audience-design module. It handles personhood
ascription, pronoun feature alignment, reference tracking, social-indexical value, audience design,
and attribution channels. It is not a diachronic stabilization module.

`SEL` is the preposition/complement-selection boundary module. It distinguishes payload preposition
choice, collocational rigidity, and argument-linking selection. It is not a general dependency-gap
module.

`PROC` is the processing/naturalness perturbation module. It handles processing cost, semantic
recoverability, felt naturalness, measurement task, reported acceptability, and attribution. It is
not a licensing, agreement-feature, or diachronic module.

`UPT` is the uptake/operator boundary module. It handles update-role configuration, repertoire
closedness, token innovability, operator-repertoire membership, stance, genre fit, repair, and
attribution. It is not a general operator-gap or social-indexical module.

## Discriminators Already Doing Work

- `left-branch-extraction`: separates `DYN` from `OPG`.
- `preposition-category-selection-cgel`: separates broad `OPG` from `SEL`.
- `pronoun-personhood-proform-gender`: separates `DYN`/`TASK` from `AUD`.
- `case-in-coordination-cgel`: separates `DYN` from `TASK`.
- `comparative-more-less-category`: separates `OPG` from `CAT`.
- `unbounded-dependency-licensing-cgel`: separates `OPG` from `SEL`.
- `subject-verb-agreement-cgel`: separates broad operator-value scaffolding from an
  agreement-specific feature/alignment mechanism.
- `agreement-attraction`: separates processing perturbation from context, task, and licensing
  modules.
- `center-embedding`: repeats the processing gap and justifies `PROC` as a scoped module.
- `interjection-boundary-source-card`: separates uptake configuration from operator-repertoire
  membership and justifies `UPT` as a scoped module.
- `clause-type-force-cgel`: shows that `OPG` can represent operator value but needs `UPT` for
  update-role/repertoire-boundary discipline.
- `frequent-condemned-form`: confirms that `DYN` and `TASK` already cover the
  frequency/condemnation split, while `CAT` is out of scope.
- `fused-head-nps-cgel`: confirms that `OPG` covers constructional analogy plus recoverability,
  while `CAT` and `SEL` cover only category/function and selection-adjacent pieces.

## Untested Cards

No phenomenon cards are completely untested in protocol-test evaluations.

## Next Evaluation Moves

1. Enrich thin source-backed cards with concrete examples, source pointers, and contrast cells.
2. Convert the strongest existing protocol-bound evaluations into explicit pass/fail prediction
   statements before any score movement.
3. Use held-out contrast cells to test whether `OPG`, `CAT`, and `SEL` remain complementary or
   require a fused-construction split.

## Working Decision

`clause-type-force-cgel` and `interjection-boundary-source-card` now show that broad operator-gap
machinery is not enough for uptake boundary cases. `uptake-operator-boundary-candidate` has been
added as a scoped module. `frequent-condemned-form` showed no new graph was needed: `DYN` and
`TASK` cover the production/condemnation split, while `CAT` remains out of scope.
`fused-head-nps-cgel` also does not justify a new graph yet: `OPG` covers the core
recoverability/constructional-support split, while `CAT` and `SEL` partly survive only on their
own narrower dimensions.
