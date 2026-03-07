# Definition of Done (DoD) — sa-technical-guidance

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `technical-guidance/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `technical-guidance/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `technical-guidance/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `technical-guidance/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `technical-guidance/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `technical-guidance/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `technical-guidance/config/outputs.yaml` exists AND all templates in `technical-guidance/templates/` |
| DoD-08 | SOP process checklist | `technical-guidance/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `technical-guidance/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `technical-guidance/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `technical-guidance/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `technical-guidance/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Technical Guidance report | `technical-guidance/technical-guidance-report.md` exists with complete guidance |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `technical-guidance/research/` contains saved research process and results |
| DoD-17 | Pattern catalog | `technical-guidance/patterns/pattern-catalog.md` exists with applicable design patterns |
| DoD-18 | Architecture-to-code mapping | `technical-guidance/architecture-code-mapping.md` exists with component-to-module mapping |
| DoD-19 | Guidance decision log | `technical-guidance/guidance-decision-log.md` exists with decisions and rationale |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
