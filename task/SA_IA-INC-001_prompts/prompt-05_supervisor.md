# Prompt 05 — Supervisor AI Agent Skill

## Context

You are continuing the creation of the **Project Structure Scan** AI Agent Skill (Task ID: SA-DISC-001). This is Step 5 of 5 (final step). Steps 1-4 have completed the main skill. This step creates the **independent Supervisor Skill**.

## Scope — Requirements 14 and 15

This prompt covers:
- Requirement 14: Supervisor AI Agent Skill (full quality inspection + closed-loop remediation)
- Requirement 15: PM Agent notification on completion

## Pre-requisites

Verify the main skill is complete before proceeding:
- `project-structure-scan/SKILL.md` (fully populated)
- `project-structure-scan/config/` (5 files)
- `project-structure-scan/templates/` (6 files)
- `project-structure-scan/references/` (4 files)
- `project-structure-scan/scripts/` (init_memory.py, memory_ops.py, verify_dod.py)
- `project-structure-scan/memory/index.md`
- `project-structure-scan/logs/` (2 template files)

If any are missing, STOP and report the issue.

## Instructions

### 1. Create Supervisor Skill Directory

Create `project-structure-scan-supervisor/` as a **separate, independent skill directory** (sibling to `project-structure-scan/`, NOT inside it):

```
project-structure-scan-supervisor/
├── SKILL.md
├── scripts/
│   └── inspect.py
├── references/
│   └── inspection-checklist.md
└── templates/
    └── inspection-report-template.md
```

### 2. Create SKILL.md for Supervisor

**Frontmatter**:
```yaml
---
name: project-structure-scan-supervisor
description: "Independent quality supervisor for the Project Structure Scan Agent (SA-DISC-001). Use when: (1) the Project Structure Scan Agent completes a round of output and quality inspection is needed, (2) verifying all 13 requirements of the Project Structure Scan have been fulfilled, (3) performing closed-loop remediation — sending failed items back for fix and re-inspecting until 100% pass, or (4) generating the final inspection report for PM Agent handoff."
---
```

**Body** — must include all of the following sections:

**## Role Definition**
- Skill Name: `project-structure-scan-supervisor`
- Role: Quality Supervisor — independent from the scan agent
- Does NOT participate in scanning — only inspects and provides feedback
- Trigger: automatically invoked after Project Structure Scan Agent completes output

**## Inspection Scope**

The supervisor inspects execution of Requirements 1 through 13 item by item:

| Check ID | Check Item | What to Verify |
|----------|------------|---------------|
| CHK-01 | Trigger Configuration | `config/triggers.md` exists, contains at least 3 trigger definitions |
| CHK-02 | RACI Matrix | `config/raci.md` exists, contains role names AND task names, at least 6 roles |
| CHK-03 | Skills List | `config/skills-and-knowledge.md` exists, skills section has 9+ items |
| CHK-04 | Knowledge Base | `config/skills-and-knowledge.md` exists, knowledge section has 7+ items |
| CHK-05 | Tools List | `config/tools.md` exists, at least 5 tools defined |
| CHK-06 | MCP Tools List | `config/mcp-tools.md` exists, at least 3 MCP tools defined |
| CHK-07 | Output Templates | All 6 template files exist in `templates/`, each > 100 bytes |
| CHK-08 | SOP Process | `references/sop.md` exists, defines 5 phases with sub-steps |
| CHK-09 | DoD Quality Gates | `references/dod.md` exists, at least 12 checkable items |
| CHK-10 | DoR Prerequisites | `references/dor.md` exists, at least 8 prerequisites |
| CHK-11 | Conversation Log | `logs/conversation-log.md` exists, contains Phase 1-3 dialogue entries |
| CHK-12 | Work Log | `logs/work-log.md` exists, contains timestamped action entries |
| CHK-13 | DoD Self-Verification | `scripts/verify_dod.py` has been run, all checks pass (query `dod_checks` table) |
| CHK-14 | OUT-01 Structure Tree | Output file exists, non-empty, no remaining placeholders |
| CHK-15 | OUT-02 Module Diagram | Output file exists, valid Mermaid diagram present |
| CHK-16 | OUT-03 Layering Analysis | Output file exists, at least one pattern identified |
| CHK-17 | OUT-04 Dependency Map | Output file exists, covers internal + third-party |
| CHK-18 | OUT-05 Module Summary | Output file exists, all modules have descriptions |
| CHK-19 | OUT-06 Final Report | Output file exists, > 500 bytes, executive summary present |
| CHK-20 | Memory Database | `memory/agent_memory.db` exists, has entries in task_memory and scan_history |
| CHK-21 | Research Artifacts | `research/` directory has at least 1 file |
| CHK-22 | Phase Questions | At least `phase1-questions.md` and `phase3-questions.md` exist |

**## Inspection Process (Closed-Loop)**

```
[Trigger] Project Structure Scan Agent signals completion
     ↓
[Load] Read inspection checklist from references/inspection-checklist.md
     ↓
[Execute] Run scripts/inspect.py against the output directory
     ↓
[Generate] Produce inspection report from templates/inspection-report-template.md
     ↓
[Decide] Pass rate = 100%?
     ├── NO → Send report to Project Structure Scan Agent with:
     │         - List of failed items
     │         - Specific remediation instructions per item
     │         - Request to fix and signal re-inspection
     │         → Wait for scan agent to signal completion again
     │         → Re-run inspection (increment round counter)
     │         → Repeat until 100% or max 3 rounds
     └── YES → Proceed to PM Notification
```

If 3 rounds fail, STOP and escalate to user with full report.

**## PM Agent Notification (Requirement 15)**

When pass rate = 100%:
1. Generate final inspection report (marked "ALL PASSED")
2. Call Project Manager AI Agent with:
   - **Deliverables path**: path to `project-structure-scan/` directory
   - **Deliverable file list**: OUT-01 through OUT-06 file names and paths
   - **RACI matrix**: path to `config/raci.md` (PM uses this to trigger downstream tasks)
   - **Final inspection report**: path to the generated report
   - **Scan summary**: project name, scan scope, total modules found, primary pattern identified
3. PM Agent uses the RACI matrix to trigger downstream tasks:
   - Step 1.2: Technology Stack Inventory
   - Step 1.3: Entry-Point Tracing
   - Step 1.4: Data Model Analysis
   - Step 1.5: Configuration & Environments
   - Step 2: Architecture Recovery (once all Step 1.x complete)

**## Logging**
- The supervisor records its own inspection actions in a work log
- Each inspection round is recorded with timestamp and results

### 3. Create scripts/inspect.py

Create the inspection script. Requirements:

**Inputs** (command line arguments):
- `--output-dir`: Path to the `project-structure-scan/` output directory
- `--report-dir`: Path to write the inspection report (default: current directory)
- `--round`: Inspection round number (default: 1)

**Behavior**:
1. Load the inspection checklist (CHK-01 through CHK-22)
2. For each check item, perform an automated verification:
   - File existence checks: `os.path.exists()` + `os.path.getsize()`
   - Content checks: Read file, search for required patterns (section headers, table rows, Mermaid blocks)
   - Placeholder checks: Search for `{project_name}`, `{date}`, `{session_id}`, `{timestamp}` etc.
   - SQLite checks: Query `memory/agent_memory.db` for expected records
   - Count checks: Count items in tables, list entries, section headers
3. Generate a structured report using the template
4. Print summary to stdout
5. Write full report to `{report-dir}/inspection-report-round-{N}.md`
6. Exit code 0 if all pass, exit code 1 if any fail

**Error handling**: If a file/DB cannot be accessed, mark as 'fail' with error details.

### 4. Create references/inspection-checklist.md

A structured checklist that `inspect.py` reads:

```markdown
# Inspection Checklist — Project Structure Scan Supervisor

| Check ID | Category | Check Item | Verification Method | Pass Criteria |
|----------|----------|------------|-------------------|---------------|
| CHK-01 | Config | Trigger configuration file | File exists + content check | File > 50 bytes, contains "Trigger" |
| CHK-02 | Config | RACI matrix file | File exists + content check | Contains at least 6 role rows |
| ... | ... | ... | ... | ... |
```

Include all 22 check items with specific, machine-checkable pass criteria.

### 5. Create templates/inspection-report-template.md

```markdown
# Project Structure Scan — Supervisor Inspection Report

- **Inspection Time**: {timestamp}
- **Inspection Round**: Round {N}
- **Output Directory**: {output_directory_path}
- **Inspector**: project-structure-scan-supervisor

## Inspection Results

| Check ID | Category | Check Item | Status | Evidence / Notes |
|----------|----------|------------|:------:|-----------------|
| CHK-01 | Config | Trigger configuration | ✅ / ❌ | {notes} |
| CHK-02 | Config | RACI matrix | ✅ / ❌ | {notes} |
| CHK-03 | Config | Skills list | ✅ / ❌ | {notes} |
| CHK-04 | Config | Knowledge base | ✅ / ❌ | {notes} |
| CHK-05 | Config | Tools list | ✅ / ❌ | {notes} |
| CHK-06 | Config | MCP tools list | ✅ / ❌ | {notes} |
| CHK-07 | Templates | Output templates (6) | ✅ / ❌ | {notes} |
| CHK-08 | References | SOP process | ✅ / ❌ | {notes} |
| CHK-09 | References | DoD quality gates | ✅ / ❌ | {notes} |
| CHK-10 | References | DoR prerequisites | ✅ / ❌ | {notes} |
| CHK-11 | Logs | Conversation log | ✅ / ❌ | {notes} |
| CHK-12 | Logs | Work log | ✅ / ❌ | {notes} |
| CHK-13 | Verification | DoD self-check passed | ✅ / ❌ | {notes} |
| CHK-14 | Deliverables | OUT-01 Structure Tree | ✅ / ❌ | {notes} |
| CHK-15 | Deliverables | OUT-02 Module Diagram | ✅ / ❌ | {notes} |
| CHK-16 | Deliverables | OUT-03 Layering Analysis | ✅ / ❌ | {notes} |
| CHK-17 | Deliverables | OUT-04 Dependency Map | ✅ / ❌ | {notes} |
| CHK-18 | Deliverables | OUT-05 Module Summary | ✅ / ❌ | {notes} |
| CHK-19 | Deliverables | OUT-06 Final Report | ✅ / ❌ | {notes} |
| CHK-20 | Memory | SQLite database | ✅ / ❌ | {notes} |
| CHK-21 | Research | Research artifacts | ✅ / ❌ | {notes} |
| CHK-22 | Questions | Phase question files | ✅ / ❌ | {notes} |

## Summary

- **Total Checks**: 22
- **Passed**: {passed_count}
- **Failed**: {failed_count}
- **Pass Rate**: {pass_rate}%

## Failed Items — Remediation Required

| # | Check ID | Issue | Remediation Instruction |
|---|----------|-------|------------------------|
| 1 | {check_id} | {what failed} | {specific action to fix} |
| ... | ... | ... | ... |

## Conclusion

{One of:}
- **ALL PASSED** ✅ — Ready for PM Agent handoff. Deliverables path: {path}
- **NEEDS REMEDIATION** ❌ — {failed_count} items require fixing. Returning to scan agent for Round {N+1}.
- **ESCALATED** ⚠️ — Failed after 3 rounds. Escalating to user for manual review.
```

## Validation Checklist

After completing all files, verify:
- [ ] `project-structure-scan-supervisor/` exists as a separate directory (sibling, not child)
- [ ] `project-structure-scan-supervisor/SKILL.md` has valid frontmatter (name + description)
- [ ] `project-structure-scan-supervisor/SKILL.md` body contains: Role Definition, Inspection Scope (22 items), Inspection Process, PM Notification, Logging
- [ ] `project-structure-scan-supervisor/scripts/inspect.py` exists and runs without import errors
- [ ] `inspect.py` accepts `--output-dir`, `--report-dir`, `--round` arguments
- [ ] `inspect.py` performs 22 automated checks
- [ ] `project-structure-scan-supervisor/references/inspection-checklist.md` exists with 22 rows
- [ ] `project-structure-scan-supervisor/templates/inspection-report-template.md` exists with 22 check rows
- [ ] PM notification section specifies exactly what data to send and which downstream tasks to trigger

If any item fails, fix it before reporting completion.
