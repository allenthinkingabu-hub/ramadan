# SOP Process — sa-non-functional-requirements

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `non-functional-requirements/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize conversation log file: `non-functional-requirements/conversation-log.md`
5. Initialize work log file: `non-functional-requirements/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why non-functional requirements definition is needed for this context
2. Formulate understanding of goals, scope, NFR categories, and quality attribute priorities
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected → refine understanding and repeat
6. If confirmed → log confirmed understanding, proceed to Phase 2
7. Record questions asked in `non-functional-requirements/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather information about:
   - Business context and objectives
   - Architecture design (IA-REQ-001 if available)
   - Expected user load and traffic patterns
   - Deployment environment (cloud, on-prem, hybrid)
   - Compliance obligations (regulatory, industry standards)
   - Service-level expectations from stakeholders
2. Present structured understanding to user
3. Ask user for confirmation
4. If rejected → return to Phase 1 to deepen understanding
5. If confirmed → log confirmed topic understanding, proceed to Phase 3
6. Record questions asked in `non-functional-requirements/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry NFR practices and benchmarks for this topic
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `non-functional-requirements/research/`
2. Generate comprehensive question list based on research
3. Save question list to `non-functional-requirements/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `non-functional-requirements/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Define NFR categories and subcategories:
   - Performance: response time targets, throughput limits, latency budgets
   - Scalability: horizontal/vertical scaling, auto-scaling thresholds, capacity
   - Security: authentication, authorization, encryption, compliance, vulnerability mgmt
   - Availability: uptime SLA, failover, disaster recovery RTO/RPO
   - Maintainability: code quality, documentation, deployment frequency
   - Observability: logging, monitoring, alerting, distributed tracing
3. For each category: define measurable targets, acceptance criteria, and test methods
4. Create SLA/SLO/SLI specifications
5. Map NFRs to architecture components
6. Identify NFR risks and mitigations
7. Produce NFR specification document → `non-functional-requirements/nfr-report.md`
8. Produce all configuration files per output templates
9. Run DoD self-verification
10. If any DoD item fails → fix and re-verify until all pass
11. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures → remediate and re-submit
3. Once Supervisor confirms 100% pass → notify PM Agent with:
   - NFR specification report file path
   - RACI matrix configuration
   - Final inspection report
