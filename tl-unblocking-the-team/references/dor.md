# Definition of Ready (DoR) -- tl-unblocking-the-team

## Readiness Prerequisites Checklist

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the blocker or impediment context |
| DoR-02 | Scope is defined or definable | Yes | Blocker scope stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `unblocking-the-team/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture Design documents | Recommended | IA-REQ-001 outputs for understanding system context |
| DoR-07 | Codebase access | Recommended | Access to repository for debugging |
| DoR-08 | Error logs/symptoms | Recommended | Error messages, stack traces, or symptoms available |
| DoR-09 | Team context | Recommended | Information about affected team members and impact |
| DoR-10 | Dependency information | Recommended | Cross-team or external dependency details |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for architecture design documents -> if available, load as context
5. Check for error logs/symptoms -> if available, load for analysis
6. If all required DoR items pass -> proceed to Phase 0 (Initialization)
7. If any required DoR item fails -> inform user and request resolution
8. If recommended items unavailable -> log gaps in work log, proceed with available info
```
