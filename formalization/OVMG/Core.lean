import Std

/-!
# OVMG structural sanity checks

This file formalizes the type-level core of the paper's revised Sections 3--4.
It checks the structural relations among coverage, hard compatibility,
saturation, speaker-level licensing, and the distinction between a population
status target and a posterior estimate of that target. It deliberately does not
attempt the stochastic claims in Section 4: those require a fully specified
probability model and remain simulation and inference targets.

The scope is deliberately narrow. Everything below is a consequence of a fixed
construction inventory, a fixed lawful constraint algebra, and a fixed
time-slice interface for obligatoriness and value supply. Nothing here shows
that a particular linguistic analysis supplies the right inventory, the right
constraints, the right obligatory dimensions, or the right supplied values.
-/

namespace OVMG

universe uForm uValue uFrame uDim uConstraint uNode uCtx uSpeaker

/-! ## The hard-compatibility interface -/

/-- The hard-compatibility interface.

A construction contributes a typed constraint; assembly construction combines
the contributed constraints; compatibility obtains exactly when the combination
is satisfiable. Atomic feature assignments are one special case, not the
general representation.

**Orientation.** The paper writes information combination as a *join* on an
information-ordered lattice (more information = higher). Lean writes the same
operation as `meet` under the dual, *constraint-strength* order, in which a
stronger constraint sits lower and `top` is the empty (uninformative)
constraint. The two presentations are the same operation read through opposite
orders; the field names below follow the Lean/meet convention.

The laws are exactly what is needed for order-independent combination of a
finite bag of contributions, together with the two satisfiability facts the
paper's Definition uses:

* `meet_top`, `meet_comm`, `meet_assoc`, `meet_idem`: combination is an
  idempotent commutative monoid operation with `top` as unit, so combining a
  list of contributions does not depend on the order or multiplicity in which
  they are presented;
* `satisfiable_top`: the empty combination is satisfiable, so vacuity is not
  produced by unsatisfiability of the unit;
* `satisfiable_of_meet_left`: satisfiability projects downwards from a
  combination to each conjunct, so an unsatisfiable contribution cannot be
  rescued by combination.

These structure fields are assumptions on the supplied algebra, not theorems
about any particular constraint language. -/
structure ConstraintAlgebra (Constraint : Type uConstraint) where
  /-- The empty, uninformative constraint: the unit of combination. -/
  top : Constraint
  /-- Information combination (the paper's join, read under the dual order). -/
  meet : Constraint -> Constraint -> Constraint
  /-- The satisfiability predicate on combined constraints. -/
  satisfiable : Constraint -> Prop
  /-- `top` is a right unit for combination. -/
  meet_top : ∀ x, meet x top = x
  /-- Combination is commutative. -/
  meet_comm : ∀ x y, meet x y = meet y x
  /-- Combination is associative. -/
  meet_assoc : ∀ x y z, meet (meet x y) z = meet x (meet y z)
  /-- Combination is idempotent. -/
  meet_idem : ∀ x, meet x x = x
  /-- The empty combination is satisfiable. -/
  satisfiable_top : satisfiable top
  /-- Satisfiability projects down to the left conjunct. -/
  satisfiable_of_meet_left : ∀ x y, satisfiable (meet x y) -> satisfiable x

namespace ConstraintAlgebra

variable {Constraint : Type uConstraint} (alg : ConstraintAlgebra Constraint)

/-- `top` is also a left unit for combination. -/
theorem top_meet (x : Constraint) : alg.meet alg.top x = x := by
  rw [alg.meet_comm, alg.meet_top]

/-- Satisfiability projects down to the right conjunct as well. -/
theorem satisfiable_of_meet_right (x y : Constraint)
    (h : alg.satisfiable (alg.meet x y)) : alg.satisfiable y := by
  refine alg.satisfiable_of_meet_left y x ?_
  rwa [alg.meet_comm]

/-- Combination is left-commutative, the form used for reordering lists. -/
theorem meet_left_comm (x y z : Constraint) :
    alg.meet x (alg.meet y z) = alg.meet y (alg.meet x z) := by
  rw [← alg.meet_assoc, ← alg.meet_assoc, alg.meet_comm x y]

end ConstraintAlgebra

/-! ## Combining contributed constraints -/

/-- Combine all operator constraints contributed by an assembly. -/
def Combined {Constraint : Type uConstraint}
    (alg : ConstraintAlgebra Constraint) (constraints : List Constraint) : Constraint :=
  constraints.foldl alg.meet alg.top

variable {Constraint : Type uConstraint}

@[simp] theorem Combined_nil (alg : ConstraintAlgebra Constraint) :
    Combined alg [] = alg.top := rfl

/-- The accumulator of the fold can always be pulled out in front. -/
theorem foldl_meet_eq (alg : ConstraintAlgebra Constraint) :
    ∀ (l : List Constraint) (a : Constraint),
      l.foldl alg.meet a = alg.meet a (Combined alg l)
  | [], a => by simp [Combined, alg.meet_top]
  | x :: l, a => by
      have ih := foldl_meet_eq alg l
      show l.foldl alg.meet (alg.meet a x) = _
      rw [ih (alg.meet a x)]
      show _ = alg.meet a (List.foldl alg.meet (alg.meet alg.top x) l)
      rw [alg.top_meet, ih x, alg.meet_assoc]

/-- Combination of a cons list is the head combined with the rest. -/
theorem Combined_cons (alg : ConstraintAlgebra Constraint)
    (x : Constraint) (l : List Constraint) :
    Combined alg (x :: l) = alg.meet x (Combined alg l) := by
  show List.foldl alg.meet (alg.meet alg.top x) l = _
  rw [alg.top_meet, foldl_meet_eq]

/-- Satisfiability of a combination projects down to every conjunct: a single
unsatisfiable contribution cannot be rescued by the others. -/
theorem satisfiable_of_mem_of_satisfiable_combined
    (alg : ConstraintAlgebra Constraint) :
    ∀ {l : List Constraint} {c : Constraint}, c ∈ l ->
      alg.satisfiable (Combined alg l) -> alg.satisfiable c
  | [], _, hmem, _ => absurd hmem (by simp)
  | x :: l, c, hmem, hsat => by
      rw [Combined_cons] at hsat
      rcases List.mem_cons.mp hmem with h | h
      · exact h ▸ alg.satisfiable_of_meet_left _ _ hsat
      · exact satisfiable_of_mem_of_satisfiable_combined alg h
          (alg.satisfiable_of_meet_right _ _ hsat)

/-- Combination does not depend on the order in which contributions are
presented. -/
theorem Combined_perm (alg : ConstraintAlgebra Constraint) :
    ∀ {l₁ l₂ : List Constraint}, l₁.Perm l₂ -> Combined alg l₁ = Combined alg l₂
  | _, _, List.Perm.nil => rfl
  | _, _, List.Perm.cons x h => by
      rw [Combined_cons, Combined_cons, Combined_perm alg h]
  | _, _, List.Perm.swap x y l => by
      rw [Combined_cons, Combined_cons, Combined_cons, Combined_cons,
        alg.meet_left_comm]
  | _, _, List.Perm.trans h₁ h₂ => by
      rw [Combined_perm alg h₁, Combined_perm alg h₂]

/-! ## Assemblies -/

/-- An assembly is represented only by the information the status definition
uses. The paper supplies the grammar-specific tree and composition machinery.

Rather than carrying independent node and constraint lists, an assembly carries
a single nonempty list of *contributions*: each entry is a node together with
the typed constraint that node contributes. Nodes and constraints are derived
from that list. This makes two degenerate representations unrepresentable:

* an assembly with no contributions at all, which would be vacuously licensed
  by every speaker and vacuously compatible; and
* an assembly whose node list and constraint list are incoherent, e.g. of
  different lengths or paired up in the wrong order. -/
structure Assembly
    (Form : Type uForm) (Value : Type uValue) (Frame : Type uFrame)
    (Constraint : Type uConstraint) (Node : Type uNode) where
  form : Form
  value : Value
  frame : Frame
  /-- The nonempty list of node-with-contributed-constraint pairs. -/
  contributions : List (Node × Constraint)
  /-- An assembly has at least one contribution. -/
  contributions_ne_nil : contributions ≠ []

variable {Form : Type uForm} {Value : Type uValue} {Frame : Type uFrame}
variable {Dim : Type uDim} {Node : Type uNode}
variable {Ctx : Type uCtx} {Speaker : Type uSpeaker}

local notation "Asm" => Assembly Form Value Frame Constraint Node

namespace Assembly

/-- The nodes of an assembly, derived from its contributions. -/
def nodes (A : Asm) : List Node := A.contributions.map Prod.fst

/-- The typed constraints of an assembly, derived from its contributions. -/
def constraints (A : Asm) : List Constraint := A.contributions.map Prod.snd

theorem nodes_ne_nil (A : Asm) : A.nodes ≠ [] := by
  intro h
  exact A.contributions_ne_nil (List.map_eq_nil_iff.mp h)

theorem constraints_ne_nil (A : Asm) : A.constraints ≠ [] := by
  intro h
  exact A.contributions_ne_nil (List.map_eq_nil_iff.mp h)

theorem exists_node (A : Asm) : ∃ k : Node, k ∈ A.nodes := by
  cases hc : A.nodes with
  | nil => exact absurd hc A.nodes_ne_nil
  | cons k t => exact ⟨k, by simp⟩

theorem mem_constraints_of_mem_contributions {A : Asm} {k : Node} {c : Constraint}
    (h : (k, c) ∈ A.contributions) : c ∈ A.constraints :=
  List.mem_map.mpr ⟨(k, c), h, rfl⟩

theorem mem_nodes_of_mem_contributions {A : Asm} {k : Node} {c : Constraint}
    (h : (k, c) ∈ A.contributions) : k ∈ A.nodes :=
  List.mem_map.mpr ⟨(k, c), h, rfl⟩

end Assembly

/-! ## Coverage, compatibility, saturation, licensing -/

/-- Value-matched structural coverage. -/
def Covers (A : Asm) (f : Form) (v : Value) : Prop :=
  A.form = f ∧ A.value = v

/-- Hard operator compatibility: the combined typed constraint structure is
satisfiable. -/
def Def (alg : ConstraintAlgebra Constraint) (A : Asm) : Prop :=
  alg.satisfiable (Combined alg A.constraints)

/-- Saturation is a derived macro: every obligatory dimension for the
assembly's independently typed frame has a supplied value.

`obl` and `supplies` are primitive parameters of this development. They are a
*fixed time-slice interface*: the obligatoriness of a dimension in a context
and the supply of a value by an assembly are given from outside. Lean does not
derive ontic obligatoriness from anything more basic, does not model change of
`obl` over time, and proves nothing about whether a particular `supplies`
relation is the linguistically correct one. Every theorem below is conditional
on whatever `obl` and `supplies` are supplied. -/
def Sat (obl : Ctx -> Frame -> Dim -> Prop) (supplies : Asm -> Dim -> Prop)
    (A : Asm) (c : Ctx) : Prop :=
  ∀ d, obl c A.frame d -> supplies A d

/-- A speaker licenses every node needed by an assembly. Since `A.nodes` is
nonempty, this is never vacuously true. -/
def LicensedNodes (z : Speaker -> Node -> Ctx -> Prop) (j : Speaker)
    (A : Asm) (c : Ctx) : Prop :=
  ∀ k ∈ A.nodes, z j k c

/-- Licensing is a real demand: it entails licensing of some actual node. -/
theorem exists_licensed_node_of_licensedNodes
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker} {A : Asm} {c : Ctx}
    (h : LicensedNodes z j A c) : ∃ k, k ∈ A.nodes ∧ z j k c := by
  rcases A.exists_node with ⟨k, hk⟩
  exact ⟨k, hk, h k hk⟩

/-- Non-empty coverage relative to an independently fixed inventory. -/
def CoverageNonempty (inventory : Asm -> Prop) (f : Form) (v : Value) : Prop :=
  ∃ A, inventory A ∧ Covers A f v

/-- The speaker-level Boolean whose population prevalence is the paper's
theta-conditional status target S^theta. -/
def SpeakerStatus (inventory : Asm -> Prop) (alg : ConstraintAlgebra Constraint)
    (obl : Ctx -> Frame -> Dim -> Prop) (supplies : Asm -> Dim -> Prop)
    (z : Speaker -> Node -> Ctx -> Prop) (j : Speaker) (f : Form) (v : Value)
    (c : Ctx) : Prop :=
  ∃ A, inventory A ∧ Covers A f v ∧ Def alg A ∧ Sat obl supplies A c ∧
    LicensedNodes z j A c

theorem speaker_status_implies_coverage
    {inventory : Asm -> Prop} {alg : ConstraintAlgebra Constraint}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker}
    {f : Form} {v : Value} {c : Ctx} :
    SpeakerStatus inventory alg obl supplies z j f v c ->
      CoverageNonempty inventory f v := by
  intro h
  rcases h with ⟨A, hInv, hCov, _hDef, _hSat, _hLic⟩
  exact ⟨A, hInv, hCov⟩

theorem no_speaker_status_of_empty_coverage
    {inventory : Asm -> Prop} {alg : ConstraintAlgebra Constraint}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker}
    {f : Form} {v : Value} {c : Ctx}
    (hEmpty : ¬ CoverageNonempty inventory f v) :
    ¬ SpeakerStatus inventory alg obl supplies z j f v c := by
  intro hStatus
  exact hEmpty (speaker_status_implies_coverage hStatus)

theorem not_def_of_unsatisfiable_combined
    {alg : ConstraintAlgebra Constraint} {A : Asm}
    (h : ¬ alg.satisfiable (Combined alg A.constraints)) : ¬ Def alg A := by
  simpa [Def] using h

/-! ### A clash dooms the assembly -/

/-- If any contributed constraint is itself unsatisfiable, the whole assembly
is hard-incompatible. -/
theorem not_def_of_unsatisfiable_constraint
    {alg : ConstraintAlgebra Constraint} {A : Asm} {c : Constraint}
    (hmem : c ∈ A.constraints) (hc : ¬ alg.satisfiable c) : ¬ Def alg A := by
  intro hDef
  exact hc (satisfiable_of_mem_of_satisfiable_combined alg hmem hDef)

/-- The same statement phrased at the level of contributions: a node whose
contributed constraint clashes on its own dooms the assembly. -/
theorem not_def_of_unsatisfiable_contribution
    {alg : ConstraintAlgebra Constraint} {A : Asm} {k : Node} {c : Constraint}
    (hmem : (k, c) ∈ A.contributions) (hc : ¬ alg.satisfiable c) : ¬ Def alg A :=
  not_def_of_unsatisfiable_constraint (Assembly.mem_constraints_of_mem_contributions hmem) hc

/-- Conversely, hard compatibility entails satisfiability of every single
contributed constraint. -/
theorem satisfiable_contribution_of_def
    {alg : ConstraintAlgebra Constraint} {A : Asm} {k : Node} {c : Constraint}
    (hDef : Def alg A) (hmem : (k, c) ∈ A.contributions) : alg.satisfiable c :=
  satisfiable_of_mem_of_satisfiable_combined alg
    (Assembly.mem_constraints_of_mem_contributions hmem) hDef

/-- An unsatisfiable contributed constraint blocks speaker-level status for
every assembly in the inventory that covers the pair. -/
theorem no_speaker_status_of_clash
    {inventory : Asm -> Prop} {alg : ConstraintAlgebra Constraint}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker}
    {f : Form} {v : Value} {c : Ctx}
    (hClash : ∀ A, inventory A -> Covers A f v ->
      ∃ k q, (k, q) ∈ A.contributions ∧ ¬ alg.satisfiable q) :
    ¬ SpeakerStatus inventory alg obl supplies z j f v c := by
  intro hStatus
  rcases hStatus with ⟨A, hInv, hCov, hDef, _hSat, _hLic⟩
  rcases hClash A hInv hCov with ⟨k, q, hmem, hq⟩
  exact not_def_of_unsatisfiable_contribution hmem hq hDef

/-! ### Order independence -/

/-- Hard compatibility does not depend on the order in which the contributions
are listed. -/
theorem def_perm_contributions
    {alg : ConstraintAlgebra Constraint} {A B : Asm}
    (h : A.contributions.Perm B.contributions) : Def alg A ↔ Def alg B := by
  have hc : Combined alg A.constraints = Combined alg B.constraints :=
    Combined_perm alg (h.map Prod.snd)
  simp only [Def, hc]

/-! ### Saturation -/

theorem not_sat_of_missing_obligatory {A : Asm}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {c : Ctx} {d : Dim}
    (hObl : obl c A.frame d) (hMissing : ¬ supplies A d) :
    ¬ Sat obl supplies A c := by
  intro hSat
  exact hMissing (hSat d hObl)

theorem no_speaker_status_of_all_covering_undefined
    {inventory : Asm -> Prop} {alg : ConstraintAlgebra Constraint}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker}
    {f : Form} {v : Value} {c : Ctx}
    (hUndefined : ∀ A, inventory A -> Covers A f v -> ¬ Def alg A) :
    ¬ SpeakerStatus inventory alg obl supplies z j f v c := by
  intro hStatus
  rcases hStatus with ⟨A, hInv, hCov, hDef, _hSat, _hLic⟩
  exact (hUndefined A hInv hCov) hDef

theorem no_speaker_status_of_all_covering_unsaturated
    {inventory : Asm -> Prop} {alg : ConstraintAlgebra Constraint}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker}
    {f : Form} {v : Value} {c : Ctx}
    (hUnsat : ∀ A, inventory A -> Covers A f v -> ¬ Sat obl supplies A c) :
    ¬ SpeakerStatus inventory alg obl supplies z j f v c := by
  intro hStatus
  rcases hStatus with ⟨A, hInv, hCov, _hDef, hSat, _hLic⟩
  exact (hUnsat A hInv hCov) hSat

/-! ### The single-pivotal-node reduction -/

theorem assembly_licensed_single_node_iff {A : Asm}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker} {c : Ctx} {k : Node}
    {q : Constraint} (hContrib : A.contributions = [(k, q)]) :
    LicensedNodes z j A c ↔ z j k c := by
  have hNodes : A.nodes = [k] := by simp [Assembly.nodes, hContrib]
  constructor
  · intro h
    apply h k
    simp [hNodes]
  · intro h k' hMem
    simp [hNodes] at hMem
    simpa [hMem] using h

theorem speaker_status_unique_single_node_iff {A : Asm}
    {inventory : Asm -> Prop} {alg : ConstraintAlgebra Constraint}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker}
    {f : Form} {v : Value} {c : Ctx} {k : Node} {q : Constraint}
    (hInv : inventory A) (hCov : Covers A f v) (hDef : Def alg A)
    (hSat : Sat obl supplies A c)
    (hUnique : ∀ B, inventory B -> Covers B f v -> B = A)
    (hContrib : A.contributions = [(k, q)]) :
    SpeakerStatus inventory alg obl supplies z j f v c ↔ z j k c := by
  constructor
  · intro hStatus
    rcases hStatus with ⟨B, hInvB, hCovB, _hDefB, _hSatB, hLicB⟩
    have hBA : B = A := hUnique B hInvB hCovB
    subst B
    exact (assembly_licensed_single_node_iff (A := A) (z := z) (j := j)
      (c := c) (k := k) (q := q) hContrib).mp hLicB
  · intro hLic
    exact ⟨A, hInv, hCov, hDef, hSat,
      (assembly_licensed_single_node_iff (A := A) (z := z) (j := j)
        (c := c) (k := k) (q := q) hContrib).mpr hLic⟩

/-- For a single-contribution assembly, hard compatibility is exactly
satisfiability of that one contributed constraint. -/
theorem def_single_contribution_iff {alg : ConstraintAlgebra Constraint} {A : Asm}
    {k : Node} {q : Constraint} (hContrib : A.contributions = [(k, q)]) :
    Def alg A ↔ alg.satisfiable q := by
  have h : A.constraints = [q] := by simp [Assembly.constraints, hContrib]
  simp [Def, h, Combined_cons, alg.meet_top]

/-! ## Rational-valued arithmetic helpers

Only what is needed for the posterior summaries below; the project depends on
`Std` alone, so these are proved from the core `Rat` API. -/

theorem rat_div_nonneg {x y : Rat} (hx : 0 ≤ x) (hy : 0 < y) : 0 ≤ x / y := by
  refine Rat.not_lt.mp ?_
  intro h
  rw [Rat.div_lt_iff hy, Rat.zero_mul] at h
  exact absurd hx (Rat.not_le.mpr h)

theorem rat_ne_zero_of_pos {x : Rat} (h : 0 < x) : x ≠ 0 := (Rat.ne_of_lt h).symm

theorem rat_lt_trans {x y z : Rat} (h₁ : x < y) (h₂ : y < z) : x < z := by
  refine Rat.not_le.mp ?_
  intro h
  exact absurd (Rat.le_trans (Rat.le_of_lt h₂) h) (Rat.not_le.mpr h₁)

theorem rat_add_pos {x y : Rat} (hx : 0 < x) (hy : 0 < y) : 0 < x + y := by
  have h : x + 0 < x + y := Rat.add_lt_add_left.mpr hy
  rw [Rat.add_zero] at h
  exact rat_lt_trans hx h

theorem rat_split_div {x K : Rat} (hK : K + 1 ≠ 0) :
    x / (K + 1) + x * K / (K + 1) = x := by
  have h1 : x + x * K = x * (K + 1) := by
    rw [Rat.mul_add, Rat.mul_one, Rat.add_comm]
  rw [Rat.div_def, Rat.div_def, ← Rat.add_mul, h1, ← Rat.div_def,
    Rat.mul_div_cancel hK]

/-! ## Population status and its posterior -/

/-- The ontic population target S^theta: the prevalence, in the population, of
the speaker-level status Boolean. It is a rational number in `[0,1]`, and the
bounds are carried in the type rather than assumed at use sites.

Lean keeps this separate from the posterior that a learner or analyst maintains
about it. -/
structure PopulationStatus where
  prevalence : Rat
  nonneg : (0 : Rat) ≤ prevalence
  le_one : prevalence ≤ 1

theorem populationStatus_range (S : PopulationStatus) :
    (0 : Rat) ≤ S.prevalence ∧ S.prevalence ≤ 1 :=
  ⟨S.nonneg, S.le_one⟩

/-- A Beta posterior over a population status target.

The posterior is parameterized by its two positive pseudo-counts `a` and `b`;
every summary the paper reports is *derived* from them rather than stored as an
unconstrained field, so no incoherent combination of mean, concentration and
uncertainties is representable. The target it is a posterior *about* is kept
inside the structure, so the target and its estimate cannot be silently
identified. -/
structure PosteriorStatus where
  /-- The target this posterior is about. -/
  target : PopulationStatus
  /-- First Beta pseudo-count. -/
  a : Rat
  /-- Second Beta pseudo-count. -/
  b : Rat
  a_pos : 0 < a
  b_pos : 0 < b

namespace PosteriorStatus

variable (P : PosteriorStatus)

/-- Posterior concentration `K = a + b`: the effective sample size. -/
def concentration : Rat := P.a + P.b

/-- Posterior mean `C = a / (a + b)`, the central estimate of the target. -/
def mean : Rat := P.a / P.concentration

/-- Epistemic uncertainty: the posterior variance of the target,
`C(1-C)/(K+1)`. It vanishes as the concentration grows. -/
def epistemicUncertainty : Rat :=
  P.mean * (1 - P.mean) / (P.concentration + 1)

/-- Heterogeneity: the expected within-population Bernoulli variance
`E[theta(1-theta)] = C(1-C)K/(K+1)`. It does not vanish as the concentration
grows; it is irreducible variability, not ignorance. -/
def heterogeneity : Rat :=
  P.mean * (1 - P.mean) * P.concentration / (P.concentration + 1)

theorem concentration_pos : 0 < P.concentration :=
  rat_add_pos P.a_pos P.b_pos

theorem concentration_add_one_pos : 0 < P.concentration + 1 :=
  rat_add_pos P.concentration_pos (by decide)

theorem mean_pos : 0 < P.mean := by
  rw [mean, Rat.lt_div_iff P.concentration_pos, Rat.zero_mul]
  exact P.a_pos

theorem mean_lt_one : P.mean < 1 := by
  rw [mean, Rat.div_lt_iff P.concentration_pos, Rat.one_mul, concentration]
  have h : P.a + 0 < P.a + P.b := Rat.add_lt_add_left.mpr P.b_pos
  rwa [Rat.add_zero] at h

/-- The posterior mean lies in `[0,1]`. -/
theorem mean_range : (0 : Rat) ≤ P.mean ∧ P.mean ≤ 1 :=
  ⟨Rat.le_of_lt P.mean_pos, Rat.le_of_lt P.mean_lt_one⟩

theorem one_sub_mean_nonneg : (0 : Rat) ≤ 1 - P.mean :=
  (Rat.le_iff_sub_nonneg _ _).mp P.mean_range.2

theorem mean_mul_one_sub_mean_nonneg : (0 : Rat) ≤ P.mean * (1 - P.mean) :=
  Rat.mul_nonneg P.mean_range.1 P.one_sub_mean_nonneg

theorem epistemicUncertainty_nonneg : (0 : Rat) ≤ P.epistemicUncertainty :=
  rat_div_nonneg P.mean_mul_one_sub_mean_nonneg P.concentration_add_one_pos

theorem heterogeneity_nonneg : (0 : Rat) ≤ P.heterogeneity :=
  rat_div_nonneg
    (Rat.mul_nonneg P.mean_mul_one_sub_mean_nonneg (Rat.le_of_lt P.concentration_pos))
    P.concentration_add_one_pos

/-- The moment identity: epistemic uncertainty and heterogeneity partition the
total Bernoulli variance at the posterior mean, `U_epi + U_het = C(1-C)`, where
`C` is the posterior mean. Concentration shifts weight between the two terms
without changing their sum. -/
theorem uncertainty_decomposition :
    P.epistemicUncertainty + P.heterogeneity = P.mean * (1 - P.mean) := by
  simp only [epistemicUncertainty, heterogeneity]
  exact rat_split_div (rat_ne_zero_of_pos P.concentration_add_one_pos)

end PosteriorStatus

/-! ## Non-vacuity witnesses

The structure laws above are assumptions, so it is worth exhibiting models of
them: the theorems are then known not to be vacuously true. -/

/-- A model of the constraint-algebra laws: `Bool` under conjunction, with
`true` as the empty constraint and `= true` as satisfiability. -/
def boolConstraintAlgebra : ConstraintAlgebra Bool where
  top := true
  meet := (· && ·)
  satisfiable := fun x => x = true
  meet_top := by decide
  meet_comm := by decide
  meet_assoc := by decide
  meet_idem := by decide
  satisfiable_top := rfl
  satisfiable_of_meet_left := by decide

/-- A one-contribution assembly over that model, showing `Assembly` is
inhabited. -/
def unitAssembly (k : Node) : Assembly Unit Unit Unit Bool Node where
  form := ()
  value := ()
  frame := ()
  contributions := [(k, true)]
  contributions_ne_nil := by simp

example (k : Node) : Def boolConstraintAlgebra (unitAssembly k) :=
  (def_single_contribution_iff (alg := boolConstraintAlgebra) rfl).mpr rfl

/-- A uniform (Beta(1,1)) posterior about a target, showing `PosteriorStatus`
is inhabited. -/
def uniformPosterior (S : PopulationStatus) : PosteriorStatus where
  target := S
  a := 1
  b := 1
  a_pos := by decide
  b_pos := by decide

/-! ## Bounded read-outs -/

/-- A bounded anomaly read-out, typed so values can only be introduced with a
proof of the stated range. -/
structure Anomaly where
  val : Rat
  gt_neg_one : (-1 : Rat) < val
  le_zero : val ≤ 0

/-- A bounded *evidence* confidence read-out: how much the evidence supports a
verdict, on a scale where `0` is no evidential support and `1` is unreachable
certainty. -/
structure EvidenceConfidence where
  val : Rat
  nonneg : (0 : Rat) ≤ val
  lt_one : val < 1

/-- A bounded *decision* confidence read-out: the probability assigned to the
side the decision comes down on. Because it is the larger of two complementary
probabilities, it never falls below `1/2`, and unlike evidence confidence it may
reach `1`. -/
structure DecisionConfidence where
  val : Rat
  half_le : (1 / 2 : Rat) ≤ val
  le_one : val ≤ 1

structure Readout where
  anomaly : Anomaly
  evidenceConfidence : EvidenceConfidence
  decisionConfidence : DecisionConfidence

theorem anomaly_range (F : Anomaly) :
    (-1 : Rat) < F.val ∧ F.val ≤ 0 :=
  ⟨F.gt_neg_one, F.le_zero⟩

theorem evidence_confidence_range (phi : EvidenceConfidence) :
    (0 : Rat) ≤ phi.val ∧ phi.val < 1 :=
  ⟨phi.nonneg, phi.lt_one⟩

theorem decision_confidence_range (psi : DecisionConfidence) :
    (1 / 2 : Rat) ≤ psi.val ∧ psi.val ≤ 1 :=
  ⟨psi.half_le, psi.le_one⟩

/-- The two confidence scales are genuinely different: decision confidence is
bounded below by `1/2`, and evidence confidence can sit strictly below that
bound, so neither structure is a subtype of the other. -/
theorem decision_confidence_nonneg (psi : DecisionConfidence) :
    (0 : Rat) ≤ psi.val :=
  Rat.le_trans (rat_div_nonneg (by decide) (by decide)) psi.half_le

theorem readout_confidences_range (R : Readout) :
    (0 : Rat) ≤ R.evidenceConfidence.val ∧ R.evidenceConfidence.val < 1 ∧
      (1 / 2 : Rat) ≤ R.decisionConfidence.val ∧ R.decisionConfidence.val ≤ 1 :=
  ⟨R.evidenceConfidence.nonneg, R.evidenceConfidence.lt_one,
    R.decisionConfidence.half_le, R.decisionConfidence.le_one⟩

end OVMG
