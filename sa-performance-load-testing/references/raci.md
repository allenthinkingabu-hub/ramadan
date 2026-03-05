# RACI Matrix -- Performance & Load Testing (IA-QA-001)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | QA Lead | Tech Lead (TL) | Dev Lead (DL) | Performance Engineer |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define test scope & NFR targets | R | A | C | C | I | C |
| Design workload models | R | I | C | C | I | C |
| Define load test scenarios | R | I | C | C | I | C |
| Define stress test scenarios | R | I | C | C | I | C |
| Define soak/spike test scenarios | R | I | C | C | I | C |
| Establish benchmark thresholds | R | A | C | C | C | C |
| Design test environment specs | R | I | I | C | C | C |
| Produce acceptance criteria matrix | R | A | C | C | I | C |
| Produce Performance Testing report | R | A | C | C | I | C |
| Review & approve final report | C | A | R | R | I | R |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Downstream Task Notification (Technical Lead)

Upon completion, send to PM Agent:
1. Performance Load Testing report file path
2. This RACI matrix
3. Supervisor inspection report

PM Agent uses this matrix to trigger the following downstream tasks:

| Downstream Task | Role | Description |
|:---|:---|:---|
| TL-QA-001 | Technical Lead | Critical Bug Investigation |
| TL-QA-002 | Technical Lead | Performance & Scalability Review |
| TL-QA-003 | Technical Lead | Release Candidate Validation |
| TL-QA-004 | Technical Lead | Technical Go/No-Go Input |
