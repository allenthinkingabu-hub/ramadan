# OUT-05: Test Coverage Assessment

**Analysis Session**: {session_id}
**Target**: {target_name}
**Target Path**: {target_path}
**Analysis Date**: {analysis_date}
**Analyst**: SA-TRF-001 Agent

---

## 1. Coverage Summary

| Test Type | Files Found | Test Cases | Coverage Level | Notes |
|----------|------------|-----------|---------------|-------|
| Unit Tests | {unit_files} | {unit_cases} | {unit_level} | {unit_notes} |
| Integration Tests | {int_files} | {int_cases} | {int_level} | {int_notes} |
| End-to-End Tests | {e2e_files} | {e2e_cases} | {e2e_level} | {e2e_notes} |
| Contract Tests | {contract_files} | {contract_cases} | {contract_level} | {contract_notes} |
| Performance Tests | {perf_files} | {perf_cases} | {perf_level} | {perf_notes} |

> Coverage levels: `High (>80%)` `Medium (50-80%)` `Low (<50%)` `None (0%)`

**Overall Coverage Assessment**: {overall_coverage_level}

---

## 2. Test File Inventory

| Test File | Test Type | Target File(s) Covered | Test Cases | Framework | Notes |
|----------|----------|----------------------|-----------|-----------|-------|
| {test_file_1} | {type_1} | {targets_1} | {cases_1} | {framework_1} | {notes_1} |
| {test_file_2} | {type_2} | {targets_2} | {cases_2} | {framework_2} | {notes_2} |
| {test_file_n} | {type_n} | {targets_n} | {cases_n} | {framework_n} | {notes_n} |

---

## 3. Unit Test Analysis

### Test Framework & Configuration

- **Framework**: {unit_test_framework}
- **Configuration File**: {unit_test_config}
- **Test Runner Command**: `{test_runner_command}`
- **Mocking Library**: {mocking_library}

### Unit Test Coverage by Responsibility

| Responsibility (from OUT-02) | Test Coverage | Test Case Count | Notes |
|-----------------------------|--------------|----------------|-------|
| R-01: {responsibility_1} | {coverage_1} | {count_1} | {notes_1} |
| R-02: {responsibility_2} | {coverage_2} | {count_2} | {notes_2} |
| R-0N: {responsibility_n} | {coverage_n} | {count_n} | {notes_n} |

### Test Quality Assessment

| Criterion | Assessment | Notes |
|-----------|-----------|-------|
| Assertion quality | {assertion_quality} | {assertion_notes} |
| Happy path coverage | {happy_path_coverage} | {happy_path_notes} |
| Edge case coverage | {edge_case_coverage} | {edge_case_notes} |
| Error path coverage | {error_path_coverage} | {error_path_notes} |
| Mock usage appropriateness | {mock_quality} | {mock_notes} |
| Test independence | {independence} | {independence_notes} |

---

## 4. Integration Test Analysis

### Integration Points Tested

| Integration Point | Test File | Scenarios Covered | Scenarios Missing |
|------------------|----------|------------------|-------------------|
| {integration_1} | {test_file_1} | {covered_1} | {missing_1} |
| {integration_2} | {test_file_2} | {covered_2} | {missing_2} |

### Test Environment Requirements

- **Database**: {db_requirement}
- **External Services**: {ext_service_requirement}
- **Infrastructure**: {infra_requirement}
- **Seed Data**: {seed_data_requirement}

---

## 5. Untested Code Paths

| Code Path | File | Line(s) | Risk Level | Why Critical | Recommended Test |
|----------|------|---------|------------|-------------|-----------------|
| {path_1} | {file_1} | {lines_1} | {risk_1} | {why_critical_1} | {recommended_test_1} |
| {path_2} | {file_2} | {lines_2} | {risk_2} | {why_critical_2} | {recommended_test_2} |

> Risk levels: `Critical` `High` `Medium` `Low`

---

## 6. Coverage Gap Analysis

### High-Risk Gaps (Must Address Before Transformation)

| Gap ID | Description | Affected Responsibility | Risk | Effort to Fix |
|--------|------------|------------------------|------|---------------|
| GAP-01 | {gap_description_1} | {responsibility_1} | {risk_1} | {effort_1} |
| GAP-02 | {gap_description_2} | {responsibility_2} | {risk_2} | {effort_2} |

### Medium-Risk Gaps (Should Address During Transformation)

| Gap ID | Description | Affected Responsibility | Risk | Effort to Fix |
|--------|------------|------------------------|------|---------------|
| GAP-03 | {gap_description_3} | {responsibility_3} | {risk_3} | {effort_3} |

### Low-Risk Gaps (Nice to Address Post-Transformation)

| Gap ID | Description | Affected Responsibility | Risk | Effort to Fix |
|--------|------------|------------------------|------|---------------|
| GAP-04 | {gap_description_4} | {responsibility_4} | {risk_4} | {effort_4} |

---

## 7. Test Infrastructure Assessment

| Item | Status | Notes |
|------|--------|-------|
| CI/CD test execution | {ci_status} | {ci_notes} |
| Test data management | {data_mgmt_status} | {data_mgmt_notes} |
| Test isolation | {isolation_status} | {isolation_notes} |
| Flaky tests identified | {flaky_count} | {flaky_notes} |
| Test execution time | {exec_time} | {exec_time_notes} |

---

## 8. Transformation Readiness (Test Perspective)

| Question | Assessment | Notes |
|---------|-----------|-------|
| Can we safely refactor with current coverage? | {safe_to_refactor} | {safety_notes} |
| Which behaviors have no regression safety net? | {unprotected_behaviors} | {unprotected_notes} |
| What tests must be added before transformation starts? | {prereq_tests} | {prereq_notes} |
| Estimated effort to reach safe coverage baseline | {effort_estimate} | {effort_notes} |
