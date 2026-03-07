# RACI Matrix — Non-Functional Requirements (IA-REQ-002)

## Matrix

| Task / Deliverable | System Architect (SA) | Project Manager (PM) | Business Analyst (BA) | Tech Lead (TL) | Dev Lead (DL) | Security Architect (SecA) | SRE/DevOps |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Define NFR scope | R | A | C | C | I | C | C |
| Define performance targets | R | A | C | C | I | I | C |
| Define scalability requirements | R | I | I | C | C | I | C |
| Define security requirements | R | I | I | C | I | C | I |
| Define availability/DR targets | R | I | I | C | C | C | C |
| Define maintainability standards | R | I | I | C | C | I | C |
| Define observability requirements | R | I | I | C | C | I | C |
| Produce NFR report | R | A | I | C | C | C | C |
| Review & approve | C | A | I | R | R | R | R |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I | I |

## Legend

- **R** = Responsible — Does the work
- **A** = Accountable — Approves / owns the outcome
- **C** = Consulted — Provides input before decisions
- **I** = Informed — Notified of outcomes

## Downstream Task Notification

Upon completion, send to PM Agent:
1. NFR specification report file path
2. This RACI matrix
3. Supervisor inspection report (if applicable)

PM Agent uses this matrix to invoke downstream responsible agents.
