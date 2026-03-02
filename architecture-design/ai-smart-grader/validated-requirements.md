# Validated Requirements — Architecture Design (IA-REQ-001)

## Generated: 2026-03-01
## Status: Confirmed by User (2026-03-01)

---

## Confirmed Context (Phase 1 & 2)

### Microservices (10)
1. `grading-service` — AI grading pipeline, LLM invocation, streaming
2. `image-service` — Upload, validation, preprocessing, object storage
3. `error-notebook-service` — Error collection, classification, spaced repetition, mastery testing
4. `analytics-service` — Pre-computed aggregations, reports, dashboards
5. `user-service` — User profiles, parent-child linking, class management
6. `auth-service` — Multi-method auth (5 providers), JWT, age gate
7. `payment-service` — Payment adapter gateway, order lifecycle, subscriptions
8. `notification-service` — Multi-channel delivery (fanout to workers)
9. `admin-service` — Admin console backend, tenant management, audit
10. `config-service` — Nacos-backed config hot-reload

### Technology Stack
- **Backend**: Java 21 + Spring Boot 3.x + Spring Cloud 2024.x + Spring AI
- **Frontend**: Flutter (iOS/Android) + Angular 18 (Web/H5/Admin) + Native WeChat Mini Program
- **API Gateway**: Spring Cloud Gateway
- **Service Discovery & Config**: Nacos 2.x
- **Database**: PostgreSQL 16 + Row-Level Security
- **Cache**: Redis 7.x
- **Message Queue**: RabbitMQ
- **Object Storage**: MinIO / S3-compatible
- **Search/Logging**: ELK Stack (OpenSearch alternative)
- **CI/CD**: GitLab CI + Argo CD + Helm + Terraform
- **APM**: Apache SkyWalking + Prometheus + Grafana
- **Security**: Spring Security, SonarQube, SpotBugs, OWASP ZAP, Trivy, Gitleaks, ModSecurity, Falco
- **Testing**: JUnit 5, Testcontainers, REST Assured, k6, Playwright, Spring Cloud Contract
- **Secret Management**: HashiCorp Vault
- **Container Registry**: Harbor

### Architectural Decisions (AD-01 to AD-15)
- AD-01: RabbitMQ (message queue)
- AD-02: Spring Cloud Gateway (API gateway)
- AD-03: Apache SkyWalking (APM)
- AD-04: Nacos (service discovery + config)
- AD-05: Separate K8s deployments per region
- AD-06: Server-wins with user override (offline sync)
- AD-07: Redis with content-hash keys (AI result caching)
- AD-08: SSE (Web/App) + WebSocket fallback (Mini Program)
- AD-09: Flutter (mobile) + Angular (web/h5/admin) + Native Mini Program
- AD-10: Angular + NG-ZORRO (admin console)
- AD-11: GitLab CI + Argo CD (CI/CD)
- AD-12: SkyWalking + Prometheus + Grafana + ELK (observability)
- AD-13: OpenAPI 3.0 + code generators (API contract sharing)
- AD-14: k6 + Chaos Mesh + Lighthouse CI (performance testing)
- AD-15: DevSecOps shift-left pipeline (security testing)

---

## Phase 3 Validated Requirements (Pending Confirmation)

### AI Grading Pipeline
| Req ID | Requirement | Decision |
|:---|:---|:---|
| VR-001 | AI model routing strategy | Subject + complexity + user tier (cascade router) |
| VR-002 | Image preprocessing approach | Hybrid: multimodal LLM primary, PaddleOCR fallback for low-confidence handwriting |
| VR-003 | AI result caching | Dual-layer: SHA-256 exact hash + pHash perceptual hash |
| VR-004 | Streaming response parsing | Real-time structured extraction (judgment → answer → explanation → knowledge points) |
| VR-005 | Questions per image capacity | Design for 3-8 questions per image; per-question result granularity |

### Error Notebook & Spaced Repetition
| Req ID | Requirement | Decision |
|:---|:---|:---|
| VR-006 | Spaced repetition algorithm | Fixed intervals for MVP (admin-configured); schema designed for FSRS evolution |
| VR-007 | Practice question generation | Pre-generated asynchronously via RabbitMQ background job |
| VR-008 | Capacity enforcement | Auto-archive oldest mastered entries; upgrade prompt alongside |

### Multi-Tenant & Data
| Req ID | Requirement | Decision |
|:---|:---|:---|
| VR-009 | Multi-tenancy | Shared DB + PostgreSQL Row-Level Security + Hibernate @Filter (defense-in-depth) |
| VR-010 | Knowledge taxonomy storage | PostgreSQL ltree/materialized path for hierarchical queries |
| VR-011 | Analytics aggregation | Dedicated analytics-service with pre-computed aggregations (CQRS read models) |

### Integration & Streaming
| Req ID | Requirement | Decision |
|:---|:---|:---|
| VR-012 | Mini Program streaming | WebSocket for Mini Program; SSE for Web/Flutter |
| VR-013 | Payment integration | Payment gateway aggregator with adapter pattern per provider |
| VR-014 | Notification architecture | RabbitMQ fanout exchange → channel-specific consumer workers |

### Deployment & Operations
| Req ID | Requirement | Decision |
|:---|:---|:---|
| VR-015 | Multi-region strategy | Fully independent K8s clusters per region; same codebase, region-specific Nacos config |
| VR-016 | MVP deployment | All 10 microservices from day one |
| VR-017 | Canary releases | Argo Rollouts with K8s traffic splitting + automated analysis |

### Security & Compliance
| Req ID | Requirement | Decision |
|:---|:---|:---|
| VR-018 | Parental consent verification | All methods (email, SMS OTP, parent login); region default via Nacos |
| VR-019 | Content moderation | Dedicated cloud moderation API (pre-check before LLM) |
| VR-020 | Account deletion | Soft-delete with background cleanup job (7-day cooling) |

### Frontend & Client
| Req ID | Requirement | Decision |
|:---|:---|:---|
| VR-021 | API contract sharing | OpenAPI 3.0 spec + generated clients (Dart, TypeScript, JavaScript) |
| VR-022 | Flutter offline storage | Drift (type-safe SQLite ORM for Dart) |
| VR-023 | Admin Console deployment | Separate Angular SPA deployment with its own gateway route |
