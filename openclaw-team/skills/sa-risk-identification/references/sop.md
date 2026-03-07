# SOP Process -- sa-risk-identification

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist -- all prerequisites met before proceeding
2. Create output directory `risk-identification/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `diagrams/`
4. Initialize conversation log file: `risk-identification/conversation-log.md`
5. Initialize work log file: `risk-identification/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why risk identification is needed for this context
2. Formulate understanding of goals, scope, risk categories, and assessment objectives
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `risk-identification/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs from Wave 9 (Solutions Architect):
   - SA-REQ-001: Solution Architecture Document (SAD)
   - SA-REQ-002: Integration Architecture
   - SA-REQ-003: NFR Mapping
   - SA-REQ-004: Technology Blueprint
   - SA-REQ-005: ARB Feedback
2. Gather additional context:
   - System landscape and component inventory
   - External system dependencies and integrations
   - Technology maturity and team familiarity
   - Non-functional requirements and SLA targets
   - Known constraints (budget, timeline, regulatory)
   - Technical discovery findings (IA-INC-001 if available)
   - Feasibility analysis results (IA-INC-002 if available)
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `risk-identification/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry risk identification practices for this topic
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `risk-identification/research/`
2. Generate comprehensive question list based on research
3. Save question list to `risk-identification/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated risk areas list
7. Save to `risk-identification/validated-risk-areas.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated risk areas
2. Produce risk register with categorized risks, severity, and mitigations
3. Produce dependency map with system dependency graph
4. Produce integration challenge analysis
5. Produce mitigation strategy matrix
6. Produce all configuration files per output templates
7. Produce Risk Identification report
8. Run DoD self-verification
9. If any DoD item fails -> fix and re-verify until all pass
10. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Risk Identification report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Technical Lead tasks:
   - TL-INC-001: Technical Vision & Direction
   - TL-INC-002: Technology Stack Decision
   - TL-INC-003: Team Capability Assessment
   - TL-INC-004: Technical Risk Assessment
   - TL-INC-005: Estimation Leadership
