# Standard Operating Procedure (SOP) — PM-DEV-005 Stakeholder Communication

## Overview

Step-by-step process from receiving the Stakeholder Communication task to delivering complete, supervisor-approved deliverables. Each phase must complete before the next begins.

---

## Phase 0: Initialization

| Step | Action | Output |
|------|--------|--------|
| 0.1 | Create output directory `~/.openclaw/workspace-pm/outputs/PM-DEV-005/` | Directory created |
| 0.2 | Initialize `conversation-log.md`, `work-log.md`, `question-lists.md`, `research-log.md` | Logs initialized |
| 0.3 | Check DoR prerequisites (read `references/dor.md`) | DoR status |
| 0.4 | If required items missing → request from PM | Missing items requested |
| 0.5 | Load upstream artifacts | Artifacts loaded |

---

## Phase 1: Understand Task Purpose

| Step | Action | Output |
|------|--------|--------|
| 1.1 | Receive topic/context from user or upstream artifacts | Raw topic recorded |
| 1.2 | Analyze and summarize understanding of **task purpose** | Task purpose summary |
| 1.3 | Present understanding to user and ask for confirmation | User confirmation |
| 1.4 | If user disagrees → return to 1.2 and re-analyze | Revised understanding |
| 1.5 | If user agrees → proceed to Phase 2 | Confirmed task purpose |

**Log**: Record all exchanges in conversation-log.md.

---

## Phase 2: Understand the Topic

| Step | Action | Output |
|------|--------|--------|
| 2.1 | Analyze topic in depth (who, what, why, when, where, how) | Topic analysis |
| 2.2 | Incorporate upstream findings and context | Enriched analysis |
| 2.3 | Present topic understanding to user | Topic summary |
| 2.4 | Ask user for confirmation | User confirmation |
| 2.5 | If user disagrees → return to 2.1, refine | Revised analysis |
| 2.6 | If user agrees → proceed to Phase 3 | Confirmed topic |

**Log**: Record all exchanges in conversation-log.md.

---

## Phase 3: Research & Question Generation

| Step | Action | Output |
|------|--------|--------|
| 3.1 | Research topic on internet and authoritative knowledge bases | Research findings |
| 3.2 | **Save research to `research-log.md`** (tool, query, findings, sources) | Research log entry |
| 3.3 | Analyze industry best practices, benchmarks, standards | Industry analysis |
| 3.4 | Generate structured question list based on research gaps | Question list |
| 3.5 | **Save question list to `question-lists.md`** | Question list logged |
| 3.6 | Present industry findings and questions to user | Presented findings |
| 3.7 | Conduct interactive Q&A (one at a time or small groups) | Q&A responses |
| 3.8 | Iterate until all critical information gathered | Complete Q&A |
| 3.9 | **Save each round's Q&A to `question-lists.md`** | Updated log |
| 3.10 | Consolidate into validated requirements list | Requirements list |
| 3.11 | Present requirements list to user for confirmation | User confirmation |

**Log**: Record Q&A in conversation-log.md. Record research in research-log.md.

---

## Phase 4: Execute & Produce Deliverables

| Step | Action | Output |
|------|--------|--------|
| 4.1 | Read `references/output-templates.md` | Template loaded |
| 4.2 | Read `references/dod.md` | DoD loaded |
| 4.3 | Research additional details as needed — **log to `research-log.md`** | Supplemental research |
| 4.4 | Draft all deliverable sections following template structure | Draft v0.1 |
| 4.5 | Self-review against DoD checklist | Self-review notes |
| 4.6 | Fix any issues found | Draft v1.0 |
| 4.7 | Save deliverables to output directory | Saved deliverables |

**Log**: Record all actions in work-log.md with timestamps.

---

## Phase 5: Completion & Handoff

| Step | Action | Output |
|------|--------|--------|
| 5.1 | Run DoD verification (check every criterion) | DoD report |
| 5.2 | If critical/high items fail → return to Phase 4 | Fixes applied |
| 5.3 | Repeat 5.1-5.2 until all checks pass | All checks passed |
| 5.4 | Save final deliverables | Final output |
| 5.5 | Generate completion summary | Summary |
| 5.6 | Send SupervisorTriggered to pm-stakeholder-communication-supervisor | Signal sent |
| 5.7 | If supervisor returns issues → fix and re-submit | Fixes applied |
| 5.8 | Once supervisor approves (100%) → send TaskCompleted to PM | PM notified |
| 5.9 | Include deliverable path, RACI matrix, final report in payload | Handoff package |

**Log**: Record handoff actions in work-log.md.
