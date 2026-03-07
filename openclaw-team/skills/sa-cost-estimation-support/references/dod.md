# Definition of Done (DoD) -- sa-cost-estimation-support

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `cost-estimation/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `cost-estimation/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `cost-estimation/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `cost-estimation/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `cost-estimation/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `cost-estimation/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `cost-estimation/config/outputs.yaml` exists AND all templates in `cost-estimation/templates/` |
| DoD-08 | SOP process checklist | `cost-estimation/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `cost-estimation/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `cost-estimation/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `cost-estimation/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `cost-estimation/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Cost Estimation report | `cost-estimation/cost-estimation-report.md` exists with complete estimation |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `cost-estimation/research/` contains saved research process and results |
| DoD-17 | Cost breakdown structure | `cost-estimation/cost-breakdown.md` exists with itemized cost categories |
| DoD-18 | TCO projection | `cost-estimation/tco-projection.md` exists with multi-year cost projections |
| DoD-19 | FinOps guardrails | `cost-estimation/finops-guardrails.md` exists with budget thresholds and optimization recommendations |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
