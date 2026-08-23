#!/usr/bin/env python3
"""Reproduce the trajectories in Figure ``posterior-means``.

The prior is Beta(1, 1). Each attributable omission contributes the affine
likelihood factor ``1 - d * theta`` with ``d = .495``. The sparse arm receives
one omission after each block of ten steps; the dense arm receives a batch of
five omissions at every step. After each step, the exact finite Beta mixture
is projected back to a Beta distribution by matching its first two moments,
exactly as specified in equation ``beta-update`` of the formal supplement.

Requires SciPy. Reproduce with::

    python3 simulate_dynamics.py > simulation_data.dat
"""

from math import exp, lgamma
import sys

from scipy.stats import beta as beta_distribution


STEPS = 50
D = 0.495
A0 = 1.0
B0 = 1.0


def beta_function(a, b):
    """Return B(a, b), evaluated through log-gamma for numerical stability."""
    return exp(lgamma(a) + lgamma(b) - lgamma(a + b))


def affine_omission_update(a, b, omission_count, d=D):
    """Moment-project ``Beta(a,b) * (1-d*theta)**m`` to Beta."""
    if omission_count == 0:
        return a, b

    # In the Bernstein basis, (1-d*theta)^m is a positive sum of terms
    # theta^k (1-theta)^(m-k). Build those coefficients one omission at a time.
    coefficients = [1.0]
    for _ in range(omission_count):
        next_coefficients = [0.0] * (len(coefficients) + 1)
        for k, coefficient in enumerate(coefficients):
            next_coefficients[k] += coefficient
            next_coefficients[k + 1] += (1.0 - d) * coefficient
        coefficients = next_coefficients

    components = []
    normalizer = 0.0
    for k, coefficient in enumerate(coefficients):
        component_a = a + k
        component_b = b + omission_count - k
        weight = coefficient * beta_function(component_a, component_b)
        components.append((weight, component_a, component_b))
        normalizer += weight

    mean = 0.0
    second_moment = 0.0
    for weight, component_a, component_b in components:
        probability = weight / normalizer
        total = component_a + component_b
        mean += probability * component_a / total
        second_moment += (
            probability
            * component_a
            * (component_a + 1.0)
            / (total * (total + 1.0))
        )

    variance = second_moment - mean * mean
    concentration = mean * (1.0 - mean) / variance - 1.0
    return mean * concentration, (1.0 - mean) * concentration


def summarize(a, b):
    """Return mean and central 95% interval for a Beta distribution."""
    mean = a / (a + b)
    lower = beta_distribution.ppf(0.025, a, b)
    upper = beta_distribution.ppf(0.975, a, b)
    return mean, lower, upper


def trajectories():
    """Return sparse and dense summaries for steps zero through ``STEPS``."""
    sparse_a, sparse_b = A0, B0
    dense_a, dense_b = A0, B0
    rows = [(0, summarize(sparse_a, sparse_b), summarize(dense_a, dense_b))]

    for step in range(1, STEPS + 1):
        sparse_batch = 1 if step % 10 == 0 else 0
        sparse_a, sparse_b = affine_omission_update(
            sparse_a, sparse_b, sparse_batch
        )
        dense_a, dense_b = affine_omission_update(dense_a, dense_b, 5)
        rows.append(
            (step, summarize(sparse_a, sparse_b), summarize(dense_a, dense_b))
        )
    return rows


def main():
    out = sys.stdout
    out.write(
        "step\tsparse_mean\tsparse_lo\tsparse_hi"
        "\tdense_mean\tdense_lo\tdense_hi\n"
    )
    for step, sparse, dense in trajectories():
        out.write(
            f"{step}\t{sparse[0]:.4f}\t{sparse[1]:.4f}\t{sparse[2]:.4f}"
            f"\t{dense[0]:.4f}\t{dense[1]:.4f}\t{dense[2]:.4f}\n"
        )


if __name__ == "__main__":
    main()
