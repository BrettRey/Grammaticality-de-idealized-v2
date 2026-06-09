# Transparent-Relative Opportunity Data Pass

**Date:** 2026-06-09
**Target mixed cell:** `transparent-rare-relative-prediction`
**Primary graph under test:** `context-aware-operator-gap-candidate`
**Source lane:** Lane A, transparent free relatives

## Question

Does the operator-gap module handle rare transparent-relative cases by comparing attestation against
a checked opportunity denominator, rather than by treating raw rarity or recoverability as decisive?

## Sources Checked

Local source files:

- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Transparent_free_relatives/two-kinds.tex`
- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Transparent_free_relatives/coca-data/README.md`
- `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/Transparent_free_relatives/coca-data/context-checks.txt`

This pass uses the already checked COCA searches and local analysis recorded in those files. It
does not run a new corpus search.

## Checked Denominators

| Subtype | Raw/check denominator | Genuine target cases | Interpretation |
|---|---:|---:|---|
| `call` plus adjective search | 619 raw hits; 595 unique; 50 sampled | 17 genuine AP-nucleus transparent free relatives; 14 externally AP | Positive scoped attestation for attributional `call`; sample supports productivity but is not a full corpus prevalence estimate. |
| Other attributional verbs | `consider` 367 raw hits; `regard as` 36; `describe as` 32; `take to be` about 15 genuine cases in the local analysis | positive evidence recorded | Supports an attributional-verb lane, but not a complete denominator model. |
| `seem`/`appear` plus adjective searches | 178 unexcluded hits checked in context | 0 genuine AP-transparent target cases | Probative absence for this subtype: the checked hits were pre-nominal modifiers inside NP nuclei or ordinary free relatives in NP function. |
| Broader `seem`/`appear` suspicious windows | 474 examined results in the local `coca-data` audit | 0 genuine non-NP transparent target cases | Broader false-positive audit confirms that the zero result is not just an artefact of a single narrow query. |

## Result

`OPG` passes this lane-specific prediction test.

The result is not that transparent relatives are globally licensed or globally unlicensed. The result
is subtype-conditioned:

- attributional `call`-type contexts have positive scoped attestation;
- `seem`/`appear` AP-transparent contexts have checked absence with a meaningful denominator;
- raw frequency alone does not decide licensing;
- recoverability alone does not license the target subtype;
- opportunity-normalized attestation and preemption/competitor structure are the right constructs
  to keep in play.

## Graph Consequence

No graph mutation follows. `context-aware-operator-gap-candidate` already has the needed constructs:

- `usage_frequency`
- `opportunity_mass`
- `opportunity_normalized_attestation`
- `competitor_availability`
- `preemption_strength`
- `community_licensing`
- `semantic_pragmatic_recoverability`
- `repair_reformulation_pressure`

No numeric score movement follows. This is one source lane for one transparent-relative contrast
cell, not a general threshold model for rare relative constructions.

## Evaluation Update

The held-out evaluation cell `transparent-rare-relative-prediction` should move from `mixed` to
`passed` for Lane A. The independent-relative-`whose` lane remains unrun and should continue to be
treated as a separate low-opportunity uncertainty test.

## Residual Risk

- The positive `call` evidence is sampled, not a complete checked denominator.
- The `seem`/`appear` result is strong for the AP-transparent subtype, not for every possible
  transparent-relative subtype.
- No formal judgment experiment has been run for the `seem`/`appear` contrast.
- Independent relative `whose` still needs its own data pass or judgment-design pass.
