# Definition of Ready (DoR) -- sa-performance-load-testing

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Topic is provided | Yes | User has supplied the system or service to performance test |
| DoR-02 | Scope is defined or definable | Yes | Test scope boundaries stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `performance-load-testing/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture design outputs | Recommended | Architecture Design (IA-REQ-001) deliverables available |
| DoR-07 | NFR mapping document | Recommended | Non-functional requirements with measurable targets available |
| DoR-08 | Deployment architecture | Recommended | Infrastructure topology and resource specs available |
| DoR-09 | SLA/SLO targets | Recommended | Business SLA definitions with latency/throughput/availability targets |
| DoR-10 | Workload profile data | Recommended | Expected user concurrency, transaction volumes, peak patterns |
| DoR-11 | Technology stack details | Recommended | Performance characteristics of chosen technologies |
| DoR-12 | Historical performance data | Optional | Existing baseline metrics if system is in production |

## Pre-flight Check Process

```
1. Verify Topic is provided -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for architecture design outputs -> if available, load as primary context
5. Check for NFR mapping and SLA targets -> if available, load as performance baseline
6. If all required DoR items pass -> proceed to Phase 0 (Initialization)
7. If any required DoR item fails -> inform user and request resolution
8. If recommended items unavailable -> log gaps in work log, proceed with available info
```
