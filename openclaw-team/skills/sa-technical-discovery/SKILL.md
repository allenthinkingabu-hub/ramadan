---
name: sa-technical-discovery
description: "Interactive AI Agent skill for conducting comprehensive technical discovery — assessing the current technology landscape, existing systems, and infrastructure capabilities. Use when: (1) a technical discovery or technology assessment is needed for a project, (2) evaluating existing systems and infrastructure, (3) PM Agent assigns task IA-INC-001 via RACI matrix, (4) conducting architecture reviews or technology audits, or (5) assessing current-state technology for modernization or migration planning."
---

# SA Technical Discovery Agent

Role: System Architect (SA) | Task ID: IA-INC-001

## Workflow Overview

Conduct technical discovery through an interactive, phased process:

```
Phase 0: Initialization
  → Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  → Present understanding of why technical discovery is needed → user confirms
Phase 2: Understand the Topic (Step 2)
  → Understand project/system, business context, tech stack, architecture → user confirms
Phase 3: Research & Question Generation (Step 3)
  → Industry research → generate question list → iterative dialogue → validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  → Assess technology landscape → produce all outputs → DoD self-verify
Phase 5: Completion & Handoff
  → Trigger Supervisor → remediate if needed → notify PM Agent
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `technical-discovery/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize `technical-discovery/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `technical-discovery/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technical discovery is needed
2. Formulate understanding of: goals, scope, assessment objectives
3. Present structured understanding to user, ask for confirmation
4. If rejected → refine and repeat. If confirmed → log and proceed
5. Record all questions in `technical-discovery/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather: business context, existing technology stack, system architecture landscape, infrastructure environment, project constraints
2. Present structured understanding to user, ask for confirmation
3. If rejected → return to Phase 1. If confirmed → log and proceed
4. Record all questions in `technical-discovery/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry practices for technical discovery on this topic
   - Save all research to `technical-discovery/research/`
2. Generate comprehensive question list → save to `technical-discovery/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list → save to `technical-discovery/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Assess the technology landscape:
   - **Technology stack**: inventory and evaluation of all current technologies
   - **System architecture**: architecture diagrams and descriptions
   - **Infrastructure**: components, configurations, capacity
   - **Integration points**: dependencies, data flows, APIs
   - **Security posture**: authentication, authorization, compliance
3. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
4. Generate Technical Discovery report using report template
5. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
6. If any item fails → fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `SA-technical-discovery-supervisor` skill for inspection
2. If inspection returns failures → remediate item-by-item, re-trigger supervisor
3. Once 100% pass → notify PM Agent with:
   - Technical Discovery report path
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
