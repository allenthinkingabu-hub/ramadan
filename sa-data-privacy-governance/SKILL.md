---
name: sa-data-privacy-governance
description: "Interactive AI Agent skill for defining data classification, retention, residency, and access-control models across domains through structured iterative dialogue. Use when: (1) data privacy or data governance design is needed, (2) defining data classification schemes and sensitivity levels, (3) establishing data retention and residency policies, (4) PM Agent assigns task IA-REQ-006 via RACI matrix, (5) translating Solutions Architect outputs (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB feedback) into definitive data privacy and governance frameworks, (6) designing role-based and attribute-based access control models, or (7) producing regulatory compliance mapping for GDPR, CCPA, HIPAA, and other data protection regulations."
---

# SA Data Privacy & Governance Agent

Role: IT Architect (SA) | Task ID: IA-REQ-006 | Wave: 10, Step: 6

## Objective

Produce the definitive data privacy and governance framework -- data classification taxonomy, retention policies, residency requirements, access-control models, and regulatory compliance mapping -- covering sensitivity levels, consent management, data subject rights, cross-border transfer rules, and audit trail requirements.

## Upstream Inputs (Wave 9 -- Solutions Architect)

- SA-REQ-001: Solution Architecture Document (SAD)
- SA-REQ-002: Integration Architecture
- SA-REQ-003: Non-Functional Requirements Mapping
- SA-REQ-004: Technology Blueprint
- SA-REQ-005: Architecture Review Board (ARB) Feedback

## Downstream Triggers (Wave 11 -- Technical Lead)

Upon completion, PM Agent triggers: TL-REQ-001 (Technical Design), TL-REQ-002 (Coding Standards), TL-REQ-003 (Task Decomposition), TL-REQ-004 (Build & Toolchain), TL-REQ-005 (Cross-Team Alignment).

## Workflow Overview

Create data privacy and governance designs through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why data privacy governance is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand upstream SA-REQ outputs, regulatory landscape, data domains -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Define classification, retention, residency, access control -> produce frameworks -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-REQ-001..005
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `data-privacy-governance/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize `data-privacy-governance/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `data-privacy-governance/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why data privacy and governance is needed for this context
2. Formulate understanding of: goals, scope, regulatory requirements, data domains, compliance obligations
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `data-privacy-governance/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SAD -- Solution Architecture Document (SA-REQ-001)
   - Integration Architecture (SA-REQ-002)
   - NFR Mapping (SA-REQ-003)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Applicable regulations (GDPR, CCPA, HIPAA, SOX, PCI-DSS, etc.)
   - Technical discovery findings (from IA-INC-001 if available)
   - Feasibility analysis results (from IA-INC-002 if available)
   - Data domains, data types, and sensitivity levels
   - Geographic deployment regions and data residency requirements
   - Existing privacy policies or governance frameworks
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `data-privacy-governance/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry data privacy and governance practices
   - Save all research to `data-privacy-governance/research/`
2. Generate comprehensive question list -> save to `data-privacy-governance/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `data-privacy-governance/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Define data privacy and governance framework:
   - **Data Classification Taxonomy**: Sensitivity levels (public, internal, confidential, restricted), classification criteria
   - **Data Retention Policy**: Retention periods per data category, deletion/archival procedures, legal hold process
   - **Data Residency Requirements**: Geographic constraints, cross-border transfer rules, sovereignty compliance
   - **Access Control Model**: RBAC/ABAC design, least privilege, segregation of duties, access review cadence
   - **Consent Management**: Consent collection, storage, withdrawal, preference center design
     - Document data subject rights workflows (access, rectification, erasure, portability)
3. Produce **Regulatory Compliance View**:
   - Regulation-to-control mapping (GDPR articles, CCPA sections, HIPAA rules)
   - Privacy Impact Assessment (PIA) template and triggers
   - Data Processing Agreement (DPA) requirements
   - Breach notification procedures and timelines
   - Save to `data-privacy-governance/diagrams/regulatory-compliance-view.md`
4. Produce **NFR Alignment Note**:
   - Map privacy/governance decisions to NFRs (security, compliance, auditability)
   - Include privacy SLO/SLI targets (consent response time, DSAR response time, encryption coverage)
   - Document constraints and assumptions
   - Save to `data-privacy-governance/nfr-alignment.md`
5. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
6. Generate Data Privacy & Governance report using report template (include rationale of major decisions/trade-offs)
7. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
8. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-data-privacy-governance-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Data Privacy & Governance report path
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

Save all diagram source files to `data-privacy-governance/diagrams/` with descriptive names.

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
