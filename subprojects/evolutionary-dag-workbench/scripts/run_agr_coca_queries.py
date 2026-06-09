#!/usr/bin/env python3
"""Run or print the registered AGR COCA query plan.

This script is intentionally thin. It does not interpret COCA results; it only
turns data/agr-coca-projection/query-plan.csv into auditable calls to the shared
English-Corpora.org wrapper.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PLAN = ROOT / "data" / "agr-coca-projection" / "query-plan.csv"
DEFAULT_RAW_DIR = ROOT / "data" / "agr-coca-projection" / "raw"
DEFAULT_WRAPPER = (
    Path("/Users/brettreynolds/Documents/LLM-CLI-projects")
    / "tools"
    / "english-corpora"
    / "bin"
    / "ecorg.mjs"
)


def slug(text: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", text.strip().lower())
    return value.strip("-") or "query"


def read_plan(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf8") as f:
        return list(csv.DictReader(f))


def iter_queries(rows: list[dict[str, str]], cells: set[str] | None) -> list[dict[str, str]]:
    expanded = []
    for row in rows:
        cell_id = row["cell_id"]
        if cells and cell_id not in cells:
            continue
        queries = [q.strip() for q in row["example_queries"].split("|") if q.strip()]
        for index, query in enumerate(queries, start=1):
            expanded.append({
                "cell_id": cell_id,
                "stage": row["stage"],
                "query_family": row["query_family"],
                "query_index": str(index),
                "query": query,
            })
    return expanded


def status(wrapper: Path, corpus: str) -> dict[str, object]:
    result = subprocess.run(
        ["node", str(wrapper), "status", "--corpus", corpus],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Could not parse wrapper status as JSON: {result.stdout!r}") from exc


def command_for(
    wrapper: Path,
    corpus: str,
    query_type: str,
    query: str,
    output: Path,
    kwic_rows: int,
    output_format: str,
) -> list[str]:
    cmd = [
        "node",
        str(wrapper),
        "query",
        "--corpus",
        corpus,
        "--type",
        query_type,
        "--query",
        query,
        "--format",
        output_format,
        "--output",
        str(output),
    ]
    if query_type == "kwic":
        cmd.extend(["--kwic", str(kwic_rows)])
    return cmd


def write_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "cell_id",
        "stage",
        "query_family",
        "query_index",
        "query",
        "output",
        "command",
    ]
    with path.open("w", newline="", encoding="utf8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--wrapper", type=Path, default=DEFAULT_WRAPPER)
    parser.add_argument("--corpus", default="coca")
    parser.add_argument("--type", choices=["kwic", "list"], default="kwic")
    parser.add_argument("--format", choices=["json", "text", "html"], default="json")
    parser.add_argument("--kwic", type=int, choices=[100, 200, 500, 1000], default=100)
    parser.add_argument("--cell", action="append", help="Restrict to one cell_id; repeatable.")
    parser.add_argument("--manifest", type=Path, help="Write expanded command manifest CSV.")
    parser.add_argument("--delay", type=float, default=4.0, help="Seconds to wait between live queries.")
    parser.add_argument("--preflight-status", action="store_true", help="Require wrapper status to report authenticated before running.")
    parser.add_argument("--run", action="store_true", help="Execute queries. Default only prints.")
    args = parser.parse_args()

    rows = read_plan(args.plan)
    expanded = iter_queries(rows, set(args.cell) if args.cell else None)
    if not expanded:
        print("No query rows selected.", file=sys.stderr)
        return 1

    manifest_rows = []
    commands = []
    for item in expanded:
        output = (
            args.raw_dir
            / item["cell_id"]
            / f"{int(item['query_index']):02d}-{slug(item['query'])}.{args.format}"
        )
        cmd = command_for(
            args.wrapper,
            args.corpus,
            args.type,
            item["query"],
            output,
            args.kwic,
            args.format,
        )
        commands.append(cmd)
        try:
            output_label = str(output.relative_to(ROOT))
        except ValueError:
            output_label = str(output)
        manifest_rows.append({
            **item,
            "output": output_label,
            "command": shlex.join(cmd),
        })

    if args.manifest:
        write_manifest(args.manifest, manifest_rows)

    if not args.run:
        for row in manifest_rows:
            print(row["command"])
        return 0

    if args.preflight_status:
        session = status(args.wrapper, args.corpus)
        if not session.get("authenticated"):
            print(
                "English-Corpora.org status does not report an authenticated browser session. "
                "Run the shared wrapper login or omit --preflight-status to let ecorg query use "
                "configured private credentials.",
                file=sys.stderr,
            )
            return 2

    for index, (row, cmd) in enumerate(zip(manifest_rows, commands, strict=True), start=1):
        output = ROOT / row["output"]
        output.parent.mkdir(parents=True, exist_ok=True)
        print(f"running: {row['cell_id']} :: {row['query']}", file=sys.stderr)
        result = subprocess.run(cmd, check=False)
        if result.returncode != 0:
            return result.returncode
        if index < len(commands) and args.delay > 0:
            time.sleep(args.delay)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
