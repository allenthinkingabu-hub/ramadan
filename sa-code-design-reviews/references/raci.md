# RACI Matrix — Code & Design Reviews (IA-DEV-002)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Tech Lead (TL) | Dev Lead (DL) | Developer (Dev) | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define review scope & criteria | R | I | C | C | I | C |
| Conduct code review | R | I | C | C | C | I |
| Conduct PR review | R | I | C | C | C | I |
| Conduct design review | R | I | C | C | I | C |
| Assess architecture compliance | R | I | C | C | I | C |
| Assess NFR compliance | R | I | C | I | I | C |
| Produce compliance matrix | R | I | C | C | I | C |
| Produce remediation plan | R | A | C | C | I | I |
| Produce Review report | R | A | C | C | I | I |
| Review & approve final report | C | A | R | R | I | I |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Upstream Inputs

| Input | Source Task | Description |
|:---|:---|:---|
| Architecture Design | IA-REQ-001 | C4 diagrams, integration views as compliance baseline |
| Technical Guidance | IA-DEV-001 | Pattern catalog, architecture-to-code mapping |
| Solution Architecture Document (SAD) | SA-REQ-001 | Comprehensive solution architecture |
| Technology Blueprint | SA-REQ-004 | Full technology stack definition |
| Coding Standards | TL-REQ-002 | Coding standards and conventions |

## Downstream Task Notification (Technical Lead)

Upon completion, send to PM Agent:
1. Code & Design Review report file path
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
