# Attribution

This directory contains material from **BIRD** (BIg Bench for LaRge-scale Database Grounded Text-to-SQL Evaluation):
the questions and hints of the BIRD dev set (`birdsql/bird_sql_dev_20251106`, revision
`3c11fb193e5439b338e23677fa0aae11e8b85db9`) and eight of its SQLite databases.

- Authors: Jinyang Li, Binyuan Hui, Ge Qu, Jiaxi Yang, Binhua Li, Bowen Li, Bailin Wang, Bowen Qin,
  Ruiying Geng, Nan Huo, et al. — *Can LLM Already Serve as A Database Interface? A BIg Bench for
  Large-Scale Database Grounded Text-to-SQLs*, NeurIPS 2023. https://bird-bench.github.io/
- License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0),
  https://creativecommons.org/licenses/by-sa/4.0/

Changes made here, released under the same license:
- Only the 8 databases under 100 MB are included (the other 3 wait for `bird-large`).
- `bird-small` is the part of Harbor's 150-question parity subset (seed 42, laude-institute/harbor
  `registry.json` at `5fcf07f5af37eba19db389c7d8916743e4591ff5`) that falls on those 8 databases.
- Each question is reworded into a case statement: the original question and hint, the database
  file name, and the answer format. The reference SQL is not included here.

The databases were assembled by the BIRD authors from public sources; those sources' own terms
may also apply.
