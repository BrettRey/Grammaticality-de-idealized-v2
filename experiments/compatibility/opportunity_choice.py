"""Keep every exposure fixed and change which competitor utterances were assigned."""

from collections import Counter

import numpy as np

from shared_history import (A_STILL, A_REOPENED, B_STILL, B_REOPENED, TRAIN_SHARE,
                            posterior, production, truth)
from transfer_test import exposure_schedule


def training(version, free_q_scene):
    # The status cue is shown before the recording, with no form printed.
    return [(word, path, "choice" if word == "P" or path == free_q_scene else "assigned")
            for word, path in exposure_schedule("split", version)]


def history(trials, use_cue):
    counts = Counter((word, path) for word, path, status in trials
                     if not use_cue or status == "choice")
    return [(scene, counts["P", path], counts["Q", path])
            for scene, path in ((A_STILL, "continuous"), (A_REOPENED, "reopened"))]


def forecast(model, experience):
    a, b, mass, _ = posterior(model, experience)
    return np.array([[(mass * truth(model, a, b, scene)).sum(),
                      (mass * production(model, a, b, scene, TRAIN_SHARE)).sum()]
                     for scene in (B_STILL, B_REOPENED)])


def run():
    paths = ("continuous", "reopened")
    examples = [training(0, path) for path in paths]
    for version in range(16):
        arms = [training(version, path) for path in paths]
        assert [row[:2] for row in arms[0]] == [row[:2] for row in arms[1]]
        for trials, example in zip(arms, examples):
            assert history(trials, True) == history(example, True)
            assert sum(status == "assigned" for _, _, status in trials) == 9
            assert all(status == "choice" for word, _, status in trials if word == "P")
        assert history(arms[0], False) == history(arms[1], False)

    rates = []
    for path, trials in zip(paths, examples):
        result = forecast("hard", history(trials, True))
        np.testing.assert_allclose(result, forecast("graded", history(trials, True)))
        rates.append(result)
        print(f"Free Q in {path} scenes. Truth / production on each held-out scene:")
        for outcome, row in zip(paths, result):
            print(f"  {outcome:10s} {row[0]:.5f} / {row[1]:.5f}")
    difference = 100 * (rates[1] - rates[0])
    print("Free Q in reopened minus continuous, truth differences (points):",
          *(f"{p:+.2f}" for p in difference[:, 0]))
    interaction = difference[1] - difference[0]
    print(f"Reopened minus continuous interaction: truth {interaction[0]:+.2f}, "
          f"production {interaction[1]:+.2f} points.")
    assert difference[0, 0] > 0 > difference[1, 0]
    # At the training payoff the two response channels are affinely related.
    np.testing.assert_allclose(interaction[1], TRAIN_SHARE * interaction[0])
    blind = forecast("hard", history(examples[0], False))
    print(f"Ignoring assignment, both arms: truth {blind[0, 0]:.5f} / {blind[1, 0]:.5f} "
          "(continuous / reopened).")


if __name__ == "__main__":
    run()
