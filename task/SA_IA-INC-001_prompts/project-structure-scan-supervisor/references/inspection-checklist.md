# Project Structure Scan — Inspection Checklist

This checklist defines all 22 verification items used by the supervisor to inspect the output of the Project Structure Scan Agent (SA-DISC-001).

## Checklist

| Check ID | Category | Check Item | Verification Method | Pass Criteria |
|----------|----------|------------|---------------------|---------------|
| CHK-01 | Configuration | Trigger config exists with sufficient triggers | Read trigger config file; count trigger definitions | File exists AND contains >= 3 trigger entries |
| CHK-02 | RACI | RACI matrix with roles and tasks | Parse RACI table; count distinct role columns | RACI table present AND >= 6 distinct roles listed |
| CHK-03 | Capabilities | Skills list completeness | Parse skills section; count listed skills | >= 9 skills listed as bullet points or table rows |
| CHK-04 | Knowledge | Knowledge base items | Parse knowledge base section; count items | >= 7 knowledge base items documented |
| CHK-05 | Tools | Tools list completeness | Parse tools section; count listed tools | >= 5 tools listed |
| CHK-06 | Tools | MCP tools listed | Parse MCP tools section; count entries | >= 3 MCP tools listed |
| CHK-07 | Templates | All 6 template files exist and are non-trivial | os.path.exists() for each; os.path.getsize() | All 6 template files exist AND each is > 100 bytes |
| CHK-08 | SOP | SOP defines 5 phases with sub-steps | Parse SOP document; search for phase headers and sub-step markers | 5 distinct phases found, each with >= 1 sub-step |
| CHK-09 | Quality | Definition of Done (DoD) has sufficient items | Parse DoD section; count checkable items (lines with `[ ]` or `[x]`) | >= 12 checkable items present |
| CHK-10 | Quality | Definition of Ready (DoR) has sufficient prerequisites | Parse DoR section; count prerequisite items | >= 8 prerequisite items present |
| CHK-11 | Logging | Conversation log covers Phase 1-3 | Read conversation log; search for Phase 1, Phase 2, Phase 3 markers | Entries for Phase 1, Phase 2, and Phase 3 all present |
| CHK-12 | Logging | Work log has timestamped entries | Read work log; search for timestamp pattern `[YYYY-MM-DD` | >= 1 timestamped entry found |
| CHK-13 | Quality | DoD self-verification passed | Query SQLite agent_memory.db table dod_checks | All rows in dod_checks have status = 'passed' |
| CHK-14 | Output | OUT-01 file directory tree | os.path.exists(); read contents; search for placeholder patterns | File exists AND size > 0 AND no `{project_name}`, `{date}`, `{session_id}` placeholders |
| CHK-15 | Output | OUT-02 visual diagram with Mermaid | os.path.exists(); search for ` ```mermaid ` block | File exists AND contains a ` ```mermaid ` code block |
| CHK-16 | Output | OUT-03 pattern identification | os.path.exists(); search for pattern entries | File exists AND >= 1 pattern identified (non-empty pattern section) |
| CHK-17 | Output | OUT-04 dependency analysis | os.path.exists(); search for "internal" and "third-party" sections | File exists AND covers both internal and third-party dependencies |
| CHK-18 | Output | OUT-05 module descriptions | os.path.exists(); verify all listed modules have description text | File exists AND all modules have non-empty descriptions |
| CHK-19 | Output | OUT-06 executive summary report | os.path.exists(); os.path.getsize(); search for "executive summary" header | File exists AND > 500 bytes AND contains executive summary section |
| CHK-20 | Memory | SQLite database has entries | os.path.exists() for agent_memory.db; query for row count | agent_memory.db exists AND total row count across tables > 0 |
| CHK-21 | Research | Research directory has artifacts | os.listdir() on research/ directory | research/ directory exists AND contains >= 1 file |
| CHK-22 | Dialogue | Phase question files exist | os.path.exists() for both files | phase1-questions.md AND phase3-questions.md both exist |

## Usage

This checklist is consumed by `scripts/run_inspection.py` to perform automated verification. Each check maps to a function in the inspection script.

**Severity levels:**

- All 22 checks are **required** for a 100% pass. There are no optional checks.
- Failure of any single check triggers a remediation cycle.
- After 3 remediation rounds with remaining failures, the supervisor escalates.
