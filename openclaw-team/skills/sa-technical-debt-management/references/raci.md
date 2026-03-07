# RACI Matrix — Technical Debt Management (IA-DEV-004)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Tech Lead (TL) | Dev Lead (DL) | Developer (Dev) | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define debt assessment scope | R | A | C | C | I | I |
| Identify and catalog debt items | R | I | C | C | C | C |
| Assess debt severity and impact | R | I | C | C | I | C |
| Prioritize debt items | R | A | C | C | I | I |
| Develop remediation strategy | R | A | C | C | I | I |
| Establish governance policy | R | A | C | C | I | C |
| Produce Technical Debt report | R | A | C | C | I | I |
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
| Architecture Design | IA-REQ-001 | C4 diagrams for architecture drift assessment |
| Technical Guidance | IA-DEV-001 | Pattern catalog for pattern compliance |
| Code & Design Reviews | IA-DEV-002 | Review findings identifying debt items |
| Spike/PoC Leadership | IA-DEV-003 | Risk assessment and technology findings |
| Solution Architecture Document (SAD) | SA-REQ-001 | Comprehensive solution architecture |
| Technology Blueprint | SA-REQ-004 | Technology stack for dependency assessment |

## Downstream Task Notification (Technical Lead)

Upon completion, send to PM Agent:
1. Technical Debt report file path
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
