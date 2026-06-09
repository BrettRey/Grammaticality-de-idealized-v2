# Forty-Third Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** Claude and GPT Pro both identified projection as the main unfunded leg.
**Change type:** Methodological decision and empirical-lane scaffold; no graph mutation, no score
movement.

## What Changed

Recorded the decision that the first empirical vertical slice should be `AGR` tested with COCA.

Added:

- `notes/agreement-coca-projection-protocol-2026-06-09.md`;
- `data/agr-coca-projection/README.md`;
- `data/agr-coca-projection/query-plan.csv`;
- `data/agr-coca-projection/kwic-coding-schema.csv`;
- `data/agr-coca-projection/prediction-register.csv`.

A follow-on implementation added `scripts/run_agr_coca_queries.py`, which expands the query plan
into auditable English-Corpora.org wrapper calls and refuses live execution if the COCA session is
not authenticated.

## Rationale

The workbench already has a scoped agreement module, and the prior Linguistic Transparency paper
has a relevant COCA pilot on number-transparent quantified NPs. That pilot is useful but mostly
supporting evidence around known CGEL categories.

The workbench can improve on it by making the next pass confirmatory:

- known central cases calibrate query and KWIC coding;
- boundary cases are registered before inspection;
- counts are interpreted against opportunity denominators;
- KWIC exclusions are reproducible;
- uncertainty and zero-cell upper bounds are reported.

## Result

No candidate changes. `AGR` remains a scoped module with all numeric scores at zero.

The next agreement move is now concrete: run the COCA protocol and test whether notional basis,
controller identification, and override pattern predict filtered agreement realization better than
surface-head number alone.

## Boundary

COCA is not being treated as a grammaticality oracle. It is a measurement source for production,
attestation, agreement-realization, and opportunity-denominator claims. Licensing or grammaticality
attribution still requires the graph's construct discipline and, where needed, judgment or repair
data.
