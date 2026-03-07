# Definition of Ready (DoR) — sa-technical-guidance

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the area or component requiring architectural guidance |
| DoR-02 | Scope is defined or definable | Yes | Guidance scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `technical-guidance/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture Design artifacts (IA-REQ-001) | Recommended | Architecture diagrams, C4 models, integration views from Requirements phase |
| DoR-07 | Solution Architecture Document (SA-REQ-001) | Recommended | SAD from Solutions Architect available for reference |
| DoR-08 | Technology Blueprint (SA-REQ-004) | Recommended | Full technology stack definition available |
| DoR-09 | ARB Feedback (SA-REQ-005) | Recommended | Architecture Review Board notes available |
| DoR-10 | Developer questions or blockers identified | Recommended | Specific areas where developers need guidance |
| DoR-11 | Current implementation status | Recommended | Understanding of what has been built so far |
| DoR-12 | Coding standards (TL-REQ-002) | Recommended | If available, existing coding standards and conventions |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for Architecture Design artifacts (IA-REQ-001) -> if available, load as primary context
5. Check for upstream SA-REQ outputs -> if available, load as additional context
6. If all required DoR items pass -> proceed to Phase 0 (Initialization)
7. If any required DoR item fails -> inform user and request resolution
8. If recommended items unavailable -> log gaps in work log, proceed with available info
```
