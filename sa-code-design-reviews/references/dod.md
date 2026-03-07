# Definition of Done (DoD) — sa-code-design-reviews

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `code-design-reviews/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `code-design-reviews/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `code-design-reviews/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `code-design-reviews/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `code-design-reviews/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `code-design-reviews/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `code-design-reviews/config/outputs.yaml` exists AND all templates in `code-design-reviews/templates/` |
| DoD-08 | SOP process checklist | `code-design-reviews/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `code-design-reviews/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `code-design-reviews/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `code-design-reviews/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `code-design-reviews/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Code & Design Review report | `code-design-reviews/code-design-review-report.md` exists with complete findings |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `code-design-reviews/research/` contains saved research process and results |
| DoD-17 | Compliance matrix | `code-design-reviews/compliance-matrix.md` exists with architecture compliance assessment |
| DoD-18 | Remediation plan | `code-design-reviews/remediation-plan.md` exists with prioritized issues and fixes |
| DoD-19 | Review decision log | `code-design-reviews/review-decision-log.md` exists with decisions and conditions |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
