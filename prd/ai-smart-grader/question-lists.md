# Question Lists - AI Smart Grader PRD

> Records all question lists generated during requirements elicitation.

---

## Question List - Phase 3: Module 1 - AI Grading Engine
- Generated: 2026-02-28
- Status: Answered

1. What should happen when image quality is too low for AI to analyze (blurry, dark, cropped)?
   - Answer: Reject + re-upload prompt. Pre-validate image quality before sending to AI; reject with tips.
2. For multi-image uploads, should each image be treated as a separate submission or combined as one assignment?
   - Answer: User chooses per upload — option to upload as separate items or group as one multi-page assignment.
3. Should the AI auto-detect the subject and academic level from the image content?
   - Answer: Auto-detect + user override. AI auto-detects and pre-fills; user can correct before submission.
4. Should users be able to select which AI model to use?
   - Answer: Yes, users can choose which AI to use; system provides a default AI if user doesn't choose.
5. For "similar question recommendations", should these be AI-generated or from a question bank?
   - Answer: Hybrid — AI generates on-the-fly + supplement from question bank if available.
6. Should the system show a confidence indicator for AI grading results?
   - Answer: Yes, show confidence score alongside grading results.

## Question List - Phase 3: Module 2 - Intelligent Error Notebook
- Generated: 2026-02-28
- Status: Answered

1. Should ALL incorrect answers be auto-added to the error notebook, or should users choose?
   - Answer: Auto-add all + user can remove. All errors auto-added; user can dismiss entries they don't want.
2. Should Ebbinghaus spaced repetition intervals be adjustable per student?
   - Answer: Admin default + student override. Admin sets defaults; students can adjust within allowed ranges.
3. What does a "review" session look like?
   - Answer: Practice question test. System presents a similar practice question; student must answer correctly to mark as mastered.
4. Should the error notebook support manual entry from non-AI sources?
   - Answer: Yes, support manual entry. Students can manually add errors from any source.
5. What is the maximum error notebook capacity per user per tier?
   - Answer: Fully configurable in admin portal by user level. No hardcoded defaults.

## Question List - Phase 3: Module 3 - Learning Analytics & Reports
- Generated: 2026-02-28
- Status: Answered

1. For teacher class analytics, what time granularity should be supported?
   - Answer: Not explicitly asked; will default to daily/weekly/monthly/custom date range (standard analytics granularity).
2. Should parents receive automated periodic reports or only view on-demand?
   - Answer: Both — on-demand in-app + configurable automated periodic summaries (frequency configurable).
3. Should the system generate AI-powered study recommendations based on analytics?
   - Answer: Not explicitly asked; will include as a Should Have feature based on competitive research.

## Question List - Phase 3: Module 4 - User & Account Management
- Generated: 2026-02-28
- Status: Answered

1. Can a student be linked to multiple parents, and can a parent be linked to multiple children?
   - Answer: Many-to-many. Multiple parents per student; multiple children per parent.
2. How is the guest uniquely identified for quota tracking?
   - Answer: Device fingerprint.
3. Should there be age verification or parental consent for underage students?
   - Answer: Yes, mandatory age gate. Under-13/16 requires parental consent flow.

## Question List - Phase 3: Module 5 - Subscription & Payment
- Generated: 2026-02-28
- Status: Answered

1. What are the default grading quotas per membership tier?
   - Answer: Fully admin-configurable per membership tier. No hardcoded defaults.
2. Should the system support monthly and annual billing, or additional cycles?
   - Answer: Admin-configurable billing periods. Admin can define any billing cycle duration.
3. For the Pro (institution) tier, how should pricing be structured?
   - Answer: Fully admin-configurable pricing model per institution.

## Question List - Phase 3: Module 6 - Notification System
- Generated: 2026-02-28
- Status: Answered

1. Should review reminders include a direct deep-link to the specific error notebook entry?
   - Answer: Yes, deep-link directly to the specific error entry for immediate review.
2. Should teachers be able to push custom notifications to their class?
   - Answer: Yes, free-text custom messages to class or individual students.

## Question List - Phase 3: Module 7 - Admin Console
- Generated: 2026-02-28
- Status: Answered

1. For AI Prompt A/B testing, what metrics should be tracked?
   - Answer: Admin-defined metrics. Admin configures which metrics to track per A/B test experiment.
2. Should the admin console support multi-tenant administration?
   - Answer: Yes, full multi-tenant with isolated admin views per institution.

## Question List - Phase 3: Module 8 - Platform & Infrastructure
- Generated: 2026-02-28
- Status: Answered

1. Should cached error notebook entries auto-sync on reconnect?
   - Answer: Auto-sync on reconnect with conflict resolution prompts for conflicting changes.
2. Should the system provide a self-service data deletion option?
   - Answer: Self-service with 7-day cooling period before permanent deletion (user can cancel during this period).
