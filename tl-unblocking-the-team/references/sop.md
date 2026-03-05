# SOP Process -- tl-unblocking-the-team

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist -- all prerequisites met before proceeding
2. Create output directory `unblocking-the-team/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `resolutions/`
4. Initialize conversation log and work log files
5. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why unblocking support is needed
2. Formulate understanding of blocker types, severity, affected teams, urgency
3. Present understanding to user, ask for confirmation
4. If rejected -> refine and repeat
5. If confirmed -> log and proceed to Phase 2
6. Record questions in `unblocking-the-team/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs and current context
2. Gather blocker details: symptoms, affected members, duration, previous attempts
3. Present structured understanding to user
4. If rejected -> return to Phase 1
5. If confirmed -> log and proceed to Phase 3
6. Record questions in `unblocking-the-team/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research solutions for identified blockers
   - Save research to `unblocking-the-team/research/`
2. Generate question list, save to `unblocking-the-team/phase3-questions.md`
3. Engage in iterative dialogue
4. Produce validated requirements list
5. Save to `unblocking-the-team/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Investigate and resolve blockers
2. Document root causes and solutions
3. Produce escalation framework
4. Produce all configuration files per output templates
5. Produce Unblocking the Team report
6. Run DoD self-verification
7. If any DoD item fails -> fix and re-verify until all pass
8. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent
