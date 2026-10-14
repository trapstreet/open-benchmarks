import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import json

import split

DEV = [
    {"question_id": 13, "db_id": "california_schools", "difficulty": "moderate", "question": "q", "evidence": "", "SQL": "SELECT 1"},
    {"question_id": 7, "db_id": "card_games", "difficulty": "simple", "question": "q", "evidence": "", "SQL": "SELECT 1"},
    {"question_id": 8, "db_id": "superhero", "difficulty": "challenging", "question": "q", "evidence": "", "SQL": "SELECT 1"},
]
REGISTRY = [
    {"name": "other", "version": "x", "tasks": [{"name": "superhero__8"}]},
    {"name": "bird-bench", "version": "parity", "tasks": [{"name": "california_schools__13"}, {"name": "card_games__7"}]},
]


def write(tmp: Path) -> tuple[Path, Path]:
    dev, reg = tmp / "dev.json", tmp / "registry.json"
    dev.write_text(json.dumps(DEV))
    reg.write_text(json.dumps(REGISTRY))
    return dev, reg


def test_small_and_large_are_the_eleven_databases_split_eight_three():
    assert len(split.SMALL_DBS) == 8 and len(split.LARGE_DBS) == 3
    assert not split.SMALL_DBS & split.LARGE_DBS
    assert {"european_football_2", "codebase_community", "card_games"} == split.LARGE_DBS


def test_harbor_ids_read_only_the_parity_dataset(tmp_path):
    _, reg = write(tmp_path)
    assert split.harbor_ids(reg) == ["california_schools__13", "card_games__7"]


def test_write_all_splits_harbor_ids_by_database_size(tmp_path):
    dev, reg = write(tmp_path)
    split.write_all(dev, reg, tmp_path)
    read = lambda p: (tmp_path / "subsets" / p).read_text().split()
    assert read("harbor-parity-150.txt") == ["california_schools__13", "card_games__7"]
    assert read("small-104.txt") == ["california_schools__13"]
    assert read("large-46.txt") == ["card_games__7"]
    rows = (tmp_path / "catalog.tsv").read_text().splitlines()
    assert rows[0] == "case_id\tdb_id\tquestion_id\tdifficulty\tsmall"
    assert rows[1] == "california_schools__13\tcalifornia_schools\t13\tmoderate\tyes"
    assert len(rows) == 4


def test_harbor_id_missing_from_dev_is_an_error(tmp_path):
    dev, reg = write(tmp_path)
    data = json.loads(reg.read_text())
    data[1]["tasks"].append({"name": "superhero__999"})
    reg.write_text(json.dumps(data))
    try:
        split.write_all(dev, reg, tmp_path)
    except SystemExit as e:
        assert "superhero__999" in str(e)
    else:
        raise AssertionError("expected SystemExit")
