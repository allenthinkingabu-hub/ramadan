# RACI Matrix -- DR/BCP Architecture (IA-REQ-007)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Business Analyst (BA) | Tech Lead (TL) | Dev Lead (DL) | SRE/Ops Lead |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define DR/BCP scope & objectives | R | A | C | C | I | C |
| Define RPO/RTO targets per tier | R | A | C | C | I | C |
| Design failover topology | R | I | I | C | C | C |
| Design backup/restore strategy | R | I | I | C | C | C |
| Create recovery runbooks | R | I | I | C | C | C |
| Design DR testing plan | R | I | I | C | C | C |
| Produce resilience architecture view | R | I | I | C | C | C |
| Produce NFR alignment note | R | I | I | C | C | C |
| Produce DR/BCP Architecture report | R | A | I | C | C | C |
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
1. DR/BCP Architecture report file path
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
