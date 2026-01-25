I have reviewed the document for inconsistencies between the semantic macros defined in your preamble and the ad-hoc formatting used in the body. Below are the identified issues where house style macros should be applied:

### Semantic Markup Inconsistencies

| Line | Current Code | Suggested Correction | Reasoning |
| :--- | :--- | :--- | :--- |
| 183 | `\textit{She texted him the address}` | `\mention{She texted him the address}` | Linguistic mention of a string. |
| 226 | `fMRI` | `\abbr{fmri}` | Uses `\textsc` via `\abbr` for consistency with other abbreviations. |
| 245 | `\textit{Ava cookie.}` | `\mention{Ava cookie.}` | Child language example (mention). |
| 250 | `\textit{I might could help you with that.}` | `\mention{I might could help you with that.}` | Dialectal example (mention). |
| 279 | `\textit{Spiro conjectures Ex-Lax}` | `\mention{Spiro conjectures Ex-Lax}` | Sentential example (mention). |
| 303 | `\textit{Elle étudie maintenant.}` | `\olang{Elle étudie maintenant.}` | French language string (other language). |
| 333 | `\textit{I've finished it yesterday.}` | `\mention{I've finished it yesterday.}` | Ungrammatical example (mention). |
| 635 | `\textit{The old man the boats.}` | `\mention{The old man the boats.}` | Garden-path example (mention). |
| 671 | `\textit{I am going to London.}` | `\mention{I am going to London.}` | Historical example (mention). |
| 944 | `\textit{I have 16 dollars}` | `\mention{I have 16 dollars}` | Comparison example (mention). |
| 1060 | `\textit{Whose is that?}` | `\mention{Whose is that?}` | Interrogative example (mention). |

### Notes on Global Macro Usage
*   **Abbreviations:** Terms like `fMRI`, `LBE`, and `ERP` appear frequently in plain text. For a consistent "old style" look in the document (matching the Garamond numbers), these should ideally be wrapped in `\abbr{}` to trigger the small-caps formatting defined in your preamble.
*   **Foreign Languages:** Several instances of Spanish (`vos`, `tú`) correctly use `\olang`, but full-sentence examples in the text (like the French in line 303) often revert to `\textit`.
*   **Judgement Markers:** In section 3.8 (lines 782-795), several ungrammatical strings are listed without any markup (e.g., `*Can the have running`). These should be wrapped in `\ungram{\mention{...}}` for consistency with the rest of the paper.
