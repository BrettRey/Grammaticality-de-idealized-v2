Here is the analysis of the typography and formatting for `main.tex`:

### Actionable Fixes

**1. Spacing after abbreviations**
LaTeX interprets a period after lowercase letters as the end of a sentence and adds extra space. When `e.g.` or `i.e.` are used mid-sentence without a comma, they need an escaped space (`\ `) or a non-breaking space (`~`).
*   **Fix:** `(e.g. word salad` $\rightarrow$ `(e.g.\ word salad` (Section 4.2)
*   **Fix:** `(e.g. tense` $\rightarrow$ `e.g.\ tense` (Section 4.2)
*   **Fix:** `(e.g. systematic garden-path repair` $\rightarrow$ `e.g.\ systematic garden-path repair` (Section 4.4 & 5.4)

**2. En-dashes for coordinate relationships**
The document generally uses en-dashes (`--`) well for "form--value" and "morphosyntax--phonology", but there are inconsistencies with other coordinate pairs which currently use hyphens.
*   **Fix:** `competence-performance` $\rightarrow$ `competence--performance` (Section 2, para 2) to match the usage in the Conclusion.
*   **Fix:** `morphosyntactic-lexical` $\rightarrow$ `morphosyntactic--lexical` (Section 6.7, para 2) to denote the relationship between the two distinct levels (similar to `phonology--syntax`).

**3. Quotes and Special Characters**
*   **Fix:** In the Appendix (Turkish examples), `intended `s/he laughed'` uses manual backtick/apostrophe. For consistency with the rest of the document, consider using `\enquote{s/he laughed}` or ensuring the `csquotes` package settings are active there.
*   **Suggestion:** `[±back]` and `[±round]` in the Appendix use the Unicode `±` symbol. While `fontspec` likely handles this, using math mode `$[\pm\text{back}]$` or `$\pm$` ensures the symbol is pulled from the correct math font if the main font lacks it.

**4. Section Headings**
*   **Check:** The Introduction is unnumbered (`\section*{Introduction}`), which is standard.
*   **Check:** All other headings follow the requested sentence case correctly (e.g., `\subsection{Diagnostic categories}`).

**5. Math Mode Leakage**
*   **Status:** Clean. The document correctly uses `\(` and `\)` or `$` for inline math (e.g., `\(\beta\approx8\;\text{ms/link}\)`), and text inside math is properly handled with `\text{}`.
