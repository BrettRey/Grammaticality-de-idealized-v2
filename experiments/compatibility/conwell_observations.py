"""Compare three response rules against published Conwell & Snedeker (2024) percentages.

These summaries pool familiar and unfamiliar verbs. The calculation uses no
participant records. See conwell-snedeker-feasibility.md for the assumptions.
"""
from dataclasses import dataclass
from math import isclose


@dataclass(frozen=True)
class Responses:
    accept_agent_first: float
    accept_patient_first: float
    produce_agent_first: float


# Judgment rates are from Table 3. Production shares are rounded in the text.
# For the semantics condition's patient-first-only verbs, the reported share
# producing patient-first is .57. Taking its complement assumes two orders.
OBSERVATIONS = {
    "Statistics only": {
        "Alternating": Responses(.9175, .8515, .68),
        "Agent-first only": Responses(.9686, .6037, .82),
        "Patient-first only": Responses(.7786, .8839, .59),
    },
    "Semantics": {
        "Alternating": Responses(.9346, .9571, .73),
        "Agent-first only": Responses(.9569, .4139, .92),
        "Patient-first only": Responses(.4543, .9826, 1 - .57),
    },
}


def choice_predictions(control, target):
    """Fit one order preference on the alternating verbs in the same condition."""
    a, b = control.accept_agent_first, control.accept_patient_first
    p = control.produce_agent_first
    # Every speaker-item occasion has at least one available order. The
    # both-available fraction is then fixed by inclusion-exclusion.
    both = a + b - 1
    if both <= 0:
        raise ValueError("The control does not identify preference when both are available")
    preference = (p - (1 - b)) / both
    if not 0 <= preference <= 1:
        raise ValueError("The control cannot arise from this categorical response law")
    bias = (p / (1 - p)) * b / a

    a, b = target.accept_agent_first, target.accept_patient_first
    if a + b < 1:
        raise ValueError("Target marginals require occasions with neither order available")
    categorical = 1 - b + preference * (a + b - 1)
    graded = bias * a / (bias * a + b)
    return categorical, graded, p


def main():
    print("Predicted and reported agent-first production (%)")
    print("Condition       Verb subclass         Categorical  Graded  Baseline  Reported"
          "   Graded range with varying preferences")
    for condition, rows in OBSERVATIONS.items():
        control = rows["Alternating"]
        for subclass, target in rows.items():
            predictions = choice_predictions(control, target)
            if subclass == "Alternating":
                assert all(isclose(x, control.produce_agent_first) for x in predictions)
            assert all(0 <= x <= 1 for x in predictions)
            estimates = (*predictions, target.produce_agent_first)
            # Jensen's inequality bounds a mixture of personal order preferences
            # between the homogeneous graded prediction and the alternating mean.
            low, high = sorted((predictions[1], control.produce_agent_first))
            print(f"{condition:16}{subclass:22}" + "".join(f"{100*x:8.1f}" for x in estimates)
                  + f"    {100*low:.1f}–{100*high:.1f}")


if __name__ == "__main__":
    main()
