# Integration Design Agent — SOP Process Checklist

## Standard Operating Procedure

### Phase 1: Understand Task Purpose
- [ ] 1.1 Review integration design task definition and scope
- [ ] 1.2 Identify why integration design is needed for this project
- [ ] 1.3 Clarify goals: what the integration design should achieve
- [ ] 1.4 Define scope boundaries: what is in-scope and out-of-scope
- [ ] 1.5 Present understanding to user for confirmation
- [ ] 1.6 Record questions and answers in conversation log
- [ ] **Gate**: User confirms understanding before proceeding

### Phase 2: Understand Topic (Project Context)
- [ ] 2.1 Read and analyze the high-level architecture design document
- [ ] 2.2 Read and analyze the technology stack decision document
- [ ] 2.3 Identify existing system landscape and integration points
- [ ] 2.4 Catalog third-party service dependencies
- [ ] 2.5 Review API standards and conventions in use
- [ ] 2.6 Identify data exchange formats required
- [ ] 2.7 Review messaging protocols in use or planned
- [ ] 2.8 Review security requirements for inter-system communication
- [ ] 2.9 Present understanding to user for confirmation
- [ ] 2.10 Record questions and answers in conversation log
- [ ] **Gate**: User confirms understanding before proceeding

### Phase 3: Research & Question List
- [ ] 3.1 Research industry best practices for integration design
- [ ] 3.2 Research API contract definition methodologies
- [ ] 3.3 Research data flow mapping patterns
- [ ] 3.4 Research third-party dependency management strategies
- [ ] 3.5 Save research process and results locally
- [ ] 3.6 Generate a comprehensive question list based on research
- [ ] 3.7 Engage in iterative dialogue with user on the question list
- [ ] 3.8 Produce a validated integration design requirements list
- [ ] 3.9 Record the question list for future review
- [ ] 3.10 Record questions and answers in conversation log
- [ ] **Gate**: User confirms validated requirements list before proceeding

### Phase 4: Execute & Output
- [ ] 4.1 Research relevant information based on validated requirements
- [ ] 4.2 Save research process and results locally
- [ ] 4.3 Generate trigger mechanism configuration file
- [ ] 4.4 Generate RACI matrix configuration file
- [ ] 4.5 Generate skills list configuration file
- [ ] 4.6 Generate knowledge base checklist
- [ ] 4.7 Generate tools checklist
- [ ] 4.8 Generate MCP tools checklist
- [ ] 4.9 Generate output content list and templates
- [ ] 4.10 Generate SOP process checklist
- [ ] 4.11 Generate DoD quality gates checklist
- [ ] 4.12 Generate DoR checklist
- [ ] 4.13 Create conversation log document
- [ ] 4.14 Create work log document
- [ ] 4.15 Run DoD verification — if any item fails, fix and re-verify
- [ ] 4.16 Save all outputs to `integration-design/` directory
- [ ] **Gate**: All DoD items pass

### Phase 5: Supervisor Review & Completion
- [ ] 5.1 Trigger SA-integration-design-supervisor for inspection
- [ ] 5.2 Receive inspection report
- [ ] 5.3 If any items fail, remediate and re-trigger supervisor
- [ ] 5.4 Repeat until 100% pass rate
- [ ] 5.5 Notify PM Agent with completion report, file paths, and RACI matrix
- [ ] **Gate**: Supervisor inspection passes at 100%

## Configuration Notes

- Add new steps by inserting into the relevant phase.
- Each phase gate must be passed before proceeding to the next phase.
