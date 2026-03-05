---
name: tl-hands-on-development
description: "Interactive AI Agent skill for contributing directly to codebase on critical paths, complex features, and setting implementation patterns. Use when: (1) critical path features need TL implementation, (2) complex features require senior-level coding, (3) reference implementations or patterns need to be established, (4) PM Agent assigns task TL-DEV-002 via RACI matrix, or (5) prototype or proof-of-concept development is needed."
---

# TL Hands-On Development Agent

Role: Technical Lead (TL) | Task ID: TL-DEV-002 | Wave: 11, Step: 2

## Objective

Contribute directly to the codebase on critical paths, complex features, and setting implementation patterns -- leading by example and establishing coding standards through reference implementations.

## Upstream Inputs (Wave 10 -- IT Architect)

- IA-REQ-001: Architecture Design (C4 diagrams, integration views, NFR alignment)
- Technical design and solution design specifications
- Coding standards and conventions documentation

## Downstream Triggers

Upon completion, downstream tasks in subsequent waves are triggered as needed.

## Workflow Overview

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why hands-on development is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand feature requirements, architecture, patterns, constraints -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Implement code, create reference patterns, document decisions -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `hands-on-development/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `implementations/`
4. Initialize `hands-on-development/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `hands-on-development/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why hands-on TL development is needed for this context
2. Formulate understanding of: goals, scope, critical paths, pattern requirements
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `hands-on-development/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design documents (IA-REQ-001)
   - Technical design specifications
   - Coding standards and conventions
   - Existing codebase patterns
2. Gather additional context:
   - Feature requirements and acceptance criteria
   - Technology stack and framework constraints
   - Team skill gaps requiring TL implementation
   - Performance and scalability requirements
   - Integration points and dependencies
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `hands-on-development/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research implementation patterns and best practices for the technology stack
   - Save all research to `hands-on-development/research/`
2. Generate comprehensive question list -> save to `hands-on-development/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `hands-on-development/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Produce deliverables:
   - **Reference Implementations**: Pattern-setting code for team to follow
   - **Critical Path Code**: Implementation of high-risk or complex features
   - **Implementation Guide**: Documentation of patterns and decisions
   - **Code Documentation**: Inline documentation and API docs
   - **Test Suite**: Unit and integration tests for implemented code
3. Produce **Implementation Patterns Document**:
   - Established patterns and their rationale
   - Anti-patterns to avoid
   - Save to `hands-on-development/implementation-patterns.md`
4. Produce **Development Report**:
   - What was implemented and why
   - Technical decisions and trade-offs
   - Save to `hands-on-development/hands-on-development-report.md`
5. Generate all configuration files (OUT-01 through OUT-10)
6. Run DoD self-verification with `scripts/verify_dod.py`
7. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `tl-hands-on-development-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Hands-On Development report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report

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
