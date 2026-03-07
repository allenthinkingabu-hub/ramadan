# SOP Process -- sa-performance-load-testing

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist -- all prerequisites met before proceeding
2. Create output directory `performance-load-testing/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `scenarios/`
4. Initialize conversation log file: `performance-load-testing/conversation-log.md`
5. Initialize work log file: `performance-load-testing/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why performance and load testing is needed for this context
2. Formulate understanding of goals, scope, NFR targets, and test types required
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `performance-load-testing/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs:
   - Architecture design documents and NFR mapping
   - SLA/SLO targets (latency, throughput, availability)
   - Deployment topology and infrastructure specs
   - Expected workload profiles and user concurrency
   - Integration points and external dependency SLAs
2. Gather additional context:
   - Business-critical user journeys
   - Peak load expectations and seasonal patterns
   - Historical performance data (if available)
   - Technology stack performance characteristics
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `performance-load-testing/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research industry performance testing practices for this topic
   - Use Web Search, Context7, and other research tools
   - Save research process and results to `performance-load-testing/research/`
2. Generate comprehensive question list based on research
3. Save question list to `performance-load-testing/phase3-questions.md`
4. Engage in iterative dialogue with user using the question list
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `performance-load-testing/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Design test scenarios (load, stress, soak, spike, scalability)
3. Define benchmark thresholds (latency percentiles, throughput, concurrency, resource utilization)
4. Produce test execution plan with environment, tools, schedule
5. Produce acceptance criteria matrix with NFR-to-test mapping
6. Produce all configuration files per output templates
7. Produce Performance Load Testing report
8. Run DoD self-verification
9. If any DoD item fails -> fix and re-verify until all pass
10. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Performance Load Testing report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Technical Lead tasks:
   - TL-QA-001: Critical Bug Investigation
   - TL-QA-002: Performance & Scalability Review
   - TL-QA-003: Release Candidate Validation
   - TL-QA-004: Technical Go/No-Go Input
