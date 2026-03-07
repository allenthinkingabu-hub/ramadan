---
name: sa-technology-selection
description: "Interactive AI Agent skill for recommending technology stacks, platforms, and frameworks aligned with project goals through structured iterative dialogue. Use when: (1) technology selection or stack evaluation is needed, (2) comparing frameworks/platforms/tools for a project, (3) PM Agent assigns task IA-INC-003 via RACI matrix, (4) making build-vs-buy decisions, or (5) evaluating vendor products and open-source alternatives."
---

# SA Technology Selection Agent

Role: System Architect (SA) | Task ID: IA-INC-003

## Workflow Overview

Create technology selection recommendations through an interactive, phased process:

```
Phase 0: Initialization
  → Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  → Present understanding of why technology selection is needed → user confirms
Phase 2: Understand the Topic (Step 2)
  → Understand business context, project requirements, existing technology stack, infrastructure constraints, team capabilities, budget boundaries → user confirms
Phase 3: Research & Question Generation (Step 3)
  → Industry research → generate question list → iterative dialogue → validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  → Technology candidates evaluation, weighted scoring matrix, proof-of-concept recommendations, vendor/license analysis, TCO comparison → DoD self-verify
Phase 5: Completion & Handoff
  → Trigger Supervisor → remediate if needed → notify PM Agent
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `technology-selection/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize `technology-selection/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `technology-selection/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technology selection is needed for this context
2. Formulate understanding of: goals, scope, evaluation objectives, technology categories to evaluate
3. Present structured understanding to user, ask for confirmation
4. If rejected → refine and repeat. If confirmed → log and proceed
5. Record all questions in `technology-selection/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather:
   - Business context and strategic goals
   - Project requirements (functional and non-functional)
   - Existing technology stack and integration points
   - Infrastructure constraints (cloud, on-premise, hybrid)
   - Team capabilities and skill gaps
   - Budget boundaries and procurement constraints
2. Present structured understanding to user, ask for confirmation
3. If rejected → return to Phase 1. If confirmed → log and proceed
4. Record all questions in `technology-selection/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry technology selection practices for this topic
   - Save all research to `technology-selection/research/`
2. Generate comprehensive question list → save to `technology-selection/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list → save to `technology-selection/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Identify candidate technologies per category
3. Create weighted scoring matrix with evaluation criteria
4. Evaluate each candidate against criteria
5. Conduct TCO analysis for top candidates
6. Assess vendor viability, licensing models, and support options
7. Produce recommendation with rationale
8. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
9. Generate Technology Selection report using report template
10. Output all deliverables to `technology-selection/` directory
11. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
12. If any item fails → fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-technology-selection-supervisor` skill for inspection
2. If inspection returns failures → remediate item-by-item, re-trigger supervisor
3. Once 100% pass → notify PM Agent with:
   - Technology Selection report path
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
