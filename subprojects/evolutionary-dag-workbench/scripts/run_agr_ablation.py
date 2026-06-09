#!/usr/bin/env python3
"""Run focused ablations over the AGR scoped module.

This script creates temporary graph variants, repoints the existing AGR
evaluations at each variant, and records which requirements or activated paths
break. It is a compression check, not a new graph archive.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
import tempfile
from copy import deepcopy
from pathlib import Path

import validate_evaluation
import validate_graph


ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "graphs/archive/agreement-controller-override-candidate.json"
EVALUATION_PATHS = [
    ROOT / "evaluations/protocol-tests/agreement-controller-override-coca-projection-2026-06-09.json",
    ROOT / "evaluations/protocol-tests/agreement-controller-override-heldout-scope-2026-06-09.json",
    ROOT / "evaluations/protocol-tests/agreement-controller-override-heldout-measure-2026-06-09.json",
]


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a JSON object")
    return data


def write_json(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")


def remove_nodes(graph: dict, nodes_to_remove: set[str]) -> dict:
    mutated = deepcopy(graph)
    mutated["nodes"] = [node for node in mutated.get("nodes", []) if node not in nodes_to_remove]
    mutated["edges"] = [
        edge
        for edge in mutated.get("edges", [])
        if edge.get("source") not in nodes_to_remove and edge.get("target") not in nodes_to_remove
    ]
    return mutated


def merge_node(graph: dict, old_node: str, new_node: str) -> dict:
    mutated = deepcopy(graph)
    nodes: list[str] = []
    for node in mutated.get("nodes", []):
        replacement = new_node if node == old_node else node
        if replacement not in nodes:
            nodes.append(replacement)
    mutated["nodes"] = nodes

    edges: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
    for edge in mutated.get("edges", []):
        next_edge = deepcopy(edge)
        if next_edge.get("source") == old_node:
            next_edge["source"] = new_node
        if next_edge.get("target") == old_node:
            next_edge["target"] = new_node
        if next_edge.get("source") == next_edge.get("target"):
            continue
        key = (next_edge.get("source"), next_edge.get("target"), next_edge.get("type"))
        if key in seen:
            continue
        seen.add(key)
        edges.append(next_edge)
    mutated["edges"] = edges
    return mutated


def ablation_variants(graph: dict) -> dict[str, dict]:
    return {
        "baseline": deepcopy(graph),
        "drop_notional_agreement_basis": remove_nodes(graph, {"notional_agreement_basis"}),
        "merge_controller_into_alignment": merge_node(
            graph,
            "agreement_controller_identification",
            "agreement_feature_alignment",
        ),
        "drop_production_probability": remove_nodes(graph, {"production_probability"}),
        "drop_retrieval_attractor_salience": remove_nodes(graph, {"retrieval_attractor_salience"}),
        "drop_agreement_override_pattern": remove_nodes(graph, {"agreement_override_pattern"}),
    }


def first_error(errors: list[str], temp_dir: Path) -> str:
    if not errors:
        return ""
    message = errors[0].replace("\n", " ")
    return message.replace(str(temp_dir), "<tmp>")


def run(output: Path | None) -> int:
    source_graph = load_json(GRAPH_PATH)
    evaluations = [(path, load_json(path)) for path in EVALUATION_PATHS]
    rows: list[dict[str, str | int]] = []

    tmp_parent = ROOT / ".tmp"
    tmp_parent.mkdir(exist_ok=True)
    temp_dir = Path(tempfile.mkdtemp(prefix="agr-ablation-", dir=tmp_parent))
    try:
        for ablation_name, graph in ablation_variants(source_graph).items():
            graph_path = temp_dir / f"{ablation_name}.json"
            write_json(graph_path, graph)
            graph_errors = validate_graph.validate(graph_path)

            for eval_path, evaluation in evaluations:
                eval_copy = deepcopy(evaluation)
                eval_copy["target_graph"] = graph_path.relative_to(ROOT).as_posix()
                temp_eval_path = temp_dir / f"{ablation_name}__{eval_path.name}"
                write_json(temp_eval_path, eval_copy)
                evaluation_errors = validate_evaluation.validate(temp_eval_path)

                rows.append(
                    {
                        "ablation": ablation_name,
                        "evaluation": eval_path.stem,
                        "graph_valid": "yes" if not graph_errors else "no",
                        "evaluation_valid": "yes" if not evaluation_errors else "no",
                        "graph_error_count": len(graph_errors),
                        "evaluation_error_count": len(evaluation_errors),
                        "first_graph_error": first_error(graph_errors, temp_dir),
                        "first_evaluation_error": first_error(evaluation_errors, temp_dir),
                    }
                )
    finally:
        shutil.rmtree(temp_dir)

    fieldnames = [
        "ablation",
        "evaluation",
        "graph_valid",
        "evaluation_valid",
        "graph_error_count",
        "evaluation_error_count",
        "first_graph_error",
        "first_evaluation_error",
    ]
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional CSV path for the ablation summary.",
    )
    args = parser.parse_args()
    return run(args.output)


if __name__ == "__main__":
    raise SystemExit(main())
