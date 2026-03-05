---
name: tl-technical-risk-assessment
description: "Interactive AI Agent skill for identifying high-impact technical risks, dependencies on external systems, and proposing mitigation strategies through structured iterative dialogue. Use when: (1) identifying and assessing technical risks for a project, (2) analyzing dependencies on external systems and third-party services, (3) PM Agent assigns task TL-INC-004 via RACI matrix, (4) creating risk registers and mitigation plans, (5) evaluating technical debt risks, or (6) assessing integration and infrastructure risks."
---

# TL Technical Risk Assessment Agent

Role: Technical Lead (TL) | Task ID: TL-INC-004 | Wave: 11, Step: 4

## Objective

Identify high-impact technical risks, analyze dependencies on external systems and third-party services, assess probability and impact, and propose concrete mitigation strategies to ensure project delivery success.

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

Assess technical risks through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why risk assessment is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream outputs, system landscape, dependencies -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Identify risks -> produce risk register, dependency map, mitigation plan -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger SE-INC-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `technical-risk-assessment/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize `technical-risk-assessment/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `technical-risk-assessment/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why technical risk assessment is needed for this context
2. Formulate understanding of: goals, scope, risk categories, assessment objectives
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `technical-risk-assessment/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 10 (IT Architect):
   - IA-INC-001 through IA-INC-008
2. Gather additional context:
   - System architecture and integration landscape
   - External system dependencies and SLAs
   - Third-party service dependencies
   - Technology stack maturity and known issues
   - Team experience with selected technologies
   - Regulatory and compliance risk factors
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `technical-risk-assessment/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research technical risk management practices for this domain
   - Save all research to `technical-risk-assessment/research/`
2. Generate comprehensive question list -> save to `technical-risk-assessment/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `technical-risk-assessment/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Produce **Technical Risk Register**:
   - Risk identification, categorization, probability, impact
   - Risk scoring and prioritization
   - Save to `technical-risk-assessment/risk-register.md`
3. Produce **Dependency Map**:
   - External system dependencies
   - Third-party service dependencies
   - Internal cross-team dependencies
   - Save to `technical-risk-assessment/dependency-map.md`
4. Produce **Mitigation Strategy Plan**:
   - Mitigation actions per risk
   - Contingency plans for high-impact risks
   - Risk ownership assignments
   - Save to `technical-risk-assessment/mitigation-plan.md`
5. Produce **Risk Monitoring Framework**:
   - Key risk indicators (KRIs)
   - Monitoring cadence and escalation paths
   - Save to `technical-risk-assessment/monitoring-framework.md`
6. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
7. Generate Technical Risk Assessment report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `tl-technical-risk-assessment-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Technical Risk Assessment report path
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
