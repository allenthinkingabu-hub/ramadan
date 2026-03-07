# SOP Process — sa-spike-poc-leadership

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `spike-poc/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `poc-code/`, `findings/`
4. Initialize conversation log file: `spike-poc/conversation-log.md`
5. Initialize work log file: `spike-poc/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why the spike or PoC is needed for this context
2. Formulate understanding of goals, uncertainty area, risks, and success criteria
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `spike-poc/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs:
   - Architecture Design artifacts (IA-REQ-001)
   - Technical Guidance outputs (IA-DEV-001)
   - Solution Architecture Document (SA-REQ-001)
   - Technology Blueprint (SA-REQ-004)
   - ARB Feedback (SA-REQ-005)
2. Gather additional context:
   - Specific uncertainty or risk to investigate
   - Competing technology options
   - Time-box and resource constraints
   - Performance/scalability targets
   - Acceptance criteria for PoC success
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `spike-poc/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry approaches to the uncertainty area
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `spike-poc/research/`
2. Generate comprehensive question list based on research
3. Save question list to `spike-poc/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated spike plan
7. Save to `spike-poc/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Define spike/PoC plan with hypothesis and methodology
2. Build minimal PoC code -> `poc-code/`
3. Execute experiments and benchmarks
4. Produce Spike/PoC Findings Report -> `spike-poc-report.md`
5. Produce Technology Comparison Matrix (if applicable) -> `findings/technology-comparison.md`
6. Produce Recommendation & Decision Record -> `findings/recommendation-decision.md`
7. Produce Risk Assessment Update -> `findings/risk-assessment.md`
8. Produce all configuration files per output templates
9. Run DoD self-verification
10. If any DoD item fails -> fix and re-verify until all pass
11. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Spike/PoC report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Technical Lead tasks:
   - TL-DEV-001: Code Review & Quality Gatekeeping
   - TL-DEV-002: Hands-On Development
   - TL-DEV-003: Technical Decision Making
   - TL-DEV-004: Unblocking the Team
   - TL-DEV-005: Technical Debt Governance
