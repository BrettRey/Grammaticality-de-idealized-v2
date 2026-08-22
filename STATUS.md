---
slug: grammaticality-de-idealized
kind: paper
title: Grammaticality de-idealized
stage: complete
external: preprint
blocked_on: []
updated: 2026-08-22
source:
- STATUS.md
- PORTFOLIO.md
- main.tex
preprints:
- lingbuzz/010118
next_action: Prepare an anonymous submission package for Linguistics while
  preserving the model's conditional empirical scope
notes: 'Title ("Grammaticality de-idealized") matches main.tex''s \title and STATUS.md''s own usage ("`Grammaticality
  de-idealized` is live on LingBuzz as `lingbuzz/010118`"). CLAUDE.md''s fuller internal label ("Grammaticality
  De-idealized: The OVMG Model") is a working/internal frame name, not the manuscript title, and is not
  in conflict with the sources used. The operator-stratum subproject (within this same directory) was
  itself desk rejected by Functions of Language on 2026-06-26 and is separately unretargeted. CHANGED
  by ADJUDICATION 2026-07-30: operator-stratum now has its own registry entry in batch-10.yaml, with `path`
  pointing at subprojects/operator-stratum, per the v2 rule that the registry unit is the manuscript rather
  than the directory. Brett authorised that specifically so the Functions of Language desk rejection would
  survive into the registry instead of sitting in a note. This block covers the main OVMG paper only.
  One sibling remains unregistered and is a candidate for the same treatment: subprojects/asterisk-de-idealized,
  which STATUS.md:6 records as a third LingBuzz subproject preprint in the OVMG family. It has a public
  preprint but no venue event, so it was not in the authorised four.'
---

# STATUS.md -- Grammaticality de-idealized
<!-- SUMMARY: OVMG main paper live as a preprint; multi-model formal repair implemented and verified · status: preprint live, formal-repair pass complete · updated: 2026-08-22 -->

**Current phase:** Main paper posted as preprint / formal repair, venue selection, and closed-loop stress test complete
**Last updated:** 2026-08-22
**Public/preprint state:** `Grammaticality de-idealized` is live on LingBuzz as `lingbuzz/010118`. Upload artifact: `Reynolds_2026_Grammaticality_de-idealized.pdf` generated from `main.pdf` on 2026-07-05. The OVMG family also includes LingBuzz subproject preprints for `operator-stratum` and `asterisk-de-idealized`; `operator-stratum` was submitted to *Functions of Language* on 2026-06-02 and desk rejected for scope/fit on 2026-06-26. It is not currently under review. Check subproject folders before making public-state claims.
**Tracking note:** Root `STATUS.md` created 2026-05-31 from existing `CLAUDE.md`, `NOTES.md`, and `DECISIONS.md`; no source state was changed.

## Project Shape

This project develops the Operator-Value Model of Grammaticality (OVMG), separating conventional grammatical status `G(u)` from the subjective feeling of grammaticality `F(u)`.

Current subproject map:

| Subproject | Function | State |
|---|---|---|
| `operator-stratum/` | What operators are | LingBuzz preprint, 2026-01-25; *Functions of Language* scope rejection, 2026-06-26; retarget TBD |
| `asterisk-de-idealized/` | What grammaticality is | LingBuzz preprint, 2026-01-28 |
| `etiological-account/` | Why gaps emerge and persist | Draft |
| `feeling-of-ungrammaticality/` | What the feeling is | Seed |
| `evolutionary-dag-workbench/` | Rival conceptual DAGs for grammaticality | Scaffolded, 2026-06-07 |

## Current Open Threads

1. LingBuzz metadata still needs one manual correction: `conventionaliz- ation` should be `conventionalization` in the keyword list for `lingbuzz/010118`. Both LingBuzz domains returned HTTP 502 on 2026-08-21, so the live field could not be checked or edited; the manuscript and PDF metadata already use the correct spelling.
2. Powell's contingency/convergence framework is a priority connection but has not been integrated.
3. The operator-stratum paper should now be cited as a LingBuzz preprint, not as under review at *Functions of Language*. The main paper still frames categoricality around role-functional operator contrasts rather than substance-based morphosyntax.
4. Bottom-up norm enforcement should be attributed to Richerson & Boyd 2005 and O'Connor 2019, not Powell.
5. Transparent free relatives remain an empirical test case for predictions about `F(u)`.
6. Kuribayashi et al. 2026 should resurface when returning to the predictability/processing-cost gap.
7. `subprojects/evolutionary-dag-workbench/` is now the non-commitment workspace for exploring rival grammaticality DAGs. Existing OVMG, detector, operator-value, Miller, usage-heavy, processing-heavy, and normativity-heavy models should be treated as seed graphs and counterexample sources, not conclusions.
8. The unification proposal collapsing `map`, `K`, and `C_t` into a single licensing hierarchy is deliberately not implemented. After Roughdraft review, the memo now recommends full unification if the criterion is the stronger/truer thesis rather than near-term readiness.
9. The July 10 formal revision replaced the older `G_t^\theta`/posterior-existence wording with `S_t^\theta` population status plus `\widehat{S}_t` estimate. Future edits should preserve the state/estimate distinction unless deliberately revising the ontology.
10. The §4 dynamics are now explicitly a coherent model with proof obligations, not a closed derivation: bounded-memory bimodality, winnerless-cell metastability, and operator-specific categoricality are conditional claims.
11. The August 22 likelihood repair and regenerated closed-loop audit are now stated in the manuscript: low/high separation is conditional on the adoption response and informative observation, while heterogeneous priors alone make normalized dispersion lag the mean after opportunity loss. Final review should police threshold circularity and keep repair outside the maintenance/control warrant.

## Known Local State

The working tree remains dirty, but its provenance was classified on 2026-08-21. Do not collapse the groups below into one submission change set.

Specific watchpoints:

1. **Submission-bearing source:** `main.tex`, `section3.tex`, the `refs.bib` link to the central bibliography, and the figure assets `figures/fig_agr_projection.pdf` and `trident.jpg`. The August 21 formal repair also changed `formalization/OVMG/Core.lean` and `formalization/README.md`; those files are a structural sanity check, not evidence establishing the empirical model. `CLAUDE.md`, `STATUS.md`, and `DECISIONS.md` are project guidance and records, not submission files.
2. **Generated artifacts:** `main.pdf` is the current rendered manuscript and `main.xdv` is an intermediate build artifact. `Reynolds_2026_Grammaticality_de-idealized.pdf` is the July 5 LingBuzz upload artifact and should not be mistaken for the repaired manuscript.
3. **Deliberate review provenance:** the August 21 zip, extracted review bundle, Codex/Opus/Aristotle reports, and `reviews/ox-alpha-formalization-review-20260821/` preserve prompts, inputs, outputs, hashes, and audits. Retain them locally; none belongs in a journal upload unless specifically requested.
4. **Local planning and literature workspace:** the July 10 formal-dynamics and reader-bridge notes, July 14 Cognition intake notes, and later source hooks are research records rather than manuscript source. The many `subprojects/etiological-account/literature/` files remain local literature workspace by default.
5. **Independent operational drift:** the absolute-path fixes in the etiological and evolutionary-DAG scripts, the verified Nefdt--Ladyman source-hook line, and `subprojects/operator-stratum/main.pdf` are separate work. Preserve them but exclude them from a root-paper submission or commit unless deliberately grouped.
6. A pre-revision safety copy of `main.tex` from 2026-06-09 is in `notes/main-2026-06-09-pre-review-revision.tex`.

### 2026-08-22 Session Notes

- Replaced the omission-LLR pseudo-count with the exact affine choice likelihood.
  Finite batches are represented as Beta mixtures and projected back to Beta by
  exact mean/variance matching after baseline-preserving discount. Independent
  quadrature, limiting cases, and generated-data recovery across population
  rates 0.1--0.9 pass.
- Added the full deterministic $(\theta,a,b)$ expected-window map, numerical
  Jacobian, and eigenvalue classification. Posterior-threshold adoption has two
  stable endpoint equilibria around an unstable crossing near 0.493 in the
  declared base cell. Logistic slope 8, not 16, is the first tested value with
  the three-crossing structure; the proportional response has one stable
  interior point. Reduced crossing slopes are not used as return rates.
- Revised the manuscript around these results. The cubic is now only a
  large-concentration limiting sketch; the adoption criterion must be
  independently motivated; concentration loss replaces dispersion-leading
  decline as the robust moribund precursor; and repair remains outside the
  warrant for maintenance or control.
- Added a finite-population closed-loop stress test in `tools/ovmg-tools/js/closed-loop-sim.mjs`. It composes the current normalized choice and evidence rules with per-speaker adoption--retention, compares three explicit response families, and does not assume the stipulated cubic normal form.
- The pre-repair statement about a calibrated negative-evidence scale and slope
  16 is superseded by the likelihood-consistent results above.
- A dominant outside option produces weak evidence without endpoint concentration in the declared high-utility cell. Low and high coupled states both return after their inclusion components alone are perturbed. The programmed majority-repair intervention is classified only as a wiring check, not independent support for a controller claim.
- In the opportunity-loss arm, heterogeneous priors make speaker evidence-mean dispersion grow sharply, but the mean reaches 25% and 50% of its eventual move first. The result is a conditional counterexample to heterogeneity alone being sufficient for the manuscript's dispersion-leading prediction; it is not an empirical language result or a judgment simulation.
- Exact parameters, seeds, diagnostics, replicate summaries, and the Ox Alpha refutation audit are preserved under `tools/ovmg-tools/results/` and `tools/ovmg-tools/reviews/`; full paths are deterministically regenerable. All 316 repaired checks pass, and two regenerations of the sweep produced SHA-256 `54f359dab7d63fb05bb7acdc19067d8698f73e62d1402ba27e147043ec275963`. Lean remains frozen and unchanged.

### 2026-08-21 Session Notes

- Three-model review of the formal apparatus (Claude Fable 5; Codex second opinion; Ox Alpha clean-room plus refutation-first adjudication via orx) converged on a repair plan. Plan of record: reviews/ox-alpha-formalization-review-20260821/raw-adjudication.md section 7.
- Key confirmed defects: omission-LLR normalization mismatch (candidate-only rho* vs outside-option denominator), double-discounted omission evidence, unclosed learner-to-population bridge (no z-dynamics), epistemic OBL inside the ontic status definition, joint likelihood not shared-latent, Lean confidence-bound and constraint-algebra gaps, paper/engine repair-link divergence, credit-assignment machinery not executable.
- Review artifacts: reviews/formalization-second-opinion-20260821.zip (bundle sent to external reviewers), reviews/formalization-second-opinion-codex-20260821.md, reviews/formalization-aristotle-hardening-20260821.md, and reviews/ox-alpha-formalization-review-20260821/ (manifest.yaml carries hashes, prompts, and usage).
- Implemented the repair across `main.tex`, `section3.tex`, the Lean scaffold, and `tools/ovmg-tools`: full-choice normalization, single discounting, explicit speaker-to-population transition, niche-indexed ontic obligatoriness with initialized hysteresis, stipulated population normal form, bearer-safe read-outs, constrained Lean types/laws, and executable contract alignment.
- Claude Opus found a first-pass niche/OBL defect, which was repaired; its report is preserved at `reviews/formalization-post-repair-opus-20260821.md`. Ox Alpha's final refutation audit then returned **MATERIAL FORMAL COHERENCE: YES**. The normalized local record and exact input are in `reviews/ox-alpha-formalization-review-20260821/` and registered in its manifest.
- Verification: `latexmk main.tex` passes with no undefined citations/references; `formalization/lake build` passes with no proof holes or forbidden shortcuts; `tools/ovmg-tools/make test` passes 27 legacy fixture, 46 smoke, 57 revised-core, 18 conditional-shell, and 168 closed-loop checks (316 total). Any future review bundle should include tests/ and the Makefile, which the original external reviewers lacked.
- Lean is frozen at this scope for the present paper. It should be described as an `OVMG structural sanity check`, not as formal verification; encoding the OBL recurrence or stochastic population dynamics is deferred unless a reviewer challenges those properties or formalization becomes a separate contribution.
- The journal target is *Linguistics: An Interdisciplinary Journal of the Language Sciences*. Its current scope fits the paper's combination of grammatical organization, meaning and use, community variation, diachrony, and mixed qualitative/quantitative method; it is diamond open access, and its current journal-specific author instructions do not state a Research Article word limit. *Journal of Linguistics* and *Glossa* are fallback targets only after substantial compression to their 15,000-word limits.
- Submission-facing metadata was refreshed: the abstract is 188 words (below the 200-word limit in *Linguistics*' instructions), and the acknowledgement now discloses drafting, editing, adversarial-review, and formalization assistance from the model families and services actually used.
- The project-specific provenance pass classified the dirty tree into submission source, generated build artifacts, deliberate review provenance, local planning/literature notes, and independent operational drift. Nothing was deleted or silently folded into the manuscript payload.

### 2026-07-10 Session Notes

- Reworked the §3 formal core around `S_t^\theta` as the population licensed-assembly state and `\widehat{S}_t` as its posterior estimate; `G_t` is retained only as compact estimate notation.
- Replaced atomic partial-function operator assignments with typed constraint unification, added explicit within-speaker joint-distribution caveats, and introduced epistemic-vs-population-heterogeneity variance decomposition.
- Split confidence into evidence confidence `\Phi^{ev}` and decision confidence `\Phi^{dec}`, so concentrated interior community division no longer masquerades as a confident binary verdict.
- Rebuilt §4's production/update/omission machinery: normalized gated-choice production, baseline-preserving discounted Beta update, generalized-Bayes effective-count caveat, and log-likelihood omission evidence with `p_t^-`/`p_t^+` instead of `q_i`.
- Demoted overstrong dynamics language: bounded-memory bimodality is a stationary-distribution target; operator-specific categoricality depends on independently estimated `N_t\cdot\Delta`; winnerless cells need low support/weak diffuse negative evidence in addition to avoidance; moribund dispersion needs heterogeneous priors/networks/recent histories.
- Added a reader-facing bridge at the start of §3.2: it gives the four assembly questions in ordinary language before the notation, then distinguishes community state from evidence-based estimate. The notation table now follows the bridge; page flow was visually checked on pp. 19--21.
- Refreshed the Lean scaffold and the separate `ovmg-tools` v2 core: typed constraint compatibility, speaker-level assembly status, latent lects, multi-node candidate-to-node availability, and a toy joint likelihood now share one interpretation. The implementation is an executable correctness layer, not a fitted empirical model; scalable inference remains conditional on an independently fixed contrast and coding protocol.
- Verification: `latexmk -silent main.tex` passed; targeted greps found no old `G_t^\theta`, `q_i`, inline `p\approx`, or binary-Beta scar tissue; `git diff --check` passed. Remaining log messages are routine EB Garamond font substitution and over/underfull boxes.

### 2026-07-05 Session Notes

- Finished the main-paper polishing arc: bibliography/source checks, terminology hygiene, category/level-error pass, `stable gap` -> `preempted gap`, operator/function glosses, double-parenthesis and quotation/macro cleanup, heading simplification, redundancy/cohesion pass, and final editorial-scar-tissue sweep.
- Added and integrated the Turkish suffix-harmony appendix as an indirect operator-exponent test case: harmony affects grammaticality when an inflectional operator lacks a well-formed exponent, not because vowel backness itself is a public-update value.
- Made the model's theoretical costs explicit in the conclusion: OVMG lacks one-variable simplicity and carries a significant, schematized memory burden.
- Prepared `Reynolds_2026_Grammaticality_de-idealized.pdf` for LingBuzz upload; live handle is `lingbuzz/010118`.
- Verification before upload prep: `latexmk main.tex` passed; no undefined citations or references; remaining messages are routine font/overfull/duplicate-object warnings.

## 2026-06-09 Revision Session

- Revised `main.tex` against the referee-style review: K now uses a null/reject outcome; `I have 25 years` is consistently treated as age-frame non-licensing; productivity is handled by hierarchical constructional partial pooling; `rho_t^\star` is defined over analogically generated candidates; `\widetilde{G}_t` now projects into production, repair, satiation, transmission, and change trajectories.
- Reworked the CxG/UBA comparison sections to match the companion paper's functional boundary: categorical grammaticality clusters around closed-paradigm, high-opportunity, update-critical contrasts rather than morphosyntax as a substance class.
- Added weak/mechanistic emergence only where tied to the formalism: categoricality is bimodality in the stationary distribution of licensing posteriors, with Hopper's "emergent grammar" explicitly distinguished.
- Added `notes/BRETT-VERIFY-2026-06-09.md` for companion citation form, Keller reference selection, and the unresolved "objective grammaticality" vs "conventional status" terminology choice.
- Build check: `latexmk -xelatex main.tex` succeeds and writes `main.pdf` (44 pages). Remaining warnings are routine overfull boxes, EB Garamond bold substitution, one float placement adjustment, and repeated `xdvipdfmx` duplicate destination warnings for table/figure anchors.

## Next-Touch Note: Operator Ecology

- Treat `subprojects/operator-stratum/` as the bridge paper for the whole family, not a side paper. The core generalization is that grammaticality judgments target **operator value**: closed, public-update repertoires that configure commitments, roles, scope, reference, and repair.
- Map this back onto the grammaticality variables explicitly: `map` asks whether a form can host operator value at all; `K` asks whether the operator values cohere; `C_t` asks whether the operator value is licensed and entrenched under opportunity and preemption.
- This should guide the main OVMG paper, the asterisk paper, the etiology branch, the feeling branch, the Miller revision path, LBC, and Varieties. It prevents the family from saying merely that morphosyntax is special; morphosyntax is special where it realizes public coordination infrastructure.

## 2026-07-14 Secondary Literature Hook: Iaia and Tavano (2026)

Source: `/Users/brettreynolds/Downloads/2026.07.11.737945v1.full.md`; bioRxiv v1, DOI `10.64898/2026.07.11.737945`.

When returning to the predictability/processing-cost gap, consider this as background for the subjective processing channel. Corpus-derived local expectations selectively improved MEG decoding of theory-defined unresolved-structure or memory features, whereas completion or integration features showed a different lag profile and generally stronger word-offset decoding. This may help distinguish locally maintained prediction from word-bound structural resolution on the processing-heavy side of the OVMG family.

**Cautions:** This is not evidence about population licensing, grammatical status, operator value, anomaly judgments, or the dynamics of `S_t^\theta`, `\widehat{S}_t`, `F`, or `\Phi`. The study presents ordinary-speech comprehension rather than violations or grammaticality judgments. "Prior knowledge" is a Brown-Corpus proxy, the feature families are theory-defined, and MEG decoding does not establish two causal systems. Treat it as processing background, not support for the OVMG ontology or formal model. The source is a non-peer-reviewed v1 preprint based on 25 English listeners and four stories.

## Next Actions

1. Prepare an anonymous *Linguistics* submission package from `main.tex`, `section3.tex`, `refs.bib`, and the cited figures; keep the review records, Lean sources, and project-management files outside the upload unless the editor asks for them.
2. Retry the LingBuzz keyword correction on `lingbuzz/010118` when the service recovers: `conventionaliz- ation` -> `conventionalization`.
3. Keep the Lean layer frozen as a structural sanity check unless referee feedback supplies a concrete reason to extend it.
4. If the *Linguistics* route fails on length or framing, do not send the same 24,500-word manuscript to *Journal of Linguistics* or *Glossa*; first produce a distinct <=15,000-word version.
5. If returning to the etiology paper, keep the corrected Richerson & Boyd/O'Connor mechanism separate from Powell's contingency/convergence framework.
6. If returning to the new DAG workbench, expand the phenomenon-card archive, enrich seed graphs, and run adversarial critique before treating any graph family as strong.

## Related reading — Cognition 2026 intake (2026-07-14)
Sources routed from a *Cognition* 2026 batch. Central index: `literature/cognition-2026-intake.md`. Verify claims/citations before use.
- **Bilingual links between multi-word phrases** [] — `notes/lit-cognition-2026-bilingual-mwe-phrases.md`
- **Gradedness survives semantic type errors** [medium] — `notes/lit-cognition-2026-graded-inconceivable.md`
- **Candidate sets distinguish ambiguity from ignorance** [medium] — `notes/lit-cognition-2026-knowability-curiosity.md`
- **Coupling history changes sensory attenuation** [medium] — `notes/lit-cognition-2026-sensory-attenuation.md`
- (cross-ref) time-resolves-role-reversal — `notes/source-hooks/cognition-2026-time-resolves-role-reversal.md`
