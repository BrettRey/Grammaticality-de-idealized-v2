"""Two restricted accounts of the English production and listener tasks.

These are design calculations. None of the probabilities are fitted to English.
"""

from fractions import Fraction

import numpy as np
from scipy.stats import binom

from payoff import fitting_tables, probability_intervals, soft_choice


def decision_inference(rates):
    """Equal prior probabilities for the two hidden speaker goals."""
    reconstruction, decision = rates
    return decision / (reconstruction + decision)


def run():
    shares = (Fraction(1, 5), Fraction(11, 20))
    target = Fraction(1, 100)  # illustration in the reconstruction condition
    gate = target / shares[0]
    odds_cost = target * (1 - shares[0]) / (shares[0] * (1 - target))
    hard = tuple(gate * r for r in shares)
    graded = tuple(soft_choice(r, odds_cost) for r in shares)
    assert hard == (target, Fraction(11, 400))
    assert graded == (target, Fraction(4, 85))
    assert decision_inference(hard) == Fraction(11, 15)
    assert decision_inference(graded) == Fraction(80, 97)
    # An unchanged categorical grammar may allow message repair at different
    # rates in each context. The same listener kernel then gives the same answers.
    access = tuple(p / r for r, p in zip(shares, graded))
    assert all(0 <= h <= 1 for h in access)
    assert tuple(r * h for r, h in zip(shares, access)) == graded
    print("Context-dependent access duplicating the odds model:", *map(str, access))
    for label, rates in (("stable gate", hard), ("graded odds", graded)):
        print(f"{label}: choose perfect {float(rates[0]):.5f}, {float(rates[1]):.5f}; "
              f"infer decision goal given perfect {float(decision_inference(rates)):.5f}, "
              f"given preterite {float(decision_inference(tuple(1-p for p in rates))):.5f}")

    # Exact cross-fits to all possible count tables, with independent speakers
    # per arm and known control shares. A model fits if some common parameter
    # matches the two simultaneous intervals (the existing payoff.py criterion).
    for n in (100, 500):
        counts = np.arange(n + 1)
        intervals = probability_intervals(n)
        gates, costs = (fitting_tables(model, tuple(map(float, shares)), intervals)
                        for model in ("gate", "cost"))
        fits = (gates & ~costs, costs & ~gates, gates & costs, ~gates & ~costs)
        for label, rates in (("gate", hard), ("cost", graded)):
            mass = np.outer(*(binom.pmf(counts, n, float(p)) for p in rates))
            probs = [mass[mask].sum() for mask in fits]
            assert np.isclose(sum(probs), 1)
            assert mass[gates if label == "gate" else costs].sum() >= .95 - 1e-12
            print(f"n={n}, {label} generated, gate only / cost only / both / neither: "
                  + " ".join(f"{p:.6f}" for p in probs))


if __name__ == "__main__":
    run()
