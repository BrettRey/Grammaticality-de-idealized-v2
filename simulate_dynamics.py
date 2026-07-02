#!/usr/bin/env python3
"""
Deterministic licensing-posterior trajectories for Figure `posterior-means`.

Beta(1,1) prior updated by a constant per-step effective preemption mass p
(the b-parameter grows by p each step; no positive evidence). Two regimes:

    rare : p = 0.01  (tiny opportunity set -> posterior stays near prior, wide)
    gap  : p = 5.00  (dense preemption   -> posterior falls AND concentrates)

Emits the posterior mean and the 2.5% / 97.5% quantiles of Beta(1, 1 + p*t),
the exact coordinates hard-coded in the figure's pgfplots block. The point of
the figure is the *dispersion* contrast, not only the mean, so the credible
band is part of the output, not an afterthought.

Reproduce:  python3 simulate_dynamics.py > simulation_data.dat
"""
import sys

STEPS = 50
REGIMES = {"rare": 0.01, "gap": 5.0}
A0, B0 = 1.0, 1.0


def beta_quantile_a1(b, q):
    """Quantile of Beta(1, b): F(x) = 1 - (1-x)**b, so x = 1 - (1-q)**(1/b)."""
    return 1.0 - (1.0 - q) ** (1.0 / b)


def trajectory(p):
    rows = []
    for t in range(STEPS):
        a, b = A0, B0 + p * t
        mean = a / (a + b)
        lo = beta_quantile_a1(b, 0.025)
        hi = beta_quantile_a1(b, 0.975)
        rows.append((t, mean, lo, hi))
    return rows


def main():
    traj = {name: trajectory(p) for name, p in REGIMES.items()}
    out = sys.stdout
    out.write("step\trare_mean\trare_lo\trare_hi\tgap_mean\tgap_lo\tgap_hi\n")
    for t in range(STEPS):
        r, g = traj["rare"][t], traj["gap"][t]
        out.write(
            f"{t}\t{r[1]:.4f}\t{r[2]:.4f}\t{r[3]:.4f}"
            f"\t{g[1]:.4f}\t{g[2]:.4f}\t{g[3]:.4f}\n"
        )


if __name__ == "__main__":
    main()
