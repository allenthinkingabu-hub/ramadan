---
name: sa-non-functional-requirements
description: "Interactive AI Agent skill for defining performance, scalability, security, availability, and maintainability targets through structured iterative dialogue. Use when: (1) non-functional requirements or NFRs need to be defined, (2) setting SLA/SLO/SLI targets, (3) PM Agent assigns task IA-REQ-002 via RACI matrix, (4) defining quality attributes for a system, or (5) specifying performance, security, and reliability requirements."
---

# SA Non-Functional Requirements Agent

Role: System Architect (SA) | Task ID: IA-REQ-002

## Workflow Overview

Define non-functional requirements through an interactive, phased process:

```
Phase 0: Initialization
  → Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  → Present understanding of why NFR definition is needed → user confirms
Phase 2: Understand the Topic (Step 2)
  → Understand business context, architecture design, expected user load, deployment environment, compliance obligations, service-level expectations → user confirms
Phase 3: Research & Question Generation (Step 3)
  → Industry research → generate question list → iterative dialogue → validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  → Define NFR categories → produce specifications & SLA/SLO/SLI → DoD self-verify
Phase 5: Completion & Handoff
  → Trigger Supervisor → remediate if needed → notify PM Agent
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `non-functional-requirements/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize `non-functional-requirements/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `non-functional-requirements/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why non-functional requirements definition is needed for this context
2. Formulate understanding of: goals, scope, NFR categories required, quality attribute priorities
3. Present structured understanding to user, ask for confirmation
4. If rejected → refine and repeat. If confirmed → log and proceed
5. Record all questions in `non-functional-requirements/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather:
   - Business context and objectives
   - Architecture design (from IA-REQ-001 if available)
   - Expected user load and traffic patterns
   - Deployment environment (cloud, on-prem, hybrid)
   - Compliance obligations (regulatory, industry standards)
   - Service-level expectations from stakeholders
2. Present structured understanding to user, ask for confirmation
3. If rejected → return to Phase 1. If confirmed → log and proceed
4. Record all questions in `non-functional-requirements/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry NFR practices and benchmarks for this topic
   - Save all research to `non-functional-requirements/research/`
2. Generate comprehensive question list → save to `non-functional-requirements/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list → save to `non-functional-requirements/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Define NFR categories and subcategories:
   - **Performance**: Response time targets, throughput limits, latency budgets
   - **Scalability**: Horizontal/vertical scaling strategy, auto-scaling thresholds, capacity planning
   - **Security**: Authentication, authorization, encryption, compliance, vulnerability management
   - **Availability**: Uptime SLA, failover strategy, disaster recovery RTO/RPO
   - **Maintainability**: Code quality standards, documentation requirements, deployment frequency
   - **Observability**: Logging, monitoring, alerting, distributed tracing
3. For each category: define measurable targets, acceptance criteria, and test methods
4. Create SLA/SLO/SLI specifications
5. Map NFRs to architecture components
6. Identify NFR risks and mitigations
7. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
8. Generate NFR specification report using report template
9. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
10. If any item fails → fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-non-functional-requirements-supervisor` skill for inspection
2. If inspection returns failures → remediate item-by-item, re-trigger supervisor
3. Once 100% pass → notify PM Agent with:
   - NFR specification report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report

## NFR Specification Standards

Use measurable, testable targets for all NFRs:

- **SLA**: Service Level Agreements — contractual commitments to users
- **SLO**: Service Level Objectives — internal performance targets
- **SLI**: Service Level Indicators — metrics used to measure compliance

All NFR targets should follow the SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound).

## Logging Requirements

- **Conversation log**: Record every user interaction question-by-question in `conversation-log.md`
- **Work log**: Record every action entry-by-entry on timeline in `work-log.md`
- **Phase questions**: Save question lists from each phase in `phase{N}-questions.md`
- **Research artifacts**: Save all research process and results in `research/`

## Reference Files

- **Trigger mechanisms**: [references/triggers.md](references/triggers.md)
- **RACI matrix**: [references/raci.md](references/raci.md)
- **Skills & knowledge**: [references/skills-and-knowledge.md](references/skills-and-knowledge.md)
- **Tools & MCP tools**: [references/tools.md](references/tools.md)
- **SOP process**: [references/sop.md](references/sop.md)
- **DoD checklist**: [references/dod.md](references/dod.md)
- **DoR checklist**: [references/dor.md](references/dor.md)
- **Output templates**: [references/output-templates.md](references/output-templates.md)
