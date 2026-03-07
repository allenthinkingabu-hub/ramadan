# Definition of Ready (DoR) -- sa-stakeholder-alignment

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the project or system requiring stakeholder alignment |
| DoR-02 | Scope is defined or definable | Yes | Alignment scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `stakeholder-alignment/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | SA-REQ-001: Solution Architecture Document (SAD) | Recommended | Solutions Architect's SAD from Wave 9 available for reference |
| DoR-07 | SA-REQ-002: Integration Architecture | Recommended | Integration patterns, interface contracts from Wave 9 |
| DoR-08 | SA-REQ-003: NFR Mapping | Recommended | Business SLAs translated into measurable NFRs from Wave 9 |
| DoR-09 | SA-REQ-004: Technology Blueprint | Recommended | Full technology stack definition from Wave 9 |
| DoR-10 | SA-REQ-005: ARB Feedback | Recommended | Architecture Review Board approval and alignment notes from Wave 9 |
| DoR-11 | Technical Discovery report (IA-INC-001) | Recommended | If available, load as additional context |
| DoR-12 | Feasibility Analysis report (IA-INC-002) | Recommended | If available, load as additional context |
| DoR-13 | Business & technical requirements | Yes | Requirements available or obtainable through dialogue |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for Wave 9 SA-REQ outputs (SA-REQ-001..005) -> if available, load as primary context
5. Check for upstream reports (IA-INC-001, IA-INC-002) -> if available, load as additional context
6. If all required DoR items pass -> proceed to Phase 0 (Initialization)
7. If any required DoR item fails -> inform user and request resolution
8. If recommended items unavailable -> log gaps in work log, proceed with available info
```
