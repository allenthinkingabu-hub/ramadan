# RACI Matrix — Technology Selection (IA-INC-003)

## Matrix

| Task / Deliverable | System Architect (SA) | Project Manager (PM) | Business Analyst (BA) | Tech Lead (TL) | Dev Lead (DL) | Infrastructure Engineer (IE) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define evaluation scope | R | A | C | C | C | I |
| Evaluate technology candidates | R | I | I | C | C | I |
| Conduct weighted scoring | R | I | I | C | C | I |
| Assess vendor/licensing | R | A | C | I | I | I |
| Perform TCO analysis | R | A | C | I | I | C |
| Produce recommendations | R | A | C | C | C | I |
| Review & approve | C | A | I | R | R | I |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible — Does the work
- **A** = Accountable — Approves / owns the outcome
- **C** = Consulted — Provides input before decisions
- **I** = Informed — Notified of outcomes

## Downstream Task Notification

Upon completion, send to PM Agent:
1. Technology Selection report file path
2. This RACI matrix
3. Supervisor inspection report (if applicable)

PM Agent uses this matrix to invoke downstream responsible agents.
