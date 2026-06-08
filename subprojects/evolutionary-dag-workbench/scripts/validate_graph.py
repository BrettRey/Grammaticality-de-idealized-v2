#!/usr/bin/env python3
"""Validate simple conceptual DAG JSON files."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path


EDGE_TYPES = {
    "causal",
    "mediating",
    "measurement",
    "constitutive",
    "evidential",
    "time_lagged",
}
TIME_SLICE_PATTERN = re.compile(r"^(?P<base>.+)_t(?P<index>[0-9]*)$")


def load_graph(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def node_id(node: str | dict) -> str:
    if isinstance(node, str):
        return node
    if isinstance(node, dict) and isinstance(node.get("id"), str):
        return node["id"]
    raise ValueError(f"Invalid node entry: {node!r}")


def time_index(node: str) -> int | None:
    match = TIME_SLICE_PATTERN.match(node)
    if not match:
        return None
    index = match.group("index")
    if not index:
        return 0
    return int(index)


def check_required(graph: dict, path: Path) -> list[str]:
    errors: list[str] = []
    for field in ("id", "title", "nodes", "edges"):
        if field not in graph:
            errors.append(f"{path}: missing required field {field!r}")
    if "nodes" in graph and not isinstance(graph["nodes"], list):
        errors.append(f"{path}: 'nodes' must be a list")
    if "edges" in graph and not isinstance(graph["edges"], list):
        errors.append(f"{path}: 'edges' must be a list")
    return errors


def check_edges(graph: dict, path: Path) -> tuple[list[str], list[tuple[str, str, str]]]:
    errors: list[str] = []
    nodes = {node_id(node) for node in graph.get("nodes", [])}
    edges_for_dag: list[tuple[str, str, str]] = []
    seen_edges: set[tuple[str, str, str]] = set()

    for index, edge in enumerate(graph.get("edges", []), start=1):
        if not isinstance(edge, dict):
            errors.append(f"{path}: edge {index} is not an object")
            continue

        source = edge.get("source")
        target = edge.get("target")
        edge_type = edge.get("type")

        if source not in nodes:
            errors.append(f"{path}: edge {index} source {source!r} is not in nodes")
        if target not in nodes:
            errors.append(f"{path}: edge {index} target {target!r} is not in nodes")
        if edge_type not in EDGE_TYPES:
            errors.append(f"{path}: edge {index} type {edge_type!r} is not allowed")
        if source == target:
            errors.append(f"{path}: edge {index} is a self-loop")
        if not edge.get("rationale"):
            errors.append(f"{path}: edge {index} lacks a rationale")
        if isinstance(source, str) and isinstance(target, str) and isinstance(edge_type, str):
            edge_key = (source, target, edge_type)
            if edge_key in seen_edges:
                errors.append(
                    f"{path}: edge {index} duplicates source/target/type "
                    f"{source!r} -> {target!r} ({edge_type})"
                )
            seen_edges.add(edge_key)
        if edge_type == "time_lagged" and isinstance(source, str) and isinstance(target, str):
            source_time = time_index(source)
            target_time = time_index(target)
            if source_time is None or target_time is None:
                errors.append(
                    f"{path}: edge {index} time_lagged endpoints must both be time-sliced"
                )
            elif target_time <= source_time:
                errors.append(
                    f"{path}: edge {index} time_lagged edge must point forward in time "
                    f"({source!r} -> {target!r})"
                )

        if edge_type != "time_lagged" and source in nodes and target in nodes:
            edges_for_dag.append((source, target, edge_type))

    return errors, edges_for_dag


def check_acyclic(nodes: set[str], edges: list[tuple[str, str, str]], path: Path) -> list[str]:
    outgoing: dict[str, list[str]] = defaultdict(list)
    indegree = {node: 0 for node in nodes}

    for source, target, _edge_type in edges:
        outgoing[source].append(target)
        indegree[target] += 1

    queue = deque(node for node, degree in indegree.items() if degree == 0)
    seen = 0

    while queue:
        current = queue.popleft()
        seen += 1
        for target in outgoing[current]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)

    if seen != len(nodes):
        return [f"{path}: non-time-lagged edges contain a cycle"]
    return []


def validate(path: Path) -> list[str]:
    try:
        graph = load_graph(path)
    except Exception as exc:  # noqa: BLE001 - CLI should report any parse/load error.
        return [f"{path}: cannot load JSON: {exc}"]

    errors = check_required(graph, path)
    if errors:
        return errors

    try:
        nodes = {node_id(node) for node in graph.get("nodes", [])}
    except ValueError as exc:
        return [f"{path}: {exc}"]

    edge_errors, edges_for_dag = check_edges(graph, path)
    errors.extend(edge_errors)
    if not edge_errors:
        errors.extend(check_acyclic(nodes, edges_for_dag, path))
    return errors


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: validate_graph.py GRAPH.json [GRAPH.json ...]", file=sys.stderr)
        return 2

    all_errors: list[str] = []
    for raw_path in argv:
        path = Path(raw_path)
        errors = validate(path)
        if errors:
            all_errors.extend(errors)
        else:
            print(f"ok: {path}")

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
