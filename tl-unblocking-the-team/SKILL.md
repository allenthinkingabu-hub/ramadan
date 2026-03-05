---
name: tl-unblocking-the-team
description: "Interactive AI Agent skill for removing technical blockers, debugging complex issues, and providing guidance to unblock team members. Use when: (1) team members are blocked on technical issues, (2) complex debugging requires senior expertise, (3) cross-team dependencies need resolution, (4) PM Agent assigns task TL-DEV-004 via RACI matrix, or (5) technical guidance is needed to unblock progress."
---

# TL Unblocking the Team Agent

Role: Technical Lead (TL) | Task ID: TL-DEV-004 | Wave: 11, Step: 4

## Objective

Remove technical blockers, debug complex issues, and provide guidance to unblock team members -- ensuring development velocity is maintained and impediments are resolved systematically.

## Upstream Inputs (Wave 10 -- IT Architect)

- IA-REQ-001: Architecture Design (C4 diagrams, integration views, NFR alignment)
- Technical design and solution design specifications

## Downstream Triggers

Upon completion, downstream tasks in subsequent waves are triggered as needed.

## Workflow Overview

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why unblocking support is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand blocker context, dependencies, team impact -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Research solutions -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Resolve blockers, document solutions, create escalation procedures -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `unblocking-the-team/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `resolutions/`
4. Initialize `unblocking-the-team/conversation-log.md`
5. Initialize `unblocking-the-team/work-log.md`
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why unblocking support is needed
2. Formulate understanding of: blocker types, affected team members, urgency, impact
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `unblocking-the-team/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design documents (IA-REQ-001)
   - Current sprint/iteration status
   - Known dependencies and integration points
2. Gather additional context:
   - Specific blockers and their symptoms
   - Team members affected and their skill levels
   - Duration of blockage and business impact
   - Previous attempts at resolution
   - Cross-team dependencies
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `unblocking-the-team/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research solutions for identified blockers
   - Save all research to `unblocking-the-team/research/`
2. Generate comprehensive question list -> save to `unblocking-the-team/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `unblocking-the-team/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Investigate and resolve identified blockers
2. Produce deliverables:
   - **Blocker Resolution Log**: Detailed record of each blocker and its resolution
   - **Debugging Guides**: Step-by-step debugging procedures for common issues
   - **Escalation Procedures**: Clear escalation paths for different blocker types
   - **Knowledge Transfer Notes**: Solutions documented for team learning
   - **Dependency Resolution Plan**: Cross-team dependency management
3. Produce **Blocker Resolution Report**:
   - All blockers identified, investigated, and resolved
   - Root cause analysis for each
   - Save to `unblocking-the-team/blocker-resolution-report.md`
4. Produce **Escalation Framework**:
   - Escalation criteria, paths, and SLAs
   - Save to `unblocking-the-team/escalation-framework.md`
5. Generate all configuration files (OUT-01 through OUT-10)
6. Generate Unblocking the Team report
7. Run DoD self-verification with `scripts/verify_dod.py`
8. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `tl-unblocking-the-team-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Unblocking the Team report path
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
