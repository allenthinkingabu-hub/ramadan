---
name: tl-technical-decision-making
description: "Interactive AI Agent skill for making day-to-day technical decisions on implementation approaches, library choices, and trade-offs. Use when: (1) implementation approach decisions are needed, (2) library or framework selection is required, (3) technical trade-off analysis is needed, (4) PM Agent assigns task TL-DEV-003 via RACI matrix, or (5) technology evaluation and comparison is required."
---

# TL Technical Decision Making Agent

Role: Technical Lead (TL) | Task ID: TL-DEV-003 | Wave: 11, Step: 3

## Objective

Make informed day-to-day technical decisions on implementation approaches, library choices, and trade-offs -- documenting rationale and ensuring alignment with architecture and project goals.

## Upstream Inputs (Wave 10 -- IT Architect)

- IA-REQ-001: Architecture Design (C4 diagrams, integration views, NFR alignment)
- Technology Blueprint and stack decisions
- Non-functional requirements mapping

## Downstream Triggers

Upon completion, downstream tasks in subsequent waves are triggered as needed.

## Workflow Overview

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why technical decisions are needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand decision context, constraints, options, criteria -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Evaluate options, document decisions, produce ADRs -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `technical-decision-making/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `decisions/`
4. Initialize `technical-decision-making/conversation-log.md`
5. Initialize `technical-decision-making/work-log.md`
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technical decision-making support is needed
2. Formulate understanding of: decision scope, constraints, urgency, impact
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `technical-decision-making/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design documents (IA-REQ-001)
   - Technology Blueprint and stack decisions
   - NFR requirements and constraints
   - Existing technical decisions and ADRs
2. Gather additional context:
   - Decision drivers and business context
   - Technical constraints and dependencies
   - Team capabilities and experience
   - Timeline and budget constraints
   - Risk tolerance
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `technical-decision-making/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research alternatives and industry practices
   - Save all research to `technical-decision-making/research/`
2. Generate comprehensive question list -> save to `technical-decision-making/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `technical-decision-making/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct detailed evaluation of alternatives
2. Produce deliverables:
   - **Architecture Decision Records (ADRs)**: Formal decision documentation
   - **Trade-off Analysis**: Comparison matrices and evaluations
   - **Decision Log**: Chronological record of decisions made
   - **Impact Assessment**: Risk and impact analysis for each decision
   - **Implementation Guidelines**: How to implement chosen approaches
3. Produce **Trade-off Analysis Document**:
   - Options evaluated with pros/cons
   - Scoring criteria and weights
   - Save to `technical-decision-making/trade-off-analysis.md`
4. Produce **Decision Register**:
   - All decisions with status, rationale, and impact
   - Save to `technical-decision-making/decision-register.md`
5. Generate all configuration files (OUT-01 through OUT-10)
6. Generate Technical Decision Making report
7. Run DoD self-verification with `scripts/verify_dod.py`
8. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `tl-technical-decision-making-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Technical Decision Making report path
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
