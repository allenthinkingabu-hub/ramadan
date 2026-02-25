# Main Tasks of a Data Architect

A Data Architect's core responsibilities throughout the project lifecycle:

---

## 📋 Project Lifecycle Tasks

### 1. Inception Phase
| Task | Description |
|---|---|
| **DA-INC-001 — Enterprise Data Landscape Assessment** | Inventorying existing data assets, databases, data warehouses, data lakes, and data flows across business domains to establish a baseline. |
| **DA-INC-002 — Data Strategy Alignment** | Aligning data architecture initiatives with business strategy, analytics goals, and digital transformation objectives. |
| **DA-INC-003 — Data Maturity Evaluation** | Assessing the organization's data management maturity across dimensions: quality, governance, integration, metadata, and master data. |
| **DA-INC-004 — Regulatory & Compliance Analysis** | Identifying data-related regulatory requirements (GDPR, CCPA, HIPAA, SOX) and their impact on data storage, retention, and processing. |
| **DA-INC-005 — Data Architecture Vision** | Defining the high-level data architecture vision, guiding principles, and target-state direction for the project or program. |

### 2. Requirements Phase
| Task | Description |
|---|---|
| **DA-REQ-001 — Conceptual & Logical Data Modeling** | Designing enterprise-level conceptual and logical data models that capture core business entities, relationships, and business rules across domains. |
| **DA-REQ-002 — Data Governance Framework Design** | Establishing data governance policies, data ownership models, data stewardship roles, and data quality accountability structures. |
| **DA-REQ-003 — Master Data Management (MDM) Strategy** | Defining MDM architecture, golden record strategies, matching/merging rules, and master data distribution patterns across systems. |
| **DA-REQ-004 — Data Standards & Dictionary** | Creating and maintaining enterprise data standards, naming conventions, data dictionaries, and canonical data definitions. |
| **DA-REQ-005 — Data Layer Architecture** | Designing the data tier architecture including ODS, staging, data warehouse (DW), data mart (DM), and consumption layer patterns. |

### 3. Sprint / Development Phase
| Task | Description |
|---|---|
| **DA-DEV-001 — Physical Data Model Design** | Translating logical models into optimized physical data models considering indexing, partitioning, sharding, and storage engine characteristics. |
| **DA-DEV-002 — Data Integration Architecture** | Designing data integration patterns (ETL/ELT, CDC, event streaming, API-based) and governing data movement across system boundaries. |
| **DA-DEV-003 — Data Quality Rules Definition** | Defining measurable data quality rules (completeness, accuracy, consistency, timeliness, uniqueness) and validation checkpoints. |
| **DA-DEV-004 — Data Model Review & Governance** | Reviewing data models produced by development teams for compliance with enterprise standards, naming conventions, and normalization rules. |
| **DA-DEV-005 — Metadata & Data Lineage Design** | Designing metadata management strategies and data lineage tracking to enable impact analysis, auditing, and regulatory traceability. |

### 4. QA & UAT Phase
| Task | Description |
|---|---|
| **DA-QA-001 — Data Model Conformance Review** | Verifying that implemented physical data models conform to approved logical models and enterprise data standards. |
| **DA-QA-002 — Data Quality Validation** | Validating data quality metrics against defined thresholds and certifying data readiness for production use. |
| **DA-QA-003 — Data Migration Verification** | Reviewing data migration results for completeness, referential integrity, transformation accuracy, and historical data preservation. |
| **DA-QA-004 — Data Integration Testing Support** | Validating end-to-end data flows across integrated systems, verifying data contracts, and confirming SLA compliance. |
| **DA-QA-005 — Data Security & Privacy Review** | Verifying data masking, encryption, access controls, and anonymization measures are correctly implemented per governance policies. |

### 5. Release & Growth Phase
| Task | Description |
|---|---|
| **DA-REL-001 — Data Catalog & Metadata Management** | Maintaining the enterprise data catalog (DataHub, Alation, Collibra) with up-to-date metadata, lineage, ownership, and usage documentation. |
| **DA-REL-002 — Data Architecture Roadmap Evolution** | Refining the data architecture roadmap based on delivered capabilities, new business requirements, and emerging data technologies. |
| **DA-REL-003 — Data Quality Monitoring** | Establishing ongoing data quality monitoring dashboards, alerting, and remediation workflows for production data assets. |
| **DA-REL-004 — Data Architecture Governance** | Conducting periodic data architecture reviews, enforcing standards compliance, and managing data-related technical debt. |
| **DA-REL-005 — Emerging Data Technology Evaluation** | Evaluating emerging data technologies (data mesh, data fabric, real-time analytics, vector databases) for strategic adoption opportunities. |
