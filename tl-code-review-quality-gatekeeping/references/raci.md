# RACI Matrix -- Code Review & Quality Gatekeeping (TL-DEV-001)

## Matrix

| Task / Deliverable | Technical Lead (TL) | Project Manager (PM) | IT Architect (SA) | Dev Lead (DL) | QA Lead | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define review standards & checklists | R | A | C | C | C | C |
| Define quality gate criteria | R | A | C | C | C | I |
| Configure automated checks | R | I | C | C | I | C |
| Conduct PR reviews | R | I | I | C | I | I |
| Enforce architectural compliance | R | I | C | C | I | I |
| Track review metrics & KPIs | R | A | I | I | C | I |
| Escalate critical findings | R | I | C | C | I | C |
| Produce quality gatekeeping report | R | A | I | C | C | I |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Upstream Inputs (Wave 10 -- IT Architect)

| Input | Source Task | Description |
|:---|:---|:---|
| Architecture Design | IA-REQ-001 | C4 diagrams, integration views, NFR alignment for compliance checks |

## Downstream Task Notification

Upon completion, send to PM Agent:
1. Code Review Quality Gatekeeping report file path
2. This RACI matrix
3. Supervisor inspection report
