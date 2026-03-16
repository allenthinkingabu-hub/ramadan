# RACI Matrix — Transformation Target Current State Analysis (SA-TRF-001)

> **Purpose 1**: The AI Agent loads this file on startup to know all stakeholders.
> **Purpose 2**: After task completion, this matrix is sent to the PM Agent to trigger downstream tasks.
> Edit this file to update roles, tasks, and downstream triggers.

---

## Role Definitions

| Role ID | Role Name | Description |
|---------|-----------|-------------|
| R-01 | PM Agent | Project Manager AI Agent — assigns tasks, tracks progress, triggers downstream |
| R-02 | SA Agent (TRF) | Transformation Target Current State Analysis AI Agent (this skill) |
| R-03 | Supervisor Agent | Transformation Target Supervisor AI Agent — independent quality inspection |
| R-04 | Transformation Design Agent | Receives OUT-07 to design the transformation approach |
| R-05 | Test Strategy Agent | Receives OUT-05 + OUT-07 to design test strategy for transformation |
| R-06 | Tech Debt Agent | Receives OUT-06 to prioritize and plan debt remediation |
| R-07 | Developer | Human engineer executing the transformation |
| R-08 | Architect | Human architect reviewing transformation design |
| R-09 | QA Lead | Human QA reviewing test strategy |

---

## RACI Matrix

> **R** = Responsible (does the work) | **A** = Accountable (owns the outcome) | **C** = Consulted | **I** = Informed

| Task | PM Agent | SA Agent (TRF) | Supervisor | Design Agent | Test Agent | Debt Agent | Developer | Architect | QA Lead |
|------|:--------:|:--------------:|:----------:|:------------:|:----------:|:----------:|:---------:|:---------:|:-------:|
| Assign SA-TRF-001 task | R/A | I | - | - | - | - | - | - | - |
| Target Intake (Step 0) | I | R/A | - | - | - | - | C | - | - |
| Understand Purpose (Step 1) | I | R/A | - | - | - | - | C | C | - |
| Understand Target (Step 2) | I | R/A | - | - | - | - | C | C | - |
| Research & Questions (Step 3) | I | R/A | - | - | - | - | C | C | - |
| Investigate & Produce OUT-01~06 (Step 4) | I | R/A | - | - | - | - | C | - | - |
| Produce OUT-07 Current State Report | I | R/A | - | I | I | I | C | C | - |
| DoD Self-Verification (Step 5) | I | R/A | - | - | - | - | - | - | - |
| Quality Inspection (Supervisor) | I | C | R/A | - | - | - | - | - | - |
| PM Agent Notification | R/A | I | I | - | - | - | - | - | - |
| Transformation Design (downstream) | A | I | - | R | C | C | C | C | - |
| Test Strategy Planning (downstream) | A | I | - | - | R | C | C | - | R |
| Tech Debt Remediation Planning | A | I | - | C | - | R | C | C | - |

---

## Downstream Task Triggers (PM Agent uses this after SA-TRF-001 completes)

| Step | Task Name | Task ID | Trigger Condition | Input from SA-TRF-001 |
|------|-----------|---------|-------------------|-----------------------|
| Next | Transformation Design | SA-TRF-002 | SA-TRF-001 completed, supervisor passed | OUT-07 path, all OUT-01~06 paths |
| Next | Test Strategy Planning | SA-TST-001 | SA-TRF-001 completed | OUT-05 (test coverage), OUT-07 (constraints) |
| Optional | Tech Debt Remediation | SA-TDB-001 | OUT-06 has Critical/High severity items | OUT-06 path |
| Parallel | Architecture Review | SA-ARC-001 | SA-TRF-001 completed | OUT-03 (dependency map), OUT-07 |
