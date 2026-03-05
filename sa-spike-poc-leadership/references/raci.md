# RACI Matrix — Spike & PoC Leadership (IA-DEV-003)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Tech Lead (TL) | Dev Lead (DL) | Developer (Dev) | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define spike objectives & hypothesis | R | A | C | C | I | I |
| Define success/failure criteria | R | A | C | C | I | I |
| Research approaches & options | R | I | C | I | I | I |
| Build PoC code | R | I | C | C | C | I |
| Execute benchmarks & experiments | R | I | C | C | C | I |
| Produce technology comparison | R | I | C | C | I | C |
| Produce recommendation & decision | R | A | C | C | I | C |
| Update risk assessment | R | A | C | C | I | C |
| Produce Spike/PoC report | R | A | C | C | I | I |
| Review & approve findings | C | A | R | R | I | I |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Upstream Inputs

| Input | Source Task | Description |
|:---|:---|:---|
| Architecture Design | IA-REQ-001 | C4 diagrams, integration views providing spike context |
| Technical Guidance | IA-DEV-001 | Pattern catalog and guidance |
| Solution Architecture Document (SAD) | SA-REQ-001 | Comprehensive solution architecture |
| Technology Blueprint | SA-REQ-004 | Full technology stack definition |
| ARB Feedback | SA-REQ-005 | Architecture Review Board notes |

## Downstream Task Notification (Technical Lead)

Upon completion, send to PM Agent:
1. Spike/PoC report file path
2. This RACI matrix
3. Supervisor inspection report

PM Agent uses this matrix to trigger the following downstream tasks:

| Downstream Task | Role | Description |
|:---|:---|:---|
| TL-DEV-001 | Technical Lead | Code Review & Quality Gatekeeping |
| TL-DEV-002 | Technical Lead | Hands-On Development |
| TL-DEV-003 | Technical Lead | Technical Decision Making |
| TL-DEV-004 | Technical Lead | Unblocking the Team |
| TL-DEV-005 | Technical Lead | Technical Debt Governance |
