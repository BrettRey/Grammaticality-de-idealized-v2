# Critique: stratified-licensing-measurement-candidate

**Target:** `graphs/archive/stratified-licensing-measurement-candidate.json`
**Family:** stratified-licensing-measurement
**Pass:** third adversarial pass, 2026-06-07

## 1. Strongest Counterexample

`singular they` is the strongest attack. The candidate can represent a synchronic split among usage,
licensing, standard-language ideology, correction, reported acceptability, and grammaticality
attribution. But the phenomenon is historical and feedback-driven: production, usage, institutional
correction, public acceptability, and community licensing change each other over time.

The graph has no `diachronic_stabilization` node and no time-indexed feedback. It can say that older
condemnation and current licensing are separate constructs, but it cannot represent the route from
longstanding use through changing correction regimes to later institutional acceptance.

## 2. Category Mistake

The candidate risks treating a synchronic measurement assembly as a general explanatory model. Its
main strength is construct hygiene at a single slice. Its main weakness is that it handles feedback
only by omitting it.

That matters because several target cases are not just cross-channel conflicts; they are
cross-channel conflicts with histories. A static DAG can keep constructs separate, but it cannot
explain stabilization, backlash, normative lag, or delayed production change.

## 3. Most Damaging Missing Node

`diachronic_stabilization`.

Without it, the graph cannot represent whether a form is becoming stable, historically stable but
recently recognized, or newly spreading under institutional pressure.

Secondary missing nodes:

- `entrenchment`
- `measurement_task`
- `medium`
- `audience_design`

These do not all need to enter the next mutation, but their absence shows that the current graph is
a useful assembly, not a final representation.

## 4. Most Suspicious Edge

`community_licensing -> reported_acceptability`.

The edge is typed as measurement and the rationale marks acceptability as noisy, which is better
than a direct synonym. Still, once the graph also gives `reported_acceptability` many causal parents,
the measurement relation becomes ambiguous. Is reported acceptability measuring licensing, ideology,
processing, recoverability, task framing, or their mixture?

The graph needs either an explicit measurement-task layer or a dynamic separation where acceptability
at one time slice can influence later production without being treated as transparent evidence of
licensing.

## 5. Minimal Mutation

Create a time-indexed mutation rather than adding more same-slice nodes.

The mutation should include:

- `production_probability_t`
- `usage_frequency_t1`
- `entrenchment_t1`
- `community_licensing_t1`
- `standard_language_ideology_t1`
- `metalinguistic_condemnation_t1`
- `editorial_correction_probability_t1`
- `reported_acceptability_t1`
- `diachronic_stabilization_t2`
- `production_probability_t2`

It should use `time_lagged` edges for feedback, especially:

- production at time `t` affecting usage at `t1`;
- licensing, entrenchment, correction, and acceptability at `t1` affecting production at `t2`;
- usage, licensing, and correction at `t1` affecting diachronic stabilization at `t2`.

## 6. Score-Readiness Judgment

`not ready`.

The candidate is the best synchronic construct-hygiene assembly so far, but it should not receive a
non-zero general score until a separate dynamic pass shows whether the same distinctions survive
feedback and historical change.
