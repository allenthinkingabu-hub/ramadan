# Business Requirements Document (BRD)

## Document Control

| Field | Value |
|-------|-------|
| Document Title | JIRA-like Multi-Platform User Login Module — Business Requirements Document |
| Version | 1.0 |
| Date | 2026-02-24 |
| Author | BRD Writer AI Agent |
| Status | Draft |
| Reviewer(s) | Project Sponsor, Project Manager |

### Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1 | 2026-02-23 | BRD Writer AI Agent | Initial draft |
| 1.0 | 2026-02-24 | BRD Writer AI Agent | Complete BRD after requirements elicitation and DoD verification |

---

## 1. Executive Summary

This BRD defines the requirements for a multi-platform, internationalized user login and authentication module for a JIRA-like project management system. The module provides secure authentication across five client platforms (PC Web, Flutter Mobile App, Responsive H5 Mobile Web, Tablet, WeChat Mini Program) with support for seven login methods, multi-factor authentication, and unlimited concurrent device sessions. The system follows a frontend-backend separation architecture with a Java Spring Boot backend serving all clients via a unified REST API using JWT-based authentication with OAuth 2.0/OIDC. Internationalization supports 13+ languages across three rollout tiers with RTL support from day one. The module complies with GDPR, China PIPL, and targets SOC2 Type II and ISO 27001 certification. Target performance is < 500ms login API response, 100K concurrent users, and 99.99% availability.

---

## 2. Business Objectives

| ID | Objective | Success Metric | Target | Timeline |
|----|-----------|---------------|--------|----------|
| BO-01 | Deliver secure, seamless authentication across all five client platforms | Number of platforms with fully functional login | 5 platforms (PC Web, Flutter App, H5, Tablet, WeChat Mini Program) | Launch |
| BO-02 | Support global user base with internationalized login experience | Number of languages supported | 3 languages (Tier 1) at launch, 8 at 6 months, 13 at 12 months | 12 months |
| BO-03 | Achieve enterprise-grade security and compliance | Compliance certifications obtained | GDPR compliance at launch; SOC2 Type II and ISO 27001 within 12 months | 12 months |
| BO-04 | Provide high-performance, high-availability authentication service | API response time and uptime | < 500ms login response, 99.99% availability | Launch |
| BO-05 | Enable multi-device concurrent access with user-controlled session management | Session management feature completeness | Users can view and revoke sessions across all devices | Launch |

---

## 3. Project Background & Context

### 3.1 Business Problem / Opportunity

The organization is building a JIRA-like project management platform targeting international teams. Modern project management tools require seamless access across multiple devices and geographies. Users expect to switch between their PC, phone, tablet, and WeChat without friction. Current competitors (JIRA, Asana, Monday.com, Linear) all support multi-platform access with varying levels of authentication sophistication. To compete effectively, the platform requires a robust, multi-platform, internationalized authentication module as its foundational access control layer.

Key market drivers:
- International teams require multi-language support with consistent UX across locales
- Chinese market penetration requires WeChat Mini Program integration
- Enterprise customers demand SSO (SAML/OIDC) and compliance certifications
- Modern security standards (passkeys, FIDO2) are becoming table-stakes

### 3.2 Current State (As-Is)

No authentication system exists. This is a greenfield project. The login module is the first module to be developed as a foundation for the larger project management platform.

### 3.3 Future State (To-Be)

A unified authentication service that:
- Serves all five client platforms through a single backend API
- Supports seven login methods including passwordless and enterprise SSO
- Provides multi-factor authentication (TOTP, SMS, email)
- Manages unlimited concurrent sessions per user with full device visibility
- Delivers a localized experience in 13+ languages with RTL support
- Meets GDPR, China PIPL, SOC2, and ISO 27001 requirements
- Scales to 100K concurrent users at 99.99% availability

---

## 4. Project Scope

### 4.1 In Scope

- User registration (email, phone, WeChat auto-registration)
- User login via email+password, phone+SMS, WeChat OAuth (Mini Program, Web QR, Mobile SDK), Google OAuth, Apple ID OAuth, enterprise SSO (SAML 2.0/OIDC), magic link, passkeys/WebAuthn
- Multi-factor authentication (TOTP authenticator app, SMS, email)
- Password recovery (email reset link, SMS reset code)
- Password policy enforcement (NIST 800-63B)
- JWT-based token lifecycle (access token, refresh token, remember me)
- Multi-device session management (view, revoke individual/all sessions)
- Internationalization for all login-related UI and notifications (Tier 1/2/3 rollout)
- RTL layout support
- Locale-aware formatting (phone numbers, dates, timezones)
- Localized email and SMS notification templates
- Account security features (new device notification, account lockout, CAPTCHA, login audit log)
- Brute-force protection (rate limiting, progressive delays)
- Security compliance (GDPR, China PIPL)
- Real-time monitoring dashboard, abnormal pattern alerting, SIEM integration
- Client platforms: PC Web SPA, Flutter mobile app (iOS + Android), responsive H5 mobile web, tablet (responsive), WeChat Mini Program (standalone)

### 4.2 Out of Scope

- Organization/workspace management
- Role-based access control (RBAC) — handled by a separate module
- Project management features (boards, issues, sprints, etc.)
- User profile management beyond authentication-related fields
- Payment and billing
- Third-party API access token management (developer API keys)
- SCIM provisioning (deferred to future phase)

---

## 5. Stakeholders

| ID | Name / Role | Department | Interest Level | Influence Level | RACI |
|----|------------|------------|---------------|-----------------|------|
| SH-01 | Project Sponsor | Executive | High | High | A |
| SH-02 | Project Manager | PMO | High | High | A |
| SH-03 | Business Analyst (BRD Writer Agent) | Product | High | Medium | R |
| SH-04 | Solution Architect / Tech Lead | Engineering | High | High | C |
| SH-05 | Frontend Lead (Web + H5) | Engineering | High | Medium | C |
| SH-06 | Flutter Mobile Lead | Engineering | High | Medium | C |
| SH-07 | WeChat Mini Program Lead | Engineering | High | Medium | C |
| SH-08 | Backend Lead (Spring Boot) | Engineering | High | Medium | R |
| SH-09 | QA Lead | Quality Assurance | Medium | Medium | C |
| SH-10 | Security Engineer | InfoSec | High | High | C |
| SH-11 | Legal / Compliance Officer | Legal | Medium | High | C |
| SH-12 | UX/UI Designer | Design | Medium | Medium | C |
| SH-13 | DevOps / SRE Lead | Infrastructure | Medium | Medium | C |
| SH-14 | End Users (International Teams) | External | High | Low | I |

---

## 6. Business Requirements

| ID | Requirement | Priority | Source | Acceptance Criteria |
|----|-------------|----------|--------|-------------------|
| BR-01 | The system shall provide secure user authentication across PC Web, Flutter mobile app, H5 mobile web, tablet, and WeChat Mini Program | Must | BO-01, Stakeholder | Users can successfully log in and access the system from all 5 platform types |
| BR-02 | The system shall support multiple authentication methods to accommodate diverse user preferences and enterprise requirements | Must | BO-01, Industry Research | All 7 login methods (email+password, phone+SMS, WeChat OAuth, Google, Apple ID, SSO, magic link, passkeys) are functional |
| BR-03 | The system shall provide multi-factor authentication to enhance account security | Must | BO-03, OWASP | Users can enable and use TOTP, SMS, or email as a second factor |
| BR-04 | The system shall support internationalized login experience for a global user base | Must | BO-02, Stakeholder | Login UI, error messages, and notifications render correctly in all Tier 1 languages at launch |
| BR-05 | The system shall allow users to manage active sessions across multiple devices | Must | BO-05, Industry Research (Linear) | Users can view all active sessions with device/location info and revoke any session |
| BR-06 | The system shall comply with GDPR, China PIPL, and target SOC2/ISO 27001 | Must | BO-03, Legal | Data handling follows GDPR/PIPL requirements; audit readiness for SOC2/ISO 27001 |
| BR-07 | The system shall deliver high-performance authentication under load | Must | BO-04, Stakeholder | Login API responds in < 500ms at p95 with 100K concurrent users |
| BR-08 | The system shall protect user accounts from unauthorized access through layered security measures | Must | BO-03, OWASP/NIST | Brute-force protection, account lockout, CAPTCHA, and login audit logging are operational |
| BR-09 | The system shall support user self-service account recovery | Must | Stakeholder | Users can reset passwords via email link or SMS code within 2 minutes |
| BR-10 | The system shall provide operational visibility into authentication activity | Should | BO-04, Stakeholder | Real-time monitoring dashboard, alerting, and SIEM integration are functional |

---

## 7. Functional Requirements

### 7.1 Registration

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-01 | The system shall allow users to register with a valid email address and password | Must | BR-01, BR-02 | User receives verification email, clicks link, account is activated |
| FR-02 | The system shall allow users to register with a valid phone number and SMS verification code | Must | BR-01, BR-02 | User enters phone number, receives SMS code, enters code, account is created |
| FR-03 | The system shall auto-register users on first WeChat login using their WeChat profile (openid) | Must | BR-01, BR-02 | First-time WeChat users are automatically created an account linked to their WeChat openid |

### 7.2 Login Methods

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-04 | The system shall authenticate users via email and password | Must | BR-02 | User enters valid email+password and receives a valid JWT access token |
| FR-05 | The system shall authenticate users via phone number and SMS verification code | Must | BR-02 | User enters phone, receives SMS within 30 seconds, enters code, and is authenticated |
| FR-06 | The system shall authenticate users via WeChat Mini Program login (wx.login → code2Session) | Must | BR-02 | User taps login in Mini Program, system exchanges code for session, issues JWT |
| FR-07 | The system shall authenticate users via WeChat Web QR code OAuth | Must | BR-02 | User scans QR code with WeChat mobile app, system receives callback, issues JWT |
| FR-08 | The system shall authenticate users via WeChat Mobile SDK OAuth | Must | BR-02 | User taps WeChat login in Flutter app, WeChat SDK opens, user confirms, system issues JWT |
| FR-09 | The system shall authenticate users via Google OAuth 2.0 | Must | BR-02 | User clicks Google login, completes Google consent flow, system issues JWT |
| FR-10 | The system shall authenticate users via Apple ID (Sign in with Apple) | Must | BR-02 | User clicks Apple login, completes Apple consent flow, system issues JWT |
| FR-11 | The system shall authenticate users via enterprise SSO (SAML 2.0 and OIDC) | Must | BR-02 | Admin configures SSO IdP, users are redirected to IdP, authenticated, and returned with JWT |
| FR-12 | The system shall authenticate users via magic link (passwordless email) | Must | BR-02 | User enters email, receives login link, clicks link, and is authenticated within 15 minutes |
| FR-13 | The system shall authenticate users via passkeys/WebAuthn | Must | BR-02 | User registers a passkey, uses biometric/PIN on subsequent logins, system verifies and issues JWT |

### 7.3 Multi-Factor Authentication

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-14 | The system shall support TOTP-based 2FA using authenticator apps (Google Authenticator, Authy, etc.) | Must | BR-03 | User scans QR code to set up TOTP, enters 6-digit code on login to complete 2FA |
| FR-15 | The system shall support SMS-based 2FA | Must | BR-03 | User receives SMS with 6-digit code on login, enters code to complete 2FA |
| FR-16 | The system shall support email-based 2FA | Must | BR-03 | User receives email with 6-digit code on login, enters code to complete 2FA |
| FR-17 | The system shall allow users to enable, disable, and switch 2FA methods in account settings | Must | BR-03 | User can manage 2FA methods without contacting support |

### 7.4 Password Management

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-18 | The system shall enforce NIST 800-63B password policy (minimum 8 characters, no forced rotation, breached password screening) | Must | BR-08 | Passwords shorter than 8 chars are rejected; passwords found in breach databases are rejected; no periodic rotation is enforced |
| FR-19 | The system shall allow users to reset their password via email reset link | Must | BR-09 | User requests reset, receives email with one-time link (valid 30 minutes), sets new password |
| FR-20 | The system shall allow users to reset their password via SMS verification code | Must | BR-09 | User requests reset, receives SMS code, verifies identity, sets new password |

### 7.5 Token Lifecycle

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-21 | The system shall issue JWT access tokens with a 15-minute expiry | Must | BR-07 | Access tokens expire after 15 minutes; expired tokens are rejected with 401 |
| FR-22 | The system shall issue refresh tokens with a 7-day expiry and enforce rotation on each use | Must | BR-08 | Each refresh call returns a new refresh token; reuse of a previously rotated token invalidates the entire token family |
| FR-23 | The system shall support a "remember me" function extending refresh token lifetime to 30 days | Must | BR-05 | Users who check "remember me" remain authenticated for 30 days without re-login |
| FR-24 | The system shall use OAuth 2.0 Authorization Code flow with PKCE for all public clients | Must | BR-08 | All SPA, mobile, and Mini Program clients use PKCE; code interception attacks are prevented |

### 7.6 Session Management

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-25 | The system shall allow unlimited concurrent sessions per user across different devices | Must | BR-05 | A user can be logged in on PC, phone, tablet, and WeChat simultaneously |
| FR-26 | The system shall display all active sessions to the user with device type, IP address, location, and last active timestamp | Must | BR-05 | User views session list showing all active sessions with metadata |
| FR-27 | The system shall allow users to revoke individual sessions or all sessions at once | Must | BR-05 | Revoking a session immediately invalidates its tokens; "revoke all" invalidates all sessions except the current one |

### 7.7 Account Security

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-28 | The system shall send a notification (email or push) when a login occurs from a new/unrecognized device | Must | BR-08 | User receives notification within 1 minute of a new-device login with device and location info |
| FR-29 | The system shall temporarily lock an account after 5 consecutive failed login attempts for 15 minutes | Must | BR-08 | After 5 failures, further attempts are rejected with lockout message; account unlocks after 15 minutes |
| FR-30 | The system shall display CAPTCHA after 3 consecutive failed login attempts | Must | BR-08 | CAPTCHA appears on the 4th attempt; login proceeds only after CAPTCHA is solved |
| FR-31 | The system shall maintain a login audit log recording IP address, device fingerprint, geographic location, timestamp, and outcome for every authentication attempt | Must | BR-08, BR-10 | Audit log entries are queryable; retained for minimum 90 days |
| FR-32 | The system shall implement rate limiting on authentication endpoints (5 attempts per 15-minute window per account+IP combination) | Must | BR-08 | Requests exceeding the limit receive HTTP 429 with Retry-After header |

### 7.8 Internationalization

| ID | Requirement | Priority | Related BR | Acceptance Criteria |
|----|-------------|----------|-----------|-------------------|
| FR-33 | The system shall support Tier 1 languages (English, Simplified Chinese, Japanese) at launch | Must | BR-04 | All login UI, error messages, and email/SMS templates render correctly in all 3 languages |
| FR-34 | The system shall support Tier 2 languages (Korean, Traditional Chinese, French, German, Spanish) within 6 months | Should | BR-04 | All login flows fully localized in Tier 2 languages |
| FR-35 | The system shall support Tier 3 languages (Portuguese, Russian, Arabic, Turkish, Indonesian) within 12 months | Could | BR-04 | All login flows fully localized in Tier 3 languages |
| FR-36 | The system shall support right-to-left (RTL) layout for Arabic, Hebrew, and Persian from launch | Must | BR-04 | Login pages render correctly in RTL mode with mirrored layout, RTL text alignment, and bidirectional text handling |
| FR-37 | The system shall detect user locale from browser/OS settings and allow manual override | Must | BR-04 | Default language matches browser/OS locale; user can switch language from login page |
| FR-38 | The system shall format phone numbers, dates, and timezones according to the user's locale | Must | BR-04 | Phone numbers display in national format; dates follow locale conventions (MM/DD vs DD/MM vs YYYY-MM-DD) |
| FR-39 | The system shall send all transactional emails and SMS in the recipient's configured locale | Must | BR-04 | Verification codes, reset links, and security alerts are sent in the user's language |

---

## 8. Non-Functional Requirements

| ID | Category | Requirement | Priority | Acceptance Criteria |
|----|----------|-------------|----------|-------------------|
| NFR-01 | Performance | Login API response time shall be less than 500ms at p95 under normal load | Must | Load test confirms p95 < 500ms with 10K concurrent requests |
| NFR-02 | Scalability | The system shall support 100,000 concurrent online users | Must | Load test confirms stable operation at 100K concurrent sessions |
| NFR-03 | Availability | The system shall maintain 99.99% uptime (< 52.6 minutes downtime per year) | Must | Monitoring confirms 99.99% availability over rolling 30-day window |
| NFR-04 | Security | All authentication data in transit shall be encrypted via TLS 1.2+ | Must | Security scan confirms no plaintext authentication traffic |
| NFR-05 | Security | Passwords shall be stored using bcrypt or Argon2 with per-user salt | Must | Database inspection confirms no plaintext or reversibly encrypted passwords |
| NFR-06 | Security | JWT tokens shall not contain sensitive PII in claims | Must | Token inspection confirms only sub, exp, iat, iss, aud, and non-sensitive custom claims |
| NFR-07 | Security | The system shall prevent account enumeration by returning identical responses for valid and invalid usernames | Must | Penetration test confirms no enumeration vector via login, registration, or password reset |
| NFR-08 | Compliance | The system shall comply with GDPR requirements (data minimization, right to access, right to erasure, 72-hour breach notification) | Must | GDPR compliance audit passes |
| NFR-09 | Compliance | The system shall comply with China Personal Information Protection Law (PIPL) requirements | Must | PIPL compliance assessment passes |
| NFR-10 | Compliance | The system architecture shall be SOC2 Type II and ISO 27001 audit-ready | Should | Pre-audit assessment identifies no critical gaps |
| NFR-11 | Usability | Login flow shall complete in 3 steps or fewer for all authentication methods | Must | UX test confirms no login method requires more than 3 user interactions |
| NFR-12 | Usability | RTL layout shall render correctly for all login pages without visual artifacts | Must | QA verifies all login screens in Arabic/Hebrew with no layout issues |
| NFR-13 | Observability | The system shall provide a real-time login failure monitoring dashboard | Should | Dashboard displays live login failure rates, geographic distribution, and error types |
| NFR-14 | Observability | The system shall alert on abnormal login patterns (credential stuffing, brute force, geographic anomaly) | Should | Alert fires within 5 minutes of pattern detection threshold being exceeded |
| NFR-15 | Observability | The system shall support SIEM integration via webhook or API for authentication event streaming | Should | Authentication events are streamable to external SIEM in near-real-time |
| NFR-16 | Reliability | Token refresh shall handle network retry scenarios with a 30-second grace period for rotated refresh tokens | Must | Intermittent network failures do not cause unexpected session termination |

---

## 9. Data Requirements

### 9.1 Data Entities

**User Account**
| Attribute | Type | Constraints |
|-----------|------|------------|
| user_id | UUID | Primary key |
| email | VARCHAR(255) | Unique, nullable |
| phone | VARCHAR(20) | Unique, nullable, E.164 format |
| password_hash | VARCHAR(255) | Nullable (for passwordless users) |
| wechat_unionid | VARCHAR(64) | Unique, nullable |
| preferred_locale | VARCHAR(10) | Default: 'en' |
| mfa_enabled | BOOLEAN | Default: false |
| mfa_method | ENUM | TOTP / SMS / EMAIL, nullable |
| totp_secret | VARCHAR(255) | Encrypted, nullable |
| status | ENUM | ACTIVE / LOCKED / DISABLED |
| created_at | TIMESTAMP | UTC |
| updated_at | TIMESTAMP | UTC |

**WeChat Identity**
| Attribute | Type | Constraints |
|-----------|------|------------|
| id | UUID | Primary key |
| user_id | UUID | Foreign key → User Account |
| openid | VARCHAR(64) | Unique per app |
| unionid | VARCHAR(64) | Links to user_account.wechat_unionid |
| app_type | ENUM | MINI_PROGRAM / WEB / MOBILE |
| app_id | VARCHAR(64) | WeChat application ID |

**OAuth Identity**
| Attribute | Type | Constraints |
|-----------|------|------------|
| id | UUID | Primary key |
| user_id | UUID | Foreign key → User Account |
| provider | ENUM | GOOGLE / APPLE / SAML / OIDC |
| provider_user_id | VARCHAR(255) | Unique per provider |
| provider_email | VARCHAR(255) | Nullable |

**User Session**
| Attribute | Type | Constraints |
|-----------|------|------------|
| session_id | UUID | Primary key |
| user_id | UUID | Foreign key → User Account |
| refresh_token_hash | VARCHAR(255) | Hashed refresh token |
| device_type | ENUM | PC_WEB / MOBILE_APP / H5 / TABLET / WECHAT_MINI |
| device_fingerprint | VARCHAR(255) | Browser/device fingerprint |
| ip_address | VARCHAR(45) | IPv4 or IPv6 |
| geo_location | VARCHAR(100) | City, Country |
| user_agent | VARCHAR(500) | Client user-agent string |
| last_active_at | TIMESTAMP | UTC |
| expires_at | TIMESTAMP | UTC |
| created_at | TIMESTAMP | UTC |

**Login Audit Log**
| Attribute | Type | Constraints |
|-----------|------|------------|
| log_id | UUID | Primary key |
| user_id | UUID | Foreign key → User Account, nullable (for failed attempts with unknown user) |
| event_type | ENUM | LOGIN_SUCCESS / LOGIN_FAILURE / LOGOUT / TOKEN_REFRESH / MFA_CHALLENGE / PASSWORD_RESET / ACCOUNT_LOCKED |
| auth_method | ENUM | EMAIL_PASSWORD / PHONE_SMS / WECHAT / GOOGLE / APPLE / SSO / MAGIC_LINK / PASSKEY |
| ip_address | VARCHAR(45) | IPv4 or IPv6 |
| device_fingerprint | VARCHAR(255) | Nullable |
| geo_location | VARCHAR(100) | Nullable |
| failure_reason | VARCHAR(255) | Nullable (only for failures) |
| timestamp | TIMESTAMP | UTC |

**Passkey Credential**
| Attribute | Type | Constraints |
|-----------|------|------------|
| credential_id | BYTEA | Primary key (WebAuthn credential ID) |
| user_id | UUID | Foreign key → User Account |
| public_key | BYTEA | WebAuthn public key |
| sign_count | BIGINT | Counter for clone detection |
| device_name | VARCHAR(100) | User-assigned name |
| created_at | TIMESTAMP | UTC |

### 9.2 Data Flows

```
User Device (Any Platform)
    │
    ▼
API Gateway (Rate Limiting, CAPTCHA, TLS Termination)
    │
    ▼
Auth Service (Spring Boot)
    ├── Login Handler → Validate Credentials → Issue JWT
    ├── Token Handler → Validate/Refresh JWT
    ├── MFA Handler → Verify TOTP/SMS/Email Code
    ├── OAuth Handler → Google/Apple/WeChat OAuth Flows
    ├── SSO Handler → SAML/OIDC Flows
    ├── Session Manager → CRUD Sessions in Redis
    └── Audit Logger → Write to PostgreSQL + Stream to SIEM
    │
    ├── PostgreSQL (User Accounts, OAuth Identities, Audit Logs, Passkeys)
    ├── Redis (Active Sessions, Rate Limit Counters, Token Blocklist)
    └── RocketMQ (Async: SMS, Email Notifications, SIEM Event Streaming)
```

### 9.3 Data Migration (if applicable)

Not applicable — greenfield project. No data migration required.

---

## 10. Assumptions

| ID | Assumption | Impact if Invalid |
|----|-----------|-------------------|
| AS-01 | WeChat Open Platform account and Mini Program are already registered and approved | WeChat login integration will be blocked until registration is complete |
| AS-02 | Google Cloud Console and Apple Developer accounts are available for OAuth configuration | Google and Apple login methods will be unavailable |
| AS-03 | SMS gateway provider supports all target countries for SMS delivery | SMS verification and 2FA will be unavailable in unsupported regions |
| AS-04 | The organization has or will obtain the necessary domain and TLS certificates | HTTPS endpoints will not be available, blocking all authentication flows |
| AS-05 | Cloud infrastructure (compute, database, Redis, RocketMQ) is available and provisioned | System deployment will be delayed |
| AS-06 | Enterprise SSO customers will provide IdP metadata (SAML) or discovery URLs (OIDC) | SSO configuration will require manual coordination with each customer |
| AS-07 | Translation services or translation management platform (Crowdin/Lokalise) is available for i18n | Tier 2 and Tier 3 language rollouts will be delayed |
| AS-08 | The RBAC module (out of scope) will integrate with this auth module via user_id | Authorization decisions will not be possible until RBAC module is built |

---

## 11. Constraints

| ID | Type | Constraint | Impact |
|----|------|-----------|--------|
| CN-01 | Technology | Backend must use Java Spring Boot, PostgreSQL, Redis, RocketMQ | Technology stack is fixed; library/framework choices must be compatible |
| CN-02 | Technology | Mobile app must use Flutter for cross-platform development | Platform-specific native features (e.g., Keychain) must be accessed via Flutter plugins |
| CN-03 | Technology | WeChat Mini Program must follow WeChat's development guidelines and API restrictions | Login flow is constrained by wx.login / code2Session API design |
| CN-04 | Regulatory | Must comply with GDPR (EU) and PIPL (China) simultaneously | Data storage and processing may need geographic separation (EU vs China) |
| CN-05 | Regulatory | WeChat login requires ICP filing for China-based services | Web-based WeChat OAuth may be restricted without proper ICP filing |
| CN-06 | Performance | Login API must respond within 500ms at p95 | External OAuth provider latency may impact response time; caching and async patterns required |
| CN-07 | Security | Passwords must follow NIST 800-63B-4 standards | Breached password screening requires integration with external breach database (e.g., HaveIBeenPwned) |
| CN-08 | Availability | System must maintain 99.99% uptime | Requires redundant deployment, health checks, and automated failover |

---

## 12. Dependencies

| ID | Dependency | Type | Owner | Status |
|----|-----------|------|-------|--------|
| DP-01 | WeChat Open Platform account registration and Mini Program approval | External | Product Manager | Open |
| DP-02 | Google Cloud Console OAuth 2.0 client configuration | External | DevOps | Open |
| DP-03 | Apple Developer account with Sign in with Apple capability | External | DevOps | Open |
| DP-04 | SMS gateway provider contract (international coverage) | External | Operations | Open |
| DP-05 | Email delivery service (SendGrid/SES/Mailgun) | External | DevOps | Open |
| DP-06 | Cloud infrastructure provisioning (compute, PostgreSQL, Redis, RocketMQ) | Internal | DevOps/SRE | Open |
| DP-07 | TLS certificates and domain configuration | Internal | DevOps | Open |
| DP-08 | Translation management platform setup (Crowdin/Lokalise) | Internal | Product Manager | Open |
| DP-09 | RBAC module (consumes user_id from this module) | Internal | Backend Team | Open |
| DP-10 | SIEM platform for security event ingestion | Internal | InfoSec | Open |
| DP-11 | Breached password database integration (HaveIBeenPwned API or local copy) | External | Security Engineer | Open |

---

## 13. Risks & Mitigation

| ID | Risk | Probability | Impact | Mitigation Strategy | Owner |
|----|------|------------|--------|---------------------|-------|
| RK-01 | WeChat Mini Program approval delayed by WeChat review process | Medium | High | Submit for review early; prepare alternative H5-based WeChat entry point | Product Manager |
| RK-02 | SMS delivery failures in certain countries/regions | Medium | Medium | Use multiple SMS gateway providers with failover; support email as alternative verification | Backend Lead |
| RK-03 | OAuth provider API changes break integration | Low | High | Abstract OAuth integrations behind adapter pattern; monitor provider changelogs; maintain integration tests | Solution Architect |
| RK-04 | GDPR and PIPL compliance conflict (data localization requirements) | Medium | High | Design data architecture with geographic separation capability from the start; consult legal early | Legal/Compliance |
| RK-05 | Performance degradation under 100K concurrent users | Medium | High | Conduct early load testing; implement horizontal scaling; use Redis for session management to reduce DB load | DevOps/SRE |
| RK-06 | RTL layout issues across all 5 platforms | Medium | Medium | Use CSS logical properties from the start; establish RTL testing as part of CI/CD pipeline | Frontend Lead |
| RK-07 | Passkey/WebAuthn browser compatibility issues on older browsers | Low | Low | Graceful degradation to password-based login; display browser upgrade notification | Frontend Lead |
| RK-08 | Credential stuffing attacks at launch | High | High | Deploy layered brute-force protection before launch; conduct penetration testing; enable WAF rules | Security Engineer |
| RK-09 | Translation quality issues for non-Tier 1 languages | Medium | Medium | Use professional translation services; implement in-context review process; support community corrections | Product Manager |
| RK-10 | Refresh token rotation causing unexpected logouts on flaky mobile networks | Medium | Medium | Implement 30-second grace period for rotated refresh tokens; implement retry logic in Flutter client | Flutter Mobile Lead |

---

## 14. Success Metrics & KPIs

| ID | KPI | Baseline | Target | Measurement Method | Frequency |
|----|-----|---------|--------|-------------------|-----------|
| KPI-01 | Login API p95 response time | N/A (new system) | < 500ms | APM monitoring (e.g., Prometheus + Grafana) | Real-time |
| KPI-02 | System availability | N/A | 99.99% | Uptime monitoring (e.g., PagerDuty, UptimeRobot) | Monthly |
| KPI-03 | Login success rate | N/A | > 98% | Login success / total login attempts ratio | Daily |
| KPI-04 | MFA adoption rate | 0% | > 30% within 6 months | Users with MFA enabled / total active users | Monthly |
| KPI-05 | Average time to complete login flow | N/A | < 10 seconds (including MFA) | Client-side performance tracking | Weekly |
| KPI-06 | Password reset completion rate | N/A | > 90% | Successful resets / reset requests | Monthly |
| KPI-07 | Concurrent online users supported | 0 | 100,000 | Load test results | Quarterly |
| KPI-08 | Security incidents (unauthorized access) | 0 | 0 | Security audit log analysis | Monthly |
| KPI-09 | i18n language coverage | 0 | 3 at launch, 8 at 6 months, 13 at 12 months | Supported locale count | Quarterly |
| KPI-10 | Brute-force attack block rate | N/A | > 99.5% | Blocked malicious attempts / total malicious attempts | Weekly |

---

## 15. Cost-Benefit Analysis

### 15.1 Estimated Costs

| Category | Item | Estimated Cost |
|----------|------|---------------|
| Development | Backend auth service (Spring Boot, 3 engineers x 3 months) | Engineering hours |
| Development | Web SPA login module (1 engineer x 2 months) | Engineering hours |
| Development | Flutter mobile login module (1 engineer x 2 months) | Engineering hours |
| Development | WeChat Mini Program login module (1 engineer x 1.5 months) | Engineering hours |
| Development | i18n framework + Tier 1 translations | Engineering hours + translation costs |
| Infrastructure | PostgreSQL (managed), Redis (managed), RocketMQ | Monthly cloud costs |
| Third-party | SMS gateway (per-message pricing, international rates) | Variable per volume |
| Third-party | Email delivery service (SendGrid/SES) | Variable per volume |
| Third-party | Translation management platform (Crowdin/Lokalise) | Monthly subscription |
| Compliance | SOC2 Type II audit | One-time + annual renewal |
| Compliance | ISO 27001 certification | One-time + annual renewal |
| Security | Penetration testing (annual) | Per engagement |

### 15.2 Expected Benefits

- **Foundation for platform**: Authentication module is a prerequisite for all other platform features; enables parallel development of other modules
- **Global market access**: i18n support opens the platform to international markets from day one
- **Enterprise readiness**: SSO and compliance certifications enable enterprise sales pipeline
- **User trust**: Strong security posture (MFA, audit logging, compliance) builds user confidence
- **Reduced support costs**: Self-service password recovery and session management reduce support ticket volume
- **WeChat market penetration**: Mini Program login provides direct access to 1.3B+ WeChat users

### 15.3 ROI Projection

As a foundational module, ROI is measured indirectly through platform adoption and enterprise deal closure rate. The authentication module is a hard prerequisite — without it, no other platform feature can be shipped. Direct ROI attribution will be tracked through enterprise deal conversion rates (SSO-enabled vs non-SSO prospects) and user activation rates across platforms.

---

## 16. Implementation Timeline

| Milestone | Target Date | Dependencies | Owner |
|-----------|------------|-------------|-------|
| M1: Architecture design & tech spike | Week 1-2 | DP-06 (infra) | Solution Architect |
| M2: Core auth service (email+password, JWT, session management) | Week 3-6 | M1 | Backend Lead |
| M3: Phone+SMS login + MFA (TOTP, SMS, email) | Week 5-8 | M2, DP-04 (SMS gateway) | Backend Lead |
| M4: OAuth integrations (Google, Apple) | Week 7-9 | M2, DP-02, DP-03 | Backend Lead |
| M5: WeChat OAuth (Mini Program, Web, Mobile SDK) | Week 7-10 | M2, DP-01 | WeChat Lead |
| M6: Enterprise SSO (SAML 2.0 + OIDC) | Week 9-12 | M2 | Backend Lead |
| M7: Passkeys/WebAuthn + Magic Link | Week 10-12 | M2 | Backend Lead |
| M8: Web SPA login UI (all methods + i18n Tier 1 + RTL) | Week 3-10 | M2 (API contracts) | Frontend Lead |
| M9: Flutter mobile login (all methods + i18n Tier 1) | Week 5-12 | M2 (API contracts) | Flutter Lead |
| M10: H5 responsive login | Week 8-11 | M8 (shared components) | Frontend Lead |
| M11: WeChat Mini Program login UI | Week 7-11 | M5 | WeChat Lead |
| M12: Security hardening (rate limiting, CAPTCHA, brute-force, audit log) | Week 10-13 | M2 | Security Engineer |
| M13: Monitoring dashboard + alerting + SIEM integration | Week 11-14 | M12 | DevOps/SRE |
| M14: Load testing & performance optimization | Week 13-14 | All platform milestones | QA Lead + DevOps |
| M15: Penetration testing | Week 14-15 | M12 | Security Engineer |
| M16: GDPR + PIPL compliance review | Week 14-15 | All milestones | Legal/Compliance |
| M17: Launch (all platforms, Tier 1 i18n) | Week 16 | All milestones | Project Manager |
| M18: Tier 2 i18n rollout | Month 6 | M17, DP-08 | Product Manager |
| M19: Tier 3 i18n rollout | Month 12 | M18 | Product Manager |
| M20: SOC2 Type II + ISO 27001 audit | Month 12 | M17 | Legal/Compliance |

---

## 17. Glossary

| Term | Definition |
|------|-----------|
| JWT | JSON Web Token — a compact, URL-safe token format for securely transmitting claims between parties |
| OAuth 2.0 | An authorization framework that enables third-party applications to obtain limited access to a web service |
| OIDC | OpenID Connect — an identity layer on top of OAuth 2.0 for authentication |
| PKCE | Proof Key for Code Exchange — an extension to OAuth 2.0 that prevents authorization code interception attacks |
| SAML | Security Assertion Markup Language — an XML-based standard for exchanging authentication data between IdP and SP |
| SSO | Single Sign-On — allows users to authenticate once and access multiple systems |
| MFA / 2FA | Multi-Factor Authentication / Two-Factor Authentication — requires multiple verification methods |
| TOTP | Time-based One-Time Password — generates time-limited codes using a shared secret (RFC 6238) |
| WebAuthn | Web Authentication API — a W3C standard for passwordless authentication using public-key cryptography |
| FIDO2 | Fast IDentity Online 2 — an authentication standard encompassing WebAuthn and CTAP |
| NIST 800-63B | NIST Digital Identity Guidelines — Authentication and Lifecycle Management |
| GDPR | General Data Protection Regulation — EU data protection law |
| PIPL | Personal Information Protection Law — China's data protection law |
| SOC2 | Service Organization Control 2 — a security compliance framework |
| ISO 27001 | International standard for information security management systems |
| RTL | Right-to-Left — text direction for Arabic, Hebrew, Persian, and Urdu scripts |
| i18n | Internationalization — designing software to support multiple languages and locales |
| E.164 | ITU-T standard for international phone number formatting (e.g., +14155552671) |
| UnionID | WeChat mechanism providing a unified user identifier across all bound applications |
| openid | WeChat user identifier unique to each application |
| SPA | Single Page Application — a web application that loads a single HTML page and dynamically updates |
| H5 | Mobile web page built with HTML5, typically accessed via mobile browser |
| RocketMQ | Apache RocketMQ — a distributed messaging and streaming platform |

---

## 18. Appendices

### Appendix A: Process Flow Diagrams

**A.1 Standard Login Flow (Email + Password)**
```
User → Enter email + password
  → API Gateway (rate limit check, TLS)
    → Auth Service: Validate credentials
      → [If MFA enabled] → MFA Challenge (TOTP/SMS/Email)
        → User enters MFA code
        → Auth Service: Verify MFA
      → Issue JWT access token + refresh token
      → Create session record in Redis
      → Write audit log entry
    → Return tokens to client
User → Access protected resources with JWT
```

**A.2 WeChat Mini Program Login Flow**
```
User → Open Mini Program → wx.login() → Receive temp code
  → Mini Program sends code to backend
    → Auth Service calls WeChat code2Session API
      → Receive openid + session_key
      → Look up user by openid
        → [If new user] → Auto-register with openid
      → Issue JWT access token + refresh token
      → Create session record in Redis
      → Write audit log entry
    → Return custom token to Mini Program
```

**A.3 Token Refresh Flow**
```
Client → Access token expired (401 response)
  → Client sends refresh token to /auth/refresh
    → Auth Service: Validate refresh token
      → [If valid] → Issue new access token + new refresh token (rotation)
        → Invalidate old refresh token
        → Update session last_active_at
      → [If reused/invalid] → Invalidate entire token family
        → Force re-authentication
    → Return new tokens or 401
```

### Appendix B: Requirements Traceability Matrix

| Requirement ID | Source | Related Requirements | Test Case |
|---------------|--------|---------------------|-----------|
| BR-01 | BO-01, Stakeholder | FR-01 to FR-13 | TC-Platform-Login |
| BR-02 | BO-01, Industry | FR-04 to FR-13 | TC-Auth-Methods |
| BR-03 | BO-03, OWASP | FR-14 to FR-17 | TC-MFA |
| BR-04 | BO-02, Stakeholder | FR-33 to FR-39 | TC-i18n |
| BR-05 | BO-05, Industry | FR-25 to FR-27 | TC-Session-Mgmt |
| BR-06 | BO-03, Legal | NFR-08 to NFR-10 | TC-Compliance |
| BR-07 | BO-04, Stakeholder | NFR-01 to NFR-03, FR-21 | TC-Performance |
| BR-08 | BO-03, OWASP/NIST | FR-18, FR-28 to FR-32, NFR-04 to NFR-07 | TC-Security |
| BR-09 | Stakeholder | FR-19, FR-20 | TC-Password-Recovery |
| BR-10 | BO-04, Stakeholder | NFR-13 to NFR-15 | TC-Monitoring |

### Appendix C: Supporting Documents

| Document | Description | Location |
|----------|-------------|----------|
| OWASP Authentication Cheat Sheet | Security best practices for authentication | https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html |
| NIST SP 800-63B-4 | Digital Identity Guidelines — Authentication | https://pages.nist.gov/800-63-3/sp800-63b.html |
| WeChat Mini Program Login Documentation | Official login API documentation | https://developers.weixin.qq.com/miniprogram/en/dev/framework/open-ability/login.html |
| WeChat Open Platform OAuth Documentation | Official OAuth documentation for web/mobile | https://developers.weixin.qq.com/doc/oplatform/en/Website_App/WeChat_Login/Wechat_Login |
| OAuth 2.0 RFC 6749 | OAuth 2.0 Authorization Framework | https://tools.ietf.org/html/rfc6749 |
| OpenID Connect Core 1.0 | OIDC specification | https://openid.net/specs/openid-connect-core-1_0.html |
| WebAuthn Specification | W3C Web Authentication API | https://www.w3.org/TR/webauthn-2/ |
| GDPR Official Text | EU General Data Protection Regulation | https://gdpr-info.eu/ |
| China PIPL Official Text | Personal Information Protection Law | National People's Congress website |

---

## 19. Approval Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor | _________________ | _________ | ________ |
| Project Manager | _________________ | _________ | ________ |
| Solution Architect | _________________ | _________ | ________ |
| Security Engineer | _________________ | _________ | ________ |
| Legal / Compliance | _________________ | _________ | ________ |
| Business Analyst | BRD Writer AI Agent | _________ | 2026-02-24 |
