# Definition of Done (DoD) — sa-technical-debt-management

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `technical-debt/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `technical-debt/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `technical-debt/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `technical-debt/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `technical-debt/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `technical-debt/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `technical-debt/config/outputs.yaml` exists AND all templates in `technical-debt/templates/` |
| DoD-08 | SOP process checklist | `technical-debt/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `technical-debt/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `technical-debt/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `technical-debt/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `technical-debt/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Technical Debt report | `technical-debt/technical-debt-report.md` exists with complete analysis |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `technical-debt/research/` contains saved research process and results |
| DoD-17 | Debt register | `technical-debt/debt-items/debt-register.md` exists with complete inventory |
| DoD-18 | Prioritization matrix | `technical-debt/debt-items/prioritization-matrix.md` exists with scoring |
| DoD-19 | Remediation strategy | `technical-debt/remediation-strategy.md` exists with phased plan |
| DoD-20 | Governance policy | `technical-debt/governance-policy.md` exists with thresholds and tracking |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
