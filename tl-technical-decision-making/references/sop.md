# SOP Process -- tl-technical-decision-making

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist -- all prerequisites met before proceeding
2. Create output directory `technical-decision-making/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `decisions/`
4. Initialize conversation log file: `technical-decision-making/conversation-log.md`
5. Initialize work log file: `technical-decision-making/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why technical decision support is needed
2. Formulate understanding of decision scope, constraints, urgency, impact
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `technical-decision-making/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs:
   - Architecture Design documents (IA-REQ-001)
   - Technology Blueprint
   - NFR requirements
   - Existing ADRs
2. Gather additional context:
   - Decision drivers and business context
   - Technical constraints and dependencies
   - Team capabilities
   - Timeline and budget constraints
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1
6. If confirmed -> log and proceed to Phase 3
7. Record questions asked in `technical-decision-making/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research alternatives, best practices, and industry patterns
   - Save research to `technical-decision-making/research/`
2. Generate comprehensive question list
3. Save to `technical-decision-making/phase3-questions.md`
4. Engage in iterative dialogue with user
5. Produce validated requirements list
6. Save to `technical-decision-making/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Evaluate alternatives using weighted criteria
2. Produce ADRs for each significant decision
3. Produce trade-off analysis document
4. Produce decision register
5. Produce all configuration files per output templates
6. Produce Technical Decision Making report
7. Run DoD self-verification
8. If any DoD item fails -> fix and re-verify until all pass
9. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Technical Decision Making report file path
   - RACI matrix configuration
   - Final inspection report
