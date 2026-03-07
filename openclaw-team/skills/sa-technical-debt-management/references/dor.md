# Definition of Ready (DoR) — sa-technical-debt-management

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the system or codebase to assess for technical debt |
| DoR-02 | Scope is defined or definable | Yes | Debt assessment scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `technical-debt/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture Design artifacts (IA-REQ-001) | Recommended | Architecture diagrams for drift assessment |
| DoR-07 | Code & Design Review findings (IA-DEV-002) | Recommended | Review findings identifying debt items |
| DoR-08 | Solution Architecture Document (SA-REQ-001) | Recommended | SAD from Solutions Architect for reference |
| DoR-09 | Technology Blueprint (SA-REQ-004) | Recommended | Technology stack definition for dependency assessment |
| DoR-10 | Codebase access | Recommended | Agent can access the codebase for analysis |
| DoR-11 | Static analysis results | Recommended | SonarQube or similar tool results available |
| DoR-12 | Known debt items list | Recommended | Existing backlog of known technical debt |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for Architecture Design artifacts (IA-REQ-001) -> if available, load for drift analysis
5. Check for Code & Design Review findings (IA-DEV-002) -> if available, load as debt input
6. Check for upstream SA-REQ outputs -> if available, load as additional context
7. If all required DoR items pass -> proceed to Phase 0 (Initialization)
8. If any required DoR item fails -> inform user and request resolution
9. If recommended items unavailable -> log gaps in work log, proceed with available info
```
