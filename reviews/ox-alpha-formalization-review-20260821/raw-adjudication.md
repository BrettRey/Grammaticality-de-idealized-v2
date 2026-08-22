# Adjudication report: OVMG formal apparatus, second-opinion review

Adjudicator role: refutation-first recomputation from the bundled sources only. Line references are to the files as packaged; where a line number is uncertain I anchor to an equation label, quotation, or function name that locates the passage uniquely.

---

## 1. Overall verdict on the two reviews

**The Claude review is a competent structural audit with one false numerical verification and two remedies that would damage the architecture if applied as worded. The Codex review is stronger on mathematics and implementation fidelity but overcorrects on two Lean findings and slightly overstates the novelty of what it found.** Neither review is safe to follow wholesale.

Specifically:

- Claude's Findings 1, 2, 4, 5 are real and correctly weighted. Its verification line "Omission LLR small-mass approximation ℓ ≈ g·ρ\* … Confirmed to first order" (`01-claude-review.md`, Numerical verifications) is **false as stated**: the first-order coefficient itself is mis-normalized (§3 below, counterexample). Its recommended fix for Finding 1, if applied verbatim, erases the ontic/epistemic distinction the 2026-07-10 revision was performed to secure; its recommended fix for Finding 6 solves a non-problem.
- Codex's three most important contributions — the omission-ratio normalization error, the double-discounting ambiguity, and the shared-latent gap in `joint-likelihood.mjs` — are all **correct and missed by Claude**, and they outrank most of Claude's Lean-level findings in publication relevance. Codex's REFUTE on Finding 8 is correct. Its WEAKEN on Finding 6 is correct. Its treatment of the cubic and of OBL is right in substance though the paper hedges more than Codex credits.
- The paper itself is more candid than either review sometimes allows: the bounded-memory stationary distribution is explicitly a conjecture with a stated outside-option condition (`main.tex`, §emergent-categoricality: "That stationary distribution claim is a formal target rather than a theorem here, and it requires an explicit condition that the outside option's fixed utility does not dominate the candidate set"), and the Limitations section repeats the provisional status. The residual overclaim is concentrated in the Conclusion and in one figure caption, not distributed through the text.

---

## 2. Adjudication of Claude Findings 1–9

| # | Finding | Verdict | Basis (one line) |
|---|---|---|---|
| 1 | Missing z-dynamics / unclosed epistemic-ontic loop | **CONFIRM** (remedy must be amended) | Section 3 distinguishes z, θ, Ŝ (`section3.tex`, Objects and eqs. Gtheta/Gt); Section 4 updates only (a,b) and defines actuation via rising C_{t+1}, G_{t+1} (`main.tex`, §actuation); `revised-sim.mjs` draws the population once (`makePopulation`) and never mutates it. |
| 2 | Epistemic leak into ontic status via derived OBL | **CONFIRM**, with the circularity horn Codex adds | `sat(A,c)` is a conjunct of S^θ (`section3.tex`, eq. Gtheta); OBL is defined via "estimated licensing below a tolerance ε with concentration above ν_min" (`main.tex`, §derived-obligatoriness block quote); the text never says whose estimate. |
| 3 | Table cell missing conditioning on D_t; pivotal-node side conditions | **CONFIRM** (minor, as Claude labeled it) | Table `tab:notation-bridge` row reads "Ŝ_t = E[S_t^θ]" without "|D_t"; the prose identity S^θ = θ(κ,c) needs the uniqueness/def/sat hypotheses that `Core.lean`, `speaker_status_unique_single_node_iff`, makes explicit. |
| 4 | `Confidence` mis-bounds decision confidence | **CONFIRM** | Φ^dec = max{P(S≥τ), P(S<τ)} ∈ [½,1] with 1 attainable under the paper's degenerate-posterior convention (`section3.tex`, §feeling-new: "effectively degenerate… by modelling convention"; worked examples write Φ ≈ 1); `Core.lean` `Confidence` is `0 ≤ val < 1`. |
| 5 | Lawless constraint algebra | **CONFIRM** | `ConstraintAlgebra` (`Core.lean`:22–30) has no laws; `Combined` foldl is order-sensitive; empty `constraints` reduces Def to `satisfiable top`, unguaranteed; clash-dooms-assembly and permutation-invariance are unprovable. |
| 6 | `PosteriorStatus.target` embeds the ontic target | **WEAKEN** | Bundling truth with estimate in a meta-level proof record is legitimate and standard; the real defects are the nominal character of the distinction (no theorem ties `prevalence` to `SpeakerStatus`) and the four unconstrained opaque `Score` fields. |
| 7 | Moment identity unproved | **WEAKEN** | U_epi + U_het = C(1−C) is correct pure algebra (epi = m₂−m₁², het = m₁−m₂); its absence is a missed regression test, not an inconsistency. |
| 8 | Bare `Readout` indexing | **REFUTE** (as a defect) | A bare record as codomain of `Speaker → Time → Utterance → Evidence → Readout` carries provenance in the function type; duplicating indices inside the record would not prevent misassignment without dependent plumbing far beyond this scaffold's declared scope. |
| 9 | Terminology near-misses (join/meet, primitive `obl`, independent `supplies`) | **CONFIRM** (documentation-grade, as characterized) | All three observations check out against `Core.lean`; none is a theory-level error. |

---

## 3. Detailed reweighting and refutations

**Finding 1 — CONFIRM, but Claude's remedy is dangerous as worded.** The gap is real: search across `main.tex` §update through §actuation, `Core.lean`, and `revised-sim.mjs` finds no rule mapping a speaker's posterior to that speaker's own inclusion state; the simulator's `makePopulation` is called once and `population` is never reassigned. Claude's proposed sentence — "under the homogeneous mean-field the shared posterior mean and the population licensing rate coincide, and that shared quantity is what the cubic evolves" — is acceptable **only if** framed as an explicit mean-field closure approximation under which θ_t and the common posterior mean coincide to O(1/N) error, with the four quantities (learner posterior, analyst estimate, inclusion vector, population rate) kept typographically distinct. Stated as a coincidence identity, it reinstates exactly the conflation the 2026-07-10 decision log entry ("preserves conventional status without making it depend on the analyst's evidence state") removed. Codex's demand for an actual transition law, or else demotion of the cubic to a qualitative normal form, is the safer default; the paper already half-takes the demotion route ("I use that ODE for qualitative fixed-point and comparative-statics arguments") and should finish it.

**Finding 2 — CONFIRM, and the circularity horn is live.** The natural reading of "estimated licensing" in the OBL definition is the analyst's G_t — and G_t is the posterior mean of S^θ, one of whose conjuncts is sat(A,c), which is defined via OBL(c,A). Under that reading the definition is circular, not merely leaky. The charitable reading — the concentration is the speakers', a world-side fact about the community's posterior dispersion — is available but nowhere stated; I searched the §derived-obligatoriness block and §objects for "whose", "speaker", "analyst", "posterior of" and found no attribution. Claude's "persistence replaces concentration" alternative is insufficient on its own (Codex is right): a starved or winnerless zero-marking candidate can stay rare indefinitely without its dimension becoming obligatory. The correct repair needs persistent low **raw availability** (θ of the zero-marking assembly, not G) **plus** an attributable-opportunity/preemption condition, with the posterior version retained as identification only.

**Finding 4 — CONFIRM.** Recomputation: for any posterior, max{p, 1−p} ≥ ½; equality 1 requires a degenerate posterior, which the paper grants "by modelling convention" for structural/compatibility failures and uses in every worked example writing Φ ≈ 1. Lean's single type therefore both under- and over-constrains. Split is required; Codex's CONFIRM agrees.

**Finding 5 — CONFIRM.** Verified by inspection of `Core.lean`:22–30 and the `Combined` foldl. Codex's additions (neutral-element law is implied by `top` + assoc; idempotence if duplicated constraints should be inert) are reasonable refinements of the same fix, not objections.

**Finding 6 — WEAKEN ( siding with Codex against Claude).** In a proof assistant, a record carrying both the true prevalence and an estimate is the normal shape of any statement about estimation error; constructing it does not commit the analyst to knowing the truth. Claude's "relocated inside a record" objection confuses object language with meta language. What survives: (i) no theorem connects `PopulationStatus.prevalence` to `SpeakerStatus`, so the distinction is presently typal decoration; (ii) all five numeric fields are unconstrained instances of one opaque `Score`, so the types cannot catch, e.g., a concentration stored in the mean slot. Repair: add field constraints and a linking definitional theorem; do not replace `target` with an index (that would make error statements inexpressible).

**Finding 7 — WEAKEN.** The identity is worth one tactic block as a typo-guard, but nothing in the scaffold is *wrong* for lacking it. Priority below the confidence split and algebra laws.

**Finding 8 — REFUTE.** Codex's refutation is correct. Internal index fields do not deliver bearer-safety; only indexed function types (or Σ-types pairing a read-out with a proof of provenance) do, and the latter is out of scope for a scaffold whose README declares it a narrow structural check. Claude's underlying observation — that the anti-mereology discipline lives in the paper's subscripting, not the Lean types — is true but is a scope note, not a defect.

**Claude's numerical verification of the omission approximation — REFUTED.** See next section; this is the largest single error in the Claude review.

---

## 4. Ranked adjudication of Codex's additional findings

| Rank | Codex claim | Verdict | Basis |
|---|---|---|---|
| 1 | Omission-ratio equality wrong (normalization mismatch) | **CONFIRM — the strongest new finding** | Recomputed below; Claude's contrary "confirmation" is refuted. |
| 2 | Double discounting of omission evidence | **CONFIRM** | Arithmetic below; the paper's two definitions cannot both hold. |
| 3 | Joint likelihood not shared-latent | **CONFIRM** (documentation overclaim in the contract) | `readoutLogLikelihood` consumes supplied `statusEstimate`/confidences; `repairLogLikelihood` consumes supplied `misSet`/`divergence`; only production touches `speaker.inclusion`. |
| 4 | Cubic not derived from the stated filter; ψ_rep treated as fixed | **CONFIRM** (partially self-hedged in the paper) | No derivation between the discrete filter and eq. cubic-normal-form; P(mis-set) is endogenous yet enters the fixed point as a constant. |
| 5 | Agreement figure caption treats production choice as licensing | **CONFIRM** (caption-level overclaim) | Caption of `fig:agr-projection`: "an estimator of licensing"; both agreement variants are licensed, so the share estimates selection. |
| 6 | Multi-node posterior dynamics absent | **CONFIRM** (scope limitation, largely acknowledged) | Section 4 updates marginal Betas only; no lect-weight or joint-inclusion transition anywhere (searched: "lect", "joint", "transition", "π_ℓ" in §dynamics). |
| 7 | Outside-option informativeness needs hypothesis-dependent utilities | **PARTIAL CONFIRM** | The paper *does* state the proviso ("provided x's counterfactual utility is low or the production rule assigns a face cost…"), so this is a documented conditional, not an undocumented gap; but the proviso does heavy lifting and the fixed-utility engine violates it except at extreme utility gaps. |
| 8 | Lean limitations (opaque Score, vacuous LicensedNodes, incoherent lists, primitive obl) | **CONFIRM** | All verified by inspection; `LicensedNodes` over `[]` is vacuously true; `nodes`/`constraints` have no coherence invariant. |
| 9 | Warrant-vs-world-side RED; conclusion overclaims stabilization/maintenance | **CONFIRM with a scope correction** | The Conclusion asserts "Bimodal dynamics stabilize the profile, and the production–repair loop maintains it" flatly; the body and Limitations are more careful. Overclaim is real but localized. |

**Recomputation of Rank 1.** The paper defines ρ\* over candidates only (`main.tex`, §usage: softmax with denominator Σ_{x'∈V\*}); the production model's denominator includes the outside weight (`main.tex`, §usage π_t equation). For an in-repertoire competitor outcome y ≠ x, available under both hypotheses, with D₀ = w_out + Σ_{active non-target} w_j:

  P(y|Z=1)/P(y|Z=0) = [a_y w_y/(D₀+w_x)] / [a_y w_y/D₀] = **1 − w_x/(D₀+w_x)**,

i.e., 1 minus the target's mass in the *full* gated distribution — not 1 − g·ρ\*(x). Counterexample: target, competitor, and outside weights all 1 → exact ratio 2/3; the paper's expression gives 1/2. Consequently the paper's first-order claim that the old N·ρ\* mass is "the first-order high-confidence competitor approximation" is wrong whenever the outside option carries non-negligible weight — which is precisely the defective-cell and avoidance regimes the distinction exists for. The bundled engine computes the correct quantity (`omissionEvidenceFromChoice` builds both gated distributions and takes the log ratio), so the code is right and the paper text is wrong. Claude's "confirmed to first order" is refuted: the first-order coefficient, not merely the log expansion, is mis-normalized.

Corollary the reviews only gesture at: the same normalization inconsistency infects the diagnostic factorization π ≈ G·ρ\* (single-node case: π = C·w_x/(w_out + C·w_x + …), which is C times a *full-denominator* choice probability, not C·ρ\*). The fix is one definition: either redefine ρ\* over the full set including ⊥, or introduce ρ̃\* = w_x/(D₀+w_x) and use it in both places.

**Recomputation of Rank 2.** The update discounts accumulated evidence and then adds p_t (`main.tex`, the align block after "Discounting applies to accumulated evidence"); p_t^± is defined as an all-history sum already carrying δ^{t−t_i} (`main.tex`, eq. preemption-mass). One unit omission at t=0: E₁ = δ·0 + δ = δ; with no new evidence, E₂ = δ·δ + δ² = **2δ²**, not the intended δ². The definitions are jointly inconsistent; exactly one discount application must be removed. The JavaScript resolves this as current-batch innovation (`revised-sim.mjs` accumulates per-step evidence, then `updateEvidence` discounts), so the code embodies one resolution the paper's text does not state. Classification: ambiguity in the paper, resolved differently in the artifact — a documentation defect with mathematical consequences.

**Rank 3 detail.** The contract promises channels "conditionally related through shared latent inclusion states and utilities" (`quantitative-model-contract.md`, Fit-Ready Joint Likelihood section). In `joint-likelihood.mjs`, toggling latent inclusion leaves the repair, rating, and confidence components unchanged because their predictors arrive via `observation`. The code's own header is candid ("conditional joint log likelihood"); the contract's "shared-latent" language and the README's framing overclaim. Verdict: rename the artifact's scope or derive the read-outs from latents.

**Rank 4 detail.** Two seams, both real. (a) "Replacing those endogenous evidence streams by their expectations yields the cubic drift" (`main.tex`, §open-loop/closed-loop block) is asserted, not derived; no moment-closure or separation-of-timescales argument appears (searched: "expectation", "approximation", "derive", "separation" around the cubic). (b) ψ_rep(n) = N_t·P(mis-set)·r(Δ,ι) (`main.tex`, eq. repair-flow) contains P(mis-set), which on the paper's own account scales with the deviant population share; the fixed point C‡ = (β+χψ)/(α+2χψ) treats χψ as constant. The paper never states a frozen-flow assumption (searched: "frozen", "fixed coefficient", "constant", "ψ" in §emergent-categoricality). Mitigating: the paper explicitly confines the ODE to qualitative use and concedes the concentration dynamics are absent. Verdict: a genuine derivation gap, softened by candid hedging; the repair is to state the frozen-flow assumption or retype the cubic as an explicitly qualitative ontic normal form.

**Rank 5 detail.** The surrounding text is careful — §measurement-C and §identification-c insist corpus rates conflate availability and selection and that ρ\* be normed independently — but the figure caption says "how a licensing estimate can be read off usage per opportunity." For collective-partitive agreement, both variants are grammatical (the paper's own "soft alternation" category), so the plural share is a selection statistic. The counts remain valuable as an audit trail and as evidence against a surface-head-only baseline; the caption's word "licensing" should become "production-choice asymmetry," with a licensing reading licensed only by an independent ρ\* norming that is not supplied.

---

## 5. Findings both reviews missed

Ranked by importance:

1. **Engine/paper divergence in the repair link.** The paper specifies Pr(repair) = σ(η₀ + η₁(1−G)·r(Δ,ι)) — a logistic link (`section3.tex`, §projectible-use). The engine implements `repairProbability = baseline + (1−baseline)·gain·(1−statusEstimate)·(1−exp(−divergence·footing))` — a linear-saturating form with no logistic and no η structure (`revised-engine.mjs`). Neither review flags this fidelity break. It matters because the controller claim's intervention signature is defined on the paper's link.
2. **λ⁻ is underived and scale-free.** λ⁻_κ ∝ |∂log P(D_t|θ_t(κ,c))/∂θ| (`main.tex`, §update) is a score-like sensitivity with no specified normalization, no stated how-it-composes-with-per-token-streams rule, and no calibration path distinct from the generic effective-count caveat. Claude and Codex both pass over it.
3. **λ⁺ references an undefined argmax.** λ⁺_κ = P(κ ∈ A\*|x,c,D_t) presupposes a designated covering assembly A\*; the selection rule for A\* (best assembly? sampled?) is never given.
4. **Codex's simulator datum does not reproduce.** Codex reports the preempted-regime posterior mean moving 0.5 → 0.01466. From the bundled parameters (utilities [0,0], outside −5, 8 opportunities/step, every occasion an omission with ℓ ≈ log 2 ≈ 0.693), the mean after t steps is 1/(2+5.55t), giving ≈0.0022 at t=80 and ≈0.0146 only at t≈12. The qualitative point survives; the specific number is unexplained and should not be quoted without a reproducible configuration.
5. **`decisionConfidence` hardcodes τ = 0.5** (`revised-engine.mjs` default), while the paper insists τ(c) is situation-indexed and must not be fit to judgments. Minor, but it is exactly the kind of silent default the identification discipline forbids.
6. **The joint-likelihood's anomaly drive omits the ε_i noise term** and floors identically; harmless, but the read-out channel fitted is a noiseless special case of the paper's M equation.
7. **Vacuous-assembly hazard is reachable, not merely theoretical:** `defaultCandidateNodeIndices` gives every candidate the singleton node list, but a user-supplied empty list is rejected only by `validateAssemblyNodeIndices`'s non-empty check in the simulator — the *engine-level* `gatedChoiceProbabilities` has no node concept at all, so the vacuous-licensing case lives one abstraction layer away from silent use.

---

## 6. Projectibility, warrant, and world-side commitment

Codex's traffic-light table is broadly right; my adjustments:

- **Warrant vs. world-side: RED is correct but localized.** The body repeatedly grades its claims (stabilization / maintenance / candidate controller; "formal target rather than a theorem"; the Limitations section's "mathematical candour" paragraph). The Conclusion, however, states "Bimodal dynamics stabilize the profile, and the production–repair loop maintains it" without the grading apparatus, and the abstract's "It earns its keep by projection" list is prospective. The repair is editorial: import the body's hedges into the Conclusion; no result needs retraction.
- **Declaration YELLOW is fair** but understates the identification subsection, which is unusually strong (registered partitions, pre-normed ρ\*, reassignment counting against the framework). The genuine declaration gap is the construction inventory H itself — Claude's grain-registration point, which I endorse as the one brief-import worth taking.
- **Controller claim:** properly conditional in both text and code (`repairProbability` is a helper, not a claim; the falsifier — repair tracking social indexing rather than Δ — is stated twice). GREEN stands.
- **World-side commitment overall:** the paper commits to less than Codex's RED implies. What it actually claims as established is: the state architecture, the variance decomposition, the LLR omission rule (modulo the normalization bug), and hyperbolic open-loop decay. Bimodality, obligatoriness-as-derived, moribundity-dispersion, and control are explicitly conditional or conjectural. The warranted reading is "candidate stabilizing dynamics with an explicit proof obligation," which is what the Limitations section says and what the Conclusion should say.

---

## 7. Final ordered repair plan

Merging both recommendation sets; items 1–4 are paper-level mathematics and precede all Lean work.

1. **Fix the omission normalization.** Redefine the counterfactual choice term over the full gated set (or add ρ̃\* = w_x/(D₀+w_x)); restate the first-order reduction of N·ρ\* with its validity condition (negligible outside weight); propagate the corrected quantity into the π ≈ G·ρ\* diagnostic. *Solves the wrong problem if done by redefining ρ\* silently mid-paper — do it at the definition site.*
2. **Resolve the double discount.** Declare p_t a current-window innovation (matching the code) and delete δ^{t−t_i} from eq. preemption-mass, or switch the update to the closed-form historical sum. One sentence, but it changes every quantitative dispersion claim's calibration.
3. **Close or demote the population bridge.** Preferred: state the missing transition (posterior → own inclusion → next θ) as an explicit stochastic law, keeping learner/population/analyst variables distinct, with the homogeneous mean-field coincidence stated as an O(1/N) closure approximation, never an identity. Fallback: demote the cubic and actuation prose to qualitative normal-form status throughout, including the Conclusion. *Claude's original wording is rejected as consensus-erasing.*
4. **Re-found OBL ontically without circularity.** Ontic predicate: every zero-marking assembly in a d-at-issue niche has raw availability θ below ε persistently across a registered window **and** the niche carries attributable opportunity/preemption pressure (ruling out starvation and winnerless cases, per Codex); the estimated/posterior version follows one sentence later as identification. Add a de-obligatorification condition. Never define OBL through G.
5. **State the cubic's standing.** Frozen-flow assumption on ψ_rep, or an explicit ψ_rep(C) with the resulting fixed-point analysis, or retype the equation as a stipulated qualitative normal form; add the outside-option-domination condition next to the equation, not pages earlier.
6. **Recalibrate warrant language.** Conclusion and abstract brought in line with the body's grading; figure caption changed from "licensing estimate" to production-choice evidence with the licensing reading made conditional on ρ\* norming.
7. **Rename or complete the joint likelihood.** Either derive read-outs and repair predictors from latent inclusion (making it genuinely shared-latent) or relabel it a conditional scoring shell in contract and README.
8. **Lean session (now safely last):** split `Confidence` into EvidenceConfidence [0,1) and DecisionConfidence [½,1]; add constraint-algebra laws (assoc/comm, satisfiable-top, antitone satisfiability; idempotence if duplicates should be inert) and prove clash-dooms-assembly plus permutation-invariance of Def; constrain `PosteriorStatus` fields and add the moment identity as a regression theorem; document join/meet duality, primitive `obl`, independent `supplies`; README wording ("types the distinction"). *Rejected from Claude's list:* replacing `PosteriorStatus.target` with an index (makes error statements inexpressible; meta-level confusion) and internal `Readout` indexing (wrong layer for provenance).
9. **Registration sentence** putting inventory/template-typing choices under the same discipline as c, n, ρ\*, τ (Claude's one brief-import; cheap and closes a real gap).
10. **Engine hygiene:** align `repairProbability` with the paper's logistic link or annotate the divergence; parameterize the decision-confidence threshold; document the current-batch discount semantics next to the paper equation it implements.

---

## 8. What Lean and JavaScript can and cannot verify

**Lean (as built) can verify:** unfolding lemmas over a fixed inventory and algebra (coverage necessity, unsatisfiability and unsaturation blocking status, the single-node reduction under explicitly stated uniqueness/def/sat hypotheses); bound-typing of read-outs once split; the moment identity once fields are constrained. These are genuine but shallow: they certify that the section-3 *shape* is coherent, not that any linguistic analysis supplies the right inventory, constraints, or obligatoriness relation (README concedes this).

**Lean cannot verify, and should not be asked to:** anything probabilistic (the Beta filter, the variance decomposition's probabilistic interpretation, stationarity, escape times); the section-4 dynamics; the derivation of OBL; the constraint-algebra laws it does not axiomatize — which is why Finding 5 gates the scaffold's usefulness for its own target claims ("compatibility is hard," "entrenchment can't repair it" are unprovable until laws exist); population-level semantics (no theorem links `prevalence` to `SpeakerStatus` today).

**JavaScript can verify:** executable consistency of the stated regimes; exact gated-choice normalization; exact LLR computation *under the written gated model* (and it is the code, not the paper, that gets the normalization right); return-to-prior under discounting; the latent-lect demonstration that marginal products misestimate assembly prevalence; regression protection against future edits.

**JavaScript cannot verify:** the paper-text formulas (it diverges on the repair link and silently resolves the double-discount ambiguity); any empirical claim (no data, no calibration of the effective-evidence scale, no test suite or manifest shipped in the bundle — Codex's verification-limits note is correct); the stationary-distribution conjecture; parameter identification; and nothing at all about whether the agreement counts, the COCA probe, or the LBE corpus numbers are accurately transcribed from their sources, which remain outside the bundle.

**Unverifiable from the bundle, flagged:** the compiled `main.pdf` build; external citations; the underlying agreement dataset; Codex's SHA-256 and workspace-hash claims; and Codex's 0.01466 simulation datum (see §5.4).
