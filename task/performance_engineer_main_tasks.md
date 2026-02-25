# Main Tasks of a Performance Engineer

A Performance Engineer's core responsibilities throughout the project lifecycle:

---

## 📋 Project Lifecycle Tasks

### 1. Inception Phase
| Task | Description |
|---|---|
| **PE-INC-001 — Performance Requirements Gathering** | Collaborating with stakeholders to define performance expectations including response time, throughput, and concurrency targets. |
| **PE-INC-002 — Workload Profiling** | Analyzing expected user patterns, peak traffic volumes, transaction mixes, and seasonal demand fluctuations. |
| **PE-INC-003 — Baseline Assessment** | Benchmarking current system performance to establish baselines for comparison and improvement measurement. |
| **PE-INC-004 — Tool & Infrastructure Planning** | Selecting performance testing tools (JMeter, Gatling, k6, Locust, NeoLoad) and provisioning load generation infrastructure. |
| **PE-INC-005 — Risk Identification** | Identifying potential performance bottlenecks, single points of failure, and resource-constrained components early. |

### 2. Requirements Phase
| Task | Description |
|---|---|
| **PE-REQ-001 — Performance Test Strategy** | Creating the performance test strategy document covering scope, approach, test types, environments, and acceptance criteria. |
| **PE-REQ-002 — NFR Specification & SLA Definition** | Defining measurable non-functional requirements with specific SLAs (P95 latency < 200ms, 99.9% availability, etc.). |
| **PE-REQ-003 — Test Scenario Design** | Designing realistic test scenarios including load, stress, endurance, spike, scalability, and capacity tests. |
| **PE-REQ-004 — Workload Model Development** | Building detailed workload models defining virtual user profiles, transaction ratios, think times, and ramp-up patterns. |
| **PE-REQ-005 — Test Data & Environment Requirements** | Specifying data volume needs, production-like environment configurations, and network topology for accurate testing. |

### 3. Sprint / Development Phase
| Task | Description |
|---|---|
| **PE-DEV-001 — Performance Test Script Development** | Writing and parameterizing test scripts with correlation, data-driven inputs, and realistic user behavior simulation. |
| **PE-DEV-002 — Component-Level Performance Testing** | Running early performance tests on APIs, microservices, and database queries to catch bottlenecks during development. |
| **PE-DEV-003 — Performance Code Review** | Reviewing code for common performance anti-patterns (N+1 queries, memory leaks, synchronous blocking, inefficient algorithms). |
| **PE-DEV-004 — APM Integration** | Configuring Application Performance Monitoring (Dynatrace, New Relic, AppDynamics, Datadog APM) for real-time profiling. |
| **PE-DEV-005 — Continuous Performance Testing** | Integrating automated performance regression tests into CI/CD pipelines to detect degradation early. |

### 4. QA & UAT Phase
| Task | Description |
|---|---|
| **PE-QA-001 — Load & Stress Testing Execution** | Executing full-scale load tests simulating production traffic patterns and stress tests beyond expected peak capacity. |
| **PE-QA-002 — Endurance & Soak Testing** | Running extended-duration tests to detect memory leaks, connection pool exhaustion, and time-based degradation. |
| **PE-QA-003 — Bottleneck Analysis & Diagnostics** | Analyzing test results using profilers, thread dumps, heap dumps, and APM data to pinpoint root causes of bottlenecks. |
| **PE-QA-004 — Scalability Validation** | Testing horizontal and vertical scaling behavior to validate auto-scaling policies and resource elasticity. |
| **PE-QA-005 — Performance Test Reporting** | Producing detailed performance test reports with metrics, graphs, bottleneck findings, and tuning recommendations. |

### 5. Release & Growth Phase
| Task | Description |
|---|---|
| **PE-REL-001 — Production Performance Baselining** | Establishing production performance baselines for ongoing monitoring and anomaly detection after go-live. |
| **PE-REL-002 — Real User Monitoring (RUM)** | Configuring and analyzing real user monitoring data to understand actual end-user experience and geographic performance. |
| **PE-REL-003 — Capacity Planning & Forecasting** | Modeling capacity thresholds and forecasting infrastructure scaling needs based on growth trends and traffic projections. |
| **PE-REL-004 — Performance Tuning & Optimization** | Driving optimization initiatives including caching strategies, query tuning, connection pooling, and CDN configuration. |
| **PE-REL-005 — Performance Governance** | Establishing ongoing performance budgets, regression thresholds, and periodic benchmark cadence for continuous assurance. |
