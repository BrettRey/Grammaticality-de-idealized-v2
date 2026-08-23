import OVMG.Core
import OVMG.OperatorStratum

/-!
# Bridge between OVMG status and operator membership

The main OVMG status scaffold and the operator-stratum interface answer
different questions. This module checks their composition. In particular, an
assembly with no operator contribution can be represented explicitly by the
constraint algebra's empty constraint `top`; operator compatibility can then be
trivial while constructional licensing still fails.
-/

namespace OVMG
namespace OperatorBridge

open OperatorStratum

universe uForm uValue uFrame uDim uConstraint uNode uCtx uSpeaker uUpdate

variable {Form : Type uForm} {Value : Type uValue} {Frame : Type uFrame}
variable {Dim : Type uDim} {Constraint : Type uConstraint} {Node : Type uNode}
variable {Ctx : Type uCtx} {Speaker : Type uSpeaker} {Update : Type uUpdate}

local notation "Asm" => Assembly Form Value Frame Constraint Node

/-- Every constraint carried by the assembly is the empty constraint. This is
the explicit bridge representation of an assembly with no operator-value
compatibility demand. -/
def OperatorNeutral (alg : ConstraintAlgebra Constraint) (A : Asm) : Prop :=
  ∀ q ∈ A.constraints, q = alg.top

theorem combined_eq_top_of_all_top (alg : ConstraintAlgebra Constraint) :
    ∀ {constraints : List Constraint},
      (∀ q ∈ constraints, q = alg.top) -> Combined alg constraints = alg.top := by
  intro constraints hTop
  induction constraints with
  | nil => rfl
  | cons q qs ih =>
      rw [Combined_cons, hTop q (by simp), alg.top_meet]
      apply ih
      intro r hr
      exact hTop r (by simp [hr])

/-- An operator-neutral assembly is hard-compatible. This does not license any
of its constructional nodes. -/
theorem def_of_operatorNeutral
    {alg : ConstraintAlgebra Constraint} {A : Asm}
    (h : OperatorNeutral alg A) : Def alg A := by
  rw [Def, combined_eq_top_of_all_top alg h]
  exact alg.satisfiable_top

def AssemblyInContrast
    (P : Contrast Value Ctx Update) (A : Asm) : Prop :=
  P.eligible A.value

theorem assemblyInContrast_of_covers
    {P : Contrast Value Ctx Update} {A : Asm} {f : Form} {v : Value}
    (hCovers : Covers A f v) (hEligible : P.eligible v) :
    AssemblyInContrast P A := by
  unfold AssemblyInContrast
  rw [hCovers.2]
  exact hEligible

/-- Constructional licensing can block status even when coverage,
compatibility, and saturation are otherwise available. -/
theorem no_speaker_status_of_all_covering_unlicensed
    {inventory : Asm -> Prop} {alg : ConstraintAlgebra Constraint}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker}
    {f : Form} {v : Value} {c : Ctx}
    (hUnlicensed : ∀ A, inventory A -> Covers A f v ->
      ¬ LicensedNodes z j A c) :
    ¬ SpeakerStatus inventory alg obl supplies z j f v c := by
  intro hStatus
  rcases hStatus with ⟨A, hInv, hCov, _hDef, _hSat, hLic⟩
  exact (hUnlicensed A hInv hCov) hLic

/-- Explicitly separates operator compatibility from constructional licensing:
neutrality supplies `Def`, but a separate node-licensing failure still blocks
speaker status.

Both hypotheses quantify over covering inventory members, so the statement
would be uninformative for an inventory with no covering assembly. The
concrete witnesses below use inventories that contain a covering assembly. -/
theorem neutral_compatibility_does_not_supply_licensing
    {inventory : Asm -> Prop} {alg : ConstraintAlgebra Constraint}
    {obl : Ctx -> Frame -> Dim -> Prop} {supplies : Asm -> Dim -> Prop}
    {z : Speaker -> Node -> Ctx -> Prop} {j : Speaker}
    {f : Form} {v : Value} {c : Ctx}
    (hNeutral : ∀ A, inventory A -> Covers A f v -> OperatorNeutral alg A)
    (hUnlicensed : ∀ A, inventory A -> Covers A f v ->
      ¬ LicensedNodes z j A c) :
    (∀ A, inventory A -> Covers A f v -> Def alg A) ∧
      ¬ SpeakerStatus inventory alg obl supplies z j f v c := by
  constructor
  · intro A hInv hCov
    exact def_of_operatorNeutral (hNeutral A hInv hCov)
  · exact no_speaker_status_of_all_covering_unlicensed hUnlicensed

/-! ## Concrete bridge witnesses -/

def neverObligatory (_ : Unit) (_ : Unit) (_ : Unit) : Prop := False

def suppliesNoDimension
    {F : Type uForm} {V : Type uValue} {Q : Type uConstraint}
    {N : Type uNode}
    (_ : Assembly F V Unit Q N) (_ : Unit) : Prop :=
  False

theorem saturated_when_nothing_obligatory
    {F : Type uForm} {V : Type uValue} {Q : Type uConstraint}
    {N : Type uNode} (A : Assembly F V Unit Q N) :
    Sat neverObligatory suppliesNoDimension A () := by
  intro d hObl
  exact False.elim hObl

/-! The preceding helper covers the vacuous no-obligation boundary. These
paired witnesses also exercise saturation with a real obligatory dimension. -/

def unitDimensionObligatory (_ : Unit) (_ : Unit) (_ : Unit) : Prop := True

def suppliesEveryUnitDimension
    {F : Type uForm} {V : Type uValue} {Q : Type uConstraint}
    {N : Type uNode}
    (_ : Assembly F V Unit Q N) (_ : Unit) : Prop :=
  True

theorem saturated_with_obligatory_unit
    {F : Type uForm} {V : Type uValue} {Q : Type uConstraint}
    {N : Type uNode} (A : Assembly F V Unit Q N) :
    Sat unitDimensionObligatory suppliesEveryUnitDimension A () := by
  intro _d _hObl
  trivial

theorem not_saturated_when_obligatory_unit_missing
    {F : Type uForm} {V : Type uValue} {Q : Type uConstraint}
    {N : Type uNode} (A : Assembly F V Unit Q N) :
    ¬ Sat unitDimensionObligatory suppliesNoDimension A () := by
  intro hSat
  exact hSat () (by trivial)

/-- A `depend of`-shaped witness: the contrast is not update-configuring, its
assembly is operator-neutral and saturated, but its constructional node is not
licensed. -/
def nonOperatorAssembly :
    Assembly Unit BinaryValue Unit Bool Unit where
  form := ()
  value := .first
  frame := ()
  contributions := [((), true)]
  contributions_ne_nil := by simp

def nonOperatorInventory
    (A : Assembly Unit BinaryValue Unit Bool Unit) : Prop :=
  A = nonOperatorAssembly

def noUnitNodeLicensed (_ : Unit) (_ : Unit) (_ : Unit) : Prop := False

def nonOperatorSpeakerStatus : Prop :=
  SpeakerStatus nonOperatorInventory boolConstraintAlgebra neverObligatory
    suppliesNoDimension noUnitNodeLicensed () () .first ()

theorem nonOperatorAssembly_neutral :
    OperatorNeutral boolConstraintAlgebra nonOperatorAssembly := by
  intro q hq
  change q = true
  simpa [Assembly.constraints, nonOperatorAssembly] using hq

theorem nonOperatorAssembly_defined :
    Def boolConstraintAlgebra nonOperatorAssembly :=
  def_of_operatorNeutral nonOperatorAssembly_neutral

theorem nonOperatorAssembly_saturated :
    Sat neverObligatory suppliesNoDimension nonOperatorAssembly () :=
  saturated_when_nothing_obligatory nonOperatorAssembly

theorem nonOperatorAssembly_in_constant_contrast :
    AssemblyInContrast constantContrast nonOperatorAssembly := by
  trivial

theorem nonOperatorAssembly_covers : Covers nonOperatorAssembly () .first :=
  ⟨rfl, rfl⟩

theorem nonOperatorAssembly_not_licensed :
    ¬ LicensedNodes noUnitNodeLicensed () nonOperatorAssembly () := by
  intro hLicensed
  exact hLicensed () (by simp [Assembly.nodes, nonOperatorAssembly])

theorem nonOperatorAssembly_not_status : ¬ nonOperatorSpeakerStatus := by
  apply no_speaker_status_of_all_covering_unlicensed
  intro A hInv _hCov
  unfold nonOperatorInventory at hInv
  subst A
  exact nonOperatorAssembly_not_licensed

/-- The same node relation with the constructional node licensed. -/
def allUnitNodesLicensed (_ : Unit) (_ : Unit) (_ : Unit) : Prop := True

def nonOperatorSpeakerStatusIfLicensed : Prop :=
  SpeakerStatus nonOperatorInventory boolConstraintAlgebra neverObligatory
    suppliesNoDimension allUnitNodesLicensed () () .first ()

/-- Node licensing is the only obstacle: changing it alone restores speaker
status. -/
theorem nonOperatorAssembly_status_if_licensed :
    nonOperatorSpeakerStatusIfLicensed :=
  ⟨nonOperatorAssembly, rfl, nonOperatorAssembly_covers,
    nonOperatorAssembly_defined, nonOperatorAssembly_saturated,
    fun _ _ => trivial⟩

/-- The constructional failure is located precisely: inventory membership,
coverage, compatibility, and saturation all hold; node licensing and speaker
status fail; changing node licensing alone restores status. -/
theorem nonoperator_constructional_failure_witness :
    ¬ IsOperator conventionallyEstablished constantContrast ∧
    AssemblyInContrast constantContrast nonOperatorAssembly ∧
    nonOperatorInventory nonOperatorAssembly ∧
    Covers nonOperatorAssembly () .first ∧
    Def boolConstraintAlgebra nonOperatorAssembly ∧
    Sat neverObligatory suppliesNoDimension nonOperatorAssembly () ∧
    ¬ LicensedNodes noUnitNodeLicensed () nonOperatorAssembly () ∧
    ¬ nonOperatorSpeakerStatus ∧
    nonOperatorSpeakerStatusIfLicensed :=
  ⟨constantContrast_not_operator,
    nonOperatorAssembly_in_constant_contrast,
    rfl,
    nonOperatorAssembly_covers,
    nonOperatorAssembly_defined,
    nonOperatorAssembly_saturated,
    nonOperatorAssembly_not_licensed,
    nonOperatorAssembly_not_status,
    nonOperatorAssembly_status_if_licensed⟩

/-- A `goed`/`le hiver`-shaped witness: the operator value is intact, the
assembly is compatible and saturated, but its excluded exponent node is not
licensed. -/
def excludedExponentAssembly :
    Assembly Unit BinaryValue Unit Bool BinaryExponent where
  form := ()
  value := .second
  frame := ()
  contributions := [(.excluded, true)]
  contributions_ne_nil := by simp

def excludedExponentInventory
    (A : Assembly Unit BinaryValue Unit Bool BinaryExponent) : Prop :=
  A = excludedExponentAssembly

def binaryExponentNodeLicensed
    (_ : Unit) (exponent : BinaryExponent) (_ : Unit) : Prop :=
  allowedBinaryExponent .second exponent

def excludedExponentSpeakerStatus : Prop :=
  SpeakerStatus excludedExponentInventory boolConstraintAlgebra neverObligatory
    suppliesNoDimension binaryExponentNodeLicensed () () .second ()

theorem excludedExponentAssembly_defined :
    Def boolConstraintAlgebra excludedExponentAssembly := by
  apply def_of_operatorNeutral
  intro q hq
  change q = true
  simpa [Assembly.constraints, excludedExponentAssembly] using hq

theorem excludedExponentAssembly_saturated :
    Sat neverObligatory suppliesNoDimension excludedExponentAssembly () :=
  saturated_when_nothing_obligatory excludedExponentAssembly

theorem excludedExponentAssembly_not_licensed :
    ¬ LicensedNodes binaryExponentNodeLicensed () excludedExponentAssembly () := by
  intro hLicensed
  exact hLicensed .excluded
    (by simp [Assembly.nodes, excludedExponentAssembly])

theorem excludedExponentAssembly_not_status :
    ¬ excludedExponentSpeakerStatus := by
  apply no_speaker_status_of_all_covering_unlicensed
  intro A hInv _hCov
  unfold excludedExponentInventory at hInv
  subst A
  exact excludedExponentAssembly_not_licensed

/-- The corresponding construction with a licensed exponent node. -/
def regularExponentAssembly :
    Assembly Unit BinaryValue Unit Bool BinaryExponent where
  form := ()
  value := .second
  frame := ()
  contributions := [(.regular, true)]
  contributions_ne_nil := by simp

def regularExponentInventory
    (A : Assembly Unit BinaryValue Unit Bool BinaryExponent) : Prop :=
  A = regularExponentAssembly

def regularExponentSpeakerStatus : Prop :=
  SpeakerStatus regularExponentInventory boolConstraintAlgebra neverObligatory
    suppliesNoDimension binaryExponentNodeLicensed () () .second ()

theorem regularExponentAssembly_defined :
    Def boolConstraintAlgebra regularExponentAssembly := by
  apply def_of_operatorNeutral
  intro q hq
  change q = true
  simpa [Assembly.constraints, regularExponentAssembly] using hq

/-- The licensing relation is not vacuously false: with the regular exponent,
and nothing else changed, speaker status holds. -/
theorem regularExponentAssembly_status : regularExponentSpeakerStatus := by
  refine ⟨regularExponentAssembly, rfl, ⟨rfl, rfl⟩,
    regularExponentAssembly_defined,
    saturated_when_nothing_obligatory regularExponentAssembly, ?_⟩
  intro k hk
  have hkEq : k = BinaryExponent.regular := by
    simpa [Assembly.nodes, regularExponentAssembly] using hk
  subst hkEq
  trivial

/-- The value/exponent failure is located precisely: operator membership,
value correctness, coverage, compatibility, and saturation all hold; exponent
licensing and speaker status fail; the same licensing relation licenses the
regular exponent. -/
theorem value_intact_exponent_failure_bridge :
    IsOperator conventionallyEstablished binaryOperatorContrast ∧
    ValueCorrect valueIntactExcludedToken ∧
    ¬ ExponentLicensed allowedBinaryExponent valueIntactExcludedToken ∧
    excludedExponentInventory excludedExponentAssembly ∧
    Covers excludedExponentAssembly () .second ∧
    Def boolConstraintAlgebra excludedExponentAssembly ∧
    Sat neverObligatory suppliesNoDimension excludedExponentAssembly () ∧
    ¬ LicensedNodes binaryExponentNodeLicensed () excludedExponentAssembly () ∧
    ¬ excludedExponentSpeakerStatus ∧
    regularExponentSpeakerStatus :=
  ⟨binaryOperator_isOperator, rfl,
    by simp [ExponentLicensed, allowedBinaryExponent, valueIntactExcludedToken],
    rfl, ⟨rfl, rfl⟩, excludedExponentAssembly_defined,
    excludedExponentAssembly_saturated,
    excludedExponentAssembly_not_licensed,
    excludedExponentAssembly_not_status,
    regularExponentAssembly_status⟩

end OperatorBridge
end OVMG
