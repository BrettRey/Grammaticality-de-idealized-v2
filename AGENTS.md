# Repository Guidelines

## Project Structure & Module Organization
- Root contains LaTeX sources (`main.tex`, `main-old.tex`, topic-focused sections like `OldSection2.tex`, `LingbuzzPreprint.tex`, `Bourdieu.tex`, `ERP.tex`) plus shared references in `refs.bib`.
- Supporting assets live beside sources (e.g., `cgisf.pdf`, `trident.jpg`); keep new figures in the repository root unless a dedicated `figures/` folder is created.
- Analytical prototype lives in `validate_entrenchment_measurement.py` for factor-analysis simulations; no package layout is used.

## Build, Test, and Development Commands
- Build primary paper PDF: `latexmk -pdf main.tex` (reruns as needed; stops on errors). Clean aux files: `latexmk -c`.
- One-off compilation: `pdflatex main.tex` (use twice if bibliography not needed).
- Run the simulation script: `python3 validate_entrenchment_measurement.py` (requires NumPy, pandas, scikit-learn, SciPy, matplotlib).

## Coding Style & Naming Conventions
- LaTeX: prefer semantic macros and `\cite{key}` over manual formatting; keep section file names descriptive and lower-case with hyphens if new files are added.
- Formatting: indent LaTeX environments by two spaces for readability; keep lines reasonably short (~100 chars).
- Bibliography keys: use `authorYearTopic` (e.g., `smith2020gradient`) and store all entries in `refs.bib`.
- Python: PEP 8 defaults; meaningful variable names; keep scripts executable via `python3 file.py`.

## Testing Guidelines
- For LaTeX, ensure `latexmk -pdf main.tex` completes without errors; scan the log for undefined references or missing figures.
- For the simulation, confirm `python3 validate_entrenchment_measurement.py` runs cleanly and reports RMSE/Correlation; update dependencies in comments if you add imports.
- No formal unit tests exist; if you add analysis code, include a minimal reproducible example or sanity checks in the script.

## Commit & Pull Request Guidelines
- Commits: use concise, imperative messages (e.g., `Add exposure analysis section`, `Refine factor analysis script`); group related changes.
- Pull requests: summarize scope, list build/test results (`latexmk`, simulation run), and note any new assets or bibliographic updates. Include screenshots of key figures if visuals change.

## Security & Configuration Tips
- Avoid committing generated PDFs except for canonical releases; rely on sources plus assets.
- Keep third-party data or proprietary stimuli out of the repo; link to external sources instead.
- If TeX Live packages are required beyond defaults, note them in the PR description so others can install as needed.
