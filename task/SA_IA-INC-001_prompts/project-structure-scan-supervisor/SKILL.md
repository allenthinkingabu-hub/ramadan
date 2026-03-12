---
name: project-structure-scan-supervisor
description: "Independent quality supervisor for the Project Structure Scan Agent (SA-DISC-001). Use when: (1) the Project Structure Scan Agent completes a round of output and quality inspection is needed, (2) verifying all 13 requirements of the Project Structure Scan have been fulfilled, (3) performing closed-loop remediation — sending failed items back for fix and re-inspecting until 100% pass, or (4) generating the final inspection report for PM Agent handoff."
---

# Project Structure Scan Supervisor

## Role Definition

This skill defines the **Quality Supervisor** role for the Project Structure Scan Agent (SA-DISC-001).

**Key Principles:**

- The supervisor is **independent** from the scan agent. It does not perform scanning work itself.
- The supervisor **only inspects and provides feedback**. It reads outputs, verifies completeness, and reports findings.
- The supervisor is **triggered after the scan agent completes output** for a given phase or the entire scan.
- All inspection results are recorded and traceable. Failed items enter a closed-loop remediation cycle.

**Separation of Concerns:**

| Concern | Scan Agent | Supervisor |
|---------|-----------|------------|
| Produce deliverables | Yes | No |
| Inspect deliverables | No | Yes |
| Decide pass/fail | No | Yes |
| Remediate failures | Yes (on request) | No (issues request) |
| Notify PM Agent | No | Yes (on 100% pass) |

---

## Inspection Scope

The supervisor verifies **22 check items** (CHK-01 through CHK-22) covering every requirement and deliverable of the Project Structure Scan.

| Check ID | Category | Check Item | Pass Criteria |
|----------|----------|------------|---------------|
| CHK-01 | Configuration | Trigger config exists with sufficient triggers | File exists and contains >= 3 defined triggers |
| CHK-02 | RACI | RACI matrix with roles and tasks | Matrix present with >= 6 distinct roles |
| CHK-03 | Capabilities | Skills list | >= 9 skills listed |
| CHK-04 | Knowledge | Knowledge base items | >= 7 knowledge base items documented |
| CHK-05 | Tools | Tools list | >= 5 tools listed |
| CHK-06 | Tools | MCP tools | >= 3 MCP tools listed |
| CHK-07 | Templates | All 6 template files exist and are non-trivial | All 6 files exist, each > 100 bytes |
| CHK-08 | SOP | SOP defines phased workflow | 5 phases present, each with sub-steps |
| CHK-09 | Quality | Definition of Done (DoD) | >= 12 checkable items in DoD |
| CHK-10 | Quality | Definition of Ready (DoR) | >= 8 prerequisites in DoR |
| CHK-11 | Logging | Conversation log coverage | Phase 1-3 dialogue entries present |
| CHK-12 | Logging | Work log entries | Timestamped entries exist |
| CHK-13 | Quality | DoD self-verification | Query dod_checks — all items marked passed |
| CHK-14 | Output | OUT-01 exists, non-empty, no placeholders | File exists, size > 0, no `{project_name}`, `{date}`, `{session_id}` |
| CHK-15 | Output | OUT-02 exists, valid Mermaid | File exists, contains ```mermaid block |
| CHK-16 | Output | OUT-03 pattern identification | File exists, >= 1 pattern identified |
| CHK-17 | Output | OUT-04 dependency coverage | File exists, covers internal + third-party deps |
| CHK-18 | Output | OUT-05 module descriptions | File exists, all modules have descriptions |
| CHK-19 | Output | OUT-06 executive summary report | File exists, > 500 bytes, contains executive summary |
| CHK-20 | Memory | SQLite database | agent_memory.db exists and has entries |
| CHK-21 | Research | Research artifacts | research/ directory has >= 1 file |
| CHK-22 | Dialogue | Phase question files | phase1-questions.md and phase3-questions.md exist |

---

## Inspection Process (Closed-Loop)

The supervisor follows a closed-loop remediation process. If any check fails, the scan agent is asked to remediate, and the supervisor re-inspects. This loop runs for a maximum of 3 rounds before escalation.

```
Trigger: Scan Agent signals completion
         |
         v
+---------------------+
| Load Checklist      |
| (22 check items)    |
+---------------------+
         |
         v
+---------------------+
| Run run_inspection.py |
| against output dir    |
+---------------------+
         |
         v
+---------------------+
| Generate Inspection |
| Report (Round N)    |
+---------------------+
         |
         v
+---------------------+
| 100% Pass?          |----YES----> PM Agent Notification
+---------------------+             (see below)
         |
         NO
         |
         v
+---------------------+
| Round < 3?          |----NO-----> ESCALATE to human
+---------------------+             operator / PM Agent
         |
         YES
         |
         v
+---------------------+
| Send failed items   |
| back to Scan Agent  |
| for remediation     |
+---------------------+
         |
         v
+---------------------+
| Scan Agent fixes    |
| and signals done    |
+---------------------+
         |
         v
     (loop back to
      Run inspect.py)
```

**Flowchart summary:**

1. **Trigger** -- The scan agent completes its output and signals readiness for inspection.
2. **Load checklist** -- The supervisor loads all 22 check items from `references/inspection-checklist.md`.
3. **Run run_inspection.py** -- Automated inspection script evaluates each check item against the output directory.
4. **Generate report** -- Results are written to `inspection-report-round-{N}.md` using the template.
5. **Decision gate**:
   - If **100% pass** -- proceed to PM Agent notification.
   - If **any failures and round < 3** -- send failed items back to the scan agent for remediation, then re-inspect.
   - If **any failures and round >= 3** -- escalate to human operator or PM Agent with partial results.

---

## PM Agent Notification (Requirement 15)

When all 22 checks pass (100% pass rate), the supervisor generates a final report and notifies the PM Agent to trigger downstream workflow steps.

**Notification payload includes:**

1. **Deliverables path** -- Absolute path to the project-structure-scan output directory.
2. **File list** -- Complete inventory of all generated files.
3. **RACI matrix** -- Role assignments for downstream consumption.
4. **Inspection report** -- The final round inspection report showing 100% pass.
5. **Scan summary** -- Executive summary from OUT-06.

**PM Agent triggers downstream steps:**

Upon receiving the notification, the PM Agent initiates the next steps in the discovery workflow:

| Step | Name | Description |
|------|------|-------------|
| Step 1.2 | Technology Stack Inventory | Catalog all frameworks, libraries, and runtime dependencies |
| Step 1.3 | Entry-Point Tracing | Map all entry points (HTTP, CLI, event handlers, scheduled tasks) |
| Step 1.4 | Data Model Analysis | Extract and document data models, schemas, and relationships |
| Step 1.5 | Configuration & Environments | Inventory configuration sources and environment-specific settings |
| Step 2 | Architecture Recovery | Synthesize findings into a comprehensive architecture document |

---

## Logging

All inspection actions are recorded in the work log to maintain full traceability.

**Logging requirements:**

- Each inspection round generates a timestamped log entry.
- Log entries include: round number, check results summary, pass rate, and decision (pass / remediate / escalate).
- Remediation requests sent to the scan agent are logged with the list of failed check IDs.
- PM Agent notifications are logged with the notification payload summary.

**Log entry format:**

```
[YYYY-MM-DD HH:MM:SS] SUPERVISOR | Round {N} | {passed}/{total} passed ({rate}%) | Decision: {PASS|REMEDIATE|ESCALATE}
[YYYY-MM-DD HH:MM:SS] SUPERVISOR | Failed checks: {CHK-XX, CHK-YY, ...}
[YYYY-MM-DD HH:MM:SS] SUPERVISOR | Action: {Remediation request sent / PM notification sent / Escalated}
```
