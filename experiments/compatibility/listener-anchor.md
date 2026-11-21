# Which day’s rule would the listener apply?

The question is whether *I’ve posted the spare key yesterday* leads a listener to carry the posting time forward into the next turn. A preference for today’s rule could also arise after the report, when the listener decides what matters now. The two explanations can produce the same answers, even when attention is manipulated independently.

## A listener comparison that can fail

Two flatmates know that one posted a key at the counter yesterday. The sender’s signature was optional at that counter yesterday and is required today. The policy applies at handover. Reverse the change in half the items, so either answer can indicate either day. Keep the delivery status unknown.

1. Play the report with *I posted* or *I’ve posted* and the same clause-integrated *yesterday*. Use separate recordings matched for emphasis and boundary cues. The listener sees no speaker goal card.
2. In the **past control**, the speaker then specifies “I mean the time I handed it over.” In the **present control**, the clarification is “I mean the situation right now.” In the **target**, leave the time open, matching the delay before the next turn.
3. After that, briefly outline either the posting-day column or today’s column on the policy display. The outline comes from the display, is uninformative about the intended answer and disappears before the question. Balance column position independently. The cue can govern which rule is consulted, trigger reinterpretation or simply affect response selection.
4. Play the identical follow-up *Signature required?* on every trial. Listeners can say a signature was required, a signature was optional, either reading makes sense, or they couldn’t interpret the exchange. Score the first two against the item’s policy change. Keep all four answers in the denominator.

Assign one critical version per listener. Cross the two report forms, three anchor conditions and two cues, balancing the reversed policies within each cell. An explicitly dated **question** would test whether a listener can read the policy display. Putting the clarification **before** the cue and keeping the question ambiguous measures what happens to an established time over the intervening cue. Explicit instructions may make an anchor more persistent than the report alone. Applying their response probabilities to the target is a hypothesis.

## A prediction from one cue to the other

For each report form separately, let $A_c$ and $B_c$ be the four response probabilities after an explicit past or present anchor under cue $c$. If the report initially selects a present anchor with probability $s$ and those response laws carry over, the target vector is $(1-s)A_c+sB_c$. Use the posting-day cue’s “today” response to estimate $s$ where the controls separate. Check the other categories. Freeze that share and predict all four responses under the today cue using that cue’s own controls. The reserved weekday family plays no part in fitting or checking this prediction.

The strict past-topic proposal predicts the past-control row under each cue ($s=0$). The strict present-topic proposal predicts the present-control row ($s=1$). A mixed reading relaxes those predictions but still uses the same share across cues because cue assignment follows the report.

The example uses invented percentages for one form. The first two columns refer to the day implied by the answer after the policy reversal is scored.

| Display cue | Prior anchor | Posting-day rule | Today’s rule | Either | Couldn’t interpret |
|---|---|---:|---:|---:|---:|
| Posting day | Explicit past | 75 | 10 | 10 | 5 |
| Posting day | Explicit present | 15 | 65 | 15 | 5 |
| Posting day | Target for fitting | 60 | 23.75 | 11.25 | 5 |
| Today | Explicit past | 45 | 30 | 20 | 5 |
| Today | Explicit present | 5 | 80 | 10 | 5 |
| Today | Target prediction | 35 | 42.50 | 17.50 | 5 |

The first target gives $s=(23.75-10)/(65-10)=1/4$. Today’s answers then rise **18.75 percentage points** under the second cue with exactly the same initial share. A stable grammatical mixture gives the whole table. So does a listener who always understands the report as describing yesterday and retrieves a present decision frame on one quarter of the target trials before the cue. Both routes feed the same response process. Comparing the two verb forms can reveal a form effect on the recovered anchor if calibration carries over. A retrieval rule sensitive to the verb form can reproduce that difference too.

There is also a result that would falsify the shared prediction. Suppose the second target instead gives **15, 67.5, 12.5, 5**. Each cue fits its own controls exactly, but the second needs $s=3/4$. Allowing the best possible common share still leaves at least **13.64 percentage points of probability mass** to be moved in one cue. This is total variation distance, half the sum of absolute category differences. A failure could arise from the proposed readings, differential attention to an explicit clarification, or repair of the unusual report. A rise in “couldn’t interpret” can also defeat the prediction when the “today” percentage fits perfectly.

The exact calculation concerns population probabilities. For a finite illustration the script also uses simultaneous binomial intervals for all 24 category probabilities in the six rows, including the estimated controls. With 400 independent listeners in **each** row and counts exactly proportional to the falsifying example, the conservative check still retains common shares from .465 to .484. Failure to reject gives little assurance here. This fixed-table calculation supplies neither power nor a recruitment target. Generalization to new items would require independent items and participant and item uncertainty. [Executable calculation](listener_anchor.py)

## What the human evidence measures

Roberts and Liszka’s English native-speaker group gave the present-perfect items lower mean ratings with mismatching fronted time adverbials (2.53) than with matching ones (4.57, table 2). That makes a separate response for an unusable exchange important in our clause-final spoken design. Vos, Minor and Ramchand used gaze to measure attention to an event’s result state. The postal policy was changed independently of the posting, so attention to the outcome of posting gives no answer about which day’s policy the listener applies. Neither study supplies the endpoint probabilities above. [Roberts and Liszka](https://eprints.whiterose.ac.uk/id/eprint/77040/1/Second_Language_Research_2013_Roberts_413_39.pdf) · [Vos, Minor and Ramchand](https://doi.org/10.1017/S1360674325100452)

**Decision.** Keep the instrument for a question about temporal interpretation. Park it as a test that could establish re-licensing from listener responses alone. The controlled-learning branch of the reviewed plan asks whether choosing a competitor teaches a learner anything extra when the target could have conveyed the intended message.
