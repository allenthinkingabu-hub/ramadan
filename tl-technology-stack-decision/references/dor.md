# Definition of Ready (DoR) — tl-technology-stack-decision

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the project or system requiring technology stack decisions |
| DoR-02 | Scope is defined or definable | Yes | Technology decision scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `technology-stack-decision/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | IA-INC-001: Technical Discovery Report | Recommended | IT Architect's technical discovery from Wave 10 |
| DoR-07 | IA-INC-002: Feasibility Analysis | Recommended | Feasibility study results from Wave 10 |
| DoR-08 | IA-INC-003: Proof of Concept Results | Recommended | PoC findings from Wave 10 |
| DoR-09 | IA-INC-004: NFR Analysis | Recommended | Non-functional requirements from Wave 10 |
| DoR-10 | IA-INC-005: Technology Landscape Assessment | Recommended | Technology landscape evaluation from Wave 10 |
| DoR-11 | IA-INC-006: Risk Assessment | Recommended | Technical risk analysis from Wave 10 |
| DoR-12 | IA-INC-007: Integration Strategy | Recommended | Integration approach from Wave 10 |
| DoR-13 | IA-INC-008: Architecture Patterns Evaluation | Recommended | Architecture patterns from Wave 10 |
| DoR-14 | Existing technology inventory | Recommended | Current technology stack documentation if available |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for Wave 10 IA-INC outputs (IA-INC-001..008) -> if available, load as primary context
5. Check for existing technology inventory -> if available, load as additional context
6. If all required DoR items pass -> proceed to Phase 0 (Initialization)
7. If any required DoR item fails -> inform user and request resolution
8. If recommended items unavailable -> log gaps in work log, proceed with available info
```
