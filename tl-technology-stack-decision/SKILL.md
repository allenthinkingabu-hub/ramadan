---
name: tl-technology-stack-decision
description: "Interactive AI Agent skill for making final technology choices for languages, frameworks, libraries, and infrastructure in collaboration with the Architect through structured iterative dialogue. Use when: (1) finalizing technology stack decisions for a project, (2) selecting languages, frameworks, libraries, and infrastructure components, (3) PM Agent assigns task TL-INC-002 via RACI matrix, (4) translating IT Architect outputs into concrete technology selections, (5) evaluating technology trade-offs and compatibility, or (6) producing a technology decision matrix with justifications."
---

# TL Technology Stack Decision Agent

Role: Technical Lead (TL) | Task ID: TL-INC-002 | Wave: 11, Step: 2

## Objective

Make final technology choices for languages, frameworks, libraries, and infrastructure — collaborating with the IT Architect to ensure alignment with architectural guidelines, team capabilities, and business constraints.

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

Make technology stack decisions through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why technology decisions are needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream IA-INC outputs, constraints, team capabilities -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Technology research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Evaluate options -> produce decision matrix, compatibility analysis, stack specification -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger SE-INC-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `technology-stack-decision/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize `technology-stack-decision/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `technology-stack-decision/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technology stack decisions are needed for this context
2. Formulate understanding of: goals, scope, decision categories, constraints
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `technology-stack-decision/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 10 (IT Architect):
   - IA-INC-001 through IA-INC-008
2. Gather additional context:
   - Current technology landscape and existing stack
   - Team skills and experience with candidate technologies
   - Licensing, cost, and vendor considerations
   - Performance and scalability requirements
   - Security and compliance constraints
   - Community support and ecosystem maturity
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `technology-stack-decision/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research technology options and industry practices for this domain
   - Save all research to `technology-stack-decision/research/`
2. Generate comprehensive question list -> save to `technology-stack-decision/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `technology-stack-decision/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Produce **Technology Decision Matrix**:
   - Evaluation criteria with weights
   - Candidate technologies scored against criteria
   - Final recommendation with justification
   - Save to `technology-stack-decision/technology-decision-matrix.md`
3. Produce **Stack Specification**:
   - Languages, frameworks, libraries with versions
   - Infrastructure components (databases, messaging, caching)
   - DevOps tooling (CI/CD, monitoring, logging)
   - Save to `technology-stack-decision/stack-specification.md`
4. Produce **Compatibility & Integration Analysis**:
   - Inter-component compatibility verification
   - Version compatibility matrix
   - Known issues and workarounds
   - Save to `technology-stack-decision/compatibility-analysis.md`
5. Produce **Migration & Adoption Plan** (if replacing existing stack):
   - Migration path and phasing
   - Training requirements
   - Save to `technology-stack-decision/adoption-plan.md`
6. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
7. Generate Technology Stack Decision report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `tl-technology-stack-decision-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Technology Stack Decision report path
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
