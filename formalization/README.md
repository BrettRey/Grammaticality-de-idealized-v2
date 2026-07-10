# OVMG Lean Formalization

This directory is a small Lean sanity check for the revised formal core of
“Grammaticality de-idealized.”

It formalizes only the structural layer:

- assemblies, value-matched coverage, and inventories;
- hard operator compatibility as pairwise unification of partial assignments;
- saturation as a macro over obligatory dimensions;
- node-level licensing and theta-conditional status existence;
- the single-pivotal-node reduction;
- bounded types for the anomaly and confidence read-outs.

It deliberately does **not** formalize the stochastic dynamics in Section 4:
Beta updating, bounded-memory stationary distributions, repair-flow control, and
bimodality are mathematical-model and simulation targets rather than current Lean
targets.

Build:

```bash
cd formalization
lake build
```
