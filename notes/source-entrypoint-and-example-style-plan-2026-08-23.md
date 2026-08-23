# Descriptive paper entrypoints and numbered-example typography

## Outcome

Replace generic `main.tex`/`main.pdf` entrypoints with filenames that identify
the paper, and normalize numbered object-language examples to `\mention{}`.
The change should make directory listings, build commands, PDFs, and agent
instructions self-explanatory without altering any paper's title or argument.

## Validated scope

The repository has four live, tracked paper entrypoints named `main.tex`:

| Paper | Source rename | Canonical PDF rename |
|---|---|---|
| Grammaticality de-idealized | `main.tex` → `grammaticality-de-idealized.tex` | `main.pdf` → `grammaticality-de-idealized.pdf` |
| De-idealizing the asterisk | `subprojects/asterisk-de-idealized/main.tex` → `subprojects/asterisk-de-idealized/asterisk-de-idealized.tex` | `main.pdf` → `asterisk-de-idealized.pdf` |
| Etiological account | `subprojects/etiological-account/main.tex` → `subprojects/etiological-account/etiological-account.tex` | `main.pdf` → `etiological-account.pdf` |
| Operator stratum | `subprojects/operator-stratum/main.tex` → `subprojects/operator-stratum/operator-stratum.tex` | `main.pdf` → `operator-stratum.pdf` |

The shorter subproject slugs are preferable to filename-length versions of the
full titles: they are meaningful, stable if a title changes, and consistent with
the repository's lower-case hyphenated naming rule.

Excluded from the rename:

- `reviews/formalization-second-opinion-20260821/paper/main.tex`, which is a
  frozen review input rather than a live paper;
- `supplement.tex`, which is already descriptive;
- `feeling-of-ungrammaticality/`, which has no paper entrypoint yet;
- historical submission bundles, review prompts, dated pass reports, and old
  session logs whose references to `main.tex` describe the state at that time.

## Numbered-example rule

Every numbered object-language expression will use `\mention{}`. This includes
the surface line introduced by `\gll` in an interlinear glossed example.

Implementation details:

- Ordinary numbered utterances remain or become `\mention{...}`.
- Judgment macros remain outside the mention, as in
  `\ungram{\mention{...}}`.
- Speaker labels, citations, adaptation notes, and explanatory instructions
  remain roman outside the mention.
- In `\gll` lines, each aligned surface token will use its own `\mention{}` so
  the gloss package can still align tokens word by word. Gloss lines and free
  translations remain roman.
- Existing `\olang{}` in running prose remains unchanged; the rule is specific
  to numbered examples.

The root and asterisk papers already satisfy most of this rule. The required
edits are concentrated in the root paper's French, Turkish, Spanish-English,
Japanese, Rioplatense Spanish, and Turkish-harmony examples. The operator paper's
numbered switch-reference forms already use `\mention{}`. The etiological paper
currently has no numbered examples.

To make the correction durable, update the central house-style guide's numbered
and glossed examples from raw `\textit{}`/unmarked surface text to
`\mention{}` and state the rule explicitly.

## Dependency updates

Update current operational references, not historical provenance:

- root `AGENTS.md`, `README.md`, `CLAUDE.md`, and the current-source/current-build
  portions of `STATUS.md`;
- each affected subproject's current build instructions and current status
  summary;
- the root pass ledger by pinning `grammaticality-de-idealized.tex` as the
  manuscript root while preserving old pass events that correctly record
  `main.tex`;
- a dated decision entry recording the four-entrypoint rename and the
  numbered-example convention.

The tracked root `main.xdv` is an obsolete build intermediate. Remove it from
version control and do not add a renamed `.xdv`; XeLaTeX can regenerate the
intermediate locally. Ignored auxiliary files with the old stem can remain local
until ordinary cleanup.

## Dirty-worktree handling

The operator-stratum source, PDF, bibliography, status, and decision log already
contain the completed companion-paper revision. Rename the current files in
place so none of that work is lost. Do not stage or rewrite unrelated notes,
etiological/evolutionary scripts, or archived review materials.

This pass will remain local until an explicit `ship` request. That keeps the
pre-existing operator revision and the repository-wide filename refactor
reviewable before commits are organized.

## Verification

1. Build all four papers from their new source names.
2. Confirm each expected descriptive PDF is produced and has the expected page
   count.
3. Scan all four logs for missing citations/references, missing files, TeX
   errors, missing glyphs, and overfull boxes.
4. Run the house-style checker on all four renamed sources.
5. Search live operational files for stale `main.tex`, `main.pdf`, `biber main`,
   and `latexmk main.tex` references.
6. Confirm frozen review/submission artifacts remain unchanged.
7. Run `git diff --check` and inspect rename detection and the dirty-worktree
   boundary before handing the result back.

## Stop conditions

Pause rather than improvise if a renamed entrypoint changes bibliography
resolution, if a subproject build depends on its old job name, or if Git cannot
preserve the existing operator-stratum edits cleanly across the rename.
