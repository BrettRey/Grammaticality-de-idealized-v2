# Seventeenth Adversarial Pass Synthesis

**Date:** 2026-06-09
**Source pass:** Gibson, *Syntax: A cognitive approach*
**Question:** does the source do something different for the phenomenon cards?

## Result

Yes, but at the card layer rather than the graph layer.

Gibson does not require the workbench to adopt dependency grammar, dependency locality, or
noisy-channel processing as a general account. It does supply sharper stress cells for processing,
production, and construction-specific dependency contrasts. The right move is therefore to add
source-backed cards and hold graph mutation until those cards are run against the current modules.

## What It Adds

1. **Licensed alternatives with unequal locality cost.** Dependency-length alternations show that
   production probability and felt naturalness can diverge while licensing remains stable.
2. **Illusions of ungrammaticality.** Garden-path sentences show low first-pass acceptability from
   temporary ambiguity rather than non-licensing.
3. **Illusions of grammaticality.** Missing material, depth-charge, and comparative-illusion cases
   show high acceptability from rational reconstruction rather than licensing.
4. **Construction-specific islands.** Island effects vary across wh-questions, relatives,
   exclamatives, and controls; a uniform extraction-ban graph is too coarse.
5. **Genre-stabilized complexity.** Legalese shows high production probability and genre fit despite
   poor comprehension and low preference.

## Card Changes

Added five source-backed cards:

- `dependency-locality-alternations-gibson`
- `garden-path-temporary-ambiguity-gibson`
- `noisy-channel-overacceptance-gibson`
- `island-construction-variation-gibson`
- `legalese-center-embedding-gibson`

These cards should be evaluated before any new Gibson-inspired graph is added.

A local minimal-pair card, `frame-conditioned-duration-have`, was also added during this pass. It
tests whether a graph treats context as selecting among licensed constructional frames rather than
as freely licensing an intended interpretation.

## Current Prediction

- `PROC` should do most of the work for garden paths, dependency-locality alternations, and
  noisy-channel overacceptance, but may need a new construct for recoverable intended-form distance.
- `OPG` should be pressured by island construction variation because construction type and discourse
  role matter, not just recoverability, opportunity, and preemption.
- `DYN` and `TASK` are likely needed for legalese persistence because genre production, officialness,
  comprehension, and preference are separated channels.
- `UPT` may help with island variation when the construction's update role explains why one
  dependency configuration is tolerated and another is not.

## Decision

No graph mutation yet. The next move is protocol-test evaluation of the Gibson cards against the
current module stack.
