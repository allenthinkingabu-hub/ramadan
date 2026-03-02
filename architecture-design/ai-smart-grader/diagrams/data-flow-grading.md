# Data Flow Diagram — AI Grading Pipeline

## Description
Shows how data flows through the AI grading pipeline, from image capture to final result storage and downstream event processing. Highlights data transformations at each stage.

## Diagram

```mermaid
flowchart LR
    subgraph "Input"
        A[/"📷 Exercise Photo\n(JPEG/PNG, ≤10MB)"/]
    end

    subgraph "Image Service"
        B[Format Validation\nsize, type, dimensions]
        C[Content Moderation\nCloud API pre-screen]
        D[Image Processing\ncompression, format\nconversion, metadata]
        E[(MinIO\nProcessed Image\nS3 URL + ETag)]
    end

    subgraph "Grading Service — Cache Layer"
        F[Hash Computation\nSHA-256 + pHash]
        G{Cache\nHit?}
        H[(Redis\nHash-keyed\ncached results)]
    end

    subgraph "Grading Service — AI Pipeline"
        I[Complexity\nEstimation]
        J[Cascade Router\nsubject + complexity\n+ user tier]
        K[Prompt Assembly\ntemplate + A/B variant]
        L[LLM Invocation\nStreaming REST + SSE]
        M[Response Parser\nReal-time structured\nextraction per question]
        N{Confidence\n≥ threshold?}
        O[PaddleOCR\nFallback text\nextraction]
        P[Re-grade with\nOCR-enhanced text]
    end

    subgraph "Output"
        Q[(PostgreSQL\ngrading_session\ngrading_result\nper-question records)]
        R[(Redis\nCache new result\nSHA-256 + pHash keys\nTTL: 24h)]
        S[/SSE Stream\nto Client\nper-question results/]
    end

    subgraph "Downstream Events"
        T[RabbitMQ\nGradingCompleted]
        U[Error Notebook\nauto-collect errors]
        V[Analytics\naggregate stats]
        W[Notification\nalert student]
    end

    A --> B
    B --> C
    C -->|PASS| D
    C -->|REJECT| X[/"❌ Rejected\n422 Response"/]
    D --> E
    E --> F
    F --> G
    G -->|HIT| H
    H --> S
    G -->|MISS| I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> N
    N -->|YES| Q
    N -->|NO| O
    O --> P
    P --> Q
    Q --> R
    Q --> S
    Q --> T
    T --> U
    T --> V
    T --> W
```

## Data Transformations

| Stage | Input Data | Output Data | Transformation |
|:---|:---|:---|:---|
| Image Upload | Raw photo (JPEG/PNG, ≤10MB) | Processed image (WebP, optimized) | Format conversion, compression, EXIF strip |
| Content Moderation | Image binary | PASS/REJECT verdict | Cloud API classification |
| Hash Computation | Image binary | SHA-256 hash + pHash | Cryptographic hash + perceptual hash |
| Complexity Estimation | Image metadata + question count | Complexity tier (simple/medium/complex) | Heuristic analysis |
| Cascade Routing | Subject + complexity + user tier | Target LLM provider + model ID | Rule-based routing table |
| Prompt Assembly | Template + image URL + context | Complete prompt string | Template interpolation + A/B variant |
| LLM Invocation | Prompt + image | Raw streaming tokens | Multimodal LLM inference |
| Response Parsing | Raw token stream | Structured per-question result | Real-time extraction: {judgment, answer, explanation, knowledgePoints[]} |
| Confidence Scoring | Parsed result | Confidence score (0.0-1.0) | Model output analysis |
| OCR Fallback | Image region | Extracted text | PaddleOCR inference |
| Persistence | Structured results | DB records | JPA entity mapping |
| Caching | Structured results | Redis hash entries | Serialization + TTL |

## Notes
- Data flows left-to-right from input to output
- Content moderation is a hard gate — rejected images never reach the AI pipeline
- Cache layer intercepts before LLM invocation — cache hits bypass the entire AI pipeline
- OCR fallback path only triggered for low-confidence handwriting (< configurable threshold)
- Per-question granularity maintained throughout: each question in an image gets its own result record
- GradingCompleted event carries the full result set for downstream consumers
