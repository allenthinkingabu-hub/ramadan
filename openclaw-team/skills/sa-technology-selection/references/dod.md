# Definition of Done (DoD) — sa-technology-selection

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `technology-selection/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `technology-selection/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `technology-selection/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `technology-selection/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `technology-selection/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `technology-selection/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `technology-selection/config/outputs.yaml` exists AND all templates in `technology-selection/templates/` |
| DoD-08 | SOP process checklist | `technology-selection/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `technology-selection/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `technology-selection/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `technology-selection/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `technology-selection/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Technology Selection report | `technology-selection/technology-selection-report.md` exists with complete evaluation |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `technology-selection/research/` contains saved research process and results |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL → log issue, fix, and re-check
  4. Repeat until all items PASS
```
