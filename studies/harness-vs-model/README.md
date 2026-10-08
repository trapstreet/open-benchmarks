# harness-vs-model

> **Status: in setup.** Arms, models and run counts are being agreed with
> ConnectOnion; nothing below is final until [PREREGISTRATION.md](PREREGISTRATION.md)
> is frozen.

**Bigger model or better harness?** This study answers that with one design: hold
the model fixed and change only the harness, then compare that against holding the
harness fixed and changing the model. Every cell runs the same cases, so the two effects are measured on the same
ground and can be put side by side.

Run with [ConnectOnion](https://github.com/openonion/connectonion) and scored on
[trapstreet.run](https://trapstreet.run).

## What is here

| Directory | Benchmark | What the harness axis means there |
|---|---|---|
| [`appworld/`](../../appworld/) | [AppWorld](https://github.com/StonyBrookNLP/appworld) — nine simulated everyday apps (Gmail, Venmo, Spotify, Todoist, files, …), 457 APIs, graded on the apps' database state | The agent loop, **and** how the tools reach the agent: MCP, a command line, or Python |
| [`dabstep/`](../../dabstep/) | [DABStep](https://huggingface.co/datasets/adyen/DABstep) — data-analysis questions over a payments dataset | The agent loop, with each harness's own tools or with one shared toolbox |
| [`mcpmark/`](../../mcpmark/) | [MCPMark](https://github.com/eval-sys/mcpmark) — file and database tasks, checked by script | The real command line (shell, `psql`) against a published MCP server for the same service |

Solutions are not in this repository. Each harness arm lives in its owner's repository and is
submitted with `tp run`; the board links every row to the exact commit it ran.

## AppWorld and MCPMark: what each can show

Both put the same agent on the same model behind a command line or behind MCP. They
answer different versions of that question.

| | AppWorld | MCPMark (filesystem + postgres) |
|---|---|---|
| Work | Everyday errands across nine apps: mail, payments, music, notes, to-dos | File and database operations |
| Tools in front of the agent | 469 over MCP (about 256K characters of tool definitions) | A short list per server: file operations, or SQL and schema inspection |
| The two surfaces | Generated from AppWorld's API documentation, so they carry the same names, descriptions and errors and differ only in how they reach the agent | The tools people already use (the shell, `psql`) against the published MCP server for the same service; nothing written for this study |
| So a difference means | The way tools reach the agent matters, including what a large tool list costs in context | The real CLI beats or trails the real MCP server, tool quality included |
| Cases | 417 in `test_challenge` | 71 that run without accounts |
| Task text | Distributed encrypted | Public on GitHub, with the verification scripts |
| Graded on | The apps' database state, including changes nobody asked for | The final files or tables, by MCPMark's scripts |

AppWorld is the closer match to an agent working across someone's accounts and
apps. MCPMark is the more direct test of "use the CLI that already exists".
Which of them the study runs is decided in [PREREGISTRATION.md](PREREGISTRATION.md).

## The grid

|                | harness A | harness B | harness C | … |
|---|---|---|---|---|
| **model 1** | | | | |
| **model 2** | | | | |

- **Harness effect**: along a row — same model, different harness.
- **Model effect**: down a column — same harness, different model.
- **Interaction**: whether a harness helps one model and not another.

Cells are compared case by case (paired), and each cell runs more than once.
The rules — which cells, how many runs, which columns, and that every result is
published whichever way it falls — are fixed in [PREREGISTRATION.md](PREREGISTRATION.md)
before the first paid run.

## Fixed in every cell

- **The model endpoint.** Every arm calls the model through the endpoint `tp run`
  provides, so spend is metered the same way and no arm routes through a hosted
  model of its own.
- **Isolation.** Agents run in a filesystem and network jail that exposes the case
  and nothing else. For AppWorld that means the tool endpoint and no route to the
  data directory or to AppWorld's code-execution server.
- **The case set and the judge.**

## AppWorld's data

AppWorld's task data is released under Apache-2.0 on the condition that any public
redistribution stays encrypted. This repository therefore carries **task ids
only**. Each user downloads the data from AppWorld directly; the instructions and
the evaluation tests come from there, never from here. See
[`appworld/README.md`](../../appworld/README.md).

## Citation

AppWorld: Trivedi et al., *AppWorld: A Controllable World of Apps and People for
Benchmarking Interactive Coding Agents*, ACL 2024. DABStep: Egg et al.,
*DABstep: Data Agent Benchmark for Multi-step Reasoning*, arXiv:2506.23719.
MCPMark: *MCPMark: A Benchmark for Stress-Testing Realistic and Comprehensive MCP
Use*, arXiv:2509.24002.
