---
name: tl-code-review-quality-gatekeeping
description: "Interactive AI Agent skill for ensuring code quality through systematic PR reviews, architectural compliance checks, and quality gates. Use when: (1) pull requests require technical review and approval, (2) code quality standards need enforcement, (3) architectural compliance must be verified in submitted code, (4) quality gate criteria need definition or evaluation, (5) PM Agent assigns task TL-DEV-001 via RACI matrix, or (6) code review metrics and trends need analysis."
---

# TL Code Review & Quality Gatekeeping Agent

Role: Technical Lead (TL) | Task ID: TL-DEV-001 | Wave: 11, Step: 1

## Objective

Ensure code quality through systematic PR reviews, architectural compliance checks, and quality gates — establishing and enforcing review standards that maintain codebase health and team alignment with architectural decisions.

## Upstream Inputs (Wave 10 — IT Architect)

- IA-REQ-001: Architecture Design (C4 diagrams, integration views, NFR alignment)
- Coding standards and conventions documentation
- Technical design and solution design specifications

## Downstream Triggers

Upon completion, downstream tasks in subsequent waves are triggered as needed.

## Workflow Overview

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why code review gatekeeping is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand codebase, architecture, standards, review scope -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Define review checklists, quality gates, review processes -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `code-review-quality-gatekeeping/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `reviews/`
4. Initialize `code-review-quality-gatekeeping/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `code-review-quality-gatekeeping/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why code review and quality gatekeeping is needed for this context
2. Formulate understanding of: goals, scope, quality objectives, review types required
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `code-review-quality-gatekeeping/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design documents (IA-REQ-001)
   - Existing coding standards and conventions
   - Technical design specifications
   - Current codebase structure and patterns
2. Gather additional context:
   - Team size and experience levels
   - Existing review processes and tools
   - Quality metrics and targets
   - Known code quality issues
   - CI/CD pipeline integration points
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `code-review-quality-gatekeeping/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry code review practices and quality gate patterns
   - Save all research to `code-review-quality-gatekeeping/research/`
2. Generate comprehensive question list -> save to `code-review-quality-gatekeeping/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `code-review-quality-gatekeeping/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Produce deliverables:
   - **PR Review Checklist**: Comprehensive checklist for code review
   - **Architectural Compliance Matrix**: Mapping code patterns to architecture decisions
   - **Quality Gate Definitions**: Entry/exit criteria for each quality gate
   - **Review Process Guide**: Step-by-step review workflow
   - **Code Review Metrics Dashboard**: KPIs and tracking mechanisms
   - **Automated Check Configuration**: Linter rules, static analysis config
3. Produce **Review Standards Document**:
   - Review types (quick review, standard review, deep review)
   - Severity classification for findings
   - Escalation procedures
   - Save to `code-review-quality-gatekeeping/review-standards.md`
4. Produce **Quality Gate Report**:
   - Gate definitions and thresholds
   - Compliance tracking
   - Save to `code-review-quality-gatekeeping/quality-gate-report.md`
5. Generate all configuration files (OUT-01 through OUT-10)
6. Generate Code Review Quality Gatekeeping report
7. Run DoD self-verification with `scripts/verify_dod.py`
8. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `tl-code-review-quality-gatekeeping-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Code Review Quality Gatekeeping report path
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
