# STATUS.md -- Grammaticality de-idealized

**Current phase:** Main paper posted as preprint / active follow-up
**Last updated:** 2026-07-05
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

1. LingBuzz metadata needs one manual correction if not already fixed: `conventionaliz- ation` should be `conventionalization` in the keyword list for `lingbuzz/010118`.
2. Powell's contingency/convergence framework is a priority connection but has not been integrated.
3. The operator-stratum paper should now be cited as a LingBuzz preprint, not as under review at *Functions of Language*. The main paper still frames categoricality around role-functional operator contrasts rather than substance-based morphosyntax.
4. Bottom-up norm enforcement should be attributed to Richerson & Boyd 2005 and O'Connor 2019, not Powell.
5. Transparent free relatives remain an empirical test case for predictions about `F(u)`.
6. Kuribayashi et al. 2026 should resurface when returning to the predictability/processing-cost gap.
7. `subprojects/evolutionary-dag-workbench/` is now the non-commitment workspace for exploring rival grammaticality DAGs. Existing OVMG, detector, operator-value, Miller, usage-heavy, processing-heavy, and normativity-heavy models should be treated as seed graphs and counterexample sources, not conclusions.
8. The unification proposal collapsing `map`, `K`, and `C_t` into a single licensing hierarchy is deliberately not implemented. After Roughdraft review, the memo now recommends full unification if the criterion is the stronger/truer thesis rather than near-term readiness.

## Known Local State

The working tree has substantial pre-existing source, artifact, and literature drift. Do not treat local source as clean or provenance-classified without a project-specific pass.

Specific watchpoints:

1. Current dirty state after the LingBuzz-prep session includes modified `main.tex`, `main.pdf`, `main.xdv`, `figures/fig_agr_projection.{pdf,png}`, and `figures/make_agr_projection.py`; deleted tracked PDFs `LingbuzzPreprint.pdf` and `exploratory-lbe.pdf`; untracked `literature/` and review-board logs. Do not treat the tree as clean without a provenance pass.
2. `Reynolds_2026_Grammaticality_de-idealized.pdf` is the upload artifact and may be ignored/untracked by the repository's PDF rules.
3. The many `subprojects/etiological-account/literature/` files are local literature workspace by default, not manuscript state.
4. A pre-revision safety copy of `main.tex` from 2026-06-09 is in `notes/main-2026-06-09-pre-review-revision.tex`.

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

## Next Actions

1. Fix the LingBuzz keyword artifact on `lingbuzz/010118` if not already corrected: `conventionaliz- ation` -> `conventionalization`.
2. Run a project-specific provenance pass to classify root source drift and untracked literature/artifacts.
3. Decide the current priority branch: post-LingBuzz main OVMG cleanup, etiological account, operator integration, or feeling of ungrammaticality.
4. If returning to the main paper, use `lingbuzz/010118` as the public citation handle and keep the Turkish appendix's indirect operator-exponent framing.
5. If returning to the etiology paper, keep the corrected Richerson & Boyd/O'Connor mechanism separate from Powell's contingency/convergence framework.
6. If returning to the new DAG workbench, expand the phenomenon-card archive, enrich seed graphs, and run adversarial critique before treating any graph family as strong.
