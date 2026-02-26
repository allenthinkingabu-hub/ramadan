# Definition of Ready (DoR) — SA-technical-discovery

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Verification |
|:---|:---|:---|
| DoR-01 | Topic is provided | User has supplied the project or system name to assess |
| DoR-02 | Scope is defined or definable | Scope boundaries are stated or can be clarified in Step 1 |
| DoR-03 | User is available for dialogue | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Parent directory exists and agent can create `technical-discovery/` |
| DoR-05 | Research tools available | Web Search or equivalent tools are accessible |
| DoR-06 | Stakeholder access | Key stakeholders identified for consultation (or user serves as proxy) |

## Pre-flight Check Process

```
1. Verify Topic is provided → if missing, ask user
2. Verify output directory is writable → if not, ask user for alternative path
3. Verify research tools → if unavailable, note limitation in work log
4. If all DoR items pass → proceed to Phase 0 (Initialization)
5. If any DoR item fails → inform user and request resolution
```
