#!/usr/bin/env python3
"""Audit whether scoped-module distinctive nodes are used by authorizing evaluations."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "graphs" / "archive"


def base_node(node_id: str) -> str:
    return re.sub(r"_t\d*$", "", node_id)


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a JSON object")
    return data


def graph_nodes(graph: dict) -> set[str]:
    return {base_node(node) for node in graph.get("nodes", []) if isinstance(node, str)}


def scoped_graphs() -> dict[str, tuple[Path, dict, set[str]]]:
    graphs: dict[str, tuple[Path, dict, set[str]]] = {}
    for path in sorted(GRAPH_DIR.glob("*.json")):
        graph = load_json(path)
        if graph.get("score_status", {}).get("kind") != "scoped_module":
            continue
        graph_id = graph.get("id")
        if isinstance(graph_id, str) and graph_id.strip():
            graphs[graph_id] = (path, graph, graph_nodes(graph))
    return graphs


def collect_evaluation_uses(evaluation: dict) -> dict[str, set[str]]:
    uses = {
        "required_nodes": set(),
        "required_edges": set(),
        "activated_paths": set(),
    }

    for card in evaluation.get("cards", []):
        if not isinstance(card, dict):
            continue
        requirements = card.get("requirements", {})
        if not isinstance(requirements, dict):
            continue

        for node in requirements.get("required_nodes", []):
            if isinstance(node, str) and node.strip():
                uses["required_nodes"].add(base_node(node))

        for edge_key in ("required_edges", "forbidden_edges"):
            for edge in requirements.get(edge_key, []):
                if not isinstance(edge, dict):
                    continue
                for endpoint in ("source", "target"):
                    node = edge.get(endpoint)
                    if isinstance(node, str) and node.strip():
                        uses["required_edges"].add(base_node(node))

    for activated_path in evaluation.get("activated_paths", []):
        if not isinstance(activated_path, dict):
            continue
        for edge in activated_path.get("edges", []):
            if not isinstance(edge, dict):
                continue
            for endpoint in ("source", "target"):
                node = edge.get(endpoint)
                if isinstance(node, str) and node.strip():
                    uses["activated_paths"].add(base_node(node))

    return uses


def load_authorizing_evaluation(graph: dict) -> tuple[str, dict | None]:
    evaluation_ref = graph.get("score_status", {}).get("evaluation")
    if not isinstance(evaluation_ref, str) or not evaluation_ref.strip():
        return "", None
    evaluation_path = ROOT / evaluation_ref
    if not evaluation_path.exists():
        return evaluation_ref, None
    return evaluation_ref, load_json(evaluation_path)


def verdict(node: str, uses: dict[str, set[str]]) -> str:
    if node in uses["activated_paths"]:
        return "activated_path"
    if node in uses["required_edges"]:
        return "required_edge"
    if node in uses["required_nodes"]:
        return "required_node_only"
    return "not_authorized"


def rows() -> list[dict[str, str]]:
    graphs = scoped_graphs()
    all_nodes_by_graph = {graph_id: nodes for graph_id, (_path, _graph, nodes) in graphs.items()}
    output: list[dict[str, str]] = []

    for graph_id, (_path, graph, nodes) in sorted(graphs.items()):
        other_nodes = set().union(
            *(other_nodes for other_id, other_nodes in all_nodes_by_graph.items() if other_id != graph_id)
        )
        distinctive_nodes = sorted(nodes - other_nodes)
        evaluation_ref, evaluation = load_authorizing_evaluation(graph)
        uses = collect_evaluation_uses(evaluation) if evaluation is not None else {
            "required_nodes": set(),
            "required_edges": set(),
            "activated_paths": set(),
        }

        for node in distinctive_nodes:
            node_verdict = verdict(node, uses)
            output.append(
                {
                    "module": graph_id,
                    "authorizing_evaluation": evaluation_ref,
                    "distinctive_node": node,
                    "in_required_nodes": "yes" if node in uses["required_nodes"] else "no",
                    "in_required_edges": "yes" if node in uses["required_edges"] else "no",
                    "in_activated_paths": "yes" if node in uses["activated_paths"] else "no",
                    "load_bearing_status": node_verdict,
                }
            )
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional CSV output path.")
    args = parser.parse_args()

    fieldnames = [
        "module",
        "authorizing_evaluation",
        "distinctive_node",
        "in_required_nodes",
        "in_required_edges",
        "in_activated_paths",
        "load_bearing_status",
    ]
    data = rows()

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
            writer.writeheader()
            writer.writerows(data)

    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
