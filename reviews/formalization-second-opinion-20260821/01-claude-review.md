# Review under adjudication: OVMG formal apparatus

<!-- SUMMARY: Claude (Fable 5) review of the OVMG formal core (section 3 state theory, section 4 dynamics, Lean scaffold, v2 contract) against the projectibility-first brief · status: awaiting second opinion · updated: 2026-08-21 -->

Reviewer: Claude (Fable 5), 2026-08-21. Scope: `paper/section3.tex`,
`paper/main.tex` lines ~749-1332, `formalization/OVMG/Core.lean`,
`ovmg-tools/` v2 contract, read against
`context/projectibility-first-wtwss-codex-brief.md` with instructions not to
take the brief as gospel. `lake build` succeeds. Line references are to the
files as packaged.

## Overall verdict

The formal core already implements the brief's programme more concretely than
the brief itself specifies, so the brief demands no rotation here. The real
findings are at two seams the brief would call unevidenced transport edges:
the learner-to-population bridge in section 4, and an epistemic term smuggled
into the ontic status definition through derived obligatoriness. The Lean
scaffold is honest about its scope but underpowered: its constraint algebra
has no laws, so it cannot prove the section-3 claims it exists to check, and
one of its bounded types encodes the wrong bounds.

## Where the formal core already does what the brief asks

The brief's four pocket questions map onto the architecture: *what travels* is
the projection list over (G_t, nu) and (F, Phi); *what travels together* is
the conjunction def-and-sat-and-L_t (the Lean necessity theorems check each
conjunct is individually needed); *how far* is the explicit non-transfer list
at section3.tex:344-351 (the classical predicate does not project processing
cost, LM string probability, typological comparanda, or cross-c transfer
without q_h); *what secures it* is section 4, explicitly graded
(stabilization / maintenance / candidate controller, each with its own
evidence standard and a clean failure condition for the controller at
main.tex:1004-1008). The brief's section-9 anti-vacuity constraints are
implemented nearly one-for-one in the identification subsection of section 3
(registered partitions, rho-star normed before licensing data, repeated
post-hoc reassignment counting against the framework). Nothing in the formal
core overclaims homeostasis or rides stability into causal order; support
grades are kept apart and the controller claim carries an explicit failure
condition.

## Findings

### Paper-level

**Finding 1. The epistemic-ontic loop is not closed (missing z dynamics).**
Section 3 separates S_t^theta (ontic, over inclusion states z_{j,t}) from
S-hat_t (posterior). But section 4 evolves only posteriors: the update
equations move (a, b), and actuation is defined as C_{t+1} and G_{t+1} rising
(main.tex ~1284). For theta_t to move, speakers' inclusion states z_{j,t} must
flip, and no rule anywhere (paper, Lean scaffold, or v2 contract, where
inclusion states are drawn statically from lect-conditional rates) maps a
speaker's posterior to their own inclusion state. The mean-field cubic
silently re-identifies the estimate with the population state that section 3
worked to keep apart. One stated bridging assumption fixes it (e.g., a
speaker's inclusion is a threshold or stochastic read-out of their own
posterior, and under homogeneous mean-field C stands for both). Without it,
the S-curve and bimodality claims are about trajectories of estimates, which
is not what actuation means.

**Finding 2. Derived obligatoriness leaks the evidence state back into the
ontic status.** sat(A,c) is a conjunct of the ontic S_t^theta (section3.tex
eq. 1, lines ~190-196), but the section-4.4 definition of OBL quantifies over
"estimated licensing below a tolerance epsilon with concentration above
nu_min" (main.tex ~1180-1185). Concentration is an epistemic quantity, so an
evidence state re-enters the status definition through the back door, undoing
what the 2026-07-10 revision was for ("preserves conventional status without
making it depend on the analyst's evidence state", DECISIONS 2026-07-10).
There is a defensible reading on which nu quantifies over speakers' posteriors
(world-side facts about the community), but the text never says whose
posterior it is. Either define OBL over the ontic licensing landscape (theta
near zero persistently across a stated window) with the estimated version as
its empirical identification, or state explicitly that the concentration is
the speakers', not the analyst's.

**Finding 3 (minor).** (a) The notation-bridge table cell (section3.tex:66)
writes S-hat_t = E[S_t^theta] without the conditioning on D_t that eq. 2
carries; given the revision hangs on that conditioning, the table should carry
it. (b) The prose identity "for a single pivotal node, S_t^theta =
theta_t(kappa,c)" (section3.tex:216-218) holds only under side conditions the
Lean theorem `speaker_status_unique_single_node_iff` makes explicit (a unique
covering assembly, defined and saturated, with that single node); a short
clause would inherit them.

### Lean-level

**Finding 4. `Confidence` mis-bounds decision confidence.** Phi^dec =
max{P(S>=tau|D), P(S<tau|D)} lies in [1/2, 1], with 1 attainable (the paper
treats structural-failure posteriors as degenerate "by modelling convention",
section3.tex ~600-604, and the worked examples write Phi approx 1). Lean's
single `Confidence` type (0 <= val < 1, Core.lean:196-199) both admits
impossible values below one half and rejects the attainable boundary 1. The
bounds fit Phi^ev only. Split into two types.

**Finding 5. The constraint algebra has no laws, so the scaffold cannot prove
its own target claims.** `ConstraintAlgebra` (Core.lean:22-25) is a bare
signature: nothing says `satisfiable top`, nothing makes `meet` associative or
commutative (so `Combined`'s foldl is order-sensitive, unlike the paper's
order-free big-join), and nothing makes satisfiability antitone under `meet`.
Consequently "compatibility is hard: there's no weighting an operator clash
away" (section3.tex:112) and worked example 3's "entrenchment of the parts
can't repair it" (a clash between any two contributed constraints dooms every
assembly containing both) are unprovable. Three laws (`sat_top`, assoc/comm,
`satisfiable (meet a b) -> satisfiable a`) would let the file prove
clash-dooms-assembly and permutation-invariance of `Def`. As it stands, the
six theorems are unfolding lemmas, and the README's "proves consequences of a
fixed constraint algebra" oversells until the algebra has at least one law.
Note also: with empty `constraints`, `Def` reduces to `satisfiable top`, which
no axiom guarantees.

**Finding 6. `PosteriorStatus` embeds the ontic target as data.** The field
`target : PopulationStatus Score` (Core.lean:180-186) means constructing an
analyst's state requires the true prevalence in hand, the very identification
the types exist to prevent, relocated inside a record. Replace the field with
an address of the target (the (f,v,c) index), not its value. Relatedly, the
distinction between `PopulationStatus` and `PosteriorStatus` is currently
nominal (two record types, no theorem ties `prevalence` to `SpeakerStatus`);
the README's "formalizes the distinction" should read "types the distinction".

**Finding 7. The one section-3 identity that is pure algebra is not proved.**
U_epi + U_het = S-hat(1 - S-hat) needs only two moments and rational
arithmetic, no probability model: with epi = m2 - m1^2 and het = m1 - m2 the
identity is immediate, and het >= 0 follows from S in [0,1] as a hypothesis
(m2 <= m1). Proving it would give `PosteriorStatus`'s four unconstrained
fields real content and guard the equation pair most likely to carry a typo
into empirical work. The current asymmetry (bounded-rational treatment for F
and Phi, opaque `Score` for the posterior summaries) has no principled ground.

**Finding 8. `Readout` drops the indexing that carries the anti-mereology
discipline.** The paper's F_{i,t}(u,e) is speaker-, utterance-, and
episode-indexed; Lean's `Readout` (Core.lean:201-204) is bare, so the types
cannot prevent attributing a read-out to the wrong bearer, the confusion the
architecture exists to block (and the brief's section-12.4 point about
grammaticality specifically).

**Finding 9 (terminology near-misses).** (a) The paper writes unification as a
join (square-cup, undefined-as-bottom, section3.tex:95-98); Lean calls the
combiner `meet`. Order-duality, not a bug, but a reader aligning the two will
stumble; one comment fixes it. (b) The README's "saturation as a derived
macro over obligatory dimensions" under-flags that the paper's "derived"
means OBL is itself derived from preemption dynamics (section 4.4), which the
scaffold cannot represent (`obl` is a primitive parameter there). (c) In
Lean, `supplies` is independent of `constraints`, so def and sat are formally
unrelated, whereas in the paper both derive from omega(A); acceptable at
scaffold level but worth a comment.

## Where not to take the brief as gospel

- **Its type-ledger demotion does not apply here.** The brief demotes explicit
  typing to audit representations. This paper's formal core is the product,
  and the Lean scaffold is precisely the audit surface the brief licenses. If
  anything the brief argues for more Lean at the seams, not less.
- **The explanatory inversion is not a definitional one.** The brief's
  ordering (projection target, then profile, then grain, then range, then
  security) governs explanatory priority in prose. A formal system must
  define the state before stating projections over it; section 3 defining
  S^theta first is not maintenance-first backsliding, and section 3's opening
  paragraph already has the explanatory order right.
- **The one brief demand worth importing is grain registration.** c, n,
  rho-star, and tau all have identification discipline; the construction
  inventory H has a criterion (the template-typing rule in the existential
  subsection) but no registration protocol, and the LBE dedicated-node
  argument shows inventory choice can decide cases. One sentence in the
  identification subsection putting contested template-typing and
  node-individuation choices under the same registration discipline would
  close the brief's section-9.4 gap without committing to inventory
  inference.

## Recommendations (as given to Brett, ranked)

**Do now (prose):**

1. Close the z-loop with one stated assumption in the "Open-loop learning and
   closed-loop dynamics" block (main.tex ~1069-1086): a speaker's inclusion
   state is a stochastic function of their own posterior mean, increasing in
   it, threshold rule as limiting case; under the homogeneous mean-field the
   shared posterior mean and the population licensing rate coincide, and that
   shared quantity is what the cubic evolves. Adjust the actuation subsection
   so actuation is movement of theta_t via inclusion flips, with rising
   C_{t+1} as its learner-side reflection.
2. Re-found derived obligatoriness ontically: every zero-marking assembly in a
   d-at-issue niche has theta below epsilon persistently over a stated window
   (persistence replacing concentration, which has no ontic analogue); keep
   the estimated-licensing version as the identification condition one
   sentence later. Alternative: keep the epistemic formulation but say whose
   posteriors (speakers', not the analyst's).
3. Small fixes: conditioning on D_t in the table cell; side conditions on the
   single-pivotal-node identity; one sentence registering inventory and
   template-typing choices in the identification subsection.

**Then (Lean, one session):**

4. Split `Confidence` into `EvidenceConfidence` [0,1) and
   `DecisionConfidence` [1/2, 1] closed at 1.
5. Add the three constraint-algebra laws; prove clash-dooms-assembly and
   permutation-invariance of `Def`.
6. Prove the moment identity (epi + het = m1(1-m1)) over rationals with
   the [0,1] hypotheses; wire `PosteriorStatus` to it.
7. Replace `PosteriorStatus.target` with an index; index `Readout` by
   speaker, utterance, episode.
8. Documentation lines: join/meet duality comment; README rewordings
   ("types the distinction"; "parameterized by an obligatoriness relation;
   its section-4 derivation is out of scope").

**Skip:** typing projection ranges in Lean (decoration until the Predictions
section is formalized); inventory inference; the stationary-distribution
theorem in Lean; reordering sections 3-4 to match the brief.

## Numerical verifications performed

- Variance decomposition: Var(theta|D) = C(1-C)/(nu+1) and
  E[theta(1-theta)|D] = C(1-C)nu/(nu+1) for Beta(a,b); sum C(1-C). Confirmed.
- Cubic fixed point C-double-dagger = (beta+chi*psi)/(alpha+2*chi*psi), with
  endpoint attraction consistent with 0 < C-double-dagger < 1. Confirmed.
- tau(c) = L_fa/(L_fa+L_fr) from asymmetric expected loss. Confirmed.
- Figure posterior-means: Beta(1,1) with per-step mass m gives mean 1/(2+mt);
  plotted coordinates match for m = 0.01 and m = 5; Beta(1,1.5) 95% CrI
  endpoints at t = 50 (0.0167, 0.9145) match closed-form quantiles. Confirmed.
- Omission LLR small-mass approximation ell approx g*rho-star from the gated
  softmax renormalization. Confirmed to first order.
- lake build: succeeds (2026-08-21).
