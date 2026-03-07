# SOP Process -- sa-data-privacy-governance

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist -- all prerequisites met before proceeding
2. Create output directory `data-privacy-governance/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize conversation log file: `data-privacy-governance/conversation-log.md`
5. Initialize work log file: `data-privacy-governance/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why data privacy and governance is needed for this context
2. Formulate understanding of goals, scope, regulatory requirements, data domains, compliance obligations
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `data-privacy-governance/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SA-REQ-001: Solution Architecture Document (SAD)
   - SA-REQ-002: Integration Architecture
   - SA-REQ-003: NFR Mapping
   - SA-REQ-004: Technology Blueprint
   - SA-REQ-005: ARB Feedback
2. Gather additional context:
   - Applicable regulations (GDPR, CCPA, HIPAA, SOX, PCI-DSS, etc.)
   - Technical discovery findings (IA-INC-001 if available)
   - Feasibility analysis results (IA-INC-002 if available)
   - Data domains, data types, and sensitivity levels
   - Geographic deployment regions and data residency requirements
   - Existing privacy policies or governance frameworks
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `data-privacy-governance/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry data privacy and governance practices
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `data-privacy-governance/research/`
2. Generate comprehensive question list based on research
3. Save question list to `data-privacy-governance/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `data-privacy-governance/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Define data privacy and governance framework:
   - Data classification taxonomy -> `diagrams/classification-taxonomy.md`
   - Access control model -> `diagrams/access-control-model.md`
   - Data retention policy -> included in report
   - Data residency requirements -> included in report
   - Consent management -> included in report
3. Produce Regulatory Compliance View -> `diagrams/regulatory-compliance-view.md`
   - Regulation mapping, PIA template, DPA requirements, breach procedures
4. Produce NFR Alignment Note -> `nfr-alignment.md`
   - Map governance decisions to NFRs, document constraints and assumptions
5. Produce all configuration files per output templates
6. Produce Data Privacy & Governance report with rationale of major decisions/trade-offs
7. Run DoD self-verification
8. If any DoD item fails -> fix and re-verify until all pass
9. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Data Privacy & Governance report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Technical Lead tasks:
   - TL-REQ-001: Technical Design & Solution Design
   - TL-REQ-002: Coding Standards & Conventions
   - TL-REQ-003: Task Decomposition & Assignment
   - TL-REQ-004: Build & Toolchain Setup
   - TL-REQ-005: Cross-Team Technical Alignment
