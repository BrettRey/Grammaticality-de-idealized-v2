"""Finite-sample recovery on the four post-disclosure truth cells, one learner per response."""

from itertools import product
from math import ceil

import numpy as np
from scipy.signal import convolve
from scipy.special import logit
from scipy.stats import binom, norm

from menu_disclosure import PATHS, eligible_history, menu_key, recordings
from opportunity_choice import forecast


ALPHA = 0.05
FRACTIONS = (0.0, 0.5, 1.0)


def truth_rates(model):
    trials = recordings(0)
    return np.array([forecast(model, eligible_history(trials, menu_key(path, 0)))[:, 0]
                     for path in PATHS])


def response_rates(full, correct, reversed_key):
    """Remaining learners ignore the key and have the scene-specific midpoint rates."""
    if min(correct, reversed_key) < 0 or correct + reversed_key > 1:
        raise ValueError("Mixture shares must be nonnegative and sum to at most one")
    return (correct * full + reversed_key * full[::-1]
            + (1 - correct - reversed_key) * full.mean(axis=0))


def count_law(n, rates):
    """Distribution of 2n plus the signed endorsement count, in the documented direction."""
    still_key, reopened_key = rates
    # Count a success in the two positive cells and a failure in the two negative cells.
    probs = (reopened_key[0], still_key[1], 1 - still_key[0], 1 - reopened_key[1])
    law = np.ones(1)
    for p in probs:
        law = convolve(law, binom.pmf(np.arange(n + 1), n, p))
    law = np.maximum(law, 0)  # FFT roundoff in the extreme tails
    np.testing.assert_allclose(law.sum(), 1, rtol=1e-10)
    return law / law.sum()


def central_region(law):
    low, high = np.searchsorted(law.cumsum(), (ALPHA / 2, 1 - ALPHA / 2))
    counts = np.arange(len(law))
    return (low <= counts) & (counts <= high)


def power_bound(n, null, alternative):
    """Bound power using the exact likelihood-ratio tails in both four-cell laws."""
    if np.array_equal(null, alternative):
        return ALPHA
    counts = np.arange(n + 1)
    slope = logit(alternative) - logit(null)
    offset = np.log1p(-alternative) - np.log1p(-null)
    log_ratio = counts * slope[..., None] + n * offset[..., None]
    # Any threshold gives a rigorous bound. Use a normal approximation only to pick one.
    mean = n * (null * slope + offset).sum()
    sd = np.sqrt(n * (null * (1 - null) * slope**2).sum())
    threshold = mean + norm.isf(ALPHA) * sd
    # Conditional on the first key's counts, sum the second key's joint tail.
    first = np.add.outer(*log_ratio[0]).ravel()
    second = np.add.outer(*log_ratio[1]).ravel()
    order = second.argsort()
    cut = np.searchsorted(second[order], threshold - first, side="right")

    def tail(rates):
        cells = binom.pmf(counts, n, rates[..., None])
        first_mass = np.multiply.outer(*cells[0]).ravel()
        second_mass = np.multiply.outer(*cells[1]).ravel()[order]
        right_tail = np.append(np.cumsum(second_mass[::-1])[::-1], 0)
        return (first_mass * right_tail[cut]).sum()

    size, hit = tail(null), tail(alternative)
    return min(1.0, hit + np.exp(threshold) * (ALPHA - size))


def verify():
    full = truth_rates("hard")
    np.testing.assert_allclose(full, truth_rates("graded"))
    for key, truth_row in zip(PATHS, full):
        history = eligible_history(recordings(0), menu_key(key, 0))
        for model in ("hard", "graded"):
            np.testing.assert_allclose(forecast(model, history)[:, 1], 0.025 + 0.5 * truth_row)
    np.testing.assert_allclose(response_rates(full, 0.5, 0), response_rates(full, 0.75, 0.25))
    null = response_rates(full, 0, 0)
    np.testing.assert_allclose(null, response_rates(full, 0.5, 0.5))
    np.testing.assert_allclose(power_bound(64, null, null), ALPHA)
    # Independent enumeration of raw counts for two learners per cell.
    n = 2
    direct = np.zeros(4 * n + 1)
    null_mass, full_mass = [], []
    for counts in product(range(n + 1), repeat=4):
        cs, cr, rs, rr = counts
        full_mass.append(binom.pmf(counts, n, full.ravel()).prod())
        null_mass.append(binom.pmf(counts, n, null.ravel()).prod())
        direct[2 * n + rs - cs - rr + cr] += full_mass[-1]
    np.testing.assert_allclose(count_law(n, full), direct)
    equal = np.full_like(full, 0.5)
    np.testing.assert_allclose(count_law(n, equal), binom.pmf(np.arange(4 * n + 1), 4 * n, 0.5))
    # Direct best possible power: spend the .05 null budget on the largest ratios first.
    null_mass, full_mass = np.array(null_mass), np.array(full_mass)
    order = np.argsort(full_mass / null_mass)[::-1]
    sizes = np.r_[0, null_mass[order].cumsum()]
    hits = np.r_[0, full_mass[order].cumsum()]
    best = np.interp(ALPHA, sizes, hits)
    assert best - 1e-12 <= power_bound(n, null, full) <= best + 0.01


def run():
    verify()
    full = truth_rates("hard")
    rates = [response_rates(full, use, 0) for use in FRACTIONS]
    print("Post-key truth judgments only. Columns are probabilities in percent.")
    print("learners  use    retain: no use / half / full    both endpoints   "
          "exclude no use   power ceiling")
    for n in (64, 256, 1024):
        laws = [count_law(n, r) for r in rates]
        # The largest two-sided null tails occur at a .5 response rate in each cell.
        null_region = central_region(binom.pmf(np.arange(4 * n + 1), 4 * n, 0.5))
        regions = [null_region, central_region(laws[1]), central_region(laws[2])]
        for index, (use, r, law) in enumerate(zip(FRACTIONS, rates, laws)):
            coverage = [law[region].sum() for region in regions]
            both = law[null_region & regions[2]].sum()
            reject = law[~null_region].sum()
            ceiling = power_bound(n, rates[0], r)
            assert reject <= ceiling + 1e-10
            assert coverage[index] >= 1 - ALPHA - 1e-10
            retained = " / ".join(f"{100 * p:5.1f}" for p in coverage)
            ceiling_percent = ceil(1000 * ceiling) / 10
            print(f"{4 * n:7d}  {use:4.2f}        {retained}          {100 * both:5.1f}"
                  f"            {100 * reject:5.1f}          {ceiling_percent:5.1f}")


if __name__ == "__main__":
    run()
