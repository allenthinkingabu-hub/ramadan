---
name: sa-architecture-design
description: "Interactive AI Agent skill for creating high-level and detailed architecture diagrams (C4, UML, sequence diagrams) through structured iterative dialogue. Use when: (1) architecture design or system design is needed, (2) creating C4 context/container/component/code diagrams, (3) producing UML class/sequence/activity diagrams, (4) PM Agent assigns task IA-REQ-001 via RACI matrix, (5) translating Solutions Architect outputs (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB feedback) into definitive architecture designs, (6) designing system integration and data flow architectures, or (7) producing interface/integration views with protocols, contracts, and error handling."
---

# SA Architecture Design Agent

Role: IT Architect (SA) | Task ID: IA-REQ-001 | Wave: 10, Step: 1

## Objective

Produce the definitive architecture design — logical + physical views — covering C4 layers (context/container/component), key sequence flows, integration points, and deployment/runtime topology.

## Upstream Inputs (Wave 9 — Solutions Architect)

- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-002: Integration Architecture
- SA-REQ-003: Non-Functional Requirements Mapping
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: Architecture Review Board (ARB) Feedback

## Downstream Triggers (Wave 11 — Technical Lead)

Upon completion, PM Agent triggers: TL-REQ-001 (Technical Design), TL-REQ-002 (Coding Standards), TL-REQ-003 (Task Decomposition), TL-REQ-004 (Build & Toolchain), TL-REQ-005 (Cross-Team Alignment).

## Workflow Overview

Create architecture designs through an interactive, phased process:

```
Phase 0: Initialization
  → Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  → Present understanding of why architecture design is needed → user confirms
Phase 2: Understand the Topic (Step 2)
  → Understand upstream SA-REQ outputs, business requirements, NFRs, integration constraints → user confirms
Phase 3: Research & Question Generation (Step 3)
  → Industry research → generate question list → iterative dialogue → validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  → Design architecture → produce diagrams, interface/integration view, NFR alignment → DoD self-verify
Phase 5: Completion & Handoff
  → Trigger Supervisor → remediate if needed → notify PM Agent → trigger TL-REQ-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites — see [references/dor.md](references/dor.md)
2. Create `architecture-design/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize `architecture-design/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `architecture-design/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why architecture design is needed for this context
2. Formulate understanding of: goals, scope, design objectives, diagram types required
3. Present structured understanding to user, ask for confirmation
4. If rejected → refine and repeat. If confirmed → log and proceed
5. Record all questions in `architecture-design/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SAD — Solution Architecture Document (SA-REQ-001)
   - Integration Architecture (SA-REQ-002)
   - NFR Mapping (SA-REQ-003)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Business requirements
   - Technical discovery findings (from IA-INC-001 if available)
   - Feasibility analysis results (from IA-INC-002 if available)
   - Selected technology stack
   - Non-functional requirements (performance, scalability, security, availability)
   - System integration constraints and interface contracts
3. Present structured understanding to user, ask for confirmation
4. If rejected → return to Phase 1. If confirmed → log and proceed
5. Record all questions in `architecture-design/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry architecture design practices for this topic
   - Save all research to `architecture-design/research/`
2. Generate comprehensive question list → save to `architecture-design/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list → save to `architecture-design/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Design architecture and produce diagrams:
   - **C4 Model**: Context, Container, Component, Code diagrams (using Mermaid/PlantUML)
   - **UML Diagrams**: Class, sequence, activity, deployment diagrams
   - **Data Flow**: Data flow diagrams, integration diagrams
   - **Infrastructure**: Deployment architecture, network topology
     - Document RPO/RTO targets per tier, backup/restore strategy (scope, frequency, retention, validation), and chaos/DR test cadence
3. Produce **Interface/Integration View**:
   - Protocols and communication patterns (REST, gRPC, messaging, etc.)
   - Interface contracts (API specs, message schemas, error codes, versioning/deprecation policy)
   - Error handling and resilience patterns (retry, circuit breaker, timeout, rate limits/backpressure, fallback)
   - Data minimization rules for external/LLM calls (what leaves the boundary, anonymization)
   - Save to `architecture-design/diagrams/integration-view.md`
4. Produce **NFR Alignment Note**:
   - Map architecture decisions to NFRs (performance, availability, security, resiliency)
   - Include observability SLO/SLI targets with alert thresholds and business KPIs (e.g., cost per grade, cache hit rate)
   - Document constraints and assumptions
   - Save to `architecture-design/nfr-alignment.md`
5. Generate all configuration files (OUT-01 through OUT-10) — see [references/output-templates.md](references/output-templates.md)
6. Generate Architecture Design report using report template (include rationale of major decisions/trade-offs)
7. Run DoD self-verification with `scripts/verify_dod.py` — see [references/dod.md](references/dod.md)
8. If any item fails → fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-architecture-design-supervisor` skill for inspection
2. If inspection returns failures → remediate item-by-item, re-trigger supervisor
3. Once 100% pass → notify PM Agent with:
   - Architecture Design report path
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

Save all diagram source files to `architecture-design/diagrams/` with descriptive names.

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
