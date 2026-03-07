# Definition of Ready (DoR) — sa-code-design-reviews

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Review subject is provided | Yes | User has supplied the code, PR, or component design to review |
| DoR-02 | Scope is defined or definable | Yes | Review scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `code-design-reviews/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture Design artifacts (IA-REQ-001) | Recommended | Architecture diagrams, C4 models, integration views as compliance baseline |
| DoR-07 | Technical Guidance outputs (IA-DEV-001) | Recommended | Pattern catalog, architecture-to-code mapping for reference |
| DoR-08 | Solution Architecture Document (SA-REQ-001) | Recommended | SAD from Solutions Architect available for reference |
| DoR-09 | Technology Blueprint (SA-REQ-004) | Recommended | Full technology stack definition available |
| DoR-10 | Coding Standards (TL-REQ-002) | Recommended | Coding standards and conventions for compliance check |
| DoR-11 | Code/PR access | Yes | Agent can access the code, repository, or PR under review |
| DoR-12 | Integration contracts | Recommended | API specs, interface contracts for compliance verification |

## Pre-flight Check Process

```
1. Verify review subject is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify code/PR access -> if not accessible, ask user for access
4. Verify research tools -> if unavailable, note limitation in work log
5. Check for Architecture Design artifacts (IA-REQ-001) -> if available, load as compliance baseline
6. Check for upstream outputs -> if available, load as additional context
7. If all required DoR items pass -> proceed to Phase 0 (Initialization)
8. If any required DoR item fails -> inform user and request resolution
9. If recommended items unavailable -> log gaps in work log, proceed with available info
```
