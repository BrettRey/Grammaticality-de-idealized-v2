# House-style audit

Date: 2026-08-22  
Scope: whole manuscript (`main.tex` and included `section3.tex`)  
Status: applied and verified

The mechanical pass normalized citation commands to the house-standard
`\citep`, put `\clearpage` immediately before the bibliography, removed the
remaining avoidable connective and auxiliary-form flags in the revised formal
section, and confirmed that the source contains no Unicode em dashes,
triple-hyphen em dashes, hard-coded TeX Live paths, or `\parencite` commands.
The keyword list is visible in the manuscript and matches the PDF metadata; the
bibliography path remains the required symlink to the central bibliography.

The final linter reports 60 potential flags. They were inspected rather than
accepted mechanically. The residuals are mathematical underscores misread as
prose subscripts, raw `\textit` used inside interlinear examples or for
mention-level foreign material, two precise procedural uses of *must*, two
substring false positives for auxiliary contractions, and advisory paragraph
cadence counts. The AI-voice advisories likewise concern technical terms such as
*pivotal* and *robust*, meaningful uses of *actually* or *genuinely*, and two
lists incorrectly classified as false ranges. None calls for a source change.

## Sentence distribution

- `main.tex`: 927 sentences; median 18 words; mean 19.9; middle half 12--26.
- `section3.tex`: 280 sentences; median 18 words; mean 19.4; middle half 11--26.

The distribution is broad, with 18--20% short sentences and 4--6% sentences of
40 words or more; the checker issued no distribution advisory.
