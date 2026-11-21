"""Does learning which alternatives were available change a later truth judgment?"""

import argparse
from collections import Counter
from itertools import product
import json

import numpy as np

from opportunity_choice import forecast
from shared_history import A_REOPENED, A_STILL
from transfer_test import exposure_schedule, make_list


PATHS = ("continuous", "reopened")
BADGES = ("circle", "triangle", "square")


def special_badges(version):
    badges = ("triangle", "square") if version < 8 else ("square", "triangle")
    return dict(zip(PATHS, badges))


def recordings(version):
    """The public record is fixed before a disclosure arm is selected."""
    seen_q = Counter()
    special = special_badges(version)
    trials = []
    for word, path in exposure_schedule("split", version):
        badge = "circle"
        if word == "Q":
            if seen_q[path] % 3 != version % 3:
                badge = special[path]
            seen_q[path] += 1
        trials.append((word, path, badge))
    return trials


def menu_key(available_in, version):
    key = {"circle": ("P", "Q")}
    for path, badge in special_badges(version).items():
        key[badge] = ("P", "Q") if path == available_in else ("Q", "R")
    return key


def eligible_history(trials, key):
    counts = Counter((word, path) for word, path, badge in trials if "P" in key[badge])
    return [(scene, counts["P", path], counts["Q", path])
            for scene, path in zip((A_STILL, A_REOPENED), PATHS)]


def materials(available_in, probe, version, before_key=False, choice=False):
    trials = recordings(version)
    base = make_list("split", probe, version, schedule=[(w, p) for w, p, _ in trials])
    base["instructions"] += (
        " Each speaker freely chooses between two descriptions on a card. Only the"
        " speaker sees its two final particles. You see its badge and hear the chosen"
        " description. Cards are assigned independently of who speaks."
    )
    forms = {"R": "su"}
    for row, (word, _, badge) in zip(base["training"], trials):
        row["badge"] = badge
        forms[word] = row["utterance"].split()[-1]
    # Present the neutral paraphrase on the two already familiar Q scenes.
    tutorial = base["familiarization_with_feedback"]
    for item in tutorial[:2]:
        scene = item["example"].copy()
        scene["utterance"] = scene["utterance"].rsplit(" ", 1)[0] + " " + forms["R"]
        tutorial.append({"example": scene, "true": True})
    base["instructions"] += f" The particles '{forms['Q']}' and 'su' mean the same thing."
    key = menu_key(available_in, version)
    disclosure = {"stage": "disclosure", "instruction": "Here is what was on each card.",
                  "cards": [{"badge": badge, "particles": sorted(forms[w] for w in key[badge])}
                            for badge in BADGES]}
    primary = {"stage": "truth_probe", **base.pop("primary")}
    checks = base.pop("post_probe_checks")
    if choice:
        target = primary["scene"].pop("utterance")
        neutral = checks[0]["scene"]["utterance"]
        primary.update(stage="choice_probe", question="Which description would you use for the target cabinet?",
                       responses=[target, neutral] if version < 8 else [neutral, target])
    base["test_stages"] = [primary, disclosure] if before_key else [disclosure, primary]
    base["post_probe_checks"] = checks
    return base


def verify_lists():
    for version in range(16):
        trials = recordings(version)
        assert Counter(b for _, _, b in trials) == dict(zip(BADGES, (12, 6, 6)))
        for available_in in PATHS:
            key = menu_key(available_in, version)
            assert all(len(key[badge]) == 2 and word in key[badge] for word, _, badge in trials)
            counts = eligible_history(trials, key)
            assert [(p, q) for _, p, q in counts] == [
                (3, 9 if path == available_in else 3) for path in PATHS]
        for probe, before_key, choice in product(PATHS, (False, True), (False, True)):
            packets = [materials(path, probe, version, before_key, choice) for path in PATHS]
            cards = []
            for packet in packets:
                first, second = packet["test_stages"]
                test, disclosure = (first, second) if before_key else (second, first)
                assert disclosure["stage"] == "disclosure"
                assert "badge" not in test["scene"]
                if choice:
                    assert test["stage"] == "choice_probe" and "utterance" not in test["scene"]
                    target = test["responses"][0 if version < 8 else 1]
                    assert len(set(test["responses"])) == 2
                else:
                    assert test["stage"] == "truth_probe"
                    target = test["scene"]["utterance"]
                exposures = packet["training"] + [
                    x["example"] for x in packet["familiarization_with_feedback"]]
                assert target not in {x["utterance"] for x in exposures}
                # Compare complete packets after removing only the disclosed mapping.
                cards.append(disclosure.pop("cards"))
            assert packets[0] == packets[1]
            assert [c["badge"] for c in cards[0]] == [c["badge"] for c in cards[1]]
            left, right = (sorted(c["particles"] for c in key_cards) for key_cards in cards)
            assert left == right
            assert sum(a != b for a, b in zip(*cards)) == 2


def run():
    verify_lists()
    rates = []
    for path in PATHS:
        history = eligible_history(recordings(0), menu_key(path, 0))
        result = forecast("hard", history)
        np.testing.assert_allclose(result, forecast("graded", history))
        rates.append(result)
        print(f"Six additional Q choices over P in {path} scenes. Held-out truth / choice:")
        for scene, (truth, choice) in zip(PATHS, result):
            print(f"  {scene:10s} {truth:.6f} / {choice:.6f}")
    difference = 100 * (rates[1] - rates[0])
    assert np.all(difference[0] > 0) and np.all(difference[1] < 0)
    for outcome, (still, reopened) in zip(("Truth", "Choice"), difference.T):
        print(f"{outcome}, reopened disclosure minus continuous disclosure (points): "
              f"still locked {still:+.2f}, reopened {reopened:+.2f}, "
              f"interaction {reopened - still:+.2f}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", nargs=3, metavar=("AVAILABLE_IN", "PROBE", "VERSION"))
    parser.add_argument("--before-key", action="store_true", help="place the single probe before disclosure")
    parser.add_argument("--choice", action="store_true", help="use a form choice as the single probe")
    args = parser.parse_args()
    if args.list:
        available_in, probe, version = args.list
        if available_in not in PATHS or probe not in PATHS or version not in map(str, range(16)):
            parser.error("Use continuous or reopened for each scene and a version from 0 to 15.")
        packet = materials(available_in, probe, int(version), args.before_key, args.choice)
        print(json.dumps(packet, indent=2))
    elif args.before_key or args.choice:
        parser.error("Probe options require --list")
    else:
        run()
