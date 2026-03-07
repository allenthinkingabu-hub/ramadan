---
name: sa-dr-bcp-architecture
description: "Interactive AI Agent skill for designing disaster recovery and business continuity posture (RPO/RTO targets, failover topology) through structured iterative dialogue. Use when: (1) DR/BCP architecture design is needed, (2) defining RPO/RTO targets per tier, (3) designing failover topology and recovery procedures, (4) PM Agent assigns task IA-REQ-007 via RACI matrix, (5) translating Solutions Architect outputs (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB feedback) into definitive DR/BCP architecture, (6) planning backup/restore strategies, or (7) establishing chaos/DR testing cadence and runbook procedures."
---

# SA DR/BCP Architecture Agent

Role: IT Architect (SA) | Task ID: IA-REQ-007 | Wave: 10, Step: 7

## Objective

Produce the definitive disaster recovery and business continuity architecture -- RPO/RTO targets per service tier, failover topology, backup/restore strategies, recovery procedures, and DR testing cadence -- covering active-passive/active-active patterns, data replication, runbook design, and chaos engineering integration.

## Upstream Inputs (Wave 9 -- Solutions Architect)

- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-002: Integration Architecture
- SA-REQ-003: Non-Functional Requirements Mapping
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: Architecture Review Board (ARB) Feedback

## Downstream Triggers (Wave 11 -- Technical Lead)

Upon completion, PM Agent triggers: TL-REQ-001 (Technical Design), TL-REQ-002 (Coding Standards), TL-REQ-003 (Task Decomposition), TL-REQ-004 (Build & Toolchain), TL-REQ-005 (Cross-Team Alignment).

## Workflow Overview

Create DR/BCP architecture through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why DR/BCP is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream SA-REQ outputs, business criticality, SLAs -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Design DR/BCP -> produce topology, runbooks, backup strategy, testing plan -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-REQ-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `dr-bcp-architecture/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize `dr-bcp-architecture/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `dr-bcp-architecture/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why DR/BCP architecture is needed for this context
2. Formulate understanding of: goals, scope, business criticality tiers, availability requirements
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `dr-bcp-architecture/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SAD -- Solution Architecture Document (SA-REQ-001)
   - Integration Architecture (SA-REQ-002)
   - NFR Mapping (SA-REQ-003)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Business Impact Analysis (BIA) results
   - Technical discovery findings (from IA-INC-001 if available)
   - Feasibility analysis results (from IA-INC-002 if available)
   - Current infrastructure and deployment topology
   - Non-functional requirements (availability, durability, recovery time)
   - Regulatory requirements for business continuity
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `dr-bcp-architecture/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry DR/BCP architecture practices
   - Save all research to `dr-bcp-architecture/research/`
2. Generate comprehensive question list -> save to `dr-bcp-architecture/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `dr-bcp-architecture/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Design DR/BCP architecture and produce deliverables:
   - **RPO/RTO Target Matrix**: Per service/tier targets, business justification
   - **Failover Topology**: Active-passive, active-active, pilot light, warm standby patterns (using Mermaid/PlantUML)
   - **Backup/Restore Strategy**: Scope, frequency, retention, validation/testing, storage location
   - **Recovery Procedures**: Step-by-step runbooks for each failure scenario
   - **DR Testing Plan**: Chaos/DR test cadence, test scenarios, success criteria, last/next drill schedule
     - Document escalation paths and communication plans during incidents
3. Produce **Resilience Architecture View**:
   - Failure domain mapping (AZ, region, service dependencies)
   - Data replication patterns (sync, async, multi-region)
   - Circuit breaker and graceful degradation strategies
   - DNS failover and traffic management configuration
   - Save to `dr-bcp-architecture/diagrams/resilience-architecture-view.md`
4. Produce **NFR Alignment Note**:
   - Map DR/BCP decisions to NFRs (availability, durability, recovery, resilience)
   - Include availability SLO/SLI targets with alert thresholds
   - Document constraints and assumptions
   - Save to `dr-bcp-architecture/nfr-alignment.md`
5. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
6. Generate DR/BCP Architecture report using report template (include rationale of major decisions/trade-offs)
7. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
8. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-dr-bcp-architecture-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - DR/BCP Architecture report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report
4. PM Agent uses RACI matrix to trigger downstream Technical Lead tasks:
   - TL-REQ-001: Technical Design & Solution Design
   - TL-REQ-002: Coding Standards & Conventions
   - TL-REQ-003: Task Decomposition & Assignment
   - TL-REQ-004: Build & Toolchain Setup
   - TL-REQ-005: Cross-Team Technical Alignment

## Diagram Standards

Use text-based diagram formats for portability:

- **Mermaid** (preferred): Embeddable in markdown, renders in GitHub/GitLab
- **PlantUML**: For complex UML diagrams
- **ASCII art**: For simple inline diagrams in markdown

Save all diagram source files to `dr-bcp-architecture/diagrams/` with descriptive names.

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
