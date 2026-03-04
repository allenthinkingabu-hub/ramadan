# Integration Design Agent — RACI Matrix Configuration

## RACI Matrix

| Task / Activity | System Architect (SA) | Technical Lead (TL) | Project Manager (PM) | Developer (Dev) | QA Engineer | Security Architect | DevOps Engineer |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Define Integration Strategy | R, A | C | I | I | — | C | C |
| API Contract Design | R, A | C | I | C | — | C | — |
| Data Flow Mapping | R, A | C | I | C | — | C | — |
| Third-Party Dependency Analysis | R, A | C | I | I | — | C | C |
| Integration Security Design | R | C | I | — | — | A, C | — |
| Message Protocol Selection | R, A | C | I | C | — | C | C |
| Error Handling & Retry Strategy | R, A | C | I | C | C | — | C |
| Integration Testing Strategy | R | C | I | C | A | — | C |
| API Gateway & Routing Design | R, A | C | I | — | — | C | C |
| Data Transformation Mapping | R, A | C | I | C | — | — | — |
| Integration Monitoring & Alerting | R | C | I | — | — | — | A, C |
| Integration Design Review | R | A, C | I | C | C | C | C |
| Integration Design Approval | R | C | A | — | — | C | — |

## Legend

- **R** = Responsible (does the work)
- **A** = Accountable (approves/owns the outcome)
- **C** = Consulted (provides input)
- **I** = Informed (kept up-to-date)

## Stakeholder Contact Points

| Role | Agent ID | Notification Channel |
| :--- | :--- | :--- |
| System Architect | SA-Agent | Direct invocation |
| Technical Lead | TL-Agent | RACI notification |
| Project Manager | PM-Agent | Task completion notification |
| Developer | Dev-Agent | RACI notification |
| QA Engineer | QA-Agent | RACI notification |
| Security Architect | SecArch-Agent | RACI notification |
| DevOps Engineer | DevOps-Agent | RACI notification |

## Downstream Task Triggers

Upon completion of Integration Design, the PM Agent uses this matrix to trigger:
1. **Developer Agent** — Implement integration interfaces per API contracts
2. **QA Agent** — Create integration test plans
3. **DevOps Agent** — Provision integration infrastructure
4. **Security Architect Agent** — Review integration security controls

## Configuration Notes

- Add new roles by appending columns to the RACI Matrix table.
- Add new tasks by appending rows.
- Update Stakeholder Contact Points as agent configurations change.
