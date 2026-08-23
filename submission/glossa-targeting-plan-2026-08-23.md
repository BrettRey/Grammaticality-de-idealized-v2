# Glossa targeting plan for _Grammaticality de-idealized_
## Outcome
Prepare the paper as a _Glossa_ Research Article without reopening its settled reader-facing architecture. The target version should remain a mathematics-free, self-contained model paper whose formal supplement establishes model-internal results and whose empirical claims remain explicitly conditional.

The main venue move is packaging and selective relocation, not another general rewrite. The first objective is a main PDF at or below **12,600 words by a documented PDF-based count**, leaving headroom below the 13,000-word initial-submission limit.
## Fixed points
- Keep the current title.

- Keep the current abstract unless a hard policy or accuracy defect is found. It is already reader-first and is about 235 words, within the 250-word limit but with little spare capacity.

- Keep mathematics out of the main paper.

- Keep _projectibility_ as a core theoretical term and, presumptively, as a keyword.

- Keep the distinctions among licensing, evidence, subjective response, processing, and population dynamics.

- Keep the Turkish borrowing-to-internalization pathway, even if the appendix moves to a separate supplementary file.

- Describe simulations, Lean, and corpus work at their actual evidential level. In particular, the BNC2014 dative passage describes a rescore that **can be done**; it is not an executed result.

## Evidence used to design the move
The plan combines four independent audits: a journal-framing pass, a line-level cut map, a submission-package audit, and a Fable review, with final adjudication by Codex. Ox Alpha subsequently reviewed this exact plan. Its useful procedural suggestions were adopted; its policy claims were checked against the live primary pages before use. The plan also uses Brett Reynolds's prior _Glossa_ outcome for manuscript 27281 as direct venue evidence.

That 2026 rejection supplies the most important editing constraint. The reviewers found the empirical contrast promising but judged the squib too compressed: key notions entered too late, premise-to-conclusion links were underdeveloped, judgments lacked enough contextual grounding, and the adjacent syntax/semantics literature was too thin. For the present paper, therefore:

- cut duplicated framing before cutting definitions or inferential bridges;

- relocate optional technical designs before shortening the central account;

- preserve the provenance and interpretation of linguistic examples;

- add only literature that sharpens a live distinction in the paper; and

- do not present terseness itself as a virtue.

## Assumptions and failure tests
1. **Separate supplements create legitimate headroom.** The live _Glossa_ guidance caps the initial article at 13,000 words including citations and references and describes appendices as separately hosted supplementary material. The submission checklist also refers to an appendix not counted toward the maximum, but does not clearly authorize treating an appendix embedded in the main PDF that way. We will therefore count everything physically present in the main PDF and state separately what the journal excludes. If the journal confirms a different counting method, use the stricter reproducible method rather than cutting on an assumption.

2. **Relocation can preserve self-containment.** The main paper already contains the theory and multiple worked contrasts. The Turkish appendix and the full regression-discontinuity design deepen the account but are not premises without which it cannot be assessed. If a cold-reader check finds otherwise, restore the necessary explanation to the main text.

3. **Current venue literature can sharpen rather than decorate.** A citation is added only if reading the full source identifies a precise proposition it supports, qualifies, or contrasts with. Venue-local citation clustering is forbidden.

4. **The model paper has completed results, but not completed population validation.** Model-internal simulations, coherence checks, formal structural checks, and the reported corpus probes may be described as completed only where they were actually run. Proposed rescoring, longitudinal validation, and participant studies stay prospective.

5. **An anonymous package can be generated without creating a second manuscript.** Canonical source remains the source of truth. If source files must be uploaded, a scrubbed staging copy is generated and inspected; merely hiding identifying material behind an inactive TeX conditional is not sufficient.

## Moves, in order
### 1. Establish the count and evidence ledger
- Record three baseline counts: `texcount -inc`, extracted main-PDF text through the references, and the declared submission count.

- Use the PDF-based count as the safety gate because it includes rendered references.

- Make a short table of every empirical or formal result named in the main paper: **executed**, **illustrative/model-internal**, **proposed**, or **externally sourced**. Use it to prevent prospective work from becoming a submission-facing “result.”

- Treat the current approximately 13,474-word PDF extraction as the conservative baseline until a single reproducible submission count is fixed.

### 2. Create headroom by relocation before compression
1. Move the Turkish vowel-harmony appendix, intact, to a publishable `supplement-turkish-vowel-harmony` file. Retain the borrowing, narrow situational licensing, and later lexical internalization pathway. Leave a concise pointer in the main paper.

2. Move the full regression-discontinuity design and its figure from the methodological section to the formal/methodological supplement. Retain in the main paper one sentence stating the decision-layer discriminator and what a smooth result would weaken.

3. Rebuild and recount. The expected relocation is roughly 800–1,000 rendered words, which may already put the main PDF near 12,500–12,700 under the conservative all-content count. Record both that count and the journal-rule count rather than treating the safety margin as the policy itself.


Only if the main PDF remains above 12,600 should prose be compressed. Use this order:

1. collapse the repeated Chomsky/logical-behavioural-economics setup while preserving the target distinction and falsifier;

2. combine the two Construction Grammar bridge paragraphs;

3. compress the limitations list without deleting any limitation;

4. shorten the repeated diagnostic criteria where the full rank order already recurs;

5. shorten the four trajectory descriptions while retaining all four labels, conditionality, and their independent evidence requirements;

6. shorten the dative illustration while preserving the both-licensed control, selection/licensing distinction, opportunity denominator, transport caution, and the prospective status of the BNC2014 rescore.


Do **not** make early cuts to the reader-profile table, the logicality or relevance sections, judgment grounding, definitions of earned terms, or the links between the status model and its predictions. Those are precisely the kinds of omissions the prior _Glossa_ reviews penalized.
### 3. Make a narrow Glossa-facing literature bridge
Read the full papers before editing and add them only at the point of argumentative contact:

- [Christensen and Nyvad (2024)](https://doi.org/10.16995/glossa.10618): use to motivate separating structural complexity, frequency, and acceptability, not as validation of OVMG.

- [Franjieh et al. (2025)](https://doi.org/10.16995/glossa.16601): use as a cross-sectional case of conventional fixation and redundant classification, not as longitudinal proof of the paper's adoption/retention dynamics.

- [Nogueira Sánchez (2025)](https://doi.org/10.16995/glossa.20004): optional, if it can replace generic prose in the dative/optionality discussion by sharpening the distinction between availability and preference.


Wall et al. is not needed in the minimal pass. Do not cite the editorial merely to signal venue fit. Do not batch the new citations in one conspicuous “recent _Glossa_ work” paragraph.

One conclusion sentence should be checked for evidence status. The present claim that “the population dynamics establish the possibility” should say clearly that the possibility is established **within the model under the stated adoption and retention conditions**. No abstract change is required for this.
### 4. Align the front and back matter with the live submission rules
- Reduce the seven keywords to six. Preserve _projectibility_; the presumptive deletion is the broadest, least discriminating label, _usage-based grammar_, subject to a final discoverability check.

- Put the word count below the anonymous title in the review PDF.

- Ensure page numbers are visible.

- Add the required Competing Interests statement.

- Add an Abbreviations list because supplementary interlinear examples use glosses.

- Resolve the COCA and other corpus-redistribution questions before drafting the Data Availability/Supplementary Files statement. Then name each uploaded file and accurately distinguish redistributable derived data from restricted corpus snippets.

- Audit the actual AI provenance before finalizing the AI Declaration. Give tools and developers, relevant model/version or date where knowable, task scope, human checking, limitations, and authorial responsibility. Do not describe model assistance more broadly or more narrowly than the record supports.

- Add Funding and Ethics statements only if applicable. The live author guidelines say that Competing Interests is universally mandatory and Ethics is required for relevant human-participant research; do not invent an ethics-review claim for this model paper.

- Keep self-citations in ordinary third-person form, as _Glossa_ instructs; do not use “Author.”

- Add all available reference DOIs, but avoid a blanket bibliography setting that hides URLs needed for web-only or preprint sources.

### 5. Build a clean anonymous review package
Initial reviewer-facing files should be:

1. one anonymous main PDF with all main-text figures and tables embedded;

2. one anonymous formal/methodological supplement PDF;

3. one anonymous Turkish vowel-harmony supplement PDF; and

4. one minimal reproducibility archive or anonymous hosted view containing only the exact code, inputs, permitted derived data, outputs, Lean source/toolchain, manifest, and hashes needed to reproduce reported checks.


Package rules:

- Remove author, affiliation, email, ORCID, acknowledgements, identifying funding language, identifying PDF metadata, the commented ChatGPT share URL, GitHub handle, home-directory paths, and identifying embedded links from review files and uploaded sources.

- A public LingBuzz preprint is permitted but limits anonymity; disclose that fact in the cover letter rather than pretending anonymity is complete.

- Do not expose the identifying `BrettRey` GitHub remote. Prefer direct Janeway-hosted files or a genuinely anonymous repository view.

- Do not upload the central bibliography symlink. Generate a minimal bibliography containing only cited entries.

- Fix the supplement's cross-document target: `\externaldocument[M-]{main}` must point to the canonical main build, not the stale older `main.aux`. Build the canonical main first, then the supplement.

- Exclude repository history, review/model logs, planning files, status files, old PDFs, caches, unrelated subprojects, secrets, and local provenance bundles.

- Resolve COCA redistribution before upload. If verbatim KWIC material cannot be redistributed, supply query specifications, coding schema, derived counts, and scripts, and state the restriction and requested exception accurately.

### 6. Verify before writing the cover letter
Required checks:

- main PDF no more than 12,600 words by the documented method;

- abstract no more than 250 words and unchanged in substance;

- no more than six keywords;

- clean `latexmk` builds of main and both supplements, in dependency order;

- no undefined citations or references and all cross-document numbers current;

- no identity leaks in PDF metadata, rendered prose outside normal self-citations, filenames, archive contents, comments, or links;

- all archives open without absolute local paths;

- all released code and Lean files replay independently against the declared versions and reproduce the reported hashes/results;

- every main figure and table is embedded, numbered, cited, and legible;

- a bounded style, bibliography, and proofreading audit passes; and

- a cold-reader regression check confirms that every earned term, central inference, example judgment, and falsifier still has enough local support after relocation.


The cold-reader check is the explicit safeguard supplied by the prior _Glossa_ rejection. Codex will give the **main PDF only** to two fresh-context readers: one general-linguistics reader and one methods/evidence reader. Each must list (i) terms used before they are locally earned, (ii) judgments whose interpretation or context is not grounded, (iii) premise-to-conclusion links that require opening a supplement, and (iv) falsifiers whose target is unclear. Zero material entries passes. Any material entry restores or rewrites the needed main-text bridge; it does not trigger further compression. The separately submitted supplements receive their own continuity check, because they are reviewer-facing rather than archival dumping grounds.
### 7. Submit with an evidence-accurate cover letter
The cover letter should be short and concrete:

- identify the submission as a Research Article;

- state the general-linguistics problem and the paper's situation-indexed alternative;

- distinguish completed model-internal results from proposed empirical validation;

- note the formal and reproducibility supplements;

- disclose the LingBuzz preprint and its effect on anonymity;

- identify the AI Declaration and any corpus-data restriction/exception;

- confirm originality, no simultaneous submission of this manuscript, and no new participant study if accurate; and

- describe the companion operator paper only at its true status on the submission date. A presubmission query elsewhere is neither a simultaneous submission nor a completed companion article.


Do not add a prediction-ledger event until the final submission is made. Save a copy of every portal field and download-check every uploaded file before clicking submit.
## Explicitly rejected moves
- changing the title or reader-first abstract without a hard defect;

- removing _projectibility_ to influence reviewer selection;

- calling the proposed BNC2014 rescore an executed result;

- presenting corpus examples as validation of population licensing;

- deleting logicality, relevance, or judgment-grounding material merely to save words;

- adding a cluster of venue-local citations for signalling purposes;

- converting to the _Glossa_ production template before acceptance unless requested;

- hiding all bibliography URLs;

- uploading canonical source that still contains identity in inactive branches; or

- creating a public repository record or DOI before the anonymous package is scrubbed.

## Completion rule
The targeting pass is complete when the verified anonymous package satisfies the live rules, the main paper is at or below the safety count, the evidence ledger contains no status inflation, and the cold-reader check finds no inference or judgment left unsupported. At that point, stop broad revision and submit.
## Sources and local evidence
- [Glossa author guidelines](https://www.glossa-journal.org/site/author-guidelines/)

- [Glossa submission checklist](https://www.glossa-journal.org/submissions/)

- [Glossa journal policies](https://www.glossa-journal.org/site/journal-policies/)

- [Open Library of Humanities AI policy](https://www.openlibhums.org/site/ai-policy/)

- [English-Corpora terms of use](https://www.english-corpora.org/licenses-termsOfUse.asp)

- `submission/venue-decision-2026-08-23.md`

- `papers/parked/focus-modifiers-interrogative-heads/STATUS.md`

- `papers/parked/focus-modifiers-interrogative-heads/correspondence/glossa-reviews-2026-07-07.md`

---
comments:
  c1:
    body: this all seems sensible to me. Pass if by Ox Alpha if you haven't already
      and then proceed as you see fit
    by: user
    at: 2026-08-23T15:10:21.310Z
  c2:
    body: Ox Alpha returned REVISE, then GO. I adopted its executable cold-reader
      rubric and earlier COCA-licensing gate. I rejected its claims that Ethics is
      universally mandatory and that the count belongs at the end because the live
      Glossa author guidelines say Ethics is conditional and the count goes under the
      title. I also retained the conservative rule of counting everything physically
      in the main PDF because the live guidance describes appendices as separately
      hosted.
    by: Codex
    at: 2026-08-23T15:14:42.000Z
    re: c1
