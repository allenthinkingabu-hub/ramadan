# Definition of Ready (DoR) — SA-feasibility-analysis

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Verification |
|:---|:---|:---|
| DoR-01 | Topic (requirements) is provided | User has supplied the client's requirements to assess |
| DoR-02 | Scope is defined or definable | Feasibility scope boundaries are stated or can be clarified in Step 1 |
| DoR-03 | User is available for dialogue | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Parent directory exists and agent can create `feasibility-analysis/` |
| DoR-05 | Research tools available | Web Search or equivalent tools are accessible |
| DoR-06 | Technical Discovery available (optional) | IA-INC-001 report available for reference if applicable |

## Pre-flight Check Process

```
1. Verify Topic (requirements) is provided → if missing, ask user
2. Verify output directory is writable → if not, ask user for alternative path
3. Verify research tools → if unavailable, note limitation in work log
4. Check if Technical Discovery report exists → if yes, load as reference context
5. If all required DoR items pass → proceed to Phase 0 (Initialization)
6. If any required DoR item fails → inform user and request resolution
```
