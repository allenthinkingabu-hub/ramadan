# SOP Process — sa-technical-guidance

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `technical-guidance/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `patterns/`
4. Initialize conversation log file: `technical-guidance/conversation-log.md`
5. Initialize work log file: `technical-guidance/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why technical guidance is needed for this context
2. Formulate understanding of goals, scope, developer concerns, and architecture areas
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `technical-guidance/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs:
   - Architecture Design artifacts (IA-REQ-001)
   - Solution Architecture Document (SA-REQ-001)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Developer questions and pain points
   - Current implementation status and blockers
   - Design patterns already in use
   - Technology stack specifics and constraints
   - Non-functional requirements impacting implementation
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `technical-guidance/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry best practices for applicable patterns and guidance
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `technical-guidance/research/`
2. Generate comprehensive question list based on research
3. Save question list to `technical-guidance/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated guidance scope
7. Save to `technical-guidance/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Produce Technical Guidance Document with:
   - Per-component architectural guidance
   - Design pattern recommendations with rationale
   - Anti-patterns to avoid
3. Produce Pattern Catalog -> `patterns/pattern-catalog.md`
4. Produce Architecture-to-Code Mapping -> `architecture-code-mapping.md`
5. Produce Guidance Decision Log -> `guidance-decision-log.md`
6. Produce all configuration files per output templates
7. Produce Technical Guidance report
8. Run DoD self-verification
9. If any DoD item fails -> fix and re-verify until all pass
10. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Technical Guidance report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Technical Lead tasks:
   - TL-DEV-001: Code Review & Quality Gatekeeping
   - TL-DEV-002: Hands-On Development
   - TL-DEV-003: Technical Decision Making
   - TL-DEV-004: Unblocking the Team
   - TL-DEV-005: Technical Debt Governance
