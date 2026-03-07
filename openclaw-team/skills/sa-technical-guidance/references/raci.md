# RACI Matrix — Technical Guidance (IA-DEV-001)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Tech Lead (TL) | Dev Lead (DL) | Developer (Dev) | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Identify guidance needs | R | I | C | C | C | I |
| Analyze architecture context | R | I | C | C | I | I |
| Research design patterns | R | I | C | I | I | I |
| Produce pattern catalog | R | I | C | C | I | I |
| Produce architecture-to-code mapping | R | I | C | C | I | I |
| Provide implementation guidance | R | I | C | C | C | C |
| Document guidance decisions | R | I | C | C | I | I |
| Produce Technical Guidance report | R | A | C | C | I | I |
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
| Architecture Design | IA-REQ-001 | C4 diagrams, deployment views, integration views |
| Solution Architecture Document (SAD) | SA-REQ-001 | Comprehensive solution architecture |
| Technology Blueprint | SA-REQ-004 | Full technology stack definition |
| ARB Feedback | SA-REQ-005 | Architecture Review Board notes |

## Downstream Task Notification (Technical Lead)

Upon completion, send to PM Agent:
1. Technical Guidance report file path
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
