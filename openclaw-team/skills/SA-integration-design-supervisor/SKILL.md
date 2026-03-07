---
name: SA-integration-design-supervisor
description: "Independent Quality Supervisor AI Agent skill for end-to-end quality monitoring and closed-loop remediation of the SA-integration-design agent output. Use when: (1) the Integration Design Agent (IA-REQ-003) completes one round of output and needs quality inspection, (2) verifying all required deliverables of the integration design task are complete and valid (including API contracts, data flows, error handling, security design, test strategy), or (3) ensuring closed-loop quality remediation before handoff to PM Agent."
---

# SA Integration Design Supervisor Agent

Role: Quality Supervisor | Parent Task: IA-REQ-003 Integration Design

Operates independently from the Integration Design Agent. Does not participate in the design — only reviews and provides feedback.

## Trigger

Automatically triggered after the Integration Design AI Agent completes one round of output.

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
| 14 | Integration Design report | `integration-design-report.md` exists with all sections complete |
| 15 | API Contract Specifications | `api-specs/` directory contains OpenAPI/AsyncAPI/Proto specs |
| 16 | Data Flow Diagrams | `diagrams/data-flow-*.md` files exist with Mermaid/PlantUML |
| 17 | Third-Party Dependency Register | `third-party-register.md` exists with risk assessment |
| 18 | Integration Security Design | `integration-security-design.md` exists with auth, encryption, threat protection |
| 19 | Error Handling Strategy | `error-handling-strategy.md` exists with retry, circuit breaker, fallback |
| 20 | Integration Test Strategy | `integration-test-strategy.md` exists with contract, integration, E2E testing |
| 21 | Monitoring & Alerting Plan | `monitoring-alerting-plan.md` exists with SLO/SLI, health checks, tracing |
| 22 | Phase question lists | `phase{N}-questions.md` files exist for all phases |
| 23 | Research records | `research/` directory contains research artifacts |
| 24 | Upstream traceability | IA-REQ-001, IA-REQ-002 references present, decisions traceable |

## Inspection Process

```
[Trigger] Integration Design Agent completes output
     ↓
[Inspect] Verify items 1 through 24
     ↓
[Generate Report] Output inspection report (see format below)
     ↓
[Decide] Pass rate = 100%?
     ├── No → Return report to Integration Design Agent for item-by-item remediation
     │         Agent completes fixes → re-triggers this Supervisor
     │         (repeat until 100% pass)
     └── Yes → Invoke PM Agent, submit completion report
```

## Inspection Report Format

Generate after each inspection round:

```markdown
# Integration Design Supervisor Inspection Report

- Inspection Time: {timestamp}
- Inspection Round: #{N}
- Integration Design Report File Path: {file_path}

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
| Item 14: Integration Design Report | PASS / FAIL | {notes} |
| Item 15: API Contract Specifications | PASS / FAIL | {notes} |
| Item 16: Data Flow Diagrams | PASS / FAIL | {notes} |
| Item 17: Third-Party Dependency Register | PASS / FAIL | {notes} |
| Item 18: Integration Security Design | PASS / FAIL | {notes} |
| Item 19: Error Handling Strategy | PASS / FAIL | {notes} |
| Item 20: Integration Test Strategy | PASS / FAIL | {notes} |
| Item 21: Monitoring & Alerting Plan | PASS / FAIL | {notes} |
| Item 22: Phase Question Lists | PASS / FAIL | {notes} |
| Item 23: Research Records | PASS / FAIL | {notes} |
| Item 24: Upstream Traceability | PASS / FAIL | {notes} |

## Overall Pass Rate: {X}% ({M}/24 items passed)

## Issues Requiring Remediation
1. {issue_description} — Suggested fix: {suggestion}

## Conclusion: [FAIL — Return for remediation | PASS — Invoke PM Agent]
```

## Post-Completion: Invoke PM Agent

When pass rate reaches **100%**:
1. Generate final inspection report (marked "ALL PASSED")
2. Invoke PM Agent, sending:
   - Integration Design report file path and filename
   - RACI matrix configuration (for PM to trigger downstream tasks)
   - Final inspection report

## Reference

- Inspection criteria details: [references/inspection-criteria.md](references/inspection-criteria.md)
