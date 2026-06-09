# Module Compression Data

This directory stores generated summaries for merge/kill and compression checks over scoped graph
modules.

## Files

- `authorizing-load-bearing.csv`: distinctive-node audit for scoped modules. Generated with:

```bash
python3 scripts/audit_authorizing_load_bearing.py --output data/module-compression/authorizing-load-bearing.csv
```

The audit is a screen, not a decision procedure. A distinctive node is compression-vulnerable when
it is absent from the module's authorizing evaluation requirements and activated paths.

The current CSV is regenerated after the provisional trim in
`notes/provisional-node-trim-2026-06-09.md`.
