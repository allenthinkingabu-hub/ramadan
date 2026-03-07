# Definition of Done (DoD) -- sa-data-privacy-governance

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `data-privacy-governance/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `data-privacy-governance/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `data-privacy-governance/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `data-privacy-governance/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `data-privacy-governance/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `data-privacy-governance/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `data-privacy-governance/config/outputs.yaml` exists AND all templates in `data-privacy-governance/templates/` |
| DoD-08 | SOP process checklist | `data-privacy-governance/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `data-privacy-governance/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `data-privacy-governance/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `data-privacy-governance/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `data-privacy-governance/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Data Privacy & Governance report | `data-privacy-governance/data-privacy-governance-report.md` exists with complete framework |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `data-privacy-governance/research/` contains saved research process and results |
| DoD-17 | Governance diagrams | `data-privacy-governance/diagrams/` contains at least classification taxonomy and access control model diagrams |
| DoD-18 | Regulatory compliance view | `data-privacy-governance/diagrams/regulatory-compliance-view.md` exists with regulation mapping, PIA, breach procedures |
| DoD-19 | NFR alignment note | `data-privacy-governance/nfr-alignment.md` exists with NFR-to-governance mapping, constraints, assumptions |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
