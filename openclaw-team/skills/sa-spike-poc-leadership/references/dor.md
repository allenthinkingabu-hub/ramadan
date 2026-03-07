# Definition of Ready (DoR) — sa-spike-poc-leadership

## Readiness Prerequisites Checklist

All items must be satisfied before the agent begins execution.

| DoR ID | Prerequisite | Required | Verification |
|:---|:---|:---:|:---|
| DoR-01 | Uncertainty area is identified | Yes | User has supplied the specific technical uncertainty to investigate |
| DoR-02 | Scope is defined or definable | Yes | Spike scope and time-box stated or clarifiable in Step 1 |
| DoR-03 | User is available for dialogue | Yes | User can participate in iterative Q&A (Steps 1-3) |
| DoR-04 | Output directory is writable | Yes | Parent directory exists and agent can create `spike-poc/` |
| DoR-05 | Research tools available | Yes | Web Search or equivalent tools are accessible |
| DoR-06 | Architecture Design artifacts (IA-REQ-001) | Recommended | Architecture diagrams providing context for the spike |
| DoR-07 | Technical Guidance outputs (IA-DEV-001) | Recommended | Pattern catalog and guidance for reference |
| DoR-08 | Solution Architecture Document (SA-REQ-001) | Recommended | SAD from Solutions Architect available for reference |
| DoR-09 | Technology Blueprint (SA-REQ-004) | Recommended | Technology stack definition available |
| DoR-10 | ARB Feedback (SA-REQ-005) | Recommended | Architecture Review Board notes available |
| DoR-11 | Success/failure criteria | Recommended | Clear criteria for what constitutes spike success |
| DoR-12 | Time-box defined | Recommended | Time constraint for the spike/PoC effort |

## Pre-flight Check Process

```
1. Verify uncertainty area is identified -> if missing, ask user
2. Verify output directory is writable -> if not, ask user for alternative path
3. Verify research tools -> if unavailable, note limitation in work log
4. Check for Architecture Design artifacts (IA-REQ-001) -> if available, load as context
5. Check for upstream SA-REQ outputs -> if available, load as additional context
6. If all required DoR items pass -> proceed to Phase 0 (Initialization)
7. If any required DoR item fails -> inform user and request resolution
8. If recommended items unavailable -> log gaps in work log, proceed with available info
```
