---
name: sa-data-architecture
description: "Interactive AI Agent skill for designing data models, storage strategies, and data migration plans through structured iterative dialogue. Use when: (1) data architecture design or data modelling is needed, (2) designing storage strategies (relational, NoSQL, data lake, warehouse), (3) planning data migration or ETL/ELT pipelines, (4) PM Agent assigns task IA-REQ-004 via RACI matrix, (5) translating Solutions Architect outputs (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB feedback) into definitive data architecture designs, (6) defining logical/physical data models, or (7) producing data lineage and data flow diagrams."
---

# SA Data Architecture Agent

Role: IT Architect (SA) | Task ID: IA-REQ-004 | Wave: 10, Step: 4

## Objective

Produce the definitive data architecture -- logical and physical data models, storage strategies, data flow designs, and data migration plans -- covering entity relationships, storage technology selection, partitioning/sharding strategies, data lineage, and ETL/ELT pipeline design.

## Upstream Inputs (Wave 9 -- Solutions Architect)

- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-002: Integration Architecture
- SA-REQ-003: Non-Functional Requirements Mapping
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: Architecture Review Board (ARB) Feedback

## Downstream Triggers (Wave 11 -- Technical Lead)

Upon completion, PM Agent triggers: TL-REQ-001 (Technical Design), TL-REQ-002 (Coding Standards), TL-REQ-003 (Task Decomposition), TL-REQ-004 (Build & Toolchain), TL-REQ-005 (Cross-Team Alignment).

## Workflow Overview

Create data architecture designs through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why data architecture is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream SA-REQ outputs, business data requirements, NFRs, integration constraints -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Design data models -> produce diagrams, storage strategy, migration plan, data flow views -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-REQ-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `data-architecture/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize `data-architecture/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `data-architecture/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why data architecture is needed for this context
2. Formulate understanding of: goals, scope, data domains, storage requirements, migration needs
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `data-architecture/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SAD -- Solution Architecture Document (SA-REQ-001)
   - Integration Architecture (SA-REQ-002)
   - NFR Mapping (SA-REQ-003)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Business data requirements and domain entities
   - Technical discovery findings (from IA-INC-001 if available)
   - Feasibility analysis results (from IA-INC-002 if available)
   - Selected technology stack (databases, data platforms)
   - Non-functional requirements (throughput, latency, data volume, retention)
   - Data integration constraints and existing data sources
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `data-architecture/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry data architecture practices for this topic
   - Save all research to `data-architecture/research/`
2. Generate comprehensive question list -> save to `data-architecture/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `data-architecture/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Design data architecture and produce deliverables:
   - **Logical Data Model**: Entity-relationship diagrams, domain model (using Mermaid/PlantUML)
   - **Physical Data Model**: Table definitions, indexes, partitioning, sharding strategies
   - **Storage Strategy**: Technology selection (RDBMS, NoSQL, data lake, warehouse, cache), justification per data domain
   - **Data Flow Diagrams**: ETL/ELT pipelines, data lineage, transformation flows
   - **Data Migration Plan**: Source-target mapping, migration sequence, rollback strategy, validation checkpoints
     - Document data volume estimates, throughput targets, and migration window constraints
3. Produce **Data Integration View**:
   - Data exchange protocols and patterns (CDC, batch, streaming, API)
   - Schema contracts and data format standards (Avro, Parquet, JSON Schema)
   - Data quality rules, validation gates, and reconciliation checks
   - Data masking and anonymization rules for sensitive data
   - Save to `data-architecture/diagrams/data-integration-view.md`
4. Produce **NFR Alignment Note**:
   - Map data architecture decisions to NFRs (performance, availability, scalability, consistency)
   - Include data SLO/SLI targets (query latency, throughput, freshness, completeness)
   - Document constraints and assumptions
   - Save to `data-architecture/nfr-alignment.md`
5. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
6. Generate Data Architecture report using report template (include rationale of major decisions/trade-offs)
7. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
8. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-data-architecture-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Data Architecture report path
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
- **PlantUML**: For complex UML and ER diagrams
- **ASCII art**: For simple inline diagrams in markdown

Save all diagram source files to `data-architecture/diagrams/` with descriptive names.

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
