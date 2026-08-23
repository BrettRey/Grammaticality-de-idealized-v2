# OVMG Lean Formalization

This directory is a narrow Lean sanity check for the structural core of
Reynolds, *Grammaticality de-idealized*.

It formalizes:

- a lawful constraint algebra: information combination is an idempotent
  commutative monoid with a satisfiable unit, and satisfiability projects from
  a combination to each conjunct. The paper writes this operation as a join on
  an information order; Lean writes it as `meet` under the dual
  constraint-strength order;
- assemblies as nonempty lists of node--constraint contributions, making empty
  assemblies and incoherent node/constraint lists unrepresentable;
- value-matched coverage relative to an inventory;
- hard compatibility as satisfiability of the combined typed constraints,
  together with proofs that a clash dooms an assembly and that compatibility
  is invariant under permutation of the contributions;
- saturation as a derived macro over obligatory dimensions;
- speaker-level licensing and the single-pivotal-node reduction;
- a rational population-status target in `[0,1]` and a Beta posterior with
  derived mean, concentration, epistemic uncertainty, and heterogeneity;
- bounds on those summaries and the moment identity
  `U_epi + U_het = C(1-C)`;
- distinct bounded types for anomaly, evidence confidence, and decision
  confidence.

Two further modules check a partial interface to the operator stratum. The paper
identifies paradigms categorically for its comparison and then assigns them a
graded operator profile. This interface is a Boolean surrogate for logical
independence proofs:

- `OVMG/OperatorStratum.lean`: a partial predicate over a contrast (finite
  eligible-value set, conventionality, non-vacuous extensional public-update
  role), with proofs that the predicate is independent of opportunity and the
  categorical licensing verdict, that each conjunct is necessary, and that
  selected-value correctness and exponent licensing vary independently. Its
  Boolean `LicensingProfile` is only a coarse interface for those proofs; it
  does not represent a recurring domain, semantic frame, obligatory value
  selection, graded operator profile, posterior means, concentration, or
  unsettled regions;
- `OVMG/OperatorBridge.lean`: the composition of that interface with the status
  scaffold, including the fact that an assembly contributing only the empty
  constraint is hard-compatible, while speaker status can still fail through
  constructional node non-licensing alone.

`Closed` is enumerability at a fixed analytical time slice, not a complete
paradigm test. `UpdateConfiguring` is a non-vacuity witness rather than a measure
of public-update contribution, and conventionality is a parameter. Empirical
paradigm identification, operator profiling, and causal attribution are
therefore supplied by linguistic analysis rather than proved here.

`obl` and `supplies` remain primitive parameters at a fixed time slice. Lean
does not derive ontic obligatoriness, model its temporal evolution, or certify
that a proposed supply relation is linguistically correct. The constraint laws
are likewise assumptions on the supplied algebra; concrete non-vacuity
witnesses show that those assumptions are jointly satisfiable. Paired
saturation witnesses exercise both supply and failure when a unit dimension is
genuinely obligatory, alongside the explicit no-obligation boundary case.

It intentionally does **not** formalize the Section 4 stochastic claims.
The corrected discounted update, normalized gated choice, omission likelihood,
repair process, within-speaker dependence, and any stationary-regime result
need a probability model beyond this `Std`-only structural scaffold. Those are
tested separately by the v2 simulation contract and, eventually, a joint
likelihood.

This artifact proves consequences of a fixed construction inventory, lawful
constraint algebra, and time-slice interface. It does not prove that a
particular linguistic analysis supplies the right inventory, constraints,
obligatory dimensions, or values.

Build:

```bash
cd formalization
lake build
lake env lean AxiomAudit.lean
```
