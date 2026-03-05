# Definition of Done (DoD) -- tl-code-review-quality-gatekeeping

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `code-review-quality-gatekeeping/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `code-review-quality-gatekeeping/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `code-review-quality-gatekeeping/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `code-review-quality-gatekeeping/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `code-review-quality-gatekeeping/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `code-review-quality-gatekeeping/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `code-review-quality-gatekeeping/config/outputs.yaml` exists AND all templates in `code-review-quality-gatekeeping/templates/` |
| DoD-08 | SOP process checklist | `code-review-quality-gatekeeping/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `code-review-quality-gatekeeping/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `code-review-quality-gatekeeping/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `code-review-quality-gatekeeping/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `code-review-quality-gatekeeping/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Code Review Quality Gatekeeping report | `code-review-quality-gatekeeping/code-review-quality-gatekeeping-report.md` exists with complete deliverables |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `code-review-quality-gatekeeping/research/` contains saved research process and results |
| DoD-17 | Review standards document | `code-review-quality-gatekeeping/review-standards.md` exists with review types, severity, escalation |
| DoD-18 | Quality gate report | `code-review-quality-gatekeeping/quality-gate-report.md` exists with gate definitions and thresholds |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
