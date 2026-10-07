# AppWorld

A case is one AppWorld task: an instruction from a simulated person ("Venmo my
roommates their share of last month's utilities…"), carried out against nine
simulated apps through their APIs. The task passes when the apps' databases end up
in the state the task's tests require — and nothing else was changed along the way.

## Setup

AppWorld is pinned to commit `42b5bcf` of
[StonyBrookNLP/appworld](https://github.com/StonyBrookNLP/appworld). Its code ships
in Git LFS bundles, so `git-lfs` must be installed first.

```bash
./setup.sh            # venv + pinned AppWorld + `appworld install` + data download
```

The data lands in `appworld-root/` (git-ignored). It is AppWorld's to distribute:
do not commit it, copy it into an agent's workspace, or publish anything derived
from it unencrypted.

## Cases

`traptask.yaml` lists cases; each `inputs/<case>/task_id.txt` holds one AppWorld
task id and nothing else.

## Tool surfaces

A harness reaches the apps through one of three surfaces, all generated from
AppWorld's own API documentation so that names, descriptions, parameters, errors
and output limits are identical across them:

| Surface | What the agent sees |
|---|---|
| [`env/mcp/`](env/mcp/) | One MCP tool per API |
| [`env/cli/`](env/cli/) | One command, `aw <app> <api> --param value`, with `--help` at every level |
| [`env/python/`](env/python/) | A Python interpreter with `apis.<app>.<api>(...)`, which can reach the API server and nothing else |

Logging in is the same on every surface: the agent gets account credentials
from the `supervisor` app and calls each app's login API itself.

## What a solution returns

A solution starts the case's world with `env/` and lets its agent work. When the
agent calls `supervisor.complete_task`, it prints one JSON object to stdout:

```json
{"task_id": "...", "dbs": {"<app>.jsonl": "<changes against the base database>"}}
```

## Judge

`judge.py` checks the submission's shape — known app names only, well-formed rows,
a size cap — then rebuilds AppWorld's output directory and runs `appworld evaluate`
on it, offline. A malformed submission scores 0 and is never handed to AppWorld.

Columns: task completion (all of a task's tests pass) and, per scenario, scenario
completion (every variant of a scenario passes), as AppWorld reports them.
