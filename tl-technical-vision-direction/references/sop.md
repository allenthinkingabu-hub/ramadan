# SOP Process — tl-technical-vision-direction

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `technical-vision-direction/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize conversation log file: `technical-vision-direction/conversation-log.md`
5. Initialize work log file: `technical-vision-direction/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why a technical vision is needed for this context
2. Formulate understanding of goals, scope, stakeholder expectations, and vision objectives
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `technical-vision-direction/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs from Wave 10 (IT Architect):
   - IA-INC-001: Technical Discovery Report
   - IA-INC-002: Feasibility Analysis
   - IA-INC-003: Proof of Concept Results
   - IA-INC-004: Non-Functional Requirements Analysis
   - IA-INC-005: Technology Landscape Assessment
   - IA-INC-006: Risk Assessment
   - IA-INC-007: Integration Strategy
   - IA-INC-008: Architecture Patterns Evaluation
2. Gather additional context:
   - Business objectives and strategic priorities
   - Organizational technology standards and constraints
   - Team capabilities and growth trajectory
   - Budget and timeline constraints
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `technical-vision-direction/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry technical vision practices for this domain
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `technical-vision-direction/research/`
2. Generate comprehensive question list based on research
3. Save question list to `technical-vision-direction/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `technical-vision-direction/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Produce Technical Vision Statement -> `technical-vision-statement.md`
3. Produce Guiding Principles -> `guiding-principles.md`
4. Produce Business-Technology Alignment Matrix -> `alignment-matrix.md`
5. Produce Technology Roadmap Overview -> `technology-roadmap.md`
6. Produce all configuration files per output templates
7. Produce Technical Vision Direction report
8. Run DoD self-verification
9. If any DoD item fails -> fix and re-verify until all pass
10. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Technical Vision Direction report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Software Engineer tasks:
   - SE-INC-001 through SE-INC-005
