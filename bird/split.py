"""Catalog and subsets for BIRD dev.

    python3 split.py <cache>        # after fetch.py; writes catalog.tsv and subsets/

The subset is Harbor's parity set (150 questions, seed 42), read from Harbor's
registry at the commit pinned in sources.json rather than re-drawn, so it is
the same 150 anyone running Harbor gets. It is split by database size: the 8
small databases fit the site's current pipeline (bird-small); the 3 large ones
wait for bird-large.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LARGE_DBS = frozenset({"european_football_2", "codebase_community", "card_games"})
SMALL_DBS = frozenset({
    "financial", "debit_card_specializing", "formula_1", "california_schools",
    "thrombosis_prediction", "toxicology", "student_club", "superhero",
})


def case_id(row: dict) -> str:
    return f"{row['db_id']}__{row['question_id']}"


def load_dev(path: Path) -> list[dict]:
    return json.loads(Path(path).read_text())


def harbor_ids(registry_path: Path) -> list[str]:
    reg = json.loads(Path(registry_path).read_text())
    for entry in reg:
        if entry.get("name") == "bird-bench" and entry.get("version") == "parity":
            return [t["name"] for t in entry["tasks"]]
    raise SystemExit("bird-bench@parity not in the registry")


def write_all(dev_path: Path, registry_path: Path, out_dir: Path) -> None:
    rows = load_dev(dev_path)
    by_id = {case_id(r): r for r in rows}
    harbor = harbor_ids(registry_path)
    missing = [h for h in harbor if h not in by_id]
    if missing:
        raise SystemExit(f"Harbor ids not in BIRD dev: {', '.join(missing)}")
    out = Path(out_dir)
    (out / "subsets").mkdir(parents=True, exist_ok=True)
    lines = ["case_id\tdb_id\tquestion_id\tdifficulty\tsmall"]
    for r in sorted(rows, key=lambda r: (r["db_id"], r["question_id"])):
        lines.append(f"{case_id(r)}\t{r['db_id']}\t{r['question_id']}\t{r['difficulty']}\t"
                     f"{'yes' if r['db_id'] in SMALL_DBS else 'no'}")
    (out / "catalog.tsv").write_text("\n".join(lines) + "\n")
    small = [h for h in harbor if by_id[h]["db_id"] in SMALL_DBS]
    large = [h for h in harbor if by_id[h]["db_id"] in LARGE_DBS]
    for name, ids in (("harbor-parity-150.txt", harbor), ("small-104.txt", small), ("large-46.txt", large)):
        (out / "subsets" / name).write_text("\n".join(sorted(ids)) + "\n")


if __name__ == "__main__":
    cache = Path(sys.argv[1]).expanduser()
    write_all(cache / "dev.json", cache / "registry.json", HERE)
