from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


TEXT_FIELDS = ("Tweets", "tweets", "tweet", "text", "full_text", "content", "body")
CONTAINER_FIELDS = ("tweets", "data", "results", "items")


def main() -> None:
    args = parse_args()
    rows = [{"Tweets": clean_text(text)} for text in load_texts(args.input)]
    rows = [row for row in rows if row["Tweets"]]

    with args.output.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Tweets"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {args.output}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a TweetClaw export into a Tweets column CSV."
    )
    parser.add_argument("input", type=Path, help="TweetClaw CSV, JSON, or JSONL export.")
    parser.add_argument("output", type=Path, help="Destination CSV file.")
    return parser.parse_args()


def load_texts(path: Path) -> list[str]:
    suffix = path.suffix.lower()

    if suffix == ".csv":
        with path.open(newline="", encoding="utf-8") as file:
            return [first_text(row) for row in csv.DictReader(file)]

    if suffix == ".jsonl":
        records = []
        with path.open(encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        return [first_text(record) for record in records]

    if suffix == ".json":
        with path.open(encoding="utf-8") as file:
            return [first_text(record) for record in unwrap_records(json.load(file))]

    raise ValueError("Input must be a CSV, JSON, or JSONL file.")


def unwrap_records(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [record for record in payload if isinstance(record, dict)]

    if isinstance(payload, dict):
        for field in CONTAINER_FIELDS:
            records = payload.get(field)
            if isinstance(records, list):
                return [record for record in records if isinstance(record, dict)]
        return [payload]

    return []


def first_text(record: dict[str, Any]) -> str:
    for field in TEXT_FIELDS:
        value = record.get(field)
        if value is not None:
            text = str(value).strip()
            if text:
                return text
    return ""


def clean_text(text: str) -> str:
    text = re.sub(r"@[A-Za-z0-9_]+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"RT[\s]+", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    return re.sub(r"\s+", " ", text).strip()


if __name__ == "__main__":
    main()
