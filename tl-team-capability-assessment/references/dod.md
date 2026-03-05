# Definition of Done (DoD) — tl-team-capability-assessment

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `team-capability-assessment/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `team-capability-assessment/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `team-capability-assessment/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `team-capability-assessment/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `team-capability-assessment/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `team-capability-assessment/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `team-capability-assessment/config/outputs.yaml` exists AND all templates in `team-capability-assessment/templates/` |
| DoD-08 | SOP process checklist | `team-capability-assessment/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `team-capability-assessment/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `team-capability-assessment/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `team-capability-assessment/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `team-capability-assessment/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Team Capability Assessment report | `team-capability-assessment/team-capability-assessment-report.md` exists with complete assessment |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `team-capability-assessment/research/` contains saved research process and results |
| DoD-17 | Team Skills Matrix | `team-capability-assessment/skills-matrix.md` exists with individual and team-level ratings |
| DoD-18 | Gap Analysis | `team-capability-assessment/gap-analysis.md` exists with identified gaps and impact assessment |
| DoD-19 | Development & Remediation Plan | `team-capability-assessment/development-plan.md` exists with training, hiring, and KT recommendations |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
