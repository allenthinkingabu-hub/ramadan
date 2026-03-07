# RACI Matrix -- Hands-On Development (TL-DEV-002)

## Matrix

| Task / Deliverable | Technical Lead (TL) | Project Manager (PM) | IT Architect (SA) | Dev Lead (DL) | QA Lead | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Identify critical path features | R | A | C | C | I | I |
| Implement reference patterns | R | I | C | C | I | I |
| Develop critical path code | R | I | I | C | I | I |
| Write unit & integration tests | R | I | I | C | C | I |
| Document implementation patterns | R | I | C | C | I | I |
| Ensure architecture alignment | R | I | C | I | I | C |
| Produce development report | R | A | I | C | C | I |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Upstream Inputs (Wave 10 -- IT Architect)

| Input | Source Task | Description |
|:---|:---|:---|
| Architecture Design | IA-REQ-001 | C4 diagrams, integration views, NFR alignment for design conformance |

## Downstream Task Notification

Upon completion, send to PM Agent:
1. Hands-On Development report file path
2. This RACI matrix
3. Supervisor inspection report
