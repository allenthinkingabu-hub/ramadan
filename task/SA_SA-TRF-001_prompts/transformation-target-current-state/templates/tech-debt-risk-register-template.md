# OUT-06: Technical Debt & Risk Register

**Analysis Session**: {session_id}
**Target**: {target_name}
**Target Path**: {target_path}
**Analysis Date**: {analysis_date}
**Analyst**: SA-TRF-001 Agent

---

## 1. Summary Dashboard

| Category | Count | High Severity | Medium Severity | Low Severity |
|---------|-------|--------------|----------------|-------------|
| Code Smells | {code_smell_count} | {code_smell_high} | {code_smell_med} | {code_smell_low} |
| Anti-Patterns | {anti_pattern_count} | {anti_pattern_high} | {anti_pattern_med} | {anti_pattern_low} |
| Known Issues (TODO/FIXME/HACK) | {known_issue_count} | {known_issue_high} | {known_issue_med} | {known_issue_low} |
| Coupling Hotspots | {coupling_count} | {coupling_high} | {coupling_med} | {coupling_low} |
| Security Concerns | {security_count} | {security_high} | {security_med} | {security_low} |
| Performance Risks | {perf_count} | {perf_high} | {perf_med} | {perf_low} |
| **Total** | **{total_count}** | **{total_high}** | **{total_med}** | **{total_low}** |

> **Note**: {no_debt_statement_if_none}
> If no debt or risks are identified, state: "No technical debt or risk items identified in this target."

---

## 2. Technical Debt Register

### 2.1 Code Smells

| ID | Smell Type | File | Line(s) | Severity | Description | Transformation Impact |
|----|-----------|------|---------|----------|-------------|----------------------|
| CS-01 | {smell_type_1} | {file_1} | {lines_1} | {severity_1} | {description_1} | {impact_1} |
| CS-02 | {smell_type_2} | {file_2} | {lines_2} | {severity_2} | {description_2} | {impact_2} |

> Smell types: `Long Method` `Large Class` `Data Class` `Feature Envy` `Primitive Obsession` `Shotgun Surgery` `Divergent Change` `Dead Code` `Duplicate Code` `Magic Numbers`

### 2.2 Anti-Patterns

| ID | Pattern | File | Line(s) | Severity | Description | Recommended Fix |
|----|---------|------|---------|----------|-------------|----------------|
| AP-01 | {pattern_1} | {file_1} | {lines_1} | {severity_1} | {description_1} | {fix_1} |
| AP-02 | {pattern_2} | {file_2} | {lines_2} | {severity_2} | {description_2} | {fix_2} |

> Anti-patterns: `God Object` `Spaghetti Code` `Golden Hammer` `Lava Flow` `Blob` `Poltergeist` `Singleton Abuse` `Service Locator` `Tight Coupling` `Circular Dependency`

### 2.3 Known Issues (TODO / FIXME / HACK)

| ID | Tag | File | Line | Severity | Message | Age | Owner |
|----|-----|------|------|----------|---------|-----|-------|
| KI-01 | {tag_1} | {file_1} | {line_1} | {severity_1} | `{message_1}` | {age_1} | {owner_1} |
| KI-02 | {tag_2} | {file_2} | {line_2} | {severity_2} | `{message_2}` | {age_2} | {owner_2} |

---

## 3. Coupling Hotspots

| ID | Component | Coupled To | Coupling Type | Afferent Coupling (Ca) | Efferent Coupling (Ce) | Instability | Transformation Risk |
|----|----------|-----------|--------------|----------------------|----------------------|-------------|---------------------|
| CH-01 | {component_1} | {coupled_to_1} | {coupling_type_1} | {ca_1} | {ce_1} | {instability_1} | {risk_1} |
| CH-02 | {component_2} | {coupled_to_2} | {coupling_type_2} | {ca_2} | {ce_2} | {instability_2} | {risk_2} |

> Coupling types: `Content` `Common` `Control` `Stamp` `Data` `Message` `Shared State`
> Instability = Ce / (Ca + Ce). High instability (→1) = risky to change.

---

## 4. Security Concerns

| ID | Concern Type | File | Line(s) | Severity | Description | CVE/CWE | Remediation |
|----|-------------|------|---------|----------|-------------|---------|-------------|
| SEC-01 | {concern_type_1} | {file_1} | {lines_1} | {severity_1} | {description_1} | {cve_1} | {remediation_1} |
| SEC-02 | {concern_type_2} | {file_2} | {lines_2} | {severity_2} | {description_2} | {cve_2} | {remediation_2} |

> Concern types: `Hardcoded Credentials` `SQL Injection` `Unvalidated Input` `Insecure Dependency` `Sensitive Data Exposure` `Missing Auth` `Insecure Deserialization`

---

## 5. Performance Risks

| ID | Risk Type | File | Line(s) | Severity | Description | Estimated Impact | Recommendation |
|----|----------|------|---------|----------|-------------|-----------------|---------------|
| PR-01 | {risk_type_1} | {file_1} | {lines_1} | {severity_1} | {description_1} | {impact_1} | {recommendation_1} |
| PR-02 | {risk_type_2} | {file_2} | {lines_2} | {severity_2} | {description_2} | {impact_2} | {recommendation_2} |

> Risk types: `N+1 Query` `Missing Index` `Unbounded Collection` `Synchronous Blocking` `Cache Miss Storm` `Memory Leak` `Thread Safety` `Inefficient Algorithm`

---

## 6. Hardcoded Values & Configuration Risks

| ID | Value | File | Line | Type | Severity | Recommended Action |
|----|-------|------|------|------|----------|-------------------|
| HV-01 | `{value_1}` | {file_1} | {line_1} | {type_1} | {severity_1} | {action_1} |
| HV-02 | `{value_2}` | {file_2} | {line_2} | {type_2} | {severity_2} | {action_2} |

> Types: `URL` `Credentials` `Magic Number` `Business Rule` `Timeout` `Limit`

---

## 7. Transformation Risk Areas

> Areas that present elevated risk specifically because of the planned transformation.

| Risk Area | Risk Description | Severity | Trigger Condition | Mitigation Strategy |
|----------|-----------------|----------|------------------|---------------------|
| {area_1} | {description_1} | {severity_1} | {trigger_1} | {mitigation_1} |
| {area_2} | {description_2} | {severity_2} | {trigger_2} | {mitigation_2} |

---

## 8. Debt Paydown Priority

> Recommended order for addressing debt items, considering transformation sequence.

| Priority | Item(s) | Rationale | Must-Fix-Before-Transform? |
|----------|---------|-----------|--------------------------|
| P1 (Critical — fix first) | {p1_items} | {p1_rationale} | Yes |
| P2 (High — fix during transform) | {p2_items} | {p2_rationale} | Recommended |
| P3 (Medium — fix after transform) | {p3_items} | {p3_rationale} | No |
| P4 (Low — backlog) | {p4_items} | {p4_rationale} | No |
