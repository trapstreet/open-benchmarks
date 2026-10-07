# harness-vs-model

**Bigger model or better harness?** This repository holds the benchmarks for a
board that answers that with one design: hold the model fixed and change only the
harness, then compare that against holding the harness fixed and changing the
model. Every cell runs the same cases, so the two effects are measured on the same
ground and can be put side by side.

Run with [ConnectOnion](https://github.com/openonion/connectonion) and scored on
[trapstreet.run](https://trapstreet.run).

## What is here

| Directory | Benchmark | What the harness axis means there |
|---|---|---|
| [`appworld/`](../../appworld/) | [AppWorld](https://github.com/StonyBrookNLP/appworld) — nine simulated everyday apps (Gmail, Venmo, Spotify, Todoist, files, …), 457 APIs, graded on the apps' database state | The agent loop, **and** how the tools reach the agent: MCP, a command line, or Python |
| [`dabstep/`](../../dabstep/) | [DABStep](https://huggingface.co/datasets/adyen/DABstep) — data-analysis questions over a payments dataset | The agent loop, with each harness's own tools or with one shared toolbox |

Solutions are not in this repository. Each harness arm lives in its owner's repository and is
submitted with `tp run`; the board links every row to the exact commit it ran.

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
