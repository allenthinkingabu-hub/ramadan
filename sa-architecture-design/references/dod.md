# Definition of Done (DoD) — sa-architecture-design

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `architecture-design/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `architecture-design/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `architecture-design/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `architecture-design/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `architecture-design/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `architecture-design/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `architecture-design/config/outputs.yaml` exists AND all templates in `architecture-design/templates/` |
| DoD-08 | SOP process checklist | `architecture-design/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `architecture-design/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `architecture-design/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `architecture-design/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `architecture-design/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Architecture Design report | `architecture-design/architecture-design-report.md` exists with complete design |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `architecture-design/research/` contains saved research process and results |
| DoD-17 | Architecture diagrams | `architecture-design/diagrams/` contains at least C4 context + container diagrams |
| DoD-18 | Interface/Integration view | `architecture-design/diagrams/integration-view.md` exists with protocols, contracts, error handling |
| DoD-19 | NFR alignment note | `architecture-design/nfr-alignment.md` exists with NFR-to-architecture mapping, constraints, assumptions |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL → log issue, fix, and re-check
  4. Repeat until all items PASS
```
