---
name: pm-vendor-procurement-management
description: "IT Project Manager skill for Coordinating vendor selection, contract negotiation, SOWs, and third-party onboarding when applicable. Use when: (1) PM assigns task PM-REQ-005 via TaskTriggered event, (2) Requirements phase vendor & procurement management activities are needed, (3) orchestrating vendor & procurement management deliverables for downstream team tasks."
---

# PM Vendor & Procurement Management

Role: IT Project Manager | Task ID: PM-REQ-005 | Wave: 1, Step: 5

## Objective

Coordinating vendor selection, contract negotiation, SOWs, and third-party onboarding when applicable.

## Upstream Inputs

- **User / Organization**: Project initiation request and strategic objectives
- **Previous PM phase outputs**: Completed Requirements prerequisites

## Downstream Triggers

On TaskCompleted (after supervisor 100% pass):
- IPM-REQ-001, IPM-REQ-002, IPM-REQ-003, IPM-REQ-004, IPM-REQ-005

## Workflow (Phase 0-5)

### Phase 0: Initialization

1. Create output directory: `~/.openclaw/workspace-pm/outputs/PM-REQ-005/`
2. Initialize logs: `conversation-log.md`, `work-log.md`, `question-lists.md`, `research-log.md`
3. Log: `[{timestamp}] Phase 0: Initialization — Status: completed`
4. Before proceeding, read `references/dor.md` to verify all prerequisites
5. Check DoR items — if required items missing, request from PM via event

### Phase 1: Understand Task Purpose

1. Receive the task context from user or upstream task artifacts
2. Analyze and summarize understanding of the **task purpose** (why vendor & procurement management is needed)
3. Present understanding to user and ask for confirmation
4. If user disagrees → re-analyze and present again
5. If user agrees → record confirmation in conversation log, proceed to Phase 2

### Phase 2: Understand the Topic

1. Analyze the topic in depth (who, what, why, when, where, how)
2. Incorporate findings from upstream task artifacts
3. Present topic understanding to user
4. Ask user for confirmation
5. If user disagrees → refine and present again
6. If user agrees → record confirmation, proceed to Phase 3

### Phase 3: Research & Question Generation

1. Research the topic using web search and authoritative knowledge bases
2. **Save all research to `research-log.md`** (tool, query, findings, sources)
3. Analyze industry best practices, benchmarks, and relevant standards
4. Present industry findings to user
5. Generate structured question list based on research gaps
6. **Save question list to `question-lists.md`**
7. Conduct interactive Q&A with user — one question at a time or small groups
8. Iterate until all critical information is gathered
9. **Save each round's questions and answered summaries to `question-lists.md`**
10. Consolidate into validated requirements list
11. Present requirements list to user for final confirmation

### Phase 4: Execute & Produce Deliverables

1. Read `references/output-templates.md` — follow the output template strictly
2. Read `references/dod.md` — ensure all quality gates are addressed
3. Research additional details as needed — **log all research to `research-log.md`**
4. Draft all deliverable sections following the template structure
5. Self-review against DoD checklist
6. Fix any issues found in self-review
7. Save deliverables to output directory

### Phase 5: Completion & Handoff

1. Read `references/dod.md` and verify every criterion
2. Check completeness, deliverable quality, process quality
3. If any critical/high items fail → return to Phase 4 to fix
4. Repeat until all checks pass
5. Save final deliverables
6. Present completion summary to user
7. Invoke supervisor: send SupervisorTriggered event to `pm-vendor-procurement-management-supervisor`
8. If supervisor returns issues → remediate and re-invoke supervisor
9. Once supervisor approves (100% pass) → send TaskCompleted to PM with:
   - Deliverable file path and filename
   - RACI matrix (for triggering downstream tasks)
   - Final inspection report

## Resources

Load these reference files at the indicated times:

- **Before Phase 1**: Read `references/dor.md` to verify all prerequisites
- **During Phase 3**: Read `references/raci.md` for stakeholder roles during elicitation
- **Before Phase 4**: Read `references/output-templates.md` for deliverable structure
- **Before Phase 4**: Read `references/dod.md` to understand quality gates while drafting
- **During Phase 4**: Read `references/sop.md` for detailed step-by-step procedure
- **After Phase 4**: Read `references/dod.md` to run self-check
- **Phase 5**: Run `scripts/verify_dod.py` for automated DoD verification
- **Trigger config**: See `references/triggers.md` for activation conditions

## Logging

Maintain four logs in the output directory throughout execution:

### conversation-log.md
```
### Question #1 — {timestamp}
**Agent**: {question asked}
**User**: {user response}
```

### work-log.md
```
- [{timestamp}] {action_description} — Status: {completed/in-progress/failed}
```

### question-lists.md
```
## Phase {N}: {phase_name} — {timestamp}
### Question List #{seq}
1. {question}
### Answered Summary
- Q1: {answer_summary}
```

### research-log.md
```
## Research #{seq} — {timestamp}
- **Tool**: {web_search / context7 / web_fetch / ...}
- **Query/URL**: {search_query_or_url}
- **Purpose**: {why this research was needed}
- **Key Findings**:
  1. {finding}
- **Source**: {url_or_reference}
```
