import Std

/-!
# OVMG structural sanity checks

This file formalizes the type-level core of the paper's revised Sections 3--4.
It checks the structural relations among coverage, hard compatibility,
saturation, speaker-level licensing, and the distinction between a population
status target and a posterior estimate of that target. It deliberately does not
attempt the stochastic claims in Section 4: those require a fully specified
probability model and remain simulation and inference targets.
-/

namespace OVMG

universe uForm uValue uFrame uDim uConstraint uNode uCtx uSpeaker uScore

/-- The hard-compatibility interface. A construction contributes a typed
constraint; assembly construction meets constraints; compatibility obtains
exactly when their meet is satisfiable. Atomic feature assignments are one
special case, not the general representation. -/
structure ConstraintAlgebra (Constraint : Type uConstraint) where
  top : Constraint
  meet : Constraint -> Constraint -> Constraint
  satisfiable : Constraint -> Prop

/-- Combine all operator constraints contributed by an assembly. -/
def Combined {Constraint : Type uConstraint}
    (alg : ConstraintAlgebra Constraint) (constraints : List Constraint) : Constraint :=
  constraints.foldl alg.meet alg.top

/-- An assembly is represented only by the information the status definition
uses. The paper supplies the grammar-specific tree and composition machinery. -/
structure Assembly
    (Form : Type uForm) (Value : Type uValue) (Frame : Type uFrame)
    (Constraint : Type uConstraint) (Node : Type uNode) where
  form : Form
  value : Value
  frame : Frame
  nodes : List Node
  constraints : List Constraint

variable {Form : Type uForm} {Value : Type uValue} {Frame : Type uFrame}
variable {Dim : Type uDim} {Constraint : Type uConstraint} {Node : Type uNode}
variable {Ctx : Type uCtx} {Speaker : Type uSpeaker}

local notation "Asm" => Assembly Form Value Frame Constraint Node

/-- Value-matched structural coverage. -/
def Covers (A : Asm) (f : Form) (v : Value) : Prop :=
  A.form = f ∧ A.value = v

/-- Hard operator compatibility: the combined typed constraint structure is
satisfiable. -/
def Def (alg : ConstraintAlgebra Constraint) (A : Asm) : Prop :=
  alg.satisfiable (Combined alg A.constraints)

/-- Saturation is a derived macro: every obligatory dimension for the
assembly's independently typed frame has a supplied value. -/
def Sat (obl : Ctx -> Frame -> Dim -> Prop) (supplies : Asm -> Dim -> Prop)
    (A : Asm) (c : Ctx) : Prop :=
  ∀ d, obl c A.frame d -> supplies A d

/-- A speaker licenses every node needed by an assembly. -/
def LicensedNodes (z : Speaker -> Node -> Ctx -> Prop) (j : Speaker)
    (A : Asm) (c : Ctx) : Prop :=
  ∀ k ∈ A.nodes, z j k c

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

theorem not_sat_of_missing_obligatory {A : Asm}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {c : Ctx} {d : Dim}
    (hObl : obl c A.frame d) (hMissing : ¬ supplies A d) :
    ¬ Sat obl supplies A c := by
  intro hSat
  exact hMissing (hSat d hObl)

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

theorem assembly_licensed_single_node_iff {A : Asm}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker} {c : Ctx} {k : Node}
    (hNodes : A.nodes = [k]) :
    LicensedNodes z j A c ↔ z j k c := by
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
    {f : Form} {v : Value} {c : Ctx} {k : Node}
    (hInv : inventory A) (hCov : Covers A f v) (hDef : Def alg A)
    (hSat : Sat obl supplies A c)
    (hUnique : ∀ B, inventory B -> Covers B f v -> B = A)
    (hNodes : A.nodes = [k]) :
    SpeakerStatus inventory alg obl supplies z j f v c ↔ z j k c := by
  constructor
  · intro hStatus
    rcases hStatus with ⟨B, hInvB, hCovB, _hDefB, _hSatB, hLicB⟩
    have hBA : B = A := hUnique B hInvB hCovB
    subst B
    exact (assembly_licensed_single_node_iff (A := A) (z := z) (j := j)
      (c := c) (k := k) hNodes).mp hLicB
  · intro hLic
    exact ⟨A, hInv, hCov, hDef, hSat,
      (assembly_licensed_single_node_iff (A := A) (z := z) (j := j)
        (c := c) (k := k) hNodes).mpr hLic⟩

/-- The ontic population target S^theta. Lean keeps this separate from the
posterior that a learner or analyst maintains about it. -/
structure PopulationStatus (Score : Type uScore) where
  prevalence : Score

/-- Posterior summaries of a population status target. The stochastic model
supplies their numerical interpretation; the types prevent the target and its
estimate from being silently identified. -/
structure PosteriorStatus (Score : Type uScore) where
  target : PopulationStatus Score
  mean : Score
  concentration : Score
  epistemicUncertainty : Score
  heterogeneity : Score

/-- A bounded anomaly read-out, typed so values can only be introduced with a
proof of the stated range. -/
structure Anomaly where
  val : Rat
  gt_neg_one : (-1 : Rat) < val
  le_zero : val ≤ 0

/-- A bounded confidence read-out, typed so values can only be introduced with
a proof of the stated range. -/
structure Confidence where
  val : Rat
  nonneg : (0 : Rat) ≤ val
  lt_one : val < 1

structure Readout where
  anomaly : Anomaly
  evidenceConfidence : Confidence
  decisionConfidence : Confidence

theorem anomaly_range (F : Anomaly) :
    (-1 : Rat) < F.val ∧ F.val ≤ 0 :=
  ⟨F.gt_neg_one, F.le_zero⟩

theorem confidence_range (phi : Confidence) :
    (0 : Rat) ≤ phi.val ∧ phi.val < 1 :=
  ⟨phi.nonneg, phi.lt_one⟩

end OVMG
