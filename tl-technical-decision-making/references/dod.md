# Definition of Done (DoD) -- tl-technical-decision-making

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `technical-decision-making/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `technical-decision-making/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `technical-decision-making/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `technical-decision-making/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `technical-decision-making/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `technical-decision-making/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `technical-decision-making/config/outputs.yaml` exists AND all templates in `technical-decision-making/templates/` |
| DoD-08 | SOP process checklist | `technical-decision-making/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `technical-decision-making/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `technical-decision-making/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `technical-decision-making/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `technical-decision-making/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Technical Decision Making report | `technical-decision-making/technical-decision-making-report.md` exists with complete deliverables |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `technical-decision-making/research/` contains saved research process and results |
| DoD-17 | Trade-off analysis | `technical-decision-making/trade-off-analysis.md` exists with options, scoring, recommendations |
| DoD-18 | Decision register | `technical-decision-making/decision-register.md` exists with all decisions, rationale, and status |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
