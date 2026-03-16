# Definition of Done (DoD) — Transformation Target Current State Analysis (SA-TRF-001)

> Quality gates that MUST pass before the analysis is considered complete.
> All checks must pass. Any failure triggers remediation and re-check.

---

## DoD Checklist

| Check ID | Check Item | Verification Method | Pass Criteria |
|----------|-----------|---------------------|---------------|
| DoD-01 | OUT-01 (Code Structure Map) produced and non-empty | File existence + size check | File exists at output path, size > 0 bytes |
| DoD-02 | OUT-02 (Responsibility & Behavior Analysis) produced and non-empty | File existence + size check | File exists at output path, size > 0 bytes |
| DoD-03 | OUT-03 (Dependency Map) produced and non-empty | File existence + size check | File exists at output path, size > 0 bytes |
| DoD-04 | OUT-04 (Data Flow & Interface Analysis) produced and non-empty | File existence + size check | File exists at output path, size > 0 bytes |
| DoD-05 | OUT-05 (Test Coverage Assessment) produced and non-empty | File existence + size check | File exists at output path, size > 0 bytes |
| DoD-06 | OUT-06 (Technical Debt & Risk Register) produced and non-empty | File existence + size check | File exists at output path, size > 0 bytes |
| DoD-07 | OUT-07 (Current State Report) produced and substantial | File existence + size check | File exists at output path, size > 1000 bytes |
| DoD-08 | All templates fully populated | Regex scan for `{placeholder}` | Zero matches for pattern `\{[a-zA-Z_]+\}` across all output files |
| DoD-09 | OUT-07 confirmed by user | User interaction record | Conversation log contains explicit user confirmation of OUT-07 |
| DoD-10 | OUT-03 covers both inbound AND outbound dependencies | Content inspection | OUT-03 contains at least one inbound entry AND at least one outbound entry (or explicit "no inbound callers" statement) |
| DoD-11 | OUT-05 includes coverage assessment with level rating | Content inspection | OUT-05 contains coverage level (`High`/`Medium`/`Low`/`None`) for at least unit tests |
| DoD-12 | OUT-06 includes at least one identified debt or risk item (or explicit "no issues found" statement) | Content inspection | OUT-06 has at least one row in risk table OR explicit "no debt identified" statement |
| DoD-13 | OUT-07 includes hard constraints section | Content inspection | OUT-07 contains "Hard Constraints" section with at least one entry or "no hard constraints" |
| DoD-14 | Conversation log contains all phase dialogue entries | File content inspection | `logs/conversation-log.md` contains entries for Step 0 through Step 4 |
| DoD-15 | Work log contains timestamped entries for all steps | File content inspection | `logs/work-log.md` contains timestamped entries referencing Step 0 through Step 5 |
| DoD-16 | All findings recorded in SQLite memory database | SQL query | `SELECT COUNT(*) FROM task_memory WHERE session_id = ?` > 0 |
| DoD-17 | Analysis history recorded in SQLite | SQL query | Exactly one `analysis_history` row with `status = 'completed'` for this session |
| DoD-18 | Phase question files exist | File existence check | `phase1-questions.md`, `phase2-questions.md`, `phase3-questions.md` all exist |
| DoD-19 | Research artifacts saved | Directory check | `research/` directory contains at least 1 file |
| DoD-20 | RACI matrix ready for PM Agent handoff | File existence check | `config/raci.md` exists with downstream task entries |

---

## Verification Process

1. **Self-Check (Step 5)**: Agent runs `scripts/verify_dod.py` after producing all deliverables. Any failure triggers remediation loop.
2. **Supervisor Check**: Supervisor agent independently re-runs all checks.
3. **Final Verdict**: Analysis is marked `completed` only when both self-check and supervisor report 20/20 passes.

## Failure Handling

| Check(s) | Failure Action |
|----------|---------------|
| DoD-01 through DoD-07 | Re-execute the corresponding deliverable production step |
| DoD-08 | Identify remaining placeholders and populate with actual data |
| DoD-09 | Present OUT-07 summary to user and collect explicit confirmation |
| DoD-10 | Re-run inbound/outbound dependency analysis (Grep for callers, Read imports) |
| DoD-11 | Locate test files and add coverage level assessment |
| DoD-12 | Re-run debt identification (Grep for TODO/FIXME/HACK, code smell analysis) |
| DoD-13 | Add hard constraints section from Phase 4 constraint identification |
| DoD-14, DoD-15 | Reconstruct missing log entries from SQLite memory records |
| DoD-16, DoD-17 | Execute missing memory operations to populate database |
| DoD-18 | Reconstruct phase question files from conversation log |
| DoD-19 | Save research tool outputs and findings to `research/` |
| DoD-20 | Verify `config/raci.md` is complete with downstream task entries |
