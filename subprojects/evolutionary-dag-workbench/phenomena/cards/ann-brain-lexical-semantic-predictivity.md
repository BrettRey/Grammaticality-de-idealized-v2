# Phenomenon Card: ANN-brain lexical-semantic predictivity

**Stress test:** Measurement validity and construct leakage.

## Description

Kauf, Tuckute, Levy, Andreas, and Fedorenko (2023) test what drives ANN-to-brain similarity for
fMRI responses in the language network. They perturb naturalistic English sentences before
extracting ANN representations, then ask how well those representations predict the original fMRI
responses.

The key contrast is that ANN-to-fMRI predictivity remains relatively high under word-order
scrambling and content-word preservation, but drops sharply when lexical-semantic content is
removed. Function-word-only strings pattern close to random-word-list controls.

## Source Pointers

- Source IDs: `kauf-et-al-2023-ann-brain-similarity`
- Local source: `/Users/brettreynolds/Downloads/nol_a_00116.pdf.txt`
- Related cards: [noisy-channel-overacceptance-gibson](noisy-channel-overacceptance-gibson.md),
  [comparative-more-less-category](comparative-more-less-category.md),
  [grammatical-but-hard](grammatical-but-hard.md)

## Why It Matters

This is not a direct grammaticality phenomenon. It is a measurement-validity discriminator.

The card guards against a bad evidential move: treating ANN/fMRI brain predictivity as if it directly
tracked syntactic structure, operator licensing, or grammaticality. The source instead shows that
this measurement channel is strongly sensitive to lexical-semantic and topical content. A graph can
use this kind of evidence only if it represents the measurement channel and avoids routing
lexical-semantic preservation directly into licensing.

## Minimum Contrast Cells

- intact sentence representation mapped to the matching fMRI response;
- word-order scrambled sentence with lexical content mostly preserved;
- content-word-only or noun/verb/adjective-preserving sentence;
- function-word-only sentence;
- random word list or random sentence control.

## Source-Checked Evidence

Checked against `kauf-et-al-2023-ann-brain-similarity`. The source reports:

- word-order manipulations reduce ANN-to-brain predictivity only modestly relative to intact
  sentences, including severe scrambling and low-PMI conditions;
- preserving content-word subsets keeps predictivity substantially above random controls;
- preserving only function words produces predictivity close to a random word-list control;
- random sentences from unrelated contexts produce near-chance predictivity;
- the authors explicitly interpret the pattern as lexical-semantic content, not syntactic form, being
  the main contributor to ANN-to-brain similarity for this fMRI benchmark.

## Candidate Nodes

- measurement_task
- task_framing
- processing_cost
- semantic_pragmatic_recoverability
- felt_naturalness_context
- reported_acceptability
- grammaticality_attribution
- community_licensing
- distributional_category_evidence
- analyst_category_assignment

## Potential Construct Pressure

Repeated use of this card may require new measurement-channel nodes, such as:

- `ann_brain_predictivity`
- `lexical_semantic_content_preservation`
- `word_order_preservation`
- `function_word_preservation`
- `neural_language_network_response`

Do not add those nodes from this card alone unless future evaluations need machine-checkable
prediction paths through the measurement channel.

## Graph Failure Modes

- Treats high ANN/fMRI predictivity as evidence for grammatical licensing.
- Treats low function-word contribution to fMRI predictivity as evidence that function words or
  operator exponents are grammatically unimportant.
- Treats lexical-semantic content preservation as grammatical well-formedness.
- Treats word-order robustness in this benchmark as evidence that word order is not part of grammar.
- Ignores task, stimulus, temporal-resolution, and measurement-channel limits.

## Predicted Discriminators

- `PROC` should partly survive if it separates measurement/task effects from licensing, but it should
  expose missing ANN/fMRI measurement-channel constructs.
- `CAT` should partly survive as a measurement-discipline graph, but only if it refuses to turn
  representational evidence into grammaticality attribution by fiat.
- `OPG` should fail as a general account or remain out of scope. Opportunity/preemption machinery
  does not explain ANN-to-brain similarity unless a specific grammar-relevant contrast cell is
  introduced.
