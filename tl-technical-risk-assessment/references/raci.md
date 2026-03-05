# RACI Matrix — Technical Risk Assessment (TL-INC-004)

## Matrix

| Task / Deliverable | Technical Lead (TL) | Project Manager (PM) | IT Architect (SA) | Business Analyst (BA) | Dev Lead (DL) | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define risk assessment scope | R | A | C | I | C | C |
| Identify technical risks | R | I | C | I | C | C |
| Analyze external dependencies | R | I | C | I | C | I |
| Assess risk probability & impact | R | I | C | I | C | C |
| Develop mitigation strategies | R | A | C | I | C | C |
| Create dependency map | R | I | C | I | C | I |
| Define risk monitoring framework | R | A | C | I | C | I |
| Produce Technical Risk Assessment report | R | A | C | I | I | I |
| Review & approve final report | C | A | R | I | C | C |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Upstream Inputs (Wave 10 — IT Architect)

| Input | Source Task | Description |
|:---|:---|:---|
| Technical Discovery Report | IA-INC-001 | Technology landscape, current state analysis |
| Feasibility Analysis | IA-INC-002 | Technical feasibility assessment |
| Proof of Concept Results | IA-INC-003 | PoC findings, validated assumptions |
| NFR Analysis | IA-INC-004 | Non-functional requirements analysis |
| Technology Landscape Assessment | IA-INC-005 | Technology ecosystem evaluation |
| Risk Assessment | IA-INC-006 | IT Architect's risk identification |
| Integration Strategy | IA-INC-007 | System integration approach |
| Architecture Patterns Evaluation | IA-INC-008 | Architecture pattern recommendations |

## Downstream Task Notification (Wave 12 — Software Engineer)

Upon completion, send to PM Agent:
1. Technical Risk Assessment report file path
2. This RACI matrix
3. Supervisor inspection report

PM Agent uses this matrix to trigger downstream tasks:

| Downstream Task | Role | Description |
|:---|:---|:---|
| SE-INC-001 | Software Engineer | SE Inception Task 1 |
| SE-INC-002 | Software Engineer | SE Inception Task 2 |
| SE-INC-003 | Software Engineer | SE Inception Task 3 |
| SE-INC-004 | Software Engineer | SE Inception Task 4 |
| SE-INC-005 | Software Engineer | SE Inception Task 5 |
