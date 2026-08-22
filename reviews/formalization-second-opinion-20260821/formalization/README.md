# OVMG Lean Formalization

This directory is a narrow Lean sanity check for the structural core of
Reynolds, *Grammaticality de-idealized*.

It formalizes:

- assemblies and value-matched coverage relative to an inventory;
- hard compatibility as satisfiability of a meet of typed constraints, rather
  than equality of atomic feature values;
- saturation as a derived macro over obligatory dimensions;
- speaker-level licensing and the single-pivotal-node reduction;
- the distinction between a population-status target and a posterior estimate
  of that target;
- bounded anomaly, evidence-confidence, and decision-confidence read-outs.

It intentionally does **not** formalize the Section 4 stochastic claims.
The corrected discounted update, normalized gated choice, omission likelihood,
repair process, within-speaker dependence, and any stationary-regime result
need a probability model beyond this `Std`-only structural scaffold. Those are
tested separately by the v2 simulation contract and, eventually, a joint
likelihood.

This artifact proves consequences of a fixed construction inventory and a
fixed constraint algebra. It does not prove that a particular linguistic
analysis supplies the right inventory or constraints.

Build:

```bash
cd formalization
lake build
```
