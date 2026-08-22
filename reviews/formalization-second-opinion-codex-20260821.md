# Second opinion on the OVMG formalization review

Date: 2026-08-21  
Reviewer: Codex, with three independent adjudication lanes, including one clean-room reader who did not read `01-claude-review.md`  
Source bundle: `reviews/formalization-second-opinion-20260821.zip`  
SHA-256: `9993d4cf22fe0213b36463b7dc2cf16141e617a217834aa00bf21ae5350479fb`

## Overall verdict

The first review is directionally good but materially too optimistic. My adjudication is **2 strengthen, 2 confirm, 4 weaken, and 1 refute**. More importantly, it misses several publication-relevant mathematical and implementation problems.

The formal apparatus needs **major revision before publication**. The state-theory decomposition remains promising, but the current state definition, evidence filter, population dynamics, and executable likelihood do not yet constitute one coherent model.

The two central problems are:

1. Section 3 distinguishes speaker inclusion, population prevalence, and posterior estimates, but Section 4 evolves only posterior evidence states and supplies no population-state transition.
2. The supposedly ontic status definition includes saturation, while obligatoriness is defined partly through estimated licensing and posterior concentration.

The Lean and JavaScript artifacts are useful sanity checks. Neither closes these gaps.

## Adjudication of Findings 1–9

| # | Finding | Verdict | Independent basis |
| --- | --- | --- | --- |
| 1 | Missing `z`-dynamics | **STRENGTHEN** | Speaker inclusion `z_{i,t}`, prevalence `theta_t`, and posterior mean `C_t` are distinguished in `paper/section3.tex:123–168`, but Section 4 updates only `a`, `b`, `C`, and `nu` (`paper/main.tex:825–855`). The simulator samples one fixed population and updates only evidence (`ovmg-tools/js/revised-sim.mjs:166–183, 253–327`). |
| 2 | Epistemic obligatoriness inside ontic status | **STRENGTHEN** | `S_t^theta` contains `sat` (`paper/section3.tex:190–214`), while OBL is defined using *estimated* licensing and posterior concentration (`paper/main.tex:1181–1195`). This is both an epistemic leak and a possible circularity. |
| 3 | Missing conditioning and pivotal-node side conditions | **WEAKEN** | The notation table should retain conditioning on `D_t`. The single-node statement needs event-equivalence conditions, but the unique-covering-assembly assumptions in `speaker_status_unique_single_node_iff` (`formalization/OVMG/Core.lean:150–170`) are sufficient rather than necessary. This is a minor clarification. |
| 4 | Confidence bounds | **CONFIRM** | Decision confidence lies in `[1/2,1]` and can equal 1 (`paper/section3.tex:607–620`); Lean's single `Confidence` type permits values below `1/2` and excludes 1 (`formalization/OVMG/Core.lean:194–204`). |
| 5 | Lawless constraint algebra | **CONFIRM** | `ConstraintAlgebra` supplies only `top`, `meet`, and `satisfiable` (`formalization/OVMG/Core.lean:22–30`). Fold order and duplicated constraints can therefore matter. The proposed remedy also needs a neutral-element law and, if duplicates should be inert, idempotence. |
| 6 | `PosteriorStatus.target` contains the ontic target | **WEAKEN** | Bundling latent truth with its estimate in a meta-level proof record does not imply that an analyst knows it (`formalization/OVMG/Core.lean:172–185`). The more serious problem is that semantically different quantities are all unconstrained instances of the same opaque `Score`. |
| 7 | Missing moment identity | **WEAKEN** | The identity in `paper/section3.tex:307–322` is correct and worth testing, but its absence is an enhancement opportunity rather than an inconsistency. Lean first needs properly constrained first- and second-moment types. |
| 8 | Bare `Readout` indexing | **REFUTE as a type defect** | A bare `Readout` can legitimately be the codomain of `Speaker -> Time -> Utterance -> Evidence -> Readout`. Duplicating those indices inside the record would not itself prevent misassignment. Provenance is outside the present scaffold, but `formalization/OVMG/Core.lean:201–204` is not intrinsically mistyped. |
| 9 | Terminology near-misses | **WEAKEN** | Join/meet duality, primitive Lean `obl`, and independent `supplies`/`constraints` deserve documentation. They are scaffold-fidelity limitations rather than theory-level errors (`formalization/OVMG/Core.lean:22–62`). |

## Reweighting the original findings

### Finding 1: the missing population bridge is not a one-sentence repair

The paper defines binary speaker inclusion `z_{i,t}`, population rates `theta_t`, and an analyst or learner posterior whose mean is `C_t` (`paper/section3.tex:123–218`). Section 4 updates only Beta evidence counts and their summaries (`paper/main.tex:825–855`). Nonetheless, the text calls the cubic a population dynamics and defines actuation through movement in `C` and `G` (`paper/main.tex:1069–1122, 1278–1286`).

The original recommendation proposes that a shared posterior mean and population prevalence coincide under homogeneous mean field. That risks undoing the manuscript's central ontic/epistemic separation. A real repair must either define a transition such as

```text
learner posterior at t -> speaker inclusion at t+1 -> population prevalence at t+1
```

while keeping learner, population, and analyst variables separate, or explicitly demote the cubic and actuation discussion to estimator dynamics or a qualitative population-level normal form.

The executable confirms the gap. In a direct run of the bundled preempted regime, target population prevalence stayed exactly `0`, while the posterior mean moved from `0.5` to approximately `0.01466`. This is inference about a fixed population, not population change.

### Finding 2: persistence alone cannot define obligatoriness

The original review correctly identifies the ontic/epistemic leak but underestimates it. Because saturation is a hard conjunct of `S_t^theta`, using an estimated licensing quantity to define OBL can make the truth of status depend on an analyst's evidence state. If “estimated licensing” means the already saturated `G`, the definition also risks circularity.

Replacing concentration with persistent low prevalence is insufficient. A sparse or winnerless zero-marking candidate can remain rare for a long period without its dimension becoming obligatory. A safer architecture would:

- define a saturation-free, time-indexed ontic availability quantity;
- define ontic `OBL_t` from persistent low raw availability plus adequate attributable opportunity or preemption;
- use posterior concentration or a credible upper bound only to identify that world-side predicate; and
- include a revision condition for de-obligatorification.

### Findings 3, 6, 7, 8, and 9

- Finding 3 identifies two worthwhile prose clarifications, not a structural failure. “Single pivotal node” should be stated as equivalence between the complete licensed-route event and the pivotal node event.
- Finding 6 confuses a meta-level representation with an observer's data structure. Renaming or separating the record may improve clarity, but the opaque and unconstrained numerical semantics are the larger problem.
- Finding 7 would be a useful regression theorem after the moment fields are redesigned. It is not required for the current narrow structural scaffold to be logically consistent.
- Finding 8's proposed internal indexing is not the natural type-theoretic fix. If provenance is formalized, the indexed mapping that returns a `Readout` should carry it.
- Finding 9 is best handled as scope documentation: Lean parameterizes obligatoriness and constraint contribution rather than deriving them.

## Independent findings missed by the first review

### 1. The displayed omission-ratio equality is wrong

The paper defines candidate-only counterfactual choice as

```text
rho*(x) = exp(U_x) / sum(candidate weights)
```

without the outside option (`paper/main.tex:782–790`). The actual production model includes outside weight in the denominator (`paper/main.tex:792–800`). It then asserts at `paper/main.tex:918–929` that

```text
P(y | Z_x = 1) / P(y | Z_x = 0) = 1 - g rho*(x).
```

Let

```text
D0 = outside weight + sum(weights of active non-target candidates).
```

The correct mixture ratio is

```text
P(y | H1) / P(y | H0) = 1 - g * w_x / (D0 + w_x).
```

The subtracted term is the target's mass in the full gated distribution, not candidate-only `rho*`.

With target, competitor, and outside weights all equal to 1, the exact ratio is `2/3`. The manuscript's expression gives `1/2`. The bundled engine correctly returns the corresponding LLR `log(3/2) = 0.405465`. Therefore the first review's statement that the approximation was numerically confirmed is false under the written definitions.

Under the stated fixed-utility softmax, every unchanged non-target outcome, including the outside option, receives the same normalization ratio. The claim at `paper/main.tex:940–948` that outside-option choices are nearly uninformative requires an explicit hypothesis-dependent utility or face-cost model. Outcome identity alone does not produce that difference.

### 2. Omission evidence is naturally read as discounted twice

The recurrence at `paper/main.tex:842–847` discounts accumulated evidence and then adds `p_t`. But `p_t` is defined at `paper/main.tex:908–913` as an all-history sum already weighted by `delta_m^(t-t_i)`.

Under that reading, one unit omission at time 0 produces `E_1 = 1`, but with no new evidence the next step becomes `E_2 = 2 delta_m`, rather than the intended `delta_m`. The JavaScript implements the sensible current-batch recurrence. The paper should either:

- define `p_t` as current-window innovation without its own historical discount; or
- remove the recursive discount and use the closed-form historical sum.

### 3. The cubic is not derived from the stated bounded-memory filter

The Beta filter evolves both mean and concentration and reverts toward a fixed baseline prior (`paper/main.tex:825–855, 1257–1265`). The cubic at `paper/main.tex:1099–1122` has no concentration or prior term and makes its endpoints absorbing. It is a valid stipulated normal form, but the text says that replacing endogenous streams by their expectations “yields” it (`paper/main.tex:1079–1086`) without supplying the approximation.

There is a second seam: `psi_rep` is defined through `P(mis-set)` (`paper/main.tex:977–983`), which will ordinarily depend on the current community state, but the displayed fixed point treats it as a constant coefficient. The manuscript should state a frozen-flow assumption, derive `psi_rep(C)`, or retype the cubic as an explicitly qualitative ontic normal form.

### 4. The executable joint likelihood is not shared-latent for ratings and repair

The contract says production, repair, ratings, confidence, and cues are conditionally connected through shared inclusion states (`ovmg-tools/quantitative-model-contract.md:134–156`). In the implementation:

- `statusEstimate`, `decisionConfidence`, and `evidenceConfidence` are supplied as observation fields (`ovmg-tools/js/joint-likelihood.mjs:263–315`);
- repair uses supplied `misSet`, divergence, and dissonance variables rather than latent inclusion (`ovmg-tools/js/joint-likelihood.mjs:318–343`); and
- only production uses the speaker's inclusion vector (`ovmg-tools/js/joint-likelihood.mjs:346–376`).

Toggling latent inclusion while holding the supplied read-out fixed left repair, rating, and confidence likelihood components unchanged. Those channels therefore cannot inform inclusion in the current implementation. It should be called a conditional scoring or likelihood shell unless the read-outs and repair predictors are derived from the latent state.

### 5. Multi-node status has no joint posterior dynamics

Section 3 correctly notes that marginal node rates do not determine multi-node assembly prevalence and introduces latent lects as one remedy (`paper/section3.tex:134–168`). Section 4 nevertheless updates only marginal per-node Betas. It supplies no posterior transition for lect weights, within-lect dependence, or the union over alternative assemblies. The executable contract acknowledges this limitation.

Formal quantitative predictions should remain restricted to unique or single-pivotal-node cases until joint assembly inference is supplied.

### 6. The agreement figure treats production choice as licensing

The measurement discussion first says corpus rates combine availability and selection and that `rho*` must be normed independently (`paper/section3.tex:674–692`). It then describes plural-agreement share as a licensing estimate read directly from usage per opportunity (`paper/section3.tex:701–716`). Those counts establish a production-choice asymmetry, not population inclusion prevalence, unless selection, repeated speakers, and opportunity sampling are separately modeled.

### 7. Additional Lean limitations

These are moderate fidelity limitations rather than compile failures:

- `PopulationStatus` and `PosteriorStatus` use one arbitrary `Score` type for prevalence, mean, concentration, and uncertainties.
- An assembly with an empty node list satisfies `LicensedNodes` vacuously.
- `Assembly.nodes` and `Assembly.constraints` are independent lists with no coherence invariant.
- The file proves event-level consequences but not population reduction or posterior semantics.
- `obl` is a primitive parameter rather than the derived relation advertised in the paper.

## Projectibility-first audit

| Check | Status | Evidence |
| --- | --- | --- |
| Declaration | **YELLOW** | Many concrete projections are named, but bearer, population, timescale, and tolerance are distributed rather than stated in complete declarations. |
| Inquiry/use, warrant plan, revision rule | **YELLOW** | Strong norming, registration, and falsifier discipline; much of the actual warrant plan remains prospective. |
| Non-trivial projection | **GREEN** | Satiation, framing, L2 transfer, repair, transmission, and diachronic predictions extend beyond membership diagnostics. |
| Warrant versus world-side claims | **RED** | A stipulated and provisional normal form is reported as evidence that stabilization and maintenance have been reached (`paper/main.tex:1347–1354`). |
| World-side order | **GREEN** | Stability, maintenance, and controller status are verbally distinguished; stability is not used to infer causal ordering. |
| Stabilizer versus controller | **GREEN** | Controller status is conditional on an intervention signature and has a clear falsifier (`paper/main.tex:985–1008`). |
| Level and mereology | **YELLOW** | Speaker `z`, population `theta`, and posterior `C` are distinguished in Section 3 but conflated by the dynamics. |
| Scope and field-relativity | **GREEN** | Context, niche, comparanda, and non-transfer restrictions are explicit. |
| Prospective revision | **GREEN** | Post-hoc repartitioning and renorming are explicitly counted against the framework. |
| Positioning and conclusion | **YELLOW** | Projection is central, but the conclusion says the dynamics stabilize and the loop maintains before those bridges are demonstrated (`paper/main.tex:1844–1856`). |

Projectibility is **structural, not decorative**. The anti-vacuity discipline and non-trivial predictions are genuine strengths. The overreach concerns warrant. The included formal evidence reaches, at most, **conditional model-level stability or a candidate stabilizing dynamics**. It does not demonstrate population stability, effective maintenance, or corrective control.

| True premise | Unearned therefore | Missing bridge | Better reading |
| --- | --- | --- | --- |
| The stipulated cubic has endpoint attractors. | Population licensing stabilizes bimodally. | A derivation from `z/theta` transitions and the bounded-memory stochastic system. | The cubic is a candidate normal form. |
| Repair changes the evidence balance. | The production-repair loop maintains the profile. | A removal or perturbation counterfactual showing that the ontic profile fragments without repair. | Repair is a candidate maintenance mechanism. |
| Zero-marking has concentrated low estimated licensing. | The dimension is ontically obligatory inside `S^theta`. | An independent, time-indexed world-side predicate tracked by the estimator. | Separate OBL truth from OBL identification. |

## Assessment of the original recommendations

The original “one prose session, then one Lean session” estimate is too light. The proposed order puts secondary Lean improvements before omitted mathematical and executable repairs.

### Recommended order

1. Separate learner posterior, analyst estimate, speaker inclusion, and population prevalence; add a transition law or demote the population-dynamics claims.
2. Split ontic OBL from its estimator and incorporate attributable opportunity and preemption, not persistence alone.
3. Fix the exact LLR normalization and the double-discounting notation.
4. State the approximation under which the cubic follows, including prior and concentration assumptions and whether `psi_rep` is fixed or depends on `C`.
5. Make the likelihood genuinely shared-latent, or rename its scope; restrict unsupported multi-node claims.
6. Recalibrate stabilization and maintenance language and reframe the agreement figure as production evidence.
7. Harden Lean: lawful constraint combination, separate confidence types, nonempty and coherent assembly invariants, and meaningful numerical posterior constraints.
8. Finish with the minor notation, event-equivalence, registration, and documentation fixes.

The original recommendation to identify shared `C = theta` is potentially harmful because it erases the separation the revision was intended to secure. Replacing concentration with persistence in OBL is likewise unsafe without opportunity and preemption conditions.

The confidence split and constraint-algebra improvements should be retained. The moment theorem should wait until the numerical record is redesigned. Replacing `PosteriorStatus.target` is lower priority, and internal indexing of `Readout` should not be the default fix.

Projection-range typing, inventory inference, and section reordering need not be done now. A stationary-distribution theorem need not live in Lean, but it cannot be bypassed if the manuscript retains unconditional emergence and maintenance claims.

## Verification and limits

Verified locally:

- ZIP integrity;
- packaged `main.tex`, `section3.tex`, and `Core.lean` match the corresponding current workspace files by hash;
- the Lean scaffold builds under its pinned Lean 4.31.0 toolchain;
- all three JavaScript modules import;
- targeted engine, simulator, and likelihood smoke tests;
- the exact outside-option LLR counterexample;
- the Beta variance decomposition, decision threshold, cubic fixed point, and plotted Beta calculations already listed in the handoff.

For absence claims, all bundled `.tex`, `.lean`, `.md`, and `.mjs` files were searched for `z`, `theta`, `transition`, `inclusion`, `OBL`, `obligat*`, `concentration`, and the relevant constraint-algebra laws.

Not independently verified:

- external citations and empirical source claims;
- the underlying agreement dataset;
- a complete LaTeX build from the bundle, which omits repository-level bibliography and figure dependencies;
- a full JavaScript regression suite, because no test suite, package manifest, or Makefile was included.

No manuscript, Lean, JavaScript, or project-instruction source was changed during this review.
