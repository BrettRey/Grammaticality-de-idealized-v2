# State of the Evolutionary DAG Workbench

**Date:** 2026-06-09
**Status:** Internal state-of-search report
**Boundary:** This is not a theory paper, release note, or score authorization.

## Short Verdict

The workbench is now useful enough to visualize and write up internally. It has not discovered a
general theory of grammaticality. It has discovered a set of scoped modules, repeated pressure
points, plus one completed source-denominator lane that makes the next round less dependent on
expert judgment.

All numeric scores remain zero. Seven graphs currently have `scoped_module` labels backed by
protocol-bound or held-out `scope-only` evaluations. `TEMP` has now joined the candidate set as a
built-on temporal-anchor module without a scoped label. The strongest current result is division of
labor, not a winner.

The next useful work is not more graph invention by default. It is to put the existing modules under
additional data pressure, especially through a pronoun/pro-form audience-reference task run, a
human judgment run for independent relative `whose`, or a second held-out modal/conditional card for
`TEMP`.

## Current Search Shape

```mermaid
flowchart LR
  DYN["DYN<br/>context/diachrony"]
  OPG["OPG<br/>operator gap/opportunity"]
  AUD["AUD<br/>pronoun/reference/audience"]
  PROC["PROC<br/>processing/naturalness"]
  UPT["UPT<br/>uptake/operator boundary"]
  FRAME["FRAME<br/>frame-specific licensing"]
  AGR["AGR<br/>agreement controller/override"]
  TEMP["TEMP<br/>temporal anchoring"]

  DYN --> ContextCases["needs washed<br/>robust vernaculars<br/>register fragments"]
  OPG --> GapCases["left-branch extraction<br/>fused relatives<br/>rare forms"]
  AUD --> PronounCases["pro-forms<br/>singular they<br/>identity framing"]
  PROC --> ProcessingCases["center embedding<br/>garden paths<br/>locality"]
  UPT --> UptakeCases["clause type<br/>interjections<br/>move type"]
  FRAME --> FrameCases["I have five years<br/>island variation"]
  AGR --> AgreementCases["measure NPs<br/>fused heads<br/>coordination<br/>number construal"]
  TEMP --> TemporalCases["perfect + yesterday<br/>narrative present<br/>modal perfect<br/>modal preterite pressure"]
```

This map should be read as a live partition of work, not as a taxonomy. The modules are useful
because each now has a reasonably sharp boundary:

| Module | Current scope | Stronger cases | Boundary |
|---|---|---|---|
| `DYN` | Context-indexed licensing, ideology, production, correction, and judgment over time | `needs-washed`, robust vernaculars, register fragments, frequent condemned forms | Not an operator-gap, processing, pronoun-reference, or agreement-controller account |
| `OPG` | Opportunity-normalized attestation, recoverability, preemption, operator gaps, and repair pressure | left-branch extraction, rare forms, fused relative constructions, fused-head NPs | Not a category-measurement, selection, agreement-controller, or diachronic account |
| `AUD` | Pronoun/pro-form reference tracking, personhood ascription, audience design, and social-indexical judgment channels | pronoun/pro-form personhood cases, singular `they` partly | Not a diachronic stabilization or general licensing account |
| `PROC` | Processing cost, recoverability, felt naturalness, task effects, and attribution perturbation | center embedding, garden paths, dependency locality, legalese partly | Not a licensing, agreement-feature, or production-feedback account |
| `UPT` | Update-role configuration, repertoire closedness, token innovability, stance, genre fit, and repair | clause type, interjection boundaries, duration-frame answer partly | Not a general social-indexical or operator-gap account |
| `FRAME` | Question-answer frame fit and construction-specific dependency licensing | `I have five years`, island construction variation | Not an opportunity/preemption or general temporal-anchor account |
| `AGR` | Controller identification, feature alignment, licensed override, notional basis, and retrieval-attractor salience | measure-NP agreement, fused determiner-head agreement, coordination and number-construal pressure | Not a category-analysis, pronoun/audience, diachronic, or general grammaticality account |
| `TEMP` | Temporal-anchor fit across tense/aspect, modal inference, current relevance, continuative intervals, experiential frames, and narrative perspective | perfect plus definite past time, continuative perfect, already plus yesterday, narrative present, modal perfect by now; modal preterite partly | Held-out modal-preterite test is partial; not scoped until modal-remoteness pressure is resolved |

## Evaluation Ladder

```mermaid
flowchart LR
  Seed["Seed graph"] --> Attack["Adversarial critique"]
  Attack --> Mutate["Graph mutation"]
  Mutate --> Eval["Protocol-bound evaluation"]
  Eval --> HeldOut["Held-out evaluation"]
  HeldOut --> Scope["scope-only module label"]
  Scope --> Measure["Measurement or parameterized test"]
  Measure --> Score["Numeric score movement"]
  Score --> General["general-account consideration"]

  Eval -. "no score" .-> Zero["all scores remain zero"]
  Scope -. "scope-only" .-> Zero
```

The ladder matters because the workbench has repeatedly become more credible when it refuses to
promote too early. A module can be real enough to retain as a scoped search object without earning a
numeric score. Numeric movement should wait for prediction paths and held-out data that are not just
the cards used to build the graph.

## What Has Stabilized

- The ontology is doing real work. It keeps `reported_acceptability`, `felt_naturalness_context`,
  `grammaticality_attribution`, `community_licensing`, `standard_language_ideology`, and
  `usage_frequency` apart.
- Edge profiles are now useful as prediction commitments, but only on activated paths. They should
  not be treated as a parameterized model yet.
- The discovery rule is doing useful anti-alignment work. A graph is not rewarded for reproducing
  OVMG, the operator-stratum paper, CGEL, or any other prior account.
- Held-out cards are now more informative than new seed cards, provided they carry source evidence,
  contrast cells, activated paths, and pass/fail conditions.
- The repeated pressure points are no longer vague: temporal anchoring now has a built-on `TEMP`
  candidate, while catenative complement subtypes, agreement-controller overrides,
  repair-neighbour distance, meaning priors, and audience/reference channels remain separate
  pressures.
- Number construal and realization have now been consolidated under `AGR` without adding a new
  construct: notional basis, controller identification, override pattern, feature alignment, and
  attractor salience remain sufficient for the current agreement bundle.
- `TEMP` has now received its first held-out temporal/modal test. It partly survives modal
  preterite remoteness but lacks a modal-remoteness or remote-conditional frame, so promotion is
  blocked.
- Comparative illusions now reinforce complementarity rather than mutation: category-analysis
  leakage belongs with `CAT`, repair distance with `RNR`/`INR`, and intended-meaning plausibility
  with `MPR`.

## Empirical Lanes

### Transparent-relative opportunity

The transparent-relative lane is the first completed source-denominator test of `OPG`, because it
distinguishes raw rarity from probative absence.

```mermaid
flowchart LR
  Raw["raw hits"] --> Filter["false-positive filter"]
  Filter --> Denom["checked opportunity denominator"]
  Denom --> Genuine["genuine transparent count"]
  Genuine --> ONA["opportunity-normalized attestation"]
  ONA --> Warrant["licensing warrant"]

  HighZero["high denominator + zero genuine"] --> Undercut["subtype undercut"]
  LowZero["low denominator + zero genuine"] --> Uncertain["uncertainty, not rejection"]
  Restricted["positive but restricted attestation"] --> Scoped["scoped licensing"]
```

The design is specified in
`notes/transparent-relative-opportunity-measurement-design-2026-06-09.md`. Lane A is now recorded in
`notes/transparent-relative-opportunity-data-pass-2026-06-09.md`: attributional `call`-type contexts
show sampled positive scoped attestation, while `seem`/`appear` AP-transparent contexts show checked
zero genuine cases over a meaningful opportunity denominator. This moves the `OPG` held-out
prediction from `mixed` to `passed` for this lane only. Lane B is recorded in
`notes/independent-relative-whose-opportunity-lane-2026-06-09.md` as measurement readiness rather
than human evidence.

### Pronoun/pro-form audience and reference

The pronoun/pro-form lane is the best immediate test of `AUD`, because it separates reference
success, personhood ascription, audience design, policy/institutional framing, and reported
acceptability.

```mermaid
flowchart LR
  Ref["reference success task"] --> Accept["reported acceptability"]
  Policy["policy/institution cue"] --> Social["social-indexical value"]
  Audience["audience/evaluator cue"] --> Social
  Identity["speaker or referent identity"] --> Social
  Social --> Accept
  Accept --> Attribution["grammaticality attribution"]
  Ref -. "forbidden shortcut" .-> Licensing["community licensing"]
```

The point is not to ask whether a pronoun form is "really grammatical" in the abstract. The task
design in `notes/pronoun-audience-policy-task-design-2026-06-09.md` varies audience, policy frame,
speaker/referent identity, and reference success so the graph has to predict which channel changes.
If reference succeeds but acceptability shifts with audience or institutional frame, that supports
the audience/reference split. If reference failure drives the same judgments regardless of audience,
`AUD` is too social-indexical for the case.

## What Not To Write Yet

This is not ready to be written as a general discovery result. In particular, do not yet claim:

- that one graph is the best account;
- that numeric scores measure evidential support;
- that relation profiles already derive predictions mechanically;
- that `scoped_module` labels are equivalent to empirical confirmation;
- that all CGEL cards have been systematically sampled;
- that the cards already form a balanced phenomenon corpus.

The defensible write-up is narrower: the workbench now has a controlled ontology, enforceable lint
rules, scoped modules, and two empirical lanes where it can start earning projective pressure.

## Next Moves

1. Run the pronoun/pro-form audience-reference task if data collection is available.
2. Run the independent-relative-`whose` human judgment task if data collection is available.
3. Add evaluation-level prediction paths only where a card actually activates an edge path.
4. Keep numeric scores at zero until a held-out, source-backed evaluation proposes score movement
   through profiled paths.
5. Use visual summaries only at the module and evaluation-ladder level until graph-level prediction
   paths become load-bearing.
