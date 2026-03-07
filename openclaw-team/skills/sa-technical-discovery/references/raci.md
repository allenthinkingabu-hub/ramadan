# RACI Matrix — Technical Discovery (IA-INC-001)

## Matrix

| Task / Deliverable | System Architect (SA) | Project Manager (PM) | Business Analyst (BA) | Tech Lead (TL) | Infrastructure Engineer (IE) | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define discovery scope & objectives | R | A | C | C | I | I |
| Assess current technology stack | R | I | C | C | C | I |
| Evaluate system architecture landscape | R | I | I | C | C | I |
| Assess infrastructure capabilities | R | I | I | C | R | I |
| Identify integration points & dependencies | R | I | C | C | C | I |
| Evaluate security posture | R | I | I | I | C | C |
| Document technical constraints & risks | R | A | C | C | C | C |
| Produce Technical Discovery report | R | A | I | C | C | C |
| Review & approve final report | C | A | I | R | R | R |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible — Does the work
- **A** = Accountable — Approves / owns the outcome
- **C** = Consulted — Provides input before decisions
- **I** = Informed — Notified of outcomes

## Downstream Task Notification

Upon completion, send to PM Agent:
1. Technical Discovery report file path
2. This RACI matrix
3. Supervisor inspection report (if applicable)

PM Agent uses this matrix to invoke downstream responsible agents.
