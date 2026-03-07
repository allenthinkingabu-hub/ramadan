---
name: sa-risk-identification-supervisor
description: "Independent Quality Supervisor AI Agent skill for end-to-end quality monitoring and closed-loop remediation of the sa-risk-identification agent output. Use when: (1) the Risk Identification Agent (IA-INC-004) completes one round of output and needs quality inspection, (2) verifying all required deliverables of the risk identification task are complete and valid (including risk register, dependency map, and mitigation strategies), or (3) ensuring closed-loop quality remediation before handoff to PM Agent."
---

# SA Risk Identification Supervisor Agent

Role: Quality Supervisor | Parent Task: IA-INC-004 Risk Identification | Wave: 10, Step: 4

Operates independently from the Risk Identification Agent. Does not participate in the assessment -- only reviews and provides feedback.

## Trigger

Automatically triggered after the Risk Identification AI Agent completes one round of output.

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
| 14 | Risk register | `risk-register.md` exists with categorized risks, severity ratings, owners, and mitigations |
| 15 | Dependency map | `diagrams/dependency-map.md` exists with system dependency graph and critical path analysis |
| 16 | Mitigation strategies | `mitigation-strategies.md` exists with risk-to-mitigation mapping and contingency plans |
| 17 | Upstream traceability | SA-REQ-001..005 references present, risks traceable to architecture and requirements |

## Inspection Process

```
[Trigger] Risk Identification Agent completes output
     |
[Inspect] Verify items 1 through 17
     |
[Generate Report] Output inspection report (see format below)
     |
[Decide] Pass rate = 100%?
     +-- No -> Return report to Risk Identification Agent for item-by-item remediation
     |         Agent completes fixes -> re-triggers this Supervisor
     |         (repeat until 100% pass)
     +-- Yes -> Invoke PM Agent, submit completion report
```

## Inspection Report Format

Generate after each inspection round:

```markdown
# Risk Identification Supervisor Inspection Report

- Inspection Time: {timestamp}
- Inspection Round: #{N}
- Risk Identification Report File Path: {file_path}

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
| Item 14: Risk Register | PASS / FAIL | {notes} |
| Item 15: Dependency Map | PASS / FAIL | {notes} |
| Item 16: Mitigation Strategies | PASS / FAIL | {notes} |
| Item 17: Upstream Traceability | PASS / FAIL | {notes} |

## Overall Pass Rate: {X}% ({M}/17 items passed)

## Issues Requiring Remediation
1. {issue_description} -- Suggested fix: {suggestion}

## Conclusion: [FAIL -- Return for remediation | PASS -- Invoke PM Agent]
```

## Post-Completion: Invoke PM Agent

When pass rate reaches **100%**:
1. Generate final inspection report (marked "ALL PASSED")
2. Invoke PM Agent, sending:
   - Risk Identification report file path and filename
   - RACI matrix configuration (for PM to trigger downstream tasks)
   - Final inspection report

## Reference

- Inspection criteria details: [references/inspection-criteria.md](references/inspection-criteria.md)
