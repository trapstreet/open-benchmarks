# Preregistration — DRAFT

Status: **draft, not yet agreed.** It is frozen by a tagged commit before the first
paid run, and every result reported on the board is read against the frozen
version. Items marked **OPEN** are still to be decided by both sides.

## Question

With the model held fixed, how much does the harness move the score and the cost?
How does that compare with holding the harness fixed and changing the model?

## Arms

| Arm | Owner | Board |
|---|---|---|
| ConnectOnion `co ai` | ConnectOnion | dabstep, appworld |
| Minimal ConnectOnion agent (shared tools only) | ConnectOnion | dabstep-shared-tools |
| Claude Code, DSH, Pi, minimal loop | trapstreet | dabstep, dabstep-shared-tools, appworld |
| **OPEN**: more harnesses (Codex: blocked until tp can meter it) | | |

Models: **OPEN** (proposal: one frontier model and one low-cost model; on dabstep
these are claude-opus-5 and deepseek-flash, which already have rows).

AppWorld tool surfaces: MCP, CLI and Python, crossed with the harnesses that can
use each. **OPEN**: whether ConnectOnion adds a `co`-style CLI as a fourth surface.

MCPMark tool surfaces (if included): the real CLI (shell, `psql`) or the published
MCP server MCPMark uses for that service.

## Cases

- dabstep: the 25 live cases, unchanged.
- appworld: **OPEN** — a subset of `test_challenge`, drawn as whole scenarios
  with a fixed seed. Size is set by cost per cell × runs per cell. The `dev`
  split is used for building and probing only, never reported.
- mcpmark: **OPEN** — whether to include it, and which ids from
  [`mcpmark/tasks.tsv`](../../mcpmark/tasks.tsv). The 71 filesystem and postgres
  tasks run locally without accounts.

## Runs

- **OPEN**: runs per cell (proposal: 3).
- Same time limit, thinking setting and caching policy within a model across all
  harnesses. Vendor defaults otherwise, written down per arm.
- Every agent runs jailed; transcripts are kept and audited for access outside
  the case before a row is published.

## Columns

- Score: dabstep — share correct; appworld — task completion and scenario completion.
- Cost: metered dollars per run and per correct case.
- Time: median and maximum per case.
- Reported, not scored: unanswered cases, cases at the time limit, tool calls.

## Analysis

- Harness effect: paired comparison of two harnesses on the same model, case by
  case (McNemar on pass/fail; runs per cell pooled per case).
- Model effect: the same comparison down a column.
- Each comparison is reported with its interval. A difference the cases cannot
  resolve is reported as unresolved, not as a tie or a win.

## Publication

Every cell that completes is published, whichever way it falls. A row is withheld
only if its audit finds access outside the case. Such a row is published as
withheld, with the reason, and rerun.
