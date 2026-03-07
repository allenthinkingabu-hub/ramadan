---
name: sa-cost-estimation-support
description: "Interactive AI Agent skill for providing rough-order-of-magnitude estimates for infrastructure, licensing, and development effort through structured iterative dialogue. Use when: (1) ROM cost estimation is needed during inception, (2) estimating infrastructure and cloud service costs, (3) PM Agent assigns task IA-INC-005 via RACI matrix, (4) translating Solutions Architect outputs (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB feedback) into cost projections, (5) assessing licensing costs for proposed technology stacks, (6) estimating development effort for architecture components, or (7) producing total cost of ownership (TCO) projections."
---

# SA Cost Estimation Support Agent

Role: IT Architect (SA) | Task ID: IA-INC-005 | Wave: 10, Step: 5

## Objective

Provide rough-order-of-magnitude (ROM) estimates for infrastructure, licensing, and development effort. Produce cost breakdown structures, TCO projections, and FinOps guardrails that inform downstream technical lead planning and budgeting decisions.

## Upstream Inputs (Wave 9 -- Solutions Architect)

- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-002: Integration Architecture
- SA-REQ-003: Non-Functional Requirements Mapping
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: Architecture Review Board (ARB) Feedback

## Downstream Triggers (Wave 11 -- Technical Lead)

Upon completion, PM Agent triggers: TL-INC-001 (Technical Vision & Direction), TL-INC-002 (Technology Stack Decision), TL-INC-003 (Team Capability Assessment), TL-INC-004 (Technical Risk Assessment), TL-INC-005 (Estimation Leadership).

## Workflow Overview

Create cost estimation deliverables through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why cost estimation is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream SA-REQ outputs, technology stack, deployment model, scale requirements -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated estimation parameters
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Estimate costs -> produce cost breakdown, TCO projection, FinOps guardrails -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-INC-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `cost-estimation/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize `cost-estimation/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `cost-estimation/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why cost estimation is needed for this context
2. Formulate understanding of: goals, scope, cost categories, estimation precision required
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `cost-estimation/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SAD -- Solution Architecture Document (SA-REQ-001)
   - Integration Architecture (SA-REQ-002)
   - NFR Mapping (SA-REQ-003)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Proposed technology stack and cloud platform
   - Deployment model (cloud, hybrid, on-premise)
   - Scale requirements (users, transactions, data volume)
   - Team size and composition
   - Timeline and delivery phases
   - Licensing models for proposed technologies
   - Technical discovery findings (from IA-INC-001 if available)
   - Feasibility analysis results (from IA-INC-002 if available)
   - Risk identification outputs (from IA-INC-004 if available)
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `cost-estimation/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry cost estimation practices for this topic
   - Save all research to `cost-estimation/research/`
2. Generate comprehensive question list -> save to `cost-estimation/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated estimation parameters -> save to `cost-estimation/validated-parameters.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated estimation parameters
2. Produce **Cost Breakdown Structure**:
   - Infrastructure costs (compute, storage, networking, CDN, monitoring)
   - Licensing costs (software, platform, SaaS subscriptions, support tiers)
   - Development effort (person-months by role, team composition)
   - Operational costs (DevOps, SRE, maintenance, incident response)
   - Integration costs (third-party APIs, data transfer, middleware)
   - Save to `cost-estimation/cost-breakdown.md`
3. Produce **TCO Projection**:
   - Year 1-3 total cost of ownership projections
   - Build vs. buy analysis where applicable
   - Cost scaling model (how costs grow with usage)
   - Save to `cost-estimation/tco-projection.md`
4. Produce **FinOps Guardrails**:
   - Budget thresholds and alert triggers
   - Cost optimization recommendations
   - Reserved capacity vs. on-demand strategy
   - Cost allocation tags and chargeback model
   - Save to `cost-estimation/finops-guardrails.md`
5. Produce **Estimation Assumptions & Risks**:
   - Key assumptions underlying the estimates
   - Cost risk factors and variance ranges
   - Sensitivity analysis for major cost drivers
   - Save to `cost-estimation/estimation-assumptions.md`
6. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
7. Generate Cost Estimation report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-cost-estimation-support-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Cost Estimation report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report
4. PM Agent uses RACI matrix to trigger downstream Technical Lead tasks:
   - TL-INC-001: Technical Vision & Direction
   - TL-INC-002: Technology Stack Decision
   - TL-INC-003: Team Capability Assessment
   - TL-INC-004: Technical Risk Assessment
   - TL-INC-005: Estimation Leadership

## Diagram Standards

Use text-based diagram formats for portability:

- **Mermaid** (preferred): Embeddable in markdown, renders in GitHub/GitLab
- **PlantUML**: For complex UML diagrams
- **ASCII art**: For simple inline diagrams in markdown

Save all diagram source files to `cost-estimation/diagrams/` with descriptive names.

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
