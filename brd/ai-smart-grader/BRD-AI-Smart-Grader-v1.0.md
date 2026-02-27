# Business Requirements Document (BRD)

## Document Control

| Field | Value |
|-------|-------|
| Document Title | AI Smart Grader — Business Requirements Document |
| Version | 1.0 |
| Date | 2026-02-27 |
| Author | BRD Writer AI Agent |
| Status | Draft |
| Reviewer(s) | Project Sponsor / Stakeholders |

### Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1 | 2026-02-27 | BRD Writer AI Agent | Initial draft |
| 1.0 | 2026-02-27 | BRD Writer AI Agent | Complete BRD with all sections populated |

---

## 1. Executive Summary

AI Smart Grader is a cloud-native, AI-powered intelligent homework grading and error notebook platform designed for global users. The platform enables students across all academic levels (primary school through university) and all subjects to photograph and upload their completed exercises, which are then analyzed by AI large language models to provide instant grading results, step-by-step solution explanations, knowledge point annotations, difficulty ratings, and similar question recommendations. The system's core differentiator is its intelligent error notebook that automatically collects incorrect answers and provides classification, knowledge point tagging, review reminders based on the Ebbinghaus forgetting curve, statistical analysis, weakness identification, and personalized exercise recommendations. The platform serves five user roles — students, teachers, parents, system administrators, and guests — across four client channels: WeChat Mini Program, native App (iOS/Android), Web, and H5 mobile. The backend is built on Java with Spring Cloud microservices and Spring AI for LLM integration, following a fully open-source, commercially licensable technology stack. The business model combines freemium tiers (Free/Basic/Premium), institutional licensing (Pro), and value-added services, with all business rules, quotas, and system parameters configurable through a comprehensive administration console.

---

## 2. Business Objectives

| ID | Objective | Success Metric | Target | Timeline |
|----|-----------|---------------|--------|----------|
| BO-01 | Launch MVP with core AI grading and error notebook functionality | MVP live on at least 2 client platforms | Functional release on Web + WeChat Mini Program | Month 6 |
| BO-02 | Acquire initial user base during cold-start phase | Registered users | 10,000 - 50,000 registered users | Month 6 |
| BO-03 | Achieve product-market fit with active daily usage | DAU | 1,000 - 5,000 DAU | Month 6 |
| BO-04 | Scale user base through growth phase | Registered users / DAU | 50,000 - 500,000 registered / 5,000 - 50,000 DAU | Month 12 |
| BO-05 | Establish revenue through subscription and advertising | Monthly Recurring Revenue (MRR) | Positive MRR from subscription + ads | Month 9 |
| BO-06 | Expand to all four client platforms | Platform coverage | WeChat Mini Program + App + Web + H5 all live | Month 12 |
| BO-07 | Onboard teachers and institutions | Teacher/institution accounts | 500+ teacher accounts, 50+ institutions | Month 18 |
| BO-08 | Achieve scale across global markets | Registered users / DAU | 500,000 - 5,000,000 registered / 50,000 - 500,000 DAU | Month 24 |

---

## 3. Project Background & Context

### 3.1 Business Problem / Opportunity

**Problem Statement:**

Students at all academic levels face a common pain point: after completing exercises or practice tests independently, they lack timely and accurate feedback on their work. Traditional grading relies on teachers or parents, which is time-consuming, inconsistent, and often delayed. Teachers are burdened by repetitive grading tasks that consume time better spent on instruction. Parents want visibility into their children's learning progress but lack accessible tools.

**Market Opportunity:**

The global AI in education market reached USD 7.05 billion in 2025 and is projected to grow to USD 136.79 billion by 2035 at a CAGR of 34.52%. Student AI usage surged from 66% in 2024 to 92% in 2025, and 85% of teachers reported using AI tools. The industry is shifting from simple "photo search for answers" to "AI-powered tutoring with process explanation," creating a significant opportunity for a platform that combines intelligent grading with deep learning analytics through error notebooks.

**Key Competitors:**

| Competitor | Company | Positioning |
|-----------|---------|-------------|
| Kuaidui AI (快对AI) | Zuoyebang (作业帮) | Question bank + AI personalized tutoring |
| Xiaoyuan AI (小猿AI) | Yuanfudao (猿辅导) | Error attribution + knowledge graph explanation |
| Xueersi (学而思) | TAL Education | Learning devices + LLM-powered tutoring |
| Gauth AI | ByteDance | #1 US education app downloads (Q3 2025) |
| Photomath | Google | Photo-based math solving + step-by-step explanation |
| Socratic | Google | Multi-subject AI learning assistant |

**Differentiation:** AI Smart Grader differentiates through its **deep error analysis and intelligent error notebook** as the core value proposition, combined with a **multi-role ecosystem** (student-teacher-parent), **highly configurable AI and business rules**, and **global multi-platform coverage** built on open-source, cloud-native architecture.

### 3.2 Current State (As-Is)

- Students complete exercises on paper or digital formats without immediate feedback
- Teachers manually grade assignments, consuming significant time (estimated 5-10 hours/week for a typical teacher)
- Parents have limited visibility into their children's specific learning weaknesses
- Existing photo-search apps focus on providing answers rather than deep analysis and error pattern tracking
- No unified platform connecting students, teachers, and parents around the homework grading workflow
- Error notebooks are maintained manually by students (if at all), lacking systematic analysis

### 3.3 Future State (To-Be)

- Students upload exercise photos from any device and receive AI-powered grading with detailed explanations within 5-8 seconds
- An intelligent error notebook automatically collects and categorizes mistakes, identifies knowledge weaknesses, and recommends targeted review
- Teachers manage classes, view student error analytics, and access knowledge mastery reports — reducing grading burden by 80%+
- Parents access learning reports showing their children's progress, error trends, and knowledge point mastery
- System administrators configure AI prompts, business rules, pricing, and all system parameters through a comprehensive admin console
- All business rules, quotas, limits, and strategies are configurable without code changes
- The platform serves global users across WeChat Mini Program, App, Web, and H5

---

## 4. Project Scope

### 4.1 In Scope

- **Core AI Grading**: Photo upload, AI-powered grading, result display with step-by-step explanations, knowledge point annotation, difficulty rating, similar question recommendations
- **Error Notebook**: Error collection, classification, knowledge point tagging, review reminders (Ebbinghaus curve), statistical analysis, weakness identification, personalized recommendations
- **Multi-Role Support**: Student, Teacher, Parent, System Administrator, Guest (unauthenticated) user roles
- **Multi-Platform Clients**: WeChat Mini Program, native App (iOS/Android), Web browser, H5 mobile
- **Teacher Features**: Class management, student error analysis, knowledge mastery reports
- **Parent Features**: Learning report viewing
- **Admin Console**: User management, RBAC permissions, AI Prompt/Model management, content management, order/membership management, data statistics, system configuration, monitoring, operations tools, audit logs
- **Business Model**: Freemium (Free/Basic/Premium), Teacher/Institution Pro tier, value-added services
- **Payment Integration**: WeChat Pay, Alipay, Apple Pay, Google Pay, Stripe — extensible to additional payment providers
- **Authentication**: Phone number, email, WeChat, Google, Apple ID
- **Multi-Language**: Chinese and English
- **System Configurability**: 40 configurable parameters across AI engine, user/permissions, business rules, payments, notifications, and system operations
- **Offline Mode**: View previously saved error notebook entries without network
- **Data Export**: Error notebook PDF export, learning report export
- **Notifications**: Review reminders, grading completion, teacher assignment notifications — extensible
- **DevOps**: Canary releases, A/B testing, APM, ELK logging, alerting, resource monitoring
- **Compliance**: GDPR, Chinese data compliance

### 4.2 Out of Scope

- **Live tutoring / video conferencing** between students and teachers
- **Content creation tools** (teachers creating original questions/exams within the platform)
- **LMS (Learning Management System)** full course management and curriculum tracking
- **Hardware devices** (dedicated learning tablets or printers)
- **Social features** (student forums, chat between users)
- **Offline AI processing** (AI grading requires network connectivity)
- **On-premise deployment** (cloud-only in initial release)
- **Languages beyond Chinese and English** in initial release

---

## 5. Stakeholders

| ID | Name / Role | Department | Interest Level | Influence Level | RACI |
|----|------------|------------|---------------|-----------------|------|
| SH-01 | Project Sponsor | Executive | High | High | A |
| SH-02 | Project Manager | PMO | High | High | R |
| SH-03 | Product Owner | Product | High | High | C |
| SH-04 | Students (End Users) | — | High | Medium | C |
| SH-05 | Teachers (End Users) | — | High | Medium | C |
| SH-06 | Parents (End Users) | — | Medium | Low | I |
| SH-07 | Solution Architect | Engineering | High | High | C |
| SH-08 | Backend Development Team | Engineering | High | Medium | R |
| SH-09 | Frontend/Mobile Development Team | Engineering | High | Medium | R |
| SH-10 | AI/ML Engineering Team | Engineering | High | High | C |
| SH-11 | QA Lead | Quality | Medium | Medium | C |
| SH-12 | DevOps / SRE Team | Operations | Medium | Medium | C |
| SH-13 | Legal / Compliance | Legal | Medium | High | C |
| SH-14 | Data Protection Officer | Legal | Medium | High | C |
| SH-15 | UI/UX Design Team | Design | Medium | Medium | C |
| SH-16 | Marketing / Growth Team | Marketing | Medium | Medium | I |
| SH-17 | Customer Support | Operations | Low | Low | I |

---

## 6. Business Requirements

| ID | Requirement | Priority | Source | Acceptance Criteria |
|----|-------------|----------|--------|-------------------|
| BR-01 | Students shall upload exercise photos from mobile, tablet, or desktop devices via WeChat Mini Program, App, Web, or H5 | Must | SH-04 | Users can successfully upload JPG/PNG/PDF images from all 4 client platforms; multi-image upload supported |
| BR-02 | The system shall send uploaded images to an AI large language model for intelligent grading analysis | Must | SH-01 | Every uploaded image is processed by the configured AI model and returns a structured grading result |
| BR-03 | AI shall return comprehensive analysis: correct/incorrect judgment, correct answer, step-by-step solution explanation, knowledge point annotation, difficulty rating, and similar question recommendations | Must | SH-04, SH-05 | Each graded item includes all 6 analysis components; knowledge points are tagged from the system taxonomy |
| BR-04 | The system shall provide an intelligent error notebook that collects, classifies, and analyzes incorrect answers with knowledge point tags, review reminders, statistical analysis, weakness identification, and personalized exercise recommendations | Must | SH-04 | Error notebook correctly captures all incorrect answers; knowledge point weakness analysis identifies top 5 weak areas; review reminders follow configured intervals |
| BR-05 | The system shall support all academic subjects and all academic levels from primary school through university | Must | SH-01, SH-04 | AI Prompts are configured for all major subjects (Math, Chinese, English, Physics, Chemistry, Biology, History, Geography, etc.) across all levels |
| BR-06 | The system shall recognize both handwritten and printed text in uploaded images | Must | SH-04 | Recognition accuracy ≥ 90% for printed text; ≥ 80% for clearly written handwritten text |
| BR-07 | AI analysis prompts shall be configurable through the admin console, organized by subject, academic level, and question type | Must | SH-03, SH-10 | Admin can create, edit, version, and A/B test Prompt templates; changes take effect without code deployment |
| BR-08 | AI grading results shall be delivered using streaming response — showing correct/incorrect judgment first, then progressively loading detailed explanations | Should | SH-04, SH-10 | Users see the correct/incorrect result within 2 seconds; full explanation streams in progressively |

---

## 7. Functional Requirements

### 7.1 Guest (Unauthenticated User) Functions

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-01 | Guests shall have a configurable daily free AI grading quota (default: 3 times/day) without registration | Must | BR-01, BR-02 | Guest can use AI grading up to the configured limit; quota resets daily |
| FR-02 | First grading result for guests shall display complete analysis; subsequent results shall show correct/incorrect only, with full analysis unlocked after registration | Must | BR-03 | First result shows all 6 analysis components; 2nd+ results show only judgment; registration unlocks full history |
| FR-03 | Guest error data shall be temporarily stored on the device and synchronized to account upon registration | Must | BR-04 | Errors stored in device localStorage/fingerprint survive browser close; one-click sync on registration preserves all data |
| FR-04 | Grading results shall be shareable as cards; sharing earns additional free grading quota (configurable) | Should | BR-03 | Share card generates correctly; bonus quota credited within 5 seconds |
| FR-05 | Registration prompts shall appear naturally at the 2nd-3rd usage or when accessing error notebook statistics, not at first use | Must | — | No registration modal on first use; natural prompt appears at configured trigger points |

### 7.2 Student Functions

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-06 | Students shall upload single or multiple exercise images in all mainstream formats (JPG, PNG, PDF, HEIC, WebP) with configurable size limits | Must | BR-01 | Upload succeeds for all listed formats; multiple images processed in sequence; rejection with clear message if over size limit |
| FR-07 | Students shall view AI grading results including: original image with correct/incorrect markers, judgment result, correct answer, step-by-step explanation, knowledge point tags, difficulty rating, similar question recommendations, add-to-error-notebook button, share button | Must | BR-03 | Result page displays all 9 listed components; each component renders correctly |
| FR-08 | Students shall manage their error notebook: browse errors, filter by subject/knowledge point/date/difficulty, view error details, mark as mastered | Must | BR-04 | All filter combinations work correctly; mastered items move to "reviewed" section |
| FR-09 | Students shall receive review reminders for error notebook items based on configurable spaced repetition intervals (Ebbinghaus forgetting curve) | Must | BR-04 | Reminders trigger at configured intervals (e.g., 1d, 3d, 7d, 14d, 30d); students can mark items as reviewed |
| FR-10 | Students shall view learning statistics: error rate trends, knowledge point mastery chart, subject-wise analysis, study streak | Must | BR-04 | Statistics accurately reflect grading history; charts render correctly on all platforms |
| FR-11 | Students shall export their error notebook as PDF for printing | Should | BR-04 | PDF generated with clear formatting; includes original question, correct answer, and explanation |
| FR-12 | Students shall link their account with parent accounts via invitation code, QR code scan, or phone number association | Must | — | All 3 linking methods work; parent can view linked student's data after confirmation |

### 7.3 Teacher Functions

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-13 | Teachers shall create and manage classes; students join via class code, teacher invitation, or school batch import | Must | — | All 3 joining methods functional; teacher sees class roster with student list |
| FR-14 | Teachers shall view aggregated class error analysis: common errors, knowledge point weakness distribution, student-by-student breakdown | Must | BR-04 | Dashboard shows class-level and individual-student error analytics; data refreshes within 5 minutes of new submissions |
| FR-15 | Teachers shall access knowledge mastery reports: per-student and per-class knowledge point coverage, mastery trends over time | Must | BR-04 | Reports show knowledge point mastery percentages; exportable as PDF/CSV |
| FR-16 | Configurable limit on the number of classes a teacher can manage and the number of students per class | Must | — | Limits enforced per configuration; clear error message when limit reached |

### 7.4 Parent Functions

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-17 | Parents shall view their linked child's learning report: grading history, error trends, knowledge point mastery, study frequency | Must | BR-04 | Report accurately reflects child's data; read-only access (no modification) |
| FR-18 | Parents shall link to their child's account via invitation code, QR code scan, or phone number association | Must | — | All 3 linking methods work; child receives notification of parent link request |

### 7.5 Admin Console Functions

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-19 | User management: CRUD operations, role assignment (Student/Teacher/Parent/Admin), account status management, batch import/export | Must | BR-07 | All CRUD operations functional; batch import supports CSV/Excel with validation |
| FR-20 | RBAC permission management: role-based menu permissions, data permissions (teacher sees own classes only, parent sees own children only), API-level access control | Must | BR-07 | Permissions correctly enforced across all endpoints; unauthorized access returns 403 |
| FR-21 | AI Prompt template management: create/edit/delete templates by subject/academic level/question type, version control, A/B testing, effectiveness statistics | Must | BR-07 | Prompt versioning tracks changes; A/B test distributes traffic per configured ratio; effectiveness dashboard shows comparison metrics |
| FR-22 | AI model management: configure multiple LLM providers, manage API keys, monitor invocation volume and costs, set intelligent routing rules | Must | BR-07 | Multiple providers configurable simultaneously; cost dashboard shows per-model and aggregate spending |
| FR-23 | Content management: subject/knowledge point taxonomy management, question bank management (optional) | Should | BR-05 | Taxonomy supports hierarchical structure; knowledge points linkable to grading results |
| FR-24 | Order and membership management: membership tier configuration, order management, payment records, refund processing | Must | — | All membership tiers configurable; order lifecycle (create → pay → active → expire/refund) tracked |
| FR-25 | Data statistics dashboard: real-time DAU, AI invocation volume, grading success rate, revenue, trending knowledge points in errors | Must | — | Dashboard data refreshes within 1 minute; metrics match backend data within 1% |
| FR-26 | System configuration: system parameter management, multi-language resource management, notification template management, file storage configuration | Must | — | Parameter changes take effect without restart; i18n resources manageable online |
| FR-27 | System monitoring: service health, API response times, error logs, alert notifications | Must | — | Health checks cover all microservices; alerts trigger within 1 minute of threshold breach |
| FR-28 | Operations tools: announcement management, banner management, campaign/coupon management, message push | Should | — | Announcements display on all client platforms within 5 minutes of publishing |
| FR-29 | Audit logs: operation logs, login logs, sensitive operation records | Must | — | All admin actions logged with timestamp, operator, action, and affected resource |

### 7.6 Notification Functions

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-30 | System shall support configurable notification channels: in-app messages, push notifications, SMS, email | Must | — | Each channel independently toggleable per notification type in admin console |
| FR-31 | Notification types shall include: grading completion, review reminders, teacher assignment publication, system announcements — extensible for future types | Must | — | All listed notification types functional; new types addable through admin configuration |
| FR-32 | Users shall configure do-not-disturb time periods | Should | — | Notifications queued during DND period and delivered after |
| FR-33 | Notification templates shall be configurable in admin console, supporting multi-language | Must | — | Templates editable per language; variable substitution works correctly |

### 7.7 System Configurability Functions

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-34 | All AI engine parameters shall be configurable: model provider/routing, Prompt templates, request timeout, retry strategy, concurrency limits, cache strategy, intelligent routing rules (CFG-01~07) | Must | BR-07 | Each parameter changeable via admin console; changes effective without deployment |
| FR-35 | All user and permission parameters shall be configurable: role permissions, data permissions, login method toggles, password policy, session timeout (CFG-08~12) | Must | — | Parameter changes enforced on next user action/login |
| FR-36 | All business rule parameters shall be configurable: grading quotas per tier, guest limits, upload limits, image size/format, error notebook capacity, review reminder rules, sharing rewards, class/teacher limits (CFG-13~22) | Must | — | All 10 parameters adjustable; enforcement verified in real-time |
| FR-37 | All commercial parameters shall be configurable: membership pricing, payment channel toggles per region, ad configuration, coupon/promotion rules, trial period settings (CFG-23~27) | Must | — | Pricing changes reflected in client within 5 minutes; payment channels toggleable per country |
| FR-38 | All notification parameters shall be configurable: channel toggles, templates, trigger rules, DND periods (CFG-28~31) | Must | — | Notification behavior matches configured rules within 1 minute of change |
| FR-39 | All system and operations parameters shall be configurable: canary release rules, A/B test groups, alert thresholds, log levels, API rate limiting, storage configuration, i18n resources, data retention policy, maintenance mode toggle (CFG-32~40) | Must | — | Each parameter adjustable; maintenance mode immediately shows custom announcement |

---

## 8. Non-Functional Requirements

| ID | Category | Requirement | Priority | Acceptance Criteria |
|----|----------|-------------|----------|-------------------|
| NFR-01 | Architecture | The system shall adopt a frontend-backend separation, cloud-native architecture using Docker containers orchestrated by Kubernetes | Must | All services containerized; K8s orchestration functional with auto-scaling |
| NFR-02 | Technology | Backend shall use Java with Spring Cloud for microservice governance and Spring AI for LLM integration | Must | All backend services built on Spring Boot/Cloud; AI integration via Spring AI |
| NFR-03 | Technology | All technology stack components shall be open-source, mainstream, and commercially licensable (Apache 2.0, MIT, or equivalent) | Must | License audit confirms no GPL-only or proprietary dependencies in core stack |
| NFR-04 | Multi-Platform | The system shall support four client platforms: WeChat Mini Program, native App (iOS/Android), Web browser, and H5 mobile | Must | All 4 platforms pass functional acceptance testing |
| NFR-05 | Internationalization | The system shall support Chinese and English with configurable i18n resources managed through admin console | Must | Full UI/notification/error message coverage in both languages; language switchable at runtime |
| NFR-06 | AI Flexibility | The system shall support multiple AI LLM providers with configurable switching through admin console | Must | At minimum 3 providers configurable (e.g., OpenAI, Claude, Chinese model); switching takes effect within 1 minute |
| NFR-07 | Availability | The system shall achieve ≥ 99.9% uptime (≤ 8.76 hours downtime/year) | Must | Monitoring confirms 99.9%+ availability over rolling 30-day windows |
| NFR-08 | Performance | AI grading response time: P50 ≤ 5s, P90 ≤ 8s, P99 ≤ 15s (end-to-end from upload to result display) | Must | Load testing confirms targets under expected concurrency |
| NFR-09 | Scalability | Initial capacity planned for DAU 100,000 with architecture supporting 10x horizontal scaling without re-architecture | Must | Load test simulates 100K DAU workload; scaling test confirms 10x capacity with linear resource addition |
| NFR-10 | Compliance | The system shall comply with GDPR (EU) and Chinese data compliance regulations (PIPL, Data Security Law) | Must | Data processing agreements in place; user data deletion/export requests fulfillable within 30 days; data residency per regional requirements |
| NFR-11 | Payment | Payment integration shall include WeChat Pay, Alipay, Apple Pay, Google Pay, and Stripe, with extensible architecture for additional providers per country | Must | All 5 payment providers integrated; payment adapter interface allows adding new providers without core code changes |
| NFR-12 | Authentication | The system shall support authentication via phone number, email, WeChat OAuth, Google OAuth, and Apple ID | Must | All 5 auth methods functional; account linking between methods supported |
| NFR-13 | Security | The system shall implement data encryption (at-rest and in-transit), anti-scraping measures, API rate limiting, and image content moderation | Must | TLS 1.3 for transit; AES-256 for at-rest; rate limiting enforced per configuration; inappropriate image content blocked before AI processing |
| NFR-14 | Offline | The system shall support offline viewing of previously saved error notebook entries | Should | Cached error notebook entries viewable without network; sync on reconnection |
| NFR-15 | Export | The system shall support error notebook PDF export and learning report export | Should | PDF generated with correct formatting; download completes within 30 seconds for up to 500 error entries |
| NFR-16 | Notifications | The system shall support push notifications across in-app, push, SMS, and email channels — extensible for future channels | Must | All 4 channels functional; new channel types addable through plugin architecture |
| NFR-17 | Observability | The system shall implement APM (application performance monitoring), centralized logging (ELK Stack), alerting, resource monitoring, business dashboard, and AI quality monitoring | Must | APM tracks all service endpoints; ELK indexes all service logs; alerts fire within 1 minute of threshold breach |
| NFR-18 | Release | The system shall support canary releases and A/B testing capabilities | Should | Canary release rolls out to configurable user percentage; A/B tests track configured metrics per variant |

---

## 9. Data Requirements

### 9.1 Data Entities

**Core Entities:**

| Entity | Key Attributes | Relationships |
|--------|---------------|--------------|
| User | id, role, name, email, phone, avatar, language, membership_tier, status | Has many Submissions, ErrorNotebookEntries |
| Submission | id, user_id, images[], subject, academic_level, status, created_at | Belongs to User; Has many GradingResults |
| GradingResult | id, submission_id, question_index, is_correct, correct_answer, explanation, knowledge_points[], difficulty_rating, similar_questions[] | Belongs to Submission |
| ErrorNotebookEntry | id, user_id, grading_result_id, subject, knowledge_points[], status (active/mastered), next_review_date | Belongs to User and GradingResult |
| Class | id, teacher_id, name, class_code, student_count, max_students | Belongs to Teacher; Has many Students |
| ParentChildLink | id, parent_user_id, child_user_id, link_method, status | Links two Users |
| MembershipPlan | id, name, tier, price, duration, features[], grading_quota | Referenced by User |
| Order | id, user_id, plan_id, payment_channel, amount, status, created_at | Belongs to User and MembershipPlan |
| AIPromptTemplate | id, subject, academic_level, question_type, prompt_content, version, is_active, ab_test_group | Used by AI Engine |
| AIModelConfig | id, provider, model_name, api_key_ref, routing_rules, is_active | Used by AI Engine |
| SystemConfig | id, config_key, config_value, category, description | System-wide configuration |
| AuditLog | id, operator_id, action, resource_type, resource_id, timestamp, details | Tracks admin actions |
| Notification | id, user_id, type, channel, content, status, scheduled_at, sent_at | Belongs to User |

### 9.2 Data Flows

1. **Grading Flow**: Client → API Gateway → Image Service (upload to object storage) → AI Grading Service (call LLM via Spring AI) → Result Service (structure and store) → Client (streaming response)
2. **Error Notebook Flow**: Grading Result (incorrect) → Error Notebook Service (auto-collect or user-add) → Knowledge Point Tagging → Review Scheduler → Notification Service (reminders)
3. **Analytics Flow**: Grading Results + Error Notebook → Analytics Service (aggregate) → Teacher Dashboard / Parent Report / Admin Statistics
4. **Configuration Flow**: Admin Console → Config Service → Distributed Config Store → All Microservices (hot reload)

### 9.3 Data Migration (if applicable)

No legacy system data migration is required for initial launch. Future consideration: import functionality for students with existing error notebooks from other platforms (CSV/Excel import).

---

## 10. Assumptions

| ID | Assumption | Impact if Invalid |
|----|-----------|-------------------|
| AS-01 | AI LLM providers (OpenAI, Claude, Chinese models) will maintain stable API availability and pricing | Need to implement fallback model switching; cost model may require revision |
| AS-02 | Multimodal AI models can achieve ≥ 80% accuracy for handwritten text recognition across all supported subjects | May need supplementary OCR preprocessing or limit handwritten support to specific subjects initially |
| AS-03 | Users (students) have access to devices with cameras capable of capturing legible exercise photos | Need to provide image quality guidance and validation before AI processing |
| AS-04 | WeChat Mini Program, App Store, and Google Play approval processes will not block app publication | May need to adjust content or features to meet platform-specific review guidelines |
| AS-05 | Open-source Spring Cloud and Spring AI ecosystems will continue active development and LTS support | Need contingency plan for framework migration if abandoned |
| AS-06 | Global users have sufficient internet connectivity for image upload and AI result retrieval | Offline mode (error notebook viewing) mitigates partial connectivity; core grading requires online |
| AS-07 | The project has budget authorization for cloud infrastructure and AI API consumption costs | Infrastructure costs directly impact scalability timeline; need early cost modeling |
| AS-08 | User is treated as the default project sponsor with decision-making authority | Delays in decision-making if sponsor is unavailable |

---

## 11. Constraints

| ID | Type | Constraint | Impact |
|----|------|-----------|--------|
| CN-01 | Technology | Backend must use Java with Spring Cloud and Spring AI | Limits technology choices but ensures ecosystem consistency |
| CN-02 | Technology | All components must be open-source and commercially licensable | Excludes proprietary solutions that may offer superior features |
| CN-03 | Regulatory | Must comply with GDPR for EU users and PIPL/DSL for Chinese users | Requires region-specific data storage and processing; increases infrastructure complexity |
| CN-04 | Platform | Must support WeChat Mini Program (subject to WeChat platform restrictions) | WeChat Mini Program has file size limits, API restrictions, and review process constraints |
| CN-05 | Budget | AI API costs scale linearly with usage volume | Requires cost optimization strategies (caching, model routing, quota management) |
| CN-06 | Performance | AI model inference latency is bounded by external LLM provider response times | Cannot guarantee sub-second grading; streaming response mitigates perceived latency |
| CN-07 | Time | MVP must be achievable within 6 months | Scope prioritization required; some features deferred to post-MVP releases |

---

## 12. Dependencies

| ID | Dependency | Type | Owner | Status |
|----|-----------|------|-------|--------|
| DP-01 | AI LLM API access (OpenAI, Claude, Chinese model providers) | External | AI/ML Team | Open |
| DP-02 | Cloud infrastructure provisioning (Kubernetes cluster, object storage, databases) | External | DevOps Team | Open |
| DP-03 | WeChat Mini Program developer account and approval | External | Product Team | Open |
| DP-04 | App Store (iOS) and Google Play developer accounts and approval | External | Product Team | Open |
| DP-05 | Payment provider integration accounts (WeChat Pay, Alipay, Stripe, etc.) | External | Finance/Engineering | Open |
| DP-06 | SMS gateway provider for phone authentication and notifications | External | Engineering | Open |
| DP-07 | CDN provider for global content delivery | External | DevOps Team | Open |
| DP-08 | UI/UX design completion for all client platforms | Internal | Design Team | Open |
| DP-09 | Knowledge point taxonomy definition (subjects × academic levels) | Internal | Product/Content Team | Open |
| DP-10 | Legal review of Terms of Service, Privacy Policy, and data processing agreements | Internal | Legal Team | Open |

---

## 13. Risks & Mitigation

| ID | Risk | Probability | Impact | Mitigation Strategy | Owner |
|----|------|------------|--------|---------------------|-------|
| RK-01 | AI grading accuracy insufficient for user satisfaction (industry benchmark: 50-55% with rubrics) | High | High | Implement Prompt A/B testing and continuous optimization; provide user feedback mechanism for incorrect results; use AI quality monitoring dashboard | AI/ML Team |
| RK-02 | AI API costs exceed budget at scale (25万+ daily calls at DAU 50K) | Medium | High | Implement intelligent model routing (fast model for simple questions, deep model for complex); result caching for similar questions; configurable quotas per membership tier | Engineering / Finance |
| RK-03 | LLM provider service disruption or API changes | Medium | High | Multi-provider support with automatic failover; configurable retry and degradation strategies; monitor provider status | Engineering |
| RK-04 | Data compliance violations (GDPR/PIPL) | Low | Critical | Engage legal counsel early; implement data residency per region; provide data deletion/export capabilities; conduct privacy impact assessment | Legal / DPO |
| RK-05 | WeChat Mini Program or App Store rejection | Medium | Medium | Study platform guidelines early; implement content moderation; prepare contingency with H5/Web as primary channels | Product Team |
| RK-06 | Handwritten text recognition accuracy below expectations | Medium | Medium | Provide image quality tips to users; implement image pre-processing (contrast, rotation); fallback to printed-text-only mode for low-confidence images | AI/ML Team |
| RK-07 | User acquisition slower than projected | Medium | Medium | Invest in guest experience for zero-friction onboarding; implement sharing/referral rewards; partner with schools and institutions | Marketing / Growth |
| RK-08 | System performance degradation under scale | Low | High | Cloud-native auto-scaling; load testing at 10x projected DAU; APM monitoring with proactive alerts | DevOps / SRE |
| RK-09 | Competitor launches similar AI error notebook feature | Medium | Medium | Differentiate through depth of error analysis, configurability, and multi-role ecosystem; maintain fast iteration cycle | Product Team |
| RK-10 | Image content moderation fails (inappropriate content uploaded) | Low | High | Implement pre-AI content moderation filter; logging and audit trail for all uploads; automated blocking with human review escalation | Engineering / Trust & Safety |

---

## 14. Success Metrics & KPIs

| ID | KPI | Baseline | Target | Measurement Method | Frequency |
|----|-----|---------|--------|-------------------|-----------|
| KPI-01 | Daily Active Users (DAU) | 0 | 5,000 (Month 6) → 50,000 (Month 12) → 500,000 (Month 24) | Analytics platform | Daily |
| KPI-02 | AI Grading Accuracy Rate | N/A | ≥ 85% user-confirmed accuracy | User feedback (thumbs up/down) on grading results | Weekly |
| KPI-03 | AI Response Time P50 | N/A | ≤ 5 seconds | APM monitoring | Real-time |
| KPI-04 | Error Notebook Adoption Rate | 0% | ≥ 60% of active students use error notebook weekly | Feature usage analytics | Weekly |
| KPI-05 | Guest-to-Registered Conversion Rate | 0% | ≥ 15% | Registration funnel analytics | Weekly |
| KPI-06 | Paid Subscription Conversion Rate | 0% | ≥ 5% of registered users | Payment analytics | Monthly |
| KPI-07 | Monthly Recurring Revenue (MRR) | $0 | Positive MRR by Month 9 | Financial reporting | Monthly |
| KPI-08 | System Availability | N/A | ≥ 99.9% | Uptime monitoring | Monthly |
| KPI-09 | User Retention (Day 7) | 0% | ≥ 30% | Cohort analysis | Weekly |
| KPI-10 | User Retention (Day 30) | 0% | ≥ 15% | Cohort analysis | Monthly |
| KPI-11 | Teacher Account Adoption | 0 | 500+ teacher accounts by Month 18 | User management data | Monthly |
| KPI-12 | NPS (Net Promoter Score) | N/A | ≥ 40 | In-app survey | Quarterly |

---

## 15. Cost-Benefit Analysis

### 15.1 Estimated Costs

| Category | Item | Estimated Monthly Cost (at DAU 50K) |
|----------|------|-------------------------------------|
| Infrastructure | Cloud (K8s, databases, object storage, CDN) | $3,000 - $8,000 |
| AI API | LLM API calls (~250K/day = ~7.5M/month) | $5,000 - $15,000 |
| Third-Party Services | SMS, email, payment gateway fees | $500 - $2,000 |
| Development | Engineering team (ongoing) | Project-dependent |
| Operations | DevOps, monitoring, customer support | $1,000 - $3,000 |
| **Total Monthly Operational** | | **$9,500 - $28,000** |

### 15.2 Expected Benefits

| Benefit | Type | Estimated Value |
|---------|------|-----------------|
| Subscription revenue (5% conversion at $5-15/month avg) | Revenue | $12,500 - $37,500/month at DAU 50K |
| Advertising revenue (free tier) | Revenue | $2,000 - $5,000/month at DAU 50K |
| Teacher/Institution Pro subscriptions | Revenue | $5,000 - $15,000/month with 50+ institutions |
| Reduced teacher grading time (80%+ efficiency gain) | Qualitative | Significant teacher satisfaction and word-of-mouth |
| Student learning improvement through targeted error review | Qualitative | Core value proposition driving retention |

### 15.3 ROI Projection

- **Break-even point**: Estimated at Month 12-18 (excluding initial development cost)
- **Revenue model scales favorably**: AI API costs are the primary variable cost; subscription revenue grows linearly with paying users while AI costs can be optimized through caching and routing
- **Long-term ROI**: At DAU 500K (Year 2-3), projected monthly revenue of $100K-$300K against operational costs of $50K-$100K

---

## 16. Implementation Timeline

| Milestone | Target Date | Dependencies | Owner |
|-----------|------------|-------------|-------|
| BRD Approved | Month 0 | — | PM / Sponsor |
| PRD & Architecture Design Complete | Month 1 | BRD approval | Product / Architecture |
| UI/UX Design Complete | Month 2 | PRD | Design Team |
| MVP Development (Core AI Grading + Error Notebook) | Month 2-5 | Architecture, Design | Engineering |
| MVP Testing & QA | Month 5 | MVP Development | QA Team |
| MVP Launch (Web + WeChat Mini Program) | Month 6 | QA signoff, Platform approval | All Teams |
| Payment & Membership Integration | Month 6-7 | MVP Launch | Engineering / Finance |
| App (iOS/Android) Launch | Month 7-9 | MVP stability | Mobile Team |
| Teacher & Parent Features | Month 8-10 | MVP Launch | Engineering |
| H5 Mobile Launch | Month 9 | MVP stability | Frontend Team |
| Admin Console Full Features | Month 10-12 | Core platform stable | Engineering |
| Global Expansion (Multi-language, Multi-region) | Month 12+ | All platforms live | All Teams |

---

## 17. Glossary

| Term | Definition |
|------|-----------|
| AI Smart Grader | The platform name for this AI-powered intelligent homework grading and error notebook system |
| Error Notebook (错题本) | A digital collection of incorrectly answered questions with analysis, categorization, and spaced repetition review capabilities |
| LLM | Large Language Model — AI models capable of understanding and generating text, including multimodal models that process images |
| Spring AI | An open-source Spring framework module for integrating AI/LLM capabilities into Java applications |
| Spring Cloud | An open-source Spring framework for building cloud-native microservice architectures in Java |
| Multimodal | AI models capable of processing multiple input types (text, images, audio) simultaneously |
| OCR | Optical Character Recognition — technology for recognizing text in images |
| Prompt | The instruction text sent to an AI model that guides its analysis behavior |
| Streaming Response | A technique where AI results are delivered progressively rather than waiting for complete generation |
| Ebbinghaus Forgetting Curve | A memory model describing the exponential decline of memory retention over time; used to schedule optimal review intervals |
| RBAC | Role-Based Access Control — permission model assigning access rights based on user roles |
| DAU | Daily Active Users — unique users who interact with the platform in a given day |
| MRR | Monthly Recurring Revenue — predictable monthly revenue from subscriptions |
| MVP | Minimum Viable Product — the smallest feature set that delivers core value for initial launch |
| GDPR | General Data Protection Regulation — EU data privacy regulation |
| PIPL | Personal Information Protection Law — China's data privacy regulation |
| DSL | Data Security Law — China's data security regulation |
| Canary Release | A deployment strategy that gradually rolls out changes to a small subset of users before full deployment |
| A/B Testing | An experimentation method comparing two variants to determine which performs better |
| APM | Application Performance Monitoring — tools for tracking application health and performance |
| ELK Stack | Elasticsearch, Logstash, Kibana — an open-source log management and analytics platform |
| CDN | Content Delivery Network — a distributed network for fast content delivery to global users |
| P50/P90/P99 | Percentile metrics — P50 means 50% of requests are faster; P90 means 90% are faster; P99 means 99% are faster |
| CAGR | Compound Annual Growth Rate |
| QPS | Queries Per Second — a measure of system throughput |

---

## 18. Appendices

### Appendix A: Core User Flow Diagram

```
[Student/Guest]
    |
    v
[Open App/Mini Program/Web/H5]
    |
    v
[Capture/Upload Exercise Photo(s)]
    |
    v
[Image Pre-processing: compression, rotation, quality check]
    |
    v
[AI Model Selection (intelligent routing based on subject/complexity)]
    |
    v
[LLM Analysis: grading + explanation + knowledge points]
    |
    v
[Streaming Result Display]
    |-- Correct → Show explanation, knowledge points, difficulty, similar questions
    |-- Incorrect → Show all above + "Add to Error Notebook" (auto-prompted)
    |
    v
[Error Notebook]
    |-- Browse / Filter by subject, knowledge point, date, difficulty
    |-- Review reminders (Ebbinghaus spaced repetition)
    |-- Statistics: error rate trends, weakness identification
    |-- Personalized exercise recommendations
    |-- Export as PDF
```

### Appendix B: Requirements Traceability Matrix

| Requirement ID | Source | Related Requirements | Test Case |
|---------------|--------|---------------------|-----------|
| BR-01 | SH-04 | FR-01, FR-06, NFR-04 | TC-Upload-01: Upload from all 4 platforms |
| BR-02 | SH-01 | FR-34, NFR-02, NFR-06 | TC-AI-01: AI model invocation and result return |
| BR-03 | SH-04, SH-05 | FR-02, FR-07, NFR-08 | TC-Result-01: Result page displays all components |
| BR-04 | SH-04 | FR-08, FR-09, FR-10, FR-11, FR-14, FR-15, FR-17 | TC-ErrorBook-01: Error collection and review cycle |
| BR-05 | SH-01, SH-04 | FR-21, FR-23, NFR-05 | TC-Subject-01: All subjects and levels supported |
| BR-06 | SH-04 | FR-06, NFR-13 | TC-OCR-01: Handwritten and printed text recognition |
| BR-07 | SH-03, SH-10 | FR-21, FR-22, FR-34 | TC-Admin-01: Prompt and model configuration |
| BR-08 | SH-04, SH-10 | NFR-08 | TC-Perf-01: Streaming response latency |

### Appendix C: System Configurability Matrix (CFG-01 to CFG-40)

| Category | IDs | Count | Description |
|----------|-----|-------|-------------|
| AI Engine | CFG-01~07 | 7 | Model routing, Prompt templates, timeout, retry, concurrency, cache, routing rules |
| User & Permissions | CFG-08~12 | 5 | Role permissions, data permissions, login toggles, password policy, session timeout |
| Business Rules | CFG-13~22 | 10 | Grading quotas, guest limits, upload limits, error notebook capacity, review rules, sharing rewards, class limits |
| Commerce & Payment | CFG-23~27 | 5 | Pricing, payment channels, ads, coupons, trial periods |
| Notifications | CFG-28~31 | 4 | Channel toggles, templates, trigger rules, DND periods |
| System & Operations | CFG-32~40 | 9 | Canary release, A/B testing, alerts, logging, rate limiting, storage, i18n, data retention, maintenance mode |
| **Total** | | **40** | |

### Appendix D: Supporting Documents

| Document | Location | Description |
|----------|----------|-------------|
| Conversation Log | `brd/ai-smart-grader/conversation-log.md` | Full record of all stakeholder interactions during BRD creation |
| Question Lists Log | `brd/ai-smart-grader/question-lists.md` | All question lists generated and answered summaries |
| Research Log | `brd/ai-smart-grader/research-log.md` | All industry research actions, findings, and sources |
| Work Log | `brd/ai-smart-grader/work-log.md` | Timeline of all BRD creation activities |

---

## 19. Approval Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor | _________ | _________ | _________ |
| Project Manager | _________ | _________ | _________ |
| Business Analyst | BRD Writer AI Agent | _________ | 2026-02-27 |
