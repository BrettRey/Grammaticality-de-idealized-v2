# Phenomenon Card: missing verb-phrase illusion

**Stress test:** Overacceptance from a close omitted-material repair.

## Description

Some complex strings missing a required verb or verb phrase are judged better than matched
grammatical controls because comprehenders reconstruct the intended dependency or clause structure.
The presented string is formally defective, but the intended neighbour is close enough that readers
often process the item as if the missing material were present.

## Source Pointers

- Source IDs: `gibson-syntax-cognitive`
- Related cards: [noisy-channel-overacceptance-gibson](noisy-channel-overacceptance-gibson.md),
  [center-embedding](center-embedding.md)

## Why It Matters

The card tests whether a graph can represent overacceptance without promoting the literal presented
string to community licensing. It also tests whether repair-neighbour distance is more precise than
general recoverability: the intended parse is recoverable because a small omitted-material repair is
available.

## Minimum Contrast Cells

- missing-verb or missing-verb-phrase item with a close intended repair;
- grammatical matched control that is more complex or less natural;
- literal-analysis or proofreading task that foregrounds the missing material;
- first-pass acceptability task that permits reconstruction.

## Source-Checked Evidence

Checked against `gibson-syntax-cognitive` section 2.2.10. The source treats missing-verb-phrase
materials as illusions of grammaticality: formally defective strings can be perceived as more
acceptable than grammatical controls because readers reconstruct a nearby intended sentence.

## Candidate Nodes

- repair_neighbour_distance
- semantic_pragmatic_recoverability
- felt_naturalness_context
- reported_acceptability
- grammaticality_attribution
- task_framing

## Graph Failure Modes

- Treats high first-pass acceptability as community licensing.
- Represents the contrast only as processing ease without the omitted-material neighbour.
- Treats literal-analysis and first-pass acceptability tasks as equivalent.
- Fails to separate the presented string from the reconstructed intended string.

## Predicted Discriminators

- `RNR` should survive if low repair-neighbour distance predicts overacceptance.
- `PROC` should partly survive but remain too coarse if it lacks the repair-neighbour construct.
- `DYN` and `OPG` should not promote the literal defective string through acceptability alone.
