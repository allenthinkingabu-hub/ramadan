# Definition of Done (DoD) -- tl-hands-on-development

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `hands-on-development/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `hands-on-development/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `hands-on-development/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `hands-on-development/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `hands-on-development/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `hands-on-development/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `hands-on-development/config/outputs.yaml` exists AND all templates in `hands-on-development/templates/` |
| DoD-08 | SOP process checklist | `hands-on-development/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `hands-on-development/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `hands-on-development/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `hands-on-development/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `hands-on-development/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Hands-On Development report | `hands-on-development/hands-on-development-report.md` exists with complete deliverables |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `hands-on-development/research/` contains saved research process and results |
| DoD-17 | Implementation patterns | `hands-on-development/implementation-patterns.md` exists with patterns and rationale |
| DoD-18 | Reference implementations | `hands-on-development/implementations/` contains reference code |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
