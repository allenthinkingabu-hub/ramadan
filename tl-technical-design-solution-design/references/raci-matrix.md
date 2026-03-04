# RACI Matrix Configuration

## Task: TL-REQ-001 — Technical Design & Solution Design

### RACI Definitions
- **R** (Responsible): Does the work to complete the task
- **A** (Accountable): Ultimately answerable for the correct completion
- **C** (Consulted): Provides input and expertise (two-way communication)
- **I** (Informed): Kept up-to-date on progress and outcomes (one-way communication)

### RACI Matrix

| Task / Activity | Technical Lead (TL) Agent | Project Manager (PM) Agent | Solution Architect (SA) Agent | Business Analyst (BA) Agent | Developer (DEV) Agent | QA Agent |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| Understand task purpose & scope | **R** | A | C | C | I | I |
| Gather business requirements | **R** | I | C | **C** | I | I |
| Review architecture decisions | **R** | I | **C** | I | I | I |
| Review technology stack selections | **R** | I | **C** | I | C | I |
| Research industry best practices | **R** | I | C | I | I | I |
| Produce component diagrams | **R** | I | C | I | I | I |
| Produce sequence diagrams | **R** | I | C | I | C | I |
| Produce detailed technical design doc | **R/A** | I | C | I | I | I |
| Design data models & schemas | **R** | I | C | I | C | I |
| Define API specifications | **R** | I | C | I | C | I |
| Design cross-cutting concerns | **R** | I | C | I | I | I |
| Design deployment architecture | **R** | I | C | I | I | I |
| Evaluate alternatives (ADR) | **R** | I | C | I | C | I |
| Define testing strategy | **R** | I | I | I | C | **C** |
| DoD self-verification | **R** | I | I | I | I | I |
| Supervisor inspection | I | I | I | I | I | I |
| Submit completion to PM | I | **R** | I | I | I | I |
| Trigger downstream DEV tasks | I | **R/A** | I | I | **R** | I |

### Downstream Task Triggers

Upon completion of TL-REQ-001, the PM Agent uses this RACI matrix to trigger:

| Downstream Task | Responsible Agent | Trigger Condition |
|:--|:--|:--|
| Feature Implementation | DEV Agent | Technical design approved (Supervisor 100% pass) |
| Test Plan Creation | QA Agent | Technical design approved |
| API Contract Review | DEV Agent | API specifications finalized |
| Database Migration Planning | DEV Agent | Data model design finalized |

### Stakeholder Contact Points

| Role | Agent Name | Communication Channel |
|:--|:--|:--|
| Project Manager | PM Agent | Task assignment, status updates, completion notification |
| Solution Architect | SA Agent | Architecture consultation, design review |
| Business Analyst | BA Agent | Requirements clarification |
| Developer | DEV Agent | Implementation feasibility consultation |
| QA | QA Agent | Testing strategy consultation |
| Supervisor | TL-Technical-Design-Supervisor Agent | Quality inspection |

## Configuration Notes

- Add new roles by adding columns to the RACI matrix
- Add new activities by adding rows
- Update downstream triggers when new dependent tasks are identified
- This matrix is sent to the PM Agent upon task completion for downstream coordination
