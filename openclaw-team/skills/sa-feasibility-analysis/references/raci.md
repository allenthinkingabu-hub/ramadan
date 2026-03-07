# RACI Matrix — Feasibility Analysis (IA-INC-002)

## Matrix

| Task / Deliverable | System Architect (SA) | Project Manager (PM) | Business Analyst (BA) | Tech Lead (TL) | Finance Lead (FL) | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define feasibility scope & objectives | R | A | C | C | I | I |
| Technical feasibility assessment | R | I | I | C | I | C |
| Operational feasibility assessment | R | I | C | C | I | I |
| Economic feasibility assessment | R | A | C | I | C | I |
| Schedule feasibility assessment | R | A | C | C | I | I |
| Legal & compliance feasibility | R | I | C | I | I | C |
| Risk analysis & mitigation strategies | R | A | C | C | C | C |
| Produce Feasibility Analysis report | R | A | I | C | C | C |
| Review & approve final report | C | A | I | R | R | R |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible — Does the work
- **A** = Accountable — Approves / owns the outcome
- **C** = Consulted — Provides input before decisions
- **I** = Informed — Notified of outcomes

## Downstream Task Notification

Upon completion, send to PM Agent:
1. Feasibility Analysis report file path
2. This RACI matrix
3. Supervisor inspection report (if applicable)

PM Agent uses this matrix to invoke downstream responsible agents.
