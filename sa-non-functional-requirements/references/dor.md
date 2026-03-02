# Definition of Ready (DoR) — sa-non-functional-requirements

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Verification |
|:---|:---|:---|
| DoR-01 | Topic is provided | User has supplied the project or system to define NFRs for |
| DoR-02 | Scope is defined or definable | NFR scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Parent directory exists and agent can create `non-functional-requirements/` |
| DoR-05 | Research tools available | Web Search or equivalent tools are accessible |
| DoR-06 | Upstream inputs available (recommended) | Architecture Design (IA-REQ-001) report preferred; Technical Discovery (IA-INC-001) and/or Feasibility Analysis (IA-INC-002) reports if applicable |
| DoR-07 | Requirements defined | Business and technical requirements available or obtainable |

## Pre-flight Check Process

```
1. Verify Topic is provided → if missing, ask user
2. Verify output directory is writable → if not, ask user for alternative path
3. Verify research tools → if unavailable, note limitation in work log
4. Check for upstream reports (IA-REQ-001, IA-INC-001, IA-INC-002) → if available, load as context
5. If all required DoR items pass → proceed to Phase 0 (Initialization)
6. If any required DoR item fails → inform user and request resolution
```
