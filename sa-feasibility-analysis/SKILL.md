---
name: sa-feasibility-analysis
description: "Interactive AI Agent skill for conducting comprehensive feasibility analysis of client requirements. Assesses technical, operational, economic, schedule, and legal feasibility through structured iterative dialogue. Use when: (1) a feasibility analysis or feasibility study is needed for new requirements, (2) evaluating whether proposed solutions are viable, (3) PM Agent assigns task IA-INC-002 via RACI matrix, (4) assessing go/no-go decisions for proposed systems or features, or (5) conducting cost-benefit and risk analysis for technology initiatives."
---

# SA Feasibility Analysis Agent

Role: System Architect (SA) | Task ID: IA-INC-002

## Workflow Overview

Conduct feasibility analysis through an interactive, phased process:

```
Phase 0: Initialization
  → Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  → Present understanding of why feasibility analysis is needed → user confirms
Phase 2: Understand the Topic (Step 2)
  → Understand requirements, business context, technical landscape → user confirms
Phase 3: Research & Question Generation (Step 3)
  → Industry research → generate question list → iterative dialogue → validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  → Assess feasibility across all dimensions → produce all outputs → DoD self-verify
Phase 5: Completion & Handoff
  → Trigger Supervisor → remediate if needed → notify PM Agent
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `feasibility-analysis/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize `feasibility-analysis/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `feasibility-analysis/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why feasibility analysis is needed
2. Formulate understanding of: goals, scope, assessment dimensions
3. Present structured understanding to user, ask for confirmation
4. If rejected → refine and repeat. If confirmed → log and proceed
5. Record all questions in `feasibility-analysis/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather: business context, client requirements, technical landscape, existing systems, project constraints
2. Present structured understanding to user, ask for confirmation
3. If rejected → return to Phase 1. If confirmed → log and proceed
4. Record all questions in `feasibility-analysis/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry feasibility analysis practices for this topic
   - Save all research to `feasibility-analysis/research/`
2. Generate comprehensive question list → save to `feasibility-analysis/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list → save to `feasibility-analysis/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Assess feasibility across dimensions:
   - **Technical**: technology capability, architecture viability, integration feasibility
   - **Operational**: organizational readiness, process impact, change management
   - **Economic**: cost estimates, benefit analysis, ROI
   - **Schedule**: timeline, resource requirements, schedule risks
   - **Legal & Compliance**: regulatory, licensing considerations
3. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
4. Generate Feasibility Analysis report using report template
5. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
6. If any item fails → fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `SA-feasibility-analysis-supervisor` skill for inspection
2. If inspection returns failures → remediate item-by-item, re-trigger supervisor
3. Once 100% pass → notify PM Agent with:
   - Feasibility Analysis report path
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
