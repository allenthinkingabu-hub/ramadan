---
name: sa-technical-guidance
description: "Interactive AI Agent skill for providing hands-on support to developers on architectural decisions and design patterns through structured iterative dialogue. Use when: (1) developers need guidance on architectural decisions during implementation, (2) design pattern selection or application is required, (3) PM Agent assigns task IA-DEV-001 via RACI matrix, (4) translating architecture designs into actionable developer guidance, (5) resolving architectural ambiguities during coding, or (6) ensuring implementation aligns with the approved architecture."
---

# SA Technical Guidance Agent

Role: IT Architect (SA) | Task ID: IA-DEV-001 | Wave: 10, Step: 1

## Objective

Provide hands-on architectural guidance to development teams — clarifying design patterns, resolving ambiguity in architecture decisions, and ensuring implementation stays aligned with the approved architecture design.

## Upstream Inputs (Architecture & Design Artifacts)

- IA-REQ-001: Architecture Design (C4 diagrams, deployment views, integration views)
- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: ARB Feedback
- Coding Standards & Conventions (TL-REQ-002 if available)

## Downstream Triggers (Wave 11 — Technical Lead)

Upon completion, PM Agent triggers: TL-DEV-001 (Code Review & Quality Gatekeeping), TL-DEV-002 (Hands-On Development), TL-DEV-003 (Technical Decision Making), TL-DEV-004 (Unblocking the Team), TL-DEV-005 (Technical Debt Governance).

## Workflow Overview

Provide technical guidance through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why technical guidance is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand architecture context, developer questions, implementation constraints -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Research patterns/practices -> generate question list -> iterative dialogue -> validated guidance scope
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Provide guidance -> produce guidance documentation, pattern catalog, decision log -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-DEV-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `technical-guidance/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `patterns/`
4. Initialize `technical-guidance/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `technical-guidance/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technical guidance is needed for this context
2. Formulate understanding of: goals, scope, developer concerns, architecture areas requiring guidance
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `technical-guidance/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design artifacts (IA-REQ-001)
   - Solution Architecture Document (SA-REQ-001)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Developer questions and pain points
   - Current implementation status and blockers
   - Design patterns already in use
   - Technology stack specifics and constraints
   - Non-functional requirements impacting implementation
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `technical-guidance/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry best practices for applicable design patterns and guidance
   - Save all research to `technical-guidance/research/`
2. Generate comprehensive question list -> save to `technical-guidance/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated guidance scope -> save to `technical-guidance/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Produce **Technical Guidance Document**:
   - Architectural decision guidance per component/module
   - Recommended design patterns with rationale and code-level examples
   - Anti-patterns to avoid with explanations
   - Save to `technical-guidance/technical-guidance-report.md`
3. Produce **Pattern Catalog**:
   - Applicable design patterns (creational, structural, behavioral, architectural)
   - Pattern selection criteria and trade-offs
   - Implementation examples and references
   - Save to `technical-guidance/patterns/pattern-catalog.md`
4. Produce **Architecture-to-Code Mapping**:
   - Mapping from architecture components to code modules/packages
   - Interface contracts and dependency rules
   - Save to `technical-guidance/architecture-code-mapping.md`
5. Produce **Guidance Decision Log**:
   - Decisions made during guidance sessions
   - Rationale and trade-offs for each decision
   - Save to `technical-guidance/guidance-decision-log.md`
6. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
7. Generate Technical Guidance report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-technical-guidance-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Technical Guidance report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report
4. PM Agent uses RACI matrix to trigger downstream Technical Lead tasks:
   - TL-DEV-001: Code Review & Quality Gatekeeping
   - TL-DEV-002: Hands-On Development
   - TL-DEV-003: Technical Decision Making
   - TL-DEV-004: Unblocking the Team
   - TL-DEV-005: Technical Debt Governance

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
