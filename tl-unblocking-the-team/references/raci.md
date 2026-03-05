# RACI Matrix -- Unblocking the Team (TL-DEV-004)

## Matrix

| Task / Deliverable | Technical Lead (TL) | Project Manager (PM) | IT Architect (SA) | Dev Lead (DL) | QA Lead | Scrum Master |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Identify and triage blockers | R | I | I | C | C | C |
| Investigate root causes | R | I | C | C | I | I |
| Debug complex issues | R | I | C | C | I | I |
| Resolve cross-team dependencies | R | A | C | C | I | C |
| Provide technical guidance | R | I | C | C | I | I |
| Document resolutions | R | I | I | C | I | I |
| Define escalation procedures | R | A | C | C | C | C |
| Produce unblocking report | R | A | I | I | I | I |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Upstream Inputs (Wave 10 -- IT Architect)

| Input | Source Task | Description |
|:---|:---|:---|
| Architecture Design | IA-REQ-001 | System context for understanding dependencies and integration points |

## Downstream Task Notification

Upon completion, send to PM Agent:
1. Unblocking the Team report file path
2. This RACI matrix
3. Supervisor inspection report
