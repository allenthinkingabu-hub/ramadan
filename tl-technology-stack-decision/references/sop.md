# SOP Process — tl-technology-stack-decision

## Standard Operating Procedure

### Phase 0: Initialization
1. Verify DoR checklist — all prerequisites met before proceeding
2. Create output directory `technology-stack-decision/` under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`
4. Initialize conversation log file: `technology-stack-decision/conversation-log.md`
5. Initialize work log file: `technology-stack-decision/work-log.md`
6. Log activation timestamp in work log

### Phase 1: Understand Task Purpose (Step 1)
1. Analyze why technology stack decisions are needed for this context
2. Formulate understanding of goals, scope, decision categories, and constraints
3. Present understanding to user in structured format
4. Ask user for confirmation
5. If rejected -> refine understanding and repeat
6. If confirmed -> log confirmed understanding, proceed to Phase 2
7. Record questions asked in `technology-stack-decision/phase1-questions.md`

### Phase 2: Understand the Topic (Step 2)
1. Gather upstream inputs from Wave 10 (IT Architect):
   - IA-INC-001 through IA-INC-008
2. Gather additional context:
   - Current technology landscape and existing stack
   - Team skills and experience with candidate technologies
   - Licensing, cost, and vendor considerations
   - Performance and scalability requirements
   - Security and compliance constraints
3. Present structured understanding to user
4. Ask user for confirmation
5. If rejected -> return to Phase 1 to deepen understanding
6. If confirmed -> log confirmed topic understanding, proceed to Phase 3
7. Record questions asked in `technology-stack-decision/phase2-questions.md`

### Phase 3: Research & Question Generation (Step 3)
1. Research technology options and industry best practices
   - Use Web Search, Context7, and other research tools
   - Save research to `technology-stack-decision/research/`
2. Generate comprehensive question list based on research
3. Save question list to `technology-stack-decision/phase3-questions.md`
4. Engage in iterative dialogue with user
5. Collect and validate answers
6. Produce validated requirements list
7. Save to `technology-stack-decision/validated-requirements.md`

### Phase 4: Execute & Produce Deliverables (Step 4)
1. Research further based on validated requirements
2. Produce Technology Decision Matrix -> `technology-decision-matrix.md`
3. Produce Stack Specification -> `stack-specification.md`
4. Produce Compatibility & Integration Analysis -> `compatibility-analysis.md`
5. Produce Migration & Adoption Plan -> `adoption-plan.md`
6. Produce all configuration files per output templates
7. Produce Technology Stack Decision report
8. Run DoD self-verification
9. If any DoD item fails -> fix and re-verify until all pass
10. Log final status in work log

### Phase 5: Completion & Handoff
1. Trigger Supervisor Agent for quality inspection
2. If Supervisor returns failures -> remediate and re-submit
3. Once Supervisor confirms 100% pass -> notify PM Agent with:
   - Technology Stack Decision report file path
   - RACI matrix configuration
   - Final inspection report
4. PM Agent triggers downstream Software Engineer tasks:
   - SE-INC-001 through SE-INC-005
