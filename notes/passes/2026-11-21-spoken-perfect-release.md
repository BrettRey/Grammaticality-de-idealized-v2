# English perfect manuscript release checks

The checked release applies the approved English perfect revision to the manuscript at Git commit `3ca61c8`. A clean build of the pinned root and its included reader section produced 28 pages using XeLaTeX and Biber. All includes and the shared bibliography resolved. The log contained the existing font substitution and microtype footnote warning. There were no undefined citations or references, missing characters, or overfull boxes. The PDF text locates the conditional diagnosis on pages 2, 9 and 12 and the spoken example on page 17.

The house-style check covered both source files. The flagged underscore on line 913 belongs to a citation key. The other scanner warnings concern recurring paragraph openings outside the revision. The source uses semantic macros for the new English examples. The visible and metadata keywords agree, and the bibliography begins after a page break. The diagnostic table now states the reading to which the conflict applies.

## Scanner output

```text
SENTENCE LENGTH
============================================================

  --- grammaticality-de-idealized.tex ---
    353 sentences | median 17 | mean 17.6 | middle half 11-23 (12 words)
         1-9  ###################        67   19%
       10-14  #####################      74   21%
       15-19  ########################   84   24%
       20-24  ################           57   16%
       25-29  ###########                39   11%
       30-34  #####                      16    5%
       35-39  ###                         9    3%
         40+  ##                          7    2%

  --- reader-model-and-dynamics.tex ---
    218 sentences | median 14 | mean 15.4 | middle half 11-19 (8 words)
         1-9  #################          46   21%
       10-14  ########################   65   30%
       15-19  ####################       54   25%
       20-24  #############              34   16%
       25-29  ####                       10    5%
       30-34  ###                         7    3%
       35-39                              1    0%
         40+                              1    0%
    [advisory] 63% of sentences fall in 12-26 words; the band is narrow, so check whether the rhythm has flattened
```
