# Industry Architecture Patterns for AI-Powered EdTech Platforms (2025-2026)

## Research Date: 2026-03-01
## Context: AI Smart Grader — IA-REQ-001, Phase 3 Research
## Scope: Architecture patterns and best practices across six key areas

---

## Table of Contents

1. [AI/LLM Grading Pipeline Architecture](#1-aillm-grading-pipeline-architecture)
2. [Spaced Repetition System Architecture](#2-spaced-repetition-system-architecture)
3. [Multi-Tenant SaaS Architecture for Education](#3-multi-tenant-saas-architecture-for-education)
4. [Offline-First Mobile Architecture](#4-offline-first-mobile-architecture)
5. [Streaming Architecture (SSE/WebSocket)](#5-streaming-architecture-ssewebsocket)
6. [Cost Optimization for LLM APIs](#6-cost-optimization-for-llm-apis)

---

## 1. AI/LLM Grading Pipeline Architecture

### 1.1 Industry Landscape

Major platforms in AI-powered homework/grading:

| Platform | Owner | Users | Core Approach |
|:---|:---|:---|:---|
| Gauth (Gauthmath) | ByteDance | 200M+ | Camera OCR -> LLM -> step-by-step + human tutor fallback (5% of queries) |
| Photomath | Google | 300M+ | Camera OCR -> animated step-by-step solutions, strong pedagogical sequencing |
| Question.ai | Zuoyebang (China) | 100M+ | OCR -> LLM grading + question bank matching |
| Squirrel AI | Yixue Group | 24M+ | Knowledge graph (10,000+ nano-level knowledge points) -> adaptive learning |
| Mathway/Symbolab | Chegg | 100M+ | Text/camera input -> symbolic solver + LLM explanation |

**Key takeaway**: The pre-GenAI pipeline was `camera -> OCR -> question bank matching -> human tutor fallback`. Modern 2025 pipelines have shifted to `camera -> multimodal LLM (or OCR + LLM) -> generative step-by-step solution -> optional human escalation`.

### 1.2 Pattern: Multimodal OCR-to-LLM Pipeline

**Pattern Name**: Image-to-Insight Pipeline (OCR-LLM Chain)

**Description**: A staged pipeline that converts student homework images into structured grading output via OCR preprocessing followed by LLM reasoning.

**Pipeline Stages**:

```
[Client] Image Upload
    |
    v
[Stage 1] Image Preprocessing
    - Image quality validation (blur detection, resolution check)
    - Orientation correction, deskewing
    - Content moderation (safety filter)
    |
    v
[Stage 2] OCR / Text Extraction
    Option A: Dedicated OCR (Tesseract, PaddleOCR v5, Google Vision)
    Option B: Multimodal LLM direct (GPT-4o, Claude Vision)
    Option C: Hybrid — OCR for text-heavy, multimodal for mixed content
    |
    v
[Stage 3] Question Segmentation
    - Detect individual question boundaries
    - Associate question numbers with content
    - Separate student answers from printed questions
    |
    v
[Stage 4] LLM Grading / Analysis
    - Per-question evaluation against rubric
    - Step-by-step solution generation
    - Error categorization and knowledge point tagging
    |
    v
[Stage 5] Response Assembly & Streaming
    - Structure output (score, explanation, knowledge points)
    - Stream via SSE/WebSocket to client
    - Persist results to database
```

**When to use**: Any platform processing student-submitted image-based homework or assessments.

**Trade-offs**:

| Approach | Latency | Accuracy | Cost | Best For |
|:---|:---|:---|:---|:---|
| Dedicated OCR + LLM | Higher (two stages) | Best for handwritten text | Lower (text-only LLM input) | Handwritten homework, math equations |
| Multimodal LLM only | Lower (single call) | Better for visual/diagram content | Higher (image tokens expensive) | Mixed text+diagram content |
| Hybrid routing | Medium | Best overall | Medium | Production systems at scale |

**Reference**: Research shows OCR-LLM pipelines achieve comparable pedagogical value to multimodal LLMs on text-centric content at much lower cost, while multimodal LLMs excel on visually dense slides (source: [Integrating Generative AI into Cybersecurity Education](https://arxiv.org/html/2509.02998)).

### 1.3 Pattern: Multi-Agent Grading Framework (GradeOpt)

**Pattern Name**: Multi-Agent LLM Grading with Self-Reflection

**Description**: Uses multiple LLM agents with distinct roles — Grader, Reflector, Refiner — to improve grading accuracy through iterative self-correction.

**Architecture**:

```
[Student Submission]
    |
    v
[Grader Agent] -- initial grading against rubric
    |
    v
[Reflector Agent] -- reviews grading for errors/inconsistencies
    |
    v
[Refiner Agent] -- optimizes rubric/guidelines based on reflection
    |
    v
[Final Grade + Feedback]
```

**When to use**: High-stakes assessments, essay grading, or anywhere grading accuracy is critical and latency tolerance is higher.

**Trade-offs**: Higher accuracy but 3x LLM API cost per submission; best suited for asynchronous grading rather than real-time.

**Reference**: [GradeOpt — LLM-Powered Automatic Grading Framework](https://educationaldatamining.org/EDM2025/proceedings/2025.EDM.long-papers.80/index.html)

### 1.4 Pattern: Microservices File Processing Pipeline

**Pattern Name**: Event-Driven Microservices for EdTech File Processing

**Description**: Decomposes the grading pipeline into six independent, event-driven microservices connected via message broker (Kafka/RabbitMQ).

**Services**:

```
1. Ingestion Service    - Receives uploads, assigns job ID, emits event
2. Validation Service   - File type, size, content safety checks
3. Transformation Svc   - Image normalization, format conversion
4. OCR Service          - Text extraction (handwritten + printed)
5. Metadata Service     - Question detection, knowledge point tagging
6. Delivery Service     - Assembles final result, triggers streaming
```

**When to use**: High-throughput platforms needing to handle deadline spikes (exam submission rushes), diverse file types, and strict privacy requirements.

**Trade-offs**: Higher operational complexity but excellent scalability; each service scales independently based on bottleneck.

**Reference**: [Microservices Architecture for Modular EdTech File Processing](https://dev.to/ideradevtools/microservices-architecture-for-modular-edtech-file-processing-268n)

### 1.5 Pattern: Human-in-the-Loop Escalation (Gauth Model)

**Pattern Name**: AI-First with Human Tutor Escalation

**Description**: AI handles ~95% of queries; complex or low-confidence queries (bottom ~5%) are escalated to human experts. Gauth's network includes tutors from the US, India, and the Philippines.

**Decision Logic**:

```
IF confidence_score >= threshold AND complexity <= max_ai_complexity:
    return AI_generated_solution
ELIF subject in [advanced_topics] OR confidence_score < threshold:
    route_to_human_tutor_queue(priority=complexity)
    return streaming_human_response
```

**When to use**: Consumer-facing education apps where quality guarantee matters more than cost per query.

**Trade-offs**: Requires maintaining a tutor workforce; adds variable human latency; but builds trust and handles edge cases AI cannot.

**Reference**: [Gauth AI Study Companion Analysis](https://www.bbntimes.com/technology/gauth-vs-photomath-the-definitive-battle-of-ai-homework-helpers-in-2025)

### 1.6 OCR Technology Selection (2025)

| Engine | Architecture | Parameters | Strengths | Best For |
|:---|:---|:---|:---|:---|
| PaddleOCR v5 | Transformer (SVTR) | Lightweight | Chinese+English, mobile-friendly | Multi-language education |
| Nanonets OCR 2 | Fine-tuned Qwen2.5-VL | 4B | LLM-ready markdown output | Document-heavy workflows |
| Tesseract 5 | LSTM-based | N/A | Open source, well-documented | Budget-constrained, text-only |
| Google Vision API | Cloud-based | N/A | Highest accuracy, math symbols | Production, math OCR |
| GPT-4o / Claude Vision | Multimodal LLM | Large | Direct image understanding | Mixed text+diagram content |

**Reference**: [7 Best Open-Source OCR Models 2025](https://www.e2enetworks.com/blog/complete-guide-open-source-ocr-models-2025)

---

## 2. Spaced Repetition System Architecture

### 2.1 Algorithm Comparison

| Algorithm | Year | Parameters | Trainable | Personalization | Efficiency vs SM-2 |
|:---|:---|:---|:---|:---|:---|
| SM-2 (SuperMemo 2) | 1990 | ease_factor, interval, repetitions | No (manual tuning) | Low (one ease factor per card) | Baseline |
| SM-17 (SuperMemo 17) | 2016 | Proprietary | Yes | High | ~20-30% fewer reviews |
| FSRS (v6) | 2024 | 21 weights | Yes (ML-based) | High (per-user optimization) | 20-30% fewer reviews |
| Duolingo HLR | 2016 | Half-life per word | Yes (regression) | Medium (per-word) | Research-grade |
| Duolingo Birdbrain v2 | 2020+ | Logistic regression | Yes | Very High (per-exercise) | Production-proven at 1.25B exercises/day |

### 2.2 Pattern: FSRS (Free Spaced Repetition Scheduler)

**Pattern Name**: DSR Memory Model with ML Optimization

**Description**: FSRS models memory using three variables — Difficulty (D), Stability (S), and Retrievability (R) — and uses 21 trainable parameters optimized via machine learning on the user's review history.

**Core Model**:

```
Memory State = {D, S, R}

- Retrievability (R): P(recall) at time t = (1 + t/(9*S))^(-1)
  - Decreases over time since last review
  - When R drops to desired_retention (default 0.9), schedule review

- Stability (S): Time in days for R to fall from 100% to 90%
  - Increases with successful reviews
  - Growth rate depends on D, current S, R at review time, and rating

- Difficulty (D): 1-10 scale, inherent complexity of the card
  - Affects how fast S grows after review
  - Updated based on review rating (Again/Hard/Good/Easy)
```

**Scheduling Algorithm**:

```
1. User reviews card, provides rating (1=Again, 2=Hard, 3=Good, 4=Easy)
2. Update D based on rating
3. Calculate new S based on (D, old_S, R_at_review, rating)
4. Calculate next review date: t = S * ((1/desired_retention)^(1/decay) - 1)
5. Store updated memory state (D, S) and schedule due date
```

**When to use**: Any flashcard or review-based learning system. FSRS is the recommended algorithm for new systems as of 2025 — it empirically outperforms SM-2 and is open source.

**Trade-offs**:

| Aspect | SM-2 | FSRS |
|:---|:---|:---|
| Complexity | Simple, easy to understand | Moderately complex |
| Customizability | Many user-tunable params | Few (ML handles it) |
| Accuracy | Baseline | 20-30% fewer reviews for same retention |
| Cold Start | Immediate (fixed params) | Needs ~1000 reviews for optimization |
| Implementation | Trivial | Requires ML optimizer |
| License | Public domain | MIT (open source) |

**Reference**: [FSRS GitHub](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler), [ABC of FSRS](https://github.com/open-spaced-repetition/fsrs4anki/wiki/abc-of-fsrs)

### 2.3 Database Schema Pattern for FSRS

**Pattern Name**: Card-Review-State Schema

**PostgreSQL Schema**:

```sql
-- Core card table with FSRS memory state
CREATE TABLE cards (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id         UUID NOT NULL REFERENCES users(id),
    deck_id         UUID REFERENCES decks(id),
    -- Content
    front_content   JSONB NOT NULL,       -- Question / error details
    back_content    JSONB NOT NULL,       -- Answer / correct solution
    -- FSRS Memory State
    state           SMALLINT NOT NULL DEFAULT 0,  -- 0=New, 1=Learning, 2=Review, 3=Relearning
    difficulty      REAL NOT NULL DEFAULT 0,       -- D: 1-10 scale
    stability       REAL NOT NULL DEFAULT 0,       -- S: days
    due             TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_review     TIMESTAMPTZ,
    -- Counters
    reps            INTEGER NOT NULL DEFAULT 0,
    lapses          INTEGER NOT NULL DEFAULT 0,
    -- Knowledge Point linkage (for EdTech)
    knowledge_point_id UUID REFERENCES knowledge_points(id),
    subject_id      UUID REFERENCES subjects(id),
    -- Metadata
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    -- Multi-tenant
    tenant_id       UUID NOT NULL REFERENCES tenants(id)
);

-- Index for due card queries (the most frequent query)
CREATE INDEX idx_cards_due_user ON cards(user_id, due) WHERE state != 0;
CREATE INDEX idx_cards_tenant ON cards(tenant_id);

-- Review history (immutable log, used for FSRS optimization)
CREATE TABLE review_logs (
    id              BIGSERIAL PRIMARY KEY,
    card_id         UUID NOT NULL REFERENCES cards(id),
    user_id         UUID NOT NULL REFERENCES users(id),
    -- Review data
    rating          SMALLINT NOT NULL CHECK (rating BETWEEN 1 AND 4),
                    -- 1=Again, 2=Hard, 3=Good, 4=Easy
    state           SMALLINT NOT NULL,    -- Card state at time of review
    -- Timing
    scheduled_days  INTEGER NOT NULL,     -- Days since last review (scheduled)
    elapsed_days    INTEGER NOT NULL,     -- Days since last review (actual)
    review_duration_ms INTEGER,           -- Time spent reviewing (for analytics)
    -- Snapshot of memory state before this review
    difficulty_before REAL,
    stability_before  REAL,
    -- Timestamp
    reviewed_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    -- Multi-tenant
    tenant_id       UUID NOT NULL REFERENCES tenants(id)
);

-- Partitioned by month for large-scale review logs
-- CREATE TABLE review_logs ... PARTITION BY RANGE (reviewed_at);

CREATE INDEX idx_review_logs_card ON review_logs(card_id, reviewed_at DESC);
CREATE INDEX idx_review_logs_user ON review_logs(user_id, reviewed_at DESC);

-- FSRS scheduler parameters (per-user, trained via optimizer)
CREATE TABLE scheduler_params (
    user_id         UUID PRIMARY KEY REFERENCES users(id),
    weights         REAL[21] NOT NULL,    -- 21 FSRS parameters
    desired_retention REAL NOT NULL DEFAULT 0.9 CHECK (desired_retention BETWEEN 0.7 AND 0.99),
    last_optimized  TIMESTAMPTZ,
    review_count    INTEGER NOT NULL DEFAULT 0,  -- Total reviews for this user
    tenant_id       UUID NOT NULL REFERENCES tenants(id)
);
```

**Key Query Pattern — Get Due Cards**:

```sql
SELECT c.id, c.front_content, c.back_content, c.difficulty, c.stability
FROM cards c
WHERE c.user_id = $1
  AND c.due <= NOW()
  AND c.state IN (1, 2, 3)  -- Learning, Review, Relearning
ORDER BY c.due ASC
LIMIT 20;
```

### 2.4 Pattern: Duolingo Birdbrain Session Generator

**Pattern Name**: ML-Driven Adaptive Session Construction

**Description**: Duolingo's Birdbrain system uses logistic regression to predict per-exercise correct probability, then constructs 14-challenge lessons from ~200 candidates to maintain optimal difficulty (the "flow state").

**Architecture**:

```
[User Session Request]
    |
    v
[Session Generator Microservice]
    |-- Fetches ~200 candidate exercises
    |-- Queries Birdbrain model for P(correct) per exercise
    |-- Selects 14 exercises targeting optimal difficulty band
    |-- Interleaves new content with spaced repetition reviews
    |
    v
[Personalized Lesson]
```

**Scale**: 1.25 billion daily exercises, 130M MAUs, lesson construction reduced from 750ms to 14ms after Scala rewrite.

**When to use**: Platforms with large content libraries needing real-time personalization of practice sessions.

**Trade-offs**: Requires extensive historical data for model training; cold-start problem for new users requires heuristic fallbacks.

**References**:
- [How Duolingo's AI Learns What You Need to Learn - IEEE Spectrum](https://spectrum.ieee.org/duolingo)
- [Duolingo Half-Life Regression (GitHub)](https://github.com/duolingo/halflife-regression)
- [Duolingo Research Papers](https://research.duolingo.com/)

### 2.5 Squirrel AI Knowledge Graph Architecture

**Pattern Name**: Nano-Level Knowledge Point Graph with Adaptive Pathfinding

**Description**: Squirrel AI breaks subjects into 10,000+ nano-level knowledge points forming a directed graph. The system diagnoses mastery via adaptive testing, identifies weak points, and generates personalized learning paths through the graph.

**Architecture**:

```
[Diagnostic Test]
    |
    v
[Knowledge Graph Engine]
    |-- Maps student mastery to graph nodes
    |-- Identifies weakest prerequisite chains
    |-- Generates learning path (topological sort with mastery weights)
    |
    v
[Personalized Learning Path]
    |-- Video lessons, examples, practice problems per knowledge point
    |-- Closed-loop: assess -> learn -> practice -> re-assess
    |
    v
[Mastery Update] --> feeds back to Knowledge Graph
```

**When to use**: Structured academic subjects (math, science) where prerequisites form a clear dependency graph.

**Trade-offs**: Extremely effective for mastery learning but requires massive upfront content creation (videos, examples, problems per knowledge point); knowledge graph construction and maintenance is labor-intensive.

**Reference**: [Squirrel AI Learning (HundrED)](https://hundred.org/en/innovations/squirrel-ai-learning), [Stanford Case Study](https://www.gsb.stanford.edu/faculty-research/case-studies/squirrel-ai-learning-scaling)

---

## 3. Multi-Tenant SaaS Architecture for Education

### 3.1 Three Primary Isolation Models

#### Model A: Shared Database, Shared Schema (Pool Model)

**Pattern Name**: Row-Level Tenant Isolation

**Description**: All tenants share the same tables; a `tenant_id` column and Row-Level Security (RLS) enforce isolation at the database engine level.

```sql
-- Enable RLS
ALTER TABLE students ENABLE ROW LEVEL SECURITY;

-- Create tenant isolation policy
CREATE POLICY tenant_isolation ON students
    USING (tenant_id = current_setting('app.current_tenant')::uuid);

-- Application sets tenant context per request
SET app.current_tenant = 'tenant-uuid-here';
```

**When to use**: Early-stage products, B2C with individual users, high tenant count (thousands+), cost-sensitive.

**Trade-offs**:

| Pro | Con |
|:---|:---|
| Lowest cost, single database | Risk of cross-tenant data leakage if RLS misconfigured |
| Simplest operations (one schema migration) | Noisy neighbor risk on shared resources |
| Easy horizontal scaling | Complex per-tenant backup/restore |
| Fast tenant provisioning | Harder to meet strict compliance (FERPA/GDPR) |

#### Model B: Schema-per-Tenant (Bridge Model)

**Pattern Name**: Schema-Level Tenant Isolation

**Description**: Single database instance with a separate PostgreSQL schema per tenant. Each tenant's tables live in their own namespace.

```sql
-- Create tenant schema
CREATE SCHEMA tenant_abc123;

-- Each tenant has identical table structure in their schema
CREATE TABLE tenant_abc123.students (...);
CREATE TABLE tenant_abc123.assignments (...);

-- Application routes queries to correct schema
SET search_path TO tenant_abc123, public;
```

**When to use**: Mid-market B2B with moderate compliance needs, dozens to hundreds of tenants.

**Trade-offs**:

| Pro | Con |
|:---|:---|
| Strong logical isolation | Schema migrations across N schemas are complex |
| Per-tenant backup/restore possible | Operational complexity grows linearly with tenants |
| Tenant-specific customizations possible | Not viable for 10,000+ tenants |
| No RLS dependency | Connection pooling harder |

#### Model C: Database-per-Tenant (Silo Model)

**Pattern Name**: Database-Level Tenant Isolation

**Description**: Each tenant gets a dedicated database instance. Strongest isolation possible.

**When to use**: Enterprise customers with strict compliance requirements (FERPA, GDPR), government/military education, highest-value contracts.

**Trade-offs**:

| Pro | Con |
|:---|:---|
| Maximum isolation and compliance | Highest infrastructure cost |
| No noisy neighbor | Complex tenant provisioning automation |
| Independent scaling per tenant | Migration coordination across N databases |
| Per-tenant encryption keys (BYOK) | Connection management overhead |

### 3.2 Pattern: Tiered Hybrid Isolation (Recommended for EdTech)

**Pattern Name**: Tier-Based Dynamic Multi-Tenancy

**Description**: Maps isolation model to customer tier, allowing cost optimization for small tenants while meeting compliance needs for enterprise.

```
Tier 1 (Free / Individual Students):
    -> Shared schema with RLS (Pool Model)
    -> tenant_id column filtering
    -> Lowest cost

Tier 2 (Schools / Small Institutions):
    -> Schema-per-tenant (Bridge Model)
    -> Logical isolation with per-tenant backup
    -> FERPA-compatible

Tier 3 (School Districts / Enterprise):
    -> Database-per-tenant (Silo Model)
    -> Full isolation, BYOK encryption
    -> FERPA + GDPR compliant
    -> Dedicated resources
```

**When to use**: EdTech SaaS serving both individual consumers and institutional customers. This is the most common pattern for mature EdTech platforms.

**Trade-offs**: Requires tenant promotion infrastructure (moving a tenant from shared to isolated as they upgrade); adds complexity to the data access layer.

**Reference**: [Microsoft Learn — Multitenant SaaS Patterns](https://learn.microsoft.com/en-us/azure/azure-sql/database/saas-tenancy-app-design-patterns), [Multi-Tenant Architecture Complete Guide](https://bix-tech.com/multi-tenant-architecture-the-complete-guide-for-modern-saas-and-analytics-platforms-2/)

### 3.3 FERPA-Specific Requirements for EdTech Multi-Tenancy

**Key Requirements**:

| FERPA Requirement | Architecture Implication |
|:---|:---|
| Student PII protection | Encryption at rest (AES-256) and in transit (TLS 1.3) |
| Access control | RBAC with tenant-scoped roles (teacher, student, parent, admin) |
| Audit trail | Per-tenant audit logs tracking all PII access |
| Data minimization | Collect only necessary data; configurable per tenant |
| Parental consent (under 13) | Auth flow must enforce age gate + parental verification |
| Data portability | Per-tenant data export in standard formats |
| Right to deletion | Soft delete + crypto-shredding after retention period |
| Vendor agreements | Vendor must act as "School Official" under contract |

**Critical implementation note**: Every internal API, service call, and background process must carry tenant context explicitly. Relying only on UI-level isolation is a serious security risk.

**Reference**: [FERPA Compliance for SaaS Tools in Education](https://www.reform.app/blog/ferpa-compliance-for-saas-tools-in-education), [Tenant Isolation in Multi-Tenant Systems](https://securityboulevard.com/2025/12/tenant-isolation-in-multi-tenant-systems-architecture-identity-and-security/)

### 3.4 Tenant-Aware Service Architecture

**Pattern Name**: Tenant Context Propagation

**Description**: Every request carries tenant context from API gateway through all microservices, ensuring data isolation at every layer.

```
[API Gateway]
    |-- Extracts tenant_id from JWT / API key
    |-- Sets X-Tenant-ID header
    |
    v
[Microservice]
    |-- Middleware extracts tenant context
    |-- Sets database session context (RLS) or selects schema/database
    |-- All queries are tenant-scoped by construction
    |-- Propagates tenant context to downstream service calls
    |
    v
[Database]
    |-- RLS policies enforce tenant isolation
    |-- No query can access data without tenant_id
```

**Implementation Pattern for Spring Boot**:

```java
@Component
public class TenantInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, ...) {
        String tenantId = request.getHeader("X-Tenant-ID");
        TenantContext.setCurrentTenant(tenantId);
        return true;
    }
}
```

---

## 4. Offline-First Mobile Architecture

### 4.1 Pattern: Local-First with Background Sync

**Pattern Name**: SSOT Local Database with Reactive Sync

**Description**: The local database (SQLite/Room/Drift) is the Single Source of Truth. The UI always reads from local storage; network sync happens in the background.

**Architecture (Flutter/Mobile)**:

```
[UI Layer]
    |-- Observes reactive streams from local DB
    |-- Immediate response, no network wait
    |
    v
[Repository Layer]
    |-- Reads: always from local DB
    |-- Writes: write to local DB + enqueue sync job
    |
    v
[Local Database] <-- Single Source of Truth
    |-- Room (Android) / CoreData (iOS) / Drift (Flutter)
    |-- Stores all data with sync metadata
    |
    v
[Sync Engine]
    |-- Background worker (WorkManager / BGTaskScheduler)
    |-- Detects connectivity changes
    |-- Batches pending changes
    |-- Pushes to server, pulls remote changes
    |-- Handles conflict resolution
    |
    v
[Remote API Server]
```

**When to use**: Any mobile education app where users may study offline (classrooms, rural areas, transit, flights).

**Trade-offs**:

| Pro | Con |
|:---|:---|
| Instant UI response | Data may be stale until sync |
| Works fully offline | Conflict resolution adds complexity |
| Resilient to poor connectivity | More local storage usage |
| Reduced server load | Sync bugs are hard to debug |

**Reference**: [Complete Guide to Offline-First Architecture in Android (Droidcon 2025)](https://www.droidcon.com/2025/12/16/the-complete-guide-to-offline-first-architecture-in-android/)

### 4.2 Conflict Resolution Strategies

| Strategy | Description | Complexity | Data Loss Risk | Best For |
|:---|:---|:---|:---|:---|
| **Last-Write-Wins (LWW)** | Most recent timestamp wins | Low | Medium (silent overwrites) | User preferences, settings, single-user data |
| **Merge by Rules** | Domain-specific merge logic | Medium | Low (if rules are correct) | Structured data with known merge semantics |
| **CRDTs** | Mathematically conflict-free data types | High | None (guaranteed convergence) | Collaborative data, shared notes, counters |
| **Operational Transform** | Transform concurrent operations | Very High | None | Real-time collaborative editing (Google Docs) |
| **Manual Resolution** | Present conflict to user | Low (code) | None | Rare conflicts, high-value data |

#### Recommended Strategy for EdTech (Error Notebook):

```
Error Notebook Cards:
  - Card content (front/back): LWW (last edit wins, single-user data)
  - Review history: Append-only (no conflicts possible)
  - FSRS memory state (D, S): Recalculate from full review history on sync
  - Mastery status: Server-authoritative after sync

Study Progress:
  - Streak counters: G-Counter CRDT (additive, no conflicts)
  - Completed exercises: G-Set CRDT (grow-only set)
  - Time-spent: G-Counter CRDT

Settings:
  - LWW with per-field timestamps
```

### 4.3 Pattern: CRDT-Based Sync

**Pattern Name**: Conflict-Free Replicated Data Types

**Description**: Data structures designed to be commutative, associative, and idempotent. When devices exchange updates, all replicas eventually converge without conflicts.

**Common CRDT Types for Education Apps**:

| CRDT Type | Use Case | How It Works |
|:---|:---|:---|
| G-Counter | Study time tracking, streak counts | Each node increments its own counter; merge = sum all |
| PN-Counter | Score adjustments | Pair of G-Counters (positive + negative) |
| G-Set | Completed exercises, collected errors | Grow-only set; merge = union |
| LWW-Register | User settings, profile fields | Last write (by timestamp) wins |
| LWW-Map | Card metadata | Map of LWW-Registers |
| OR-Set (Observed-Remove Set) | Bookmark lists, tag sets | Tracks add/remove with unique IDs |

**Available Libraries**:

| Library | Language | Notes |
|:---|:---|:---|
| Yjs | TypeScript/JS | Most popular, used for collaborative editing |
| Automerge | Rust/JS/Swift | JSON-like CRDT, good for structured data |
| Synk | Kotlin Multiplatform | Works with Room/SQLDelight, mobile-focused |
| dart-fsrs | Dart | FSRS scheduler for Flutter |

**When to use**: Multi-device sync scenarios where conflicts are expected (e.g., student studies on phone and tablet).

**Trade-offs**: More metadata overhead per record; requires careful choice of CRDT type per data field; some operations (like "delete") are more complex.

**Reference**: [TypeScript CRDT Toolkits for Offline-First Apps](https://medium.com/@2nick2patel2/typescript-crdt-toolkits-for-offline-first-apps-conflict-free-sync-without-tears-df456c7a169b), [Synk — Kotlin Multiplatform CRDT Library](https://github.com/CharlieTap/synk)

### 4.4 Offline Content Strategy for Education

**Pattern Name**: Tiered Content Pre-caching

**Description**: Proactively download content to local storage based on predicted need, tiered by importance.

```
Tier 1 (Always Cached):
  - User's error notebook cards + associated content
  - Due review cards for next 24 hours
  - Active lesson content

Tier 2 (Wi-Fi Pre-cache):
  - Next 3 lessons in learning path
  - Practice questions for weak knowledge points
  - Frequently accessed reference materials

Tier 3 (On-Demand with Cache):
  - Historical review data
  - Analytics dashboards
  - Other students' shared content

Cache Eviction:
  - LRU with priority: Tier 1 never evicted, Tier 2 evicted after 7 days,
    Tier 3 evicted after 24 hours
  - Total cache budget: configurable, default 500MB
```

**Implementation for Flutter (Drift/sqflite)**:

```dart
// Sync metadata per record
class SyncMeta {
  final String id;
  final DateTime lastModifiedLocal;
  final DateTime lastModifiedServer;
  final SyncStatus status; // synced, pending_push, pending_pull, conflict
  final int version;
}
```

---

## 5. Streaming Architecture (SSE/WebSocket)

### 5.1 Protocol Comparison for LLM Streaming

| Feature | SSE | WebSocket | gRPC Streaming |
|:---|:---|:---|:---|
| Direction | Server -> Client (unidirectional) | Bidirectional | Bidirectional |
| Protocol | HTTP/1.1 or HTTP/2 | Upgrade from HTTP | HTTP/2 |
| Auto-reconnect | Built-in (EventSource API) | Manual implementation | Manual |
| Browser support | Native (EventSource) | Native (WebSocket API) | Requires grpc-web proxy |
| Load balancer support | Standard HTTP | Requires sticky sessions | Requires HTTP/2 support |
| Mobile support | HTTP client (no native EventSource) | Native on iOS/Android | Native on iOS/Android |
| Scaling | Stateless, easy horizontal | Stateful, needs session affinity | Stateless with HTTP/2 |
| Industry adoption for LLM | OpenAI, Anthropic, most LLM APIs | Real-time chat apps | Internal microservice communication |

**Verdict for EdTech LLM Streaming**: SSE is the recommended default for LLM response streaming. Use WebSocket only if bidirectional communication is required (e.g., stop generation, mid-stream feedback).

**Reference**: [The Streaming Backbone of LLMs: Why SSE Still Wins (Procedure Blog)](https://procedure.tech/blogs/the-streaming-backbone-of-llms-why-server-sent-events-(sse)-still-wins-in-2025), [Streaming at Scale: SSE, WebSockets & Real-Time AI APIs](https://learnwithparam.com/blog/streaming-at-scale-sse-websockets-real-time-ai-apis)

### 5.2 Pattern: SSE with Last-Event-ID Resumption

**Pattern Name**: Resumable Token Streaming

**Description**: Each streamed token is assigned a monotonic event ID. If the connection drops, the client reconnects with `Last-Event-ID` and the server resumes from the next token.

**Server Implementation**:

```
HTTP/1.1 200 OK
Content-Type: text/event-stream
Cache-Control: no-store
Connection: keep-alive
X-Accel-Buffering: no

id: 1
data: {"token": "The", "index": 0}

id: 2
data: {"token": " answer", "index": 1}

id: 3
data: {"token": " is", "index": 2}

...

id: 250
data: [DONE]
```

**Client Reconnection**:

```
-- Client reconnects after disconnect --
GET /stream/grading-result/job-123
Last-Event-ID: 47

-- Server resumes from event 48 --
id: 48
data: {"token": "step", "index": 47}
```

**When to use**: Any LLM streaming endpoint, especially for mobile clients on unreliable networks.

**Trade-offs**: Requires server-side token buffer (Redis or in-memory) with TTL for in-progress streams; adds storage overhead but dramatically improves mobile UX.

### 5.3 Pattern: Hybrid SSE + WebSocket Architecture

**Pattern Name**: Dual-Protocol Streaming

**Description**: Use SSE for server-to-client LLM token streaming (stateless, easy to scale) and WebSocket for client-to-server control messages (stop generation, send follow-up).

```
[Mobile Client]
    |
    |-- SSE Connection (read-only, LLM token stream)
    |   GET /api/v1/stream/grading/{jobId}
    |   Content-Type: text/event-stream
    |
    |-- WebSocket Connection (control channel)
    |   WS /api/v1/ws/session/{sessionId}
    |   Messages: { "action": "stop" }, { "action": "follow_up", "question": "..." }
    |
    v
[API Gateway]
    |-- Routes SSE to Streaming Service
    |-- Routes WS to Session Service
    |
    v
[Backend Services]
    |-- Streaming Service: pulls tokens from LLM, buffers, sends SSE
    |-- Session Service: handles control messages, manages generation lifecycle
```

**When to use**: Interactive AI tutoring where users need to interrupt, ask follow-ups, or control the generation process.

### 5.4 WeChat Mini Program Considerations

**Problem**: WeChat Mini Programs do not support native SSE (EventSource API). The `wx.request` API is request-response based.

**Solutions**:

| Approach | Description | Trade-offs |
|:---|:---|:---|
| `wx.request` with `enableChunked: true` | Chunked transfer encoding, parse chunks manually | Works on iOS/Android; no auto-reconnect |
| WebSocket (`wx.connectSocket`) | Full WebSocket support in Mini Programs | Bidirectional but more complex server-side |
| Long Polling fallback | Repeated short-lived requests | Highest latency, simplest to implement |
| Unified WebSocket for all platforms | Single protocol for web, app, Mini Program | Loses SSE benefits on web; adds WS scaling complexity |

**Recommended**: Use `wx.connectSocket` (WebSocket) for Mini Program; SSE for web/Flutter. Backend provides both protocols via protocol adapter pattern.

### 5.5 Backpressure Handling

**Pattern Name**: Buffered Token Streaming with Backpressure

**Description**: When the LLM generates tokens faster than the client can consume (mobile on slow network), implement backpressure to prevent memory exhaustion.

```
[LLM Provider] --> tokens at ~50-100 tokens/sec
    |
    v
[Token Buffer] (bounded, e.g., 1000 tokens)
    |-- If buffer full: pause LLM consumption (backpressure upstream)
    |-- If buffer empty: wait for next token
    |
    v
[SSE Writer]
    |-- Checks write buffer: if ws.bufferedAmount > threshold, pause
    |-- Flushes tokens as client ACKs
    |-- Sends keep-alive (`: heartbeat\n\n`) every 15-30 seconds
    |
    v
[Client]
    |-- Processes tokens into UI
    |-- If overwhelmed: browser/OS handles TCP backpressure naturally
```

**Key Configuration**:

```yaml
streaming:
  token_buffer_size: 1000          # Max buffered tokens
  heartbeat_interval_seconds: 15    # Keep-alive interval
  idle_timeout_seconds: 300         # Close idle connections
  max_stream_duration_seconds: 120  # Safety timeout
  flush_interval_ms: 50            # Batch flush for efficiency
```

**Reference**: [How We Used SSE to Stream LLM Responses at Scale](https://medium.com/@daniakabani/how-we-used-sse-to-stream-llm-responses-at-scale-fa0d30a6773f)

### 5.6 API Gateway Configuration for SSE

**Key settings to prevent SSE breakage through API gateways and load balancers**:

```yaml
# Nginx / API Gateway configuration
location /api/v1/stream/ {
    proxy_pass http://streaming-service;

    # Critical for SSE
    proxy_buffering off;           # Do NOT buffer the response
    proxy_cache off;
    proxy_set_header Connection '';
    proxy_http_version 1.1;
    chunked_transfer_encoding on;

    # Timeouts for long-lived connections
    proxy_read_timeout 300s;       # Match max stream duration
    proxy_send_timeout 300s;
    send_timeout 300s;

    # Headers
    add_header Cache-Control "no-store";
    add_header X-Accel-Buffering "no";

    # CORS for web clients
    add_header Access-Control-Allow-Origin $cors_origin;
    add_header Access-Control-Allow-Credentials true;
}
```

**AWS API Gateway**: Now supports response streaming natively (announced 2025). Set payload format to `chunked` and response content type to `text/event-stream`.

**Reference**: [Building Responsive APIs with Amazon API Gateway Response Streaming](https://aws.amazon.com/blogs/compute/building-responsive-apis-with-amazon-api-gateway-response-streaming/), [KrakenD SSE Documentation](https://www.krakend.io/docs/enterprise/endpoints/streaming/)

---

## 6. Cost Optimization for LLM APIs

### 6.1 Cost Landscape (2025)

| Provider/Model | Input (per 1M tokens) | Output (per 1M tokens) | Best For |
|:---|:---|:---|:---|
| GPT-4o | $2.50 | $10.00 | Complex reasoning, multimodal |
| GPT-4o-mini | $0.15 | $0.60 | Simple tasks, classification |
| Claude 3.5 Sonnet | $3.00 | $15.00 | Long-form explanation, coding |
| Claude 3.5 Haiku | $0.25 | $1.25 | Fast, cheap, good quality |
| Gemini 1.5 Flash | $0.0375 | $0.15 | Highest volume, lowest cost |
| Gemini 1.5 Pro | $1.25 | $5.00 | Complex with long context |
| DeepSeek v3 | $0.27 | $1.10 | Cost-effective reasoning |

**At 100M tokens/month**: Using Claude 3.5 Sonnet costs ~$1,800/month. Routing 50% to Gemini Flash drops that portion from $900 to ~$19. **Savings compound fast**.

### 6.2 Pattern: Semantic Caching

**Pattern Name**: Vector-Similarity Response Cache

**Description**: Cache LLM responses keyed by semantic similarity (not exact match). When a new query is semantically similar to a cached query (cosine similarity > threshold), return the cached response instead of calling the LLM.

**Architecture**:

```
[Incoming Query]
    |
    v
[Embedding Model] -- generate query embedding (e.g., text-embedding-3-small, ~$0.02/1M tokens)
    |
    v
[Vector Store] -- cosine similarity search
    |
    |-- IF similarity > 0.85: return cached response (cache HIT)
    |-- IF similarity <= 0.85: call LLM, cache response + embedding (cache MISS)
    |
    v
[Response to Client]
```

**Implementation Stack**:

```
Layer 1 (Exact Match):    Redis hash lookup on prompt hash (~0.1ms)
Layer 2 (Semantic Match):  Vector DB similarity search (~5-10ms)
                           Options: Redis Vector, pgvector, FAISS, Pinecone
Layer 3 (LLM Call):        Full API call (~1-10 seconds)
```

**Cache Invalidation**:

```
- TTL-based: expire after N days (configurable per content type)
- Version-based: invalidate when prompt template changes
- Content-based: invalidate when underlying knowledge base updates
- Manual: admin can clear cache for specific topics
```

**Expected Savings**: 30-70% reduction in API calls for workloads with repetitive patterns. Education is particularly well-suited because students across a class submit similar problems.

**When to use**: High-volume applications with repetitive query patterns (FAQ bots, homework grading where many students submit the same worksheet).

**Trade-offs**: Requires embedding model costs (small); risk of returning stale/incorrect cached responses if similarity threshold is too low; cache storage costs.

**Reference**: [Cut LLM Costs with Semantic Caching (ScyllaDB)](https://www.scylladb.com/2025/11/24/cut-llm-costs-and-latency-with-scylladb-semantic-caching/), [AWS — Optimize LLM Response Costs with Caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)

### 6.3 Pattern: Intelligent Model Routing (Cascade Router)

**Pattern Name**: Complexity-Based Model Cascade

**Description**: A lightweight classifier routes queries to the cheapest model capable of producing a quality response. Complex queries cascade to more expensive models.

**Architecture**:

```
[Incoming Query]
    |
    v
[Complexity Classifier]
    |-- Option A: Fine-tuned DistilBERT (~66M params, <20ms inference)
    |-- Option B: Rule-based heuristics (question length, subject, keywords)
    |-- Option C: Small LLM classifier (GPT-4o-mini as router)
    |
    |-- Simple (e.g., factual recall, basic arithmetic):
    |   --> Gemini Flash / GPT-4o-mini (~$0.15/1M input)
    |
    |-- Medium (e.g., multi-step math, short explanation):
    |   --> Claude Haiku / GPT-4o-mini (~$0.25-1.50/1M input)
    |
    |-- Complex (e.g., essay grading, proof, multi-concept):
    |   --> GPT-4o / Claude Sonnet (~$2.50-3.00/1M input)
    |
    v
[Quality Gate]
    |-- If response quality score < threshold:
    |   --> Escalate to next tier (cascade)
    |-- If quality OK:
    |   --> Return response
```

**Routing vs. Cascading vs. Cascade Routing**:

| Strategy | Description | Latency | Cost Savings |
|:---|:---|:---|:---|
| **Routing** | Pick one model upfront based on classifier | Lowest (single call) | 30-55% |
| **Cascading** | Try cheapest first, escalate if quality is insufficient | Higher (multiple calls possible) | 40-70% |
| **Cascade Routing** | Unified optimal strategy (ICLR 2025) | Optimal | Best theoretical bounds |

**Complexity Signals for Education**:

```python
def estimate_complexity(query: str, subject: str, image_features: dict) -> str:
    signals = {
        "question_count": count_questions(query),
        "subject_difficulty": SUBJECT_DIFFICULTY_MAP[subject],
        "requires_proof": has_proof_keywords(query),
        "is_essay": len(query) > 500,
        "has_diagram": image_features.get("has_diagram", False),
        "grade_level": extract_grade_level(query),
        "multi_concept": count_knowledge_points(query) > 2,
    }
    # Trained classifier or rule-based
    return classifier.predict(signals)  # "simple" | "medium" | "complex"
```

**Savings Example**:

```
Before (all queries to GPT-4o):
  10K queries/day * ~500 tokens avg * $2.50/1M = $12.50/day = $375/month

After (routed):
  6K simple -> Gemini Flash: 6K * 500 * $0.0375/1M = $0.11/day
  3K medium -> Claude Haiku: 3K * 500 * $0.25/1M  = $0.38/day
  1K complex -> GPT-4o:      1K * 500 * $2.50/1M  = $1.25/day
  Total: $1.74/day = $52/month (86% reduction)
```

**Reference**: [A Unified Approach to Routing and Cascading for LLMs (ICLR 2025)](https://arxiv.org/abs/2410.10347), [Intelligent LLM Routing in Enterprise AI](https://www.requesty.ai/blog/intelligent-llm-routing-in-enterprise-ai-uptime-cost-efficiency-and-model), [AWS Multi-LLM Routing Strategies](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/)

### 6.4 Pattern: Prompt Optimization and Compression

**Pattern Name**: Token-Efficient Prompt Engineering

**Description**: Reduce input token count through systematic prompt optimization without losing output quality.

**Techniques**:

| Technique | Token Reduction | Quality Impact | Effort |
|:---|:---|:---|:---|
| Remove redundant instructions | 10-20% | None | Low |
| Use structured output (JSON mode) | 15-30% | Improved (structured) | Low |
| Few-shot -> zero-shot with good system prompt | 40-60% | Slight decrease | Medium |
| Prompt compression (LLMLingua) | Up to 20x | Slight decrease | Medium |
| Provider prompt caching (Anthropic/OpenAI) | 50-90% on cached portion | None | Low |
| RAG context pruning | 30-50% of context | Depends on pruning quality | Medium |

**Provider Prompt Caching**:

```
System prompt (rubric, instructions) = ~2000 tokens
  -> Cached after first call
  -> Subsequent calls: 50-90% discount on cached portion
  -> Anthropic: Automatic caching for prompts > 1024 tokens
  -> OpenAI: Automatic caching for prompts > 1024 tokens
```

**When to use**: Always — prompt optimization should be the first cost reduction step before implementing routing or caching infrastructure.

### 6.5 Pattern: LLM Gateway

**Pattern Name**: Unified LLM Access Layer

**Description**: A proxy layer between application and LLM providers that centralizes routing, caching, monitoring, rate limiting, and failover.

**Architecture**:

```
[Application Services]
    |
    v
[LLM Gateway]
    |-- Semantic Cache (check before routing)
    |-- Model Router (select optimal model)
    |-- Rate Limiter (per tenant, per model)
    |-- Cost Tracker (per request, per tenant)
    |-- Failover (automatic provider switching)
    |-- Prompt Template Manager
    |-- Observability (latency, tokens, cost, quality metrics)
    |
    v
[LLM Providers]
    |-- OpenAI (GPT-4o, GPT-4o-mini)
    |-- Anthropic (Claude Sonnet, Haiku)
    |-- Google (Gemini Pro, Flash)
    |-- Self-hosted (open source models)
```

**Open Source Gateway Options**:

| Gateway | Language | Key Features |
|:---|:---|:---|
| LiteLLM | Python | 100+ providers, OpenAI-compatible API |
| Portkey | TypeScript | Caching, routing, guardrails |
| Martian | Python | Model routing optimization |
| Bifrost | Go | Semantic caching, dual-layer |

**Key Metrics to Track**:

```yaml
llm_metrics:
  - request_count (by model, tenant, endpoint)
  - token_usage (input, output, cached)
  - cost_per_request
  - latency_p50, latency_p95, latency_p99
  - time_to_first_token (TTFT)
  - cache_hit_rate
  - quality_score (if quality evaluation enabled)
  - error_rate (by provider, model)
  - routing_decision_distribution
```

**When to use**: Any production system using multiple LLM providers. Over 90% of production AI teams now run 5+ LLMs simultaneously.

**Reference**: [Top 5 LLM Gateways in 2025](https://www.getmaxim.ai/articles/top-5-llm-gateways-in-2025-the-definitive-guide-for-production-ai-applications/), [LLM Cost Optimization Complete Guide](https://ai.koombea.com/blog/llm-cost-optimization)

### 6.6 Pattern: Image Hash Deduplication for Grading

**Pattern Name**: Perceptual Hash + Exact Hash Dual Dedup

**Description**: For image-based homework grading, deduplicate at the image level before expensive LLM processing.

```
[Uploaded Image]
    |
    v
[Hash Computation]
    |-- Exact hash (SHA-256): catches identical uploads
    |-- Perceptual hash (pHash/dHash): catches re-photographed same page
    |   (different angle, lighting, crop variations)
    |
    v
[Cache Lookup]
    |-- Exact match found: return cached result immediately
    |-- Perceptual match (hamming distance < threshold): return cached result
    |-- No match: proceed to OCR + LLM pipeline, cache result
```

**Expected Dedup Rate for Education**: In a classroom setting where 30 students photograph the same worksheet, exact dedup catches identical photos, and perceptual dedup catches the remaining variations. Expected dedup rate: 40-80% of images in a class assignment.

**When to use**: Homework grading platforms where multiple students submit photos of the same printed worksheet.

### 6.7 Comprehensive Cost Optimization Stack

**Layered approach — apply in order of implementation ease**:

```
Layer 1 (Easy, Immediate):
  - Prompt optimization: remove redundancy, use structured output
  - Provider prompt caching: leverage built-in caching
  - Exact-match response caching: Redis hash lookup
  Expected savings: 20-30%

Layer 2 (Medium, 1-2 weeks):
  - Semantic caching with vector similarity
  - Image hash deduplication (for grading pipeline)
  - Token usage monitoring and alerting
  Expected savings: additional 20-30%

Layer 3 (Complex, 2-4 weeks):
  - Intelligent model routing (complexity classifier)
  - LLM Gateway with unified metrics
  - Per-tenant cost tracking and budget enforcement
  Expected savings: additional 30-50%

Layer 4 (Advanced, 1-3 months):
  - Knowledge distillation (train smaller model on GPT-4o outputs)
  - Self-hosted open-source models for simple tasks
  - Cascade routing with quality gates
  Expected savings: additional 20-40%

Cumulative potential: 60-80% total cost reduction
```

**Reference**: [Taming the Beast: Cost Optimization Strategies for LLM API Calls](https://medium.com/@ajayverma23/taming-the-beast-cost-optimization-strategies-for-llm-api-calls-in-production-11f16dbe2c39), [LLM Cost Optimization Guide: Reduce AI Infrastructure 30%](https://futureagi.com/blogs/llm-cost-optimization-2025), [How to Reduce LLM Costs by 40% in 24 Hours](https://scalemind.ai/blog/reduce-llm-costs)

---

## Summary: Pattern Selection Matrix

| Area | Recommended Pattern | Alternatives | Key Decision Factor |
|:---|:---|:---|:---|
| AI Grading Pipeline | Hybrid OCR + Multimodal LLM | Pure multimodal; pure OCR+LLM | Content type (handwritten vs printed) |
| Spaced Repetition | FSRS with ML optimization | SM-2 (simpler); Birdbrain-style (more complex) | Data volume for optimization |
| Multi-Tenancy | Tiered hybrid (Pool + Schema + Silo) | Pool-only; Silo-only | Customer segments and compliance |
| Offline-First | Local SSOT + Background Sync + LWW/CRDT | Online-first with cache | Connectivity reliability of users |
| LLM Streaming | SSE with Last-Event-ID + WS control channel | WebSocket-only; gRPC | Platform constraints (Mini Program) |
| Cost Optimization | Layered: cache + route + compress + gateway | Single strategy | Budget and engineering bandwidth |

---

## Source References

### AI Grading Pipeline
- [Microservices Architecture for Modular EdTech File Processing (DEV Community)](https://dev.to/ideradevtools/microservices-architecture-for-modular-edtech-file-processing-268n)
- [LLM-Powered Automatic Grading Framework (EDM 2025)](https://educationaldatamining.org/EDM2025/proceedings/2025.EDM.long-papers.80/index.html)
- [Integrating Generative AI: OCR and Multimodal LLM (ArXiv)](https://arxiv.org/html/2509.02998)
- [7 Best Open-Source OCR Models 2025 (E2E Networks)](https://www.e2enetworks.com/blog/complete-guide-open-source-ocr-models-2025)
- [Gauth vs Photomath Comparison (BBN Times)](https://www.bbntimes.com/technology/gauth-vs-photomath-the-definitive-battle-of-ai-homework-helpers-in-2025)
- [ByteDance Gauth Dominates US Education Charts (FoxData)](https://foxdata.com/en/blogs/bytedances-gauth-ai-study-companion-dominates-2025-us-education-charts-as-top-ai-homework-helper/)

### Spaced Repetition
- [FSRS GitHub Repository](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler)
- [ABC of FSRS (Wiki)](https://github.com/open-spaced-repetition/fsrs4anki/wiki/abc-of-fsrs)
- [FSRS-rs Architecture (DeepWiki)](https://deepwiki.com/open-spaced-repetition/fsrs-rs)
- [Duolingo Half-Life Regression (GitHub)](https://github.com/duolingo/halflife-regression)
- [How Duolingo's AI Learns What You Need to Learn (IEEE Spectrum)](https://spectrum.ieee.org/duolingo)
- [Duolingo AI Strategy (Chief AI Officer)](https://chiefaiofficer.com/duolingos-ai-strategy-fuels-51-user-growth-and-1b-revenue/)
- [Squirrel AI Learning (HundrED)](https://hundred.org/en/innovations/squirrel-ai-learning)
- [Squirrel AI Stanford Case Study](https://www.gsb.stanford.edu/faculty-research/case-studies/squirrel-ai-learning-scaling)
- [FSRS RemNote Help Center](https://help.remnote.com/en/articles/9124137-the-fsrs-spaced-repetition-algorithm)

### Multi-Tenant SaaS
- [Microsoft Azure Multitenant SaaS Patterns](https://learn.microsoft.com/en-us/azure/azure-sql/database/saas-tenancy-app-design-patterns)
- [Multi-Tenant Architecture Complete Guide (BIX Tech)](https://bix-tech.com/multi-tenant-architecture-the-complete-guide-for-modern-saas-and-analytics-platforms-2/)
- [Multi-Tenant SaaS — Database Per Tenant (LK Tech Academy)](https://www.lktechacademy.com/2025/10/multi-tenant-saas-architecture-database-per-tenant.html)
- [Tenant Isolation — Architecture, Identity, and Security (Security Boulevard)](https://securityboulevard.com/2025/12/tenant-isolation-in-multi-tenant-systems-architecture-identity-and-security/)
- [FERPA Compliance for SaaS Tools in Education (Reform)](https://www.reform.app/blog/ferpa-compliance-for-saas-tools-in-education)
- [Data Isolation in Multi-Tenant SaaS (Redis)](https://redis.io/blog/data-isolation-multi-tenant-saas/)

### Offline-First Mobile
- [Complete Guide to Offline-First Architecture in Android (Droidcon)](https://www.droidcon.com/2025/12/16/the-complete-guide-to-offline-first-architecture-in-android/)
- [Offline-First Sync Patterns (DevelopersVoice)](https://developersvoice.com/blog/mobile/offline-first-sync-patterns/)
- [TypeScript CRDT Toolkits for Offline-First Apps (Medium)](https://medium.com/@2nick2patel2/typescript-crdt-toolkits-for-offline-first-apps-conflict-free-sync-without-tears-df456c7a169b)
- [Synk — Kotlin Multiplatform CRDT Library (GitHub)](https://github.com/CharlieTap/synk)
- [Design Guide for Building Offline First Apps (Hasura)](https://hasura.io/blog/design-guide-to-offline-first-apps)

### Streaming Architecture
- [The Streaming Backbone of LLMs: Why SSE Still Wins (Procedure Blog)](https://procedure.tech/blogs/the-streaming-backbone-of-llms-why-server-sent-events-(sse)-still-wins-in-2025)
- [How We Used SSE to Stream LLM Responses at Scale (Medium)](https://medium.com/@daniakabani/how-we-used-sse-to-stream-llm-responses-at-scale-fa0d30a6773f)
- [Streaming at Scale: SSE, WebSockets & Real-Time AI APIs (LearnWithParam)](https://learnwithparam.com/blog/streaming-at-scale-sse-websockets-real-time-ai-apis)
- [Building Responsive APIs with Amazon API Gateway Response Streaming (AWS)](https://aws.amazon.com/blogs/compute/building-responsive-apis-with-amazon-api-gateway-response-streaming/)
- [KrakenD SSE Documentation](https://www.krakend.io/docs/enterprise/endpoints/streaming/)
- [Complete Guide to Streaming LLM Responses (DEV Community)](https://dev.to/pockit_tools/the-complete-guide-to-streaming-llm-responses-in-web-applications-from-sse-to-real-time-ui-3534)

### Cost Optimization
- [Taming the Beast: Cost Optimization for LLM API Calls (Medium)](https://medium.com/@ajayverma23/taming-the-beast-cost-optimization-strategies-for-llm-api-calls-in-production-11f16dbe2c39)
- [Cost-Effective LLM Applications (Glukhov Blog)](https://www.glukhov.org/post/2025/11/cost-effective-llm-applications/)
- [LLM Cost Optimization Guide (FutureAGI)](https://futureagi.com/blogs/llm-cost-optimization-2025)
- [LLM Cost Optimization: Reduce AI Expenses by 80% (Koombea)](https://ai.koombea.com/blog/llm-cost-optimization)
- [Top 5 LLM Gateways in 2025 (Maxim)](https://www.getmaxim.ai/articles/top-5-llm-gateways-in-2025-the-definitive-guide-for-production-ai-applications/)
- [Cut LLM Costs with Semantic Caching (ScyllaDB)](https://www.scylladb.com/2025/11/24/cut-llm-costs-and-latency-with-scylladb-semantic-caching/)
- [Optimize LLM Response Costs with Caching (AWS)](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)
- [A Unified Approach to Routing and Cascading for LLMs (ICLR 2025)](https://arxiv.org/abs/2410.10347)
- [AWS Multi-LLM Routing Strategies](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/)
- [How to Reduce LLM Costs by 40% in 24 Hours (ScaleMind)](https://scalemind.ai/blog/reduce-llm-costs)
