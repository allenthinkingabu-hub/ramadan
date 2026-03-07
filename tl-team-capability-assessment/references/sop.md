# SOP Process — tl-team-capability-assessment

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `team-capability-assessment/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize conversation log file: `team-capability-assessment/conversation-log.md`
5. Initialize work log file: `team-capability-assessment/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why team capability assessment is needed for this context
2. Formulate understanding of goals, scope, team size, and assessment objectives
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `team-capability-assessment/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs from Wave 10 (IT Architect):
   - IA-INC-001 through IA-INC-008
2. Gather additional context:
   - Current team composition and roles
   - Individual skill profiles (if available)
   - Technology stack decisions (from TL-INC-002 if available)
   - Project complexity and domain requirements
   - Timeline constraints affecting ramp-up
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `team-capability-assessment/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research team assessment methodologies and capability frameworks
   - Use Web Search, Context7, and other research tools
   - Save research to `team-capability-assessment/research/`
2. Generate comprehensive question list based on research
3. Save question list to `team-capability-assessment/phase3-questions.md`
4. Engage in iterative dialogue with user
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `team-capability-assessment/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Produce Team Skills Matrix -> `skills-matrix.md`
3. Produce Gap Analysis -> `gap-analysis.md`
4. Produce Development & Remediation Plan -> `development-plan.md`
5. Produce Team Readiness Assessment -> `readiness-assessment.md`
6. Produce all configuration files per output templates
7. Produce Team Capability Assessment report
8. Run DoD self-verification
9. If any DoD item fails -> fix and re-verify until all pass
10. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Team Capability Assessment report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Software Engineer tasks:
   - SE-INC-001 through SE-INC-005
