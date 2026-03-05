# Definition of Ready (DoR) -- tl-hands-on-development

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the feature or component requiring TL development |
| DoR-02 | Scope is defined or definable | Yes | Implementation scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `hands-on-development/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture Design documents | Recommended | IA-REQ-001 outputs available for design alignment |
| DoR-07 | Technical design specifications | Recommended | Solution design docs available for implementation guidance |
| DoR-08 | Codebase access | Yes | Access to repository for development |
| DoR-09 | Development environment | Recommended | Build tools, dependencies, and dev environment configured |
| DoR-10 | Feature requirements | Yes | Requirements and acceptance criteria available |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for architecture design documents -> if available, load as primary context
5. Check for technical design specs -> if available, load as reference
6. If all required DoR items pass -> proceed to Phase 0 (Initialization)
7. If any required DoR item fails -> inform user and request resolution
8. If recommended items unavailable -> log gaps in work log, proceed with available info
```
