---
name: SA-integration-design
description: "Interactive AI Agent skill for mapping out system integrations, API contracts, data flows, and third-party dependencies through structured iterative dialogue. Use when: (1) integration design is needed for a project or system, (2) defining API contracts (OpenAPI/AsyncAPI/gRPC), (3) mapping data flows and transformation pipelines, (4) analyzing third-party service dependencies and risks, (5) PM Agent assigns task IA-REQ-003 via RACI matrix, (6) designing message protocols, event-driven integrations, or middleware topology, (7) defining error handling, resilience patterns (circuit breaker, retry, fallback), or (8) producing integration security design, monitoring/alerting plans, and integration test strategies."
---

# SA Integration Design Agent

Role: System Architect (SA) | Task ID: IA-REQ-003 | Task Name: Integration Design

## Objective

Produce the definitive integration design — covering API contracts, data flow mappings, third-party dependency analysis, message protocol specifications, integration security controls, error handling strategies, and integration test plans — for the given project or system.

## Upstream Inputs

- IA-REQ-001: Architecture Design (high-level and detailed architecture diagrams)
- IA-REQ-002: Technology Stack Decision (selected technologies, frameworks, platforms)
- Existing system landscape documentation (if applicable)
- API standards and guidelines (if any)
- Security requirements for inter-system communication

## Downstream Triggers

Upon completion, PM Agent triggers downstream tasks:
1. **Developer Agent** — Implement integration interfaces per API contracts
2. **QA Agent** — Create integration test plans
3. **DevOps Agent** — Provision integration infrastructure
4. **Security Architect Agent** — Review integration security controls

## Workflow Overview

Create integration designs through an interactive, phased process:

```
Phase 0: Initialization
  → Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  → Present understanding of why integration design is needed → user confirms
Phase 2: Understand the Topic (Step 2)
  → Understand architecture design, tech stack, existing systems, API standards,
    data exchange formats, messaging protocols, security requirements → user confirms
Phase 3: Research & Question Generation (Step 3)
  → Industry research → generate question list → iterative dialogue → validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  → Design integrations → produce API contracts, data flows, error handling,
    test strategy, monitoring plan → DoD self-verify
Phase 5: Completion & Handoff
  → Trigger Supervisor → remediate if needed → notify PM Agent → trigger downstream tasks
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor-checklist.md](references/dor-checklist.md)
2. Create `integration-design/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`, `api-specs/`
4. Initialize `integration-design/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `integration-design/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why integration design is needed for this context
2. Formulate understanding of: goals, scope, integration objectives, expected integration points
3. Present structured understanding to user, ask for confirmation
4. If rejected → refine and repeat. If confirmed → log and proceed
5. Record all questions in `integration-design/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design document (IA-REQ-001)
   - Technology Stack Decision document (IA-REQ-002)
2. Gather additional context:
   - High-level architecture design and system boundaries
   - Selected technology stack and platform capabilities
   - Existing system landscape and current integration points
   - Third-party service dependencies (SaaS, APIs, payment gateways, etc.)
   - API standards and conventions in use (REST, GraphQL, gRPC)
   - Data exchange formats (JSON, XML, Protobuf, Avro)
   - Messaging protocols (Kafka, RabbitMQ, SQS/SNS, MQTT)
   - Security requirements for inter-system communication (OAuth2, mTLS, API keys)
3. Present structured understanding to user, ask for confirmation
4. If rejected → return to Phase 1. If confirmed → log and proceed
5. Record all questions in `integration-design/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry integration design practices for this topic:
   - API contract definition methodologies (design-first vs code-first)
   - Data flow mapping patterns and best practices
   - Third-party dependency management strategies
   - Integration security best practices
   - Error handling and resilience patterns
   - Save all research to `integration-design/research/`
2. Generate comprehensive question list → save to `integration-design/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated integration design requirements list → save to `integration-design/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Design integrations and produce deliverables:
   - **Integration Strategy Document**: Overall integration approach, patterns, and middleware topology
   - **API Contract Specifications**: OpenAPI 3.x specs for REST APIs, AsyncAPI for event-driven, gRPC proto definitions
   - **Data Flow Diagrams**: End-to-end data flow maps for all integration scenarios (using Mermaid/PlantUML)
   - **Third-Party Dependency Register**: All external dependencies cataloged with risk assessment, SLA, fallback strategy
   - **Integration Security Design**: Security controls per integration point (authentication, authorization, encryption)
   - **Message Protocol Specifications**: Protocol selection and configuration per integration
   - **Error Handling Strategy**: Retry, circuit breaker, fallback, timeout, dead-letter queue strategies
   - **Integration Test Strategy**: Contract testing, integration testing, E2E testing, mock service approach
   - **API Gateway & Routing Design**: Gateway topology, rate limiting, versioning, routing rules
   - **Data Transformation Mappings**: Schema mappings for all data transformations between systems
   - **Monitoring & Alerting Plan**: Observability strategy, distributed tracing, SLA/SLO monitoring, health checks
3. Save all diagrams to `integration-design/diagrams/` with descriptive names
4. Save all API specifications to `integration-design/api-specs/`
5. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
6. Generate Integration Design report using report template
7. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod-checklist.md](references/dod-checklist.md)
8. If any item fails → fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `SA-integration-design-supervisor` skill for inspection
2. If inspection returns failures → remediate item-by-item, re-trigger supervisor
3. Once 100% pass → notify PM Agent with:
   - Integration Design report path
   - RACI matrix (see [references/raci-matrix.md](references/raci-matrix.md))
   - Final inspection report
4. PM Agent uses RACI matrix to trigger downstream tasks:
   - Developer Agent — Implement integration interfaces per API contracts
   - QA Agent — Create integration test plans
   - DevOps Agent — Provision integration infrastructure
   - Security Architect Agent — Review integration security controls

## Diagram Standards

Use text-based diagram formats for portability:

- **Mermaid** (preferred): Embeddable in markdown, renders in GitHub/GitLab
- **PlantUML**: For complex UML diagrams and sequence flows
- **ASCII art**: For simple inline diagrams in markdown

Save all diagram source files to `integration-design/diagrams/` with descriptive names.

## Logging Requirements

- **Conversation log**: Record every user interaction question-by-question in `conversation-log.md`
- **Work log**: Record every action entry-by-entry on timeline in `work-log.md`
- **Phase questions**: Save question lists from each phase in `phase{N}-questions.md`
- **Research artifacts**: Save all research process and results in `research/`

## Reference Files

- **Trigger mechanisms**: [references/trigger-config.md](references/trigger-config.md)
- **RACI matrix**: [references/raci-matrix.md](references/raci-matrix.md)
- **Skills configuration**: [references/skills-config.md](references/skills-config.md)
- **Knowledge base**: [references/knowledge-base.md](references/knowledge-base.md)
- **Tools checklist**: [references/tools-checklist.md](references/tools-checklist.md)
- **MCP tools checklist**: [references/mcp-tools-checklist.md](references/mcp-tools-checklist.md)
- **SOP process**: [references/sop-process.md](references/sop-process.md)
- **DoD checklist**: [references/dod-checklist.md](references/dod-checklist.md)
- **DoR checklist**: [references/dor-checklist.md](references/dor-checklist.md)
- **Output templates**: [references/output-templates.md](references/output-templates.md)
