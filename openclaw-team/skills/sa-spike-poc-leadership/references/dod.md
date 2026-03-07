# Definition of Done (DoD) — sa-spike-poc-leadership

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `spike-poc/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `spike-poc/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `spike-poc/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `spike-poc/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `spike-poc/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `spike-poc/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `spike-poc/config/outputs.yaml` exists AND all templates in `spike-poc/templates/` |
| DoD-08 | SOP process checklist | `spike-poc/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `spike-poc/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `spike-poc/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `spike-poc/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `spike-poc/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Spike/PoC report | `spike-poc/spike-poc-report.md` exists with findings and results |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `spike-poc/research/` contains saved research process and results |
| DoD-17 | Technology comparison | `spike-poc/findings/technology-comparison.md` exists (if multiple options evaluated) |
| DoD-18 | Recommendation & decision record | `spike-poc/findings/recommendation-decision.md` exists with rationale |
| DoD-19 | Risk assessment update | `spike-poc/findings/risk-assessment.md` exists with updated risk register |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
