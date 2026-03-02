# UML Sequence Diagram — Spaced Repetition Review Flow

## Description
Shows the flow when a student opens their error notebook for a scheduled review session: loading due entries, attempting practice questions, evaluating mastery, updating review schedules, and publishing events.

## Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Student
    participant Client as Flutter/Angular App
    participant Gateway as API Gateway
    participant ErrorSvc as Error Notebook Service
    participant DB as PostgreSQL
    participant Redis as Redis Cache
    participant LLM as LLM Provider
    participant MQ as RabbitMQ
    participant ObjStore as MinIO

    Student->>Client: Open Error Notebook
    Client->>Gateway: GET /api/v1/error-notebook/due-reviews?subject={s}&limit=20
    Gateway->>ErrorSvc: Forward request (X-Tenant-Id, X-User-Id headers)

    ErrorSvc->>DB: Query error entries WHERE next_review_date <= NOW() ORDER BY priority
    DB-->>ErrorSvc: Due entries (with knowledge point tags, original image refs)
    ErrorSvc-->>Gateway: 200 {dueEntries[], totalDue, nextReviewSummary}
    Gateway-->>Client: Due review entries
    Client-->>Student: Display review list (grouped by subject/knowledge point)

    Student->>Client: Start review session
    Client->>Gateway: POST /api/v1/error-notebook/review-sessions
    Gateway->>ErrorSvc: Create review session
    ErrorSvc->>DB: INSERT review_session (status: IN_PROGRESS)
    ErrorSvc-->>Gateway: 200 {sessionId}

    loop For each error entry in review
        Client-->>Student: Show original error (image + correct answer + explanation)
        Student->>Client: Mark as "understood" or "still confused"

        alt Student requests mastery test
            Client->>Gateway: GET /api/v1/error-notebook/entries/{entryId}/practice
            Gateway->>ErrorSvc: Get practice question

            ErrorSvc->>DB: Query pre-generated practice question

            alt Practice question exists (pre-generated)
                DB-->>ErrorSvc: Practice question
            else No pre-generated question
                ErrorSvc->>LLM: Generate similar practice question on-demand
                LLM-->>ErrorSvc: Generated question
                ErrorSvc->>DB: Cache generated question for future use
            end

            ErrorSvc-->>Gateway: 200 {practiceQuestion}
            Gateway-->>Client: Practice question
            Client-->>Student: Display practice question

            Student->>Client: Submit answer
            Client->>Gateway: POST /api/v1/error-notebook/entries/{entryId}/mastery-test
            Gateway->>ErrorSvc: Evaluate mastery

            ErrorSvc->>ErrorSvc: Evaluate answer correctness

            alt Mastery ACHIEVED
                ErrorSvc->>DB: UPDATE entry SET status = 'MASTERED', mastery_date = NOW()
                ErrorSvc->>ErrorSvc: Remove from active review schedule
                ErrorSvc->>MQ: Publish MasteryAchieved event
            else Mastery NOT achieved
                ErrorSvc->>ErrorSvc: Calculate next review interval (current_interval * factor)
                ErrorSvc->>DB: UPDATE entry SET next_review_date = calculated_date, review_count += 1
            end
        else Student skips mastery test
            ErrorSvc->>ErrorSvc: Recalculate based on self-assessment

            alt Marked "understood"
                ErrorSvc->>DB: Advance to next interval (3d -> 7d -> 14d -> 30d)
            else Marked "still confused"
                ErrorSvc->>DB: Reset to shortest interval (1d)
            end
        end

        ErrorSvc->>DB: INSERT review_record (entryId, sessionId, result, timestamp)
    end

    Client->>Gateway: PUT /api/v1/error-notebook/review-sessions/{sessionId}/complete
    Gateway->>ErrorSvc: Complete session
    ErrorSvc->>DB: UPDATE review_session SET status = 'COMPLETED', summary stats
    ErrorSvc->>MQ: Publish ReviewSessionCompleted event {entriesReviewed, masteredCount, accuracy}
    ErrorSvc-->>Gateway: 200 {sessionSummary}
    Gateway-->>Client: Session summary
    Client-->>Student: Display review summary (entries reviewed, mastered, accuracy, streak)

    Note over MQ: Downstream event processing
    MQ-->>MQ: analytics-service consumes for dashboard aggregation
    MQ-->>MQ: notification-service sends parent report (if configured)
```

## Notes
- **Fixed-interval spaced repetition**: Intervals of 1d, 3d, 7d, 14d, 30d — admin-configurable via Nacos
- **Schema FSRS-ready**: Database schema includes `stability`, `difficulty`, `elapsed_days` fields for future FSRS algorithm upgrade
- **Pre-generated practice questions**: Most practice questions are pre-generated asynchronously; on-demand LLM generation as fallback
- **Dual assessment modes**: Student self-assessment ("understood"/"confused") or active mastery test with practice questions
- **Mastery promotion**: Entries achieving mastery are removed from active review queue; tracked for weakness analysis trends
- **Event-driven**: ReviewSessionCompleted and MasteryAchieved events flow to analytics and notification services
- **Capacity awareness**: Capacity enforcer (not shown) may auto-archive oldest mastered entries when tier limit reached
