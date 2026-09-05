from __future__ import annotations

import json
from pathlib import Path

from catalog import RECORDS_DIR, build_index


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    index, entries = build_index()
    RECORDS_DIR.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        write_json(RECORDS_DIR / f"{entry['id']}.json", entry)

    write_json(RECORDS_DIR / "index.json", index)


if __name__ == "__main__":
    main()

