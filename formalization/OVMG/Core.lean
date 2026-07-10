import Std

/-!
# OVMG structural sanity checks

This file formalizes the type-level core of the paper's revised Section 3.
It is deliberately narrow: it checks the structural relations among coverage,
hard compatibility, saturation, licensing, status existence, and the bounded
subjective read-out. It does not attempt to prove the stochastic convergence
claims in Section 4.
-/

namespace OVMG

universe uForm uValue uFrame uDim uOpVal uNode uCtx uScore

/-- A partial operator assignment maps dimensions to optional values. -/
abbrev OpAssign (Dim : Type uDim) (OpVal : Type uOpVal) :=
  Dim -> Option OpVal

/-- Two partial operator assignments are compatible iff any overlapping
defined dimension receives the same value. -/
def Compatible {Dim : Type uDim} {OpVal : Type uOpVal}
    (ω₁ ω₂ : OpAssign Dim OpVal) : Prop :=
  ∀ d x y, ω₁ d = some x -> ω₂ d = some y -> x = y

/-- A concrete clash between two partial assignments. -/
def Clash {Dim : Type uDim} {OpVal : Type uOpVal}
    (ω₁ ω₂ : OpAssign Dim OpVal) : Prop :=
  ∃ d x y, ω₁ d = some x ∧ ω₂ d = some y ∧ x ≠ y

/-- An assembly is a filled tree of constructional nodes, represented here only
by the data needed for the status definition. -/
structure Assembly
    (Form : Type uForm) (Value : Type uValue) (Frame : Type uFrame)
    (Dim : Type uDim) (OpVal : Type uOpVal) (Node : Type uNode) where
  form : Form
  value : Value
  frame : Frame
  nodes : List Node
  ops : List (OpAssign Dim OpVal)

variable {Form : Type uForm} {Value : Type uValue} {Frame : Type uFrame}
variable {Dim : Type uDim} {OpVal : Type uOpVal} {Node : Type uNode}
variable {Ctx : Type uCtx}

local notation "Asm" => Assembly Form Value Frame Dim OpVal Node

/-- Value-matched coverage. -/
def Covers (A : Asm) (f : Form) (v : Value) : Prop :=
  A.form = f ∧ A.value = v

/-- Hard operator compatibility: all operator contributions in an assembly
must unify pairwise. -/
def Def (A : Asm) : Prop :=
  ∀ ω ∈ A.ops, ∀ ω' ∈ A.ops, Compatible ω ω'

/-- A dimension is supplied when some operator assignment defines it. -/
def Supplies (A : Asm) (d : Dim) : Prop :=
  ∃ ω ∈ A.ops, ∃ x, ω d = some x

/-- Saturation of the obligatory dimensions derived for the assembly's frame. -/
def Sat (obl : Ctx -> Frame -> Dim -> Prop) (A : Asm) (c : Ctx) : Prop :=
  ∀ d, obl c A.frame d -> Supplies A d

/-- Node-level licensing for every constructional node in an assembly. -/
def LicensedNodes (L : Node -> Ctx -> Prop) (A : Asm) (c : Ctx) : Prop :=
  ∀ κ ∈ A.nodes, L κ c

/-- Non-empty coverage relative to an independently fixed inventory. -/
def CoverageNonempty (inventory : Asm -> Prop) (f : Form) (v : Value) : Prop :=
  ∃ A, inventory A ∧ Covers A f v

/-- The theta-conditional status proposition: a licensed route to the
form--value pair exists. -/
def ExistsStatus (inventory : Asm -> Prop) (L : Node -> Ctx -> Prop)
    (obl : Ctx -> Frame -> Dim -> Prop) (f : Form) (v : Value)
    (c : Ctx) : Prop :=
  ∃ A, inventory A ∧ Covers A f v ∧ Def A ∧ Sat obl A c ∧ LicensedNodes L A c

theorem compatible_refl (ω : OpAssign Dim OpVal) :
    Compatible ω ω := by
  intro d x y hx hy
  rw [hx] at hy
  cases hy
  rfl

theorem not_compatible_of_clash {ω₁ ω₂ : OpAssign Dim OpVal}
    (h : Clash ω₁ ω₂) : ¬ Compatible ω₁ ω₂ := by
  intro hcompat
  rcases h with ⟨d, x, y, hx, hy, hxy⟩
  exact hxy (hcompat d x y hx hy)

theorem not_def_of_clash_in_assembly {A : Asm}
    {ω₁ ω₂ : OpAssign Dim OpVal}
    (h₁ : ω₁ ∈ A.ops) (h₂ : ω₂ ∈ A.ops)
    (hclash : Clash ω₁ ω₂) : ¬ Def A := by
  intro hdef
  exact not_compatible_of_clash hclash (hdef ω₁ h₁ ω₂ h₂)

theorem clashing_assembly_not_status_witness {A : Asm}
    {ω₁ ω₂ : OpAssign Dim OpVal}
    (h₁ : ω₁ ∈ A.ops) (h₂ : ω₂ ∈ A.ops)
    (hclash : Clash ω₁ ω₂)
    (obl : Ctx -> Frame -> Dim -> Prop) (L : Node -> Ctx -> Prop) (c : Ctx) :
    ¬ (Def A ∧ Sat obl A c ∧ LicensedNodes L A c) := by
  intro h
  exact not_def_of_clash_in_assembly h₁ h₂ hclash h.1

theorem not_sat_of_missing_obligatory {A : Asm}
    {obl : Ctx -> Frame -> Dim -> Prop} {c : Ctx} {d : Dim}
    (hobl : obl c A.frame d) (hmissing : ¬ Supplies A d) :
    ¬ Sat obl A c := by
  intro hsat
  exact hmissing (hsat d hobl)

theorem existsStatus_implies_coverage
    {inventory : Asm -> Prop} {L : Node -> Ctx -> Prop}
    {obl : Ctx -> Frame -> Dim -> Prop} {f : Form} {v : Value} {c : Ctx} :
    ExistsStatus inventory L obl f v c -> CoverageNonempty inventory f v := by
  intro h
  rcases h with ⟨A, hInv, hCov, _hDef, _hSat, _hLic⟩
  exact ⟨A, hInv, hCov⟩

theorem no_status_of_empty_coverage
    {inventory : Asm -> Prop} {L : Node -> Ctx -> Prop}
    {obl : Ctx -> Frame -> Dim -> Prop} {f : Form} {v : Value} {c : Ctx}
    (hEmpty : ¬ CoverageNonempty inventory f v) :
    ¬ ExistsStatus inventory L obl f v c := by
  intro hStatus
  exact hEmpty (existsStatus_implies_coverage hStatus)

theorem assembly_licensed_single_node_iff {A : Asm}
    {L : Node -> Ctx -> Prop} {c : Ctx} {κ : Node}
    (hNodes : A.nodes = [κ]) :
    LicensedNodes L A c ↔ L κ c := by
  constructor
  · intro h
    apply h κ
    rw [hNodes]
    simp
  · intro h κ' hmem
    rw [hNodes] at hmem
    simp at hmem
    rw [hmem]
    exact h

theorem existsStatus_unique_single_node_iff {A : Asm}
    {inventory : Asm -> Prop} {L : Node -> Ctx -> Prop}
    {obl : Ctx -> Frame -> Dim -> Prop} {f : Form} {v : Value} {c : Ctx}
    {κ : Node}
    (hInv : inventory A) (hCov : Covers A f v) (hDef : Def A)
    (hSat : Sat obl A c)
    (hUnique : ∀ B, inventory B -> Covers B f v -> B = A)
    (hNodes : A.nodes = [κ]) :
    ExistsStatus inventory L obl f v c ↔ L κ c := by
  constructor
  · intro hStatus
    rcases hStatus with ⟨B, hInvB, hCovB, _hDefB, _hSatB, hLicB⟩
    have hBA : B = A := hUnique B hInvB hCovB
    subst B
    exact (assembly_licensed_single_node_iff (A := A) (L := L) (c := c)
      (κ := κ) hNodes).mp hLicB
  · intro hL
    exact ⟨A, hInv, hCov, hDef, hSat,
      (assembly_licensed_single_node_iff (A := A) (L := L) (c := c)
        (κ := κ) hNodes).mpr hL⟩

/-- Abstract scalar type for posterior summaries. The stochastic model supplies
the interpretation; Lean only enforces the separation between the existence
proposition and its posterior summaries. -/
structure StatusEstimate (Score : Type uScore) where
  existsVariable : Prop
  mean : Score
  concentration : Score

/-- A bounded anomaly read-out, typed so values can only be introduced with a
proof of the stated range. -/
structure Anomaly where
  val : Rat
  gt_neg_one : (-1 : Rat) < val
  le_zero : val ≤ 0

/-- A bounded confidence read-out, typed so values can only be introduced with a
proof of the stated range. -/
structure Confidence where
  val : Rat
  nonneg : (0 : Rat) ≤ val
  lt_one : val < 1

structure Readout where
  anomaly : Anomaly
  confidence : Confidence

theorem anomaly_range (F : Anomaly) :
    (-1 : Rat) < F.val ∧ F.val ≤ 0 :=
  ⟨F.gt_neg_one, F.le_zero⟩

theorem confidence_range (Φ : Confidence) :
    (0 : Rat) ≤ Φ.val ∧ Φ.val < 1 :=
  ⟨Φ.nonneg, Φ.lt_one⟩

end OVMG
