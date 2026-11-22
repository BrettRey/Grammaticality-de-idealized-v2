"""Learn the two word orders from training counts and forecast an unheard verb.

Run with Python and NumPy. All likelihoods and forecasts use exact fractions.
Each TrainingVerb describes a distinct lexical item. Counts summarize the
observed order choices for that item. No test responses enter the models.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import cache
from math import prod

from numpy.polynomial import Polynomial


ONE = Polynomial([Fraction(1)])
THETA = Polynomial([Fraction(0), Fraction(1)])
MODELS = ("categorical", "graded", "frequency", "gate+preference")
MEANINGS = ("contact", "posture", "motion")


@dataclass(frozen=True)
class TrainingVerb:
    meaning: str
    agent_first: int
    patient_first: int


def training_history(semantic_cue, repetitions):
    """One illustrative list, with two distinct video examples per trained verb.

    Each row gives the numbers of agent-only, alternating and patient-only
    training verbs for one action class. Learners see only the resulting
    examples. The arbitrary meaning-to-order mapping can be permuted.
    """
    layout = ((4, 0, 0), (0, 4, 0), (0, 0, 4)) if semantic_cue else (
        (2, 1, 1), (1, 2, 1), (1, 1, 2))
    verbs = []
    for meaning, row in zip(MEANINGS, layout, strict=True):
        for count, (agent, patient) in zip(row, ((2, 0), (1, 1), (0, 2)), strict=True):
            verbs.extend(TrainingVerb(meaning, agent * repetitions, patient * repetitions)
                         for _ in range(count))
    return verbs


@cache
def verb_likelihood(model, agent, patient, concentration=1):
    """Probability of the observed order sequence for one verb given theta."""
    if min(agent, patient) < 0:
        raise ValueError("Order counts must be nonnegative")
    if concentration <= 0:
        raise ValueError("The beta prior concentration must be positive")
    if model not in (*MODELS, "gate+lexical"):
        raise ValueError(f"Unknown learner: {model}")
    if agent + patient == 0:
        return ONE
    if model == "frequency":
        return THETA**agent * (1 - THETA)**patient
    if model == "gate+lexical":
        # Half of verbs license both orders and have their own graded choice
        # preference. The remainder are restricted to one order. Both orders
        # observed rules out a singleton repertoire in this error-free toy.
        singleton = (patient == 0) * THETA + (agent == 0) * (1 - THETA)
        return (singleton + verb_likelihood("graded", agent, patient, concentration)) / 2
    if model == "categorical":
        # Two draws for the verb's repertoire. If both orders occur in
        # the repertoire, either is chosen with probability one half.
        mixed = 2 * THETA * (1 - THETA) / 2**(agent + patient)
        return mixed + (patient == 0) * THETA**2 + (agent == 0) * (1 - THETA)**2
    if model == "gate+preference":
        # A verb that has exhibited both orders is known to license both.
        # Its choice probability depends on what the learner infers about
        # the action class. The gate masses are derived in the research note.
        preference = (THETA + 1) / 3
        if agent and patient:
            first_mixed_pair = THETA * (1 - THETA) / 2
            return first_mixed_pair * preference**(agent - 1) * (1 - preference)**(patient - 1)
        if agent + patient == 1:
            return THETA if agent else 1 - THETA
        # P(all A up to n) = P(all A up to n-1) - P(A ... A P).
        if agent:
            return verb_likelihood(model, agent - 1, 0) - verb_likelihood(model, agent - 1, 1)
        return verb_likelihood(model, 0, patient - 1) - verb_likelihood(model, 1, patient - 1)
    # The beta prior has mean theta and the specified total concentration.
    numerator = prod((concentration * THETA + i for i in range(agent)), start=ONE)
    numerator *= prod((concentration * (1 - THETA) + i for i in range(patient)), start=ONE)
    return numerator / prod(concentration + i for i in range(agent + patient))


def uniform_integral(polynomial):
    return sum(Fraction(coefficient, degree + 1)
               for degree, coefficient in enumerate(polynomial.coef))


def evidence(model, verbs, by_meaning, concentration=1):
    likelihoods = defaultdict(lambda: ONE)
    for verb in verbs:
        group = verb.meaning if by_meaning else None
        likelihoods[group] *= verb_likelihood(model, verb.agent_first, verb.patient_first,
                                              concentration)
    return prod(uniform_integral(likelihood) for likelihood in likelihoods.values())


def forecast(model, training, probe, concentration=1):
    """Next agent-first choice for this probe verb, plus posterior P(grouping).

    The probe's two counts are demonstrations already heard for this distinct
    verb. Set both to zero for its first encounter. Each learner infers whether
    semantic groups have separate theta values, with prior probability 1/2.
    """
    observed = [*training, probe]
    next_agent = TrainingVerb(probe.meaning, probe.agent_first + 1, probe.patient_first)
    extended = [*training, next_agent]
    pooled = evidence(model, observed, False, concentration)
    grouped = evidence(model, observed, True, concentration)
    weight = pooled + grouped
    choice = (evidence(model, extended, False, concentration)
              + evidence(model, extended, True, concentration)) / weight
    return choice, grouped / weight


def paired_predictions(repetitions=1, concentration=1):
    """First production after both new contact verbs have been demonstrated."""
    history = training_history(True, repetitions)
    first = TrainingVerb("contact", 2, 1)
    second = TrainingVerb("contact", 1, 2)
    rates = {}
    for model in (*MODELS, "gate+lexical"):
        rates[model] = (forecast(model, [*history, second], first, concentration)[0],
                        forecast(model, [*history, first], second, concentration)[0])
    # Independent Beta(1,1) choice rate for each verb.
    rates["lexical counts"] = tuple(
        Fraction(v.agent_first + 1, v.agent_first + v.patient_first + 2)
        for v in (first, second)
    )
    return rates


def run():
    # Matched first and second moments give identical sequence likelihoods
    # at every theta whenever no verb contributes more than two observations.
    for total in range(3):
        for agent in range(total + 1):
            counts = (agent, total - agent)
            assert verb_likelihood("categorical", *counts) == verb_likelihood("graded", *counts)
    for total in range(4):
        for agent in range(total + 1):
            counts = (agent, total - agent)
            assert verb_likelihood("gate+preference", *counts) == verb_likelihood("graded", *counts)
    repeated = [TrainingVerb("contact", 3, 0)]
    new = TrainingVerb("contact", 0, 0)
    assert forecast("categorical", repeated, new)[0] == Fraction(13, 18)
    assert forecast("graded", repeated, new)[0] == Fraction(97, 135)

    for cue in (True, False):
        print("\nSemantic cue" if cue else "\nCrossed control (one counterbalancing list)")
        for repetitions in (1, 3):
            history = training_history(cue, repetitions)
            assert len(history) == 12
            assert sum(v.agent_first for v in history) == sum(v.patient_first for v in history) == 12 * repetitions
            print(f"  Each distinct example weighted {repetitions} time(s). Agent-first probability:")
            print("  Learner          Contact   Posture    Motion    P(separate meaning groups)")
            for model in MODELS:
                predictions = [forecast(model, history, TrainingVerb(m, 0, 0)) for m in MEANINGS]
                (first, groups), (middle, _), (last, _) = predictions
                assert first + last == 1 and middle == Fraction(1, 2)
                print(f"  {model:16}{float(first):8.4f}{float(middle):10.4f}"
                      f"{float(last):10.4f}{float(groups):15.4f}")

    # Both new verbs belong to the same family. Both are demonstrated before
    # testing either one. The only difference is which verb got the extra A.
    print("\nTwo new contact verbs, next agent-first choice after all six demonstrations:")
    print("  Learner            Verb 2A/1P   Verb 1A/2P   Difference")
    for model, (p_first, p_second) in paired_predictions().items():
        difference = p_first - p_second
        print(f"  {model:16}{float(p_first):12.4f}{float(p_second):13.4f}{float(difference):13.4f}")
        expected = {"graded": Fraction(1, 4), "gate+lexical": Fraction(1, 4),
                    "lexical counts": Fraction(1, 5)}
        assert difference == expected.get(model, 0)


if __name__ == "__main__":
    run()
