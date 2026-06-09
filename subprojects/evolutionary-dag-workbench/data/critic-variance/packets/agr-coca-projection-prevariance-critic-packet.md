# Critic Verdict Variance Packet

You are one independent critic pass for the evolutionary DAG workbench.

Your job is not to improve the graph first. Your job is to decide whether the
existing evaluation verdicts are stable under adversarial reading.

Use only the packet contents. Do not assume outside facts.

Return JSON only, matching this shape:

```json
{
  "critic_id": "short identifier you choose",
  "target_evaluation": "evaluation id",
  "overall_score_decision": "no-score-change | scope-only | score-change-proposed",
  "overall_stability": "stable | unstable | underdetermined",
  "prediction_test_verdicts": [
    {
      "id": "prediction test id",
      "evidence_status": "passed | failed | mixed | inconclusive | not-run",
      "confidence": 0.0,
      "reason": "one sentence"
    }
  ],
  "card_result_verdicts": [
    {
      "phenomenon": "card id",
      "result": "survives_as_module | partly_survives | fails | fails_general_out_of_scope | exploratory",
      "confidence": 0.0,
      "reason": "one sentence"
    }
  ],
  "strongest_instability": "one sentence",
  "score_movement_allowed": false,
  "minimal_change": "one sentence"
}
```

Important: do not award numeric score movement unless the packet itself contains
enough evidence to justify it under the workbench scoring policy.

## Target Evaluation JSON

```json
{
  "id": "agreement-controller-override-coca-projection-2026-06-09",
  "target_graph": "graphs/archive/agreement-controller-override-candidate.json",
  "protocol": "notes/agreement-coca-projection-protocol-2026-06-09.md",
  "status": "protocol-bound",
  "score_decision": "no-score-change",
  "activated_paths": [
    {
      "id": "notional-basis-to-production",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "bunch-animate-plural-dominant",
      "expected_path_reading": "indeterminate",
      "prediction": "Animate plural-member construal should provide contextual warrant for controller identification, agreement alignment, licensing, and higher production probability of plural agreement.",
      "edges": [
        {
          "source": "notional_agreement_basis",
          "target": "agreement_controller_identification",
          "type": "evidential"
        },
        {
          "source": "agreement_controller_identification",
          "target": "agreement_feature_alignment",
          "type": "constitutive"
        },
        {
          "source": "agreement_feature_alignment",
          "target": "community_licensing",
          "type": "constitutive"
        },
        {
          "source": "community_licensing",
          "target": "production_probability",
          "type": "causal"
        }
      ]
    },
    {
      "id": "inanimate-bunch-contrast",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "bunch-inanimate-sparse-contrast",
      "expected_path_reading": "indeterminate",
      "prediction": "If animacy/member construal matters, inanimate `bunch` cells should not simply reproduce the animate plural-dominant profile.",
      "edges": [
        {
          "source": "notional_agreement_basis",
          "target": "agreement_controller_identification",
          "type": "evidential"
        },
        {
          "source": "agreement_controller_identification",
          "target": "agreement_feature_alignment",
          "type": "constitutive"
        },
        {
          "source": "agreement_feature_alignment",
          "target": "community_licensing",
          "type": "constitutive"
        },
        {
          "source": "community_licensing",
          "target": "production_probability",
          "type": "causal"
        }
      ]
    },
    {
      "id": "majority-controller-to-production",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "majority-plural-dominant",
      "expected_path_reading": "non_sign_propagating",
      "prediction": "For `majority` with plural human complements, controller identification and agreement alignment should route to licensing and production probability in the plural direction, not collapse to surface singular head number.",
      "edges": [
        {
          "source": "agreement_controller_identification",
          "target": "agreement_feature_alignment",
          "type": "constitutive"
        },
        {
          "source": "agreement_feature_alignment",
          "target": "community_licensing",
          "type": "constitutive"
        },
        {
          "source": "community_licensing",
          "target": "production_probability",
          "type": "causal"
        }
      ]
    },
    {
      "id": "partitive-qn-controller-to-production",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "partitive-qn-people-plural-dominant",
      "expected_path_reading": "non_sign_propagating",
      "prediction": "For usable `lots/plenty/rest` people frames, controller identification and agreement alignment should route to plural production probability rather than singular surface-head agreement.",
      "edges": [
        {
          "source": "agreement_controller_identification",
          "target": "agreement_feature_alignment",
          "type": "constitutive"
        },
        {
          "source": "agreement_feature_alignment",
          "target": "community_licensing",
          "type": "constitutive"
        },
        {
          "source": "community_licensing",
          "target": "production_probability",
          "type": "causal"
        }
      ]
    },
    {
      "id": "minority-controller-to-production",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "minority-zero-cell",
      "expected_path_reading": "non_sign_propagating",
      "prediction": "The same controller/alignment/production route would be needed for `minority`, but the registered direct-query cells returned no raw rows.",
      "edges": [
        {
          "source": "agreement_controller_identification",
          "target": "agreement_feature_alignment",
          "type": "constitutive"
        },
        {
          "source": "agreement_feature_alignment",
          "target": "community_licensing",
          "type": "constitutive"
        },
        {
          "source": "community_licensing",
          "target": "production_probability",
          "type": "causal"
        }
      ]
    }
  ],
  "prediction_tests": [
    {
      "id": "bunch-animate-coca-projection",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "bunch-animate-plural-dominant",
      "activated_paths": [
        "notional-basis-to-production"
      ],
      "prediction": "Filtered COCA rows for `a bunch of people/kids` should be strongly plural-dominant if animate member construal supplies the controller basis.",
      "pass_condition": "KWIC-filtered target plural rows substantially outnumber target singular rows, and counter-direction singular raw hits mostly disappear under row coding.",
      "fail_condition": "The prediction fails if target singular rows remain common after KWIC filtering or if plural dominance is only a raw-query artifact.",
      "evidence_status": "passed",
      "evidence_note": "Filtered counts from `data/agr-coca-projection/summary.csv`: animate `bunch` has 71 target plural rows and 1 target singular row; five of six raw singular hits were non-subject false positives."
    },
    {
      "id": "bunch-inanimate-coca-contrast",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "bunch-inanimate-sparse-contrast",
      "activated_paths": [
        "inanimate-bunch-contrast"
      ],
      "prediction": "Inanimate `bunch` should differ from the animate profile, or else the animate result may be a generic `bunch` query-template effect.",
      "pass_condition": "The inanimate cells are sparse or non-plural-dominant after KWIC filtering, contrasting with the animate profile.",
      "fail_condition": "The contrast fails if inanimate cells reproduce the same plural-dominant profile at comparable density without a separate conditioning explanation.",
      "evidence_status": "mixed",
      "evidence_note": "Filtered counts are 1 target plural row and 1 target singular row. This contrasts with animate `bunch`, but the sparse denominator prevents a stable inanimate profile estimate."
    },
    {
      "id": "majority-coca-portability",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "majority-plural-dominant",
      "activated_paths": [
        "majority-controller-to-production"
      ],
      "prediction": "The agreement-controller module should generalize beyond `bunch`: `a/the majority of people` should show plural agreement dominance after KWIC filtering.",
      "pass_condition": "KWIC-filtered majority cells show target plural agreement while raw singular hits are zero or filtered out as non-target/nonstandard rows.",
      "fail_condition": "The portability claim fails if majority cells require constructs absent from `AGR`, or if surface singular head number predicts the filtered data as well as the controller/alignment bundle.",
      "evidence_status": "passed",
      "evidence_note": "Filtered counts from `data/agr-coca-projection/summary.csv`: majority/minority tranche has 105 target plural rows and 0 target singular rows. Positive evidence comes from majority cells; both registered minority cells returned zero raw rows."
    },
    {
      "id": "majority-denominator-omission-audit",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "majority-plural-dominant",
      "activated_paths": [
        "majority-controller-to-production"
      ],
      "prediction": "If the `majority` result is not a direct-string artifact, a denominator sample for `the majority of people` should not reveal omitted singular-agreement opportunities that reverse the plural-dominant direction.",
      "pass_condition": "The audit passes if false-positive pressure is low in exact rows and omitted agreement-bearing opportunities in a bounded denominator sample are plural-dominant rather than singular-dominant.",
      "fail_condition": "The audit fails if omitted singular-agreement opportunities are common enough to make the direct `are/is` result misleading.",
      "evidence_status": "passed",
      "evidence_note": "Measurement audit from `notes/agr-coca-measurement-audit-2026-06-09.md`: exact `majority` rows have 105 target rows, 1 denominator-only row, and 4 excluded false positives. A 98-row denominator sample for `the majority of people` found 37 omitted plural-agreement rows and 0 omitted singular-agreement rows."
    },
    {
      "id": "partitive-qn-coca-targeted-kwic",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "partitive-qn-people-plural-dominant",
      "activated_paths": [
        "partitive-qn-controller-to-production"
      ],
      "prediction": "Partitive/QN people frames should show plural agreement dominance after KWIC filtering, with counter-direction singular raw hits disappearing or being coded as non-target/nonstandard rows.",
      "pass_condition": "The test passes only when the registered positive and counter-direction cells are KWIC-filtered enough to show target plural dominance over licensed target singular agreement.",
      "fail_condition": "The portability claim fails if the singular cells yield licensed target rows at comparable density, or if plural dominance is only a raw-query artifact.",
      "evidence_status": "passed",
      "evidence_note": "Targeted KWIC/sample evidence from `data/agr-coca-projection/summary.csv`: `lots of people is` has 0 licensed target singular rows; `lots of people are` has a pre-declared 100-row bounded KWIC sample with 100 target plural rows; the additional filtered positive subset has 63 `plenty of people are` rows and 14 `the rest of the people are` rows. The `lots` positive cell is sample-coded rather than fully filtered, so this remains evidence-trail movement only, not score movement."
    },
    {
      "id": "minority-coca-uninformative",
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "contrast_cell": "minority-zero-cell",
      "activated_paths": [
        "minority-controller-to-production"
      ],
      "prediction": "`minority` cells should eventually test whether the majority result extends across the pair, but the registered direct strings may be too sparse.",
      "pass_condition": "The cells are informative only if COCA yields enough target rows to compare agreement direction.",
      "fail_condition": "This does not fail the graph; it fails the query cell as a useful projection test if both registered strings are raw zero.",
      "evidence_status": "inconclusive",
      "evidence_note": "Both `a minority of voters are` and `a minority of voters is` returned zero raw rows, so no majority/minority-family inference should be drawn from the minority cells."
    }
  ],
  "cards": [
    {
      "phenomenon": "collective-number-transparent-agreement-cgel",
      "result": "survives_as_module",
      "expected_survival_pattern": "The COCA projection should support `AGR` only if filtered production evidence tracks notional basis and controller identification better than simple surface-head number.",
      "notes": "Data-bearing protocol evaluation. The result supports `AGR` portability and exposes the need for a production bridge, now represented as `community_licensing -> production_probability`. No numeric score movement follows because calibration and opportunity-denominator work remain incomplete.",
      "requirements": {
        "required_nodes": [
          "notional_agreement_basis",
          "agreement_controller_identification",
          "agreement_feature_alignment",
          "community_licensing",
          "production_probability",
          "retrieval_attractor_salience",
          "reported_acceptability",
          "grammaticality_attribution"
        ],
        "required_edges": [
          {
            "source": "notional_agreement_basis",
            "target": "agreement_controller_identification",
            "type": "evidential"
          },
          {
            "source": "agreement_controller_identification",
            "target": "agreement_feature_alignment",
            "type": "constitutive"
          },
          {
            "source": "agreement_feature_alignment",
            "target": "community_licensing",
            "type": "constitutive"
          },
          {
            "source": "community_licensing",
            "target": "production_probability",
            "type": "causal"
          }
        ],
        "forbidden_edges": [
          {
            "source": "retrieval_attractor_salience",
            "target": "community_licensing",
            "type": "causal"
          }
        ]
      },
      "contrast_cells": [
        {
          "id": "bunch-animate-plural-dominant",
          "axes": {
            "community": "COCA-attested English production in target subject-position `a bunch of people/kids` contexts.",
            "norm_centre": "Descriptive corpus-attestation frame, not prescriptive judgment.",
            "genre": "Mixed COCA spoken, fiction, web, blog, movie/TV, news, magazine, and academic registers as returned by KWIC.",
            "medium": "Written corpus transcripts/texts from COCA KWIC rows.",
            "task_framing": "Corpus production measurement with KWIC filtering, not acceptability judgment.",
            "speaker_identity": "Corpus speaker/writer identity as available only through COCA source metadata."
          }
        },
        {
          "id": "bunch-inanimate-sparse-contrast",
          "axes": {
            "community": "COCA-attested English production in target subject-position `a bunch of flowers/things` contexts.",
            "norm_centre": "Descriptive corpus-attestation frame, not prescriptive judgment.",
            "genre": "Mixed COCA registers, though the filtered cell is sparse.",
            "medium": "Written corpus transcripts/texts from COCA KWIC rows.",
            "task_framing": "Corpus production measurement with KWIC filtering and sparse-cell caution.",
            "speaker_identity": "Corpus speaker/writer identity as available only through COCA source metadata."
          }
        },
        {
          "id": "majority-plural-dominant",
          "axes": {
            "community": "COCA-attested English production in `a/the majority of people` contexts.",
            "norm_centre": "Descriptive corpus-attestation frame, not prescriptive judgment.",
            "genre": "Mixed COCA registers with most positive rows from `the majority of people are`.",
            "medium": "Written corpus transcripts/texts from COCA KWIC rows.",
            "task_framing": "Corpus production measurement with KWIC filtering, not acceptability judgment.",
            "speaker_identity": "Corpus speaker/writer identity as available only through COCA source metadata."
          }
        },
        {
          "id": "partitive-qn-people-plural-dominant",
          "axes": {
            "community": "COCA-attested English production in registered `lots/plenty/rest` people-frame contexts.",
            "norm_centre": "Descriptive corpus-attestation frame, not prescriptive judgment.",
            "genre": "Mixed COCA registers for the targeted KWIC subset plus a pre-declared 100-row bounded sample from the high-count `lots of people are` cell.",
            "medium": "Written corpus transcripts/texts from COCA list and KWIC rows.",
            "task_framing": "Corpus production measurement with full KWIC filtering for smaller cells and bounded-sample caution for the high-count positive cell.",
            "speaker_identity": "Corpus speaker/writer identity as available only through COCA source metadata."
          }
        },
        {
          "id": "minority-zero-cell",
          "axes": {
            "community": "COCA-attested English production in registered `a minority of voters` direct-query contexts.",
            "norm_centre": "Descriptive corpus-attestation frame, not prescriptive judgment.",
            "genre": "No positive rows returned by the registered direct strings.",
            "medium": "COCA list-query output.",
            "task_framing": "Sparse-cell / zero-cell query diagnostic.",
            "speaker_identity": "Unavailable because the direct strings returned no rows."
          }
        }
      ]
    }
  ]
}
```


## Target Graph JSON

```json
{
  "id": "agreement-controller-override-candidate",
  "title": "Agreement controller and override candidate",
  "family": "agreement-controller-override",
  "status": "candidate",
  "edge_semantics_level": "profiled",
  "notes": "Twenty-ninth-round mutation generated after agreement cards repeatedly split controller choice, licensed override, and attraction/error pressure. This graph is a narrow agreement module built from source-backed cards, not a general grammar account and not eligible for projective credit until held-out agreement cards are added.",
  "nodes": [
    "agreement_controller_identification",
    "agreement_feature_alignment",
    "agreement_override_pattern",
    "notional_agreement_basis",
    "retrieval_attractor_salience",
    "processing_cost",
    "community_licensing",
    "repair_reformulation_pressure",
    "reported_acceptability",
    "grammaticality_attribution",
    "task_framing",
    "standard_language_ideology",
    "metalinguistic_condemnation",
    "production_probability"
  ],
  "edges": [
    {
      "source": "notional_agreement_basis",
      "target": "agreement_controller_identification",
      "type": "evidential",
      "relation_profile": "contextual_warrant",
      "rationale": "Unit construal, distributivity, or participant-identity readings provide contextual warrant for identifying the agreement controller."
    },
    {
      "source": "agreement_controller_identification",
      "target": "agreement_feature_alignment",
      "type": "constitutive",
      "relation_profile": "partial_component",
      "rationale": "Agreement feature alignment depends on first identifying the relevant controller rather than simply choosing the nearest noun phrase."
    },
    {
      "source": "agreement_override_pattern",
      "target": "agreement_feature_alignment",
      "type": "constitutive",
      "relation_profile": "partial_component",
      "rationale": "Licensed override patterns can satisfy agreement alignment even when they depart from simple head-feature matching."
    },
    {
      "source": "agreement_feature_alignment",
      "target": "community_licensing",
      "type": "constitutive",
      "relation_profile": "necessary_component",
      "rationale": "For agreement cards, controller-feature alignment is a necessary component of licensing in the target repertoire."
    },
    {
      "source": "community_licensing",
      "target": "repair_reformulation_pressure",
      "type": "causal",
      "relation_profile": "negative_monotone",
      "rationale": "Lower licensing of an agreement value predicts greater repair or reformulation pressure."
    },
    {
      "source": "community_licensing",
      "target": "production_probability",
      "type": "causal",
      "relation_profile": "positive_monotone",
      "rationale": "Licensed agreement values tend to have higher production probability in relevant opportunity contexts, without making raw frequency identical to licensing."
    },
    {
      "source": "community_licensing",
      "target": "grammaticality_attribution",
      "type": "evidential",
      "relation_profile": "evidential_warrant",
      "rationale": "Community licensing provides warrant for agreement-related grammaticality attribution without being identical to the attribution."
    },
    {
      "source": "repair_reformulation_pressure",
      "target": "grammaticality_attribution",
      "type": "evidential",
      "relation_profile": "contextual_warrant",
      "rationale": "Repair pressure is contextual evidence that an agreement value is being treated as problematic."
    },
    {
      "source": "retrieval_attractor_salience",
      "target": "processing_cost",
      "type": "causal",
      "relation_profile": "positive_monotone",
      "rationale": "A salient non-controller feature source can increase processing or retrieval cost in agreement production and judgment."
    },
    {
      "source": "retrieval_attractor_salience",
      "target": "production_probability",
      "type": "causal",
      "relation_profile": "mixed_contextual",
      "rationale": "A salient attractor can increase production of agreement errors in some tasks while having little effect in others."
    },
    {
      "source": "processing_cost",
      "target": "reported_acceptability",
      "type": "causal",
      "relation_profile": "negative_monotone",
      "rationale": "Processing or retrieval difficulty can lower reported acceptability independently of agreement licensing."
    },
    {
      "source": "reported_acceptability",
      "target": "grammaticality_attribution",
      "type": "evidential",
      "relation_profile": "contextual_warrant",
      "rationale": "Acceptability reports provide contextual evidence for attribution but can be perturbed by processing or task framing."
    },
    {
      "source": "task_framing",
      "target": "reported_acceptability",
      "type": "causal",
      "relation_profile": "mixed_contextual",
      "rationale": "Speeded, correctness-framed, naturalness-framed, and editing tasks can shift reported acceptability for agreement contrasts."
    },
    {
      "source": "task_framing",
      "target": "grammaticality_attribution",
      "type": "causal",
      "relation_profile": "mixed_contextual",
      "rationale": "Task framing can cue whether respondents treat an agreement contrast as grammar, style, error, or acceptable override."
    },
    {
      "source": "standard_language_ideology",
      "target": "metalinguistic_condemnation",
      "type": "causal",
      "relation_profile": "positive_monotone",
      "rationale": "Standard-language ideology can raise explicit condemnation of agreement variants independently of production probability."
    },
    {
      "source": "metalinguistic_condemnation",
      "target": "grammaticality_attribution",
      "type": "evidential",
      "relation_profile": "contextual_warrant",
      "rationale": "Condemnation can influence attribution while remaining separable from controller alignment and licensing."
    }
  ],
  "scores": {
    "empirical_coverage": 0,
    "projective_power": 0,
    "counterexample_resilience": 0,
    "measurement_clarity": 0,
    "explanatory_payoff": 0,
    "cross_domain_stability": 0,
    "complexity_penalty": 0,
    "circularity_penalty": 0,
    "construct_confusion_penalty": 0,
    "theory_preservation_penalty": 0
  },
  "score_status": {
    "kind": "scoped_module",
    "evaluation": "evaluations/protocol-tests/agreement-controller-override-heldout-scope-2026-06-09.json",
    "scope": "Agreement controller identification, agreement feature alignment, licensed override patterns, notional agreement basis, and retrieval-attractor salience; not a general grammaticality account."
  }
}
```


## Phenomenon Card: collective-number-transparent-agreement-cgel

```markdown
# Phenomenon Card: collective and number-transparent agreement

**Stress test:** Licensed agreement overrides vs processing errors.

## Description

CGEL distinguishes proximity agreement errors from established override patterns. Collective nouns
can take singular or plural agreement in Standard English, while number-transparent nouns can
require an agreement value that differs from the head noun:

- `The committee has not yet come to a decision.`
- `The committee have not yet come to a decision.`
- `A number of spots have appeared.`
- `Heaps of money has been spent.`

These are not simply nearest-NP errors. They involve more specific agreement patterns that override
simple head-noun agreement.

## Source Pointers

- Source IDs: `cgel-subject-verb-agreement`
- Local source: `/Users/brettreynolds/Documents/CGEL/out/058_18 Subjectverb agreement 499.pdf`
- Related cards: [subject-verb-agreement-cgel](subject-verb-agreement-cgel.md),
  [proximity-agreement-error-cgel](proximity-agreement-error-cgel.md)

## Why It Matters

The card prevents an over-simple processing account of all non-simple agreement. Some departures
from simple agreement are grammatical in the relevant repertoire, while others are production or
processing errors.

## Minimum Contrast Cells

- simple singular collective agreement: `The committee has ...`;
- plural collective override: `The committee have ...`;
- number-transparent plural override: `A number of spots have ...`;
- number-transparent singular override: `Heaps of money has ...`;
- proximity error: singular head plus plural nearest NP with plural verb.

## Candidate Nodes

- operator_value
- community_licensing
- constructional_function
- reported_acceptability
- grammaticality_attribution
- processing_cost
- task_framing

## Potential Construct Pressure

This card may require an agreement-controller or agreement-pattern licensing construct. Broad
operator value can say agreement is grammar-relevant, but it cannot distinguish simple agreement,
licensed override, and proximity error without extra structure.

## Graph Failure Modes

- Treats all non-head agreement as processing error.
- Treats all non-head agreement as licensed.
- Treats British/American or formal/informal variation as mere ideology.
- Collapses number-transparent constructions with collective nouns.

## Predicted Discriminators

- `OPG` should partly survive as broad operator-value scaffolding.
- `PROC` should fail as a general account because these are not all processing errors.
- A future agreement graph would need agreement-controller and override-pattern constructs.
```


## Extra File: notes/agr-coca-vertical-slice-report-2026-06-09.md

```md
# AGR COCA Vertical Slice Report

**Date:** 2026-06-09
**Graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Evaluation:** `evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`
**Data directory:** `data/agr-coca-projection/`
**Status:** Worked vertical slice; no numeric score movement.

## One-Sentence Result

The `AGR` module beats a simple surface-head-number baseline in the checked English production
cells, with the strongest pressure from `majority`: 105:0 exact plural agreement rows, 142:0 after a
bounded denominator omission audit, and no detected omitted singular-agreement competitors.

## What Was Being Tested

The target graph separates five agreement constructs:

- `agreement_controller_identification`;
- `agreement_feature_alignment`;
- `agreement_override_pattern`;
- `notional_agreement_basis`;
- `retrieval_attractor_salience`.

The corpus vertical slice asks whether production evidence in COCA supports that separation better
than a simpler baseline:

> Agreement tracks the number of the surface head noun in the agreement-bearing subject phrase.

The test is deliberately narrow. It is about English corpus production in selected number-transparent
agreement cells. It is not a general grammaticality account and it is not a licensing score.

## Method

The lane used a staged procedure:

1. Register query cells and expected directions in `query-plan.csv` and `prediction-register.csv`.
2. Treat raw COCA list counts as triage only.
3. Use KWIC filtering to code target agreement rows separately from false positives, denominator-only
   nonstandard/error rows, and non-target rows.
4. Add a bounded positive-cell sample for the high-count `lots of people are` row set.
5. Add a false-positive audit across already coded exact-query rows.
6. Add a bounded false-omission denominator sample for `the majority of people`.
7. Report Wilson intervals for plural share among coded target agreement rows.

This improves on a raw-frequency corpus pass by separating discovery, filtering, denominator risk,
and uncertainty.

## Main Discriminator

The cleanest discriminator is `majority`, not `bunch`.

| cell | surface-head baseline | AGR expectation | evidence | result |
|---|---|---|---:|---|
| `a/the majority of people` | singular from `majority` | plural under plural-set controller construal | 105:0 exact; 142:0 audit-augmented | baseline disconfirmed |

The exact query rows already disconfirm the surface-head baseline. The denominator omission audit
then checks whether direct `are/is` queries missed enough singular opportunities to reverse the
result. They did not. In a bounded 98-row `the majority of people` denominator sample, omitted
agreement-bearing opportunities were 37 plural and 0 singular.

## Other Discriminator Cells

| cell | evidence | interpretation |
|---|---:|---|
| animate `bunch` | 71 plural vs. 1 singular | strong baseline pressure, but `bunch` is a known boundary item |
| `the rest of the people` | 14 plural vs. 0 singular | clean direction, small cell |
| inanimate `bunch` | 1 plural vs. 1 singular | contrastive/sparse, not an estimate |
| `lots/plenty of people` | 163 plural vs. 0 licensed singular in checked/sample rows | supportive portability evidence, less clean as a surface-head diagnostic |

The result is therefore not "all plural complements take plural agreement." It is narrower:
controller identification and notional basis matter in cells where the surface head alone predicts
the wrong dominant direction.

## Measurement Audit

False-positive pressure is low in the clean cells:

| audit | target rows | excluded false positives | result |
|---|---:|---:|---|
| animate `bunch` exact rows | 72 | 5 | low false-positive pressure |
| `majority` exact rows | 105 | 4 | low false-positive pressure |
| selected partitive/QN exact rows | 77 | 4 | low false-positive pressure |
| `lots of people are` bounded sample | 100 | 0 | no false-positive pressure in sample |

False omission was checked for the strongest non-`bunch` discriminator:

| denominator sample | omitted plural | omitted singular | result |
|---|---:|---:|---|
| `the majority of people` | 37 | 0 | omission strengthens the plural direction |

## Uncertainty Summary

| cell | plural | singular | plural share | 95% Wilson interval |
|---|---:|---:|---:|---:|
| animate `bunch` | 71 | 1 | 0.986 | [0.925, 0.998] |
| `majority` exact rows | 105 | 0 | 1.000 | [0.965, 1.000] |
| `majority` audit-augmented | 142 | 0 | 1.000 | [0.974, 1.000] |
| `the rest of the people` | 14 | 0 | 1.000 | [0.785, 1.000] |

This makes the evidence hierarchy explicit: `majority` is the strongest cell, animate `bunch` is
strong but constructionally special, and `rest` is directionally clean but small.

## What This Licenses

The current warranted claim is:

> In the checked English production cells, plural agreement is not a raw-query artifact and is not
> predicted by a simple surface-head-number baseline; the strongest current pressure comes from
> `majority` plus the denominator omission audit.

The slice supports the workbench method because the graph did work a flat baseline could not do:
it identified where controller identification and notional basis should matter, separated production
from licensing, and forced measurement audits before any score movement.

## What This Does Not License

This does not show that `AGR` is a general account of grammaticality.

It also does not authorize numeric scores because:

- the evidence is English-only;
- the evidence is corpus-production-only;
- only one denominator omission audit has been run;
- no cross-domain stability test has been passed;
- no sealed held-out tranche was reserved before the AGR lane began.

The result is a publishable pilot slice for the workbench method, not a claim that the best graph of
grammaticality has been found.

## Completed Follow-Up

The compression test is now recorded in `notes/agr-coca-ablation-test-2026-06-09.md`.

It found that the core agreement-scope constructs remain load-bearing across the existing
evaluations, while `production_probability` and `retrieval_attractor_salience` are load-bearing for
the COCA projection layer specifically. No graph mutation, compression, numeric score movement, or
new held-out card tranche follows from that result.

## Next Decision Boundary

The next step should not be another nearby COCA query.

For a methods/pilot paper, use this report plus the ablation note as the worked example. For
discovery pressure, move to critic-verdict variance or to a compression pass over overlap pairs such
as `FDL`/`UOB` and `OPG`/`DYN`.
```


## Extra File: notes/agr-coca-ablation-test-2026-06-09.md

```md
# AGR COCA Ablation Test

**Date:** 2026-06-09
**Graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Runner:** `scripts/run_agr_ablation.py`
**Summary data:** `data/agr-coca-projection/ablation-summary.csv`
**Status:** Compression check; no graph mutation and no numeric score movement.

## Question

The AGR vertical slice showed that the module beats a simple surface-head-number baseline in
checked COCA production cells. This ablation asks a different question:

> Which AGR constructs are load-bearing for the existing COCA and held-out evaluations?

The test creates temporary graph variants, repoints the existing AGR evaluations at each variant,
and records whether graph validation and evaluation validation survive. The invalid variants are
not archived as candidates.

## Ablations

The runner tests five graph changes:

- remove `notional_agreement_basis`;
- merge `agreement_controller_identification` into `agreement_feature_alignment`;
- remove `production_probability`;
- remove `retrieval_attractor_salience`;
- remove `agreement_override_pattern`.

The evaluations are:

- `agreement-controller-override-coca-projection-2026-06-09`;
- `agreement-controller-override-heldout-scope-2026-06-09`;
- `agreement-controller-override-heldout-measure-2026-06-09`.

## Results

| ablation | COCA projection | held-out scope | held-out measure | interpretation |
|---|---|---|---|---|
| baseline | passes | passes | passes | sanity check |
| drop `notional_agreement_basis` | fails | fails | fails | load-bearing across the AGR module |
| merge controller into alignment | fails | fails | fails | the controller/alignment split is load-bearing |
| drop `production_probability` | fails | passes | passes | production bridge is load-bearing for the COCA vertical slice, not for the older scope tests |
| drop `retrieval_attractor_salience` | fails | passes | passes | retrieval-attractor salience is load-bearing for the COCA/attraction-facing evaluation layer only |
| drop `agreement_override_pattern` | passes | fails | fails | override pattern is load-bearing for held-out agreement scope, not for the current COCA cells |

All ablated graphs remain graph-valid. Failures are evaluation failures: required nodes, required
edges, or activated paths disappear.

## Decision

Do not compress AGR right now.

The current module is not obviously overbuilt relative to the tests it has actually faced. The
ablation instead separates two kinds of load-bearing structure:

- core agreement-scope structure: `notional_agreement_basis`, `agreement_controller_identification`,
  `agreement_feature_alignment`, and `agreement_override_pattern`;
- COCA vertical-slice structure: `production_probability` and `retrieval_attractor_salience`.

This is useful because it keeps the pilot corpus lane from being mistaken for the whole agreement
module. `production_probability` is needed when the graph is asked to make corpus-production
claims. `agreement_override_pattern` is needed when the graph is asked to handle held-out agreement
override cases. Neither result authorizes numeric score movement.

## Next Marginal Move

Do not add more nearby AGR cards immediately. The next higher-value pressure is either:

1. a critic-verdict variance check on one existing evaluation, to estimate how noisy the survival
   labels are; or
2. a second compression pass over the more suspicious overlap pairs, especially `FDL`/`UOB` and
   `OPG`/`DYN`.

Held-out cards become urgent only when a graph is being considered for projective score movement or
a broader scope claim. AGR is not there yet.
```


## Extra File: data/agr-coca-projection/summary.csv

```csv
run_id,cell_id,query,query_type,agreement_value,raw_count,filtered_count,filtering_status,source_file,evidence_status,notes
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,a bunch of people is,list,singular_present,3,0,kwic_filtered,raw/bunch-animate-confirmatory/kwic/01-a-bunch-of-people-is.json,kwic_filtered_false_positive_only,KWIC-filtered: all 3 raw hits are non-subject false positives.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,a bunch of people are,list,plural_present,27,26,kwic_filtered,raw/bunch-animate-confirmatory/kwic/02-a-bunch-of-people-are.json,kwic_filtered_target_observed,KWIC-filtered: 26 target plural text rows; raw list frequency was 27.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,a bunch of people was,list,singular_past,0,0,raw_zero,raw/bunch-animate-confirmatory/03-a-bunch-of-people-was.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,a bunch of people were,list,plural_past,28,28,kwic_filtered,raw/bunch-animate-confirmatory/kwic/04-a-bunch-of-people-were.json,kwic_filtered_target_observed,KWIC-filtered: 28 target plural text rows.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,a bunch of kids is,list,singular_present,3,1,kwic_filtered,raw/bunch-animate-confirmatory/kwic/05-a-bunch-of-kids-is.json,kwic_filtered_target_observed,KWIC-filtered: 1 target singular row; 2 raw hits are non-subject false positives.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,a bunch of kids are,list,plural_present,5,5,kwic_filtered,raw/bunch-animate-confirmatory/kwic/06-a-bunch-of-kids-are.json,kwic_filtered_target_observed,KWIC-filtered: 5 target plural text rows.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,a bunch of kids was,list,singular_past,0,0,raw_zero,raw/bunch-animate-confirmatory/07-a-bunch-of-kids-was.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,a bunch of kids were,list,plural_past,12,12,kwic_filtered,raw/bunch-animate-confirmatory/kwic/08-a-bunch-of-kids-were.json,kwic_filtered_target_observed,KWIC-filtered: 12 target plural text rows.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,aggregate plural,list,plural,72,71,kwic_filtered,,kwic_filtered_target_observed,Filtered plural target total: 26 people are + 28 people were + 5 kids are + 12 kids were.
2026-06-09-bunch-animate-list,bunch-animate-confirmatory,aggregate singular,list,singular,6,1,kwic_filtered,,kwic_filtered_target_observed,Filtered singular target total: 0 people is + 0 people was + 1 kids is + 0 kids was.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,a bunch of flowers is,list,singular_present,2,1,kwic_filtered,raw/bunch-inanimate-confirmatory/kwic/01-a-bunch-of-flowers-is.json,kwic_filtered_target_observed,KWIC-filtered: 1 target singular row; 1 raw hit is a non-subject false positive.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,a bunch of flowers are,list,plural_present,0,0,raw_zero,raw/bunch-inanimate-confirmatory/02-a-bunch-of-flowers-are.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,a bunch of flowers was,list,singular_past,0,0,raw_zero,raw/bunch-inanimate-confirmatory/03-a-bunch-of-flowers-was.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,a bunch of flowers were,list,plural_past,0,0,raw_zero,raw/bunch-inanimate-confirmatory/04-a-bunch-of-flowers-were.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,a bunch of things is,list,singular_present,1,0,kwic_filtered,raw/bunch-inanimate-confirmatory/kwic/05-a-bunch-of-things-is.json,kwic_filtered_false_positive_only,KWIC-filtered: the only raw hit is a non-subject false positive.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,a bunch of things are,list,plural_present,0,0,raw_zero,raw/bunch-inanimate-confirmatory/06-a-bunch-of-things-are.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,a bunch of things was,list,singular_past,0,0,raw_zero,raw/bunch-inanimate-confirmatory/07-a-bunch-of-things-was.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,a bunch of things were,list,plural_past,1,1,kwic_filtered,raw/bunch-inanimate-confirmatory/kwic/08-a-bunch-of-things-were.json,kwic_filtered_target_observed,KWIC-filtered: 1 target plural row.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,aggregate plural,list,plural,1,1,kwic_filtered,,kwic_filtered_target_observed,Filtered plural target total: 0 flowers are + 0 flowers were + 0 things are + 1 things were.
2026-06-09-bunch-inanimate-list,bunch-inanimate-confirmatory,aggregate singular,list,singular,3,1,kwic_filtered,,kwic_filtered_target_observed,Filtered singular target total: 1 flowers is + 0 flowers was + 0 things is + 0 things was.
2026-06-09-majority-minority-list,majority-minority-confirmatory,a majority of people are,list,plural_present,7,7,kwic_filtered,raw/majority-minority-confirmatory/kwic/01-a-majority-of-people-are.json,kwic_filtered_target_observed,KWIC-filtered: 7 target plural rows.
2026-06-09-majority-minority-list,majority-minority-confirmatory,a majority of people is,list,singular_present,0,0,raw_zero,raw/majority-minority-confirmatory/02-a-majority-of-people-is.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-majority-minority-list,majority-minority-confirmatory,the majority of people are,list,plural_present,99,98,kwic_filtered,raw/majority-minority-confirmatory/kwic/03-the-majority-of-people-are.json,kwic_filtered_target_observed,KWIC-filtered: 98 parsed target plural rows from a raw list frequency of 99; one COCA row was absent from the KWIC frame.
2026-06-09-majority-minority-list,majority-minority-confirmatory,the majority of people is,list,singular_present,5,0,kwic_filtered,raw/majority-minority-confirmatory/kwic/04-the-majority-of-people-is.json,kwic_filtered_false_positive_only,KWIC-filtered: 4 non-subject false positives and 1 nonstandard/error denominator-only row; 0 target singular rows.
2026-06-09-majority-minority-list,majority-minority-confirmatory,a minority of voters are,list,plural_present,0,0,raw_zero,raw/majority-minority-confirmatory/05-a-minority-of-voters-are.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-majority-minority-list,majority-minority-confirmatory,a minority of voters is,list,singular_present,0,0,raw_zero,raw/majority-minority-confirmatory/06-a-minority-of-voters-is.json,raw_zero,Raw no-match result; zero cell not KWIC-fetched.
2026-06-09-majority-minority-list,majority-minority-confirmatory,aggregate plural,list,plural,106,105,kwic_filtered,,kwic_filtered_target_observed,Filtered plural target total: 7 a-majority people are + 98 the-majority people are + 0 a-minority voters are.
2026-06-09-majority-minority-list,majority-minority-confirmatory,aggregate singular,list,singular,5,0,kwic_filtered,,kwic_filtered_false_positive_only,Filtered singular target total: 0 a-majority people is + 0 the-majority people is + 0 a-minority voters is.
2026-06-09-known-qn-list,known-qn-calibration,a number of people are,list,plural_present,52,51,kwic_filtered,raw/known-qn-calibration/kwic/01-a-number-of-people-are.json,kwic_filtered_target_observed,KWIC-filtered: 51 target plural rows; 1 grammar-instruction/metalinguistic row excluded.
2026-06-09-known-qn-list,known-qn-calibration,a number of people were,list,plural_past,48,47,kwic_filtered,raw/known-qn-calibration/kwic/02-a-number-of-people-were.json,kwic_filtered_target_observed,KWIC-filtered: 47 target plural rows; 1 grammar-instruction/metalinguistic row excluded.
2026-06-09-known-qn-list,known-qn-calibration,a lot of money is,list,singular_present,60,42,kwic_filtered,raw/known-qn-calibration/kwic/03-a-lot-of-money-is.json,kwic_filtered_target_observed,KWIC-filtered: 42 target singular rows; 18 raw hits are non-subject false positives.
2026-06-09-known-qn-list,known-qn-calibration,a lot of money are,list,plural_present,12,0,kwic_filtered,raw/known-qn-calibration/kwic/04-a-lot-of-money-are.json,kwic_filtered_false_positive_only,KWIC-filtered: 9 parse-shift rows and 2 non-subject rows; 1 denominator-only nonstandard/error row; 0 licensed target plural rows.
2026-06-09-known-qn-list,known-qn-calibration,aggregate number-transparent plural,list,plural,100,98,kwic_filtered,,kwic_filtered_target_observed,Filtered plural target total for a number of people: 51 are + 47 were.
2026-06-09-known-qn-list,known-qn-calibration,aggregate mass singular,list,singular,60,42,kwic_filtered,,kwic_filtered_target_observed,Filtered singular target total for a lot of money is: 42 target rows.
2026-06-09-known-qn-list,known-qn-calibration,aggregate mass plural,list,plural,12,0,kwic_filtered,,kwic_filtered_false_positive_only,Filtered plural target total for a lot of money are: 0 target rows; one denominator-only nonstandard/error row retained in coding.
2026-06-09-partitive-list,partitive-calibration,lots of people,list,not_applicable,3875,,raw_unfiltered,raw/partitive-calibration/01-lots-of-people.json,raw_phrase_count,Raw phrase-count denominator probe only; COCA reports a sampled high-frequency phrase count.
2026-06-09-partitive-list,partitive-calibration,lots of the people,list,not_applicable,5,,raw_unfiltered,raw/partitive-calibration/02-lots-of-the-people.json,raw_phrase_count,Raw phrase-count denominator probe only; definite-partitive variant is rare.
2026-06-09-partitive-list,partitive-calibration,plenty of people,list,not_applicable,1563,,raw_unfiltered,raw/partitive-calibration/03-plenty-of-people.json,raw_phrase_count,Raw phrase-count denominator probe only; COCA reports a sampled high-frequency phrase count.
2026-06-09-partitive-list,partitive-calibration,plenty of the people,list,not_applicable,1,,raw_unfiltered,raw/partitive-calibration/04-plenty-of-the-people.json,raw_phrase_count,Raw phrase-count denominator probe only; definite-partitive variant is nearly absent.
2026-06-09-partitive-list,partitive-calibration,the rest of people,list,not_applicable,12,,raw_unfiltered,raw/partitive-calibration/05-the-rest-of-people.json,raw_phrase_count,Raw phrase-count denominator probe only; likely needs KWIC filtering for non-target uses.
2026-06-09-partitive-list,partitive-calibration,the rest of the people,list,not_applicable,272,,raw_unfiltered,raw/partitive-calibration/06-the-rest-of-the-people.json,raw_phrase_count,Raw phrase-count denominator probe only; definite complement is the expected high-frequency frame for rest.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,lots of people are,list,plural_present,287,100,kwic_sample,raw/partitive-agreement-followup/kwic/01-lots-of-people-are.json,kwic_sample_target_observed,Bounded 100-row default KWIC sample from the high-count raw cell; all 100 sampled rows are target plural agreement. Not a full filtered count for all 287 raw hits.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,lots of people is,list,singular_present,5,0,kwic_filtered,raw/partitive-agreement-followup/kwic/02-lots-of-people-is.json,kwic_filtered_false_positive_only,KWIC-filtered: 4 non-subject rows and 1 denominator-only nonstandard/error row; 0 licensed target singular rows.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,plenty of people are,list,plural_present,65,63,kwic_filtered,raw/partitive-agreement-followup/kwic/03-plenty-of-people-are.json,kwic_filtered_target_observed,KWIC-filtered: 63 target plural rows from 64 parsed KWIC rows; 1 malformed denominator-only row; raw list count was 65.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,plenty of people is,list,singular_present,0,,raw_zero,raw/partitive-agreement-followup/04-plenty-of-people-is.json,raw_zero,Raw no-match result.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,the rest of the people are,list,plural_present,15,14,kwic_filtered,raw/partitive-agreement-followup/kwic/05-the-rest-of-the-people-are.json,kwic_filtered_target_observed,KWIC-filtered: 14 parsed target plural rows from a raw list count of 15; one COCA row was absent from the KWIC frame.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,the rest of the people is,list,singular_present,0,,raw_zero,raw/partitive-agreement-followup/06-the-rest-of-the-people-is.json,raw_zero,Raw no-match result.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,aggregate raw plural,list,plural,367,,raw_unfiltered,,raw_phrase_count,Raw plural total only: 287 lots + 65 plenty + 15 rest; not KWIC-filtered.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,aggregate raw singular,list,singular,5,,raw_unfiltered,,raw_counter_cell_needs_kwic,Raw singular total only: 5 lots + 0 plenty + 0 rest; not KWIC-filtered.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,aggregate targeted KWIC/sample plural subset,list,plural,367,177,kwic_sample_plus_filtered,,kwic_sample_target_observed,Sample/filter evidence: 100 sampled lots are + 63 plenty are + 14 rest are. The lots of people are cell is sample-coded only and not fully filtered.
2026-06-09-partitive-agreement-list,partitive-agreement-followup,aggregate targeted KWIC singular subset,list,singular,5,0,kwic_filtered,,kwic_filtered_false_positive_only,Filtered counter-direction subset: lots of people is has 0 licensed target singular rows.
```


## Extra File: data/agr-coca-projection/baseline-discriminator.csv

```csv
discriminator_id,cell_family,query_subset,surface_head_baseline_prediction,agr_prediction,evidence,result,notes
animate_bunch,bunch-animate-confirmatory,a bunch of people/kids + finite agreement,singular agreement from singular head bunch,plural agreement when animate plural member construal supplies the controller,71 target plural rows vs 1 target singular row,baseline_disconfirmed_for_cell,Strongest current discriminator: surface head number predicts the wrong dominant direction.
majority_people,majority-minority-confirmatory,a/the majority of people + finite agreement,singular agreement from singular head majority,plural agreement licensed by controller identification over plural human set construal,105 target plural rows vs 0 target singular rows,baseline_disconfirmed_for_cell,Best non-bunch portability discriminator against surface-head-only agreement.
rest_people,partitive-agreement-followup,the rest of the people are/is,singular agreement from singular head rest,plural agreement available when the people-set supplies the relevant controller,14 filtered target plural rows vs 0 target singular rows,baseline_disconfirmed_for_cell,Small but clean singular-head pressure point inside the partitive/QN follow-up.
inanimate_bunch,bunch-inanimate-confirmatory,a bunch of flowers/things + finite agreement,singular agreement from singular head bunch,distinct sparse or non-animate profile rather than animate-member plural dominance,1 target plural row vs 1 target singular row,inconclusive_sparse,Useful as an animate/inanimate contrast but not a stable baseline-disconfirmation cell.
lots_plenty_people,partitive-agreement-followup,lots/plenty of people + finite agreement,not a clean surface-head-only baseline because quantity-head status differs by item,plural agreement should dominate in usable people-frame contexts,163 target plural rows vs 0 licensed target singular rows,supportive_not_baseline_clean,Portability evidence for the people-frame direction; weaker as a surface-head-number discriminator.
```


## Extra File: data/agr-coca-projection/uncertainty-summary.csv

```csv
summary_id,cell_family,scope,plural_target_rows,singular_target_rows,total_target_rows,plural_share,wilson_95_low,wilson_95_high,interpretation,notes
animate_bunch_exact,bunch-animate-confirmatory,full exact-query KWIC coding,71,1,72,0.986,0.925,0.998,strong_directional_result,Surface-head singular baseline is strongly pressured; lower interval bound remains well above parity.
majority_exact,majority-minority-confirmatory,full exact-query KWIC coding,105,0,105,1.000,0.965,1.000,tight_directional_result,Best exact-query non-bunch discriminator.
majority_audit_augmented,majority-minority-confirmatory,exact rows plus 37 omitted plural opportunities from bounded denominator sample,142,0,142,1.000,0.974,1.000,tight_audit_augmented_result,Direct are/is strings undercount plural opportunities but do not reveal omitted singular competitors.
rest_people_exact,partitive-agreement-followup,full exact-query KWIC coding for the small rest people cell,14,0,14,1.000,0.785,1.000,clean_but_wide_small_cell,Direction is clean but the interval is wide; useful as a small supporting discriminator rather than a main estimate.
```
