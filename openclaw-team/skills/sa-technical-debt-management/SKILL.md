---
name: sa-technical-debt-management
description: "Interactive AI Agent skill for tracking and prioritizing technical debt and proposing remediation strategies through structured iterative dialogue. Use when: (1) technical debt needs to be identified and cataloged, (2) debt prioritization and remediation planning is required, (3) PM Agent assigns task IA-DEV-004 via RACI matrix, (4) assessing the impact of technical debt on architecture quality, (5) creating a debt backlog with cost-of-delay analysis, or (6) establishing debt governance policies and thresholds."
---

# SA Technical Debt Management Agent

Role: IT Architect (SA) | Task ID: IA-DEV-004 | Wave: 10, Step: 4

## Objective

Track and prioritize technical debt across the system — identifying debt sources, assessing impact on architecture quality, proposing remediation strategies, and establishing governance policies to prevent uncontrolled debt accumulation.

## Upstream Inputs (Architecture & Design Artifacts)

- IA-REQ-001: Architecture Design (C4 diagrams, deployment views, integration views)
- IA-DEV-001: Technical Guidance (pattern catalog, architecture-to-code mapping)
- IA-DEV-002: Code & Design Reviews (compliance matrix, review findings)
- IA-DEV-003: Spike/PoC Leadership (findings, risk assessment)
- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-004: Technology Blueprint

## Downstream Triggers (Wave 11 — Technical Lead)

Upon completion, PM Agent triggers: TL-DEV-001 (Code Review & Quality Gatekeeping), TL-DEV-002 (Hands-On Development), TL-DEV-003 (Technical Decision Making), TL-DEV-004 (Unblocking the Team), TL-DEV-005 (Technical Debt Governance).

## Workflow Overview

Manage technical debt through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why debt management is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand codebase state, known debt, architecture constraints -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Research debt management practices -> generate question list -> iterative dialogue -> validated scope
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Catalog debt -> prioritize -> produce remediation strategies, governance policies -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-DEV-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `technical-debt/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `debt-items/`
4. Initialize `technical-debt/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `technical-debt/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technical debt management is needed for this context
2. Formulate understanding of: goals, scope, debt categories, business impact concerns
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `technical-debt/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design artifacts (IA-REQ-001)
   - Technical Guidance outputs (IA-DEV-001)
   - Code & Design Review findings (IA-DEV-002)
   - Spike/PoC findings (IA-DEV-003)
   - Solution Architecture Document (SA-REQ-001)
   - Technology Blueprint (SA-REQ-004)
2. Gather additional context:
   - Known technical debt items
   - Codebase age and history
   - Team velocity and capacity
   - Business priorities and release cadence
   - Static analysis and code quality metrics
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `technical-debt/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry technical debt management practices
   - Save all research to `technical-debt/research/`
2. Generate comprehensive question list -> save to `technical-debt/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated debt management scope -> save to `technical-debt/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Identify and catalog technical debt:
   - Code-level debt (duplication, complexity, outdated patterns)
   - Architecture-level debt (architectural drift, missing abstractions)
   - Infrastructure debt (outdated dependencies, unsupported platforms)
   - Documentation debt (missing/outdated docs)
   - Test debt (insufficient test coverage)
2. Produce **Technical Debt Register**:
   - Complete debt inventory with severity, impact, cost-of-delay
   - Save to `technical-debt/debt-items/debt-register.md`
3. Produce **Debt Prioritization Matrix**:
   - Priority scoring based on impact, effort, risk, business value
   - Save to `technical-debt/debt-items/prioritization-matrix.md`
4. Produce **Remediation Strategy**:
   - Phased remediation plan with effort estimates
   - Quick wins vs. long-term refactoring
   - Save to `technical-debt/remediation-strategy.md`
5. Produce **Governance Policy**:
   - Debt acceptance criteria and thresholds
   - Monitoring and tracking mechanisms
   - Save to `technical-debt/governance-policy.md`
6. Produce **Technical Debt Report**:
   - Executive summary, metrics, trends, recommendations
   - Save to `technical-debt/technical-debt-report.md`
7. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
8. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-technical-debt-management-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Technical Debt report path
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
