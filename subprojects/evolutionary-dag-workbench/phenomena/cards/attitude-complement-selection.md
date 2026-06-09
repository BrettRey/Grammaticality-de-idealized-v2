# Phenomenon Card: attitude complement selection

**Stress test:** Complement selection, update role, and recoverability.

## Description

Ordinary English attitude predicates differ in which complement types they license:

- `Anna knows that Mary has eaten.`
- `Anna knows whether Mary has eaten.`
- `Anna believes that Mary has eaten.`
- `*Anna believes whether Mary has eaten.`
- `*Anna wonders that Mary has eaten.`
- `Anna wonders whether Mary has eaten.`

The bad cells are usually interpretable: one can infer the intended proposition or question. But
recoverability does not license the wrong complement type for the predicate in this construction.

## Source Pointers

- Source IDs: `brett-that-whether-attitude-complement-minimal-pair`
- Related cards: [preposition-category-selection-cgel](preposition-category-selection-cgel.md),
  [clause-type-force-cgel](clause-type-force-cgel.md),
  [frame-conditioned-duration-have](frame-conditioned-duration-have.md)

## Why It Matters

The card tests whether complement-type selection is represented as a constructional licensing
relation rather than a loose collocation or an ordinary payload choice. It also separates selection
from update role: `that` and `whether` differ in the kind of complement relation they provide, but
the graph should not simply treat every proposition/question distinction as automatic grammar.

## Minimum Contrast Cells

- `know` with declarative `that` complement;
- `know` with interrogative `whether` complement;
- `believe` with declarative `that` complement;
- `believe` with interrogative `whether` complement;
- `wonder` with declarative `that` complement;
- `wonder` with interrogative `whether` complement.

## Candidate Nodes

- argument_linking_selection
- constructional_function
- constructional_frame_fit
- update_role_configuration
- operator_value
- community_licensing
- semantic_pragmatic_recoverability
- repair_reformulation_pressure
- reported_acceptability
- grammaticality_attribution

## Potential Construct Pressure

This card may require a complement-type or selected-update-role construct if
`argument_linking_selection`, `constructional_frame_fit`, and `update_role_configuration` stay too
coarse to distinguish `know`, `believe`, and `wonder` without hand-coded predicate lists.

## Graph Failure Modes

- Treats complementizer choice as a free payload lexical choice.
- Treats semantic recoverability as licensing.
- Treats all `that`/`whether` contrasts as the same update-role contrast, ignoring predicate
  selection.
- Treats fixedness or collocation alone as operator value.

## Predicted Discriminators

- `SEL` should survive as a complement-selection boundary module.
- `FRAME` should partly survive if it represents selected complement frame fit.
- `UPT` should help with update-role distinctions but may lack predicate-selection machinery.
- `PROC` should not explain the core contrast as processing difficulty.
