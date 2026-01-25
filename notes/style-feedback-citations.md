# Bibliography and Citation Report

## 1. Citation Command Usage
The document generally follows `biblatex-apa` standards using `\autocite` and `\textcite`. However, there are a few inconsistencies where raw `\cite` or manual formatting is used.

**Issues Found:**
*   **Section 3.3.1**: `(FOK; \cite{hart1965})`
    *   **Recommendation**: Use `\autocite[FOK;][]{hart1965}` to generate `(FOK; Hart, 1965)` and avoid nested parentheses or incorrect formatting.
*   **Section 3.3.3**: `(modified from \cite{corbett2016})`
    *   **Recommendation**: Use `\autocite[modified from][]{corbett2016}` to generate `(modified from Corbett, 2016)` or `\parencite[modified from][]{corbett2016}`.
*   **Section 3.1.1**: "As Toribio (2001) reports..."
    *   **Issue**: "Toribio (2001)" is hardcoded text. The actual citation `\autocite{Toribio2001}` appears later inside the example block.
    *   **Recommendation**: Change to `As \textcite{Toribio2001} reports...` to link the name to the bibliography.

## 2. Citation Keys
Citation keys appear largely consistent (format `authorYEAR` or `authorYEARword`), though capitalization varies (e.g., `goldberg` vs `Goldberg`). `biblatex` is case-sensitive regarding keys matching the `.bib` file, so ensure `refs.bib` matches these exactly.

## 3. Formatting of Page Numbers
Page numbers are formatted correctly using the optional argument (e.g., `\textcite[71]{schutze2016}`), which `biblatex` handles automatically (inserting "p." or "pp.").

## 4. Missing Citations
*   **Author (in prep.)**: Placeholder found in Section 2. Ensure this is updated or confirmed before final compilation.
*   **Scott-Phillips (personal communication)**: Correctly handled in text without a bibliography entry.

## Summary of Action Items
1.  Replace `\cite{hart1965}` with `\autocite[FOK;][]{hart1965}`.
2.  Replace `\cite{corbett2016}` with `\autocite[modified from][]{corbett2016}`.
3.  Replace "Toribio (2001)" with `\textcite{Toribio2001}`.
