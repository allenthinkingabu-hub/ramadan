# Inspection Report

## Header

| Field | Value |
|-------|-------|
| Inspection Time | {inspection_time} |
| Round | {round_number} |
| Output Directory | {output_dir} |
| Inspector | Project Structure Scan Supervisor (Automated) |

---

## Results

| Check ID | Category | Check Item | Status | Evidence / Notes |
|----------|----------|------------|--------|------------------|
| CHK-01 | Configuration | Trigger config exists with >= 3 triggers | {status} | {evidence} |
| CHK-02 | RACI | RACI matrix with >= 6 roles | {status} | {evidence} |
| CHK-03 | Capabilities | Skills list >= 9 items | {status} | {evidence} |
| CHK-04 | Knowledge | Knowledge base >= 7 items | {status} | {evidence} |
| CHK-05 | Tools | Tools list >= 5 tools | {status} | {evidence} |
| CHK-06 | Tools | MCP tools >= 3 tools | {status} | {evidence} |
| CHK-07 | Templates | All 6 template files exist, each > 100 bytes | {status} | {evidence} |
| CHK-08 | SOP | SOP defines 5 phases with sub-steps | {status} | {evidence} |
| CHK-09 | Quality | DoD has >= 12 checkable items | {status} | {evidence} |
| CHK-10 | Quality | DoR has >= 8 prerequisites | {status} | {evidence} |
| CHK-11 | Logging | Conversation log has Phase 1-3 dialogue | {status} | {evidence} |
| CHK-12 | Logging | Work log has timestamped entries | {status} | {evidence} |
| CHK-13 | Quality | DoD self-verification passed | {status} | {evidence} |
| CHK-14 | Output | OUT-01 exists, non-empty, no placeholders | {status} | {evidence} |
| CHK-15 | Output | OUT-02 exists, valid Mermaid | {status} | {evidence} |
| CHK-16 | Output | OUT-03 exists, >= 1 pattern identified | {status} | {evidence} |
| CHK-17 | Output | OUT-04 covers internal + third-party | {status} | {evidence} |
| CHK-18 | Output | OUT-05 all modules have descriptions | {status} | {evidence} |
| CHK-19 | Output | OUT-06 exists, > 500 bytes, executive summary | {status} | {evidence} |
| CHK-20 | Memory | SQLite DB exists and has entries | {status} | {evidence} |
| CHK-21 | Research | research/ has >= 1 file | {status} | {evidence} |
| CHK-22 | Dialogue | phase1-questions.md and phase3-questions.md exist | {status} | {evidence} |

---

## Summary

| Metric | Value |
|--------|-------|
| Total Checks | 22 |
| Passed | {passed_count} |
| Failed | {failed_count} |
| Pass Rate | {pass_rate}% |

---

## Failed Items — Remediation Required

| Check ID | Check Item | Failure Reason | Suggested Remediation |
|----------|------------|----------------|----------------------|
{failed_items_rows}

*(If no items failed, this section will read: "No failed items. All checks passed.")*

---

## Conclusion

**Verdict: {verdict}**

- **ALL PASSED** — All 22 checks passed. Output is ready for PM Agent handoff.
- **NEEDS REMEDIATION** — One or more checks failed. Failed items have been sent back to the Scan Agent for correction. Re-inspection will follow.
- **ESCALATED** — Maximum remediation rounds (3) reached with remaining failures. Escalating to human operator / PM Agent for manual review.
