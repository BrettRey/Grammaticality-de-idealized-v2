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

## Does the order of exposure change the choice?

Four groups see the same 24 opportunities in the same order and hear the
target particle P six times. One use of P trades places with the alternative
Q. It can occur at trial 13, 16, 19 or 22. These four trials have identical
cabinet logs and refer to different sites. All groups finish with the same
two Q examples. Afterward each learner chooses between two descriptions of a
reopened target with the held-out time word. The outcome is the probability of
choosing P on that first choice. Assign positions equally within each of the
16 versions. Each learner receives one version at one position.

| Learning rule | P at 13 | P at 16 | P at 19 | P at 22 |
|---|---:|---:|---:|---:|
| Stationary model using the counts for each scene | 19.85% | 19.85% | 19.85% | 19.85% |
| Delta rule with learning rate 0.30 | 19.09% | 19.76% | 21.80% | 28.59% |

The stationary hard and graded learners share the first row at the training
payoff. The second row uses the independently proposed delta rule and its
original transfer and choice parameters. All entries are model predictions.

The four positions also test the *shape* of the recency effect. Under the
delta rule, a P seen at trial $t$ contributes $\eta(1-\eta)^{24-t}$ to final
strength. With log odds of choosing P linear in that strength, moving one P
three trials later multiplies its contribution by $(1-\eta)^{-3}$. The five
fixed uses of P contribute the same amount in every arm. Write $L_t$ for
the log odds of choosing P in arm $t$, and $D_1=L_{16}-L_{13}$,
$D_2=L_{19}-L_{16}$ and $D_3=L_{22}-L_{19}$. The model requires

$$
\frac{D_1}{D_2}=\frac{D_2}{D_3}=(1-\eta)^3.
$$

When $0<D_1<D_2$, the first three arms imply
$\eta=1-(D_1/D_2)^{1/3}$ and predict $L_{22}=L_{19}+D_2^2/D_1$.
This gives a fourth-arm prediction even if the common intercept and transfer
gain are unknown. In the model example the first two arms differ by only
0.67 percentage points. With observed data, uncertainty in that difference
would carry into both the learning rate and the fourth-arm prediction.
Flat population rates leave the rate unidentified by this contrast.

The inferred rate describes how past choices are weighted. A learner can
retain the whole history and apply the same geometric weights when choosing
a description. Expanding the delta recursion gives exactly that weighted
sum, so the two accounts agree for every history under the shared readout.
The ratio also assumes a common learning rate and a common linear relation
between strength and log odds across learners and versions. Mixing different
response probabilities can change the ratio. Even a clean order effect
would leave the hard-versus-graded question open.

## Could the speaker have chosen the marker?

In the split history, change a single feature of what learners see. Before
each recording a cue says “speaker chooses” or “speaker reads an assigned
message.” The cue reveals no words. All learners hear the same 24 utterances
in the same order for a given version and see the same scenes. All six uses
of the target P are free choices, three while the cabinet stays locked and
three after it reopens. The 18 uses of its competitor Q are split nine per
scene. In one history the nine Qs in still-locked scenes are freely chosen
and the other nine are assigned. In the other history the assignment is
reversed. A forced Q supplies no evidence about what the speaker would
have chosen. This assumes the device assigns a message before the speaker
can choose, independently of the speaker's repertoire.

| Scene in which Q was freely chosen | Endorse P, still locked | Endorse P, reopened | Produce P, still locked | Produce P, reopened |
|---|---:|---:|---:|---:|
| Still locked | 67.17% | 52.77% | 36.09% | 28.88% |
| Reopened | 75.54% | 43.88% | 40.27% | 24.44% |

These are predictions for the familiar but untrained adverb B. Each learner
would receive one primary probe, with no assignment cue or feedback. Use
independent groups for truth and form choice. In the original two-parameter
learner, free Qs after reopening specifically count against the broader
reading that would allow P there. Meanwhile all three still-locked P choices
face zero freely chosen Qs in that scene, supporting the narrower use.
Moving the informative omissions therefore predicts opposite changes.

The hard and graded models yield the same table at the training payoff.
With their specified response rules the production interaction is exactly
half the truth interaction. A learner that uses only the positive P tokens,
or that processes every recording as freely chosen, receives the same
relevant history in both arms and predicts zero difference between arms.
An interaction would show sensitivity to the circumstances of non-use.
Selective attention to freely chosen messages could also yield it.
The cue manipulates the speaker's freedom of choice while keeping the
intended message fixed. Whether learners spontaneously recognize semantic
opportunities in conversation remains a separate question.

Run `python3 experiments/compatibility/opportunity_choice.py` to check the
16 matched histories and reproduce the table and the comparison that ignores
the cue.

### What if learners discover the alternatives afterward?

In a second design every speaker freely chooses between two expressions.
Learners hear the same 24 messages and see the same scenes and card badges
in both arms. Only the speaker sees the two particles on the card. After the
last message, learners receive a key showing which particles each badge
permitted. Every version uses two P/Q cards and one Q/R card. Q and R are
familiar paraphrases. Both keys show the same words equally often.

The circle card accounts for three P and three Q choices in each scene.
Six further Qs in still-locked scenes carry one badge, and six Qs after
reopening carry another. The keys exchange which of those badges allowed P.
Thus the disclosure tells the learner *where speakers passed up P*.
The model treats the recordings as choices by independent tutors, the cards
as assigned independently of repertoire, and the chance of choosing Q over
R as independent of the parameters governing P. Under these assumptions
the Q/R choices contribute a constant to the likelihood. On P/Q cards the
learner observes three P choices in each scene and either nine or three Qs.
Writing $p_s$ and $p_r$ for the chances of choosing P when offered in
still-locked and reopened scenes, respectively, the reopened-key likelihood
divided by the still-locked-key likelihood is $[(1-p_r)/(1-p_s)]^6$ when
Q and R are equiprobable. The six shared P tokens cancel from this ratio.

| Scene with six additional Q choices over P | Endorse P, still locked | Endorse P, reopened | Choose P, still locked | Choose P, reopened |
|---|---:|---:|---:|---:|
| Still locked | 62.36% | 45.93% | 33.68% | 25.46% |
| Reopened | 69.33% | 41.39% | 37.16% | 23.20% |

Randomize each learner to one disclosure, one test scene and one probe,
given either before or after the key. Use the familiar adverb B, which has
never appeared with P. The test speaker has no badge. Take truth endorsement
as primary. For each test scene, subtract endorsement under the still-locked
key from endorsement under the reopened key. After disclosure, the predicted
differences are +6.96 points while still locked and −4.54 after reopening.
Subtracting the first from the second gives **−11.50 percentage points**.
Before disclosure the two arms have identical observable histories, so their
expected difference is zero on each scene, even for learners who infer
possible menus from the badges. Form choice at the training payoff gives
half the truth interaction under the specified response rules.

A learner who fixes attention during exposure and ignores later information
predicts zero interaction at both times. An interaction emerging after the
key would show that later information about speakers' options affected
responses to a fresh combination. The hard and graded models agree on the
whole table. A learner could also remember which scene went with each badge
and use the key when answering. Indeed, discarding all Q/R trials at test
and applying the same P/Q likelihood reproduces the model for every history.
The timing contrast leaves open when linguistic knowledge itself changed.
Forgetting which scenes went with which badge could erase the interaction
even in learners who take speakers' alternatives into account.

Run `python3 experiments/compatibility/menu_disclosure.py` to verify all 256
lists and reproduce the table. Add `--list reopened continuous 0` for a
complete example. The first argument names the scene with the six additional
P/Q opportunities, the second the probe scene, and the third the list
version. Add `--before-key` to move that learner's probe ahead of disclosure,
or `--choice` to elicit a choice of description.

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

Run `python3 experiments/compatibility/exposure_order.py` to check the 64
order-test lists, reproduce both predictions and reconstruct the fourth arm
from the first three. Add `--list 22 0` to print the trial-22 list for
version 0.

The earlier calculations cover [choice at different payoffs](payoff.py),
[learning from the exposure histories](shared_history.py) and
[paired judgment and production](joint_measurement.py). The last calculation
regenerates [the synthetic design results](joint_measurement_results.json).

The [English perfect comparison](english-perfect-contrast.md) takes the question
into British conversation, screens *yesterday* reports in BNC Baby and tests
what can be inferred from form choice and a listener’s choice of temporal anchor.
The [listener design](listener-anchor.md) checks whether that anchor predicts
responses under an independently varied attention cue.
