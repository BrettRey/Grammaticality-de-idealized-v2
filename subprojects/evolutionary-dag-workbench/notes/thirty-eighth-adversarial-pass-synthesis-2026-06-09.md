# Thirty-Eighth Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** Test the comparative-illusion noisy-channel card against `CAT`.
**Change type:** Protocol-bound evaluation, no graph mutation.

## What Changed

Added:

- `evaluations/protocol-tests/category-measurement-discipline-comparative-illusion-2026-06-09.json`

## Result

`CAT` partly survives `comparative-illusion-noisy-channel-gibson`.

The graph handles the category-analysis side:

- measurement task and task framing can elicit analyst category assignment;
- distributional evidence can warrant category assignment;
- analyst category assignment can influence grammaticality attribution without becoming community
  licensing;
- recoverability can raise reported acceptability without licensing the literal string.

It intentionally does not absorb the noisy-channel side:

- repair-neighbour distance remains an `RNR`/`INR` matter;
- intended-meaning plausibility remains an `MPR` matter;
- category assignment, reported acceptability, and community licensing stay separated.

No score movement follows. This pass is useful because it keeps `CAT`, `INR`, and `MPR`
complementary instead of forcing a premature fused noisy-channel/category graph.
