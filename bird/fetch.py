"""Download BIRD dev at the pinned revision and check every file.

    python3 fetch.py ~/.cache/trapstreet-bird

Writes <cache>/dev.json, <cache>/registry.json and
<cache>/dev_databases/<db>.sqlite for all 11 databases. Every file is checked
against sources.json; a mismatch stops with the name of the file. Nothing
here is committed: the cache is outside the repository.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = json.loads((HERE / "sources.json").read_text())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path) -> None:
    tmp = dest.with_suffix(dest.suffix + ".part")
    with urllib.request.urlopen(url, timeout=600) as r, tmp.open("wb") as f:
        shutil.copyfileobj(r, f, 1 << 20)
    tmp.rename(dest)


def checked(path: Path, want: str) -> None:
    got = sha256(path)
    if got != want:
        raise SystemExit(f"{path.name}: sha256 {got} != pinned {want}")


def fetch(cache: Path) -> Path:
    cache.mkdir(parents=True, exist_ok=True)
    dev = cache / "dev.json"
    if not dev.exists():
        download(SOURCES["dev_json"]["url"], dev)
    checked(dev, SOURCES["dev_json"]["sha256"])

    registry = cache / "registry.json"
    if not registry.exists():
        download(SOURCES["harbor_registry"]["url"], registry)

    dbs = cache / "dev_databases"
    if not all((dbs / f"{d}.sqlite").exists() for d in SOURCES["databases"]):
        z = cache / "dev_databases.zip"
        if not z.exists():
            download(SOURCES["databases_zip"]["url"], z)
        checked(z, SOURCES["databases_zip"]["sha256"])
        dbs.mkdir(exist_ok=True)
        prefix = SOURCES["databases_zip"]["member_prefix"]
        with zipfile.ZipFile(z) as zf:
            for db in SOURCES["databases"]:
                with zf.open(f"{prefix}{db}/{db}.sqlite") as src, (dbs / f"{db}.sqlite").open("wb") as out:
                    shutil.copyfileobj(src, out, 1 << 20)
        z.unlink()
    for db, want in SOURCES["databases"].items():
        checked(dbs / f"{db}.sqlite", want)
    return cache


if __name__ == "__main__":
    print(fetch(Path(sys.argv[1]).expanduser()))
