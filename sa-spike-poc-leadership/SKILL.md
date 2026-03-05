---
name: sa-spike-poc-leadership
description: "Interactive AI Agent skill for leading technical spikes and proof-of-concepts to de-risk uncertain areas through structured iterative dialogue. Use when: (1) technical uncertainty needs to be resolved before committing to an approach, (2) a proof-of-concept is needed to validate feasibility, (3) PM Agent assigns task IA-DEV-003 via RACI matrix, (4) evaluating competing technology options or architectural approaches, (5) de-risking integration with third-party systems, or (6) validating performance characteristics of proposed designs."
---

# SA Spike & PoC Leadership Agent

Role: IT Architect (SA) | Task ID: IA-DEV-003 | Wave: 10, Step: 3

## Objective

Lead technical spikes and proof-of-concepts to de-risk uncertain areas — defining spike objectives, executing targeted investigations, building minimal PoCs, and producing actionable findings that inform architecture and implementation decisions.

## Upstream Inputs (Architecture & Design Artifacts)

- IA-REQ-001: Architecture Design (C4 diagrams, deployment views, integration views)
- IA-DEV-001: Technical Guidance (pattern catalog, architecture-to-code mapping)
- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: ARB Feedback

## Downstream Triggers (Wave 11 — Technical Lead)

Upon completion, PM Agent triggers: TL-DEV-001 (Code Review & Quality Gatekeeping), TL-DEV-002 (Hands-On Development), TL-DEV-003 (Technical Decision Making), TL-DEV-004 (Unblocking the Team), TL-DEV-005 (Technical Debt Governance).

## Workflow Overview

Lead spikes and PoCs through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why spike/PoC is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand uncertainty area, risks, constraints, success criteria -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Research approaches -> generate question list -> iterative dialogue -> validated spike plan
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Execute spike/PoC -> produce findings, recommendation report, decision record -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-DEV-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `spike-poc/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `poc-code/`, `findings/`
4. Initialize `spike-poc/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `spike-poc/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why the spike or PoC is needed for this context
2. Formulate understanding of: goals, uncertainty area, risks to de-risk, success/failure criteria
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `spike-poc/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture Design artifacts (IA-REQ-001)
   - Technical Guidance outputs (IA-DEV-001)
   - Solution Architecture Document (SA-REQ-001)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Specific uncertainty or risk to investigate
   - Competing technology options or approaches
   - Time-box and resource constraints
   - Performance/scalability/integration targets
   - Acceptance criteria for PoC success
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `spike-poc/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry approaches to the uncertainty area
   - Save all research to `spike-poc/research/`
2. Generate comprehensive question list -> save to `spike-poc/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated spike plan -> save to `spike-poc/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Define spike/PoC plan:
   - Hypothesis to test
   - Approach and methodology
   - Time-box and deliverables
   - Success/failure criteria
2. Execute spike/PoC:
   - Build minimal PoC code (save to `spike-poc/poc-code/`)
   - Run experiments and benchmarks
   - Document observations and measurements
3. Produce **Spike/PoC Findings Report**:
   - Hypothesis tested and results
   - Performance/feasibility measurements
   - Risks identified and mitigated
   - Save to `spike-poc/spike-poc-report.md`
4. Produce **Technology Comparison Matrix** (if applicable):
   - Side-by-side comparison of evaluated options
   - Scoring against criteria
   - Save to `spike-poc/findings/technology-comparison.md`
5. Produce **Recommendation & Decision Record**:
   - Recommended approach with rationale
   - Impact on architecture design
   - Save to `spike-poc/findings/recommendation-decision.md`
6. Produce **Risk Assessment Update**:
   - Updated risk register based on findings
   - Residual risks after spike
   - Save to `spike-poc/findings/risk-assessment.md`
7. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
8. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-spike-poc-leadership-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Spike/PoC report path
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
