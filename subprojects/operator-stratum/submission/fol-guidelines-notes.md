# Functions of Language Submission Notes

Date: 2026-06-02

Status: FoL is the current target. This note records guideline checks and likely
submission-package changes only. No blind version has been prepared.

## Sources Checked

- FoL homepage: <https://benjamins.com/catalog/fol>
- FoL author information page: <https://benjamins.com/catalog/fol/submission>
- Editorial Manager entry point: <https://www.editorialmanager.com/fol/default2.aspx>
- John Benjamins APA manuscript guidelines PDF:
  <https://benjamins.com/downloads/guidelines/jb-guidelines-manuscript-submission-apa.pdf>
- Benjamins ethics/AI guidance is linked from the FoL author information page:
  <https://benjamins.com/content/authors/ethics>
- Benjamins alt-text guidance is referenced in the APA guidelines:
  <https://benjamins.com/content/authors/guidancealttext>

The FoL HTML pages were blocked by Cloudflare from the command line, but the
search index exposed the relevant FoL author-info text. The Benjamins APA
guidelines PDF was directly accessible and extracted locally.

## Fit

FoL is a strong fit for this paper's current argument. The journal presents
itself as a venue for functionalist linguistics, including prosodic phenomena,
the clause in communicative context, conversation and discourse regularities,
and interaction between levels of analysis. That matches the paper's strongest
version: grammaticality judgments target public-update operators across
clause structure, prosody, interaction, typology, and social accountability.

The FoL version should foreground functional, interactional, and discourse-
contextual stakes. It does not need a new theoretical rebuild.

## FoL Submission Route

- Submit through Editorial Manager.
- Consult FoL's 9-point checklist before submission.
- Consult the FoL style sheet and the Short Guide to EM for Authors before
  package preparation.
- FoL says manuscripts that do not conform to the style sheet will not be
  considered.
- FoL requires anonymisation for review.
- FoL says submissions must not be published in a widely available form and
  must not be under review elsewhere.

## Required or Likely Changes

1. Abstract. The current abstract is about 225 words. Benjamins' APA guidelines
   set a maximum of 120 words. This is the largest immediate mismatch. The FoL
   abstract should be self-contained, active-voice, and centred on public-update
   operators, grammaticality judgments, clause structure, typology, and
   interaction.

2. Keywords. Benjamins allows up to 10 comma-separated keywords. The current
   keyword list is within the limit. For FoL, consider keeping the list but
   making the functional/discourse framing more visible, for example with
   `functionalist linguistics`, `discourse pragmatics`, or `interaction`.

3. Running head. The title is long, so Benjamins asks for a short running head
   of at most 55 characters on the title page. Candidate: `Public-update
   operators and grammaticality`.

4. English variety. Benjamins permits either British or American English if used
   consistently. This manuscript should stay in Oxford/British spelling.

5. Blind review. The later blind version will need to remove or mask the author
   line, ORCID, affiliation, acknowledgements, AI disclosure, and any
   self-identifying references or status language. Do not do this yet.

6. AI declaration. The current acknowledgements name Claude Opus 4.5 and
   ChatGPT 5.2 Pro as drafting/editing aids. For submission, follow Benjamins'
   AI declaration guidance. The declaration may belong in the submission system
   or cover materials during blind review rather than in the anonymised
   manuscript.

7. Formatting. Benjamins' production guidelines prefer 12-point Times New
   Roman, double spacing, and minimal formatting. The current LaTeX PDF is
   readable but not in that house layout. Before submission, check whether FoL
   accepts a PDF/LaTeX manuscript package through EM or expects Word-preferred
   formatting.

8. PDF/fonts. Benjamins asks for a PDF with embedded fonts and correct special
   characters at production stage. Verify this before final package upload.

9. Quotations and cited forms. Benjamins uses double quotation marks for text
   quotations and terms, and single quotation marks for translations of cited
   forms. The current LaTeX quotation system likely renders correctly, but the
   example/translations pass should check this explicitly.

10. Examples and glosses. Benjamins wants linguistic examples numbered with
    Arabic numerals in parentheses and indented; glosses should follow Leipzig
    conventions and be aligned if alignment matters. The current paper mostly
    uses inline examples and tables. If any typological examples are expanded,
    convert them to compliant numbered examples.

11. Notes. Benjamins asks authors to keep notes to a minimum and place note
    indicators after punctuation. The manuscript has a number of footnotes.
    Review whether any should be folded into the text before submission.

12. Tables and figures. Tables and figures should be numbered, captioned
    concisely, and referenced in the text without relative phrases like "below".
    The current diagnostic table is already numbered and captioned. If figures
    or images are added, provide alt text following Benjamins guidance.

13. References. Benjamins specifies APA style, all and only cited works in the
    reference list, precise page references where needed, and DOI inclusion
    where available. The current `biblatex-apa` setup is close, but run a final
    citation/bibliography audit before submission.

14. First-person and author identity. FoL does not forbid first-person argument,
    but the blind version should avoid self-identifying phrasing. The current
    abstract uses "I argue"; decide later whether to keep first person in the
    unblinded version and neutralise it in the blind version.

15. Dates and status. The current `\date{\today}` is fine for drafts but should
    be removed or normalised in the submission package. Do not include
    submission-status language in the manuscript itself.

## Current Manuscript Flags

- Current abstract: about 225 words, so it must be cut by roughly half.
- Current title: long enough to require a running head.
- Current front matter: contains author, ORCID, affiliation, and date.
- Current acknowledgements: contain a personal origin note plus AI disclosure.
- Current PDF length: 20 pages, which looks reasonable for FoL.
- Current formatting: LaTeX article format, not Benjamins' preferred
  double-spaced Times New Roman production format.
- Current bibliography: should receive a final APA/DOI/all-cited-only pass.

## Next Submission-Prep Pass

When ready to prepare for FoL, make a dedicated blind submission branch or copy,
then:

1. Cut the abstract to 120 words or fewer.
2. Add a running head.
3. Prepare the anonymised title page/manuscript.
4. Move acknowledgements and AI disclosure out of the blind manuscript as needed.
5. Re-check all examples, notes, quotes, tables, and references against
   Benjamins APA style.
6. Build a clean PDF and verify embedded fonts.
7. Confirm the EM upload formats and FoL checklist immediately before
   submission.
