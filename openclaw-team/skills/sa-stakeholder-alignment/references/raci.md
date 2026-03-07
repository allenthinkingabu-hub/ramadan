# RACI Matrix -- Stakeholder Alignment (IA-INC-006)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Business Analyst (BA) | Tech Lead (TL) | Dev Lead (DL) | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Identify stakeholder landscape | R | A | C | C | I | C |
| Define workshop agenda & objectives | R | A | C | C | I | C |
| Facilitate alignment workshops | R | A | C | C | I | C |
| Produce stakeholder map | R | A | C | I | I | I |
| Produce decision criteria matrix | R | A | C | C | I | C |
| Document trade-off analysis | R | I | C | C | I | C |
| Record workshop outcomes | R | A | C | C | I | C |
| Produce consensus documentation | R | A | C | C | I | C |
| Produce Stakeholder Alignment report | R | A | C | C | I | C |
| Review & approve final report | C | A | R | R | I | R |
| Trigger downstream tasks via PM Agent | I | R | I | I | I | I |

## Legend

- **R** = Responsible -- Does the work
- **A** = Accountable -- Approves / owns the outcome
- **C** = Consulted -- Provides input before decisions
- **I** = Informed -- Notified of outcomes

## Upstream Inputs (Wave 9 -- Solutions Architect)

| Input | Source Task | Description |
|:---|:---|:---|
| Solution Architecture Document (SAD) | SA-REQ-001 | Comprehensive solution architecture covering logical, physical, deployment views |
| Integration Architecture | SA-REQ-002 | System integration patterns, API gateway, ESB, event-driven, pub/sub |
| NFR Mapping | SA-REQ-003 | Business SLAs translated into measurable NFRs |
| Technology Blueprint | SA-REQ-004 | Full technology stack, platform services, middleware, infrastructure |
| ARB Feedback | SA-REQ-005 | Architecture Review Board approval and alignment notes |

## Downstream Task Notification (Wave 11 -- Technical Lead)

Upon completion, send to PM Agent:
1. Stakeholder Alignment report file path
2. This RACI matrix
3. Supervisor inspection report

PM Agent uses this matrix to trigger the following downstream tasks:

| Downstream Task | Role | Description |
|:---|:---|:---|
| TL-INC-001 | Technical Lead | Technical Vision & Direction |
| TL-INC-002 | Technical Lead | Technology Stack Decision |
| TL-INC-003 | Technical Lead | Team Capability Assessment |
| TL-INC-004 | Technical Lead | Technical Risk Assessment |
| TL-INC-005 | Technical Lead | Estimation Leadership |
