# Knowledge Base Checklist

## Role: Technical Lead (TL) — Technical Design & Solution Design Agent

### 1. Architecture & Design Knowledge

| # | Knowledge Domain | Key Topics | Priority |
|:--|:--|:--|:--|
| K1 | **Software Architecture Patterns** | Layered, Hexagonal, Event-Driven, CQRS, Microservices, Monolithic, Serverless, Pipe-and-Filter | Critical |
| K2 | **Design Patterns (GoF)** | Creational (Factory, Builder, Singleton), Structural (Adapter, Facade, Proxy), Behavioral (Strategy, Observer, Command) | Critical |
| K3 | **Enterprise Integration Patterns** | Message Channel, Message Router, Message Translator, Message Endpoint, Publish-Subscribe, Request-Reply | High |
| K4 | **Cloud-Native Patterns** | Sidecar, Ambassador, Circuit Breaker, Strangler Fig, Saga, Outbox, CQRS+ES | High |
| K5 | **API Design Principles** | REST (Richardson Maturity Model), gRPC, GraphQL, API versioning, HATEOAS, OpenAPI/Swagger | Critical |

### 2. Modeling & Diagramming Knowledge

| # | Knowledge Domain | Key Topics | Priority |
|:--|:--|:--|:--|
| K6 | **C4 Model** | Context diagrams, Container diagrams, Component diagrams, notation rules, abstraction levels | Critical |
| K7 | **UML Sequence Diagrams** | Lifelines, activation bars, synchronous/asynchronous messages, combined fragments (alt, loop, opt, par, ref) | Critical |
| K8 | **UML Component Diagrams** | Provided/required interfaces, dependency arrows, stereotypes, packages | High |
| K9 | **Entity-Relationship Modeling** | Entities, relationships, cardinality, normalization (1NF-3NF), denormalization strategies | High |
| K10 | **State Machine Diagrams** | States, transitions, guards, actions, composite states | Medium |

### 3. Technology Domain Knowledge

| # | Knowledge Domain | Key Topics | Priority |
|:--|:--|:--|:--|
| K11 | **Database Technologies** | RDBMS (PostgreSQL, MySQL), NoSQL (MongoDB, Redis, DynamoDB), NewSQL, time-series databases | High |
| K12 | **Messaging Systems** | Kafka, RabbitMQ, AWS SQS/SNS, Azure Service Bus — patterns, guarantees, partitioning | High |
| K13 | **Caching Strategies** | In-memory (Redis, Memcached), CDN, application-level, cache invalidation patterns | High |
| K14 | **Authentication & Authorization** | OAuth 2.0, OpenID Connect, JWT, RBAC, ABAC, API keys, mTLS | High |
| K15 | **Container & Orchestration** | Docker, Kubernetes, service mesh (Istio), container networking | Medium |

### 4. Quality & Non-Functional Knowledge

| # | Knowledge Domain | Key Topics | Priority |
|:--|:--|:--|:--|
| K16 | **Performance Engineering** | Latency budgets, throughput calculation, bottleneck analysis, load testing approaches | High |
| K17 | **Security Design** | OWASP Top 10, threat modeling (STRIDE), encryption at rest/in transit, secrets management | High |
| K18 | **Resilience & Reliability** | Failure modes, redundancy, graceful degradation, chaos engineering principles, SLA/SLO/SLI | High |
| K19 | **Scalability** | Horizontal vs vertical scaling, sharding, read replicas, auto-scaling policies | High |
| K20 | **Observability** | Distributed tracing (OpenTelemetry), structured logging, metrics (RED/USE methods), alerting | Medium |

### 5. Process & Methodology Knowledge

| # | Knowledge Domain | Key Topics | Priority |
|:--|:--|:--|:--|
| K21 | **arc42 Documentation Template** | 12 sections, when to use each, how to structure building block views | Critical |
| K22 | **Architecture Decision Records (ADR)** | ADR structure (Title, Status, Context, Decision, Consequences), when to write an ADR | High |
| K23 | **RFC Process** | Request for Comments workflow, review lifecycle, stakeholder alignment | Medium |
| K24 | **Technical Design Review** | Review checklist categories, ATAM method, quality attribute utility trees | Medium |
| K25 | **Agile / Lean Principles** | Iterative design, just-enough documentation, evolutionary architecture | Medium |

### 6. Documentation Framework Knowledge

| # | Knowledge Domain | Key Topics | Priority |
|:--|:--|:--|:--|
| K26 | **Mermaid Syntax** | Flowcharts, sequence diagrams, class diagrams, C4 diagrams, state diagrams, ER diagrams | Critical |
| K27 | **PlantUML Syntax** | C4 macros, sequence diagram syntax, component diagram syntax | High |
| K28 | **Markdown Best Practices** | Tables, code blocks, cross-references, document structure, front matter | High |
| K29 | **IEEE 1016 SDD Standard** | Software Design Description structure, views, viewpoints, stakeholder concerns | Low |
| K30 | **ISO/IEC/IEEE 42010** | Architecture description framework, architecture viewpoints, model kinds | Low |

## Configuration Notes

- Priority levels: Critical → High → Medium → Low
- "Critical" knowledge is required for basic operation — agent cannot proceed without it
- "High" knowledge is needed for most tasks — agent should load relevant references as needed
- "Medium" and "Low" knowledge is supplementary — loaded only for specific scenarios
- Add new domains by appending rows to the appropriate table
