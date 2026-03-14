# Definition of Done (DoD): Project Structure Scan (SA-DISC-001)

> Quality gates that must pass before a Project Structure Scan is considered complete.
> Each check is independently verifiable. All checks must pass for the scan to be accepted.

---

## DoD Checklist

| Check ID | Check Item | Verification Method | Pass Criteria |
|----------|-----------|---------------------|---------------|
| DoD-01 | OUT-01 (Project Structure Tree) produced and non-empty | File existence check + byte size check | File exists at expected path and size > 0 bytes |
| DoD-02 | OUT-02 (Module Relationship Diagram) produced and non-empty | File existence check + byte size check | File exists at expected path and size > 0 bytes |
| DoD-03 | OUT-03 (Layering Pattern Analysis) produced and non-empty | File existence check + byte size check | File exists at expected path and size > 0 bytes |
| DoD-04 | OUT-04 (Package Dependency Map) produced and non-empty | File existence check + byte size check | File exists at expected path and size > 0 bytes |
| DoD-05 | OUT-05 (Module Responsibility Summary) produced and non-empty | File existence check + byte size check | File exists at expected path and size > 0 bytes |
| DoD-06 | OUT-06 (Project Structure Scan Report) produced and non-empty | File existence check + byte size check | File exists at expected path and size > 500 bytes |
| DoD-07 | All templates fully populated | Regex scan for `{placeholder}` patterns | Zero matches for pattern `\{[a-zA-Z_]+\}` across all 6 output files |
| DoD-08 | Module relationship diagram renders valid Mermaid syntax | Mermaid syntax validation (parse without error) | Mermaid code block parses successfully with no syntax errors |
| DoD-09 | At least one architecture pattern identified with evidence | Content inspection of OUT-03 | OUT-03 contains at least one pattern name and a non-empty evidence section |
| DoD-10 | All identified modules have responsibility descriptions | Cross-reference OUT-01 modules against OUT-05 entries | Every module listed in OUT-01 has a corresponding entry in OUT-05 with a non-empty description |
| DoD-11 | Dependency map covers both internal and third-party dependencies | Content inspection of OUT-04 | OUT-04 contains at least one internal dependency entry AND at least one third-party dependency entry |
| DoD-12 | Circular dependencies flagged if any exist | Dependency graph cycle detection on OUT-04 data | If cycles exist in the dependency graph, they are explicitly listed in OUT-04; if none exist, an explicit "no circular dependencies detected" statement is present |
| DoD-13 | Conversation log contains Phase 1-3 dialogue entries | File content inspection of `logs/conversation-log.md` | Log file contains section headers or entries for Phase 1, Phase 2, and Phase 3 |
| DoD-14 | Work log contains timestamped entries for all phases | File content inspection of `logs/work-log.md` | Log file contains timestamped entries referencing Phase 0 through Phase 5 |
| DoD-15 | All findings recorded in SQLite memory database | SQL query: `SELECT COUNT(*) FROM task_memory` | `task_memory` row count > 0 |
| DoD-16 | Scan history recorded in SQLite | SQL query: `SELECT COUNT(*) FROM scan_history WHERE scan_id = ?` | Exactly one `scan_history` row exists for the current scan ID with status `completed` |
| DoD-17 | RACI matrix ready for PM Agent handoff | File existence and content check | RACI matrix document exists, contains at least one row with R/A/C/I assignments |

---

## Verification Process

1. **Self-Check (Phase 4):** The agent runs all 17 checks after producing deliverables. Any failure triggers a remediation loop back to the relevant production step.
2. **Supervisor Check (Phase 5):** The supervisor independently re-runs all 17 checks. Results are compared against the agent's self-check.
3. **Final Verdict:** The scan is marked `completed` only when both self-check and supervisor check report 17/17 passes.

## Failure Handling

- **DoD-01 through DoD-06 failure:** Re-execute the corresponding deliverable production step (SOP 4-6 through 4-11).
- **DoD-07 failure:** Identify remaining placeholders and populate them with actual data or "N/A" with justification.
- **DoD-08 failure:** Fix Mermaid syntax errors in OUT-02 and re-validate.
- **DoD-09 failure:** Re-run pattern recognition (SOP 4-5) and update OUT-03.
- **DoD-10 failure:** Identify modules missing descriptions and add them to OUT-05.
- **DoD-11 failure:** Re-run dependency analysis (SOP 4-4) and update OUT-04.
- **DoD-12 failure:** Run cycle detection on dependency data and update OUT-04.
- **DoD-13 through DoD-14 failure:** Reconstruct missing log entries from memory DB records.
- **DoD-15 through DoD-16 failure:** Execute missing memory operations to populate the database.
- **DoD-17 failure:** Generate RACI matrix from scan findings and role assignments.
