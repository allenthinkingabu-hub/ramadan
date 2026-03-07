# Definition of Done (DoD) -- sa-dr-bcp-architecture

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `dr-bcp-architecture/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `dr-bcp-architecture/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `dr-bcp-architecture/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `dr-bcp-architecture/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `dr-bcp-architecture/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `dr-bcp-architecture/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `dr-bcp-architecture/config/outputs.yaml` exists AND all templates in `dr-bcp-architecture/templates/` |
| DoD-08 | SOP process checklist | `dr-bcp-architecture/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `dr-bcp-architecture/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `dr-bcp-architecture/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `dr-bcp-architecture/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `dr-bcp-architecture/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | DR/BCP Architecture report | `dr-bcp-architecture/dr-bcp-architecture-report.md` exists with complete design |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `dr-bcp-architecture/research/` contains saved research process and results |
| DoD-17 | DR/BCP diagrams | `dr-bcp-architecture/diagrams/` contains at least failover topology and backup strategy diagrams |
| DoD-18 | Resilience architecture view | `dr-bcp-architecture/diagrams/resilience-architecture-view.md` exists with failure domains, replication, degradation strategies |
| DoD-19 | NFR alignment note | `dr-bcp-architecture/nfr-alignment.md` exists with NFR-to-DR/BCP mapping, constraints, assumptions |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
