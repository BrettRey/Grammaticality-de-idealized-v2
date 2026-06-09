# CGEL and Local Correction Source Registry

This registry records source pools for phenomenon-card extraction. These sources supply
contrast cells, examples, and adversarial pressure. They do not supply conclusions the
workbench must vindicate.

## Use Rule

Use CGEL and Brett's correction papers as discovery inputs:

- extract a phenomenon only when it can stress a construct boundary;
- paraphrase examples and analyses rather than copying source prose;
- mark whether a card was used to build a mutation or held out for projection;
- do not treat a CGEL category, correction-paper category, or named theory as the target
  construct unless a graph explicitly earns that move.

Local paths below are working pointers, not publication metadata. Remove or anonymize them
before any public release.

## Local Source Pools

| Source ID | Working source | Likely card use |
|---|---|---|
| `cgel-case` | `<CGEL_ROOT>/out/056_16 Case 455.pdf` | Case form, coordination, hypercorrection, standard ideology |
| `cgel-subject-verb-agreement` | `<CGEL_ROOT>/out/058_18 Subjectverb agreement 499.pdf` | Agreement, attraction, notional agreement, operator vs processing |
| `cgel-fused-head-nps` | `<CGEL_ROOT>/out/049_9 Fused-head and elliptical NPs 410.pdf` | Ellipsis/fusion, recoverability vs licensing |
| `cgel-fused-relatives` | `<CGEL_ROOT>/out/123_6 The fused relative construction.pdf` | Fused relatives, transparent relatives, rarity vs licensing |
| `cgel-unbounded-dependencies` | `<CGEL_ROOT>/out/124_7 Unbounded dependency constructions.pdf` | Extraction, dependency licensing, recoverability |
| `cgel-comparison` | `<CGEL_ROOT>/out/128_4 Scalar term comparison.pdf`; `<CGEL_ROOT>/out/127_3 Metalinguistic comparison more apparent than real.pdf` | Comparative category pressure and metalinguistic diagnostics |
| `reynolds-more-less` | `<LITERATURE_ROOT>/reynolds2024-more-less-never-adverbs.md` | Category/function correction; "more/less" as adversarial category test |
| `cgel-prepositions` | `<CGEL_ROOT>/out/068_1 The category of prepositions 598.pdf`; `<CGEL_ROOT>/out/071_4 The position of a complement relative to the head preposition 626.pdf`; `<CGEL_ROOT>/out/073_6 Grammaticised prepositions 647.pdf` | Preposition selection, grammaticized prepositions, operator-like vs payload-like selection |
| `cgel-clause-type` | `<CGEL_ROOT>/out/101_1 Type as a grammatical system of the clause.pdf`; `<CGEL_ROOT>/out/102_2 Distinctive grammatical properties of the major clause types.pdf` | Clause type, force, response space |
| `cgel-negation-polarity` | `<CGEL_ROOT>/out/095_2 Verbal negation.pdf`; `<CGEL_ROOT>/out/097_4 Polarity-sensitive items.pdf`; `<CGEL_ROOT>/out/099_6 Multiple negation.pdf` | Negation, NPI licensing, negative concord contrast cells |
| `cgel-pronouns` | `<CGEL_ROOT>/out/158_2 The personal pronouns.pdf`; `<CGEL_ROOT>/out/057_17 Gender and pronounantecedent agreement 484.pdf` | Pronoun agreement, personhood, reference tracking, social value |
| `reynolds-personhood-proforms` | `<PAPERS_ROOT>/Personhood_and_proforms/personhood+pro-forms.docx` | Personhood/pro-form category pressure and pronoun contrast cells |
| `reynolds-transparent-free-relatives` | `<PAPERS_ROOT>/Transparent_free_relatives/` | Transparent free relatives, verb-class corpus checks, opportunity/absence discipline |
| `reynolds-independent-relative-whose` | `<PAPERS_ROOT>/Independent_relative_whose/` | Rare relative constructions, independent relative whose, corpus attestation vs apparent gaps |
| `cgel-exclamatives-minor-types` | `<CGEL_ROOT>/out/108_8 Exclamatives and exclamations.pdf`; `<CGEL_ROOT>/out/110_10 Minor clause types.pdf` | Exclamatives, minor clauses, interjection boundary |
| `reynolds-interjections` | `<PAPERS_ROOT>/English_Interjections_as_HPC/` | Uptake-configuring forms, open innovation, operator-boundary tests |
| `cgel-number-quantification` | `<CGEL_ROOT>/out/043_3 Number and countability 333.pdf`; `<CGEL_ROOT>/out/045_5 Quantification 358.pdf`; `<CGEL_ROOT>/out/051_11 Determinative Phrases 431.pdf` | Numeratives, determinatives, countability, category/function pressure |
| `reynolds-numeratives` | `<LITERATURE_ROOT>/Reynolds2026_lexicon_syntax_numerals.md` | Numerative category correction and constructional diagnostics |
| `cgel-nonfinite-verbless` | `<CGEL_ROOT>/out/023_1 Inflectional categories of the verb 74.pdf`; `<CGEL_ROOT>/out/140_10 Verbless clauses.pdf`; `<CGEL_ROOT>/out/23_14 Non-finite and verbless clauses.pdf` | Fragment and clause-boundary licensing |

Path roots for local use:

- `<CGEL_ROOT>` = `/Users/brettreynolds/Documents/CGEL`
- `<LITERATURE_ROOT>` = `/Users/brettreynolds/Documents/LLM-CLI-projects/literature`
- `<PAPERS_ROOT>` = `/Users/brettreynolds/Documents/LLM-CLI-projects/papers`

## Extraction Protocol

For each extracted card, record:

- source IDs;
- a short phenomenon description;
- minimum contrast cells;
- candidate nodes from `ontology/nodes.yaml`;
- graph failure modes;
- predicted discriminators between live graph families.

A source-backed card can be used as held-out evidence only if it was not used to choose the
mutation being evaluated. Held-out use must name the card ID, not only the source text.
