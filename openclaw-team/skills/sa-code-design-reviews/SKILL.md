---
name: sa-code-design-reviews
description: "Interactive AI Agent skill for reviewing critical code, pull requests, and component designs for architectural compliance through structured iterative dialogue. Use when: (1) critical code or pull requests need architectural review, (2) component designs require compliance verification against the approved architecture, (3) PM Agent assigns task IA-DEV-002 via RACI matrix, (4) ensuring code changes align with C4/UML architecture, integration patterns, and NFRs, (5) validating design patterns and coding standards adherence, or (6) catching architectural drift in implementation."
---

# SA Code & Design Reviews Agent

Role: IT Architect (SA) | Task ID: IA-DEV-002 | Wave: 10, Step: 2

## Objective

Review critical code, pull requests, and component designs for architectural compliance — ensuring implementation adheres to the approved architecture design, design patterns, integration contracts, and non-functional requirements.

## Upstream Inputs (Architecture & Design Artifacts)

- IA-REQ-001: Architecture Design (C4 diagrams, deployment views, integration views)
- IA-DEV-001: Technical Guidance (pattern catalog, architecture-to-code mapping)
- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-004: Technology Blueprint
- TL-REQ-002: Coding Standards & Conventions (if available)

## Downstream Triggers (Wave 11 — Technical Lead)

Upon completion, PM Agent triggers: TL-DEV-001 (Code Review & Quality Gatekeeping), TL-DEV-002 (Hands-On Development), TL-DEV-003 (Technical Decision Making), TL-DEV-004 (Unblocking the Team), TL-DEV-005 (Technical Debt Governance).

## Workflow Overview

Conduct code and design reviews through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why review is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand code/PR context, architecture baseline, review scope -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Research review criteria -> generate question list -> iterative dialogue -> validated review scope
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Conduct review -> produce review findings, compliance report, remediation plan -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-DEV-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `code-design-reviews/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `reviews/`
4. Initialize `code-design-reviews/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `code-design-reviews/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why code/design review is needed for this context
2. Formulate understanding of: goals, scope, review type (code/PR/design), compliance areas
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `code-design-reviews/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design artifacts (IA-REQ-001)
   - Technical Guidance outputs (IA-DEV-001)
   - Solution Architecture Document (SA-REQ-001)
   - Technology Blueprint (SA-REQ-004)
   - Coding Standards (TL-REQ-002 if available)
2. Gather additional context:
   - Code or PR to be reviewed
   - Component design documents under review
   - Known architectural constraints and NFRs
   - Previous review findings (if any)
   - Integration contracts and interface specifications
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `code-design-reviews/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry code review best practices and architectural compliance patterns
   - Save all research to `code-design-reviews/research/`
2. Generate comprehensive question list -> save to `code-design-reviews/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated review scope -> save to `code-design-reviews/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct architectural review of code/PR/design:
   - Verify compliance with C4 architecture (component boundaries, dependencies)
   - Check design pattern adherence
   - Validate integration contract compliance
   - Assess NFR implementation (performance, security, resilience)
   - Identify architectural drift
2. Produce **Review Findings Report**:
   - Per-file/component findings with severity ratings
   - Architecture compliance status per component
   - Save to `code-design-reviews/code-design-review-report.md`
3. Produce **Compliance Matrix**:
   - Architecture requirement vs. implementation compliance
   - NFR compliance assessment
   - Save to `code-design-reviews/compliance-matrix.md`
4. Produce **Remediation Plan**:
   - Prioritized list of issues to fix
   - Suggested fixes with rationale
   - Save to `code-design-reviews/remediation-plan.md`
5. Produce **Review Decision Log**:
   - Review decisions (approve, request changes, reject)
   - Conditions for approval
   - Save to `code-design-reviews/review-decision-log.md`
6. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
7. Generate Code & Design Review report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-code-design-reviews-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Code & Design Review report path
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
