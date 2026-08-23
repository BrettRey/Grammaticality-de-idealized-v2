# Aristotle audit of the OVMG Lean correspondence

Date: 2026-08-22 (America/Toronto)

Aristotle project: `b185b116-760d-442a-8a7d-a04022fcc3f8`
Aristotle task: `6c8797eb-73d9-4816-8430-01d9cc0358ea`

## Question

Could the structural Lean layer be strengthened without pretending to verify
the stochastic dynamics or empirical linguistic classifications?

## Result

Yes. Aristotle's output supported a bounded extension of the existing
structural correspondence. The useful additions were integrated manually and
replayed against the local sources. The formalization remains a logical
interface check, not a proof of the population model or of any example's
linguistic analysis.

Integrated strengthenings:

- an operator witness with zero current opportunity, showing that opportunity
  is absent from operator membership;
- separate witnesses showing that closure, conventional establishment, and
  public-update configuration are each necessary;
- all four combinations of correct/wrong value and licensed/excluded exponent;
- concrete constructional and exponent-licensing failures, with status restored
  when licensing alone is changed;
- a regular-exponent witness showing that the exponent-licensing relation is
  not uniformly false;
- paired saturation witnesses with a genuinely obligatory dimension, covering
  both supply and omission.

## Scope retained

`LicensingProfile` is explicitly documented as a coarse Boolean interface for
independence proofs. It does not encode posterior means, concentrations, or
unsettled regions. Obligatoriness and value supply remain supplied time-slice
interfaces. The Lean development does not formalize the affine likelihood,
memory, repair process, adoption transition, or stationary regimes.

## Local verification

- `lake build`: passed (6 jobs).
- `lake env lean AxiomAudit.lean`: passed.
- Kernel footprint: only Lean's standard `propext` and, for one finite-list
  argument, `Quot.sound`; the new saturation witnesses require no axioms.
- No project-specific axiom, `sorryAx`, `sorry`, `admit`, `unsafe`,
  `native_decide`, or `implemented_by` is used in the proof sources.

Authoritative files: `formalization/OVMG/Core.lean`,
`formalization/OVMG/OperatorStratum.lean`,
`formalization/OVMG/OperatorBridge.lean`, and
`formalization/AxiomAudit.lean`.
