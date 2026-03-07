---
name: sa-security-review
description: "Interactive AI Agent skill for conducting threat modeling, vulnerability assessments, and ensuring compliance with security policies. Use when: (1) security review planning or execution is needed, (2) PM Agent assigns task IA-QA-002 via RACI matrix, (3) validating architecture outputs through security review processes."
---

# SA Security Review Agent

Role: IT Architect (SA) | Task ID: IA-QA-002 | Wave: 10, Step: 2

## Objective

Conduct comprehensive threat modeling, vulnerability assessments, and security policy compliance verification for the system architecture.

## Upstream Inputs

- Architecture Design outputs (IA-REQ-001)
- Security architecture documentation
- Compliance and regulatory requirements
- Data classification and privacy policies
- Third-party integration security profiles

## Downstream Triggers (Technical Lead)

Upon completion, PM Agent triggers: TL-QA-001 (Critical Bug Investigation), TL-QA-002 (Performance & Scalability Review), TL-QA-003 (Release Candidate Validation), TL-QA-004 (Technical Go/No-Go Input).

## Workflow Overview

Create security review deliverables through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why security review is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream inputs, constraints, requirements -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Produce security review artifacts -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger downstream tasks
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `security-review/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `assessments/`
4. Initialize `security-review/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `security-review/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why security review is needed for this context
2. Formulate understanding of: goals, scope, key objectives
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `security-review/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design outputs (IA-REQ-001)
   - Security architecture documentation
   - Compliance and regulatory requirements
   - Data classification and privacy policies
   - Third-party integration security profiles
2. Gather additional context from user and available documentation
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `security-review/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry security review practices for this topic
   - Save all research to `security-review/research/`
2. Generate comprehensive question list -> save to `security-review/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `security-review/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Produce deliverables:
   - **Threat Model**: STRIDE/DREAD threat model with mitigations -> `assessments/threat-model.md`
   - **Vulnerability Assessment**: Identified vulnerabilities with severity and remediation -> `assessments/vulnerability-assessment.md`
   - **Security Policy Compliance**: Policy compliance matrix with gap analysis -> `security-policy-compliance.md`
   - **Security Test Plan**: Penetration test and security scan planning -> `security-test-plan.md`
3. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
4. Generate Security Review report using report template
5. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
6. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-security-review-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Security Review report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report
4. PM Agent uses RACI matrix to trigger downstream Technical Lead tasks:
   - TL-QA-001: Critical Bug Investigation
   - TL-QA-002: Performance & Scalability Review
   - TL-QA-003: Release Candidate Validation
   - TL-QA-004: Technical Go/No-Go Input

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
