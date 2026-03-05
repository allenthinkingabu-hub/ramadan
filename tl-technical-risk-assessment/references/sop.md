# SOP Process — tl-technical-risk-assessment

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `technical-risk-assessment/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize conversation log file: `technical-risk-assessment/conversation-log.md`
5. Initialize work log file: `technical-risk-assessment/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why technical risk assessment is needed for this context
2. Formulate understanding of goals, scope, risk categories, and assessment objectives
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `technical-risk-assessment/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs from Wave 10 (IT Architect):
   - IA-INC-001 through IA-INC-008
2. Gather additional context:
   - System architecture and integration landscape
   - External system dependencies and SLAs
   - Third-party service dependencies
   - Technology stack maturity and known issues
   - Team experience with selected technologies
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `technical-risk-assessment/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research technical risk management practices
   - Use Web Search, Context7, and other research tools
   - Save research to `technical-risk-assessment/research/`
2. Generate comprehensive question list
3. Save question list to `technical-risk-assessment/phase3-questions.md`
4. Engage in iterative dialogue with user
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `technical-risk-assessment/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Produce Risk Register -> `risk-register.md`
3. Produce Dependency Map -> `dependency-map.md`
4. Produce Mitigation Strategy Plan -> `mitigation-plan.md`
5. Produce Risk Monitoring Framework -> `monitoring-framework.md`
6. Produce all configuration files per output templates
7. Produce Technical Risk Assessment report
8. Run DoD self-verification
9. If any DoD item fails -> fix and re-verify until all pass
10. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Technical Risk Assessment report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Software Engineer tasks:
   - SE-INC-001 through SE-INC-005
