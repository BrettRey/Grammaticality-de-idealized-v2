# Aristotle Lean hardening record

Project `e736b57b-ded2-48a8-a914-3d6beda42f78`, task `1d57f08d-1cd7-4150-8868-0cb10ec936fa`. The returned source was independently diffed, selectively adopted, rebuilt locally under Lean 4.31, scanned for forbidden proof shortcuts, and checked with `#print axioms`. The local project source is authoritative.

# Summary of changes for run 1d57f08d-1cd7-4150-8868-0cb10ec936fa
Hardened the Std-only Lean 4.31 scaffold in `OVMG/Core.lean`. The project builds from scratch with no warnings, and contains no `sorry`/`admit`, no new axioms (only the declared structure-law fields), no `native_decide`, `unsafe`, or `implemented_by`. All theorems check out on `propext`/`Quot.sound`/`Classical.choice` only.

What changed:

1. **Lawful constraint algebra.** `ConstraintAlgebra` now carries `meet_top` (unit), `meet_comm`, `meet_assoc`, `meet_idem`, `satisfiable_top`, and `satisfiable_of_meet_left` (downward projection). Derived: `top_meet`, `satisfiable_of_meet_right`, `meet_left_comm`. A docstring records that the paper writes this information-combination operation as a join, while Lean writes it as `meet` under the dual constraint-strength order with `top` as the empty constraint.

2. **Contribution-based assemblies.** `Assembly` now has a single field `contributions : List (Node × Constraint)` with `contributions_ne_nil`; `nodes` and `constraints` are derived by projection. Empty assemblies (vacuously licensed / vacuously compatible) and node/constraint list incoherence are therefore unrepresentable; `nodes_ne_nil`, `constraints_ne_nil`, `exists_node`, and `exists_licensed_node_of_licensedNodes` record that licensing is a real demand.

3. **New theorems.** `not_def_of_unsatisfiable_constraint` / `not_def_of_unsatisfiable_contribution` (a clash dooms the assembly), the converse `satisfiable_contribution_of_def`, `no_speaker_status_of_clash`, and `def_perm_contributions` (hard compatibility is invariant under permutation of the contributions), supported by `Combined_cons`, `satisfiable_of_mem_of_satisfiable_combined`, and `Combined_perm`. All existing coverage, saturation, and single-node theorems are retained, with the single-node results restated over a single contribution `[(k, q)]`; `def_single_contribution_iff` was added.

4. **Time-slice interface documented.** `obl` and `supplies` remain primitive parameters, with a docstring stating that this is a fixed time-slice interface: Lean does not derive ontic obligatoriness, does not model its change over time, and proves nothing about the correctness of a given `supplies` relation.

5. **Rat-valued status types.** `PopulationStatus` now carries a rational `prevalence` with `0 ≤ p ≤ 1`. `PosteriorStatus` is a Beta posterior with positive pseudo-counts `a, b`, keeping `target` inside; `concentration = a + b`, `mean = a/(a+b)`, `epistemicUncertainty = C(1-C)/(K+1)` and `heterogeneity = C(1-C)K/(K+1)` are *derived*, not stored. Proved: `mean_range` (mean in [0,1]), `concentration_pos`, `epistemicUncertainty_nonneg`, `heterogeneity_nonneg`, and `uncertainty_decomposition` : `U_epi + U_het = C(1-C)`, where `C` is the posterior mean (noted in the docstring, since the identity is a statement about the central estimate, not the concentration).

6. **Split confidence types.** `EvidenceConfidence` (`0 ≤ val < 1`) and `DecisionConfidence` (`1/2 ≤ val ≤ 1`) replace the single `Confidence`; `Readout` and the range theorems (`evidence_confidence_range`, `decision_confidence_range`, `readout_confidences_range`, plus `decision_confidence_nonneg`) were updated accordingly.

Additionally, small `Rat` helper lemmas were proved from the core API (the project has no Mathlib), and non-vacuity witnesses (`boolConstraintAlgebra`, `unitAssembly`, `uniformPosterior`) were added so the assumed structure laws are known to be satisfiable.

The submitted layout has no `formalization/README.md`; the project's own `README.md` (which describes exactly this artifact) was updated to match the hardened scope. All work is committed and pushed.
