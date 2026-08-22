# Bibliography-integrity audit

Date: 2026-08-22  
Scope: `main.tex`, included `section3.tex`, and `refs.bib`  
Status: verified with one shared-data warning

`biber --validate-datamodel main` resolved all 119 citekeys used in the compiled
document. The build reports no undefined citations, and `refs.bib` is the
expected symlink to `../../../.house-style/references.bib`.

One central-bibliography data-model warning remains:
`CuneoGoldberg2022Islands` is typed as `article` but contains the field
`organization`, which isn't valid for that entry type. This doesn't prevent
resolution or rendering. The bibliography is shared across the portfolio, so
entries unused by this one manuscript aren't evidence of a local integrity
problem and weren't removed.
