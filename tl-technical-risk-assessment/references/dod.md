# Definition of Done (DoD) — tl-technical-risk-assessment

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `technical-risk-assessment/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `technical-risk-assessment/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `technical-risk-assessment/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `technical-risk-assessment/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `technical-risk-assessment/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `technical-risk-assessment/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `technical-risk-assessment/config/outputs.yaml` exists AND all templates in `technical-risk-assessment/templates/` |
| DoD-08 | SOP process checklist | `technical-risk-assessment/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `technical-risk-assessment/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `technical-risk-assessment/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `technical-risk-assessment/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `technical-risk-assessment/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Technical Risk Assessment report | `technical-risk-assessment/technical-risk-assessment-report.md` exists with complete assessment |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `technical-risk-assessment/research/` contains saved research process and results |
| DoD-17 | Risk Register | `technical-risk-assessment/risk-register.md` exists with categorized risks, probability, and impact |
| DoD-18 | Dependency Map | `technical-risk-assessment/dependency-map.md` exists with external and internal dependencies |
| DoD-19 | Mitigation Strategy Plan | `technical-risk-assessment/mitigation-plan.md` exists with actions per risk and contingency plans |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
