"""Which temporal meaning can a learner recover from the same P/Q history?

Run: python3 experiments/compatibility/shared_history.py

Both learners observe one independently sampled tutor per opportunity. In a
closed-past niche P competes with Q. A is the exposure adverb. B's lexical
time interval is already known, but P+B never occurs in training. Full
transfer of the relevant closed-past feature is a hypothesis of both models.
Locking is instantaneous, followed by an uninterrupted locked state until
the stated end time. The meaning candidates come from neon-model-theory.json.

Hard: a fraction a of the population licenses some closed-past analysis.
Among those, fraction b licenses reference-interval attachment, which permits
P when the door has since reopened. The remainder uses event attachment,
which preserves the requirement that the result hold at speech time. The
original, unmodified analysis clashes with the adverb in both scenes.
After exposure an imitating learner adopts one sampled repertoire and retains
it across the no-feedback probes.

Graded: a is a continuous compatibility for a matching event and persistent
result; b discounts compatibility when the result has ceased. Both are
properties of one learner's mapping. At the training payoff r0, scale each
cost so its probability of producing P matches the hard population. This
predeclared matching makes the two accounts serious observational rivals:
it gives neither a head start on any training history. It is one possible
graded rival, distinct from the delta-rule proposal in rival.json.

Learning: with independent uniform priors on a and b, both learners update
by Bayes' rule using all the P choices and Q omissions. Restrictions b=1
(changed temporal contribution) and b=0 (persistence obligatory) can also
be tested. The priors and lapse rates are illustrative. This is an exact
finite-fragment likelihood with no forgetting or population turnover. The
population is inferred from choices rather than directly observed gates,
as distinguished in formal-dynamics.tex. This experiment introduces an
imitation rule and two candidate analyses; it does not fit the full OVMG.

Readout: on a truth probe a hard learner answers from the adopted analysis.
A graded learner endorses with probability equal to compatibility. Both have
independent report slips. For paired probes, both retain the same draw from
their posterior throughout. Positive dependence from posterior uncertainty
therefore enters both predictions. Choice slips are separate from truth
reports. Neither model receives the test response during training.

Identification: at the training payoff both learners give the choice P
probability slip + (1-2*slip)*r0*g, where g=a in persistent scenes and
g=a*b in reopened scenes. Every history consisting only of persistent scenes
therefore leaves the independent prior on b intact. With a fixed payoff and
independent tutors, identical pointwise likelihoods imply identical posteriors
for both learners for ANY sequence of P/Q choices, including reopened scenes.

The stable hard repertoire and independent graded truth reports do separate
on repeated probes. For two reopened B tokens their joint-positive difference
is (1-2*truth_slip)^2 E[g*(1-g) | history]. A persistent response criterion
in the graded model removes that difference: draw U uniformly on [0,1] once
per learner and endorse a scene when U <= g, before independent slips. The
three ranges U <= a*b, a*b < U <= a and U > a have exactly the hard type
probabilities. This duplicates the entire joint truth-response law on these
scenes, for any number of probes. The location of persistence remains open.
"""

from dataclasses import dataclass
from math import exp

import numpy as np
from numpy.polynomial.legendre import leggauss

from payoff import soft_choice


TRAIN_SHARE = 0.5
CHOICE_SLIP = 0.05
TRUTH_SLIP = 0.05
INTERVALS = {"A": (-4, -2), "B": (-8, -6)}
NOW = 0


@dataclass(frozen=True)
class Scene:
    adverb: str
    event: int
    locked_until: int

    def readings(self):
        """(event attachment, changed marker) under the two temporal clauses."""
        left, right = INTERVALS[self.adverb]
        event_matches = left <= self.event <= right
        # R is a positive-length interval inside the adverb's interval.
        # After the event, S must hold through the right endpoint of R.
        broad = any(start <= self.event <= end <= self.locked_until
                    for start in range(left, right)
                    for end in range(start + 1, right + 1))
        return event_matches and self.locked_until >= NOW, broad


A_STILL = Scene("A", -3, NOW)
A_REOPENED = Scene("A", -3, -2)
B_STILL = Scene("B", -7, NOW)
B_REOPENED = Scene("B", -7, -6)

# (scene, # P, # Q). Each history has six P choices and eighteen Q choices.
# The two mixed histories also have identical counts of both scene types.
HISTORIES = {
    "still only": [(A_STILL, 6, 18)],
    "P only while still locked": [(A_STILL, 6, 6), (A_REOPENED, 0, 12)],
    "P equally often after reopening": [(A_STILL, 3, 9), (A_REOPENED, 3, 9)],
}


def hard_types(a, b, scene):
    narrow, broad = scene.readings()
    return ((1 - a, False), (a * (1 - b), narrow), (a * b, broad))


def compatibility(a, b, scene):
    narrow, broad = scene.readings()
    if narrow:
        return a
    return a * b if broad else 0 * a


def observed(p, slip):
    return slip + (1 - 2 * slip) * p


def production(model, a, b, scene, share):
    if model == "hard":
        p = sum(mass * licensed * share for mass, licensed in hard_types(a, b, scene))
    elif model == "graded":
        g = compatibility(a, b, scene)
        # Invert graded production once at r0. The learned odds weight stays
        # fixed when the paraphrase payoff, and hence share, changes at test.
        weight = g * (1 - TRAIN_SHARE) / (1 - TRAIN_SHARE * g)
        p = soft_choice(share, weight)
    else:
        raise ValueError(model)
    return observed(p, CHOICE_SLIP)


def posterior(model, history, fixed_b=None, order=32):
    nodes, weights = leggauss(order)
    a = ((nodes + 1) / 2)[:, None]
    weights = weights / 2
    if fixed_b is None:
        b = a.T
        likelihood_mass = np.outer(weights, weights)
    else:
        b = np.array([[fixed_b]])
        likelihood_mass = weights[:, None].copy()
    for scene, count_p, count_q in history:
        p = production(model, a, b, scene, TRAIN_SHARE)
        likelihood_mass *= p**count_p * (1 - p)**count_q
    evidence = likelihood_mass.sum()  # likelihood of one specified ordering
    return a, b, likelihood_mass / evidence, evidence


def truth(model, a, b, scene, probes=1):
    """Probability of 'true' on every probe, conditional on a,b."""
    if model == "hard":
        return sum(mass * observed(licensed, TRUTH_SLIP)**probes
                   for mass, licensed in hard_types(a, b, scene))
    if model == "graded":
        return observed(compatibility(a, b, scene), TRUTH_SLIP)**probes
    raise ValueError(model)


def delta_transfer(choices):
    """Claude's original ordered update and B readout from rival.json."""
    strength = 0.0
    for choice in choices:
        strength += 0.3 * ((choice == "P") - strength)
    return 1 / (1 + exp(-(0.75 * strength - 0.4) / 0.2))


def run():
    assert A_STILL.readings() == B_STILL.readings() == (True, True)
    assert A_REOPENED.readings() == B_REOPENED.readings() == (False, True)
    assert Scene("B", A_STILL.event, NOW).readings() == (False, False)
    print("Shared priors; 'both true' uses two reopened B tokens per learner.")
    print("history | E[b] | Pr(true B: still / reopened) | "
          "both true H/G | produce B reopened H/G at r=.75 | BF(b=1:b=0)")
    for name, history in HISTORIES.items():
        a, b, mass, _ = posterior("hard", history)
        np.testing.assert_allclose(mass, posterior("graded", history)[2])
        def mean(x):
            return float(np.sum(mass * x))

        for scene in (B_STILL, B_REOPENED):
            np.testing.assert_allclose(truth("hard", a, b, scene) -
                                       truth("graded", a, b, scene), 0, atol=1e-14)
        still = mean(truth("hard", a, b, B_STILL))
        reopened = mean(truth("hard", a, b, B_REOPENED))
        pair = [mean(truth(m, a, b, B_REOPENED, 2)) for m in ("hard", "graded")]
        g = compatibility(a, b, B_REOPENED)
        np.testing.assert_allclose(pair[0] - pair[1],
                                   (1 - 2 * TRUTH_SLIP)**2 * mean(g * (1 - g)))
        productions = [mean(production(m, a, b, B_REOPENED, .75))
                       for m in ("hard", "graded")]
        _, _, _, broad_evidence = posterior("hard", history, fixed_b=1)
        _, _, _, narrow_evidence = posterior("graded", history, fixed_b=0)
        print(f"{name} | {mean(b):.3f} | {still:.3f}/{reopened:.3f} | "
              f"{pair[0]:.3f}/{pair[1]:.3f} | "
              f"{productions[0]:.3f}/{productions[1]:.3f} | "
              f"{broad_evidence/narrow_evidence:.4g}")

    print("Still-only exposure, restricted readings, truth of reopened B:")
    for model, setting in (("hard", 1), ("graded", 0), ("graded", 1), ("hard", 0)):
        a, b, mass, _ = posterior(model, HISTORIES["still only"], fixed_b=setting)
        print(f"{model}, b={setting}: {(mass * truth(model, a, b, B_REOPENED)).sum():.3f}")

    # Two orderings of the identical still-only block. The stationary
    # Bayesian learner uses the same sufficient counts for either sequence.
    # The original delta learner forecasts a generic P-response on B. It
    # supplies no independent truth conditions for the reopened scene.
    print("Original delta learner, still-only history, P-response on B:")
    for period in ("PQQQ", "QQQP"):
        print(f"  {period} repeated six times: {delta_transfer(period * 6):.3f}")


if __name__ == "__main__":
    run()
