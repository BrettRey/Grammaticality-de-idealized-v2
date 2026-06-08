# Third Adversarial Pass Synthesis

**Date:** 2026-06-07
**Inputs:** stratified licensing-measurement candidate, third critique, diachronic phenomenon card

## Summary

The stratified candidate survives as a useful synchronic measurement assembly. It keeps the central
constructs apart better than the seeds and first-round candidates: licensing, ideology, correction,
production, acceptability, recoverability, processing, operator value, and attribution no longer
collapse into one another.

But this strength produces the next failure. The graph is static. It can represent a disagreement
between channels at one time slice, but not the way those channels change one another across time.

The next mutation should therefore be dynamic rather than broader.

## What Survived

### 1. Stratification Is Worth Keeping

The second-round graph should not be discarded. It is currently the best representation for
synchronic construct hygiene. In particular, it preserves:

- frequency as evidence, not licensing;
- ideology as pressure, not licensing;
- acceptability as noisy measurement, not grammaticality;
- correction as institutional evidence, not impossibility;
- recoverability as response support, not licensing;
- operator value as a scoped wager, not a universal definition.

### 2. Static Acyclicity Is Now the Binding Constraint

The workbench has reached the point where a larger same-slice DAG mostly adds complexity. The
interesting pressure is feedback:

- production affects later usage;
- usage affects later entrenchment;
- entrenchment affects later production and judgment;
- correction affects later production and attribution;
- public judgments affect later production;
- stabilization changes later licensing and ideology.

The current schema can handle this by using time-sliced nodes and `time_lagged` edges.

### 3. Diachronic Cases Are Not Side Cases

`singular they` is not merely a special historical example. It exposes a general problem for the
workbench: many forms move through lagged interactions among use, ideology, correction, and
community uptake. A representation that cannot model this will overstate the stability of any
single-slice judgment.

### 4. Do Not Add Every Missing Node

The third critique names `measurement_task`, `medium`, and `audience_design` as missing. These are
real omissions, but adding all of them to the static graph would make the candidate less testable.

The next move should be a narrower dynamic mutation:

`dynamic-stratified-feedback-candidate`

Its job is to test whether the workbench can represent feedback legally while preserving the
licensing/ideology/measurement distinctions.

## Score Discipline

No existing score should change. The stratified candidate is more promising than the earlier
candidates, but it has not yet survived the overfitting and feedback critique. Keep all scores zero.

## Next Action

Create `graphs/archive/dynamic-stratified-feedback-candidate.json`.

The candidate should:

- use time-sliced controlled nodes;
- use `time_lagged` edges for feedback;
- keep same-slice edges acyclic;
- model production, usage, entrenchment, licensing, ideology, correction, reported acceptability,
  attribution, and diachronic stabilization;
- leave operator-gap structure to the synchronic stratified candidate unless a later pass shows it
  must be time-indexed too.
