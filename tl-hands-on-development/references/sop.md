# SOP Process -- tl-hands-on-development

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist -- all prerequisites met before proceeding
2. Create output directory `hands-on-development/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `implementations/`
4. Initialize conversation log file: `hands-on-development/conversation-log.md`
5. Initialize work log file: `hands-on-development/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why TL hands-on development is needed for this context
2. Formulate understanding of goals, scope, critical paths, pattern requirements
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `hands-on-development/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs:
   - Architecture Design documents (IA-REQ-001)
   - Technical design specifications
   - Coding standards and conventions
   - Existing codebase patterns
2. Gather additional context:
   - Feature requirements and acceptance criteria
   - Technology stack constraints
   - Team skill gaps
   - Performance requirements
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `hands-on-development/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research implementation patterns and best practices
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `hands-on-development/research/`
2. Generate comprehensive question list based on research
3. Save question list to `hands-on-development/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `hands-on-development/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Implement reference patterns and critical path code
3. Write comprehensive tests
4. Document implementation patterns
5. Produce all configuration files per output templates
6. Produce Hands-On Development report
7. Run DoD self-verification
8. If any DoD item fails -> fix and re-verify until all pass
9. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Hands-On Development report file path
   - RACI matrix configuration
   - Final inspection report
