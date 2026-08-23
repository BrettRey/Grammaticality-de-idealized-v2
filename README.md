# Grammaticality de-idealized

This repository is an active research workspace for Brett Reynolds's grammaticality
projects. The canonical root manuscript is `grammaticality-de-idealized.tex`. Other root `.tex` files are
older drafts, exploratory pieces, preprint sources, talks, or side materials unless
explicitly documented otherwise.

The main paper develops a de-idealized account of grammaticality that separates
objective grammatical status from the felt experience of anomaly. Current project
notes describe the model as evolving from MMMG/MVMG terminology toward OVMG
(Operator-Value Model of Grammaticality); archived files may still use older names.

## Repository Map

- `grammaticality-de-idealized.tex`: canonical root manuscript source.
- `grammaticality-de-idealized.pdf`: current rendered root manuscript.
- `refs.bib`: shared bibliography for the root manuscript family.
- `LingbuzzPreprint.tex`: older Lingbuzz preprint source, kept for provenance.
- `subprojects/`: related paper-shaped and exploratory subprojects.
- `notes/`, `STATUS.md`, `DECISIONS.md`, `CLAUDE.md`: working-state and governance notes.
- `simulate_dynamics.py`, `validate_entrenchment_measurement.py`: prototype analysis scripts.

## Build

The root manuscript uses `fontspec`, so build with XeLaTeX. The repository includes
`.latexmkrc`, making this the canonical command:

```bash
latexmk grammaticality-de-idealized.tex
```

For manual diagnosis:

```bash
xelatex grammaticality-de-idealized.tex
biber grammaticality-de-idealized
xelatex grammaticality-de-idealized.tex
xelatex grammaticality-de-idealized.tex
```

Clean generated LaTeX files with:

```bash
latexmk -c
```

The manuscript currently expects EB Garamond, Charis SIL, and Inconsolata to be
available to XeLaTeX.

## Scripts

The analysis scripts are prototypes rather than packaged modules. The main external
Python dependencies used by `validate_entrenchment_measurement.py` are:

- NumPy
- pandas
- scikit-learn
- SciPy
- matplotlib

Run the simulation prototype with:

```bash
python3 validate_entrenchment_measurement.py
```

## Public Status

This is not yet a clean reproducible release. The repository intentionally contains
working notes, older drafts, and subprojects that preserve research history. Treat
`grammaticality-de-idealized.tex` as the canonical root manuscript and check `STATUS.md` plus subproject
status files before making public-state claims.

Generated PDFs and build artifacts are not necessarily canonical release artifacts
unless explicitly identified as such.

## License

Unless otherwise noted, the original paper text, documentation, figures, and research
scripts in this repository are licensed under CC BY 4.0. See `LICENSE`.
