# SOP Process — sa-technology-selection

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `technology-selection/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize conversation log file: `technology-selection/conversation-log.md`
5. Initialize work log file: `technology-selection/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why technology selection is needed for this context
2. Formulate understanding of goals, scope, evaluation objectives, and technology categories
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected → refine understanding and repeat
6. If confirmed → log confirmed understanding, proceed to Phase 2
7. Record questions asked in `technology-selection/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather information about:
   - Business context and strategic goals
   - Project requirements (functional and non-functional)
   - Existing technology stack and integration points
   - Infrastructure constraints (cloud, on-premise, hybrid)
   - Team capabilities and skill gaps
   - Budget boundaries and procurement constraints
2. Present structured understanding to user
3. Ask user for confirmation
4. If rejected → return to Phase 1 to deepen understanding
5. If confirmed → log confirmed topic understanding, proceed to Phase 3
6. Record questions asked in `technology-selection/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry technology selection practices for this topic
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `technology-selection/research/`
2. Generate comprehensive question list based on research
3. Save question list to `technology-selection/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `technology-selection/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Identify candidate technologies per category
3. Create weighted scoring matrix with evaluation criteria
4. Evaluate each candidate against criteria
5. Conduct TCO analysis for top candidates
6. Assess vendor viability and licensing models
7. Produce recommendation with rationale
8. Produce all configuration files per output templates
9. Produce Technology Selection report
10. Output all deliverables to `technology-selection/` directory
11. Run DoD self-verification
12. If any DoD item fails → fix and re-verify until all pass
13. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures → remediate and re-submit
3. Once Supervisor confirms 100% pass → notify PM Agent with:
   - Technology Selection report file path
   - RACI matrix configuration
   - Final inspection report
