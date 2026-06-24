#!/usr/bin/env python3
"""Select AGR-vs-listing v2 candidate frames from denominator-only COCA scout rows.

This script is a boundary guard, not an evidence adjudicator. It reads raw list-query
artifacts for a predeclared scout cell and flags phrase frames whose denominator counts
are large enough to be runnable but not so large that construction-specific listing can
claim an already-central stored preference by default.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PLAN = ROOT / "data" / "agr-coca-projection" / "query-plan.csv"
DEFAULT_RAW_DIR = ROOT / "data" / "agr-coca-projection" / "raw"


def slug(text: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", text.strip().lower())
    return value.strip("-") or "query"


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).upper()


def read_queries(plan: Path, cell_id: str) -> list[str]:
    with plan.open(newline="", encoding="utf8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        if row.get("cell_id") == cell_id:
            return [q.strip() for q in row.get("example_queries", "").split("|") if q.strip()]
    raise SystemExit(f"No query-plan row found for cell {cell_id!r}")


def parse_list_count(path: Path, query: str) -> tuple[int | None, str]:
    if not path.exists():
        return None, "missing"

    try:
        with path.open(encoding="utf8") as handle:
            data = json.load(handle)
    except Exception:
        return None, "unparseable_json"

    text = data.get("text", "")
    if isinstance(text, str) and "no matching records" in text.lower():
        return 0, "raw_zero"

    wanted = normalize(query)
    tables = data.get("tables", [])
    if isinstance(tables, list):
        for table in tables:
            if not isinstance(table, list):
                continue
            for row in table:
                if not isinstance(row, list):
                    continue
                cells = [cell for cell in row if isinstance(cell, str)]
                if not any(normalize(cell) == wanted for cell in cells):
                    continue
                for cell in reversed(cells):
                    token = cell.replace(",", "").strip()
                    if token.isdigit():
                        return int(token), "parsed"

    if isinstance(text, str):
        pattern = re.compile(re.escape(wanted) + r"\s+([0-9][0-9,]*)")
        match = pattern.search(normalize(text))
        if match:
            return int(match.group(1).replace(",", "")), "parsed_text"

    return None, "count_not_found"


def classify(count: int | None, minimum: int, maximum: int) -> tuple[str, str]:
    if count is None:
        return "unusable", "No denominator count was available."
    if count < minimum:
        return "too_sparse", "Too few denominator opportunities for an agreement follow-up."
    if count > maximum:
        return "too_listable", "Too frequent for a clean low-frequency listing-rival challenge."
    return "eligible", "Eligible for pre-registered finite-agreement follow-up."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--cell", default="low-frequency-qn-scout")
    parser.add_argument("--min-count", type=int, default=3)
    parser.add_argument("--max-count", type=int, default=200)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    queries = read_queries(args.plan, args.cell)
    rows: list[dict[str, str]] = []
    for index, query in enumerate(queries, start=1):
        raw_file = args.raw_dir / args.cell / f"{index:02d}-{slug(query)}.json"
        count, parse_status = parse_list_count(raw_file, query)
        selection_status, recommendation = classify(count, args.min_count, args.max_count)
        rows.append({
            "cell_id": args.cell,
            "query": query,
            "raw_count": "" if count is None else str(count),
            "parse_status": parse_status,
            "selection_status": selection_status,
            "raw_file": str(raw_file.relative_to(ROOT)),
            "recommendation": recommendation,
        })

    fieldnames = [
        "cell_id",
        "query",
        "raw_count",
        "parse_status",
        "selection_status",
        "raw_file",
        "recommendation",
    ]

    output = sys.stdout
    close_output = False
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        output = args.output.open("w", newline="", encoding="utf8")
        close_output = True

    try:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if close_output:
            output.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
