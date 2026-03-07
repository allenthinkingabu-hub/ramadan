# RACI Matrix -- Cost Estimation Support (IA-INC-005)

## Matrix

| Task / Deliverable | IT Architect (SA) | Project Manager (PM) | Business Analyst (BA) | Tech Lead (TL) | Dev Lead (DL) | Finance/Procurement |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Define estimation scope & parameters | R | A | C | C | I | C |
| Estimate infrastructure costs | R | I | I | C | C | I |
| Estimate licensing costs | R | I | I | C | I | C |
| Estimate development effort | R | A | I | C | C | I |
| Estimate operational costs | R | I | I | C | C | C |
| Produce cost breakdown structure | R | A | I | C | I | C |
| Produce TCO projection | R | A | C | C | I | C |
| Produce FinOps guardrails | R | A | I | C | I | C |
| Produce Cost Estimation report | R | A | I | C | C | C |
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
1. Cost Estimation report file path
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
