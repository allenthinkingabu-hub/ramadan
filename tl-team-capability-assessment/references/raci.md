# RACI Matrix — Team Capability Assessment (TL-INC-003)

## Matrix

| Task / Deliverable | Technical Lead (TL) | Project Manager (PM) | IT Architect (SA) | HR / People Manager | Dev Lead (DL) | Scrum Master (SM) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define assessment scope & methodology | R | A | C | C | C | I |
| Gather team composition data | R | C | I | C | C | I |
| Assess individual skill levels | R | I | I | I | C | I |
| Identify required skills from project needs | R | I | C | I | C | I |
| Conduct gap analysis | R | I | C | I | C | I |
| Develop training recommendations | R | A | C | C | I | I |
| Develop hiring recommendations | R | A | I | R | I | I |
| Create knowledge transfer plan | R | I | C | I | C | I |
| Produce Team Capability Assessment report | R | A | I | C | I | I |
| Review & approve final report | C | A | I | C | C | I |
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
| Risk Assessment | IA-INC-006 | Technical risk identification |
| Integration Strategy | IA-INC-007 | System integration approach |
| Architecture Patterns Evaluation | IA-INC-008 | Architecture pattern recommendations |

## Downstream Task Notification (Wave 12 — Software Engineer)

Upon completion, send to PM Agent:
1. Team Capability Assessment report file path
2. This RACI matrix
3. Supervisor inspection report

PM Agent uses this matrix to trigger the following downstream tasks:

| Downstream Task | Role | Description |
|:---|:---|:---|
| SE-INC-001 | Software Engineer | SE Inception Task 1 |
| SE-INC-002 | Software Engineer | SE Inception Task 2 |
| SE-INC-003 | Software Engineer | SE Inception Task 3 |
| SE-INC-004 | Software Engineer | SE Inception Task 4 |
| SE-INC-005 | Software Engineer | SE Inception Task 5 |
