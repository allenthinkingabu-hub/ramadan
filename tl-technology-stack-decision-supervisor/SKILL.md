---
name: tl-technology-stack-decision-supervisor
description: "Independent Quality Supervisor AI Agent skill for end-to-end quality monitoring and closed-loop remediation of the tl-technology-stack-decision agent output. Use when: (1) the Technology Stack Decision Agent (TL-INC-002) completes one round of output and needs quality inspection, (2) verifying all required deliverables of the technology stack decision task are complete and valid, or (3) ensuring closed-loop quality remediation before handoff to PM Agent."
---

# TL Technology Stack Decision Supervisor Agent

Role: Quality Supervisor | Parent Task: TL-INC-002 Technology Stack Decision | Wave: 11, Step: 2

Operates independently from the Technology Stack Decision Agent. Does not participate in the decision-making — only reviews and provides feedback.

## Trigger

Automatically triggered after the Technology Stack Decision AI Agent completes one round of output.

## Inspection Checklist

Verify all items have been fully executed:

| # | Check Item | Verification |
|:---|:---|:---|
| 1 | Trigger mechanism config | `config/triggers.yaml` exists and is valid |
| 2 | RACI matrix config | `config/raci.yaml` exists with role names + task names |
| 3 | Skills list config | `config/skills.yaml` exists with competencies |
| 4 | Knowledge base checklist | `config/knowledge-domains.yaml` exists |
| 5 | Tools list | `config/tools.yaml` exists |
| 6 | MCP tools list | `config/mcp-tools.yaml` exists |
| 7 | Output list + templates | `config/outputs.yaml` exists AND `templates/` populated |
| 8 | SOP process checklist | `config/sop.yaml` exists |
| 9 | DoD checklist | `config/dod.yaml` exists |
| 10 | DoR checklist | `config/dor.yaml` exists |
| 11 | Conversation log | `conversation-log.md` exists, logged question by question |
| 12 | Work log | `work-log.md` exists, logged entry by entry on timeline |
| 13 | DoD verification | All DoD items verified with auto-remediation completed |
| 14 | Technology Decision Matrix | `technology-decision-matrix.md` exists with evaluation criteria, weighted scoring, and justified recommendations |
| 15 | Stack Specification | `stack-specification.md` exists with specific versions for languages, frameworks, libraries, infrastructure |
| 16 | Compatibility Analysis | `compatibility-analysis.md` exists with inter-component compatibility verification and known issues |
| 17 | Upstream traceability | IA-INC-001..008 references present, technology decisions traceable to architect inputs and NFRs |

## Inspection Process

```
[Trigger] Technology Stack Decision Agent completes output
     |
[Inspect] Verify items 1 through 17
     |
[Generate Report] Output inspection report (see format below)
     |
[Decide] Pass rate = 100%?
     +-- No -> Return report to Technology Stack Decision Agent for item-by-item remediation
     |         Agent completes fixes -> re-triggers this Supervisor
     |         (repeat until 100% pass)
     +-- Yes -> Invoke PM Agent, submit completion report
```

## Inspection Report Format

Generate after each inspection round:

```markdown
# Technology Stack Decision Supervisor Inspection Report

- Inspection Time: {timestamp}
- Inspection Round: #{N}
- Technology Stack Decision Report File Path: {file_path}

## Inspection Results Summary

| Check Item | Status | Notes |
| :--- | :---: | :--- |
| Item 1: Trigger Mechanism Config | PASS / FAIL | {notes} |
| Item 2: RACI Matrix Config | PASS / FAIL | {notes} |
| Item 3: Skills List Config | PASS / FAIL | {notes} |
| Item 4: Knowledge Base Checklist | PASS / FAIL | {notes} |
| Item 5: Tools List | PASS / FAIL | {notes} |
| Item 6: MCP Tools List | PASS / FAIL | {notes} |
| Item 7: Output List + Templates | PASS / FAIL | {notes} |
| Item 8: SOP Process Checklist | PASS / FAIL | {notes} |
| Item 9: DoD Checklist | PASS / FAIL | {notes} |
| Item 10: DoR Checklist | PASS / FAIL | {notes} |
| Item 11: Conversation Log | PASS / FAIL | {notes} |
| Item 12: Work Log | PASS / FAIL | {notes} |
| Item 13: DoD Verification | PASS / FAIL | {notes} |
| Item 14: Technology Decision Matrix | PASS / FAIL | {notes} |
| Item 15: Stack Specification | PASS / FAIL | {notes} |
| Item 16: Compatibility Analysis | PASS / FAIL | {notes} |
| Item 17: Upstream Traceability | PASS / FAIL | {notes} |

## Overall Pass Rate: {X}% ({M}/17 items passed)

## Issues Requiring Remediation
1. {issue_description} — Suggested fix: {suggestion}

## Conclusion: [FAIL — Return for remediation | PASS — Invoke PM Agent]
```

## Post-Completion: Invoke PM Agent

When pass rate reaches **100%**:
1. Generate final inspection report (marked "ALL PASSED")
2. Invoke PM Agent, sending:
   - Technology Stack Decision report file path and filename
   - RACI matrix configuration (for PM to trigger downstream tasks)
   - Final inspection report

## Reference

- Inspection criteria details: [references/inspection-criteria.md](references/inspection-criteria.md)
