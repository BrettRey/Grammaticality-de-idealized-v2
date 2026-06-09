# Audience Reference Pilot Packet

This packet is for a small pilot or structured critic run. It is not itself evidence.

For each item, read the context and target sentence, then answer each response prompt
separately. Do not collapse the prompts into a single acceptability judgment.

Use the response template at `data/audience-reference-projection/pilot-response-template.csv`
for row-level coding.

## Response Channels

### reference_identification

- Prompt: Who does the target pro-form refer to? How confident are you?
- Response type: forced_choice_plus_confidence
- Scale or labels: referent options; confidence 1-7

### feature_personhood_fit

- Prompt: Does the pro-form fit the described referent in this context?
- Response type: likert
- Scale or labels: 1=does not fit; 7=fits very well

### reported_acceptability

- Prompt: How acceptable or natural is the sentence in the stated context?
- Response type: likert
- Scale or labels: 1=very unacceptable/unnatural; 7=fully acceptable/natural

### grammaticality_attribution

- Prompt: If something is wrong here, what kind of problem is it?
- Response type: category
- Scale or labels: grammar error; style/register issue; respect/policy issue; reference ambiguity; no problem; other

### social_sanction

- Prompt: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- Response type: category_plus_optional_reason
- Scale or labels: correct; challenge; avoid; leave alone; depends

### norm_orientation

- Prompt: Which audience, rule, or institution are you orienting to in your judgment?
- Response type: category
- Scale or labels: ordinary conversation; school correctness; workplace policy; community-local norm; personal preference; other

## Stimuli

### aud-ref-001

- Cell: `low-stakes-reference`
- Audience/evaluator: `ordinary_interlocutor`
- Norm centre: `descriptive_usage`
- Speaker identity: `unmarked`

**Context**

Riley left a jacket in the seminar room. The next sentence is from a classmate.

**Target Sentence**

Riley said they would come back for it after lunch.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-ref-002

- Cell: `low-stakes-reference`
- Audience/evaluator: `ordinary_interlocutor`
- Norm centre: `descriptive_usage`
- Speaker identity: `unmarked`

**Context**

Maria emailed the committee about the schedule. The next sentence is from the chair.

**Target Sentence**

Maria said she would send the revised agenda tonight.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-pol-001

- Cell: `policy-or-identity-framing`
- Audience/evaluator: `ordinary_interlocutor`
- Norm centre: `descriptive_usage`
- Speaker identity: `unmarked`

**Context**

Morgan uses they/them pronouns. A coworker is speaking informally after a meeting.

**Target Sentence**

Morgan said they would update the file tomorrow.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-pol-002

- Cell: `policy-or-identity-framing`
- Audience/evaluator: `teacher_editor`
- Norm centre: `school_standard`
- Speaker identity: `unmarked`

**Context**

Morgan uses they/them pronouns. A teacher is marking a grammar worksheet that asks for traditional singular/plural agreement.

**Target Sentence**

Morgan said they would update the file tomorrow.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-pol-003

- Cell: `policy-or-identity-framing`
- Audience/evaluator: `institution_policy_officer`
- Norm centre: `institutional_policy`
- Speaker identity: `institutional_representative`

**Context**

Morgan uses they/them pronouns. The sentence appears in a workplace inclusion policy example.

**Target Sentence**

Morgan said they would update the file tomorrow.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-amb-001

- Cell: `policy-or-identity-framing`
- Audience/evaluator: `ordinary_interlocutor`
- Norm centre: `descriptive_usage`
- Speaker identity: `unmarked`

**Context**

Alex talked with Sam after the meeting. The next sentence appears without further context.

**Target Sentence**

They said the plan had changed.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-amb-002

- Cell: `policy-or-identity-framing`
- Audience/evaluator: `institution_policy_officer`
- Norm centre: `institutional_policy`
- Speaker identity: `institutional_representative`

**Context**

Alex talked with Sam after the meeting. The sentence appears in a policy memo without further context.

**Target Sentence**

They said the plan had changed.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-pers-001

- Cell: `personified-referent`
- Audience/evaluator: `ordinary_interlocutor`
- Norm centre: `descriptive_usage`
- Speaker identity: `unmarked`

**Context**

A family is talking about a dog they treat as a companion.

**Target Sentence**

Luna barked until her dinner was ready.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-pers-002

- Cell: `personified-referent`
- Audience/evaluator: `ordinary_interlocutor`
- Norm centre: `descriptive_usage`
- Speaker identity: `unmarked`

**Context**

A veterinary report describes the same dog in an administrative record.

**Target Sentence**

Luna barked until its dinner was ready.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-chain-001

- Cell: `personified-referent`
- Audience/evaluator: `ordinary_interlocutor`
- Norm centre: `descriptive_usage`
- Speaker identity: `unmarked`

**Context**

A story first introduces a ship as an object and then changes the pro-form without explanation.

**Target Sentence**

The vessel left port at dawn. She reached the harbour before nightfall.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

### aud-chain-002

- Cell: `personified-referent`
- Audience/evaluator: `ordinary_interlocutor`
- Norm centre: `descriptive_usage`
- Speaker identity: `unmarked`

**Context**

A story explicitly personifies a ship before using a personal pro-form.

**Target Sentence**

The crew called the vessel Amelia. She reached the harbour before nightfall.

**Prompts**

- `reference_identification`: Who does the target pro-form refer to? How confident are you?
- `feature_personhood_fit`: Does the pro-form fit the described referent in this context?
- `reported_acceptability`: How acceptable or natural is the sentence in the stated context?
- `grammaticality_attribution`: If something is wrong here, what kind of problem is it?
- `social_sanction`: Would you correct, challenge, avoid, or leave this form alone in the stated situation?
- `norm_orientation`: Which audience, rule, or institution are you orienting to in your judgment?

## Coding Boundary

For evidence updates, code the response channels independently. A row can support the
audience/reference prediction only if reference identification is recorded separately
from acceptability, attribution, sanction, and norm orientation.
