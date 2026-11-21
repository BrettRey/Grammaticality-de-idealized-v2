# Learning the temporal meaning of a marker

When speakers use a marker for an event whose result is still visible, a learner
could infer that the result persisted throughout or simply that it holds now.
The two interpretations agree if a lock either stays locked or is unlocked
and left that way. They diverge if it is unlocked and subsequently relocked.

The original miniature language has two closed-past time words and two competing
particles. In familiarization the learner encounters both time words with
the neutral particle and the target particle in bare descriptions. Training
then supplies 24 opportunities with one time word. Six speakers use the
target particle. In the restricted history all six use it when the target
stays locked. In the split history three use it when the lock is later undone.
Each history has 12 scenes of each kind. The first test presents the particle
with the other time word in a fresh scene and asks whether the description
is true.

## The relocking test

In one version, a worker locks the target cabinet at 10:00, unlocks it at
16:00 and relocks it at 17:00. The report is made at 18:00 and refers to
the morning. Only the first locking falls in that window. In the continuous
control, the 16:00 and 17:00 actions affect a different cabinet. The two
scenes have the same actions, times and final lock states.

| Predicted endorsement of the relocked scene | Restricted history | Split history | Split minus restricted |
|---|---:|---:|---:|
| Learner tracks persistence from the named locking event | 18.0% | 34.7% | +16.7 points |
| Learner tracks whether the target is locked at report time | 70.0% | 54.5% | −15.5 points |

Both predictions use the same exposure likelihood, priors, transfer assumption
and response rule. These are model outputs. The comparison tests whether
learners attend to an intervening change. A learner who remembers which cabinet
was unlocked can also give the continuity response. Assigning that response
to a particular linguistic analysis requires further evidence.

## Which locking does the time word name?

At 10:00 a worker locks the target cabinet, at 12:00 unlocks it, and at 14:00
locks it again. At 18:00 one learner hears the marker with the morning word.
Another sees the same log and hears it with the afternoon word. The morning
locking was undone. The afternoon locking still holds. A learner who uses only
the scene has the same evidence on both trials, even if they remember every
action.

Training in this experiment uses a third word, meaning midday. The morning
and afternoon words each occur twice with the neutral particle during
familiarization. Each is new in combination with the target marker. Within
each training history and list version, assign learners equally to one of the
two test words. The word is the only difference between the paired lists.
The outcome is the probability of a “true” response on the first probe,
averaged across the 16 versions within each condition.

| Rule for the narrow reading | Restricted, morning → afternoon | Split, morning → afternoon |
|---|---:|---:|
| The result persists from a locking in the named period | 18.0% → 70.0% (+52.0 points) | 34.7% → 54.5% (+19.8 points) |
| The target was never unlocked | 18.0% → 18.0% | 34.7% → 34.7% |
| The target is locked at report time | 70.0% → 70.0% | 54.5% → 54.5% |
| The last change to the target was a locking in the named period | 18.0% → 70.0% | 34.7% → 54.5% |

All four rules require a locking in the named period for either reading. They
agree on every exposure trial and share the same learning and response model.
The numerical effects assume that the learner transfers the temporal reading
from midday to both test words. An observed difference would establish that
the choice of time word influenced responses on this scene. Either a learned
meaning or a strategy that consults the time word could produce it.

The last row gives an exact limit on this comparison. Consider any complete,
strictly ordered log of changes to a binary lock up to report time. If a
locking in the named period persists to report time, the target cannot be
locked again in between without first being unlocked. That locking must be
its last change. Conversely, if its last change was a locking in the named
period, the result has persisted since then. With no locking in the period,
both rules fail. The equivalence holds for either initial state. More scenes
made of these same transitions cannot distinguish the two rules by their
truth judgments.

## Replay

From the repository root, with Python, NumPy and SciPy installed, run

```sh
python3 experiments/compatibility/transfer_test.py
python3 experiments/compatibility/transfer_test.py --list split restored 0
python3 experiments/compatibility/transfer_test.py --list restricted earlier 0
python3 experiments/compatibility/transfer_test.py --list restricted later 0
```

The first command checks the 96 original lists, the 32 new pairs and the
last-change equivalence for every subset of nine possible change times with
either initial state. It prints the model predictions. The other commands
print a full list as JSON, including the answer key for the comprehension
checks. List arguments are the history (`restricted` or `split`), probe
(`continuous`, `reopened`, `restored`, `earlier` or `later`) and version
(0–15). Each learner would receive a single list. No responses have been
collected.

The earlier calculations cover [choice at different payoffs](payoff.py),
[learning from the exposure histories](shared_history.py) and
[paired judgment and production](joint_measurement.py). The last calculation
regenerates [the synthetic design results](joint_measurement_results.json).
