# Definition of Done (DoD) -- sa-risk-identification

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `risk-identification/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `risk-identification/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `risk-identification/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `risk-identification/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `risk-identification/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `risk-identification/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `risk-identification/config/outputs.yaml` exists AND all templates in `risk-identification/templates/` |
| DoD-08 | SOP process checklist | `risk-identification/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `risk-identification/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `risk-identification/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `risk-identification/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `risk-identification/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Risk Identification report | `risk-identification/risk-identification-report.md` exists with complete risk assessment |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `risk-identification/research/` contains saved research process and results |
| DoD-17 | Risk register | `risk-identification/risk-register.md` exists with categorized risks, severity, and owners |
| DoD-18 | Dependency map | `risk-identification/diagrams/dependency-map.md` exists with system dependency graph |
| DoD-19 | Mitigation strategies | `risk-identification/mitigation-strategies.md` exists with risk-to-mitigation mapping |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
