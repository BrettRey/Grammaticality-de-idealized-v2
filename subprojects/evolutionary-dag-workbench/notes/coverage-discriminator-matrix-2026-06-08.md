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
- `FRAME`: `frame-specific-dependency-licensing-candidate`
- `RNR`: `repair-neighbour-reconstruction-candidate`
- `INR`: `information-normalized-repair-candidate`

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
| `dependency-locality-alternations-gibson` | . | . | . | . | . | . | S | . |
| `garden-path-temporary-ambiguity-gibson` | . | . | . | . | . | . | S | . |
| `noisy-channel-overacceptance-gibson` | . | . | . | . | . | . | P | . |
| `island-construction-variation-gibson` | . | P | . | . | . | . | . | P |
| `legalese-center-embedding-gibson` | P | . | . | P | . | . | P | . |
| `frame-conditioned-duration-have` | . | P | . | . | . | . | . | S |

## Nineteenth-Pass Addendum

`FRAME` has been evaluated after the table above was created. It survives as a scoped module for:

- `frame-conditioned-duration-have`: `S`; it separates constructional/question-answer frame fit
  from recoverability and reported acceptability.
- `island-construction-variation-gibson`: `S`; it represents construction-specific dependency
  licensing without converting island effects into a global extraction ban.

## Twenty-First-Pass Addendum

`RNR` has been evaluated after the table above was created. It survives
`noisy-channel-overacceptance-gibson` as a one-card reconstruction module, but it is unscored and
has no `scoped_module` label. The key contrast is repair-neighbour distance, not general
recoverability.

## Twenty-Second-Pass Addendum

Four sharper noisy-channel subtype cards have been added from Gibson:

- `missing-verb-phrase-illusion-gibson`: `RNR` = `S`; close omitted-material repair is the clean
  case for repair-neighbour distance.
- `depth-charge-semantic-illusion-gibson`: `RNR` = `P`; reconstruction is represented, but a
  meaning-prior or intended-meaning-plausibility construct is missing.
- `comparative-illusion-noisy-channel-gibson`: `RNR` = `P`; repair-neighbour reconstruction is
  represented, but category/function analysis still belongs with `CAT`.
- `edit-distance-acceptability-gibson`: `RNR` = `P`; repair distance is represented, but the graph
  lacks length or information-mass normalization.

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

`FRAME` is the frame-specific dependency-licensing module. It handles question-answer frame fit and
construction-specific dependency licensing. It is not a general operator-gap, opportunity/preemption,
or processing account.

`RNR` is the repair-neighbour reconstruction candidate. It handles noisy-channel overacceptance
where a nearby intended repair inflates first-pass reported acceptability. It is not yet a scoped
module.

`INR` is the information-normalized repair candidate. It handles noisy-channel cases where raw
repair distance must be interpreted against target sentence length or information mass. It is not
yet a scoped module.

## Twenty-Third-Pass Addendum

`INR` has been evaluated after the table above was created:

- `edit-distance-acceptability-gibson`: `INR` = `S`; raw repair distance and target information mass
  jointly predict acceptability.
- `missing-verb-phrase-illusion-gibson`: `INR` = `S`; the close-repair path is preserved through
  normalized distance.

`INR` remains unscored and has no `scoped_module` label until tested against depth-charge and
comparative-illusion cases.

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
- `dependency-locality-alternations-gibson`: strengthens `PROC` as a licensed-but-less-natural
  alternation module.
- `garden-path-temporary-ambiguity-gibson`: strengthens `PROC` by adding first-pass illusion of
  ungrammaticality.
- `noisy-channel-overacceptance-gibson`: pressures `PROC` toward an intended-form-distance
  construct because recoverability alone is too coarse.
- `noisy-channel-overacceptance-gibson`: now justifies `RNR` as an unscored one-card candidate, but
  not as a scoped module.
- `island-construction-variation-gibson`: separates `OPG`'s opportunity/preemption machinery from
  `UPT`'s construction-specific update-role machinery.
- `legalese-center-embedding-gibson`: separates `DYN`/`TASK` genre and production persistence from
  the missing processing/comprehension mechanism.
- `legalese-center-embedding-gibson`: now also shows that `PROC` covers the processing,
  naturalness, comprehension, and preference side without explaining genre persistence.
- `frame-conditioned-duration-have`: separates `UPT`'s question-answer frame fit from `OPG`'s
  broader recoverability/licensing separation.
- `frame-conditioned-duration-have` and `island-construction-variation-gibson`: justify `FRAME` as
  a scoped module when the needed contrast is finer than broad update-role configuration or broad
  operator value.

## Untested Cards

No phenomenon cards are completely untested in protocol-test evaluations.

Newly exposed untested pairings remain:

- depth-charge and comparative-illusion cards against `INR`, to test whether normalization helps or
  whether meaning-prior and category-analysis modules are still needed.
- comparative-illusion cards against `CAT`, to test whether category-analysis divergence remains
  separable from repair-neighbour reconstruction.
- richer island and dependency cards against `FRAME`, to test whether the new module stays scoped
  or overfits the first Gibson island card.

## Next Evaluation Moves

1. Add data pointers for unresolved prediction-test cells: pronoun policy/audience design and rare
   transparent-relative opportunity thresholds.
2. Use held-out contrast cells to test whether `OPG`, `CAT`, and `SEL` remain complementary or
   require a fused-construction split.
3. Test whether `INR` handles depth-charge and comparative-illusion cards or remains limited to
   edit-distance and missing-material cases.
4. Add richer island and dependency cards against `FRAME` before any numeric movement or broader
   dependency claim.

## Working Decision

`clause-type-force-cgel` and `interjection-boundary-source-card` now show that broad operator-gap
machinery is not enough for uptake boundary cases. `uptake-operator-boundary-candidate` has been
added as a scoped module. `frequent-condemned-form` showed no new graph was needed: `DYN` and
`TASK` cover the production/condemnation split, while `CAT` remains out of scope.
`fused-head-nps-cgel` also does not justify a new graph yet: `OPG` covers the core
recoverability/constructional-support split, while `CAT` and `SEL` partly survive only on their
own narrower dimensions.
The Gibson/local-card pass does not justify a new graph yet. It strengthens `PROC` and `UPT`, and
it exposes three named pressure points: intended-form distance, construction-specific dependency
licensing, and legalese as a genre-processing hybrid.
The nineteenth pass resolves one of those pressure points by adding
`frame-specific-dependency-licensing-candidate`. It leaves intended-form distance and
legalese/processing interaction as live pressure points.
The twentieth pass resolves legalese/processing interaction without a new graph: `PROC` covers the
processing side, while `DYN` and `TASK` cover genre persistence and production/judgment separation.
The twenty-first pass resolves the intended-form-distance pressure by adding
`repair-neighbour-reconstruction-candidate`, while keeping it unscored until it survives more than
one noisy-channel contrast family.
The twenty-second pass shows that `RNR` survives the close-repair subtype but is too coarse for
depth-charge, comparative-illusion, and edit-distance/length effects.
The twenty-third pass adds `information-normalized-repair-candidate`, resolving the
edit-distance/length pressure while leaving meaning-prior and category-sensitive noisy-channel cases
open.
