# SOP Process — sa-architecture-design

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `architecture-design/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize conversation log file: `architecture-design/conversation-log.md`
5. Initialize work log file: `architecture-design/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why architecture design is needed for this context
2. Formulate understanding of goals, scope, diagram types, and design objectives
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected → refine understanding and repeat
6. If confirmed → log confirmed understanding, proceed to Phase 2
7. Record questions asked in `architecture-design/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SA-REQ-001: Solution Architecture Document (SAD)
   - SA-REQ-002: Integration Architecture
   - SA-REQ-003: NFR Mapping
   - SA-REQ-004: Technology Blueprint
   - SA-REQ-005: ARB Feedback
2. Gather additional context:
   - Business requirements
   - Technical discovery findings (IA-INC-001 if available)
   - Feasibility analysis results (IA-INC-002 if available)
   - Selected technology stack
   - Non-functional requirements (performance, scalability, security, availability)
   - System integration constraints and interface contracts
2. Present structured understanding to user
3. Ask user for confirmation
4. If rejected → return to Phase 1 to deepen understanding
5. If confirmed → log confirmed topic understanding, proceed to Phase 3
6. Record questions asked in `architecture-design/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry architecture design practices for this topic
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `architecture-design/research/`
2. Generate comprehensive question list based on research
3. Save question list to `architecture-design/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `architecture-design/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Design architecture and produce diagrams:
   - C4 Context diagram → `diagrams/c4-context.md`
   - C4 Container diagram → `diagrams/c4-container.md`
   - C4 Component diagrams → `diagrams/c4-component-{name}.md`
   - UML Sequence diagrams → `diagrams/uml-sequence-{name}.md`
   - UML Class diagrams → `diagrams/uml-class-{name}.md`
   - Deployment architecture → `diagrams/deployment.md`
   - Data flow diagrams → `diagrams/data-flow-{name}.md`
3. Produce Interface/Integration View → `diagrams/integration-view.md`
   - Protocols, interface contracts, error handling, resilience patterns
4. Produce NFR Alignment Note → `nfr-alignment.md`
   - Map architecture decisions to NFRs, document constraints and assumptions
5. Produce all configuration files per output templates
6. Produce Architecture Design report with rationale of major decisions/trade-offs
7. Run DoD self-verification
8. If any DoD item fails → fix and re-verify until all pass
9. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures → remediate and re-submit
3. Once Supervisor confirms 100% pass → notify PM Agent with:
   - Architecture Design report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Technical Lead tasks:
   - TL-REQ-001: Technical Design & Solution Design
   - TL-REQ-002: Coding Standards & Conventions
   - TL-REQ-003: Task Decomposition & Assignment
   - TL-REQ-004: Build & Toolchain Setup
   - TL-REQ-005: Cross-Team Technical Alignment
