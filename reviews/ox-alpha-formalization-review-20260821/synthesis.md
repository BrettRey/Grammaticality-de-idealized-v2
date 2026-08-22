# Synthesis of the Ox Alpha formalization review

Date: 2026-08-21  
Model: `stealth/ox-alpha` through `orx`  
Runs: one source-only clean-room audit, one review-informed adjudication, and one completion-only addendum

## Bottom line

Ox Alpha substantially corroborates the Codex second opinion. Its adjudication calls the outside-option normalization error the strongest new finding and confirms the double-discounting inconsistency, shared-latent gap, cubic/filter derivation gap, endogenous `psi_rep` problem, multi-node scope limitation, agreement-caption overclaim, and the localized stabilization/maintenance overclaim.

The clean-room pass independently rediscovered most of the structural and implementation defects. That is stronger evidence than the adjudication's agreement because the clean-room prompt did not contain either prior review. It did **not** independently discover the double-discount problem and only approached the exact omission-ratio error through the adjacent `pi approximately G rho*` normalization problem. Those two claims remain locally recomputed and correct, but Ox Alpha's later agreement on them was review-informed.

The overall Codex verdict therefore stands: the state-theory architecture is valuable, while the current state definition, filter, population dynamics, and measurement implementation do not yet form one publication-ready formal explanation. Ox Alpha usefully moderates one point: the paper's strongest overclaim is localized mainly in the conclusion, agreement caption, and tool documentation; the body and limitations section are more candid than the Codex report sometimes suggests.

## Independent clean-room convergence

Ox Alpha independently found:

1. The joint likelihood does not connect rating, confidence, or repair to the advertised shared inclusion latents; only production uses them.
2. The simulator samples a fixed population and can demonstrate epistemic filtering regimes, not population emergence, actuation, or closed-loop repair dynamics.
3. Lean's `ConstraintAlgebra` has no laws, so `Combined` can be order-sensitive and the hard-compatibility consequences remain unproved.
4. Candidate-only `rho*` is incompatible with the production model's outside-option denominator; it gave the equal-weight `1/3` versus `1/2` counterexample for the usage factorization.
5. OBL's dependence on estimated licensing makes the status definition circular or epistemically constituted on its natural reading.
6. Lean's single confidence type has the wrong bounds for decision confidence.
7. The agreement figure's licensing-estimator language conflicts with the paper's own licensing/selection distinction.
8. The paper and engine use different repair links.
9. Per-node positive/negative evidence routing and shared-node credit assignment are absent from the executable.

This convergence is on recomputed artifact facts, not reviewer taste.

## Adjudication of the Codex second opinion

| Codex claim | Ox Alpha adjudication | Synthesis |
| --- | --- | --- |
| Exact omission-ratio equality is mis-normalized | **CONFIRM; strongest new finding** | Confirmed. The code computes the full gated ratio correctly; the paper's candidate-only `rho*` does not. |
| Omission evidence is discounted twice under the natural reading | **CONFIRM** | Confirmed. Define `p_t` as current-window innovation or remove the recursive discount. |
| Joint likelihood is not genuinely shared-latent | **CONFIRM** | Confirmed independently in the clean-room pass. |
| Cubic is not derived from the Beta filter; `psi_rep` is treated as fixed | **CONFIRM**, with candid hedging noted | Confirmed. The paper should state the closure/frozen-flow approximation or call the ODE a stipulated qualitative normal form. |
| Agreement figure treats selection-contaminated usage as licensing | **CONFIRM**, caption-level | Confirmed independently. The counts remain useful production-choice evidence. |
| Multi-node posterior dynamics are absent | **CONFIRM**, largely acknowledged | Confirmed. Scope quantitative claims to unique/single-pivotal cases until joint inference exists. |
| Outside-option informativeness requires extra utility assumptions | **PARTIAL CONFIRM** | The paper states a face-cost/low-utility proviso, but the fixed-utility engine does not create the claimed competitor/outside distinction by outcome identity alone. |
| Lean has additional vacuity and semantic limitations | **CONFIRM** | Confirmed, with several items remaining deliberate scaffold scope restrictions rather than errors. |
| Warrant/world-side language overclaims stabilization and maintenance | **CONFIRM with scope correction** | Correct, but localized: the body and limitations are more careful than the conclusion. |

Ox Alpha also sides with Codex in weakening Claude's `PosteriorStatus.target` objection and refuting internal indexing of `Readout` as the natural provenance fix.

Its classification difference on Claude Findings 1 and 2 is mostly verbal: it calls them CONFIRM rather than STRENGTHEN, while accepting Codex's substantive point that Claude's proposed repairs are unsafe and insufficient.

## New findings worth retaining

### 1. Paper/engine repair-link divergence

`paper/section3.tex:266–275` specifies a logistic repair probability,

```text
sigma(eta_0 + eta_1 (1-G) r(Delta,iota)),
```

whereas `ovmg-tools/js/revised-engine.mjs:327–342` implements a baseline-plus-product link using `1-exp(-divergence*footing)`. Both are monotone, but they are not the same measurement model. Pick one or label the engine explicitly as a qualitative simulation link.

### 2. Credit-assignment machinery is not executable

The paper defines per-node `lambda+_k` and `lambda-_k` at `paper/main.tex:863–878`, but the engine accepts only global scalar `lambdaPos` and `lambdaNeg`. The simulator's default candidates use private singleton nodes, so no shipped scenario exercises compositional sharing or the claimed positive/negative grain asymmetry. This is a model-fidelity limitation, especially for the LBE argument.

### 3. `A*` and negative-weight normalization are underdefined

`A*` occurs at `paper/main.tex:866` without a selection definition elsewhere in the bundled paper. The proportional definition of `lambda-_k` says it ranges over activated nodes but does not explicitly state its normalization or how its scale interacts with effective-count calibration. These are moderate specification gaps, not foundational defects.

### 4. Minor documentation and special-case drift

- The quantitative contract says it separates three things and lists four.
- The executable anomaly drive omits the paper's noise term, a legitimate toy special case that should be labeled.
- Ascription weighting of all evidence streams is not represented in the engine.

## Ox Alpha errors and overreaches

Ox Alpha is useful here but not self-validating.

1. The clean-room report says it found no numerical errors and calls the discounted-update algebra correct, but it missed the paper's all-history `p_t` being reinserted into the recursive discount. Its later confirmation was prompted by the Codex report.
2. The clean-room report treats posterior concentration as an ontic property of the population's evidence history and calls a matched-mean concentration dissociation causally efficacious. In the paper, concentration is explicitly epistemic; the claimed empirical dissociation remains prospective. This cannot be the strongest warranted world-side commitment.
3. It initially calls the conclusion appropriately hedged even though `paper/main.tex:1852` flatly says the dynamics stabilize and the loop maintains. The adjudication corrects this.
4. Its clean-room suggestion to compute OBL from the previous posterior window removes instantaneous circularity but does not remove epistemic constitution. The ontic/estimated OBL split remains the stronger repair.
5. Its adjudication says `decisionConfidence` hardcodes `tau=0.5`; the function is already parameterized as `decisionConfidence(state, threshold = 0.5)`. The default deserves documentation, but this is not a hardcoded limitation.
6. Its engine-level “vacuous assembly” warning is overstated: the simulator validates non-empty assembly node lists, and the lower-level choice engine intentionally has no node representation.
7. It flags the Codex simulation datum `0.01466` as unreproducible under the default 80-step run. Local replay shows it is exactly reproducible with `REVISED_REGIMES.preempted`, 12 steps, seed 1: mean `0.0146583862`, population prevalence `0`. The Codex report should have recorded that configuration; at 80 steps the mean is `0.0022549496`.

These errors support using Ox Alpha as an adversarial reviewer whose claims must be replayed, not as a final judge.

## Revised repair order after Ox Alpha

1. Fix the outside-option normalization in both the exact omission identity and the `pi approximately G rho*` diagnostic.
2. Resolve the double-discount definition.
3. Add a genuine learner-posterior to speaker-inclusion to population-prevalence transition, or consistently demote the cubic and actuation claims.
4. Split ontic OBL from its estimator, with attributable opportunity/preemption and a de-obligatorification condition.
5. State the cubic's closure assumptions and whether `psi_rep` is fixed or state-dependent.
6. Calibrate stabilization/maintenance language to the body's actual proof obligations.
7. Rename or complete the shared-latent likelihood.
8. Align or document the repair link, per-node evidence routing, ascription weighting, and `A*`/lambda normalization.
9. Then harden Lean and make the minor notation, registration, and documentation repairs.

## Lineage and raw material

- Clean-room review: `raw-cleanroom.md`
- Completion-only tail: `raw-cleanroom-addendum.md`
- Review-informed adjudication: `raw-adjudication.md`
- Exact prompts and input bundles: `prompt-*.md`, `input-*.txt`
- Hashes, model identity, token use, elapsed time, and dependence clusters: `manifest.yaml`

The clean-room output reached the configured 18,000-token cap in its last verification-limits bullet. The original capped file is preserved unchanged; only the missing tail was requested in the addendum. The adjudication completed naturally. Total provider cost reported by `orx` was `$0`.
