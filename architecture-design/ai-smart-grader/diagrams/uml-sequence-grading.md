# UML Sequence Diagram — AI Grading Flow

## Description
Shows the end-to-end flow when a student uploads an exercise image and receives AI grading results via streaming. Covers image upload, content moderation, cache check, LLM invocation, real-time response parsing, result persistence, and downstream event publishing.

## Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Student
    participant Client as Flutter/Angular/Mini Program
    participant Gateway as API Gateway
    participant ImageSvc as Image Service
    participant ModAPI as Content Moderation API
    participant ObjStore as MinIO
    participant GradingSvc as Grading Service
    participant Redis as Redis Cache
    participant LLM as LLM Provider
    participant OCR as PaddleOCR
    participant DB as PostgreSQL
    participant MQ as RabbitMQ

    Student->>Client: Capture/select exercise photo
    Client->>Gateway: POST /api/v1/images/upload (multipart)
    Gateway->>Gateway: JWT validation, rate limit check, tenant context injection

    Gateway->>ImageSvc: Forward upload request
    ImageSvc->>ImageSvc: Validate format, size, quality (blur detection)
    ImageSvc->>ModAPI: Pre-screen image (content moderation)
    ModAPI-->>ImageSvc: Moderation result (PASS/REJECT)

    alt Moderation REJECTED
        ImageSvc-->>Gateway: 422 Content rejected
        Gateway-->>Client: Error: inappropriate content
    end

    ImageSvc->>ImageSvc: Format conversion, compression, metadata extraction
    ImageSvc->>ObjStore: Store processed image (S3 PUT)
    ObjStore-->>ImageSvc: Image URL + ETag
    ImageSvc-->>Gateway: 200 {imageId, imageUrl}
    Gateway-->>Client: Image uploaded successfully

    Client->>Gateway: POST /api/v1/grading/submit {imageId, subject, gradeLevel}
    Gateway->>GradingSvc: Forward grading request

    GradingSvc->>GradingSvc: Compute SHA-256 + pHash of image
    GradingSvc->>Redis: Check dual-layer cache (exact hash, perceptual hash)

    alt Cache HIT
        Redis-->>GradingSvc: Cached grading result
        GradingSvc-->>Gateway: 200 Cached result (SSE stream)
        Gateway-->>Client: Stream cached result
        Client-->>Student: Display grading results (instant)
    end

    Note over GradingSvc: Cache MISS — invoke LLM pipeline

    GradingSvc->>GradingSvc: Complexity estimation (image metadata + question count)
    GradingSvc->>GradingSvc: Cascade routing (subject + complexity + user tier)
    GradingSvc->>GradingSvc: Assemble prompt template (+ A/B variant selection)

    Client->>Gateway: GET /api/v1/grading/{taskId}/stream (SSE/WebSocket)
    Gateway->>GradingSvc: Establish streaming connection

    GradingSvc->>LLM: Send image + prompt (REST + SSE stream)

    loop For each streamed chunk
        LLM-->>GradingSvc: Streaming token chunk
        GradingSvc->>GradingSvc: Real-time structured parsing (judgment/answer/explanation/knowledge points)
        GradingSvc-->>Gateway: SSE event {type, questionIndex, partialData}
        Gateway-->>Client: Forward SSE/WebSocket event
        Client-->>Student: Progressive UI update (per-question results)
    end

    GradingSvc->>GradingSvc: Confidence scoring on parsed results

    alt Low Confidence (handwriting < threshold)
        GradingSvc->>OCR: Extract text via PaddleOCR
        OCR-->>GradingSvc: Extracted text
        GradingSvc->>LLM: Re-grade with OCR-enhanced text
        LLM-->>GradingSvc: Enhanced grading result
    end

    GradingSvc->>GradingSvc: Finalize per-question structured results
    GradingSvc->>Redis: Cache result (SHA-256 key + pHash key, TTL: 24h)
    GradingSvc->>DB: Persist grading_session + grading_results (per-question)
    GradingSvc->>MQ: Publish GradingCompleted event

    GradingSvc-->>Gateway: SSE complete event
    Gateway-->>Client: Stream complete
    Client-->>Student: Display final grading results with knowledge point tags

    Note over MQ: Downstream event processing
    MQ-->>MQ: Route to error-notebook (auto-collect errors)
    MQ-->>MQ: Route to analytics (aggregate stats)
    MQ-->>MQ: Route to notification (notify completion)
```

## Notes
- **Two-phase flow**: Image upload (sync) followed by grading submission (async streaming)
- **Content moderation gate**: Images pre-screened before any LLM call — rejected images never reach grading
- **Dual-layer cache check**: SHA-256 exact hash + pHash perceptual hash checked before LLM invocation
- **Cascade routing**: LLM selection based on subject + complexity estimation + user tier
- **Real-time structured parsing**: LLM stream parsed in-flight, extracting per-question results progressively
- **OCR fallback**: Triggered only when confidence scorer detects low-confidence handwriting recognition
- **Event fan-out**: GradingCompleted event consumed by 3 downstream services (error-notebook, analytics, notification)
- **Streaming protocols**: SSE for Web/Flutter clients; WebSocket for WeChat Mini Program (transparent at gateway)
