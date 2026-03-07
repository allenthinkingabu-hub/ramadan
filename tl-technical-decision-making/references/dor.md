# Definition of Ready (DoR) -- tl-technical-decision-making

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the decision context or technical question |
| DoR-02 | Scope is defined or definable | Yes | Decision scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `technical-decision-making/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture Design documents | Recommended | IA-REQ-001 outputs available for alignment |
| DoR-07 | Technology Blueprint | Recommended | Existing tech stack decisions for context |
| DoR-08 | NFR requirements | Recommended | Non-functional requirements for evaluation criteria |
| DoR-09 | Existing ADRs | Recommended | Previous architectural decision records for consistency |
| DoR-10 | Decision drivers identified | Yes | Key decision drivers and constraints known or obtainable |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for architecture design documents -> if available, load as context
5. Check for existing ADRs -> if available, load for consistency
6. If all required DoR items pass -> proceed to Phase 0 (Initialization)
7. If any required DoR item fails -> inform user and request resolution
8. If recommended items unavailable -> log gaps in work log, proceed with available info
```
