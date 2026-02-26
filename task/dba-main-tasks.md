# Main Tasks of a Database Administrator (DBA)

A DBA's core responsibilities throughout the project lifecycle:

---

## 📋 Project Lifecycle Tasks

### 1. Inception Phase
| Task | Description |
|---|---|
| **DA(-INC-001 — Database Landscape Assessment** | Inventorying existing database instances, versions, configurations, and licensing across environments. |
| **DA(-INC-002 — Database Platform Selection** | Recommending database engines (Oracle, PostgreSQL, MySQL, SQL Server, MongoDB) based on workload and scalability needs. |
| **DA(-INC-003 — Capacity & Sizing Estimation** | Estimating storage, memory, IOPS, and connection pool requirements based on projected data volumes and user load. |
| **DA(-INC-004 — Compliance & Security Review** | Identifying data residency, encryption, auditing, and regulatory requirements (PCI-DSS, HIPAA, SOX) impacting database design. |
| **DA(-INC-005 — High Availability Strategy** | Proposing HA/DR topology (replication, clustering, failover) aligned with business continuity requirements (RPO/RTO). |

### 2. Requirements Phase
| Task | Description |
|---|---|
| **DA(-REQ-001 — Physical Database Design** | Translating logical data models into optimized physical schemas with appropriate data types, constraints, and partitioning. |
| **DA(-REQ-002 — Indexing Strategy** | Designing index plans (B-tree, hash, composite, covering) to support anticipated query patterns and performance SLAs. |
| **DA(-REQ-003 — Security Architecture** | Defining database roles, privileges, row-level security, encryption at rest/in transit, and audit logging policies. |
| **DA(-REQ-004 — Backup & Recovery Planning** | Establishing backup schedules (full, incremental, differential), retention policies, and recovery procedures. |
| **DA(-REQ-005 — Migration Planning** | Designing data migration strategies, ETL workflows, and cutover plans for legacy database transitions. |

### 3. Sprint / Development Phase
| Task | Description |
|---|---|
| **DA(-DEV-001 — Schema Change Management** | Reviewing, approving, and deploying DDL changes (tables, views, stored procedures, triggers) through controlled processes. |
| **DA(-DEV-002 — Query Optimization** | Analyzing slow queries via execution plans, adding indexes, rewriting SQL, and tuning join strategies. |
| **DA(-DEV-003 — Stored Procedure & Function Development** | Writing and reviewing database-side logic including stored procedures, functions, and triggers. |
| **DA(-DEV-004 — Developer Support** | Advising developers on efficient SQL patterns, ORM configuration, connection pooling, and transaction management. |
| **DA(-DEV-005 — Data Integrity Enforcement** | Implementing and validating constraints, foreign keys, check constraints, and data validation rules. |

### 4. QA & UAT Phase
| Task | Description |
|---|---|
| **DA(-QA-001 — Performance Benchmarking** | Running database load tests, stress tests, and identifying bottlenecks (locks, deadlocks, I/O contention). |
| **DA(-QA-002 — Test Data Management** | Provisioning realistic test data sets with data masking/anonymization for non-production environments. |
| **DA(-QA-003 — Failover & Recovery Testing** | Executing HA failover drills and backup restoration tests to validate RPO/RTO targets are achievable. |
| **DA(-QA-004 — Security Audit** | Verifying database access controls, encryption settings, audit trails, and vulnerability scan results before go-live. |
| **DA(-QA-005 — Schema Freeze Validation** | Confirming all schema changes are finalized, migration scripts are tested, and rollback scripts are prepared. |

### 5. Release & Growth Phase
| Task | Description |
|---|---|
| **DA(-REL-001 — Production Deployment** | Executing database migrations, schema updates, and data seeding scripts during release windows. |
| **DA(-REL-002 — Monitoring & Alerting** | Configuring database monitoring (CPU, memory, disk, connections, replication lag) with threshold-based alerts. |
| **DA(-REL-003 — Performance Tuning** | Continuously analyzing production query performance, optimizing execution plans, and adjusting configurations. |
| **DA(-REL-004 — Storage & Growth Management** | Monitoring data growth trends, managing tablespace expansion, archiving strategies, and data purging policies. |
| **DA(-REL-005 — Patching & Upgrades** | Planning and executing database engine patches, version upgrades, and security hotfixes with minimal downtime. |
