# Learning the temporal meaning of a marker

When speakers use a marker for an event whose result is still visible, a learner
could infer that the result persisted throughout or simply that it holds now.
The two interpretations agree if a lock either stays locked or is unlocked
and left that way. They diverge if it is unlocked and subsequently relocked.

The miniature language has two closed-past time words and two competing
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

## Replay

From the repository root, with Python, NumPy and SciPy installed, run

```sh
python3 experiments/compatibility/transfer_test.py
python3 experiments/compatibility/transfer_test.py --list split restored 0
```

The first command checks the 96 lists and prints the predictions. The second
prints one list, including the familiarization key, exposure, the first test
and two subsequent comprehension checks. List arguments are the history
(`restricted` or `split`), trajectory (`continuous`, `reopened` or `restored`)
and version (0–15). Each learner would receive a single list. The JSON is for
study preparation and includes experimenter-only answers for the checks.

The earlier calculations cover [choice at different payoffs](payoff.py),
[learning from the exposure histories](shared_history.py) and
[paired judgment and production](joint_measurement.py). The last calculation
regenerates [the synthetic design results](joint_measurement_results.json).
