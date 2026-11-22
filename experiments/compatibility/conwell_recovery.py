"""Fake-data recovery for the proposed two-verb experiment (NumPy and SciPy).

Each person makes one binary production. Equal-sized groups receive different
probe verbs. The two group counts suffice for all six fixed response laws.
"""
import numpy as np
from scipy.stats import binom, hypergeom

from conwell_learning import paired_predictions


def response_tables(n, rates):
    """Joint count probabilities and a 95% acceptance region for each law."""
    count = np.arange(n + 1)
    saturated = binom.logpmf(count, n, count / n)
    saturated_joint = np.add.outer(saturated, saturated)
    tables, regions = {}, {}
    for model, (first, second) in rates.items():
        log_joint = np.add.outer(binom.logpmf(count, n, float(first)),
                                 binom.logpmf(count, n, float(second)))
        mass = np.exp(log_joint)
        np.testing.assert_allclose(mass.sum(), 1, atol=1e-12, rtol=0)
        # Include the least discrepant tables up to at least 95% mass,
        # retaining ties. Rounding removes floating-point differences in ties.
        deviance = np.round(2 * (saturated_joint - log_joint), 10)
        order = np.argsort(deviance, axis=None)
        cumulative = np.cumsum(mass.ravel()[order])
        cutoff = deviance.ravel()[order[np.searchsorted(cumulative, 0.95)]]
        tables[model] = mass
        regions[model] = deviance <= cutoff
        assert mass[regions[model]].sum() >= 0.95 - 1e-12
    return tables, regions


def fisher_rejections(n):
    """Rejection tables for the two-sided, 5% equal-proportions test."""
    # With equal group sizes the conditional null is symmetric in the two
    # counts. Twice its lower tail gives the two-sided Fisher exact p-value.
    count = np.arange(n + 1)
    lower = np.minimum.outer(count, count)
    total = np.add.outer(count, count)
    return 2 * hypergeom.cdf(lower, 2 * n, total, n) <= 0.05 + 1e-12


def run(n, rates):
    tables, regions = response_tables(n, rates)
    retained = sum(mask.astype(int) for mask in regions.values())
    detect = fisher_rejections(n)
    replicates = 50000
    rng = np.random.default_rng([20261122, n])
    print(f"\n{2*n} people, {n} per probe; probabilities in percent")
    print("generator           verb effect    sole correct     sole wrong      multiple          none")
    for model, mass in tables.items():
        outcomes = (detect, (retained == 1) & regions[model],
                    (retained == 1) & ~regions[model], retained > 1, retained == 0)
        exact = np.array([mass[mask].sum() for mask in outcomes])
        np.testing.assert_allclose(exact[1:].sum(), 1, atol=1e-12, rtol=0)
        print(f"{model:17}" + "".join(f"{100*p:14.2f}" for p in exact))
        # Independent replay with random participant counts. Compare the
        # study-level results with their probabilities from full enumeration.
        first, second = (float(p) for p in rates[model])
        x = rng.binomial(n, first, replicates)
        y = rng.binomial(n, second, replicates)
        replay = np.array([mask[x, y].mean() for mask in outcomes])
        se = np.sqrt(exact * (1 - exact) / replicates)
        assert np.all(np.abs(replay - exact) <= 6 * se + 1 / replicates)
    # With equal prior odds the best rule selects the more probable generator
    # on each table. This bound uses the full response levels in both groups.
    best = np.maximum(tables["graded"], tables["gate+lexical"]).sum() / 2
    print(f"Optimal graded vs gate+lexical accuracy (equal odds): {100*best:.2f}%")


if __name__ == "__main__":
    predictions = paired_predictions()
    for per_probe in (12, 48, 96):
        run(per_probe, predictions)
