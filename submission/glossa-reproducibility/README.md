# Supplementary File 3: Reproducibility materials

This archive accompanies _Grammaticality de-idealized_. It separates three
kinds of evidence that the paper also keeps distinct:

- `model/` contains the executable quantitative contract, finite-population
  stress tests, declared seeds and parameters, and machine-readable outputs.
- `figure/` contains the Python script and data used for the posterior-trajectory
  figure in Supplementary File 1.
- `formalization/` contains the Lean structural sanity check.
- `corpus/` contains registered COCA agreement queries, the coding scheme, and
  aggregate counts, but no concordance lines.

None of these artifacts is a fit to participant data. The simulations establish
model-internal possibility or failure under declared assumptions. The Lean files
check consequences of supplied structural interfaces; they do not verify the
statistical dynamics or the linguistic classification of an example. In
particular, the Boolean operator predicate is a partial structural surrogate for
the discrete interface. It doesn't formalize the recurring domain, semantic
frame, or obligatory selection used to identify paradigms; the graded operator
profile; or operator-specific causal attribution. The
corpus summaries concern production choice over registered query sets and do
not identify community licensing on their own.

## Tested environment

- Node.js 26.7.0; the JavaScript uses only the standard library.
- Python 3.14.7 with SciPy 1.17.0 for the posterior-trajectory figure.
- Lean 4.31.0, fixed by `formalization/lean-toolchain`.

## Replay

From `model/`:

```bash
make test
make closed-loop
make bifurcation
```

The release suite contains 328 checks. Regenerated results should have these
SHA-256 hashes:

```text
ebfa2a75064bfbbff72d1798a04cea65dff211ac3cf9f567f596ba527ed48679  results/closed-loop-sweep.json
8bd38cab97ed52cbeac474361f6a03c7cecbb767eb81a26ebb23f9ff3feac6c0  results/bifurcation-diagnostics.json
```

From `figure/`:

```bash
python3 simulate_dynamics.py > regenerated-simulation-data.dat
shasum -a 256 regenerated-simulation-data.dat
```

The expected hash is:

```text
2a15f8f517df3aae9555447d200b17dce7b68d9121bb3982900ea5be108200ef
```

From `formalization/`:

```bash
lake build
lake env lean AxiomAudit.lean
```

`SHA256SUMS.txt` records the files distributed in this review archive. The
publication archive will restore the author-identifying software licence after
double-blind review.
