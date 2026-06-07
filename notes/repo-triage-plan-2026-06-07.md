# Repository Triage Plan

**Date:** 2026-06-07
**Trigger:** External review of the public `Grammaticality-de-idealized-v2` repository.
**Goal:** Make the public repo safer, clearer, and more reproducible without erasing useful research-state material.

## Verified Findings

- `LingbuzzPreprint.tex` contains unresolved conflict markers in several places.
- `a_an_allophone_pre_reg_plan.tex` also contains unresolved conflict markers, although it was not mentioned in the review.
- `main.tex` declares XeLaTeX and uses `fontspec`; `AGENTS.md` still recommends `latexmk -pdf` and `pdflatex`.
- There is no root `README.md`, root `LICENSE`, `.latexmkrc`, `requirements.txt`, or `pyproject.toml`.
- Tracked generated or semi-generated root files include `main.xdv`, `biber_debug.txt`, `biber_err.txt`, `biber_out.txt`, `simulation_data.dat`, and several PDFs.
- The repo still has substantial unrelated dirty state: modified `main.tex`, `main.pdf`, `NOTES.md`, status files, a `refs.bib` typechange, and many untracked literature files.

## Load-Bearing Assumptions

- The canonical public source is `main.tex`, not `LingbuzzPreprint.tex`.
- The immediate goal is repo hygiene and public reproducibility, not a full conceptual OVMG rewrite.
- Generated build products should be ignored by default, but canonical PDFs may remain tracked if explicitly documented.
- Private working notes should not be deleted in a cleanup pass; they should be documented or moved only after a provenance pass.

## Phase 1: Safe Public-Hygiene Fixes

These are low-risk and should be done first.

1. Resolve conflict markers in `LingbuzzPreprint.tex`.
   - Prefer the more current "near-zero entrenchment/stable gap" language over categorical structural-ban wording where the local context supports it.
   - Preserve substantive HEAD additions unless they are clearly duplicated or stale.
   - Run a conflict-marker scan afterward.

2. Resolve conflict markers in `a_an_allophone_pre_reg_plan.tex`.
   - Treat this as an archival/prereg cleanup, not a conceptual rewrite.
   - Preserve the richer analysis-plan text unless the conflict clearly marks it as superseded.

3. Add `.latexmkrc` with XeLaTeX as the default engine.
   - Use `latexmk -xelatex` behavior by default.
   - Keep biber in the normal latexmk dependency chain.

4. Update `AGENTS.md` build instructions.
   - Replace `latexmk -pdf main.tex` with `latexmk main.tex` or `latexmk -xelatex main.tex`, depending on `.latexmkrc`.
   - Remove the `pdflatex main.tex` suggestion.
   - Keep the existing simulation command.

5. Add generated-artifact ignore rules to `.gitignore`.
   - Add `.xdv`, biber debug/output files, common generated PDFs policy notes, and generated simulation data as appropriate.
   - Do not remove tracked PDFs yet unless Phase 2 approves their status.

6. Add a root `README.md`.
   - State the public status.
   - Identify `main.tex` as canonical.
   - Explain `LingbuzzPreprint.tex`, old drafts, side projects, and `subprojects/`.
   - Give build commands and script dependencies.
   - State that dirty/private research notes exist and are not necessarily canonical claims.

7. Add a root `LICENSE` or a license note.
   - If the intended license is CC BY 4.0 for paper prose, add a standard CC BY 4.0 license file or a concise repository license note.
   - If code should use a different license, split prose/code licensing explicitly.

## Phase 2: Cleanup That Needs Explicit Choice

These are higher-blast-radius because they change what the public repository presents as canonical.

1. Decide which PDFs, if any, remain tracked.
   - Candidate to keep: `main.pdf` only if it is a canonical release artifact.
   - Candidate to untrack: `LingbuzzPreprint.pdf`, `exploratory-lbe.pdf`, and generated subproject PDFs unless documented as releases.

2. Remove tracked generated files from git.
   - Candidates: `main.xdv`, `biber_debug.txt`, `biber_err.txt`, `biber_out.txt`, `simulation_data.dat`.
   - Use `git rm --cached` where the local file should stay on disk but no longer be tracked.

3. Rationalize root source layout.
   - Move archival drafts into `archive/`.
   - Move public or released PDFs into `preprints/` or `releases/`.
   - Move one-off scripts/data into `scripts/` and `outputs/`.
   - Defer unless you want a visible repo-architecture cleanup now.

4. Separate public docs from private working notes.
   - Keep public `README.md`, `STATUS.md`, and `DECISIONS.md`.
   - Move correspondence-adjacent or agent-session notes only after checking provenance.

5. Add CI.
   - A minimal GitHub Actions workflow can build `main.tex` with XeLaTeX and biber.
   - This should wait until local `latexmk main.tex` succeeds cleanly.

## Phase 3: Paper Revision Track

These should not be mixed into the repo-hygiene commit.

1. Decide whether the canonical model name is MVMG or OVMG.
   - If OVMG is now canonical, revise conceptually, not by global replacement.
   - Add a historical terminology note only if older names remain in archived files.

2. Tighten `K(u,c)`.
   - Restrict it to grammar-relevant operator/value coherence or split lexical-conceptual plausibility from grammar-relevant coherence.

3. Operationalize `c`, `C_t`, and expected rarity.
   - Define how experiments, corpus studies, and dialect cases set the conditioning state.
   - Add falsification conditions for the prediction section.

4. Build one worked empirical case.
   - Best candidates: independent relative `whose` or left-branch extraction.
   - Add a small expectation model and a proposed satiation or corpus test.

## Proposed First Commit

Commit only Phase 1 items:

```text
Fix public repo build and conflict hygiene
```

This commit would:

- resolve conflict markers in two `.tex` files;
- add `.latexmkrc`;
- correct `AGENTS.md`;
- add a root `README.md`;
- add or clarify licensing;
- extend `.gitignore`;
- leave generated tracked files and root restructuring for a later explicit decision.

## Checks After Phase 1

```bash
rg -n '<<<<<<<|=======|>>>>>>>' .
latexmk -C main.tex
latexmk main.tex
git diff --check
```

If `latexmk main.tex` fails for reasons unrelated to the Phase 1 changes, record the failure in the final note rather than broadening the cleanup pass.
