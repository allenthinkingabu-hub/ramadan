# SOP Process — SA-technical-discovery

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `technical-discovery/` under parent directory
3. Initialize conversation log file: `technical-discovery/conversation-log.md`
4. Initialize work log file: `technical-discovery/work-log.md`
5. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why technical discovery is needed for this context
2. Formulate understanding of goals, scope, and assessment objectives
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected → refine understanding and repeat
6. If confirmed → log confirmed understanding, proceed to Phase 2
7. Record questions asked in `technical-discovery/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather information about:
   - Business context and domain
   - Existing technology stack
   - System architecture landscape
   - Infrastructure environment
   - Project constraints and limitations
2. Present structured understanding to user
3. Ask user for confirmation
4. If rejected → return to Phase 1 to deepen understanding
5. If confirmed → log confirmed topic understanding, proceed to Phase 3
6. Record questions asked in `technical-discovery/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry practices for technical discovery on this topic
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `technical-discovery/research/`
2. Generate comprehensive question list based on research
3. Save question list to `technical-discovery/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save validated requirements to `technical-discovery/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Produce all deliverables per output templates (see output-templates.md)
3. Save all outputs to `technical-discovery/` directory
4. Run DoD self-verification
5. If any DoD item fails → fix and re-verify until all pass
6. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures → remediate and re-submit
3. Once Supervisor confirms 100% pass → notify PM Agent with:
   - Technical Discovery report file path
   - RACI matrix configuration
   - Final inspection report
