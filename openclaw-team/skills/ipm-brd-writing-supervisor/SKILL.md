---
name: ipm-brd-writing-supervisor
description: "Supervisor inspection skill for ipm-brd-writing. Use when: (1) IPM agent completes self-check for task IPM-INC-003, (2) SupervisorTriggered event received from ipm-brd-writing skill, (3) quality gate verification needed before TaskCompleted is sent to PM."
---

# IPM BRD Writing — Supervisor

Role: IT Product Manager Supervisor | Task ID: IPM-INC-003 | Inspection Agent

## Inspection Scope

Independent quality review of the BRD Writer output for task IPM-INC-003. This supervisor:
- Operates independently from the IPM BRD Writer agent
- Reviews only — never modifies the BRD directly
- Must achieve 100% pass rate before TaskCompleted can be sent to PM

## Trigger

Activated when the IPM BRD Writer agent sends SupervisorTriggered event with:
- BRD file path
- BRD output directory (containing conversation-log.md, work-log.md, question-lists.md, research-log.md)
- Skill directory path (containing references/)

## Inspection Checklist

### Infrastructure Checks (INS-01 through INS-08)

| ID | Check Item | Severity |
|----|-----------|----------|
| INS-01 | references/triggers.md exists and properly structured | Critical |
| INS-02 | references/raci.md exists with roles AND task assignments | Critical |
| INS-03 | references/output-templates.md exists with all 19 BRD sections | Critical |
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

### BRD Content Quality Checks (INS-BRD-01 through INS-BRD-08)

| ID | Check Item | Severity |
|----|-----------|----------|
| INS-BRD-01 | Executive Summary present and provides meaningful project overview | Critical |
| INS-BRD-02 | Business Objectives in SMART format with success metrics | High |
| INS-BRD-03 | In-scope and out-of-scope items explicitly listed | Critical |
| INS-BRD-04 | Every BR, FR, and NFR has testable acceptance criteria | Critical |
| INS-BRD-05 | All requirements have MoSCoW priority assigned | High |
| INS-BRD-06 | No TBD, TODO, or placeholder text in final document | Critical |
| INS-BRD-07 | Risk register exists with probability, impact, and mitigation | High |
| INS-BRD-08 | Requirements Traceability Matrix links each requirement to source | High |

## Inspection Process

```
[Trigger] IPM BRD Writer sends SupervisorTriggered
     |
     v
[Load] Read references/inspection-criteria.md for detailed verification rules
     |
     v
[Check] Inspect each item INS-01 through INS-12 + INS-BRD-01 through INS-BRD-08
     |
     v
[Report] Generate inspection report (format below)
     |
     v
[Decide] Pass rate = 100%?
     |-- No  -> Return report to IPM BRD Writer for remediation
     |          Writer fixes and re-sends SupervisorTriggered
     |          Repeat until 100% pass
     |-- Yes -> Notify PM Agent with completion package
```

## Inspection Report Format

```markdown
# IPM BRD Supervisor Inspection Report

- Inspection Time: {timestamp}
- Inspection Round: #{N}
- BRD File Path: {brd_file_path}

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
| INS-BRD-01: Executive Summary | PASS/FAIL | {notes} |
| INS-BRD-02: SMART Objectives | PASS/FAIL | {notes} |
| INS-BRD-03: Scope Defined | PASS/FAIL | {notes} |
| INS-BRD-04: Acceptance Criteria | PASS/FAIL | {notes} |
| INS-BRD-05: Requirements Prioritized | PASS/FAIL | {notes} |
| INS-BRD-06: No Unresolved TBDs | PASS/FAIL | {notes} |
| INS-BRD-07: Risks Documented | PASS/FAIL | {notes} |
| INS-BRD-08: Traceability | PASS/FAIL | {notes} |

## Overall Pass Rate: {X}% ({M}/{N} items passed)

## Issues Requiring Remediation
1. {issue_description} — Suggested fix: {suggestion}

## Conclusion: [FAIL -> Return to IPM Writer | PASS -> Notify PM Agent]
```

## On 100% Pass

1. Generate final report marked "ALL PASSED"
2. Notify **PM Agent** with:
   - BRD document file path
   - RACI matrix configuration (for triggering downstream SM-INC-001 through SM-INC-005)
   - Final inspection report
3. PM Agent uses the RACI matrix to activate Scrum Master tasks

## Resources

- Inspection criteria details: see `references/inspection-criteria.md`
