# Definition of Done (DoD) -- sa-performance-load-testing

## Quality Gates Checklist

Every item must pass before the task is considered complete.

| DoD ID | Check Item | Verification Criteria |
|:---|:---|:---|
| DoD-01 | Trigger mechanism config | `performance-load-testing/config/triggers.yaml` exists with valid trigger definitions |
| DoD-02 | RACI matrix config | `performance-load-testing/config/raci.yaml` exists with role names + task names |
| DoD-03 | Skills list config | `performance-load-testing/config/skills.yaml` exists with agent competencies |
| DoD-04 | Knowledge base checklist | `performance-load-testing/config/knowledge-domains.yaml` exists with required knowledge |
| DoD-05 | Tools list | `performance-load-testing/config/tools.yaml` exists with available tools |
| DoD-06 | MCP tools list | `performance-load-testing/config/mcp-tools.yaml` exists with MCP integrations |
| DoD-07 | Output content list + templates | `performance-load-testing/config/outputs.yaml` exists AND all templates in `performance-load-testing/templates/` |
| DoD-08 | SOP process checklist | `performance-load-testing/config/sop.yaml` exists with operating procedure |
| DoD-09 | DoD checklist | `performance-load-testing/config/dod.yaml` exists with quality thresholds |
| DoD-10 | DoR checklist | `performance-load-testing/config/dor.yaml` exists with readiness prerequisites |
| DoD-11 | Conversation log | `performance-load-testing/conversation-log.md` exists, logged question by question |
| DoD-12 | Work log | `performance-load-testing/work-log.md` exists, logged entry by entry on timeline |
| DoD-13 | DoD self-verification | All items DoD-01 through DoD-12 verified, auto-remediation completed |
| DoD-14 | Performance Load Testing report | `performance-load-testing/performance-load-testing-report.md` exists with complete plan |
| DoD-15 | Phase question lists | Question list files exist for each phase |
| DoD-16 | Research artifacts | `performance-load-testing/research/` contains saved research process and results |
| DoD-17 | Test scenarios | `performance-load-testing/scenarios/` contains load, stress, soak, spike test definitions |
| DoD-18 | Benchmark definitions | `performance-load-testing/scenarios/benchmarks.md` exists with latency, throughput, concurrency targets |
| DoD-19 | Test execution plan | `performance-load-testing/test-execution-plan.md` exists with environment, tools, schedule |
| DoD-20 | Acceptance criteria matrix | `performance-load-testing/acceptance-criteria.md` exists with NFR-to-test mapping |

## Self-Verification Process

```
For each DoD item:
  1. Check if deliverable file exists
  2. Check if content is non-empty and structurally valid
  3. If FAIL -> log issue, fix, and re-check
  4. Repeat until all items PASS
```
