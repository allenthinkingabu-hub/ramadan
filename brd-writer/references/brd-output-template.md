# BRD Output Template

Use this template as the strict structure for all BRD documents produced by the agent. Every section must be populated with meaningful content. Do not leave any section empty or with placeholder text in the final output.

---

```markdown
# Business Requirements Document (BRD)

## Document Control

| Field | Value |
|-------|-------|
| Document Title | {project_name} — Business Requirements Document |
| Version | {version_number} |
| Date | {date} |
| Author | BRD Writer AI Agent |
| Status | Draft / In Review / Approved |
| Reviewer(s) | {reviewer_names} |

### Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1 | {date} | BRD Writer AI Agent | Initial draft |

---

## 1. Executive Summary

{One-paragraph overview of the project purpose, key objectives, and expected outcomes. Write this section LAST after all other sections are complete.}

---

## 2. Business Objectives

{List business objectives in SMART format: Specific, Measurable, Achievable, Relevant, Time-bound.}

| ID | Objective | Success Metric | Target | Timeline |
|----|-----------|---------------|--------|----------|
| BO-01 | {objective} | {metric} | {target_value} | {deadline} |

---

## 3. Project Background & Context

### 3.1 Business Problem / Opportunity
{Describe the current business situation, pain points, market drivers, and the reason for this initiative.}

### 3.2 Current State (As-Is)
{Describe existing business processes, systems, and their limitations.}

### 3.3 Future State (To-Be)
{Describe the desired business processes, capabilities, and outcomes.}

---

## 4. Project Scope

### 4.1 In Scope
{Bulleted list of items explicitly included in this project.}

### 4.2 Out of Scope
{Bulleted list of items explicitly excluded from this project.}

---

## 5. Stakeholders

| ID | Name / Role | Department | Interest Level | Influence Level | RACI |
|----|------------|------------|---------------|-----------------|------|
| SH-01 | {name/role} | {dept} | High/Medium/Low | High/Medium/Low | R/A/C/I |

---

## 6. Business Requirements

| ID | Requirement | Priority | Source | Acceptance Criteria |
|----|-------------|----------|--------|-------------------|
| BR-01 | {requirement_description} | Must / Should / Could / Won't | {stakeholder/source} | {testable_criteria} |

---

## 7. Functional Requirements

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-01 | {functional_requirement} | Must / Should / Could / Won't | BR-{XX} | {testable_criteria} |

---

## 8. Non-Functional Requirements

| ID | Category | Requirement | Priority | Acceptance Criteria |
|----|----------|-------------|----------|-------------------|
| NFR-01 | Performance / Security / Scalability / Usability / Availability / Compliance | {requirement} | Must / Should / Could | {measurable_criteria} |

---

## 9. Data Requirements

### 9.1 Data Entities
{Key data entities, their attributes, and relationships.}

### 9.2 Data Flows
{How data moves between systems and processes.}

### 9.3 Data Migration (if applicable)
{Data migration needs, source-target mapping, and cleansing requirements.}

---

## 10. Assumptions

| ID | Assumption | Impact if Invalid |
|----|-----------|-------------------|
| AS-01 | {assumption} | {impact} |

---

## 11. Constraints

| ID | Type | Constraint | Impact |
|----|------|-----------|--------|
| CN-01 | Budget / Time / Technology / Regulatory / Resource | {constraint} | {impact} |

---

## 12. Dependencies

| ID | Dependency | Type | Owner | Status |
|----|-----------|------|-------|--------|
| DP-01 | {dependency_description} | Internal / External | {owner} | Open / Resolved |

---

## 13. Risks & Mitigation

| ID | Risk | Probability | Impact | Mitigation Strategy | Owner |
|----|------|------------|--------|---------------------|-------|
| RK-01 | {risk_description} | High/Medium/Low | High/Medium/Low | {mitigation} | {owner} |

---

## 14. Success Metrics & KPIs

| ID | KPI | Baseline | Target | Measurement Method | Frequency |
|----|-----|---------|--------|-------------------|-----------|
| KPI-01 | {kpi_name} | {current_value} | {target_value} | {how_measured} | {how_often} |

---

## 15. Cost-Benefit Analysis

### 15.1 Estimated Costs
{Breakdown of project costs: development, infrastructure, operations, etc.}

### 15.2 Expected Benefits
{Quantified benefits: revenue increase, cost reduction, efficiency gains, etc.}

### 15.3 ROI Projection
{Return on investment calculation and timeline to break-even.}

---

## 16. Implementation Timeline

| Milestone | Target Date | Dependencies | Owner |
|-----------|------------|-------------|-------|
| {milestone_name} | {date} | {dependencies} | {owner} |

---

## 17. Glossary

| Term | Definition |
|------|-----------|
| {term} | {definition} |

---

## 18. Appendices

### Appendix A: Process Flow Diagrams
{Include as-is and to-be process flow diagrams.}

### Appendix B: Requirements Traceability Matrix
{Map each requirement to its source, related requirements, and test cases.}

| Requirement ID | Source | Related Requirements | Test Case |
|---------------|--------|---------------------|-----------|
| BR-01 | {source} | FR-01, FR-02 | TC-01 |

### Appendix C: Supporting Documents
{List and link any supporting documents referenced in this BRD.}

---

## 19. Approval Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor | {name} | _________ | {date} |
| Project Manager | {name} | _________ | {date} |
| Business Analyst | BRD Writer AI Agent | _________ | {date} |
```
