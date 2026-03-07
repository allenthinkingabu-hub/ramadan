# SOP Process — SA-feasibility-analysis

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `feasibility-analysis/` under parent directory
3. Initialize conversation log file: `feasibility-analysis/conversation-log.md`
4. Initialize work log file: `feasibility-analysis/work-log.md`
5. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why feasibility analysis is needed for this context
2. Formulate understanding of goals, scope, and assessment objectives
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected → refine understanding and repeat
6. If confirmed → log confirmed understanding, proceed to Phase 2
7. Record questions asked in `feasibility-analysis/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather information about:
   - Business context and domain
   - Client's requirements to be assessed
   - Technical landscape and existing systems
   - Project constraints and limitations
2. Present structured understanding to user
3. Ask user for confirmation
4. If rejected → return to Phase 1 to deepen understanding
5. If confirmed → log confirmed topic understanding, proceed to Phase 3
6. Record questions asked in `feasibility-analysis/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry practices for feasibility analysis on this topic
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `feasibility-analysis/research/`
2. Generate comprehensive question list based on research
3. Save question list to `feasibility-analysis/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save validated requirements to `feasibility-analysis/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Assess feasibility across all dimensions:
   - Technical feasibility
   - Operational feasibility
   - Economic feasibility
   - Schedule feasibility
   - Legal & compliance feasibility
3. Produce all deliverables per output templates (see output-templates.md)
4. Save all outputs to `feasibility-analysis/` directory
5. Run DoD self-verification
6. If any DoD item fails → fix and re-verify until all pass
7. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures → remediate and re-submit
3. Once Supervisor confirms 100% pass → notify PM Agent with:
   - Feasibility Analysis report file path
   - RACI matrix configuration
   - Final inspection report
