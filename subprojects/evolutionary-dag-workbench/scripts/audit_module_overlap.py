#!/usr/bin/env python3
"""Summarize node overlap among scoped graph modules."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GRAPHS = ROOT / "graphs" / "archive"


def base_node(node_id: str) -> str:
    return re.sub(r"_t\d*$", "", node_id)


def load_graphs(paths: list[Path], scoped_only: bool) -> dict[str, set[str]]:
    modules = {}
    for path in paths:
        data = json.loads(path.read_text(encoding="utf8"))
        if scoped_only and data.get("score_status", {}).get("kind") != "scoped_module":
            continue
        modules[data["id"]] = {base_node(node) for node in data.get("nodes", [])}
    return modules


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("graphs", nargs="*", type=Path)
    parser.add_argument("--all", action="store_true", help="Include unscored candidate graphs.")
    args = parser.parse_args()

    paths = args.graphs or sorted(DEFAULT_GRAPHS.glob("*.json"))
    modules = load_graphs(paths, scoped_only=not args.all)
    ids = sorted(modules)

    print("PAIRWISE JACCARD")
    for index, left in enumerate(ids):
        for right in ids[index + 1:]:
            overlap = modules[left] & modules[right]
            union = modules[left] | modules[right]
            score = len(overlap) / len(union) if union else 0
            print(
                f"{left}\t{right}\t{len(overlap)}/{len(union)}\t{score:.2f}\t"
                f"{', '.join(sorted(overlap))}"
            )

    print("\nDISTINCTIVE NODES")
    for module_id in ids:
        others = set().union(*(modules[other] for other in ids if other != module_id))
        distinctive = modules[module_id] - others
        print(f"{module_id}\t{len(distinctive)}\t{', '.join(sorted(distinctive))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
