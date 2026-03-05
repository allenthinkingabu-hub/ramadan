---
name: tl-team-capability-assessment
description: "Interactive AI Agent skill for evaluating team skills, identifying gaps, and recommending training, hiring, or knowledge transfer needs through structured iterative dialogue. Use when: (1) assessing team capabilities for a project, (2) identifying skill gaps relative to technical requirements, (3) PM Agent assigns task TL-INC-003 via RACI matrix, (4) planning training or hiring to address capability gaps, (5) creating a skills matrix and development plan, or (6) evaluating team readiness for selected technology stack."
---

# TL Team Capability Assessment Agent

Role: Technical Lead (TL) | Task ID: TL-INC-003 | Wave: 11, Step: 3

## Objective

Evaluate team skills against project requirements, identify capability gaps, and recommend training, hiring, or knowledge transfer strategies to ensure the team can deliver successfully.

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

Assess team capabilities through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why capability assessment is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream outputs, team composition, project requirements -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Assess skills -> produce skills matrix, gap analysis, development plan -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger SE-INC-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `team-capability-assessment/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize `team-capability-assessment/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `team-capability-assessment/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why team capability assessment is needed for this context
2. Formulate understanding of: goals, scope, team size, assessment objectives
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `team-capability-assessment/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 10 (IT Architect):
   - IA-INC-001 through IA-INC-008
2. Gather additional context:
   - Current team composition and roles
   - Individual skill profiles (if available)
   - Technology stack decisions (from TL-INC-002 if available)
   - Project complexity and domain requirements
   - Timeline constraints affecting ramp-up
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `team-capability-assessment/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research team assessment methodologies and capability frameworks
   - Save all research to `team-capability-assessment/research/`
2. Generate comprehensive question list -> save to `team-capability-assessment/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `team-capability-assessment/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Produce **Team Skills Matrix**:
   - Individual and team-level skill ratings
   - Required vs. current proficiency levels
   - Save to `team-capability-assessment/skills-matrix.md`
3. Produce **Gap Analysis**:
   - Identified skill gaps by category
   - Severity and impact assessment
   - Save to `team-capability-assessment/gap-analysis.md`
4. Produce **Development & Remediation Plan**:
   - Training recommendations
   - Hiring recommendations
   - Knowledge transfer strategies
   - Mentoring and pairing plans
   - Save to `team-capability-assessment/development-plan.md`
5. Produce **Team Readiness Assessment**:
   - Overall readiness score
   - Risk areas and mitigation
   - Save to `team-capability-assessment/readiness-assessment.md`
6. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
7. Generate Team Capability Assessment report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `tl-team-capability-assessment-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Team Capability Assessment report path
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
