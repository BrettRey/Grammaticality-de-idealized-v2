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
- `MPR`: `meaning-prior-reconstruction-candidate`
- `AGR`: `agreement-controller-override-candidate`
- `TEMP`: `temporal-anchor-alignment-candidate`

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

`MPR` is the meaning-prior reconstruction candidate. It handles semantic noisy-channel cases where a
plausible intended meaning diverges from literal compositional coherence. It is not yet a scoped
module.

`AGR` is the agreement-controller/override candidate. It handles controller identification, feature
alignment, licensed override, notional agreement basis, and retrieval-attractor salience. It is a
scoped agreement module, not a category-analysis, pronoun/audience, diachronic, or general
grammaticality account.

`TEMP` is the temporal-anchor alignment candidate. It handles tense/aspect anchoring, modal
temporal inference, definite or by-now temporal anchors, current relevance, continuative intervals,
experiential frames, and narrative perspective. It is built from the current temporal cards and is
not a scoped module yet.

## Twenty-Third-Pass Addendum

`INR` has been evaluated after the table above was created:

- `edit-distance-acceptability-gibson`: `INR` = `S`; raw repair distance and target information mass
  jointly predict acceptability.
- `missing-verb-phrase-illusion-gibson`: `INR` = `S`; the close-repair path is preserved through
  normalized distance.

`INR` remains unscored and has no `scoped_module` label until tested against depth-charge and
comparative-illusion cases.

## Twenty-Fourth-Pass Addendum

`INR` has now been tested against the harder noisy-channel subtype cards:

- `depth-charge-semantic-illusion-gibson`: `INR` = `P`; normalized repair helps, but a meaning-prior
  or intended-meaning-plausibility construct is missing.
- `comparative-illusion-noisy-channel-gibson`: `INR` = `P`; normalized repair helps, but category
  analysis remains a `CAT` problem.

This blocks promotion of `INR`.

## Twenty-Fifth-Pass Addendum

`MPR` has been evaluated after the table above was created:

- `depth-charge-semantic-illusion-gibson`: `MPR` = `S`; intended-meaning plausibility and literal
  composition coherence are now separated.
- `comparative-illusion-noisy-channel-gibson`: `MPR` = `P`; meaning-prior reconstruction helps, but
  category/function analysis remains a `CAT` problem.

`MPR` remains unscored and has no `scoped_module` label.

## Twenty-Sixth-Pass Addendum

Three local minimal-pair cards have been added and evaluated:

- `perfect-definite-past-time`: `FRAME` = `P`; frame fit and recoverability are separated,
  but a temporal-anchor or tense/aspect alignment construct is still missing.
- `nearest-noun-agreement-attraction`: `PROC` = `P`; processing/naturalness perturbation is
  represented, but agreement-controller and retrieval-attractor machinery is still missing.
- `attitude-complement-selection`: `SEL` = `S`; complement-type choice patterns as
  argument-linking selection rather than payload choice or raw collocation.

No graph mutation or score movement follows from this pass.

## Twenty-Seventh-Pass Addendum

One local cohort-conditioned complement-selection card has been added:

- `allowed-to-doing-cohort-contrast`: `SEL` = `P`; complement selection is represented, but the
  adult/children contrast requires speaker/cohort identity, production probability, and diachronic
  stabilization machinery that `SEL` intentionally lacks.

No graph mutation or score movement follows from this pass.

## Twenty-Eighth-Pass Addendum

Four source-backed CGEL cards have been added and evaluated:

- `continuative-perfect-since-cgel`: `FRAME` = `P`; frame fit and recoverability are separated,
  but temporal-anchor or tense/aspect-alignment machinery is still missing.
- `catenative-complement-form-selection-cgel`: `SEL` = `P`; complement selection is represented,
  but catenative form-type subclasses are still missing.
- `proximity-agreement-error-cgel`: `PROC` = `P`; processing/naturalness perturbation is
  represented, but agreement-controller and retrieval-attractor machinery is still missing.
- `collective-number-transparent-agreement-cgel`: `OPG` = `P`; agreement is represented only as
  broad operator value, not as simple agreement vs licensed override vs proximity error.

No graph mutation or score movement follows from this pass.

## Twenty-Ninth-Pass Addendum

Three more source-backed CGEL discriminator cards have been added and evaluated:

- `perfect-already-yesterday-cgel`: `FRAME` = `P`; frame fit separates the bare present-perfect
  mismatch from the restricted `already` case, but the graph still lacks a temporal-anchor/current
  relevance construct.
- `allow-prevent-complement-selection-cgel`: `SEL` = `P`; selection is represented, but the graph
  lacks catenative verb-class subtype and cohort-stabilization machinery.
- `coordination-agreement-resolution-cgel`: `OPG` = `P`; broad operator-value and processing
  channels are represented, but agreement-controller identification and override-pattern licensing
  are missing.

The coordination card crosses the mutation threshold for a narrow agreement module. Added
`agreement-controller-override-candidate`; it survives the built-on agreement cards in a
protocol-bound no-score-change evaluation, but it has no `scoped_module` label or projective credit.

## Thirtieth-Pass Addendum

One held-out agreement card has been added and evaluated:

- `measure-agreement-override-cgel`: `AGR` = `S`; a formally plural measure NP can license singular
  agreement under single-measure construal, and the new agreement candidate routes the case through
  notional basis, controller identification, override pattern, and feature alignment.

This is the first projective check for `agreement-controller-override-candidate`. It supports the
candidate as a real agreement module but does not authorize score movement or a `scoped_module`
label yet, because it is one held-out subtype from the same CGEL chapter.

## Thirty-First-Pass Addendum

One additional held-out agreement card has been added and evaluated:

- `fused-determiner-head-agreement-cgel`: `AGR` = `S`; fused determiner-head agreement varies with
  non-count singular construal, plural-set construal, and formal-style pressure, and the agreement
  candidate survives without adding nodes.

Created `agreement-controller-override-heldout-scope-2026-06-09`, a held-out `scope-only`
evaluation combining the measure and fused determiner-head cards. `agreement-controller-override-candidate`
now has a `scoped_module` label. All numeric scores remain zero.

## Thirty-Fourth-Pass Addendum

One measurement-validity card has been added and evaluated:

- `ann-brain-lexical-semantic-predictivity`: `PROC` = `P`, `CAT` = `P`, `OPG` = `O`. The Kauf et
  al. ANN/fMRI result is useful evidence about a measurement channel, not direct evidence about
  grammatical licensing, syntactic structure, or operator gaps.

No graph mutation follows. The card's main value is to block inference from ANN-to-brain
predictivity to grammar-facing constructs unless a graph explicitly represents the measurement
channel and a grammar-relevant contrast cell.

## Thirty-Fifth-Pass Addendum

Lane A of the transparent-relative opportunity-denominator design has been run against local
transparent-free-relative sources:

- `fused-relative-constructions-cgel`: the `OPG` held-out prediction
  `transparent-rare-relative-prediction` moves from `mixed` to `passed` for this source lane.
  Attributional `call`-type contexts have sampled positive scoped attestation, while `seem`/`appear`
  AP-transparent contexts show checked zero genuine cases over a meaningful opportunity
  denominator.

No graph mutation or numeric score movement follows. The independent-relative-`whose` lane remains
unrun.

## Thirty-Sixth-Pass Addendum

The remaining pronoun/audience mixed cell has been converted into a task design:

- `pronoun-personhood-proform-gender`: `AUD` remains `S` as a scoped module, but
  `audience-policy-framing-prediction` remains `mixed` until actual task outcomes exist. The new
  design specifies how to vary audience, evaluator, institution, norm centre, speaker/referent cue,
  and judgment prompt while separately measuring reference tracking, acceptability, attribution,
  and social sanction.

No graph mutation or numeric score movement follows.

## Thirty-Seventh-Pass Addendum

The independent-relative-`whose` lane has been recorded as a design/simulation lane:

- `fused-relative-constructions-cgel`: Lane B supports `OPG`'s low-opportunity discipline at the
  design level. The materials explicitly manipulate licensing context, include dependent-`whose`
  baselines and fillers, and contain LLM/simulation outputs. They do not supply human or corpus
  evidence, so no additional score movement or evidence-status change follows.

No graph mutation follows.

## Thirty-Eighth-Pass Addendum

`CAT` has now been evaluated against the comparative-illusion noisy-channel card:

- `comparative-illusion-noisy-channel-gibson`: `CAT` = `P`; it represents category-analysis and
  measurement-task leakage, but intentionally leaves repair-neighbour distance, normalized repair,
  and intended-meaning priors to the noisy-channel modules.

No graph mutation or score movement follows.

## Thirty-Ninth-Pass Addendum

`TEMP` has been added after repeated temporal-anchor pressure crossed the mutation threshold:

- `perfect-definite-past-time`: `TEMP` = `S`; temporal-anchor fit separates the
  present-perfect-plus-definite-past mismatch from recoverable event meaning.
- `continuative-perfect-since-cgel`: `TEMP` = `S`; continuative interval relation feeds
  temporal-anchor fit for the present-perfect-plus-since frame.
- `perfect-already-yesterday-cgel`: `TEMP` = `S`; experiential relevance can change the fit of
  `already` plus `yesterday` without licensing all present-perfect-plus-definite-past expressions.
- `narrative-present-past-time-frame`: `TEMP` = `S`; narrative perspective keeps past story time
  distinct from present-tense viewpoint.
- `modal-perfect-by-now-inference`: `TEMP` = `S`; modal temporal inference licenses `will` plus
  perfect with `by now` without treating English `will` as future tense.

`TEMP` remains unscored and has no `scoped_module` label because all five cards were used to shape
the mutation.

## Fortieth-Pass Addendum

`AGR` has now been run against a consolidated number-construal/realization bundle:

- `collective-number-transparent-agreement-cgel`: `AGR` = `S`; notional basis and override pattern
  separate collective/member and number-transparent construals from simple head matching.
- `coordination-agreement-resolution-cgel`: `AGR` = `S`; controller identification and notional
  basis distinguish ordinary plural, unit singular, one-participant, distributive, and mixed-number
  cases.
- `measure-agreement-override-cgel`: `AGR` = `S`; single-measure construal licenses singular
  realization despite formal plurality.
- `fused-determiner-head-agreement-cgel`: `AGR` = `S`; fused-head construal and formal-style
  pressure remain separate paths.
- `proximity-agreement-error-cgel`: `AGR` = `S`; nearest-NP effects remain processing/attribution
  perturbations, not licensing paths.

No mutation follows. The current `AGR` graph already has the needed separation among notional
basis, controller identification, override pattern, feature alignment, and retrieval-attractor
salience.

## Forty-First-Pass Addendum

`TEMP` has now been tested against a held-out modal-preterite card:

- `modal-preterite-remoteness-cgel`: `TEMP` = `P`; it avoids treating preterite form as simple
  past-time anchoring, but it lacks a modal-remoteness or remote-conditional frame construct.

This blocks a `scoped_module` label for `TEMP`. A second held-out modal/conditional card is needed
before mutating the graph.

## Forty-Second-Pass Addendum

`TEMP` has now been tested against a second held-out preterite-orientation card:

- `backshifted-preterite-orientation-cgel`: `TEMP` = `P`; it avoids treating backshifted preterite
  as ordinary deictic past time, but it lacks a temporal-orientation frame for matrix/report-supplied
  orientation.

Together with `modal-preterite-remoteness-cgel`, this justifies a future `TEMP` mutation. The repair
should be broader than a modal-remoteness-only node: the needed construct is temporal orientation
source.

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
- `ann-brain-lexical-semantic-predictivity`: separates measurement-channel sensitivity from
  grammatical licensing, keeping `PROC` and `CAT` partial while blocking `OPG` overreach.
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
- `perfect-definite-past-time`: now separates `FRAME`'s broad frame fit from `TEMP`'s
  temporal-anchor fit.
- `nearest-noun-agreement-attraction`: repeats the agreement-controller/retrieval gap left by the
  broader agreement cards and keeps `PROC` scoped to processing perturbation.
- `attitude-complement-selection`: strengthens `SEL` as the complement-selection boundary module
  and sets up a future comparison with `FRAME` and `UPT`.
- `allowed-to-doing-cohort-contrast`: separates complement-selection structure from
  cohort-conditioned licensing and adult correction frames.
- `continuative-perfect-since-cgel`: repeats the temporal-anchor pressure exposed by
  `perfect-definite-past-time` and now supports `TEMP`.
- `catenative-complement-form-selection-cgel`: repeats the complement-selection subtype pressure
  exposed by `allowed-to-doing-cohort-contrast` and `attitude-complement-selection`.
- `proximity-agreement-error-cgel` and `collective-number-transparent-agreement-cgel`: split
  agreement processing errors from licensed agreement overrides.
- `perfect-already-yesterday-cgel`: blocks a blanket present-perfect-plus-past-time rule and
  sharpens the difference between broad `FRAME` and narrow `TEMP`.
- `narrative-present-past-time-frame`: prevents `TEMP` from overgeneralizing a ban on present
  morphology with past-time expressions.
- `modal-perfect-by-now-inference`: prevents `TEMP` from treating English `will` as future tense
  and forces a modal temporal inference frame.
- `modal-preterite-remoteness-cgel`: first held-out pressure on `TEMP`; it separates preterite form
  from past-time anchoring and exposes the missing modal-remoteness frame.
- `backshifted-preterite-orientation-cgel`: second held-out pressure on `TEMP`; it shows the missing
  construct is temporal orientation source, not modal remoteness alone.
- `allow-prevent-complement-selection-cgel`: separates catenative class structure from local
  cohort-conditioned `allowed doing` production.
- `coordination-agreement-resolution-cgel`: forces agreement-controller and override constructs,
  triggering `agreement-controller-override-candidate`.
- `measure-agreement-override-cgel`: first held-out support for
  `agreement-controller-override-candidate`; it tests a new override direction rather than another
  build-card subtype.
- `fused-determiner-head-agreement-cgel`: second held-out support for `AGR`; it keeps fused-head
  category analysis separate from the agreement-controller path.
- `fused-relative-constructions-cgel`: now gives a passed Lane A opportunity-denominator test for
  `OPG`, separating raw rarity from checked subtype-conditioned absence.
- `pronoun-personhood-proform-gender`: now has a runnable audience-policy task design, but the
  mixed prediction cell is deliberately unchanged until channel-specific data exist.
- `fused-relative-constructions-cgel`: now has both Lane A checked opportunity evidence and Lane B
  experiment-ready independent-relative-`whose` materials, with only Lane A counting as evidence.
- `comparative-illusion-noisy-channel-gibson`: now keeps `CAT`, `INR`, and `MPR` complementary
  rather than forcing a fused category/noisy-channel graph.

## Untested Cards

No phenomenon cards are completely untested in protocol-test evaluations.

Newly exposed untested pairings remain:

- comparative-illusion cards against `CAT`, to test whether category-analysis divergence remains
  separable from repair-neighbour reconstruction.
- comparative-illusion cards against combined `CAT` plus noisy-channel candidates, to test whether
  the category/reconstruction interaction can be represented without merging constructs.
- richer island and dependency cards against `FRAME`, to test whether the new module stays scoped
  or overfits the first Gibson island card.

## Next Evaluation Moves

1. Run the pronoun policy/audience task or independent-relative-`whose` human judgment task if data
   collection is available.
2. Pause agreement growth unless a genuinely different source domain is available; the consolidated
   number-construal pass did not force mutation.
3. Mutate `TEMP` with a temporal-orientation frame if continuing the temporal lane; keep the new
   construct distinct from modal inference and English future-tense analysis.
4. Use held-out contrast cells to test whether `OPG`, `CAT`, and `SEL` remain complementary or
   require a fused-construction split.
5. Test comparative-illusion cards against a combined category/noisy-channel interpretation only if
   a future card forces the interaction.
6. Add richer island and dependency cards against `FRAME` before any numeric movement or broader
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
The twenty-fourth pass confirms that INR remains partial on depth-charge and comparative-illusion
cards; those should not be folded into repair-distance normalization.
The twenty-fifth pass adds `meaning-prior-reconstruction-candidate`, resolving the depth-charge
pressure while leaving comparative category/reconstruction interaction open.
The twenty-sixth pass adds three local operator-contrast cards. It records two partial survivals
without mutation (`FRAME` for perfect-plus-definite-past anchoring, `PROC` for nearest-noun
agreement attraction) and one scoped survival (`SEL` for attitude complement selection).
The twenty-seventh pass adds the `allowed to do` / `allowed doing` cohort contrast. It partly
survives `SEL`, exposing the need to keep complement-selection structure separate from
speaker/cohort and diachronic licensing channels.
The twenty-eighth pass adds a targeted CGEL discriminator pack. All four new source-backed cards
partly survive their target modules, strengthening pressure for temporal-anchor,
catenative-complement, and agreement-controller constructs without yet justifying mutation.
The twenty-ninth pass adds one more card in each repeated pressure zone. Temporal-anchor and
catenative-subtype pressure remain unresolved without mutation. Agreement pressure crosses the
mutation threshold, yielding `agreement-controller-override-candidate`; because it is built from the
current agreement cards, it has no held-out projective credit, scoped label, or numeric score.
The thirtieth pass adds a held-out measure-agreement override card. The agreement candidate survives
without adding nodes, which is projective evidence for the module. It remains unscored and unlabeled
until at least one more held-out agreement subtype is tested.
The thirty-first pass adds a second held-out agreement subtype, fused determiner-head agreement.
Together with the measure override card, it authorizes a `scope-only` evaluation and a scoped label
for `agreement-controller-override-candidate`. Numeric scores remain zero.
The thirty-fifth pass resolves Lane A of the transparent-relative opportunity threshold question:
`OPG` passes the checked attributional-vs-`seem`/`appear` subtype contrast without score movement,
while the independent-relative-`whose` lane remains open.
The thirty-sixth pass resolves the pronoun/audience bookkeeping gap into a runnable task design, but
keeps the evidence status `mixed` until data exist.
The thirty-seventh pass records the independent-relative-`whose` materials as a design/simulation
lane, preserving the distinction between measurement readiness and human evidence.
The thirty-eighth pass keeps comparative illusions split across complementary modules: category
analysis belongs with `CAT`, repair distance with `INR`/`RNR`, and intended meaning with `MPR`.
The thirty-ninth pass resolves the repeated temporal-anchor pressure by adding
`temporal-anchor-alignment-candidate`. It survives the built-on perfect, narrative-present, and
modal-perfect-by-now cards, but it has no scoped label or score until a held-out temporal/modal card
tests whether the anchor-fit machinery projects.
The fortieth pass consolidates number construal/realization under `AGR` without mutation:
notional basis, controller identification, override pattern, feature alignment, and attractor
salience remain sufficient for the current agreement bundle.
The forty-first pass gives `TEMP` its first held-out test. It partly survives
`modal-preterite-remoteness-cgel`, but the missing modal-remoteness frame blocks scoped-module
promotion and leaves mutation pending a second modal/conditional card.
The forty-second pass adds that second pressure point. Backshifted preterite partly survives but
shows the repair should be a temporal-orientation frame rather than a modal-remoteness-only node.
