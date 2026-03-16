# Skills & Knowledge Base — Transformation Target Current State Analysis (SA-TRF-001)

> Configurable skills and knowledge base for the Transformation Target Current State Analysis AI Agent.
> Edit this file to add or remove skills and knowledge items as requirements evolve.

---

## Agent Skills

The agent must possess the following skills:

| # | Skill | Description |
|---|-------|-------------|
| 1 | Code Reading & Deep Comprehension | Read and understand source code across languages (Java, Python, TypeScript, Go, etc.), including complex control flow, design patterns, and implicit behaviors |
| 2 | Dependency Graph Tracing | Trace both inbound dependencies (who calls/uses the target) and outbound dependencies (what the target calls/uses), including transitive dependencies |
| 3 | API Contract & Interface Analysis | Identify and document all public APIs, event contracts, shared interfaces, and service boundaries exposed or consumed by the target |
| 4 | Data Flow & Event Tracing | Map all data flows through the target: request/response paths, event publishing/subscription, shared state mutations, database read/write patterns |
| 5 | Test Coverage Assessment | Locate and evaluate existing unit, integration, and E2E tests for the target; classify coverage level; identify untested code paths |
| 6 | Technical Debt Identification | Recognize and classify code smells (Fowler's catalogue), anti-patterns, TODO/FIXME markers, hardcoded values, missing abstractions, and dead code |
| 7 | Anti-Pattern Recognition | Identify GoF and architectural anti-patterns: God Object, Spaghetti Code, Shotgun Surgery, Feature Envy, Data Clump, etc. |
| 8 | Configuration & Environment Dependency Mapping | Identify all environment variables, feature flags, external configuration keys, and deployment-specific settings consumed by the target |
| 9 | Coupling Metrics Analysis | Calculate or estimate afferent coupling (Ca), efferent coupling (Ce), instability index (I = Ce/(Ca+Ce)), and identify coupling hotspots |
| 10 | Refactoring Risk Assessment | Assess transformation risk based on coupling, test coverage gaps, shared state, external contracts, and blast radius |
| 11 | Incremental Analysis | Compare current target state against previous analysis results to produce delta reports and avoid redundant investigation |
| 12 | Cross-Target Pattern Recognition | Apply pattern knowledge from previously analyzed components in the same project to accelerate hypothesis-driven analysis |

---

## Knowledge Base

The agent must have knowledge of the following domains:

| # | Knowledge Area | Specific Items |
|---|---------------|----------------|
| 1 | Software Design Patterns — GoF | Creational: Factory, Builder, Singleton, Prototype, Abstract Factory; Structural: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy; Behavioral: Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor |
| 2 | SOLID Principles | Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion — with indicators of violation in code |
| 3 | Clean Code Principles | Meaningful names, small functions, comments as last resort, formatting, error handling, unit tests, classes, systems, emergence, concurrency |
| 4 | Technical Debt Taxonomy | Cunningham's original concept; Fowler's quadrant (Reckless/Prudent × Deliberate/Inadvertent); McConnell's debt types |
| 5 | Code Smell Catalogue | Fowler's 24 smells: Bloaters (Long Method, Large Class, Primitive Obsession, Long Parameter List, Data Clumps); Object-Orientation Abusers; Change Preventers; Dispensables; Couplers |
| 6 | Refactoring Catalogue | Fowler's Refactoring 2nd Ed.: Extract Method/Class/Function, Move Method/Field, Rename, Inline, Replace Conditional with Polymorphism, Introduce Parameter Object, etc. |
| 7 | Coupling & Cohesion Metrics | Afferent coupling (Ca), Efferent coupling (Ce), Instability (I), Abstractness (A), Distance from Main Sequence (D), LCOM variants |
| 8 | API Contract Principles | REST (OpenAPI), GraphQL schema contracts, gRPC .proto definitions, Event contracts (AsyncAPI, CloudEvents), Backward/Forward compatibility |
| 9 | Test Coverage Standards | Line coverage, branch coverage, mutation coverage; industry thresholds (80% line as baseline); test pyramid (unit/integration/E2E ratios) |
| 10 | Dependency Injection & Inversion | Constructor injection, setter injection, field injection; IoC containers; impact on testability and coupling |
| 11 | Architectural Layering Patterns | Layered Architecture, Hexagonal (Ports & Adapters), Clean Architecture, DDD (Domain/Application/Infrastructure/Presentation), MVC, CQRS, Event Sourcing |
| 12 | Transformation Patterns | Strangler Fig, Branch by Abstraction, Feature Toggle, Expand-Contract (parallel change), Mikado Method for safe refactoring sequences |
