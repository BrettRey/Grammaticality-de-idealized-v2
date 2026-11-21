"""A finite identification test for the perfect/closed-past fragment.

Run with python3 experiments/compatibility/payoff.py (NumPy and SciPy).
Manuscript claim: grammaticality-de-idealized.tex, "Change requires a new
analysis". Hard compatibility is defined in section3.tex at def(A).
The production gate and the independently normed full-choice share are in
formal-dynamics.tex, "Dynamics: evidence streams" and the preceding equations.

Fragment: P on its old reading requires an open reference interval. A and B
supply a closed interval. A second analysis of P permits that closed interval.
Both readings have coverage and all other obligatory dimensions supplied.
The two hard inventories have the old reading alone or both readings. The
new analysis licenses both P+A and P+B. The competitor Q expresses the same
intended message. Its availability is fixed. All other available options
(including avoidance) can be pooled in the denominator. Use A in training,
B as a held-out adverb. The calculations condition on one history and on B.

r in (0,1) is the probability of choosing P when all options are available at the
given payoff. Its value is assumed known from an independent control and
common to both hard inventories. Calibration must transport to the target.
A stable fraction h of speakers have a compatible P-route. Their full-choice
rate is r; the others cannot produce P for this value. Thus p_hard = h*r.
For recovery, randomize independent speakers to arms and observe one choice
each. Repeated trials of a speaker with a stable gate require another likelihood.

The graded learner in rival.json updates W <- W + eta*(outcome - W) on
training opportunities (P succeeds = 1, competitor wins = 0). At transfer,
s = overlap*W. Its logistic choice with a competitor offset gives an odds
multiplier w = exp((s-s_ref)/temperature) relative to an intact reference
strength s_ref. We restrict s <= s_ref and hold strength and payoff sensitivity
fixed across test arms. This bounded comparison fits w at one history; it
does not estimate the learning rate or overlap. The hard model likewise fits
one prevalence at that history. Both can transfer to B.

Writing d(r,w) = 1-r+r*w, p_soft/r = w/d(r,w). Between r1 < r2 the
increment in this ratio is (r2-r1)*w*(1-w)/(d(r1,w)*d(r2,w)). This holds
pointwise. For any common distribution of w on [0,1] the expected contrast
is positive iff the distribution has positive mass on (0,1). Mixtures of
the two endpoint inventories have exactly zero contrast. This identifies
interior effective costs under the measurement assumptions; ordinary costs
of retrieving a categorical analysis would enter the same odds multiplier.

At one payoff both models cover the entire interval (0,r]. We include w=0
as the limiting case of infinite cost when discussing the closed hull.
For ANY joint kernel K of responses conditional on the
chosen route D, the likelihood P(D)*K(interpretation,repair,confidence|D)
also agrees when both use the same K and choose D at the matched rate. For
a choice of P to index one route, P must be unambiguous in the elicited niche.
The within-speaker paired example below relaxes that shared-kernel assumption.

Possible design: supply matched closed-past training histories, randomize the
payoff for the always-available paraphrase at test, and offer avoidance in
both arms. Estimate the two intact shares in separate all-routes-available
controls. Elicit the target on the untrained closed-past adverb, once per
speaker, without feedback. A separate meaning probe should distinguish a
changed reference interval from recovery of the intended event time. The
gate interpretation requires evidence that payoff leaves the intended value,
available analyses and processing costs fixed. Calibration error, or hard
access that depends on payoff, can produce a positive contrast. The recovery
calculation takes r as known, so its sample sizes do not power a human study.
"""

from fractions import Fraction as F
from itertools import product

import numpy as np
from scipy.stats import beta, binom


def soft_choice(r, weight):
    return r * weight / (1 - r + r * weight)


def check_witnesses():
    r1, r2 = F(1, 4), F(3, 4)
    h = F(1, 2)
    weight = h * (1 - r1) / (1 - h * r1)
    hard = (h * r1, h * r2)
    soft = tuple(soft_choice(r, weight) for r in (r1, r2))
    assert hard == (F(1, 8), F(3, 8))
    assert soft == (F(1, 8), F(9, 16))

    # A payoff-dependent gate duplicates both cells exactly.
    assert tuple(p / r for p, r in zip(soft, (r1, r2))) == (h, F(3, 4))
    # Enumerate the fixed-inventory hull: vertices (0,0) and (r1,r2).
    vertices = [(z * r1, z * r2) for z in (0, 1)]
    assert all(y * r1 == x * r2 for x, y in vertices)
    assert hard[1] * r1 == hard[0] * r2
    assert soft[1] * r1 > soft[0] * r2
    for w in (F(i, 16) for i in range(17)):
        contrast = soft_choice(r2, w) / r2 - soft_choice(r1, w) / r1
        assert (contrast > 0) == (0 < w < 1)
    print(f"Calibrated shares {r1}, {r2}; gate {h}: {hard[0]}, {hard[1]}; "
          f"weight {weight}: {soft[0]}, {soft[1]}")

    # One speaker, repeated no-feedback tokens. Hard retrieval samples one
    # of two available analyses on each token. Conditional reporting error
    # is 1/10 on each probe. Compare a direct graded readout with independent
    # noise per probe, then allow the graded learner one shared decode.
    pi, error = F(327, 400), F(1, 10)
    marginal = error + (1 - 2 * error) * pi

    def pair(rate, first, second):
        return (rate if first else 1 - rate) * (rate if second else 1 - rate)

    cells = list(product((0, 1), repeat=2))
    joint = [(1 - pi) * pair(error, i, a) + pi * pair(1 - error, i, a)
             for i, a in cells]
    separate = [pair(marginal, i, a) for i, a in cells]
    assert sum(joint) == sum(separate) == 1
    assert sum(joint[2:]) == sum(separate[2:]) == marginal
    assert joint[1] + joint[3] == separate[1] + separate[3] == marginal
    assert joint[3] - marginal**2 == pi * (1 - pi) * (1 - 2 * error)**2
    # With a shared decode of probability pi, either architecture uses joint.
    # Hard resampling per probe gives separate exactly.
    print(f"Paired marginals {float(marginal):.3f}; P(both positive): "
          f"shared decode {float(joint[3]):.6f}, separate draws {float(separate[3]):.6f}")


def probability_intervals(n):
    """Two Clopper-Pearson intervals with simultaneous coverage >= 95%."""
    k = np.arange(n + 1)
    tail = 0.05 / 4
    lo, hi = np.zeros(n + 1), np.ones(n + 1)
    lo[1:] = beta.ppf(tail, k[1:], n - k[1:] + 1)
    hi[:-1] = beta.ppf(1 - tail, k[:-1] + 1, n - k[:-1])
    return lo, hi


def fitting_tables(model, shares, intervals):
    """For each possible two-arm count table, does a common parameter fit?"""
    def inverse(p, r):
        if model == "gate":
            return p / r
        with np.errstate(divide="ignore"):
            return p * (1 - r) / (r * (1 - p))

    bounds = [(inverse(intervals[0], r), inverse(intervals[1], r))
              for r in shares]
    low = np.maximum.outer(bounds[0][0], bounds[1][0])
    high = np.minimum.outer(bounds[0][1], bounds[1][1])
    return low <= np.minimum(high, 1)


def cross_recovery(n, shares):
    """Integrate both fits over all (n+1)^2 count tables, without sampling."""
    counts = np.arange(n + 1)
    intervals = probability_intervals(n)
    gate, cost = (fitting_tables(m, shares, intervals) for m in ("gate", "cost"))
    if shares[0] == shares[1]:
        assert np.array_equal(gate, cost)
    masks = [gate & ~cost, cost & ~gate, gate & cost, ~gate & ~cost]
    print(f"n={n} per arm, full-choice shares={shares}")
    for name, rates in (
        ("gate", [0.5 * r for r in shares]),
        ("cost", [soft_choice(r, 3 / 7) for r in shares]),
        ("intact", shares),
    ):
        mass = np.outer(*(binom.pmf(counts, n, rate) for rate in rates))
        probs = [mass[m].sum() for m in masks]
        assert np.isclose(sum(probs), 1)
        if name in ("gate", "intact"):
            assert mass[gate].sum() >= 0.95 - 1e-12
        if name in ("cost", "intact"):
            assert mass[cost].sum() >= 0.95 - 1e-12
        print(f"  {name:6s}  " + "  ".join(f"{p:.5f}" for p in probs))


if __name__ == "__main__":
    check_witnesses()
    print("Generating model | gate only | cost only | both | neither")
    cross_recovery(64, (0.25, 0.25))
    for trials in (64, 256, 1024):
        cross_recovery(trials, (0.25, 0.75))
