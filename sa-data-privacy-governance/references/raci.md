# RACI Matrix -- Data Privacy & Governance (IA-REQ-006)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Business Analyst (BA) | Tech Lead (TL) | Legal/Compliance | Security Architect (SecA) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define governance scope & objectives | R | A | C | C | C | C |
| Create data classification taxonomy | R | I | C | C | C | C |
| Define data retention policy | R | I | C | I | C | C |
| Define data residency requirements | R | I | I | C | C | C |
| Design access control model | R | I | I | C | I | C |
| Define consent management framework | R | I | C | C | C | I |
| Produce regulatory compliance view | R | I | C | I | C | C |
| Produce NFR alignment note | R | I | I | C | C | C |
| Produce Data Privacy & Governance report | R | A | I | C | C | C |
| Review & approve final report | C | A | I | R | R | R |
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
1. Data Privacy & Governance report file path
2. This RACI matrix
3. Supervisor inspection report

PM Agent uses this matrix to trigger the following downstream tasks:

| Downstream Task | Role | Description |
|:---|:---|:---|
| TL-REQ-001 | Technical Lead | Technical Design & Solution Design |
| TL-REQ-002 | Technical Lead | Coding Standards & Conventions |
| TL-REQ-003 | Technical Lead | Task Decomposition & Assignment |
| TL-REQ-004 | Technical Lead | Build & Toolchain Setup |
| TL-REQ-005 | Technical Lead | Cross-Team Technical Alignment |
