"""One held-out form choice after four orderings of the same split history.

Run directly for the model predictions or use --list 22 0 for one stimulus list.
"""

import argparse
from collections import Counter
import json

import numpy as np
from scipy.special import expit, logit

from shared_history import B_REOPENED, HISTORIES, TRAIN_SHARE, delta_transfer, posterior, production
from transfer_test import make_list


POSITIONS = (13, 16, 19, 22)
FIXED_P = (3, 8, 11, 18, 21)
REOPENED = (2, 4, 5, 8, 10, 12, 13, 16, 18, 19, 22, 24)
HISTORY = HISTORIES["P equally often after reopening"]


def schedule(position):
    return [("P" if trial == position or trial in FIXED_P else "Q",
             "reopened" if trial in REOPENED else "continuous")
            for trial in range(1, 25)]


def choice_list(position, version):
    item = make_list("split", "reopened", version, schedule=schedule(position))
    scene = item["primary"]["scene"]
    target = scene.pop("utterance")
    neutral = item["post_probe_checks"][0]["scene"]["utterance"]
    choices = [target, neutral] if version < 8 else [neutral, target]
    item["primary"] = {
        "scene": scene, "question": "Which description would you use for the target cabinet?",
        "responses": choices,
    }
    return item


def verify_design():
    counts = {}
    for scene, n_target, n_neutral in HISTORY:
        path = "continuous" if scene.readings()[0] else "reopened"
        counts["P", path] = n_target
        counts["Q", path] = n_neutral
    for pos in POSITIONS:
        assert Counter(schedule(pos)) == counts
    for version in range(16):
        reference = choice_list(POSITIONS[0], version)
        for pos in POSITIONS[1:]:
            item = choice_list(pos, version)
            base_trials = reference["training"]
            trials = item.pop("training")
            assert item == {k: v for k, v in reference.items() if k != "training"}
            assert len(trials) == len(base_trials) == 24
            changes = []
            for i, (trial, base) in enumerate(zip(trials, base_trials), 1):
                if trial != base:
                    assert trial["utterance"].split()[:-1] == base["utterance"].split()[:-1]
                    assert {**trial, "utterance": base["utterance"]} == base
                    changes.append(i)
            assert changes == [POSITIONS[0], pos]
            first, moved = (trials[i - 1] for i in changes)
            assert first["log"] == moved["log"] and first["target"] == moved["target"]
            for choice in item["primary"]["responses"]:
                assert choice not in {t["utterance"] for t in trials}
            assert len(set(item["primary"]["responses"])) == 2


def predict():
    # All four training likelihoods have exactly the same scene-by-choice counts.
    count_predictions = []
    for model in ("hard", "graded"):
        a, b, mass, _ = posterior(model, HISTORY)
        p = production(model, a, b, B_REOPENED, TRAIN_SHARE)
        count_predictions.append(np.sum(mass * p))
    np.testing.assert_allclose(*count_predictions)
    print(f"Count learner, all positions: {count_predictions[0]:.6f}")

    rates = []
    for pos in POSITIONS:
        choices = [choice for choice, _ in schedule(pos)]
        p = delta_transfer(choices)
        rates.append(p)
        # Independent calculation: retrieve all past choices with geometric weights.
        strength = sum(0.3 * 0.7 ** lag for lag, choice in enumerate(reversed(choices))
                       if choice == "P")
        np.testing.assert_allclose(p, expit((0.75 * strength - 0.4) / 0.2), atol=1e-14, rtol=0)
        print(f"Position {pos}: {''.join(choices)}  P(target) = {p:.6f}")

    # Use only the first three arm probabilities to estimate decay and forecast arm 4.
    first, second, third = logit(rates[:3])
    ratio = (second - first) / (third - second)
    rate = 1 - ratio ** (1 / (POSITIONS[1] - POSITIONS[0]))
    held_out = expit(third + (third - second) / ratio)
    np.testing.assert_allclose([rate, held_out], [0.3, rates[3]], atol=1e-13, rtol=0)
    print(f"First three arms imply learning rate {rate:.6f} and fourth-arm P(target) {held_out:.6f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--list", nargs=2, type=int, metavar=("POSITION", "VERSION"))
    args = parser.parse_args()
    if args.list is None:
        verify_design()
        predict()
    else:
        position, version = args.list
        if position not in POSITIONS or version not in range(16):
            parser.error("choose position 13, 16, 19 or 22 and version 0..15")
        print(json.dumps(choice_list(position, version), indent=2))
