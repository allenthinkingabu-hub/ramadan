# RACI Matrix -- Technical Decision Making (TL-DEV-003)

## Matrix

| Task / Deliverable | Technical Lead (TL) | Project Manager (PM) | IT Architect (SA) | Dev Lead (DL) | QA Lead | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Identify decision needs | R | I | C | C | I | I |
| Research alternatives | R | I | C | C | I | C |
| Evaluate trade-offs | R | I | C | C | C | C |
| Document ADRs | R | A | C | I | I | I |
| Select implementation approach | R | A | C | C | I | C |
| Assess risk and impact | R | I | C | C | C | C |
| Communicate decisions | R | A | I | C | C | I |
| Produce decision register | R | A | I | I | I | I |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Upstream Inputs (Wave 10 -- IT Architect)

| Input | Source Task | Description |
|:---|:---|:---|
| Architecture Design | IA-REQ-001 | Architecture decisions for alignment and consistency |

## Downstream Task Notification

Upon completion, send to PM Agent:
1. Technical Decision Making report file path
2. This RACI matrix
3. Supervisor inspection report
