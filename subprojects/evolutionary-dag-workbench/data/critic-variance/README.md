# Critic Verdict Variance

This directory stores packets, critic outputs, and summaries for repeated independent critique of
one target evaluation.

## Files

- `packets/`: prompt packets produced by `scripts/build_critic_variance_packet.py`.
- `runs/`: JSON outputs from critic passes.
- `summaries/`: CSV summaries produced by `scripts/summarize_critic_variance.py`.
- `critic-output.schema.json`: JSON Schema for structured critic output.

## Registered First Target

The first registered target is:

`evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json`

Build its packet with:

```bash
python3 scripts/build_critic_variance_packet.py \
  evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json \
  --output data/critic-variance/packets/agr-coca-projection-prevariance-critic-packet.md
```

Summarize three or more critic outputs with:

```bash
python3 scripts/summarize_critic_variance.py \
  evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json \
  data/critic-variance/runs/*.json \
  --output data/critic-variance/summaries/agr-coca-projection-variance-summary.csv
```

Do not treat the summary as empirical evidence about grammaticality. It is evidence about the
stability of the evaluation verdict under repeated critique.

One local read-only Codex critic pass can be run with:

```bash
codex exec -C . --ephemeral -s read-only --output-schema data/critic-variance/critic-output.schema.json \
  -o data/critic-variance/runs/agr-coca-projection-codex-run1.json \
  - < data/critic-variance/packets/agr-coca-projection-prevariance-critic-packet.md
```

## First Result

The first three-run check is recorded in
`notes/critic-verdict-variance-agr-coca-2026-06-09.md`. It preserves the AGR card-level
`survives_as_module` result but downgrades `partitive-qn-coca-targeted-kwic` from `passed` to
`mixed`, because the largest positive cell is sample-coded rather than fully filtered.
