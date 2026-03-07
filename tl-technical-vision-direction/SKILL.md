---
name: tl-technical-vision-direction
description: "Interactive AI Agent skill for defining the overall technical approach and aligning it with business objectives and architectural guidelines through structured iterative dialogue. Use when: (1) establishing the technical vision for a project or product, (2) aligning technical direction with business strategy and architectural guidelines, (3) PM Agent assigns task TL-INC-001 via RACI matrix, (4) translating IT Architect outputs (Technical Discovery, Feasibility Analysis, PoC results, NFR analysis, Technology Landscape, Risk Assessment, Integration Strategy, Architecture Patterns) into a cohesive technical vision, (5) defining guiding principles for technical execution, or (6) creating a technical vision statement and roadmap."
---

# TL Technical Vision & Direction Agent

Role: Technical Lead (TL) | Task ID: TL-INC-001 | Wave: 11, Step: 1

## Objective

Define the overall technical approach — vision statement, guiding principles, technology direction, and alignment with business objectives and architectural guidelines — to provide a clear north star for all downstream technical decisions.

## Upstream Inputs (Wave 10 — IT Architect)

- IA-INC-001: Technical Discovery Report
- IA-INC-002: Feasibility Analysis
- IA-INC-003: Proof of Concept Results
- IA-INC-004: Non-Functional Requirements Analysis
- IA-INC-005: Technology Landscape Assessment
- IA-INC-006: Risk Assessment
- IA-INC-007: Integration Strategy
- IA-INC-008: Architecture Patterns Evaluation

## Downstream Triggers (Wave 12 — Software Engineer)

Upon completion, PM Agent triggers: SE-INC-001 through SE-INC-005 (Software Engineer Inception tasks).

## Workflow Overview

Create technical vision through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why technical vision is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream IA-INC outputs, business objectives, architectural guidelines -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Define vision -> produce vision statement, guiding principles, alignment matrix -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger SE-INC-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `technical-vision-direction/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize `technical-vision-direction/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `technical-vision-direction/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why a technical vision is needed for this context
2. Formulate understanding of: goals, scope, vision objectives, stakeholder expectations
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `technical-vision-direction/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 10 (IT Architect):
   - IA-INC-001: Technical Discovery Report
   - IA-INC-002: Feasibility Analysis
   - IA-INC-003: Proof of Concept Results
   - IA-INC-004: Non-Functional Requirements Analysis
   - IA-INC-005: Technology Landscape Assessment
   - IA-INC-006: Risk Assessment
   - IA-INC-007: Integration Strategy
   - IA-INC-008: Architecture Patterns Evaluation
2. Gather additional context:
   - Business objectives and strategic priorities
   - Organizational technology standards and constraints
   - Team capabilities and growth trajectory
   - Budget and timeline constraints
   - Regulatory and compliance requirements
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `technical-vision-direction/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry technical vision practices for this domain
   - Save all research to `technical-vision-direction/research/`
2. Generate comprehensive question list -> save to `technical-vision-direction/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `technical-vision-direction/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Produce **Technical Vision Statement**:
   - Clear articulation of the technical direction
   - Alignment with business strategy
   - Time horizon and milestones
   - Save to `technical-vision-direction/technical-vision-statement.md`
3. Produce **Guiding Principles**:
   - Core technical principles (e.g., API-first, cloud-native, security-by-design)
   - Decision-making framework for trade-offs
   - Save to `technical-vision-direction/guiding-principles.md`
4. Produce **Business-Technology Alignment Matrix**:
   - Map business objectives to technical capabilities
   - Identify gaps and investment areas
   - Save to `technical-vision-direction/alignment-matrix.md`
5. Produce **Technology Roadmap Overview**:
   - High-level technology evolution plan
   - Key decision points and milestones
   - Save to `technical-vision-direction/technology-roadmap.md`
6. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
7. Generate Technical Vision Direction report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `tl-technical-vision-direction-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Technical Vision Direction report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report
4. PM Agent uses RACI matrix to trigger downstream Software Engineer tasks:
   - SE-INC-001 through SE-INC-005

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
