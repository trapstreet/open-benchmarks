# MCPMark

[MCPMark](https://github.com/eval-sys/mcpmark) (Apache-2.0, ICLR 2026) — agent tasks
against real tool environments, each checked by a script that inspects the final
state. Pinned to commit `cd45b7f57923b9b3985467f5139927575f83141c`.

This directory carries **task ids only**. The descriptions, verification scripts
and test data come from MCPMark itself: clone the pinned commit, and download the
test folders and database backups from MCPMark's storage as its docs describe.

## Catalog

[`tasks.tsv`](tasks.tsv) lists all 239 task ids at the pinned commit, with what
each one needs to run. No subset is chosen yet: a study picks its cases from this
list and records the choice in its preregistration.

| Service | Tasks | Needs | Runs locally without accounts |
|---|---|---|---|
| filesystem | 40 | Test folders | yes |
| postgres | 31 | A local PostgreSQL and five sample databases | yes |
| github | 33 | A GitHub account and token | no |
| notion | 38 | A Notion account and token | no |
| playwright | 4 | The live web | no |
| playwright_webarena | 31 | WebArena's Docker images | yes, but heavy |
| supabase | 31 | Local Supabase (Docker) | the postgres tasks on another backend |
| insforge | 31 | An InsForge backend | the postgres tasks on another backend |

The 71 filesystem and postgres tasks are graded by deterministic scripts — no
model in the loop.

## Why it is here

Both local services already have a command line people use every day: the shell
for files, `psql` for the database. MCPMark runs each through a published MCP
server instead: `@modelcontextprotocol/server-filesystem@2025.12.18` and
`postgres-mcp==0.3.0`. So the same agent on the same model can be given the real
CLI or the real MCP server, with no tool layer written by us in between.

## Isolation

MCPMark's verification scripts are public. An agent runs in a jail that exposes
its test folder or its database connection and nothing else.
