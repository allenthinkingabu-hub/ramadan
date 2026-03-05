# Definition of Done (DoD) -- sa-stakeholder-alignment

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `stakeholder-alignment/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `stakeholder-alignment/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `stakeholder-alignment/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `stakeholder-alignment/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `stakeholder-alignment/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `stakeholder-alignment/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `stakeholder-alignment/config/outputs.yaml` exists AND all templates in `stakeholder-alignment/templates/` |
| DoD-08 | SOP process checklist | `stakeholder-alignment/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `stakeholder-alignment/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `stakeholder-alignment/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `stakeholder-alignment/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `stakeholder-alignment/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Stakeholder Alignment report | `stakeholder-alignment/stakeholder-alignment-report.md` exists with complete alignment record |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `stakeholder-alignment/research/` contains saved research process and results |
| DoD-17 | Stakeholder map | `stakeholder-alignment/stakeholder-map.md` exists with influence/interest matrix and engagement strategy |
| DoD-18 | Decision criteria matrix | `stakeholder-alignment/decision-criteria.md` exists with weighted criteria and trade-off analysis |
| DoD-19 | Workshop outcomes | `stakeholder-alignment/workshop-outcomes.md` exists with agreed scope, risk posture, and action items |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
