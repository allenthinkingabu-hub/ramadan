# Architect SOP: New Feature Design on an Existing System

## Overview: Two Phases, Six Steps

```
┌─────────────────────────────────────────────────────────┐
│         Phase 1: System Discovery (As-Is Analysis)      │
│                                                         │
│  Step 1: Code Archaeology — Understand the current state│
│  Step 2: Architecture Recovery — Reverse-engineer the   │
│          full architecture landscape                    │
│  Step 3: Tech Debt & Risk Assessment — Identify hazards │
│                                                         │
├─────────────────────────────────────────────────────────┤
│         Phase 2: Requirements & Solution Design         │
│                        (To-Be Design)                   │
│                                                         │
│  Step 4: Requirements Alignment — Understand what the   │
│          customer truly needs                           │
│  Step 5: Architecture Design — Design new features on   │
│          top of the existing system                     │
│  Step 6: Review & Delivery — Ensure the solution is     │
│          implementable                                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Phase 1: System Discovery (As-Is Analysis)

### Step 1: Code Archaeology — Understand the Current State

**Objective**: Rapidly build a holistic understanding of the existing system.

| Activity | Approach | Deliverable |
|----------|----------|-------------|
| **1.1 Project Structure Scan** | Analyze directory structure, module decomposition, package dependencies; identify layering patterns (MVC / DDD / Hexagonal, etc.) | Project structure tree + module relationship diagram |
| **1.2 Technology Stack Inventory** | Catalog language versions, framework versions, middleware, databases, third-party services, CI/CD toolchain | Technology stack inventory table |
| **1.3 Entry-Point Tracing** | Trace core business flows from API entry points (Controller / Router) to understand the full request lifecycle | Core business flow diagrams (3-5 main chains) |
| **1.4 Data Model Analysis** | Analyze database schemas, ORM mappings, entity relationships; understand the core domain model | ER diagram + domain model overview |
| **1.5 Configuration & Environments** | Catalog configuration files, environment variables, feature flags, multi-environment differences | Configuration matrix table |

**Key Principle**: Go broad before going deep — spend 20% of the time to gain 80% of the global picture, then dive into the modules relevant to the new feature.

---

### Step 2: Architecture Recovery — Reverse-Engineer the Full Architecture Landscape

**Objective**: Reverse-engineer the actual system architecture from code (not from what the documentation claims).

| Activity | Approach | Deliverable |
|----------|----------|-------------|
| **2.1 C4 Context Diagram** | Identify interactions between the system, external systems, and user roles | C4 Level 1 — Context diagram |
| **2.2 C4 Container Diagram** | Identify independently deployable units within the system (Web App, API, DB, MQ, etc.) | C4 Level 2 — Container diagram |
| **2.3 C4 Component Diagram** | For containers affected by the new feature, identify internal components and their responsibilities | C4 Level 3 — Component diagram |
| **2.4 Integration Mapping** | Catalog inter-system communication patterns (synchronous REST/gRPC, asynchronous MQ, file/batch) | Integration relationship matrix |
| **2.5 Deployment Architecture** | Analyze deployment model (K8s / VM / Serverless), network topology, CDN, load balancer | Deployment architecture diagram |

**Key Principle**: **Code is the single source of truth** — legacy documentation may be referenced but must not be trusted. The actual behavior of the code takes precedence.

---

### Step 3: Tech Debt & Risk Assessment — Identify Hazards

**Objective**: Identify the landmines that could be hit when building new features on the existing system.

| Activity | Approach | Deliverable |
|----------|----------|-------------|
| **3.1 Code Quality Scan** | Use static analysis tools (e.g., SonarQube) or manual review to identify high-complexity, high-coupling areas | Quality heatmap |
| **3.2 Tech Debt Inventory** | Identify outdated dependencies, hard-coded values, missing abstractions, design-principle violations | Tech debt list (prioritized by impact) |
| **3.3 Test Coverage Assessment** | Evaluate unit/integration test coverage; identify weakly tested areas | Test coverage report |
| **3.4 Performance Bottleneck Prediction** | Analyze slow queries, N+1 problems, memory leak risks, concurrency bottlenecks | Performance risk list |
| **3.5 Security Risk Screening** | Check for OWASP Top 10 vulnerabilities, dependency CVEs, sensitive data exposure | Security risk list |

**Key Principle**: Not all tech debt needs to be paid off — focus only on tech debt that **intersects** with the new feature scope.

---

## Phase 2: Requirements & Solution Design (To-Be Design)

### Step 4: Requirements Alignment — Understand What the Customer Truly Needs

**Objective**: Translate customer requirements into technically actionable design inputs.

| Activity | Approach | Deliverable |
|----------|----------|-------------|
| **4.1 Requirements Clarification** | Walk through each requirement with PM/BA; distinguish "must-have" from "nice-to-have"; eliminate ambiguity | Requirements clarification log |
| **4.2 Scenario-Based Analysis** | Decompose requirements into user stories, use cases, and key scenarios (including exception scenarios) | Use case diagram + scenario list |
| **4.3 NFR Extraction** | Define performance targets (TPS / latency), availability (SLA), security, and compliance requirements | NFR requirements matrix |
| **4.4 Constraint Identification** | Identify time constraints, budget constraints, team capability constraints, technology constraints | Constraint list |
| **4.5 Impact Analysis** | Assess the impact of the new feature on existing modules — what needs modification, what can be reused | Impact analysis matrix |

**Key Principle**: **Business goals lie behind every requirement** — architects must understand the "why" to design the right solution.

---

### Step 5: Architecture Design — Design New Features on the Existing System

**Objective**: Design an implementable solution that respects the existing architecture.

| Activity | Approach | Deliverable |
|----------|----------|-------------|
| **5.1 Option Evaluation** | Propose 2-3 viable options; compare across cost, risk, timeline, and extensibility dimensions | Option comparison matrix |
| **5.2 Architecture Design** | For the selected option, produce C4 diagrams (incremental changes), sequence diagrams, data flow diagrams | Architecture design document + diagram set |
| **5.3 Interface Design** | Define API contracts, message formats, error codes, versioning strategy | API Spec (OpenAPI / AsyncAPI) |
| **5.4 Data Design** | Design new/changed data models and data migration plans | Data model changes + migration script design |
| **5.5 NFR Alignment** | Verify each architectural decision against NFRs; flag risks and mitigation measures | NFR alignment table |
| **5.6 Tech Debt Remediation Strategy** | Decide which tech debts must be addressed in this iteration and which can be deferred | Tech debt remediation plan |

**Key Principle**: **Incremental evolution over big-bang rewrite** — unless the existing architecture is fundamentally incapable, prefer extending it over replacing it.

---

### Step 6: Review & Delivery — Ensure the Solution Is Implementable

**Objective**: Validate the design through reviews and hand off to the development team.

| Activity | Approach | Deliverable |
|----------|----------|-------------|
| **6.1 Internal Review** | Architecture team peer review — check consistency, completeness, feasibility | Review feedback log |
| **6.2 External Review (ARB)** | Submit to the Architecture Review Board for formal approval | ARB approval record |
| **6.3 Technical Briefing** | Present the architecture design to the development team — explain intent, key decisions, and caveats | Briefing notes |
| **6.4 Task Decomposition Support** | Assist the Tech Lead in breaking down the architecture design into executable development tasks | Task decomposition list |
| **6.5 Architecture Guardianship** | Continuously review during development to ensure implementation does not deviate from the design | Code review records |

**Key Principle**: **Architecture design is not a one-time handoff** — the architect must continuously guard and adaptively adjust during development.

---

## Summary: Core Mindset

```
  Discovery Questions                Design Questions
  ┌──────────────────────┐          ┌──────────────────────┐
  │ What does the system │          │ What does the        │
  │ look like today?     │          │ customer need?       │
  │                      │          │                      │
  │ What is the real     │  ──→     │ What is the best     │
  │ architecture?        │          │ approach?            │
  │                      │          │                      │
  │ What are the risks?  │          │ How do we ensure     │
  │                      │          │ successful delivery? │
  └──────────────────────┘          └──────────────────────┘
```

> **One-line summary**: Start with code archaeology to recover the real architecture, then use impact analysis to bridge old and new requirements, and finally apply incremental evolution to complete the design.
