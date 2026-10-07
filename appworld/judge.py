"""Per-case judge for appworld. Not written yet.

Contract (see README.md):
- stdout of the solution is one JSON object {"task_id", "dbs": {"<app>.jsonl": str}}.
- Shape check first: task_id equals the case's; only AppWorld's app names; rows
  parse as JSON; total size capped. Anything else scores 0 and is never handed
  to AppWorld.
- Then rebuild experiments/outputs/<run>/tasks/<task_id>/dbs under the job's own
  work directory and run AppWorld's evaluation offline against appworld-root.
- Print one JSON line: score (1.0 iff every test passes), passes, failures,
  scenario id for the grader's scenario completion.
"""
raise SystemExit("judge.py: not implemented yet")
