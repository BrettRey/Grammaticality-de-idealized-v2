import OVMG

/-!
Kernel-footprint audit for representative OVMG structural results.

Run with `lake env lean AxiomAudit.lean`. The `#print axioms` commands report
the constants on which each theorem depends; no theorem may depend on `sorryAx`
or a project-specific axiom declaration.
-/

#print axioms OVMG.OperatorStratum.binaryOperator_isOperator
#print axioms OVMG.OperatorStratum.isSituatedOperator_withProfile
#print axioms OVMG.OperatorStratum.operator_with_no_opportunity
#print axioms OVMG.OperatorStratum.binaryOperator_fails_operator_by_convention_only
#print axioms OVMG.OperatorStratum.openValueContrast_fails_operator_by_closure_only
#print axioms OVMG.OperatorStratum.value_and_exponent_independent
#print axioms OVMG.OperatorStratum.value_correct_exponent_unlicensed_consistent
#print axioms OVMG.OperatorStratum.wrong_value_can_change_update
#print axioms OVMG.OperatorBridge.neutral_compatibility_does_not_supply_licensing
#print axioms OVMG.OperatorBridge.saturated_with_obligatory_unit
#print axioms OVMG.OperatorBridge.not_saturated_when_obligatory_unit_missing
#print axioms OVMG.OperatorBridge.nonoperator_constructional_failure_witness
#print axioms OVMG.OperatorBridge.value_intact_exponent_failure_bridge
#print axioms OVMG.OperatorBridge.regularExponentAssembly_status
