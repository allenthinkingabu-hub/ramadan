# Inspection Checklist — Transformation Target Supervisor

> Independent DoD check list. These checks mirror the primary agent's `references/dod.md` but are
> implemented independently in `scripts/run_inspection.py`.

---

## Check List (20 items)

| Check ID | Description | Pass Criteria | Failure Action |
|----------|-------------|---------------|----------------|
| DoD-01 | OUT-01 produced and non-empty | File exists, size > 0 bytes | Re-execute Step 4-2 (Code Structure Map) |
| DoD-02 | OUT-02 produced and non-empty | File exists, size > 0 bytes | Re-execute Step 4-3 (Responsibility Analysis) |
| DoD-03 | OUT-03 produced and non-empty | File exists, size > 0 bytes | Re-execute Step 4-4 (Dependency Map) |
| DoD-04 | OUT-04 produced and non-empty | File exists, size > 0 bytes | Re-execute Step 4-5 (Data Flow Analysis) |
| DoD-05 | OUT-05 produced and non-empty | File exists, size > 0 bytes | Re-execute Step 4-6 (Test Coverage Assessment) |
| DoD-06 | OUT-06 produced and non-empty | File exists, size > 0 bytes | Re-execute Step 4-7 (Tech Debt Register) |
| DoD-07 | OUT-07 produced and substantial | File exists, size > 1000 bytes | Re-execute Step 4-9 (Current State Report) |
| DoD-08 | All templates fully populated | Zero `{placeholder}` matches across all output files | Identify and populate all remaining placeholders |
| DoD-09 | OUT-07 confirmed by user | `logs/conversation-log.md` contains explicit user confirmation referencing OUT-07 | Present OUT-07 summary to user, collect explicit confirmation |
| DoD-10 | OUT-03 covers both inbound AND outbound | OUT-03 contains inbound section + outbound section (or explicit "no inbound" statement) | Re-run dependency analysis (Grep callers + Read imports) |
| DoD-11 | OUT-05 has coverage level rating | OUT-05 contains `High`/`Medium`/`Low`/`None` coverage rating for unit tests | Locate test files, add coverage level assessment |
| DoD-12 | OUT-06 has debt/risk item or no-debt statement | OUT-06 has ≥1 row in risk table OR explicit "no debt identified" statement | Re-run debt identification (Grep TODO/FIXME/HACK + code smell analysis) |
| DoD-13 | OUT-07 has Hard Constraints section | OUT-07 contains "Hard Constraints" section with ≥1 entry or "no hard constraints" | Add constraints section from Step 4-8 findings |
| DoD-14 | Conversation log covers Steps 0-4 | `logs/conversation-log.md` has entries referencing Step 0, 1, 2, 3, 4 | Reconstruct missing entries from SQLite task_memory records |
| DoD-15 | Work log has timestamped entries for Steps 0-5 | `logs/work-log.md` has ISO timestamp entries referencing Step 0-5 | Reconstruct from task_memory and analysis_history |
| DoD-16 | Findings in SQLite task_memory | `SELECT COUNT(*) FROM task_memory WHERE session_id = ?` > 0 | Execute missing memory record operations |
| DoD-17 | Analysis history completed in SQLite | Exactly 1 `analysis_history` row with `status = 'completed'` for this session | Run `update_history_status("completed")` |
| DoD-18 | Phase question files exist | `phase1-questions.md`, `phase2-questions.md`, `phase3-questions.md` all exist | Reconstruct from conversation-log.md |
| DoD-19 | research/ directory has ≥1 file | `research/` directory contains at least 1 file | Save research tool outputs to `research/` |
| DoD-20 | config/raci.md ready for PM handoff | `config/raci.md` exists with downstream task entries (SA-TRF-002, SA-TST-001, etc.) | Verify `config/raci.md` is complete |

---

## File Location Conventions

Expected output file names (supervisor looks for these in `output_dir`):

```
OUT-01-code-structure-map.md
OUT-02-responsibility-analysis.md
OUT-03-dependency-map.md
OUT-04-data-flow-analysis.md
OUT-05-test-coverage-report.md
OUT-06-tech-debt-risk-register.md
OUT-07-current-state-report.md
```

If exact names differ, match by `OUT-0N-*` prefix pattern.

---

## Pass Threshold

**Required**: 20/20 checks pass.
**Max rounds**: 3.
**Escalation**: If round 3 still fails, escalate unresolved checks to user.
