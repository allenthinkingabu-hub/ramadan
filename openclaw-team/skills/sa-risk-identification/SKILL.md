---
name: sa-risk-identification
description: "Interactive AI Agent skill for identifying technical risks, dependencies, and potential integration challenges early through structured iterative dialogue. Use when: (1) technical risk assessment is needed during inception, (2) identifying cross-system dependencies and integration challenges, (3) PM Agent assigns task IA-INC-004 via RACI matrix, (4) translating Solutions Architect outputs (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB feedback) into a comprehensive risk register, (5) assessing architecture-level risks that could impact downstream design and delivery, or (6) surfacing dependency chains and coupling risks across system boundaries."
---

# SA Risk Identification Agent

Role: IT Architect (SA) | Task ID: IA-INC-004 | Wave: 10, Step: 4

## Objective

Identify technical risks, dependencies, and potential integration challenges early in the inception phase. Produce a comprehensive risk register with severity assessments, dependency maps, and mitigation strategies that inform downstream technical lead planning.

## Upstream Inputs (Wave 9 -- Solutions Architect)

- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-002: Integration Architecture
- SA-REQ-003: Non-Functional Requirements Mapping
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: Architecture Review Board (ARB) Feedback

## Downstream Triggers (Wave 11 -- Technical Lead)

Upon completion, PM Agent triggers: TL-INC-001 (Technical Vision & Direction), TL-INC-002 (Technology Stack Decision), TL-INC-003 (Team Capability Assessment), TL-INC-004 (Technical Risk Assessment), TL-INC-005 (Estimation Leadership).

## Workflow Overview

Create risk identification deliverables through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why risk identification is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream SA-REQ outputs, system landscape, integration points, NFRs -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated risk areas
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Identify risks -> produce risk register, dependency map, integration challenge analysis -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-INC-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `risk-identification/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize `risk-identification/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `risk-identification/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technical risk identification is needed for this context
2. Formulate understanding of: goals, scope, risk categories, dependency types to assess
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `risk-identification/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SAD -- Solution Architecture Document (SA-REQ-001)
   - Integration Architecture (SA-REQ-002)
   - NFR Mapping (SA-REQ-003)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - System landscape and component inventory
   - External system dependencies and third-party integrations
   - Technology maturity and team familiarity
   - Non-functional requirements and SLA targets
   - Known constraints (budget, timeline, regulatory)
   - Technical discovery findings (from IA-INC-001 if available)
   - Feasibility analysis results (from IA-INC-002 if available)
   - Architecture design outputs (from IA-INC-003 if available)
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `risk-identification/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry risk identification practices for this topic
   - Save all research to `risk-identification/research/`
2. Generate comprehensive question list -> save to `risk-identification/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated risk areas list -> save to `risk-identification/validated-risk-areas.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated risk areas
2. Produce **Risk Register**:
   - Technical risks with severity (likelihood x impact), category, and owner
   - Integration risks at system boundaries
   - Dependency risks (upstream/downstream, third-party, infrastructure)
   - Technology risks (maturity, skill gaps, vendor lock-in)
   - NFR risks (performance, scalability, security, availability shortfalls)
   - Save to `risk-identification/risk-register.md`
3. Produce **Dependency Map**:
   - System dependency graph (Mermaid diagram)
   - Critical path dependencies
   - Circular dependency identification
   - External dependency inventory
   - Save to `risk-identification/diagrams/dependency-map.md`
4. Produce **Integration Challenge Analysis**:
   - Integration point inventory
   - Protocol/contract mismatch risks
   - Data consistency and synchronization challenges
   - Error propagation and cascading failure risks
   - Save to `risk-identification/integration-challenges.md`
5. Produce **Mitigation Strategy Matrix**:
   - Risk-to-mitigation mapping
   - Contingency plans for high-severity risks
   - Residual risk assessment
   - Save to `risk-identification/mitigation-strategies.md`
6. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
7. Generate Risk Identification report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-risk-identification-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Risk Identification report path
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

Save all diagram source files to `risk-identification/diagrams/` with descriptive names.

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
