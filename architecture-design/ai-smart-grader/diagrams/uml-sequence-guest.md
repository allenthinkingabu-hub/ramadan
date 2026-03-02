# UML Sequence Diagram — Guest Onboarding Flow

## Description
Shows the flow for an unauthenticated guest user: device fingerprint tracking, limited AI grading trial, quota enforcement, and conversion prompt to registration.

## Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Guest
    participant Client as Flutter/Angular/Mini Program
    participant Gateway as API Gateway
    participant AuthSvc as Auth Service
    participant UserSvc as User Service
    participant Redis as Redis Cache
    participant ImageSvc as Image Service
    participant GradingSvc as Grading Service
    participant DB as PostgreSQL
    participant LLM as LLM Provider

    Guest->>Client: Open app / visit website
    Client->>Client: Generate device fingerprint (canvas, WebGL, UA, screen, timezone)
    Client->>Gateway: POST /api/v1/auth/guest-session {fingerprint, platform}
    Gateway->>AuthSvc: Create guest session

    AuthSvc->>Redis: Check fingerprint against existing guest sessions

    alt Returning guest (fingerprint recognized)
        Redis-->>AuthSvc: Existing guest profile {remainingQuota, history}
        AuthSvc-->>Gateway: 200 {guestToken (JWT), remainingQuota}
    else New guest
        AuthSvc->>UserSvc: Create guest profile
        UserSvc->>DB: INSERT guest_user (fingerprint, device_info, created_at)
        UserSvc-->>AuthSvc: Guest profile created
        AuthSvc->>Redis: Store guest session {quota: 3, ttl: 24h}
        AuthSvc-->>Gateway: 200 {guestToken (JWT, role: GUEST), quota: 3}
    end

    Gateway-->>Client: Guest session established
    Client-->>Guest: Show AI grading UI with "3 free tries" indicator

    Guest->>Client: Upload exercise photo
    Client->>Gateway: POST /api/v1/images/upload (multipart, guestToken)
    Gateway->>Gateway: Validate guest JWT, inject X-User-Role: GUEST

    Gateway->>ImageSvc: Forward upload (guest context)
    ImageSvc->>ImageSvc: Validate + process image
    ImageSvc-->>Gateway: 200 {imageId, imageUrl}
    Gateway-->>Client: Upload success

    Client->>Gateway: POST /api/v1/grading/submit {imageId, subject}
    Gateway->>GradingSvc: Forward grading request (guest context)

    GradingSvc->>Redis: Check guest quota (fingerprint key)

    alt Quota EXHAUSTED (0 remaining)
        GradingSvc-->>Gateway: 429 Quota exceeded
        Gateway-->>Client: Quota exhausted
        Client-->>Guest: Display "Free trial complete! Register to continue" CTA

        Note over Guest, Client: Conversion funnel
        Guest->>Client: Tap "Register" CTA
        Client->>Gateway: POST /api/v1/auth/register {phone/email/wechat}
        Gateway->>AuthSvc: Register with guest profile migration
        AuthSvc->>UserSvc: Convert guest to registered user (preserve history)
        UserSvc->>DB: UPDATE user SET role = 'STUDENT', link guest history
        AuthSvc-->>Gateway: 200 {authToken, profile}
        Gateway-->>Client: Registration complete
        Client-->>Guest: Welcome! Your grading history has been preserved.
    else Quota AVAILABLE
        GradingSvc->>Redis: Decrement quota (DECR fingerprint:quota)
        GradingSvc->>GradingSvc: Execute grading pipeline (same as registered user)
        GradingSvc->>LLM: Send image + prompt
        LLM-->>GradingSvc: Streaming grading result

        GradingSvc-->>Gateway: SSE grading stream
        Gateway-->>Client: Stream results
        Client-->>Guest: Display grading results + "X tries remaining"

        alt Last free try used
            Client-->>Guest: "Great results! Register to unlock unlimited grading + Error Notebook"
        end
    end
```

## Notes
- **Device fingerprint**: Composite fingerprint (canvas, WebGL, user agent, screen resolution, timezone) — not PII, used for quota tracking only
- **Guest quota**: 3 free grading attempts per device per 24-hour period (configurable via Nacos)
- **JWT for guests**: Guests receive a JWT with role `GUEST` — same API pipeline, different authorization rules
- **Feature restrictions**: Guests cannot access error notebook, analytics, class features, or payment
- **Seamless conversion**: Guest-to-registered-user migration preserves grading history — no data loss
- **Anti-abuse**: Device fingerprint + Redis TTL prevents trivial quota bypass; rate limiting at gateway level
- **Conversion tracking**: Guest registration events tracked for analytics (conversion rate, time-to-convert, feature that triggered conversion)
