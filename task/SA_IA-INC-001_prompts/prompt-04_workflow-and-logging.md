# Prompt 04 — Interactive Workflow, Logging & DoD Verification

## Context

You are continuing the creation of the **Project Structure Scan** AI Agent Skill (Task ID: SA-DISC-001). This is Step 4 of 5. Steps 1-3 have created the directory structure, config files, templates, SOP, DoD/DoR, memory architecture, and memory scripts.

## Scope — Requirements 11, 12, 13, 16, 17

This prompt covers:
- Requirement 11: Conversation log recording
- Requirement 12: Work log recording
- Requirement 13: DoD self-verification and remediation loop
- Requirement 16: Phase question list recording
- Requirement 17: Research process and results recording
- Complete interactive workflow (Phase 0–5) written into SKILL.md

## Pre-requisites

Verify these exist before proceeding:
- `project-structure-scan/SKILL.md` (with skeleton + memory protocol from prompts 01 & 03)
- `project-structure-scan/config/` (5 files)
- `project-structure-scan/templates/` (6 files)
- `project-structure-scan/references/` (sop.md, dod.md, dor.md, output-templates.md)
- `project-structure-scan/scripts/init_memory.py`
- `project-structure-scan/scripts/memory_ops.py`
- `project-structure-scan/memory/index.md`
- `project-structure-scan/logs/` (empty directory)
- `project-structure-scan/research/` (empty directory)
- `project-structure-scan/diagrams/` (empty directory)

If any are missing, STOP and report the issue.

## Instructions

### 1. Create logs/conversation-log.md (template)

```markdown
# Conversation Log — Project Structure Scan (SA-DISC-001)

- **Project**: {project_name}
- **Session ID**: {session_id}
- **Started**: {start_timestamp}

---

## Phase 1: Understand Task Purpose

### Q1: {question_text}
- **Asked by**: Agent / User
- **Timestamp**: {timestamp}
- **Response**: {response_text}
- **Status**: Confirmed / Rejected / Pending

### Q2: ...

---

## Phase 2: Understand Target Project

### Q1: ...

---

## Phase 3: Research & Question Generation

### Q1: ...

---

## Phase 4: Execute & Produce Deliverables

### Observation 1: ...

---

## Session Summary

- **Total Questions Asked**: {count}
- **Total User Confirmations**: {count}
- **Total Rejections/Refinements**: {count}
- **Session Duration**: {duration}
```

### 2. Create logs/work-log.md (template)

```markdown
# Work Log — Project Structure Scan (SA-DISC-001)

- **Project**: {project_name}
- **Session ID**: {session_id}
- **Started**: {start_timestamp}

---

| # | Timestamp | Phase | Action | Details | Status | Memory Op |
|---|-----------|-------|--------|---------|--------|-----------|
| 1 | {ts} | Phase 0 | Verify DoR prerequisites | Checked: codebase access ✅, build files ✅, ... | Done | — |
| 2 | {ts} | Phase 0 | Initialize memory database | Created agent_memory.db, 4 tables | Done | init_memory.py |
| 3 | {ts} | Phase 0 | Load project history | Found {N} previous scans | Done | load_project_history() |
| 4 | {ts} | Phase 1 | Present task purpose understanding | "{understanding}" | Awaiting user confirmation | — |
| 5 | {ts} | Phase 1 | User confirmed task purpose | — | Done | record_decision() |
| ... | ... | ... | ... | ... | ... | ... |

---

## Summary

- **Total Actions**: {count}
- **Phases Completed**: {list}
- **Memory Operations**: {count} reads, {count} writes
- **DoD Checks**: Round {N}, Pass Rate: {rate}%
- **Completed**: {end_timestamp}
```

### 3. Create scripts/verify_dod.py (Requirement 13)

Create a Python script that performs DoD self-verification. Requirements:

**Inputs**:
- Path to the `project-structure-scan/` output directory
- Path to `references/dod.md` (to read the checklist)
- Path to `memory/agent_memory.db` (to record check results)
- Session ID and task ID

**Behavior**:
1. Read the DoD checklist from `references/dod.md`
2. For each DoD item, run an automated check:

| DoD Item | Automated Check |
|----------|----------------|
| OUT-01 exists and non-empty | Check file exists, size > 100 bytes |
| OUT-02 exists and non-empty | Check file exists, size > 100 bytes |
| OUT-03 exists and non-empty | Check file exists, size > 100 bytes |
| OUT-04 exists and non-empty | Check file exists, size > 100 bytes |
| OUT-05 exists and non-empty | Check file exists, size > 100 bytes |
| OUT-06 (final report) exists and non-empty | Check file exists, size > 500 bytes |
| No remaining placeholder fields | Grep for `{project_name}`, `{date}`, `{session_id}` etc. in output files |
| Mermaid diagrams have valid syntax | Check for ` ```mermaid ` blocks, basic syntax validation |
| At least one architecture pattern identified | Grep OUT-03 for "✅ Match" or "Identified Primary Pattern" |
| All modules have responsibility descriptions | Check OUT-05 for "### Module:" sections |
| Both internal and third-party dependencies covered | Check OUT-04 for "Third-Party" and "Internal" sections |
| Circular dependencies flagged (if any) | Check OUT-02 for "Circular Dependencies" section |
| Conversation log has Phase 1-3 dialogue | Check `logs/conversation-log.md` for Phase 1, 2, 3 headers with content |
| Work log has timestamped entries | Check `logs/work-log.md` for table entries |
| Findings recorded in SQLite | Query `task_memory` table, count > 0 |
| Scan history recorded | Query `scan_history` table for this session |
| RACI matrix ready for PM handoff | Check `config/raci.md` exists and non-empty |

3. Record each check result in the `dod_checks` table via `memory_ops.record_dod_check()`
4. Print a summary report:
   ```
   DoD Verification Report — Round {N}
   =====================================
   ✅ PASS: {item} — {evidence}
   ❌ FAIL: {item} — {reason}
   ...
   =====================================
   Overall: {passed}/{total} items passed ({percentage}%)
   Status: ALL PASSED ✅ / NEEDS REMEDIATION ❌
   ```
5. Return exit code 0 if all pass, exit code 1 if any fail

**Error handling**: If a file cannot be read or DB cannot be queried, mark that item as 'fail' with the error as the note.

### 4. Write Complete Workflow into SKILL.md

Replace the skeleton section headers in `project-structure-scan/SKILL.md` with the full interactive workflow. The SKILL.md body (after frontmatter) should now contain:

**## Objective**
- Produce a comprehensive project structure analysis for an existing codebase, covering directory hierarchy, module decomposition, architectural patterns, dependency mapping, and module responsibilities.

**## Upstream Inputs**
- PM Agent task assignment (SA-DISC-001 via RACI matrix)
- Target project path (collected via Project Intake if not provided)
- Git repository URL and branch (optional, collected via Project Intake)
- Scan purpose description (collected via Project Intake if not provided)
- Scan scope (full / partial / specific modules, collected via Project Intake)

**## Downstream Triggers**
- Upon completion, PM Agent triggers: Step 1.2 (Technology Stack Inventory), Step 1.3 (Entry-Point Tracing), Step 2 (Architecture Recovery)

**## Workflow Overview**
```
Phase 0: Initialization & Project Intake
  → Verify DoR → **collect project info (path/git/scope/purpose)** → user confirms intake → create output dir → init memory DB → load history → determine scan mode

Phase 1: Understand Task Purpose (Interactive + Memory-Enhanced)
  → Load previous purpose if exists → present understanding → user confirms → log

Phase 2: Understand Target Project (Interactive + Memory-Accelerated)
  → Load known tech stack if exists → pre-fill answers → ask delta questions → user confirms → log

Phase 3: Research & Question Generation (Interactive + Memory-Informed)
  → Load previous research if exists → skip known areas → focus on gaps → generate questions → dialogue → validated requirements

Phase 4: Execute & Produce Deliverables (Memory-Optimized)
  → Determine scan strategy (full/incremental) → scan codebase → produce OUT-01~06 → record findings → DoD self-verify

Phase 5: Completion & Handoff
  → Trigger supervisor → remediate if needed → record lessons → notify PM → trigger downstream
```

**## Phase 0: Initialization & Project Intake** (detailed sub-steps with memory ops)

This phase has two parts:

**Part A — Project Intake (Interactive)**:
1. Check if project info was provided via trigger parameters.
2. For each missing required item, ask the user interactively (see `config/triggers.md` Section 2.1 for the full intake checklist):
   - Project local path (REQUIRED) — validate with `ls {path}`
   - Git repository URL (OPTIONAL) — validate with `git -C {path} status`
   - Git branch (OPTIONAL) — validate branch exists
   - Project name (REQUIRED) — can infer from directory name
   - Scan scope (REQUIRED) — full / partial / exclude-list
   - Directories to exclude (CONDITIONAL) — only if partial/exclude
   - Scan purpose (REQUIRED) — why this scan is needed
3. Present **Project Intake Summary** to user for confirmation.
4. If user rejects → re-ask corrected items. If user confirms → proceed.
5. Memory ops: call `memory_ops.start_scan()` to record in `scan_history`.
6. Memory ops: call `memory_ops.record_knowledge()` to store project info for future re-invocations.

**Part B — System Initialization**:

**## Phase 1: Understand Task Purpose** (detailed with memory-enhanced behavior)

**## Phase 2: Understand the Target Project** (detailed with memory-accelerated behavior)

**## Phase 3: Research & Question Generation** (detailed with memory-informed behavior)

**## Phase 4: Execute & Produce Deliverables** (detailed with memory-optimized behavior, tool usage instructions, output production steps)

**## Phase 5: Completion & Handoff** (supervisor trigger, PM notification, downstream triggers)

**## Logging Requirements**
- Conversation log: every user interaction in `logs/conversation-log.md`
- Work log: every action with timestamp in `logs/work-log.md`
- Phase questions: save question lists in `phase{N}-questions.md`
- Research artifacts: save all research to `research/`

**## Reference Files**
- Link to all config, template, reference, and script files with relative paths

Each phase must specify:
1. What memory queries to run at the start
2. What actions to perform
3. What memory writes to make after each action
4. What the user interaction pattern is
5. What the success criteria are for proceeding

## Validation Checklist

After completing all files, verify:
- [ ] `logs/conversation-log.md` exists with complete template structure
- [ ] `logs/work-log.md` exists with complete template structure (table format)
- [ ] `scripts/verify_dod.py` exists and runs without import errors
- [ ] `scripts/verify_dod.py` checks at least 15 DoD items
- [ ] `SKILL.md` now contains fully populated Phase 0-5 workflow (not just section headers)
- [ ] Each phase in SKILL.md specifies memory read/write operations
- [ ] Each phase in SKILL.md specifies user interaction patterns
- [ ] SKILL.md contains `## Logging Requirements` section
- [ ] SKILL.md contains `## Reference Files` section with valid relative paths
- [ ] `research/` directory exists
- [ ] `diagrams/` directory exists

If any item fails, fix it before reporting completion.
