# SOP Process -- sa-security-review

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist -- all prerequisites met before proceeding
2. Create output directory `security-review/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `assessments/`
4. Initialize conversation log file: `security-review/conversation-log.md`
5. Initialize work log file: `security-review/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why security review is needed for this context
2. Formulate understanding of goals, scope, and key objectives
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `security-review/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs:
   - Architecture Design outputs (IA-REQ-001)
   - Security architecture documentation
   - Compliance and regulatory requirements
   - Data classification and privacy policies
   - Third-party integration security profiles
2. Gather additional context from user and documentation
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `security-review/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry security review practices for this topic
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `security-review/research/`
2. Generate comprehensive question list based on research
3. Save question list to `security-review/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `security-review/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Produce deliverables:
   - Threat Model -> `assessments/threat-model.md`
   - Vulnerability Assessment -> `assessments/vulnerability-assessment.md`
   - Security Policy Compliance -> `security-policy-compliance.md`
   - Security Test Plan -> `security-test-plan.md`
3. Produce all configuration files per output templates
4. Produce Security Review report
5. Run DoD self-verification
6. If any DoD item fails -> fix and re-verify until all pass
7. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Security Review report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Technical Lead tasks:
   - TL-QA-001: Critical Bug Investigation
   - TL-QA-002: Performance & Scalability Review
   - TL-QA-003: Release Candidate Validation
   - TL-QA-004: Technical Go/No-Go Input
