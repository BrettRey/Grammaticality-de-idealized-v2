# STATUS.md -- Grammaticality de-idealized

**Current phase:** Framework family / active development
**Last updated:** 2026-06-09
**Public/preprint state:** The OVMG family includes LingBuzz subproject preprints for `operator-stratum` and `asterisk-de-idealized`; `operator-stratum` was submitted to *Functions of Language* on 2026-06-02 and is under initial editorial evaluation. Check subproject folders before making public-state claims.
**Tracking note:** Root `STATUS.md` created 2026-05-31 from existing `CLAUDE.md`, `NOTES.md`, and `DECISIONS.md`; no source state was changed.

## Project Shape

This project develops the Operator-Value Model of Grammaticality (OVMG), separating objective grammaticality `G(u)` from the subjective feeling of grammaticality `F(u)`.

Current subproject map:

| Subproject | Function | State |
|---|---|---|
| `operator-stratum/` | What operators are | LingBuzz preprint, 2026-01-25; submitted to *Functions of Language*, 2026-06-02 |
| `asterisk-de-idealized/` | What grammaticality is | LingBuzz preprint, 2026-01-28 |
| `etiological-account/` | Why gaps emerge and persist | Draft |
| `feeling-of-ungrammaticality/` | What the feeling is | Seed |
| `evolutionary-dag-workbench/` | Rival conceptual DAGs for grammaticality | Scaffolded, 2026-06-07 |

## Current Open Threads

1. Powell's contingency/convergence framework is a priority connection but has not been integrated.
2. The operator-stratum paper still needs citation-form confirmation in `main.tex` (`reynolds2026operators` is currently marked `BRETT-VERIFY`), but the main paper now frames categoricality around role-functional operator contrasts rather than substance-based morphosyntax.
3. Bottom-up norm enforcement should be attributed to Richerson & Boyd 2005 and O'Connor 2019, not Powell.
4. Transparent free relatives remain an empirical test case for predictions about `F(u)`.
5. Kuribayashi et al. 2026 should resurface when returning to the predictability/processing-cost gap.
6. `subprojects/evolutionary-dag-workbench/` is now the non-commitment workspace for exploring rival grammaticality DAGs. Existing OVMG, detector, operator-value, Miller, usage-heavy, processing-heavy, and normativity-heavy models should be treated as seed graphs and counterexample sources, not conclusions.
7. The unification proposal collapsing `map`, `K`, and `C_t` into a single licensing hierarchy is deliberately not implemented. After Roughdraft review, the memo now recommends full unification if the criterion is the stronger/truer thesis rather than near-term readiness.

## Known Local State

The working tree has substantial pre-existing source, artifact, and literature drift. Do not treat local source as clean or provenance-classified without a project-specific pass.

Specific watchpoints:

1. `DECISIONS.md` is currently untracked but substantive; preserve it and track or commit it in a project cleanup session.
2. `refs.bib` appears as a typechange and should be inspected before build or provenance claims.
3. The many `subprojects/etiological-account/literature/` files are local literature workspace by default, not manuscript state.
4. A pre-revision safety copy of `main.tex` from 2026-06-09 is in `notes/main-2026-06-09-pre-review-revision.tex`.

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

1. Run a project-specific provenance pass to classify root source drift, the `refs.bib` typechange, and untracked literature/artifacts.
2. Decide the current priority branch: main OVMG, etiological account, operator integration, or feeling of ungrammaticality.
3. If returning to the main paper, integrate the operator-stratum explanation of why grammaticality concentrates on operator value.
4. If returning to the etiology paper, keep the corrected Richerson & Boyd/O'Connor mechanism separate from Powell's contingency/convergence framework.
5. If returning to the new DAG workbench, expand the phenomenon-card archive, enrich seed graphs, and run adversarial critique before treating any graph family as strong.
