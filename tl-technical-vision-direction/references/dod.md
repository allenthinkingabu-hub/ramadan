# Definition of Done (DoD) — tl-technical-vision-direction

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `technical-vision-direction/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `technical-vision-direction/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `technical-vision-direction/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `technical-vision-direction/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `technical-vision-direction/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `technical-vision-direction/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `technical-vision-direction/config/outputs.yaml` exists AND all templates in `technical-vision-direction/templates/` |
| DoD-08 | SOP process checklist | `technical-vision-direction/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `technical-vision-direction/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `technical-vision-direction/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `technical-vision-direction/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `technical-vision-direction/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Technical Vision Direction report | `technical-vision-direction/technical-vision-direction-report.md` exists with complete vision |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `technical-vision-direction/research/` contains saved research process and results |
| DoD-17 | Technical Vision Statement | `technical-vision-direction/technical-vision-statement.md` exists with clear vision articulation |
| DoD-18 | Guiding Principles | `technical-vision-direction/guiding-principles.md` exists with core principles and trade-off framework |
| DoD-19 | Business-Technology Alignment Matrix | `technical-vision-direction/alignment-matrix.md` exists with objective-to-capability mapping |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
