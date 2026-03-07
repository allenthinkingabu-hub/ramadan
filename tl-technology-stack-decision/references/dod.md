# Definition of Done (DoD) — tl-technology-stack-decision

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `technology-stack-decision/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `technology-stack-decision/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `technology-stack-decision/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `technology-stack-decision/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `technology-stack-decision/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `technology-stack-decision/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `technology-stack-decision/config/outputs.yaml` exists AND all templates in `technology-stack-decision/templates/` |
| DoD-08 | SOP process checklist | `technology-stack-decision/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `technology-stack-decision/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `technology-stack-decision/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `technology-stack-decision/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `technology-stack-decision/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Technology Stack Decision report | `technology-stack-decision/technology-stack-decision-report.md` exists with complete decisions |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `technology-stack-decision/research/` contains saved research process and results |
| DoD-17 | Technology Decision Matrix | `technology-stack-decision/technology-decision-matrix.md` exists with evaluation criteria and scoring |
| DoD-18 | Stack Specification | `technology-stack-decision/stack-specification.md` exists with languages, frameworks, libraries, infrastructure |
| DoD-19 | Compatibility Analysis | `technology-stack-decision/compatibility-analysis.md` exists with inter-component compatibility verification |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
