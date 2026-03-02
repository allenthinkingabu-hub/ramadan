# NFR Alignment Note — AI Smart Grader Architecture Design

## Generated: 2026-03-01

---

## NFR-to-Architecture Mapping

### Performance

| NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|
| NFR-01: API response < 500ms (p95) | Spring Cloud Gateway + Nacos service discovery | Direct HTTP routing (no service mesh overhead); Nacos client-side caching reduces discovery latency |
| NFR-02: AI grading first token < 3s | Cascade router + streaming SSE/WebSocket (AD-08) | Model routing selects fastest-capable model; streaming delivers first token immediately without waiting for full result |
| NFR-03: Image upload < 2s | Image Service + MinIO S3 API + CDN | Direct upload to MinIO; CDN for static asset delivery; async processing after upload acknowledgement |
| NFR-04: Dashboard data freshness ≤ 5 min (teacher), ≤ 1 min (admin) | CQRS read models + pre-computed aggregations (VR-011) | Analytics service consumes events and maintains pre-computed aggregation tables; Redis cache with 5-min TTL for teacher, 1-min for admin |
| AI result caching (60-80% cost reduction target) | Dual-layer cache: SHA-256 + pHash in Redis (VR-003, AD-07) | Exact hash catches identical re-submissions; perceptual hash catches re-photographed same page. TTL: 24h. |

### Scalability

| NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|
| NFR-05: 10,000 concurrent users | Kubernetes HPA + 10 microservices (AD-05, VR-016) | Independent scaling per service; Grading Service scales 3-10 pods based on CPU + queue depth |
| NFR-06: 100 concurrent grading requests | Grading Service HPA + LLM connection pooling | Horizontal pod autoscaling; connection pool per LLM provider; RabbitMQ absorbs burst via queuing |
| Database scalability | PostgreSQL read replicas + connection pooling (HikariCP) | Write to primary; analytics and reporting read from replicas; HikariCP manages connection efficiency |
| Storage scalability | MinIO cluster (4 nodes) + S3-compatible API | Distributed object storage with erasure coding; scales by adding nodes |

### Availability & Reliability

| NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|
| NFR-07: 99.9% uptime (excluding planned maintenance) | Kubernetes + PodDisruptionBudgets + multi-pod deployments | All services deploy ≥2 pods; PDB ensures min 1 pod during rolling updates; zero-downtime deployments via Argo Rollouts |
| NFR-08: Zero-downtime deployments | Argo Rollouts canary strategy (VR-017, AD-17) | Canary releases with automated analysis; traffic gradually shifted from 10% → 50% → 100% based on SkyWalking metrics |
| Infrastructure HA | PostgreSQL streaming replication, Redis Sentinel, RabbitMQ cluster, Nacos cluster | All stateful infrastructure runs in clustered/replicated mode with automatic failover |
| LLM provider availability | Cascade router with multi-provider fallback | Circuit breaker per LLM provider; automatic failover to secondary provider on failure |

### Security

| NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|
| NFR-09: Data encryption at rest and in transit | TLS 1.3 (transit) + PostgreSQL pgcrypto + MinIO server-side encryption | All communication over TLS; PII columns encrypted; object storage encrypted at rest |
| NFR-10: RBAC with 5 user roles | Spring Security + JWT + API Gateway enforcement | JWT contains role claim; gateway injects X-User-Role header; services enforce role-based access |
| NFR-11: Multi-tenant data isolation | PostgreSQL Row-Level Security + Hibernate @Filter (VR-009) | Defense-in-depth: RLS policies at DB level + @Filter at ORM level; tenant_id in every query |
| NFR-12: GDPR/PIPL compliance | Independent regional clusters + 7-day soft-delete (VR-015, VR-020) | No cross-region data flow; account deletion with 7-day cooling period; data export API |
| NFR-13: Content moderation for minors | Dedicated moderation API pre-gate (VR-019) | All uploaded images screened before LLM processing; rejected content logged for audit |
| NFR-14: Age verification and parental consent | Multi-method consent (email, SMS OTP, parent login) (VR-018) | Age gate on registration; region-appropriate consent method via Nacos config |
| Secret management | HashiCorp Vault + sidecar injection | Secrets never in config files; Vault injects at runtime via K8s init container |
| DevSecOps pipeline | SAST (SonarQube) + DAST (OWASP ZAP) + SCA (Trivy) + Gitleaks (AD-15) | Shift-left security: scans run in CI pipeline; vulnerabilities block deployment |
| Runtime security | Falco + ModSecurity WAF | WAF at ingress; Falco monitors container runtime for anomalous behavior |

### Resiliency

| NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|
| NFR-15: Graceful degradation | Circuit breakers + fallback strategies (Resilience4j) | LLM failure → fallback to secondary provider; cache failure → bypass cache; moderation failure → queue for review |
| NFR-16: Message delivery guarantee | RabbitMQ publisher confirms + consumer acknowledgement + DLQ | At-least-once delivery; failed messages routed to Dead Letter Queue for manual intervention |
| NFR-17: Offline capability | Flutter Drift (SQLite) + server-wins sync (VR-022, AD-06) | Error notebook available offline via local Drift DB; sync on reconnect with server-wins + user override for conflicts |
| Data consistency | Event-driven eventual consistency + idempotent consumers | Services communicate via events; consumers are idempotent (deduplication by event ID) |

### Observability

| NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|
| NFR-18: Distributed tracing | Apache SkyWalking (AD-03, AD-12) | Auto-instrumented via SkyWalking Java agent; trace ID propagated across all services and RabbitMQ messages |
| NFR-19: Centralized logging | ELK Stack (Elasticsearch + Fluentd + Kibana) | Fluentd DaemonSet collects logs; structured JSON logging; Kibana dashboards per service |
| NFR-20: Metrics and alerting | Prometheus + Grafana + Alertmanager | Custom metrics (grading latency, cache hit rate, LLM errors); alert rules for SLA breaches |
| NFR-21: Health checks | Spring Boot Actuator + K8s probes | Liveness and readiness probes; /actuator/health endpoint; Nacos health check |

### Maintainability

| NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|
| Configuration hot-reload | Nacos 2.x config center (AD-04) | Config changes pushed to services without restart; namespace/group organization for multi-env |
| API contract management | OpenAPI 3.0 + code generators (AD-13, VR-021) | Single source of truth for API contracts; auto-generated client SDKs for 3 codebases |
| A/B testing for AI prompts | Admin Service prompt management + variant routing | Prompt templates managed centrally; A/B variants selected by cascade router |
| Canary releases | Argo Rollouts + SkyWalking metrics analysis (VR-017) | Automated canary promotion/rollback based on error rate and latency metrics |

---

## Constraints

| Constraint ID | Description | Impact | Mitigation |
|:---|:---|:---|:---|
| CON-001 | WeChat Mini Program does not support SSE | Must maintain dual streaming protocol (SSE + WebSocket) | API Gateway transparently routes Mini Program traffic to WebSocket; shared backend streaming logic |
| CON-002 | LLM API rate limits and cost | Grading throughput capped by provider limits; costs scale with usage | Dual-layer caching (60-80% cost reduction); cascade routing selects cost-effective models; rate limiting at gateway |
| CON-003 | GDPR/PIPL requires data residency | No cross-region data flow; independent infrastructure per region | Fully independent K8s clusters; same codebase, region-specific Nacos config |
| CON-004 | PostgreSQL single-database multi-tenancy | Must ensure tenant isolation at every query | Defense-in-depth: RLS + Hibernate @Filter + gateway tenant header injection |
| CON-005 | 3 separate frontend codebases | Higher maintenance cost; risk of API contract drift | OpenAPI 3.0 spec as single source of truth; auto-generated SDKs; contract testing in CI |
| CON-006 | Spring Cloud ecosystem dependency | Tightly coupled to Spring ecosystem | Mitigated by industry-standard components; service interfaces are protocol-based (HTTP, AMQP) not framework-coupled |
| CON-007 | MinIO operational complexity | MinIO cluster requires operational expertise | Can swap to cloud-managed S3 (AWS S3, Aliyun OSS) via S3-compatible API without code changes |
| CON-008 | Content moderation for educational content | Over-aggressive moderation may block legitimate exercise images | Configurable moderation sensitivity thresholds; manual review queue for borderline cases |

---

## Assumptions

| Assumption ID | Description | Risk if Invalid |
|:---|:---|:---|
| ASM-001 | LLM providers (OpenAI, Claude, ZhiPu) will maintain current API stability and pricing | If APIs change significantly, Spring AI abstraction + adapter pattern limits blast radius to LLM Invoker component |
| ASM-002 | Average 3-8 questions per uploaded image | If images contain significantly more questions (>15), grading latency increases; may need batch splitting strategy |
| ASM-003 | PostgreSQL RLS provides sufficient tenant isolation for compliance | If auditors require stronger isolation, must migrate to schema-per-tenant (higher operational cost) |
| ASM-004 | RabbitMQ throughput sufficient for event processing (target: 10K msg/s) | If exceeded, consider sharding exchanges or migrating to Apache Kafka |
| ASM-005 | PaddleOCR accuracy sufficient for handwriting recognition fallback | If accuracy insufficient for specific handwriting styles, may need fine-tuned OCR model or additional LLM re-grading pass |
| ASM-006 | Device fingerprinting provides adequate guest tracking | If users clear browser data / reinstall app frequently, guest quota enforcement weakens; acceptable for MVP |
| ASM-007 | Fixed-interval spaced repetition acceptable for MVP | If user retention data shows suboptimal learning outcomes, must accelerate FSRS algorithm adoption |
| ASM-008 | k6 load testing accurately simulates production traffic patterns | If production traffic differs significantly from test patterns, must update k6 scripts with production traffic analysis |
| ASM-009 | Single Redis Sentinel cluster sufficient for cache + session + rate limiting workloads | If Redis becomes bottleneck, split into dedicated clusters per workload (cache cluster, session cluster, rate-limit cluster) |
| ASM-010 | Team has sufficient Kubernetes operational expertise | If not, consider managed K8s (EKS, GKE, ACK) to reduce operational burden |
