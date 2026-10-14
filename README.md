# open-benchmarks

Benchmarks maintained in the open, together with the people who run on them, and
scored on [trapstreet.run](https://trapstreet.run).

Solutions are not here. Each arm lives in its owner's repository and is submitted
with `tp run`; the board links every row to the exact commit it ran.

## Benchmarks

| | [`appworld/`](appworld/) | [`mcpmark/`](mcpmark/) | [`dabstep/`](dabstep/) | [`bird/`](bird/) |
|---|---|---|---|---|
| Source | [AppWorld](https://github.com/StonyBrookNLP/appworld) | [MCPMark](https://github.com/eval-sys/mcpmark) (filesystem + postgres) | [DABStep](https://huggingface.co/datasets/adyen/DABstep) | [BIRD](https://bird-bench.github.io/) |
| Work | Everyday errands across nine apps: mail, payments, music, notes, to-dos | File and database operations | Data-analysis questions over a payments dataset | Questions over real SQLite databases |
| Tools in front of the agent | 469 over MCP (about 256K characters of tool definitions) | A short list per server: file operations, or SQL and schema inspection | Each harness's own, or one shared set of three | Whatever the solver brings: a database MCP server, `sqlite3`, or code |
| Command line vs MCP | Both generated from AppWorld's API documentation, so they carry the same names, descriptions and errors and differ only in how they reach the agent | The tools people already use (the shell, `psql`) against the published MCP server for the same service | — | — |
| So a difference means | The way tools reach the agent matters, including what a large tool list costs in context | The real CLI beats or trails the real MCP server, tool quality included | The agent loop matters | The database tool, or the agent around it, finds and queries the right data |
| Cases | 417 in `test_challenge` | 71 that run without accounts | 25 (20 hard, 5 easy) | 104 (`bird-small`), 1,028 (`bird-small-full`) |
| Task text | Distributed encrypted; this repository has task ids only | Public on GitHub with the verification scripts; this repository has task ids only | Public; reference answers held privately | Public, with the databases |
| Graded on | The apps' database state, including changes nobody asked for | The final files or tables, by MCPMark's scripts | The final answer | The query's result rows, by execution |

AppWorld is the closer match to an agent working across someone's accounts and
apps. MCPMark is the more direct test of "use the CLI that already exists".

## Now running: harness vs model, with ConnectOnion

> **Status: in setup.** Arms, models and run counts are being agreed with
> [ConnectOnion](https://github.com/openonion/connectonion); nothing is final until
> [PREREGISTRATION.md](PREREGISTRATION.md) is frozen.

**Bigger model or better harness?** Hold the model fixed and change only the
harness, then compare that against holding the harness fixed and changing the
model. Every cell runs the same cases, compared case by case, more than once.

|                | harness A | harness B | harness C | … |
|---|---|---|---|---|
| **model 1** | | | | |
| **model 2** | | | | |

- **Harness effect**: along a row — same model, different harness.
- **Model effect**: down a column — same harness, different model.
- **Interaction**: whether a harness helps one model and not another.

Which benchmarks, cells, models and runs, and the promise that every result is
published whichever way it falls, are in [PREREGISTRATION.md](PREREGISTRATION.md).

## Third-party data

A benchmark built on someone else's dataset follows that dataset's terms.
AppWorld's data may only be redistributed encrypted, so `appworld/` carries task
ids only and each user downloads the data from AppWorld. `mcpmark/` carries task ids only too. `bird/` is the exception: BIRD's license
(CC BY-SA 4.0) allows redistribution, so it carries its questions and eight of its
databases, with the attribution in `bird/ATTRIBUTION.md`. Reference answers stay private.

## Citation

- AppWorld: Trivedi et al., *AppWorld: A Controllable World of Apps and People for
  Benchmarking Interactive Coding Agents*, ACL 2024.
- MCPMark: *MCPMark: A Benchmark for Stress-Testing Realistic and Comprehensive
  MCP Use*, arXiv:2509.24002.
- DABStep: Egg et al., *DABstep: Data Agent Benchmark for Multi-step Reasoning*,
  arXiv:2506.23719.
- BIRD: Li et al., *Can LLM Already Serve as A Database Interface? A BIg Bench for
  Large-Scale Database Grounded Text-to-SQLs*, NeurIPS 2023.
