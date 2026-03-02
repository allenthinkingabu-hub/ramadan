# Phase 3 Question List — Architecture Design

## Phase: Research & Question Generation
## Generated: 2026-03-01T00:25:00+08:00
## Context: AI Smart Grader — IA-REQ-001

---

## Category 1: AI Grading Pipeline Architecture

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q3-001 | For AI model routing, should we route by: (a) subject only, (b) subject + complexity estimation, or (c) subject + complexity + user tier? This affects whether we need a complexity-estimation pre-processing step before LLM invocation. | AI Pipeline | Pending | |
| Q3-002 | For image preprocessing before LLM call, do we need a dedicated OCR step (e.g., Tesseract) or rely entirely on the multimodal LLM's vision capability for both text recognition and grading? Trade-off: dedicated OCR adds latency but improves accuracy for handwritten text. | AI Pipeline | Pending | |
| Q3-003 | Should AI grading results be cached per (a) exact image hash (strict dedup), (b) perceptual image hash (similar images return cached result), or (c) both? Perceptual hashing catches re-photographed same page but adds complexity. | AI Pipeline | Pending | |
| Q3-004 | For the streaming response, should the backend parse and structure the LLM output in real-time (extracting judgment, answer, explanation, knowledge points as separate structured fields), or stream raw LLM text first and structure it after completion? | AI Pipeline | Pending | |
| Q3-005 | What is the expected average number of questions per uploaded image? This affects: batch processing strategy, result storage granularity, and error notebook auto-collection logic. | AI Pipeline | Pending | |

## Category 2: Error Notebook & Spaced Repetition

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q3-006 | For the spaced repetition algorithm, should we use: (a) fixed intervals (1d, 3d, 7d, 14d, 30d — admin-configured), (b) SM-2 algorithm (adaptive based on performance), or (c) FSRS (modern, data-driven)? Fixed is simplest but least personalized. | Error Notebook | Pending | |
| Q3-007 | Should practice question generation for mastery testing be synchronous (user waits for AI to generate) or pre-generated asynchronously (background job generates practice questions when error is first collected)? Pre-generation improves UX but increases AI API costs. | Error Notebook | Pending | |
| Q3-008 | For error notebook capacity enforcement (tier-based), when a user hits their limit, should we: (a) block new entries entirely, (b) auto-archive oldest mastered entries to make room, or (c) allow soft overflow with upgrade prompt? | Error Notebook | Pending | |

## Category 3: Multi-Tenant & Data Architecture

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q3-009 | For multi-tenancy, should we use: (a) shared database with row-level tenant_id filtering, (b) schema-per-tenant in same PostgreSQL instance, or (c) separate database per tenant? Trade-off: (a) simplest but risk of data leakage; (b) balanced; (c) strongest isolation but highest ops cost. | Data | Pending | |
| Q3-010 | For the knowledge point taxonomy (subjects × academic levels × knowledge points), should this be: (a) a flat table with parent_id hierarchy, (b) a materialized path/ltree approach in PostgreSQL, or (c) a separate knowledge graph service? The taxonomy drives tagging, weakness analysis, and mastery reports. | Data | Pending | |
| Q3-011 | Should analytics aggregation be: (a) real-time via PostgreSQL materialized views, (b) near-real-time via dedicated analytics service with pre-computed aggregations (≤ 5 min), or (c) event-sourced with CQRS read models? The PRD requires ≤ 5 min data freshness for teacher dashboards and ≤ 1 min for admin dashboard. | Data | Pending | |

## Category 4: Integration & Streaming

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q3-012 | For the WeChat Mini Program SSE limitation, should we: (a) use WebSocket exclusively for Mini Program, (b) use wx.request enableChunked with polling fallback, or (c) implement a unified WebSocket-based streaming for all platforms? Option (c) simplifies backend but loses SSE benefits on web/app. | Integration | Pending | |
| Q3-013 | For payment integration (5 providers), should we: (a) implement each provider adapter directly, (b) use an open-source payment abstraction layer, or (c) route through a single payment gateway aggregator service? This affects maintenance and adding new providers. | Integration | Pending | |
| Q3-014 | For notification delivery across 4 channels (in-app, push, SMS, email), should the notification-service: (a) directly call each channel API, (b) use a channel-adapter plugin architecture, or (c) use RabbitMQ fanout to channel-specific workers? The PRD requires extensibility for future channels. | Integration | Pending | |

## Category 5: Deployment & Operations

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q3-015 | For multi-region deployment (GDPR EU + PIPL China), should the architecture use: (a) fully independent clusters with no cross-region data flow, (b) independent clusters with shared global services (user auth, billing), or (c) single cluster with data routing? Option (b) complicates auth but optimizes user experience for travelers. | Deployment | Pending | |
| Q3-016 | For the MVP (Month 6), should we deploy all 10 microservices from day one, or start with a modular monolith (single deployable with module boundaries) and decompose into microservices post-MVP? Trade-off: monolith is faster to develop/deploy but requires later refactoring. | Deployment | Pending | |
| Q3-017 | For canary releases (NFR-18), should we use: (a) Argo Rollouts with K8s traffic splitting, (b) Spring Cloud Gateway weighted routing, or (c) Istio traffic management? This also affects A/B testing for AI prompt variants. | Deployment | Pending | |

## Category 6: Security & Compliance

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q3-018 | For the age verification gate (under 13 GDPR / under 14 PIPL), should parental consent be verified via: (a) parent email confirmation link, (b) parent SMS OTP verification, (c) parent account login + consent toggle, or (d) all of the above? This affects the auth flow complexity. | Security | Pending | |
| Q3-019 | For content moderation of uploaded images, should we: (a) use a dedicated moderation API (e.g., cloud provider moderation service), (b) use the same multimodal LLM for moderation as a pre-check, or (c) implement a lightweight on-premise classifier? Trade-off: (a) adds external dependency; (b) increases LLM cost; (c) needs ML expertise. | Security | Pending | |
| Q3-020 | For the 7-day account deletion cooling period (GDPR right to erasure), should deleted data be: (a) soft-deleted with flag + background cleanup job, (b) moved to a quarantine schema + cleaned after 7 days, or (c) encrypted with a key that is destroyed after 7 days (crypto-shredding)? | Security | Pending | |

## Category 7: Frontend & Client Architecture

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q3-021 | For the 3-codebase approach (Flutter + Angular + Mini Program), should we maintain a shared API client library via OpenAPI Generator, or let each team implement API calls independently? Shared generator ensures consistency but adds a code-gen step to CI. | Frontend | Pending | |
| Q3-022 | For Flutter offline mode (error notebook), should we use: (a) Hive (key-value, fast, encrypted), (b) sqflite (SQLite, relational queries), or (c) Drift (type-safe SQLite ORM for Dart)? The error notebook has relational data (filters by subject, knowledge point, date, difficulty). | Frontend | Pending | |
| Q3-023 | For the Admin Console (Angular + NG-ZORRO), should it be: (a) a separate deployment with its own API gateway route, (b) part of the same web deployment with role-based UI rendering, or (c) a completely separate SPA with its own backend-for-frontend (BFF)? | Frontend | Pending | |
