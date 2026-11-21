"""Meaning transfer in the miniature language, at the original payoff.

Run python3 experiments/compatibility/transfer_test.py to replay the model
predictions and check the lists. Add --list split restored 0 to print one
complete example as JSON. This generates materials and records no responses.

Design: independent learners are balanced across two training histories,
three held-out scene types and 16 list versions. The reference calculation
conditions on knowledge of the two adverbs and both particles' baseline uses.
The familiarization examples illustrate that assumed starting point. Q is an
available description of the past locking in every critical scene; somebody
choosing Q supplies an opportunity for P to have occurred. Exposure uses a
fresh speaker for each opportunity. At test, one truth judgment on P+B is the
first response to that combination. B was familiarized with Q. There is no
test feedback. Distinct cabinets at different sites are new event tokens of
one lexical predicate, lock. Generalization to another predicate is open.

Primary transfer estimand: split minus restricted training in probability
of a 'true' response on reopened B. The continuous B arm estimates whether
the training effect is scene-specific. The restored B arm compares two
accounts *within each history*, using the continuous and reopened arms as
anchors. Analyze the six randomized condition means and their contrasts on
the probability scale, standardizing over equally weighted list versions.
The restored arm is informative only to the extent that its anchors differ.
Estimate the differences directly; each respondent supplies one primary
observation. Post-probe checks are separate outcomes. No screening threshold,
recruitment target or empirical effect size has been established.

Continuity implements the temporal clause in neon-model-theory.json: the
locking event must fall in B, and for the narrow reading its result must
hold from that event through speech time. The endpoint rival checks only
whether the result holds at speech time, given a locking event in B.
Their broad reading permits the event in a past reference interval. Both
inherit the same shared_history learner, prior, production and response
rules. They agree on every training scene; only the readout on the new
trajectory differs. This probes sensitivity to an interruption. A strategy
that tracks which cabinet was unlocked can also produce the continuity
pattern. The result is specific to the miniature language.
"""

import argparse
from collections import Counter
from dataclasses import dataclass
import json
from random import Random

import numpy as np

from shared_history import HISTORIES, TRUTH_SLIP, observed, posterior


ARMS = {"restricted": "P only while still locked", "split": "P equally often after reopening"}
PATHS = ("continuous", "reopened", "restored")
WINDOWS = {"morning": (9, 11), "afternoon": (13, 15)}
COLORS = ("blue", "green", "orange")


@dataclass(frozen=True)
class Event:
    hour: int
    cabinet: str
    action: str


def trajectory(window, path):
    """Only 'other' is locked initially. Events are the complete change log."""
    unlock, relock = {
        "continuous": ("other", "other"),
        "reopened": ("target", "spare"),
        "restored": ("target", "target"),
    }[path]
    return (Event(WINDOWS[window][0] + 1, "target", "locks"),
            Event(16, unlock, "unlocks"), Event(17, relock, "locks"))


def readings(events, window, rule):
    start, end = WINDOWS[window]
    eligible = [event for event in events if event.cabinet == "target"
                and event.action == "locks" and start <= event.hour < end]
    # Each eligible event persists at least to the end of its named window
    # in these lists, giving a past reference interval for the broad reading.
    broad = bool(eligible)
    target_events = [e for e in events if e.cabinet == "target"]
    if rule == "endpoint":
        return broad and target_events[-1].action == "locks", broad
    if rule == "continuity":
        uninterrupted = any(all(later.action != "unlocks" for later in target_events
                                if later.hour > event.hour) for event in eligible)
        return uninterrupted, broad
    raise ValueError(rule)


def exposure_schedule(arm, version):
    """One P, three Q, two scenes of each kind in every four-opportunity block."""
    schedule = []
    for block in range(6):
        paths = ["continuous", "continuous", "reopened", "reopened"]
        if arm == "split" and block % 2 == version % 2:
            paths[0], paths[2] = paths[2], paths[0]
        indices = list(range(4))
        Random(7021 + block).shuffle(indices)
        for offset in range(4):
            index = indices[(offset + version // 4) % 4]
            schedule.append(("P" if index == 0 else "Q", paths[index]))
    return schedule


def make_list(arm, probe, version):
    trained, held = ("morning", "afternoon") if version % 2 else ("afternoon", "morning")
    times = dict(zip(("morning", "afternoon"),
                     ("vek", "nif") if version % 4 < 2 else ("nif", "vek")))
    particles = {"P": "pa", "Q": "ti"}
    if (version // 4 + version % 2) % 2:
        particles = {"P": "ti", "Q": "pa"}

    def trial(site, window, path, particle, say_window=None, bare=False):
        # Keep the layout and identity of the target yoked across conditions.
        rotation = (site + version) % 3
        colors = COLORS[rotation:] + COLORS[:rotation]
        color = dict(zip(("target", "other", "spare"), colors))
        words = ["lock", particles[particle]]
        if not bare:
            words.insert(0, times[say_window or window])
        return {
            "site": site, "target": color["target"], "initially_locked": color["other"],
            "log": [f"{e.hour}:00 A worker {e.action} the {color[e.cabinet]} cabinet."
                    for e in trajectory(window, path)],
            "utterance": " ".join(words),
        }

    tutorial = []
    for window in WINDOWS:
        for path in ("continuous", "reopened"):
            tutorial.append({"example": trial(101 + len(tutorial), window, path, "Q"),
                             "true": True})
    for path in ("continuous", "reopened"):
        tutorial.append({"example": trial(101 + len(tutorial), trained, path, "P", bare=True),
                         "true": path == "continuous"})
    return {
        "instructions": (
            "Each log lists every change to the locks at one site. At the start only "
            "the listed cabinet is locked. The speaker reports at 18:00 about the "
            "highlighted target cabinet. The time word, when present, comes before "
            "'lock'; the particle comes last. Learn from the examples and from which "
            "description each new speaker chooses."
        ),
        "time_words": times,
        "familiarization_with_feedback": tutorial,
        "training": [trial(i, trained, path, particle)
                     for i, (particle, path) in enumerate(exposure_schedule(arm, version), 1)],
        "primary": {"scene": trial(25, held, probe, "P"),
                    "question": "Is this speaker's description of the target cabinet true?",
                    "responses": ["true", "false"]},
        "post_probe_checks": [
            {"scene": trial(26, held, "reopened", "Q"), "expected_truth": True},
            {"scene": trial(27, trained, "reopened", "Q", say_window=held),
             "expected_truth": False},
        ],
    }


def verify_lists():
    for v in range(16):
        restricted = exposure_schedule("restricted", v)
        split = exposure_schedule("split", v)
        assert [p for p, _ in restricted] == [p for p, _ in split]
        for arm, schedule in (("restricted", restricted), ("split", split)):
            tally = Counter(schedule)
            for scene, count_p, count_q in HISTORIES[ARMS[arm]]:
                path = "continuous" if scene.readings()[0] else "reopened"
                assert (tally["P", path], tally["Q", path]) == (count_p, count_q)
            lists = [make_list(arm, probe, v) for probe in PATHS]
            assert all(item["training"] == lists[0]["training"] for item in lists)
            primary = lists[0]["primary"]["scene"]
            assert all(item["primary"]["scene"]["utterance"] == primary["utterance"]
                       for item in lists)
            assert primary["utterance"] not in {x["utterance"] for x in lists[0]["training"]}
            assert primary["utterance"] not in {
                x["example"]["utterance"] for x in lists[0]["familiarization_with_feedback"]}
    for window in WINDOWS:
        for path in PATHS:
            events = trajectory(window, path)
            locked = {"other"}
            for event in events:
                if event.action == "locks":
                    assert event.cabinet not in locked
                    locked.add(event.cabinet)
                else:
                    locked.remove(event.cabinet)
            assert readings(events, window, "continuity") == (path == "continuous", True)
            assert readings(events, window, "endpoint") == (path != "reopened", True)
            for wrong in WINDOWS.keys() - {window}:
                assert readings(events, wrong, "continuity") == (False, False)


def predictions():
    print("P(true) on held-out B; columns are continuous, reopened, restored")
    restored = {}
    for arm, history_name in ARMS.items():
        a, b, mass, _ = posterior("hard", HISTORIES[history_name])
        for rule in ("continuity", "endpoint"):
            rates = []
            for path in PATHS:
                narrow, broad = readings(trajectory("morning", path), "morning", rule)
                availability = a * ((1 - b) * narrow + b * broad)
                rates.append(np.sum(mass * observed(availability, TRUTH_SLIP)))
            restored[arm, rule] = rates[-1]
            print(f"{arm:10s} {rule:10s} " + " ".join(f"{rate:.4f}" for rate in rates))
    print("Restored B, split minus restricted (percentage points):")
    for rule in ("continuity", "endpoint"):
        effect = restored["split", rule] - restored["restricted", rule]
        print(f"{rule:10s} {100 * effect:+.2f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--list", nargs=3, metavar=("HISTORY", "PROBE", "VERSION"))
    args = parser.parse_args()
    if args.list is None:
        verify_lists()
        predictions()
    else:
        arm, probe, v = args.list
        if arm not in ARMS or probe not in PATHS or v not in map(str, range(16)):
            parser.error("choose restricted/split, continuous/reopened/restored, and 0..15")
        print(json.dumps(make_list(arm, probe, int(v)), indent=2))
