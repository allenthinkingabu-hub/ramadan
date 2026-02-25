# Main Tasks of a Cloud Engineer

A Cloud Engineer's core responsibilities throughout the project lifecycle:

---

## 📋 Project Lifecycle Tasks

### 1. Inception Phase
| Task | Description |
|---|---|
| **CE-INC-001 — Cloud Strategy Assessment** | Evaluating cloud adoption models (public, private, hybrid, multi-cloud) aligned with business and compliance needs. |
| **CE-INC-002 — Cloud Platform Selection** | Recommending cloud providers (AWS, Azure, GCP) and managed services based on workload requirements and team expertise. |
| **CE-INC-003 — Landing Zone Design** | Planning account structure, organizational units, resource groups, and governance guardrails for the cloud environment. |
| **CE-INC-004 — Cost Modeling & FinOps** | Building cloud cost projections, selecting pricing models (on-demand, reserved, spot), and defining budget controls. |
| **CE-INC-005 — Compliance & Sovereignty Review** | Identifying data residency, sovereignty requirements, and cloud-specific regulatory constraints (FedRAMP, SOC 2). |

### 2. Requirements Phase
| Task | Description |
|---|---|
| **CE-REQ-001 — Cloud Architecture Design** | Designing cloud-native architecture with compute, storage, networking, and managed service selections. |
| **CE-REQ-002 — Network Topology Design** | Planning VPCs, subnets, peering, VPN/Direct Connect, DNS, load balancing, and CDN configurations. |
| **CE-REQ-003 — Identity & Access Management** | Designing IAM policies, roles, service accounts, SSO integration, and least-privilege access models. |
| **CE-REQ-004 — Infrastructure as Code (IaC)** | Selecting IaC tooling (Terraform, CloudFormation, Bicep, CDK) and defining module structure and state management. |
| **CE-REQ-005 — Service Level Design** | Defining availability targets, redundancy strategies, and mapping cloud service SLAs to business requirements. |

### 3. Sprint / Development Phase
| Task | Description |
|---|---|
| **CE-DEV-001 — Infrastructure Provisioning** | Building and deploying cloud resources through IaC pipelines with version control and peer review. |
| **CE-DEV-002 — Container & Serverless Implementation** | Configuring Kubernetes clusters (EKS, AKS, GKE), serverless functions (Lambda, Cloud Functions), and container registries. |
| **CE-DEV-003 — Cloud Service Integration** | Implementing managed services (message queues, caches, databases, object storage) and connecting them to application workloads. |
| **CE-DEV-004 — Automation & Scripting** | Developing automation scripts for resource management, scheduled tasks, and self-healing infrastructure. |
| **CE-DEV-005 — Environment Parity** | Ensuring consistency across dev, staging, and production environments through parameterized IaC and configuration management. |

### 4. QA & UAT Phase
| Task | Description |
|---|---|
| **CE-QA-001 — Infrastructure Testing** | Validating IaC deployments with policy-as-code (OPA, Sentinel) and infrastructure test frameworks (Terratest, Checkov). |
| **CE-QA-002 — Load & Resilience Testing** | Conducting cloud-level load tests and chaos engineering experiments (AWS FIS, Chaos Monkey) to validate fault tolerance. |
| **CE-QA-003 — Security Posture Validation** | Running cloud security scans (Prowler, ScoutSuite, Cloud Custodian) and verifying configurations against CIS benchmarks. |
| **CE-QA-004 — Disaster Recovery Drills** | Executing DR failover tests across regions/zones, validating backup restoration, and measuring RTO/RPO compliance. |
| **CE-QA-005 — Cost Optimization Review** | Identifying over-provisioned resources, unused assets, and right-sizing opportunities before production launch. |

### 5. Release & Growth Phase
| Task | Description |
|---|---|
| **CE-REL-001 — Production Deployment** | Executing production cloud infrastructure rollouts with blue-green or canary strategies and rollback readiness. |
| **CE-REL-002 — Cloud Monitoring & Observability** | Configuring CloudWatch, Azure Monitor, or Cloud Operations with dashboards, alerts, and log aggregation. |
| **CE-REL-003 — Auto-Scaling & Elasticity** | Implementing and tuning auto-scaling policies (HPA, KEDA, ASG) to handle traffic fluctuations efficiently. |
| **CE-REL-004 — Cost Management & Optimization** | Monitoring cloud spend, implementing tagging strategies, rightsizing instances, and leveraging savings plans. |
| **CE-REL-005 — Cloud Platform Evolution** | Evaluating new cloud services, migrating workloads to better-fit services, and upgrading infrastructure components. |
