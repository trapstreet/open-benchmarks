#!/usr/bin/env bash
# Install the pinned AppWorld and download its data into ./appworld-root.
# Needs: uv, git, git-lfs (AppWorld's code ships in LFS bundles).
set -euo pipefail
cd "$(dirname "$0")"

APPWORLD_COMMIT=42b5bcf
command -v git-lfs >/dev/null || { echo "git-lfs is required (brew install git-lfs)" >&2; exit 1; }

uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.lock.txt
uv pip install --python .venv/bin/python "appworld @ git+https://github.com/StonyBrookNLP/appworld@${APPWORLD_COMMIT}"
.venv/bin/appworld install
mkdir -p appworld-root
.venv/bin/appworld download data --root appworld-root
