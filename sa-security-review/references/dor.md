# Definition of Ready (DoR) -- sa-security-review

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the system or project for security review |
| DoR-02 | Scope is defined or definable | Yes | Security review scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `security-review/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture Design outputs (IA-REQ-001) | Recommended | Available for reference |
| DoR-07 | Security architecture documentation | Recommended | Available for reference |
| DoR-08 | Compliance and regulatory requirements | Recommended | Available for reference |
| DoR-09 | Data classification and privacy policies | Recommended | Available for reference |
| DoR-10 | Third-party integration security profiles | Recommended | Available for reference |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for upstream inputs -> if available, load as primary context
5. If all required DoR items pass -> proceed to Phase 0 (Initialization)
6. If any required DoR item fails -> inform user and request resolution
7. If recommended items unavailable -> log gaps in work log, proceed with available info
```
