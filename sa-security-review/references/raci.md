# RACI Matrix -- Security Review (IA-QA-002)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Tech Lead (TL) | QA Lead | Security Architect |
|:---|:---:|:---:|:---:|:---:|:---:|
| Define security review scope & objectives | R | A | C | C | C |
| Produce Threat Model | R | I | C | C | C |
| Produce Vulnerability Assessment | R | I | C | C | C |
| Produce Security Policy Compliance | R | I | C | C | C |
| Produce Security Test Plan | R | I | C | C | C |
| Produce Security Review report | R | A | C | C | C |
| Review & approve final report | C | A | R | R | R |
| Trigger downstream tasks via PM Agent | I | R | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Downstream Task Notification (Technical Lead)

Upon completion, send to PM Agent:
1. Security Review report file path
2. This RACI matrix
3. Supervisor inspection report

PM Agent uses this matrix to trigger the following downstream tasks:

| Downstream Task | Role | Description |
|:---|:---|:---|
| TL-QA-001 | Technical Lead | Critical Bug Investigation |
| TL-QA-002 | Technical Lead | Performance & Scalability Review |
| TL-QA-003 | Technical Lead | Release Candidate Validation |
| TL-QA-004 | Technical Lead | Technical Go/No-Go Input |
