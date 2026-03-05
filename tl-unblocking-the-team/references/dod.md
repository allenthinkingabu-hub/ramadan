# Definition of Done (DoD) -- tl-unblocking-the-team

## Quality Gates Checklist

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `unblocking-the-team/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `unblocking-the-team/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `unblocking-the-team/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `unblocking-the-team/config/knowledge-domains.yaml` exists |
| DoD-05 | Tools list | `unblocking-the-team/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `unblocking-the-team/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `unblocking-the-team/config/outputs.yaml` exists AND templates in `unblocking-the-team/templates/` |
| DoD-08 | SOP process checklist | `unblocking-the-team/config/sop.yaml` exists |
| DoD-09 | DoD checklist | `unblocking-the-team/config/dod.yaml` exists |
| DoD-10 | DoR checklist | `unblocking-the-team/config/dor.yaml` exists |
| DoD-11 | Conversation log | `unblocking-the-team/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `unblocking-the-team/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified |
| DoD-14 | Unblocking report | `unblocking-the-team/unblocking-the-team-report.md` exists with complete deliverables |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `unblocking-the-team/research/` contains saved research |
| DoD-17 | Blocker resolution report | `unblocking-the-team/blocker-resolution-report.md` exists with resolutions and root causes |
| DoD-18 | Escalation framework | `unblocking-the-team/escalation-framework.md` exists with escalation paths and SLAs |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
