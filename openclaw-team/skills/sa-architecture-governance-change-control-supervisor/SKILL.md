---
name: sa-architecture-governance-change-control-supervisor
description: "Supervisor inspection skill for sa-architecture-governance-change-control. Use when: (1) SA agent completes self-check for task IA-REL-009, (2) SupervisorTriggered event received from sa-architecture-governance-change-control skill, (3) quality gate verification needed before TaskCompleted is sent to PM."
---

# SA Architecture Governance & Change Control — Supervisor

Role: System Architect Supervisor | Task ID: IA-REL-009 | Inspection Agent

## Inspection Scope

Independent quality review of the Architecture Governance & Change Control output for task IA-REL-009. This supervisor:
- Operates independently from the SA Architecture Governance & Change Control agent
- Reviews only — never modifies deliverables directly
- Must achieve 100% pass rate before TaskCompleted can be sent to PM

## Trigger

Activated when the SA Architecture Governance & Change Control agent sends SupervisorTriggered event with:
- Deliverable file path
- Output directory (containing conversation-log.md, work-log.md, question-lists.md, research-log.md)
- Skill directory path (containing references/)

## Inspection Checklist

### Infrastructure Checks (INS-01 through INS-08)

| ID | Check Item | Severity |
|----|-----------|----------|
| INS-01 | references/triggers.md exists and properly structured | Critical |
| INS-02 | references/raci.md exists with roles AND task assignments | Critical |
| INS-03 | references/output-templates.md exists with deliverable template | Critical |
| INS-04 | references/sop.md exists with complete Phase 0-5 workflow | Critical |
| INS-05 | references/dod.md exists with quality gate definitions | Critical |
| INS-06 | references/dor.md exists with prerequisite definitions | Critical |
| INS-07 | conversation-log.md exists with numbered user interactions | Critical |
| INS-08 | work-log.md exists with timestamped agent actions | Critical |

### Process Checks (INS-09 through INS-12)

| ID | Check Item | Severity |
|----|-----------|----------|
| INS-09 | DoD verification was performed and all critical/high items passed | Critical |
| INS-10 | question-lists.md exists with phase-labeled sections and answered summaries | Critical |
| INS-11 | research-log.md exists with tool, query, findings, source for each entry | Critical |
| INS-12 | User confirmation obtained for task purpose and topic understanding | Critical |

### Deliverable Quality Checks (INS-DQ-01 through INS-DQ-05)

| ID | Check Item | Severity |
|----|-----------|----------|
| INS-DQ-01 | All required deliverable sections present and populated | Critical |
| INS-DQ-02 | No TBD, TODO, or placeholder text in final deliverable | Critical |
| INS-DQ-03 | Deliverable follows output template structure | High |
| INS-DQ-04 | All acceptance criteria are testable and measurable | High |
| INS-DQ-05 | Upstream traceability — inputs referenced and decisions traceable | High |

## Inspection Process

```
[Trigger] SA Architecture Governance & Change Control agent sends SupervisorTriggered
     |
     v
[Load] Read references/inspection-criteria.md for detailed verification rules
     |
     v
[Check] Inspect each item INS-01 through INS-12 + INS-DQ-01 through INS-DQ-05
     |
     v
[Report] Generate inspection report (format below)
     |
     v
[Decide] Pass rate = 100%?
     |-- No  -> Return report to SA agent for remediation
     |          Agent fixes and re-sends SupervisorTriggered
     |          Repeat until 100% pass
     |-- Yes -> Notify PM Agent with completion package
```

## Inspection Report Format

```markdown
# SA Architecture Governance & Change Control Supervisor Inspection Report

- Inspection Time: {timestamp}
- Inspection Round: #{N}
- Deliverable File Path: {file_path}

## Inspection Results

| Check Item | Status | Notes |
|:-----------|:------:|:------|
| INS-01: Triggers Config | PASS/FAIL | {notes} |
| INS-02: RACI Matrix | PASS/FAIL | {notes} |
| INS-03: Output Template | PASS/FAIL | {notes} |
| INS-04: SOP Process | PASS/FAIL | {notes} |
| INS-05: DoD Checklist | PASS/FAIL | {notes} |
| INS-06: DoR Checklist | PASS/FAIL | {notes} |
| INS-07: Conversation Log | PASS/FAIL | {notes} |
| INS-08: Work Log | PASS/FAIL | {notes} |
| INS-09: DoD Verification Passed | PASS/FAIL | {notes} |
| INS-10: Question Lists Log | PASS/FAIL | {notes} |
| INS-11: Research Log | PASS/FAIL | {notes} |
| INS-12: User Confirmation | PASS/FAIL | {notes} |
| INS-DQ-01: Deliverable Complete | PASS/FAIL | {notes} |
| INS-DQ-02: No Unresolved TBDs | PASS/FAIL | {notes} |
| INS-DQ-03: Template Followed | PASS/FAIL | {notes} |
| INS-DQ-04: Acceptance Criteria | PASS/FAIL | {notes} |
| INS-DQ-05: Upstream Traceability | PASS/FAIL | {notes} |

## Overall Pass Rate: {X}% ({M}/17 items passed)

## Issues Requiring Remediation
1. {issue_description} — Suggested fix: {suggestion}

## Conclusion: [FAIL -> Return to SA Agent | PASS -> Notify PM Agent]
```

## On 100% Pass

1. Generate final report marked "ALL PASSED"
2. Notify **PM Agent** with:
   - Deliverable file path
   - RACI matrix configuration (for triggering downstream tasks)
   - Final inspection report

## Resources

- Inspection criteria details: see `references/inspection-criteria.md`
