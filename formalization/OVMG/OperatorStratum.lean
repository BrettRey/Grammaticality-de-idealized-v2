import Std

/-!
# Operator-stratum interface

This module checks type and level distinctions used at the interface between
OVMG and the operator-stratum paper. Paradigm identification is categorical for
the paper's comparison, and the operator profile is graded. The Boolean predicate
below is a partial core-interface surrogate used only where the formal scaffold needs a discrete
inventory. It does not infer paradigm status, operator profile, or causal
attribution from judgment data. Instead, it proves
that this surrogate, opportunity, categorical licensing, value correctness, and
exponent licensing can vary independently in the combinations claimed.

`Closed` is a fixed-analysis enumerability surrogate, not a complete test of the
recurring domain, semantic frame, or obligatory selection needed to identify a
living paradigm.
`UpdateConfiguring` is only a non-vacuity condition: two eligible values have
different effects on an abstract public-update state somewhere. It does not
measure the magnitude or ordinary-use reach of that contribution. Whether and
how strongly an identified paradigm has that contribution is supplied by
empirical analysis, not proved here.
-/

namespace OVMG
namespace OperatorStratum

universe uValue uCtx uUpdate uExponent

/-- A candidate contrast with an eligibility condition on values and an
extensional effect on a public-update state. -/
structure Contrast
    (Value : Type uValue) (Ctx : Type uCtx) (Update : Type uUpdate) where
  eligible : Value -> Prop
  update : Value -> Ctx -> Update -> Update

/-- Closure at a fixed analytical time slice: the eligible values can be
enumerated without duplication. -/
def Closed {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    (P : Contrast Value Ctx Update) : Prop :=
  ∃ values : List Value, values.Nodup ∧ ∀ v, P.eligible v ↔ v ∈ values

/-- Public-update configuration: some pair of eligible values has a different
effect in the same context and prior update state. -/
def UpdateConfiguring
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    (P : Contrast Value Ctx Update) : Prop :=
  ∃ v₁ v₂ c s,
    P.eligible v₁ ∧ P.eligible v₂ ∧ P.update v₁ c s ≠ P.update v₂ c s

/-- This partial core-interface predicate belongs to the contrast, not to a
token. It requires Boolean surrogates for closure, independent conventionality,
and a non-vacuous public-update role, but it omits other empirical requirements
for paradigm identification and operator profiling. -/
def IsCoreOperator
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    (conventional : Contrast Value Ctx Update -> Prop)
    (P : Contrast Value Ctx Update) : Prop :=
  Closed P ∧ conventional P ∧ UpdateConfiguring P

/-- Backwards-compatible internal name. This abbreviation denotes the partial
core-interface surrogate, not the paper's full paradigm/profile architecture. -/
abbrev IsOperator
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    (conventional : Contrast Value Ctx Update -> Prop)
    (P : Contrast Value Ctx Update) : Prop :=
  IsCoreOperator conventional P

theorem distinct_values_of_updateConfiguring
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    {P : Contrast Value Ctx Update} (h : UpdateConfiguring P) :
    ∃ v₁ v₂, P.eligible v₁ ∧ P.eligible v₂ ∧ v₁ ≠ v₂ := by
  rcases h with ⟨v₁, v₂, c, s, hv₁, hv₂, hUpdate⟩
  refine ⟨v₁, v₂, hv₁, hv₂, ?_⟩
  intro hEq
  subst v₂
  exact hUpdate rfl

/-! ## Licensing profiles stay outside the core-interface surrogate -/

/-- A deliberately small profile sufficient to state the independence claims.
It is a coarse logical interface, not the paper's posterior state: `licensed`
and `categorical` collapse graded means, concentrations, and unsettled regions
to Boolean verdicts solely so the operator/licensing independence claims can be
checked. `categorical` records concentration of that verdict, not operator
categorization. -/
structure LicensingProfile where
  opportunity : Nat
  licensed : Bool
  categorical : Bool
  deriving DecidableEq, Repr

/-- A contrast paired with a licensing profile. -/
structure SituatedContrast
    (Value : Type uValue) (Ctx : Type uCtx) (Update : Type uUpdate) where
  contrast : Contrast Value Ctx Update
  profile : LicensingProfile

def IsSituatedOperator
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    (conventional : Contrast Value Ctx Update -> Prop)
    (S : SituatedContrast Value Ctx Update) : Prop :=
  IsOperator conventional S.contrast

def SituatedContrast.withProfile
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    (S : SituatedContrast Value Ctx Update) (profile : LicensingProfile) :
    SituatedContrast Value Ctx Update :=
  { S with profile := profile }

/-- Changing opportunity, concentration, or the licensing verdict cannot by
itself change the sharpened classification: those fields are absent from its
definition. -/
@[simp] theorem isSituatedOperator_withProfile
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    {conventional : Contrast Value Ctx Update -> Prop}
    (S : SituatedContrast Value Ctx Update) (profile : LicensingProfile) :
    IsSituatedOperator conventional (S.withProfile profile) ↔
      IsSituatedOperator conventional S := by
  rfl

def CategoricallyLicensed (profile : LicensingProfile) : Prop :=
  profile.categorical = true ∧ profile.licensed = true

def CategoricallyUnlicensed (profile : LicensingProfile) : Prop :=
  profile.categorical = true ∧ profile.licensed = false

/-! ## Token-level value and exponent questions -/

structure TokenAnalysis (Value : Type uValue) (Exponent : Type uExponent) where
  intendedValue : Value
  selectedValue : Value
  exponent : Exponent

def ValueCorrect
    {Value : Type uValue} {Exponent : Type uExponent}
    (token : TokenAnalysis Value Exponent) : Prop :=
  token.selectedValue = token.intendedValue

def WrongValue
    {Value : Type uValue} {Exponent : Type uExponent}
    (token : TokenAnalysis Value Exponent) : Prop :=
  token.selectedValue ≠ token.intendedValue

def ExponentLicensed
    {Value : Type uValue} {Exponent : Type uExponent}
    (allowed : Value -> Exponent -> Prop)
    (token : TokenAnalysis Value Exponent) : Prop :=
  allowed token.selectedValue token.exponent

def UpdateResult
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    {Exponent : Type uExponent}
    (P : Contrast Value Ctx Update) (token : TokenAnalysis Value Exponent)
    (c : Ctx) (s : Update) : Update :=
  P.update token.selectedValue c s

theorem updateResult_eq_intended_of_valueCorrect
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    {Exponent : Type uExponent}
    {P : Contrast Value Ctx Update} {token : TokenAnalysis Value Exponent}
    {c : Ctx} {s : Update} (h : ValueCorrect token) :
    UpdateResult P token c s = P.update token.intendedValue c s := by
  rw [UpdateResult, h]

theorem updateResult_ne_intended_of_distinct_effect
    {Value : Type uValue} {Ctx : Type uCtx} {Update : Type uUpdate}
    {Exponent : Type uExponent}
    {P : Contrast Value Ctx Update} {token : TokenAnalysis Value Exponent}
    {c : Ctx} {s : Update}
    (h : P.update token.selectedValue c s ≠
      P.update token.intendedValue c s) :
    UpdateResult P token c s ≠ P.update token.intendedValue c s := by
  exact h

/-! ## Finite non-vacuity and independence witnesses -/

inductive BinaryValue where
  | first
  | second
  deriving DecidableEq, Repr

inductive BinaryUpdate where
  | initial
  | firstSet
  | secondSet
  deriving DecidableEq, Repr

inductive BinaryExponent where
  | regular
  | excluded
  deriving DecidableEq, Repr

def binaryOperatorContrast : Contrast BinaryValue Unit BinaryUpdate where
  eligible := fun _ => True
  update := fun value _ _ =>
    match value with
    | .first => .firstSet
    | .second => .secondSet

def constantContrast : Contrast BinaryValue Unit BinaryUpdate where
  eligible := fun _ => True
  update := fun _ _ _ => .initial

def conventionallyEstablished
    (_ : Contrast BinaryValue Unit BinaryUpdate) : Prop :=
  True

theorem binaryOperator_closed : Closed binaryOperatorContrast := by
  refine ⟨[.first, .second], by decide, ?_⟩
  intro value
  cases value <;> simp [binaryOperatorContrast]

theorem binaryOperator_updateConfiguring :
    UpdateConfiguring binaryOperatorContrast := by
  refine ⟨.first, .second, (), .initial, by trivial, by trivial, ?_⟩
  decide

theorem binaryOperator_isOperator :
    IsOperator conventionallyEstablished binaryOperatorContrast := by
  exact ⟨binaryOperator_closed, by trivial,
    binaryOperator_updateConfiguring⟩

theorem constantContrast_closed : Closed constantContrast := by
  refine ⟨[.first, .second], by decide, ?_⟩
  intro value
  cases value <;> simp [constantContrast]

theorem constantContrast_not_updateConfiguring :
    ¬ UpdateConfiguring constantContrast := by
  rintro ⟨v₁, v₂, c, s, _hv₁, _hv₂, hUpdate⟩
  exact hUpdate rfl

theorem constantContrast_not_operator :
    ¬ IsOperator conventionallyEstablished constantContrast := by
  intro h
  exact constantContrast_not_updateConfiguring h.2.2

def categoricalLicensedProfile : LicensingProfile where
  opportunity := 100
  licensed := true
  categorical := true

def categoricalUnlicensedProfile : LicensingProfile where
  opportunity := 100
  licensed := false
  categorical := true

def operatorLicensedCase : SituatedContrast BinaryValue Unit BinaryUpdate where
  contrast := binaryOperatorContrast
  profile := categoricalLicensedProfile

def operatorUnlicensedCase : SituatedContrast BinaryValue Unit BinaryUpdate where
  contrast := binaryOperatorContrast
  profile := categoricalUnlicensedProfile

def nonOperatorLicensedCase : SituatedContrast BinaryValue Unit BinaryUpdate where
  contrast := constantContrast
  profile := categoricalLicensedProfile

def nonOperatorUnlicensedCase : SituatedContrast BinaryValue Unit BinaryUpdate where
  contrast := constantContrast
  profile := categoricalUnlicensedProfile

theorem operator_and_categorically_licensed_consistent :
    ∃ S : SituatedContrast BinaryValue Unit BinaryUpdate,
      IsSituatedOperator conventionallyEstablished S ∧
      CategoricallyLicensed S.profile := by
  refine ⟨operatorLicensedCase, binaryOperator_isOperator, ?_⟩
  exact ⟨rfl, rfl⟩

theorem operator_and_categorically_unlicensed_consistent :
    ∃ S : SituatedContrast BinaryValue Unit BinaryUpdate,
      IsSituatedOperator conventionallyEstablished S ∧
      CategoricallyUnlicensed S.profile := by
  refine ⟨operatorUnlicensedCase, binaryOperator_isOperator, ?_⟩
  exact ⟨rfl, rfl⟩

theorem nonoperator_and_categorically_licensed_consistent :
    ∃ S : SituatedContrast BinaryValue Unit BinaryUpdate,
      ¬ IsSituatedOperator conventionallyEstablished S ∧
      CategoricallyLicensed S.profile := by
  refine ⟨nonOperatorLicensedCase, constantContrast_not_operator, ?_⟩
  exact ⟨rfl, rfl⟩

theorem nonoperator_and_categorically_unlicensed_consistent :
    ∃ S : SituatedContrast BinaryValue Unit BinaryUpdate,
      ¬ IsSituatedOperator conventionallyEstablished S ∧
      CategoricallyUnlicensed S.profile := by
  refine ⟨nonOperatorUnlicensedCase, constantContrast_not_operator, ?_⟩
  exact ⟨rfl, rfl⟩

/-- A profile with no opportunity and no recorded licensing verdict. -/
def noOpportunityProfile : LicensingProfile where
  opportunity := 0
  licensed := false
  categorical := false

/-- Concrete counterpart of `isSituatedOperator_withProfile` for opportunity:
the same contrast is still an operator when its opportunity count is zero. -/
theorem operator_with_no_opportunity :
    IsSituatedOperator conventionallyEstablished
        (operatorLicensedCase.withProfile noOpportunityProfile) ∧
      (operatorLicensedCase.withProfile noOpportunityProfile).profile.opportunity
        = 0 :=
  ⟨binaryOperator_isOperator, rfl⟩

def allowedBinaryExponent (_ : BinaryValue) (exponent : BinaryExponent) : Prop :=
  match exponent with
  | .regular => True
  | .excluded => False

def valueIntactExcludedToken : TokenAnalysis BinaryValue BinaryExponent where
  intendedValue := .second
  selectedValue := .second
  exponent := .excluded

def wrongValueToken : TokenAnalysis BinaryValue BinaryExponent where
  intendedValue := .second
  selectedValue := .first
  exponent := .regular

theorem value_correct_exponent_unlicensed_consistent :
    ∃ token : TokenAnalysis BinaryValue BinaryExponent,
      ValueCorrect token ∧ ¬ ExponentLicensed allowedBinaryExponent token := by
  refine ⟨valueIntactExcludedToken, rfl, ?_⟩
  simp [ExponentLicensed, allowedBinaryExponent, valueIntactExcludedToken]

theorem wrong_value_can_change_update :
    ∃ token : TokenAnalysis BinaryValue BinaryExponent,
      WrongValue token ∧
      UpdateResult binaryOperatorContrast token () .initial ≠
        binaryOperatorContrast.update token.intendedValue () .initial := by
  refine ⟨wrongValueToken, ?_, ?_⟩
  · simp [WrongValue, wrongValueToken]
  · simp [UpdateResult, binaryOperatorContrast, wrongValueToken]

/-! ### Each conjunct of the `IsOperator` core-interface surrogate is necessary

For each condition there is a contrast satisfying the other two and failing
that one. `constantContrast` above witnesses failure of
`UpdateConfiguring`; the witnesses here cover conventionality and closure. -/

/-- A conventionality predicate under which no contrast counts as established.
Whether a contrast is conventional is supplied by empirical analysis; Lean
only checks here that the conjunct is not idle. -/
def neverConventional (_ : Contrast BinaryValue Unit BinaryUpdate) : Prop :=
  False

/-- Closure and update configuration alone do not give the core classification. -/
theorem binaryOperator_fails_operator_by_convention_only :
    Closed binaryOperatorContrast ∧
      UpdateConfiguring binaryOperatorContrast ∧
      ¬ IsOperator neverConventional binaryOperatorContrast :=
  ⟨binaryOperator_closed, binaryOperator_updateConfiguring, fun h => h.2.1⟩

/-- A contrast whose eligible values are unbounded and therefore not
enumerable at the fixed analytical time slice. -/
def openValueContrast : Contrast Nat Unit BinaryUpdate where
  eligible := fun _ => True
  update := fun value _ _ =>
    match value with
    | 0 => .firstSet
    | _ + 1 => .secondSet

def alwaysConventional (_ : Contrast Nat Unit BinaryUpdate) : Prop := True

theorem le_foldr_max :
    ∀ values : List Nat, ∀ n ∈ values, n ≤ values.foldr max 0 := by
  intro values
  induction values with
  | nil => intro n hn; cases hn
  | cons a t ih =>
      intro n hn
      rcases List.mem_cons.mp hn with h | h
      · subst h; exact Nat.le_max_left _ _
      · exact Nat.le_trans (ih n h) (Nat.le_max_right _ _)

theorem openValueContrast_not_closed : ¬ Closed openValueContrast := by
  rintro ⟨values, _hNodup, hMem⟩
  have hIn : values.foldr max 0 + 1 ∈ values :=
    (hMem (values.foldr max 0 + 1)).mp trivial
  have hLe := le_foldr_max values _ hIn
  omega

theorem openValueContrast_updateConfiguring :
    UpdateConfiguring openValueContrast := by
  refine ⟨0, 1, (), .initial, trivial, trivial, ?_⟩
  simp [openValueContrast]

/-- Conventionality and update configuration alone do not give the core classification:
an unbounded value set defeats the closure condition. -/
theorem openValueContrast_fails_operator_by_closure_only :
    ¬ Closed openValueContrast ∧
      alwaysConventional openValueContrast ∧
      UpdateConfiguring openValueContrast ∧
      ¬ IsOperator alwaysConventional openValueContrast :=
  ⟨openValueContrast_not_closed, trivial, openValueContrast_updateConfiguring,
    fun h => openValueContrast_not_closed h.1⟩

/-! ### Selected value and exponent licensing vary independently -/

def valueIntactRegularToken : TokenAnalysis BinaryValue BinaryExponent where
  intendedValue := .second
  selectedValue := .second
  exponent := .regular

def wrongValueExcludedToken : TokenAnalysis BinaryValue BinaryExponent where
  intendedValue := .second
  selectedValue := .first
  exponent := .excluded

/-- All four combinations of value correctness and exponent licensing are
realized, so neither question determines the other. -/
theorem value_and_exponent_independent :
    (ValueCorrect valueIntactRegularToken ∧
        ExponentLicensed allowedBinaryExponent valueIntactRegularToken) ∧
      (ValueCorrect valueIntactExcludedToken ∧
        ¬ ExponentLicensed allowedBinaryExponent valueIntactExcludedToken) ∧
      (WrongValue wrongValueToken ∧
        ExponentLicensed allowedBinaryExponent wrongValueToken) ∧
      (WrongValue wrongValueExcludedToken ∧
        ¬ ExponentLicensed allowedBinaryExponent wrongValueExcludedToken) :=
  ⟨⟨rfl, trivial⟩, ⟨rfl, fun h => h⟩,
    ⟨by simp [WrongValue, wrongValueToken], trivial⟩,
    ⟨by simp [WrongValue, wrongValueExcludedToken], fun h => h⟩⟩

/-!
No theorem here routes a token deterministically to a repair response. The
paper's update-oriented versus form-oriented repair claim is probabilistic and
requires an independently measured response model. Lean checks only the prior
logical distinction between changed update value and excluded form.
-/

end OperatorStratum
end OVMG
