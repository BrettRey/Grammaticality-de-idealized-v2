#!/usr/bin/env python3
"""Print a compact summary of evaluation JSON files."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_json(path: Path) -> dict | None:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def count_requirements(requirements: object) -> str:
    if not isinstance(requirements, dict):
        return "requirements=0"
    parts: list[str] = []
    for key in ("required_nodes", "required_edges", "forbidden_nodes", "forbidden_edges"):
        value = requirements.get(key, [])
        if isinstance(value, list) and value:
            parts.append(f"{key}={len(value)}")
    return ", ".join(parts) if parts else "requirements=0"


def summarize(path: Path) -> list[str]:
    data = load_json(path)
    if data is None:
        return [f"{path}: cannot load JSON object"]

    lines = [
        f"{path}",
        f"  id: {data.get('id', '<missing>')}",
        f"  target_graph: {data.get('target_graph', '<missing>')}",
        f"  status: {data.get('status', '<missing>')}",
        f"  score_decision: {data.get('score_decision', '<missing>')}",
    ]

    held_out_from = data.get("held_out_from")
    if isinstance(held_out_from, list) and held_out_from:
        lines.append(f"  held_out_from: {', '.join(str(item) for item in held_out_from)}")

    cards = data.get("cards")
    if isinstance(cards, list):
        lines.append(f"  cards: {len(cards)}")
        for card in cards:
            if not isinstance(card, dict):
                continue
            phenomenon = card.get("phenomenon", "<missing>")
            result = card.get("result", "<missing>")
            cells = card.get("contrast_cells", [])
            cell_count = len(cells) if isinstance(cells, list) else 0
            requirements = count_requirements(card.get("requirements"))
            lines.append(f"    - {phenomenon}: {result}; cells={cell_count}; {requirements}")

    activated_paths = data.get("activated_paths")
    if isinstance(activated_paths, list) and activated_paths:
        lines.append(f"  activated_paths: {len(activated_paths)}")
        for activated_path in activated_paths:
            if not isinstance(activated_path, dict):
                continue
            path_id = activated_path.get("id", "<missing>")
            phenomenon = activated_path.get("phenomenon", "<missing>")
            cell = activated_path.get("contrast_cell", "<missing>")
            reading = activated_path.get("expected_path_reading", "<none>")
            edges = activated_path.get("edges", [])
            edge_count = len(edges) if isinstance(edges, list) else 0
            lines.append(
                f"    - {path_id}: {phenomenon}/{cell}; edges={edge_count}; "
                f"reading={reading}"
            )

    prediction_tests = data.get("prediction_tests")
    if isinstance(prediction_tests, list) and prediction_tests:
        lines.append(f"  prediction_tests: {len(prediction_tests)}")
        for prediction_test in prediction_tests:
            if not isinstance(prediction_test, dict):
                continue
            test_id = prediction_test.get("id", "<missing>")
            phenomenon = prediction_test.get("phenomenon", "<missing>")
            cell = prediction_test.get("contrast_cell", "<missing>")
            status = prediction_test.get("evidence_status", "<missing>")
            path_refs = prediction_test.get("activated_paths", [])
            path_count = len(path_refs) if isinstance(path_refs, list) else 0
            lines.append(
                f"    - {test_id}: {phenomenon}/{cell}; paths={path_count}; "
                f"evidence_status={status}"
            )

    return lines


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: summarize_evaluations.py EVALUATION.json [EVALUATION.json ...]", file=sys.stderr)
        return 2

    for index, raw_path in enumerate(argv):
        if index:
            print()
        for line in summarize(Path(raw_path)):
            print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
