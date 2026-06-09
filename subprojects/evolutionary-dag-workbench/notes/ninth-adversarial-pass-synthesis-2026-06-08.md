# Ninth Adversarial Pass Synthesis: Selection and Collocation Split

**Date:** 2026-06-08
**Mutation:** `selection-collocation-split-candidate`
**Trigger:** `preposition-category-selection-cgel` remained only partly handled by the
context-aware operator-gap module.

## Pressure

The prior operator-gap graph could represent operator value, competitors, opportunity mass,
preemption, repair pressure, and licensing. Its weak point was the preposition boundary case:
fixedness could be mistaken for operator value.

The pressure is to distinguish:

- open payload preposition choice;
- collocational rigidity;
- argument-linking or complement-selection value;
- grammaticized prepositions in restricted constructions.

Without that distinction, examples like selected PP complements risk being over-assimilated to
operator gaps, while ordinary collocations or fixed expressions risk being treated as grammatical
licensing failures.

## Mutation

Added controlled nodes:

- `payload_preposition_choice`
- `collocational_rigidity`
- `argument_linking_selection`

Created `selection-collocation-split-candidate`, a compact profiled graph that keeps:

- argument-linking selection -> operator value -> community licensing;
- constructional function -> argument-linking selection;
- payload preposition choice -> reported acceptability;
- collocational rigidity -> preemption strength;
- competitor availability and opportunity mass -> preemption strength;
- licensing -> repair pressure and attribution.

The graph blocks the dangerous shortcuts:

- collocational rigidity -> operator value;
- payload preposition choice -> community licensing;
- collocational rigidity -> community licensing.

## Evaluation

Added `evaluations/protocol-tests/selection-collocation-split-2026-06-08.json`.

Results:

- `preposition-category-selection-cgel`: survives as a scoped preposition-selection boundary
  module.
- `comparative-more-less-category`: partly survives because the graph uses constructional function
  but lacks analyst category assignment and distributional category evidence.
- `unbounded-dependency-licensing-cgel`: fails as out of scope because the graph deliberately lacks
  dependency-specific recoverability structure.

## Decision

No score movement. The graph is useful as a scoped module for the collocation/selection boundary,
not as a replacement for the broader operator-gap graph.

The next productive move is to compare the live modules by coverage/discriminator matrix rather
than immediately adding another graph.
