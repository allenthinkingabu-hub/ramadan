# RACI Matrix — Project Structure Scan (SA-DISC-001)

## Stakeholder Roles

| Role | Description |
|------|-------------|
| **IT Architect (SA)** | The AI agent executing this task — responsible for the scan |
| **Solutions Architect** | Upstream input provider — defines architecture requirements |
| **Technical Lead** | Downstream consumer — uses scan results for technical decisions |
| **Project Manager (PM)** | Task coordinator — triggers task, manages workflow, triggers downstream |
| **Development Team** | Informed of scan results — uses findings for implementation |
| **Enterprise Architect** | Consulted on architecture pattern decisions and standards |
| **QA Lead** | Informed of structural risks and test coverage implications |

## RACI Assignment

| # | Task | IT Architect (SA) | Solutions Architect | Technical Lead | Project Manager | Dev Team | Enterprise Architect | QA Lead |
|---|------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | Initiate project structure scan | R | C | C | A | I | I | I |
| 2 | Define scan scope and requirements | R | C | C | A | I | C | I |
| 3 | Collect project intake information | R | I | C | A | I | I | I |
| 4 | Execute codebase scanning | R | I | I | A | I | I | I |
| 5 | Produce Structure Tree (OUT-01) | R | I | I | A | I | I | I |
| 6 | Produce Module Relationship Diagram (OUT-02) | R | I | C | A | I | C | I |
| 7 | Produce Layering Pattern Analysis (OUT-03) | R | C | C | A | I | C | I |
| 8 | Produce Package Dependency Map (OUT-04) | R | I | C | A | I | I | I |
| 9 | Produce Module Responsibility Summary (OUT-05) | R | I | C | A | I | I | I |
| 10 | Produce Final Scan Report (OUT-06) | R | C | C | A | I | C | I |
| 11 | DoD self-verification | R | I | I | A | I | I | I |
| 12 | Review and approve scan results | I | A | R | C | I | C | I |
| 13 | Trigger downstream tasks | I | I | I | R | I | I | I |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

## PM Agent Downstream Task Triggering

After the Project Structure Scan completes and the Supervisor passes 100%, the PM Agent uses this RACI matrix to trigger downstream tasks in the Code Archaeology phase:

| Downstream Task | Task ID | Triggered Agent | Input From This Task |
|----------------|---------|-----------------|---------------------|
| Technology Stack Inventory | SA-DISC-002 | IT Architect (SA) | OUT-04 (Dependency Map), project understanding |
| Entry-Point Tracing | SA-DISC-003 | IT Architect (SA) | OUT-01 (Structure Tree), OUT-02 (Module Relationships) |
| Data Model Analysis | SA-DISC-004 | IT Architect (SA) | OUT-01, project path, tech stack info |
| Configuration & Environments | SA-DISC-005 | IT Architect (SA) | OUT-01, config file locations |
| Architecture Recovery | SA-DISC-010 | Solutions Architect | All OUT-01~06 (after all Step 1.x complete) |

The PM Agent:
1. Receives the completion notification with deliverables path and this RACI matrix.
2. Identifies downstream tasks from the table above.
3. Triggers each downstream task with the appropriate inputs from this task's deliverables.
4. Monitors downstream task completion using their respective RACI matrices.
