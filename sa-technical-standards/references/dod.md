# Definition of Done (DoD) -- sa-technical-standards

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `technical-standards/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `technical-standards/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `technical-standards/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `technical-standards/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `technical-standards/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `technical-standards/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `technical-standards/config/outputs.yaml` exists AND all templates in `technical-standards/templates/` |
| DoD-08 | SOP process checklist | `technical-standards/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `technical-standards/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `technical-standards/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `technical-standards/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `technical-standards/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Technical Standards report | `technical-standards/technical-standards-report.md` exists with complete standards |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `technical-standards/research/` contains saved research process and results |
| DoD-17 | Standards documentation | `technical-standards/diagrams/` contains at least coding standards and design patterns catalog |
| DoD-18 | Standards enforcement view | `technical-standards/diagrams/standards-enforcement-view.md` exists with linting, review, CI/CD quality gates |
| DoD-19 | NFR alignment note | `technical-standards/nfr-alignment.md` exists with NFR-to-standards mapping, constraints, assumptions |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
