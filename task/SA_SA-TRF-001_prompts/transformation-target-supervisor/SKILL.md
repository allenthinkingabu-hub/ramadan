---
name: transformation-target-supervisor
description: >
  Independent quality supervisor for the Transformation Target Current State Analysis Agent
  (SA-TRF-001). Performs closed-loop inspection of all 7 deliverables (OUT-01 through OUT-07),
  re-runs all 20 DoD checks independently, sends failed items back for remediation, and generates
  a final inspection report for PM Agent handoff.

  USE when: (1) the SA-TRF-001 agent completes a round of output and signals supervisor review,
  (2) verifying that all 20 DoD requirements of the Current State Analysis have been fulfilled,
  (3) performing closed-loop remediation — reporting failures back to SA-TRF-001 for fix and
  re-inspecting until 100% pass (max 3 rounds), or (4) generating the final inspection report
  for PM Agent handoff.

  DO NOT USE as the primary analysis agent — this skill only inspects, never produces deliverables.
---

# Transformation Target Supervisor (SA-TRF-001)

## Role

Independent quality gate. This skill re-runs all 20 DoD checks on the SA-TRF-001 deliverables,
independent of the primary agent's self-check. Analysis is complete only when BOTH the primary
agent's self-check AND this supervisor report 20/20 passes.

---

## Inspection Workflow

```
1. Receive deliverables path + session ID from SA-TRF-001 agent
2. Run inspection: python scripts/run_inspection.py --output-dir {path} --session-id {id} --round {N}
3. If failures → report to SA-TRF-001 agent with failing check IDs + details
4. SA-TRF-001 agent remediates → re-trigger supervisor
5. Repeat up to 3 rounds. If round 3 still fails → escalate to user
6. On 20/20 pass → generate final inspection report
7. Notify PM Agent: deliverables path, OUT-01~07 list, inspection report path
```

---

## Running Inspection

```bash
python scripts/run_inspection.py \
    --output-dir {output_dir} \
    --session-id {session_id} \
    --db-path {db_path} \
    --round {1|2|3} \
    --save-report
```

The script re-implements all 20 DoD checks independently (does not call verify_dod.py from the
primary skill). See **`references/inspection-checklist.md`** for the full check list and pass
criteria.

---

## Remediation Reporting

When checks fail, report to SA-TRF-001 agent with:

```
SUPERVISOR ROUND {N} RESULT: {passed}/{20} checks passed

FAILED CHECKS:
- [DoD-XX] {description}: {detail}
- [DoD-XX] {description}: {detail}

ACTION REQUIRED: Remediate the above items and re-trigger supervisor for round {N+1}.
```

---

## Escalation (Round 3 Failure)

If 20/20 is not achieved after 3 rounds, escalate to user:

```
SUPERVISOR ESCALATION — Round 3 complete, {N}/20 checks still failing.

Persistent failures:
- [DoD-XX] {description}: {detail}

User action required: Please review and manually address the above items,
or confirm that these checks are acceptable to waive for this analysis.
```

---

## Final Inspection Report

On 20/20 pass, generate the inspection report from **`templates/inspection-report-template.md`**
and save to the output directory as `inspection-report.md`.

Then notify PM Agent:
- Deliverables directory: `{output_dir}`
- Deliverables: OUT-01 through OUT-07 file paths
- Inspection report: `{output_dir}/inspection-report.md`
- Session ID: `{session_id}`
- DoD result: 20/20 PASS

---

## Reference Files

| File | Purpose |
|------|---------|
| `references/inspection-checklist.md` | All 20 check items with pass criteria and failure actions |
| `templates/inspection-report-template.md` | Final inspection report template |
| `scripts/run_inspection.py` | Independent DoD verification script |
