---
name: sa-stakeholder-alignment
description: "Interactive AI Agent skill for running architecture workshops to align business, product, security, and ops stakeholders on scope, risks, and decision criteria through structured iterative dialogue. Use when: (1) stakeholder alignment on architecture decisions is needed during inception, (2) facilitating cross-functional architecture workshops, (3) PM Agent assigns task IA-INC-006 via RACI matrix, (4) translating Solutions Architect outputs (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB feedback) into stakeholder-aligned decision records, (5) resolving conflicting priorities between business, security, and operations teams, or (6) building consensus on scope boundaries, risk tolerance, and decision criteria."
---

# SA Stakeholder Alignment Agent

Role: IT Architect (SA) | Task ID: IA-INC-006 | Wave: 10, Step: 6

## Objective

Run architecture workshops to align business, product, security, and ops stakeholders on scope, risks, and decision criteria. Produce stakeholder alignment records, decision matrices, and consensus documentation that ensure all parties share a common understanding before downstream design work begins.

## Upstream Inputs (Wave 9 -- Solutions Architect)

- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-002: Integration Architecture
- SA-REQ-003: Non-Functional Requirements Mapping
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: Architecture Review Board (ARB) Feedback

## Downstream Triggers (Wave 11 -- Technical Lead)

Upon completion, PM Agent triggers: TL-INC-001 (Technical Vision & Direction), TL-INC-002 (Technology Stack Decision), TL-INC-003 (Team Capability Assessment), TL-INC-004 (Technical Risk Assessment), TL-INC-005 (Estimation Leadership).

## Workflow Overview

Create stakeholder alignment deliverables through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why stakeholder alignment is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream SA-REQ outputs, stakeholder landscape, conflicting priorities -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated alignment areas
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Facilitate alignment -> produce stakeholder map, decision matrix, workshop outcomes -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-INC-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `stakeholder-alignment/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize `stakeholder-alignment/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `stakeholder-alignment/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why stakeholder alignment is needed for this context
2. Formulate understanding of: goals, scope, stakeholder groups, alignment objectives
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `stakeholder-alignment/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SAD -- Solution Architecture Document (SA-REQ-001)
   - Integration Architecture (SA-REQ-002)
   - NFR Mapping (SA-REQ-003)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Stakeholder landscape (business, product, security, ops, compliance)
   - Known conflicts or competing priorities
   - Organizational decision-making structure
   - Risk tolerance per stakeholder group
   - Budget and timeline constraints
   - Technical discovery findings (from IA-INC-001 if available)
   - Feasibility analysis results (from IA-INC-002 if available)
   - Risk identification outputs (from IA-INC-004 if available)
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `stakeholder-alignment/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry stakeholder alignment practices for this topic
   - Save all research to `stakeholder-alignment/research/`
2. Generate comprehensive question list -> save to `stakeholder-alignment/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated alignment agenda -> save to `stakeholder-alignment/validated-agenda.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated alignment agenda
2. Produce **Stakeholder Map**:
   - Stakeholder identification and influence/interest matrix
   - Communication preferences and engagement strategy
   - RACI assignments for architecture decisions
   - Save to `stakeholder-alignment/stakeholder-map.md`
3. Produce **Decision Criteria Matrix**:
   - Weighted evaluation criteria agreed by stakeholders
   - Priority rankings per stakeholder group
   - Trade-off analysis and compromise positions
   - Save to `stakeholder-alignment/decision-criteria.md`
4. Produce **Workshop Outcomes Record**:
   - Agreed scope boundaries
   - Accepted risk posture per stakeholder group
   - Open items and action items with owners
   - Escalation paths for unresolved conflicts
   - Save to `stakeholder-alignment/workshop-outcomes.md`
5. Produce **Consensus Documentation**:
   - Signed-off decisions and rationale
   - Dissenting opinions recorded with resolution path
   - Follow-up schedule for pending items
   - Save to `stakeholder-alignment/consensus-record.md`
6. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
7. Generate Stakeholder Alignment report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-stakeholder-alignment-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Stakeholder Alignment report path
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

Save all diagram source files to `stakeholder-alignment/diagrams/` with descriptive names.

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
