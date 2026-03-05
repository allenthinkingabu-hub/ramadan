# SOP Process — sa-code-design-reviews

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `code-design-reviews/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `reviews/`
4. Initialize conversation log file: `code-design-reviews/conversation-log.md`
5. Initialize work log file: `code-design-reviews/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why code/design review is needed for this context
2. Formulate understanding of goals, scope, review type, and compliance areas
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `code-design-reviews/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs:
   - Architecture Design artifacts (IA-REQ-001)
   - Technical Guidance outputs (IA-DEV-001)
   - Solution Architecture Document (SA-REQ-001)
   - Technology Blueprint (SA-REQ-004)
   - Coding Standards (TL-REQ-002 if available)
2. Gather additional context:
   - Code or PR to be reviewed
   - Component design documents
   - Known architectural constraints and NFRs
   - Previous review findings
   - Integration contracts and interface specifications
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `code-design-reviews/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry code review best practices
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `code-design-reviews/research/`
2. Generate comprehensive question list based on research
3. Save question list to `code-design-reviews/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated review scope
7. Save to `code-design-reviews/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Conduct architectural review of code/PR/design
2. Produce Review Findings Report -> `code-design-review-report.md`
3. Produce Compliance Matrix -> `compliance-matrix.md`
4. Produce Remediation Plan -> `remediation-plan.md`
5. Produce Review Decision Log -> `review-decision-log.md`
6. Produce all configuration files per output templates
7. Run DoD self-verification
8. If any DoD item fails -> fix and re-verify until all pass
9. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Code & Design Review report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Technical Lead tasks:
   - TL-DEV-001: Code Review & Quality Gatekeeping
   - TL-DEV-002: Hands-On Development
   - TL-DEV-003: Technical Decision Making
   - TL-DEV-004: Unblocking the Team
   - TL-DEV-005: Technical Debt Governance
