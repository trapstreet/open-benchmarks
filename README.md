# open-benchmarks

Benchmarks maintained in the open, together with the people who run on them, and
scored on [trapstreet.run](https://trapstreet.run).

Two kinds of directory:

- **Benchmarks** (top level) — a case list, a judge, and whatever environment the
  cases need. A benchmark is not tied to any one study and can be reused.
- **Studies** ([`studies/`](studies/)) — a question asked of one or more
  benchmarks: which arms, which cells, how many runs, what gets published. Each
  study fixes its rules in a preregistration before the first paid run.

Solutions are not here. Each arm lives in its owner's repository and is submitted
with `tp run`; the board links every row to the exact commit it ran.

## Benchmarks

| Directory | Source | Graded on |
|---|---|---|
| [`appworld/`](appworld/) | [AppWorld](https://github.com/StonyBrookNLP/appworld) — nine simulated everyday apps, 457 APIs | The apps' database state after the task |
| [`dabstep/`](dabstep/) | [DABStep](https://huggingface.co/datasets/adyen/DABstep) — data-analysis questions over a payments dataset | The final answer (held privately) |

## Studies

| Study | Question | With |
|---|---|---|
| [`harness-vs-model`](studies/harness-vs-model/) | Hold the model fixed and change the harness, compared with holding the harness fixed and changing the model | [ConnectOnion](https://github.com/openonion/connectonion) |

## Third-party data

A benchmark built on someone else's dataset follows that dataset's terms. AppWorld's
data may only be redistributed encrypted, so `appworld/` carries task ids only and
each user downloads the data from AppWorld.
