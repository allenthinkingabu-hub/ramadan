# Architecture Design Report — AI Smart Grader

## Task: IA-REQ-001 | Wave 10, Step 1
## Role: IT Architect
## Generated: 2026-03-01
## Status: Complete

---

## 1. Executive Summary

The AI Smart Grader is a cloud-native, AI-powered homework grading and intelligent error notebook platform serving 5 user roles (Student, Teacher, Parent, Administrator, Guest) across 4 client platforms (Flutter mobile, Angular web/H5, WeChat Mini Program, Admin Console). This architecture design defines a **10-microservice system** built on Java 21 / Spring Boot 3.x / Spring Cloud 2024.x, deployed on Kubernetes with fully independent regional clusters for GDPR/PIPL compliance. The architecture addresses key challenges including multi-LLM cascade routing with streaming responses, dual-layer AI result caching (SHA-256 + pHash) for 60-80% cost reduction, event-driven error notebook with spaced repetition, multi-tenant data isolation via PostgreSQL Row-Level Security, and a DevSecOps shift-left security pipeline. 15 architectural decisions (AD-01 through AD-15) and 23 validated requirements (VR-001 through VR-023) guide the design.

---

## 2. Design Scope & Objectives

### 2.1 Purpose
Produce the definitive architecture design — logical + physical views — covering C4 layers (context/container/component), key sequence flows, integration points, and deployment/runtime topology for the AI Smart Grader platform.

### 2.2 Scope
- **In scope**: All 10 microservices, 4 client applications, data stores, message broker, observability stack, CI/CD pipeline, security architecture, multi-region deployment
- **Out of scope**: Detailed UI/UX design, individual API endpoint specifications, database migration scripts, Helm chart authoring

### 2.3 Constraints
See: `nfr-alignment.md` — Constraints section (CON-001 through CON-008)

### 2.4 Upstream References
- **PRD**: `prd/ai-smart-grader/PRD-AI-Smart-Grader-v1.0.md` (1965 lines, 120+ requirements)
- **BRD**: `brd/ai-smart-grader/BRD-AI-Smart-Grader-v1.0.md` (545 lines, 39 functional requirements)
- **Note**: Wave 9 SA-REQ deliverables were not available; PRD/BRD served as primary inputs

---

## 3. Architecture Overview

### 3.1 C4 Context Diagram

The system context shows 5 user roles interacting with the AI Smart Grader platform boundary, and 17 external system integrations grouped by AI/ML, Authentication, Payment, Messaging, and Infrastructure.

See: [`diagrams/c4-context.md`](diagrams/c4-context.md)

**Key aspects**:
- 5 user roles: Student, Teacher, Parent, Administrator, Guest
- 17 external integrations: 3 LLM providers, PaddleOCR, Content Moderation, 3 OAuth providers, 5 Payment providers, SMS Gateway, Email Service, CDN
- All client communication over HTTPS; AI providers use REST + SSE for streaming

### 3.2 C4 Container Diagram

The container diagram shows the internal structure of the platform: 4 client containers, 10 microservice containers behind Spring Cloud Gateway, 4 data stores, 1 message broker, and Nacos config/discovery.

See: [`diagrams/c4-container.md`](diagrams/c4-container.md)

**Container inventory**:

| Category | Containers |
|:---|:---|
| Clients (4) | Flutter App, Angular Web/H5, WeChat Mini Program, Admin Console |
| Services (10) | Auth, Grading, Image, Error Notebook, Analytics, User, Payment, Notification, Admin, Config (Nacos) |
| Data Stores (4) | PostgreSQL 16, Redis 7.x, MinIO/Cloud OSS, Elasticsearch |
| Message Broker (1) | RabbitMQ |

### 3.3 C4 Component Diagrams

Two component-level diagrams detail the internals of the most complex services:

**Grading Service** (11 components): Cascade Router, Complexity Estimator, Result Cache Manager, LLM Invoker, Streaming Response Parser, Confidence Scorer, OCR Fallback Handler, Result Persistence, Event Publisher, Prompt Template Manager.
See: [`diagrams/c4-component-grading-engine.md`](diagrams/c4-component-grading-engine.md)

**Error Notebook Service** (11 components): Error Collector, Classification Engine, Spaced Repetition Scheduler, Practice Question Generator, Mastery Evaluator, Weakness Analyzer, Capacity Enforcer, PDF Export Service, Error Persistence, Event Publisher.
See: [`diagrams/c4-component-error-notebook.md`](diagrams/c4-component-error-notebook.md)

---

## 4. Detailed Design

### 4.1 UML Sequence Diagrams

Three key interaction flows are documented:

**AI Grading Flow**: End-to-end flow from image upload through content moderation, cache check, LLM invocation with streaming, real-time response parsing, OCR fallback, result persistence, and downstream event publishing.
See: [`diagrams/uml-sequence-grading.md`](diagrams/uml-sequence-grading.md)

**Spaced Repetition Review Flow**: Student opens error notebook, loads due entries, attempts practice questions, evaluates mastery, updates review schedules, publishes events.
See: [`diagrams/uml-sequence-review.md`](diagrams/uml-sequence-review.md)

**Guest Onboarding Flow**: Device fingerprint tracking, limited AI grading trial (3 free tries), quota enforcement, and conversion prompt to registration with history preservation.
See: [`diagrams/uml-sequence-guest.md`](diagrams/uml-sequence-guest.md)

### 4.2 Data Flow Diagrams

**Grading Pipeline Data Flow**: Shows data transformations from raw image capture through processing, caching, LLM invocation, structured parsing, persistence, and event fan-out.
See: [`diagrams/data-flow-grading.md`](diagrams/data-flow-grading.md)

**Analytics Aggregation Pipeline**: Shows how raw events from grading, review, and user activity flow through aggregation engines to produce pre-computed dashboard data.
See: [`diagrams/data-flow-analytics.md`](diagrams/data-flow-analytics.md)

---

## 5. Deployment Architecture

Kubernetes-based deployment across 8 namespaces with independent regional clusters for compliance.

See: [`diagrams/deployment.md`](diagrams/deployment.md)

**Key deployment decisions**:
- 8 K8s namespaces: ingress, gateway, core-services, infrastructure, data, observability, security, canary
- Grading Service scales 3-10 pods (highest resource consumer)
- All stateful infrastructure in clustered/replicated mode
- Argo Rollouts for canary releases with SkyWalking metrics analysis
- HashiCorp Vault for runtime secret injection
- ModSecurity WAF at ingress + Falco DaemonSet for runtime security
- Fully independent clusters per region (China, EU, SEA) — no cross-region data flow

---

## 6. Interface/Integration View

### 6.1 Communication Protocols
- **Internal**: HTTP sync (gateway → services), AMQP async (RabbitMQ events), Nacos push (config)
- **Client-to-Platform**: HTTPS + SSE (Web/App), HTTPS + WebSocket (Mini Program)
- **External**: REST + SSE (LLM providers), OAuth 2.0 (auth), REST + Webhook (payments)

### 6.2 Interface Contracts
- 9 OpenAPI 3.0 service contracts with auto-generated client SDKs (Dart, TypeScript, JavaScript)
- 6 RabbitMQ event contracts with JSON schemas
- URL path versioning (`/api/v1/`) with 6-month deprecation policy

### 6.3 Error Handling & Resilience
- Resilience4j circuit breakers on all external integrations
- Exponential backoff retry policies (2-3 retries per interface)
- Dead Letter Queue for failed async messages
- LLM provider fallback (primary → secondary model)
- Fail-open cache strategy (cache unavailability doesn't block grading)

See: [`diagrams/integration-view.md`](diagrams/integration-view.md)

---

## 7. NFR Alignment Note

Comprehensive mapping of all NFR requirements to architecture decisions:

| Category | Key NFRs Addressed |
|:---|:---|
| Performance | API < 500ms, AI first token < 3s, upload < 2s, dashboard freshness |
| Scalability | 10K concurrent users, 100 concurrent grading, horizontal pod autoscaling |
| Availability | 99.9% uptime, zero-downtime deployments, infrastructure HA |
| Security | Encryption at rest/transit, RBAC, RLS multi-tenancy, GDPR/PIPL, DevSecOps |
| Resiliency | Circuit breakers, DLQ, offline capability, graceful degradation |
| Observability | Distributed tracing, centralized logging, metrics/alerting, health checks |
| Maintainability | Config hot-reload, OpenAPI contracts, A/B testing, canary releases |

See: [`nfr-alignment.md`](nfr-alignment.md)

---

## 8. Architecture Decision Records

| ADR# | Decision | Rationale | Status |
|:---|:---|:---|:---|
| AD-01 | RabbitMQ as message broker | Sufficient throughput for event-driven architecture; mature Spring AMQP support; simpler ops than Kafka for current scale. Future migration to Kafka if >10K msg/s needed. | Accepted |
| AD-02 | Spring Cloud Gateway as API gateway | Native Spring Cloud integration; JWT validation, rate limiting, circuit breaker out-of-box; consistent Java ecosystem. | Accepted |
| AD-03 | Apache SkyWalking for APM | Auto-instrumentation via Java agent; low overhead; native Spring Cloud support; open-source with strong community. | Accepted |
| AD-04 | Nacos 2.x for service discovery + config | Dual-purpose (discovery + config center); hot-reload via long-polling; namespace/group for multi-env; proven in Chinese cloud ecosystem. | Accepted |
| AD-05 | Independent K8s clusters per region | Strongest data residency compliance (GDPR, PIPL); eliminates cross-region data flow complexity; same codebase, region-specific Nacos config. | Accepted |
| AD-06 | Server-wins with user override for offline sync | Simplest conflict resolution for MVP; server is source of truth; user can manually override if needed. Future: CRDT for complex merge. | Accepted |
| AD-07 | Redis with content-hash keys for AI caching | Dual-layer (SHA-256 exact + pHash perceptual) catches identical and re-photographed submissions; projected 60-80% LLM cost reduction. | Accepted |
| AD-08 | SSE (Web/App) + WebSocket (Mini Program) | SSE is simpler and more HTTP-friendly for web/Flutter; WebSocket required for Mini Program (SSE not supported). Gateway handles protocol transparently. | Accepted |
| AD-09 | Flutter (mobile) + Angular (web/H5/admin) + Native Mini Program | User preference. 3-codebase hybrid with OpenAPI-generated shared API clients mitigates contract drift. Each platform uses native strengths. | Accepted |
| AD-10 | Angular + NG-ZORRO for admin console | Consistent with web frontend stack; NG-ZORRO provides 60+ enterprise components; separate SPA deployment isolates admin from student-facing app. | Accepted |
| AD-11 | GitLab CI + Argo CD for CI/CD | GitLab CI for pipeline definition + testing; Argo CD for GitOps-based K8s deployment; clear separation of build vs deploy. | Accepted |
| AD-12 | SkyWalking + Prometheus + Grafana + ELK for observability | Comprehensive 4-pillar observability: traces (SkyWalking), metrics (Prometheus/Grafana), logs (ELK), alerting (Alertmanager). | Accepted |
| AD-13 | OpenAPI 3.0 + code generators for API contracts | Single source of truth for 3 frontend codebases; auto-generated Dart, TypeScript, JavaScript SDKs; contract testing in CI via Spring Cloud Contract. | Accepted |
| AD-14 | k6 + Chaos Mesh + Lighthouse CI for performance testing | k6 for load/stress testing; Chaos Mesh for resilience validation; Lighthouse CI for frontend performance in CI pipeline. | Accepted |
| AD-15 | DevSecOps shift-left security pipeline | SAST (SonarQube), SCA (Trivy), secret detection (Gitleaks) in CI; DAST (OWASP ZAP) scheduled; runtime security (Falco, ModSecurity WAF). | Accepted |

---

## 9. Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| LLM provider API instability or pricing changes | High | Medium | Spring AI abstraction + adapter pattern limits blast radius; multi-provider fallback; cascade routing can shift traffic |
| LLM costs exceed budget projections | High | Medium | Dual-layer caching (60-80% reduction); cascade routing selects cost-effective models; tier-based quotas; monitoring dashboards |
| Multi-tenant data leakage | Critical | Low | Defense-in-depth: PostgreSQL RLS + Hibernate @Filter + gateway tenant header injection; automated RLS audit tests |
| Operational complexity of 10 microservices from day 1 | Medium | Medium | GitOps (Argo CD) simplifies deployments; standardized Helm charts; centralized observability; shared Spring Boot starter |
| 3-codebase frontend drift | Medium | Medium | OpenAPI-generated SDKs; contract testing in CI; shared API spec as single source of truth |
| Content moderation false positives blocking legitimate educational content | Medium | Medium | Configurable sensitivity thresholds; manual review queue for borderline cases; moderation analytics dashboard |
| PostgreSQL RLS performance at scale | Medium | Low | Index optimization on tenant_id; connection pooling (HikariCP); read replicas for analytics; benchmark with k6 at 10K users |
| RabbitMQ throughput bottleneck under high load | Medium | Low | Current target 10K msg/s well within RabbitMQ capacity; monitoring dashboards; migration path to Apache Kafka documented |
| PaddleOCR handwriting recognition accuracy | Medium | Medium | OCR is fallback only (not primary path); confidence threshold tunable; degradation path returns LLM result with low-confidence flag |
| Team Kubernetes expertise gap | Medium | Medium | Consider managed K8s (EKS/GKE/ACK); standardized Helm charts reduce operational burden; runbooks for common operations |

---

## 10. Appendices

### A: Full Technology Stack

| Layer | Technology | Version | Purpose |
|:---|:---|:---|:---|
| **Backend** | Java | 21 (LTS) | Runtime |
| | Spring Boot | 3.x | Application framework |
| | Spring Cloud | 2024.x | Cloud-native patterns |
| | Spring AI | Latest | LLM integration abstraction |
| | Spring Security | 6.x | Authentication/authorization |
| | Spring Data JPA | 3.x | Data access |
| | Spring AMQP | 3.x | RabbitMQ integration |
| **Frontend** | Flutter | Latest | iOS/Android mobile app |
| | Dart | Latest | Flutter language |
| | Drift | Latest | Flutter SQLite ORM (offline) |
| | Angular | 18 | Web/H5 client |
| | TypeScript | 5.x | Angular language |
| | NG-ZORRO | Latest | Admin console UI components |
| | WXML/WXSS | N/A | WeChat Mini Program |
| **API Gateway** | Spring Cloud Gateway | Latest | Request routing, JWT, rate limiting |
| **Discovery/Config** | Nacos | 2.x | Service discovery + configuration |
| **Database** | PostgreSQL | 16 | Primary RDBMS (RLS, ltree) |
| **Cache** | Redis | 7.x | Caching, sessions, rate limiting |
| **Message Queue** | RabbitMQ | Latest | Async event processing |
| **Object Storage** | MinIO | Latest | S3-compatible storage |
| **Search/Logging** | Elasticsearch | 8.x | Centralized logging, search |
| | Fluentd | Latest | Log collection |
| | Kibana | 8.x | Log visualization |
| **APM** | Apache SkyWalking | Latest | Distributed tracing |
| **Metrics** | Prometheus | Latest | Metrics collection |
| | Grafana | Latest | Metrics visualization |
| | Alertmanager | Latest | Alert routing |
| **CI/CD** | GitLab CI | Latest | CI pipeline |
| | Argo CD | Latest | GitOps deployment |
| | Argo Rollouts | Latest | Canary/blue-green releases |
| | Helm | 3.x | K8s package management |
| | Terraform | Latest | Infrastructure as Code |
| **Container** | Harbor | Latest | Container registry |
| | Docker | Latest | Container runtime |
| | Kubernetes | Latest | Container orchestration |
| **Security** | HashiCorp Vault | Latest | Secret management |
| | SonarQube | Latest | SAST |
| | SpotBugs | Latest | Java bug detection |
| | OWASP ZAP | Latest | DAST |
| | Trivy | Latest | Container/SCA scanning |
| | Gitleaks | Latest | Secret detection |
| | ModSecurity | Latest | WAF |
| | Falco | Latest | Runtime security |
| **Testing** | JUnit 5 | Latest | Unit testing |
| | Testcontainers | Latest | Integration testing |
| | REST Assured | Latest | API testing |
| | Spring Cloud Contract | Latest | Contract testing |
| | k6 | Latest | Load/stress testing |
| | Playwright | Latest | E2E browser testing |
| | Chaos Mesh | Latest | Chaos engineering |
| | Lighthouse CI | Latest | Frontend performance |
| | pgbench | Bundled | Database benchmarking |

### B: Research References
- Industry Architecture Patterns: `research/industry-architecture-patterns.md`
- Spring Cloud Microservices Patterns: `research/spring-cloud-microservices-architecture-patterns.md`

### C: Stakeholder Input Summary
- User confirmed microservice decomposition (10 services) in Phase 2
- User selected Flutter + Angular + Native Mini Program for frontend (AD-09)
- User confirmed all 23 architecture questions (Phase 3) — 5 manually, 18 via agent recommendation
- All 15 architectural decisions accepted

### D: Alternative Architectures Considered

| Area | Selected | Alternatives Considered | Why Not Selected |
|:---|:---|:---|:---|
| Frontend | Flutter + Angular + Mini Program | Taro (React cross-platform), uni-app, React Native | User preference for Flutter + Angular; Taro's Mini Program restrictions unacceptable |
| Message Queue | RabbitMQ | Apache Kafka, Redis Streams | Kafka over-complex for current scale; Redis Streams lacks routing flexibility |
| API Gateway | Spring Cloud Gateway | Kong, APISIX, Envoy | Spring ecosystem integration; consistent Java stack; avoids polyglot ops |
| APM | Apache SkyWalking | Jaeger, Zipkin, DataDog | Auto-instrumentation via Java agent; lower overhead; open-source; Spring Cloud integration |
| Service Discovery | Nacos | Consul, Eureka, etcd | Dual-purpose (discovery + config); strong Spring Cloud support; proven in Chinese cloud ecosystem |
| Multi-tenancy | Shared DB + RLS | Schema-per-tenant, DB-per-tenant | Simplest ops; RLS provides strong isolation; Hibernate @Filter adds defense-in-depth |
| Offline Storage (Flutter) | Drift | Hive, sqflite | Type-safe ORM for relational data (error notebook has complex queries); better developer experience |
| Spaced Repetition | Fixed intervals (FSRS-ready schema) | SM-2, FSRS from day 1 | Fixed intervals simplest for MVP; schema designed for FSRS evolution; reduces initial complexity |

---

## Deliverables Index

| ID | Deliverable | Path |
|:---|:---|:---|
| OUT-01 | Trigger Config | `config/triggers.yaml` |
| OUT-02 | RACI Config | `config/raci.yaml` |
| OUT-03 | Skills Config | `config/skills.yaml` |
| OUT-04 | Knowledge Domains | `config/knowledge-domains.yaml` |
| OUT-05 | Tools Config | `config/tools.yaml` |
| OUT-06 | MCP Tools Config | `config/mcp-tools.yaml` |
| OUT-07 | Outputs Config | `config/outputs.yaml` |
| OUT-08 | SOP Config | `config/sop.yaml` |
| OUT-09 | DoD Config | `config/dod.yaml` |
| OUT-10 | DoR Config | `config/dor.yaml` |
| OUT-11 | Conversation Log | `conversation-log.md` |
| OUT-12 | Work Log | `work-log.md` |
| OUT-13 | Architecture Design Report | `architecture-design-report.md` |
| OUT-14 | Phase Questions | `phase1-questions.md`, `phase2-questions.md`, `phase3-questions.md` |
| OUT-15 | Research | `research/industry-architecture-patterns.md`, `research/spring-cloud-microservices-architecture-patterns.md` |
| OUT-16 | Diagrams | `diagrams/c4-context.md`, `diagrams/c4-container.md`, `diagrams/c4-component-grading-engine.md`, `diagrams/c4-component-error-notebook.md`, `diagrams/uml-sequence-grading.md`, `diagrams/uml-sequence-review.md`, `diagrams/uml-sequence-guest.md`, `diagrams/deployment.md`, `diagrams/data-flow-grading.md`, `diagrams/data-flow-analytics.md` |
| OUT-17 | Integration View | `diagrams/integration-view.md` |
| OUT-18 | NFR Alignment | `nfr-alignment.md` |
| — | Validated Requirements | `validated-requirements.md` |
