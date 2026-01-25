# HOUSE STYLE AUDIT REPORT
## main.tex — Comprehensive Style Violations Analysis

---

## EXECUTIVE SUMMARY

**File:** `main.tex` (1,367 lines, ~136 KB)  
**Status:** Comprehensive academic paper on grammaticality theory  
**Total Violations Found:** 257 (18.8% of lines)  
**Critical Issues:** 0 (None blocking)  
**Recommended Action:** 2 minor fixes + optional cleanup

---

## VIOLATIONS BY CATEGORY

### I. INDENTATION VIOLATIONS (3-SPACE vs 2-SPACE)

**Severity:** MINOR (stylistic consistency)  
**Count:** 15 instances  
**Location:** Lines 948–963 (enumerate block in "Worked Examples")

#### Affected Lines:
- Line 948: `   \item \textbf{\ungram{\mention{Can the have running}}} (Nonsense):`
- Line 949: `   $\mathsf{map}=0$ because structural analysis fails...`
- Line 950: `   Result: $\widetilde{G} = 0$. Status: Ungrammatical.`
- Line 951: blank line with 3 spaces
- Line 952: `   \item \textbf{*I've finished it yesterday} (Semantic Clash):`
- Line 953: `   $\mathsf{map}=1$ (well-formed syntax), $C_t \approx 1$...`
- Line 954: `   Result: $\widetilde{G} \approx 0$. Status: Ungrammatical.`
- Line 955: blank line with 3 spaces
- Line 956: `   \item \textbf{?friend of whose} (Situationally-Novel):`
- Line 957: `   $\mathsf{map}=1$, $K \approx 1$ (perfectly interpretable)...`
- Line 959: blank line with 3 spaces
- Line 960: `   \item \textbf{*Which did you buy car?} (Stable Gap):`
- Line 961: `   $\mathsf{map}=1$, $K \approx 1$, but $C_t \to 0$...`
- Line 962: `   Result: $\widetilde{G} \approx 0$. Status: Categorically...`
- Line 963: blank line with 3 spaces

#### Suggested Fix:
Replace 3-space indentation with 2-space or 4-space:

```latex
# BEFORE (3 spaces):
\begin{enumerate}
   \item \textbf{...}

# AFTER (2 spaces):
\begin{enumerate}
  \item \textbf{...}

# OR AFTER (4 spaces):
\begin{enumerate}
    \item \textbf{...}
```

---

### II. LINE LENGTH VIOLATIONS (>100 CHARACTERS)

**Severity:** MINOR–MODERATE (readability)  
**Count:** 226 instances throughout document  
**Note:** Flowing prose naturally exceeds 100 chars; severity grades below:

#### EXTREME CASES (>500 chars):
| Line | Chars | Context |
|------|-------|---------|
| 205 | 1020 | Abstract paragraph |
| 225 | 858 | Unacceptability types discussion |
| 253 | 935 | Structural analysis explanation |
| 257 | 780 | Interpretive coherence section |
| 259 | 684 | Value compatibility discussion |

#### MODERATE CASES (100–130 chars):
| Line | Chars | Content |
|------|-------|---------|
| 217 | 106 | Example with label and mention |
| 221 | 104 | Example with \textbf |
| 303 | 118 | Subsubsection heading |
| 311 | 119 | Citation followed by prose |
| 401 | 104 | Value incompatibility description |
| 477 | 128 | Categorical gaps description |
| 489 | 118 | Categorical rejection definition |
| 490 | 119 | Satiation resistance definition |
| 584 | 111 | Subsubsection heading |
| 648 | 124 | Ungrammatical constructions paragraph |
| 698 | 103 | New communicative challenges paragraph |
| 867 | 104 | Equation definition |
| 916 | 101 | Locality component explanation |
| 939 | 106 | Measurement model definition |
| 945 | 121 | Worked examples introduction |
| + 211 additional violations at 100–130 chars |

#### Suggested Action:
**Recommendation: LEAVE AS-IS** (acceptable for academic prose)

Flowing paragraphs naturally exceed 100 chars and are standard in thesis/paper writing. Breaking would harm readability. Only consider breaking:
- Structural/heading lines (Lines 303, 311, 584)
- Equation/formula lines (Lines 867, 939)

Example break (if desired):
```latex
# BEFORE:
\subsubsection{Morphosyntactic form--value relations within communicative situations}

# AFTER:
\subsubsection{Morphosyntactic form--value relations within%
  communicative situations}
```

---

### III. TRAILING WHITESPACE

**Severity:** MINOR (hygiene/formatting)  
**Count:** 16 instances  
**Locations:** Scattered throughout

#### Affected Lines:
- Line 94: 3 trailing spaces after `citecolor=linkmaroon,`
- Line 104: 1 trailing space after `\usepackage[style=american]{csquotes}`
- Line 219: 1 trailing space after `\label{ex:whose}`
- Line 463: 1 trailing space after long paragraph
- Lines 948–963: Variable trailing spaces in enumerate block
- Line 1120: 1 trailing space after "contributions"

#### Suggested Fix (Automated):

**Using sed (macOS/Linux):**
```bash
sed -i '' 's/[[:space:]]*$//' main.tex
```

**Using VS Code:**
Select All → Cmd+K Cmd+X (Trim Trailing Whitespace)

**Using Vim/Neovim:**
```vim
:%s/\s\+$//e
```

**Using find/replace (regex):**
Find: `\s+$`  
Replace: (empty)

---

## COMPLIANCE ASSESSMENT

### ✓ STRONG COMPLIANCE (House Style Rules Met):

1. **Semantic Macros:** Correctly uses `\ipa`, `\term`, `\mention`, `\posscite`, `\ungram`, `\marg`, `\odd`
2. **Bibliography Keys:** Follow `authorYearTopic` convention:
   - `chosky1957`, `goldberg1995constructions`, `bybee2006`
   - `lakoff1971`, `mccawley1968`, `hankamer1973whose`
   - `wiese2023`, `grodnerGibson2005`, etc.
3. **Mathematical Notation:** Proper use of `\mathsf`, `\widetilde`, `\scshape`, `\textsc`
4. **Linguistic Examples:** Correct use of `\ea`, `\ex`, `\gll`, `\glt`, `\z`
5. **Formatting:** Good use of `\textit` for mentions, `\textbf` for emphasis, `\olang` for non-English

### ⚠ MINOR NON-COMPLIANCE:

1. **Indentation:** 15 lines use 3-space instead of 2- or 4-space
2. **Trailing Whitespace:** 16 lines have trailing spaces/tabs
3. **Line Length:** 226 instances exceed 100 chars (mostly acceptable; prose-specific)

---

## PRIORITY ACTION PLAN

### PRIORITY 1: File Hygiene (Recommended)
- **Task:** Strip trailing whitespace (16 instances)
- **Time Cost:** 5 minutes (automated)
- **Benefit:** Cleaner version control diffs
- **Command:** `sed -i '' 's/[[:space:]]*$//' main.tex`

### PRIORITY 2: Indentation Consistency (Optional)
- **Task:** Fix 3-space indentation in enumerate block (Lines 948–963, ~15 lines)
- **Time Cost:** 10 minutes (manual or find-replace)
- **Benefit:** Stylistic consistency with rest of document
- **Change:** Replace `   ` (3 spaces) with `  ` (2 spaces) or `    ` (4 spaces)

### PRIORITY 3: Line Length (Low Priority)
- **Task:** Break long prose lines (226 instances)
- **Time Cost:** 30–60 minutes
- **Benefit:** Marginal readability improvement
- **Recommendation:** **SKIP** — not necessary for academic paper
- **Note:** Only consider for publication/archival purposes

---

## SUMMARY STATISTICS

| Metric | Count | Percentage |
|--------|-------|-----------|
| Total Lines | 1,367 | 100% |
| Compliant Lines | 1,110 | 81.2% |
| Lines with Violations | 257 | 18.8% |
| — Indentation Issues | 15 | 1.1% |
| — Line Length Violations | 226 | 16.5% |
| — Trailing Whitespace | 16 | 1.2% |
| **Critical Issues** | **0** | **0%** |
| **Blocking Issues** | **0** | **0%** |

---

## CONCLUSION

**Overall Status:** Excellent compliance with house style guidelines

The document shows strong adherence to semantic markup, bibliography conventions, and LaTeX best practices. The three identified violation categories are:

1. **Indentation (15 lines)** — easily fixed, isolated to one block
2. **Line Length (226 lines)** — mostly acceptable for prose; not a blocking issue
3. **Trailing Whitespace (16 lines)** — easily automated

**Recommendation:** Apply Priority 1 (trailing whitespace cleanup) and Priority 2 (indentation fix) before final submission. Priority 3 is optional.

---

**Audit Date:** January 24, 2026  
**Auditor:** GitHub Copilot CLI  
**Guideline Reference:** Repository guidelines (README.md style section)
