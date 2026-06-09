# Phenomenon Card: fused relative constructions

**Stress test:** Low opportunity, transparent relatives, and licensing uncertainty.

## Description

Fused relatives and transparent-relative-like cases create forms that are often interpretable but
unevenly licensed across speakers, registers, and constructions. Some cases look rare rather than
impossible; others are understandable while still triggering repair or reformulation pressure.

## Source Pointers

- Source IDs: `cgel-fused-relatives`, `reynolds-transparent-free-relatives`,
  `reynolds-independent-relative-whose`
- Related seed card: [transparent-free-relatives](transparent-free-relatives.md)

## Why It Matters

The case tests whether rarity is interpreted against opportunity and constructional support, rather
than converted directly into ungrammaticality.

## Minimum Contrast Cells

- ordinary fused relative;
- transparent-relative-like construction with high recoverability;
- low-frequency literary or formal case;
- paraphrase/reformulation competitor available in the same slot.

## Source-Checked Contrast Examples

- Ordinary fused-relative baseline: fused relatives function as phrases rather than clauses in the
  relevant diagnostics.
- Relative/interrogative contrast: similar surface forms can be fused relatives or open
  interrogatives depending on constructional function.
- Preposition contrast: a fused relative can differ from an integrated relative in whether a
  preposition can be fronted.
- Reduction contrast: open interrogatives can reduce in ways fused relatives cannot.
- Restricted-word contrast: several wh forms occur in fused relatives only under special
  restrictions, while `-ever` forms are freer in fused relatives.
- Corpus-opportunity contrast: local transparent-free-relative work treats corpus absences and
  verb-class asymmetries as evidence about where a construction is licensed, not as immediate proof
  of global ungrammaticality.
- Rare-attestation contrast: the independent relative `whose` work treats rare relative patterns as
  constrained but attested, requiring context and information-structural support rather than a raw
  frequency verdict.

## Source-Checked Evidence

Checked against `cgel-fused-relatives`. The source supports constructional-function and
competitor/paraphrase contrasts. It does not by itself settle low-frequency thresholds, so rarity
and transparent-relative projectibility remain incomplete. Checked against local
transparent-free-relative and independent-relative-`whose` materials; those sources add corpus and
attestation pressure for opportunity-normalized reasoning, but they still do not provide a general
threshold that would make rare transparent cases categorically resolved.

## Data Pointers

- For transparent free relatives, use `Transparent_free_relatives/two-kinds.tex` and `coca-data/` to
  split opportunity by verb class, nucleus category, external position, and false-positive type.
  The immediate threshold lane is not "rare vs common" but "absence after a checked opportunity
  set."
- For independent relative `whose`, use
  `Independent_relative_whose_A_Bayesian_analysis_of_a_low-frequency_gap/` for the
  low-opportunity/weak-absence logic and `Independent_relative_whose/items/all_items.csv` for
  judgment contrasts that vary licensing context against baselines.
- A future `passed` prediction should require an explicit opportunity denominator, a verified
  attestation count or absence check, and a named competitor set. Until then, the card should remain
  `mixed` or `partly_survives` rather than promoting numeric score movement.

## Candidate Nodes

- constructional_analogy
- opportunity_mass
- opportunity_normalized_attestation
- competitor_availability
- community_licensing
- semantic_pragmatic_recoverability
- repair_reformulation_pressure

## Graph Failure Modes

- Treats low frequency as non-licensing.
- Treats transparent meaning as licensing.
- Fails to represent competitor availability.
- Cannot distinguish speaker uncertainty from semantic incoherence.

## Predicted Discriminators

- An opportunity/preemption graph should predict stronger rejection where opportunity mass and
  competitor availability are high.
- A context graph should predict genre-conditioned tolerance without needing a general score.
