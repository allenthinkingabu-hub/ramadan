# SOP Process -- tl-code-review-quality-gatekeeping

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist -- all prerequisites met before proceeding
2. Create output directory `code-review-quality-gatekeeping/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `reviews/`
4. Initialize conversation log file: `code-review-quality-gatekeeping/conversation-log.md`
5. Initialize work log file: `code-review-quality-gatekeeping/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why code review and quality gatekeeping is needed for this context
2. Formulate understanding of goals, scope, quality objectives, review types
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `code-review-quality-gatekeeping/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs:
   - Architecture Design documents (IA-REQ-001)
   - Existing coding standards and conventions
   - Technical design specifications
   - Current codebase structure and patterns
2. Gather additional context:
   - Team structure and experience levels
   - Current review processes and tooling
   - Quality metrics and baselines
   - CI/CD pipeline configuration
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `code-review-quality-gatekeeping/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry code review practices and quality gate patterns
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `code-review-quality-gatekeeping/research/`
2. Generate comprehensive question list based on research
3. Save question list to `code-review-quality-gatekeeping/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `code-review-quality-gatekeeping/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Produce review standards and quality gate definitions
3. Produce review process documentation
4. Produce automated check configurations
5. Produce all configuration files per output templates
6. Produce Code Review Quality Gatekeeping report
7. Run DoD self-verification
8. If any DoD item fails -> fix and re-verify until all pass
9. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Code Review Quality Gatekeeping report file path
   - RACI matrix configuration
   - Final inspection report
