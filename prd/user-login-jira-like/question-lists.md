# PRD Writer Agent - Question Lists

## Question List - Phase 3: M-AUTH (Core Authentication)
- Generated: 2026-02-25
- Status: Answered

1. Should password-based registration require email verification before any login is allowed, or can users access a limited set of features before verification?
   - Answer: Lenient - Allow limited access before verification; auto-approve after email verification. No admin approval gate (scope change from BR-14).
2. For the admin approval workflow (BR-14), what should happen after email verification?
   - Answer: Admin approval removed from mandatory flow. Registration is self-service with email verification. (Admin approval may be added as optional feature for enterprise orgs.)
3. What is the password expiration policy?
   - Answer: Configurable per organization. Org admins can set expiration policy for their tenants.
4. For account lockout (BR-19), should the lockout be IP-based, account-based, or both?
   - Answer: Account-based lockout only with auto-unlock after 15 minutes. No admin manual unlock needed.
5. Should the system support "magic link" email login?
   - Answer: Not discussed. Out of scope for Phase 1.

## Question List - Phase 3: M-SOCIAL (Social Login)
- Generated: 2026-02-25
- Status: Answered

6. When a user logs in via social provider with an email that already has a password-based account, how should account linking work?
   - Answer: User confirmation prompt - show user a prompt asking if they want to link to the existing account.
7. Should social login users be required to set a password for email/password login?
   - Answer: Not asked. Will make optional (user can add password in profile settings).
8. For Apple Sign-In "Hide My Email" feature?
   - Answer: Not asked. Will support proxy email as standard Apple Sign-In behavior.

## Question List - Phase 3: M-SSO (Enterprise SSO)
- Generated: 2026-02-25
- Status: Answered

9. Should the system support SAML JIT provisioning?
   - Answer: Yes - support SAML JIT provisioning for auto user creation on first SSO login.
10. Should the system enforce domain-based SSO routing?
    - Answer: Yes - auto-route @company.com emails to company's IdP.
11. Should the system support SCIM?
    - Answer: Yes - support SCIM for automated user provisioning/deprovisioning.
    - Note: Also support pre-provisioned users (admin creates users before SSO).

## Question List - Phase 3: M-WECHAT (WeChat & WeCom)
- Generated: 2026-02-25
- Status: Answered

12. How should Flutter app handle WeChat mobile login?
    - Answer: Full WeChat ecosystem - detect WeChat installation, offer WeChat login only when available. Support WeCom workplace SSO and standalone QR login.
13. WeCom integration scope?
    - Answer: Support both WeCom workplace app entry (auto-SSO) and standalone web login via WeCom QR code.

## Question List - Phase 3: M-MFA (Multi-Factor Authentication)
- Generated: 2026-02-25
- Status: Answered

14. MFA enforcement policy scope?
    - Answer: Per-organization configurable. Org admin decides whether to enforce MFA for their users.
15. Backup codes specification?
    - Answer: Not specifically asked. Will default to 10 one-time backup codes, regeneratable.
16. "Remember this device" duration?
    - Answer: 7 days default, configurable by org admin (1-90 days range).

## Question List - Phase 3: M-SESSION (Session Management)
- Generated: 2026-02-25
- Status: Answered

17. Force logout all sessions?
    - Answer: Yes, support force logout all sessions (included in concurrent session management).
18. Concurrent session limits?
    - Answer: Default max 5 concurrent sessions. Terminate oldest session when limit reached.

## Question List - Phase 3: M-RBAC (Role & Organization Management)
- Generated: 2026-02-25
- Status: Answered

19. Can a user belong to multiple organizations?
    - Answer: Yes. Org switcher dropdown in UI header. Each org has its own roles/permissions.
20. Custom roles support?
    - Answer: Support both predefined (Super Admin, Org Admin, User, Viewer) AND custom roles from the start.

## Question List - Phase 3: M-PLATFORM (Platform Adapters)
- Generated: 2026-02-25
- Status: Answered

21. Biometric login usage?
    - Answer: Both - quick unlock (password alternative for returning users) AND usable as MFA factor.
22. WeChat Mini Program auth methods?
    - Answer: Included in "Full WeChat ecosystem" - Mini Program uses WeChat-specific OAuth only.

## Question List - Phase 3: M-COMPLIANCE (Security & Compliance)
- Generated: 2026-02-25
- Status: Answered

23. GDPR account deletion approach?
    - Answer: Soft-delete with 30-day grace period. User can recover within 30 days. Permanent deletion after grace period.
24. Real-time security alerts?
    - Answer: Yes - real-time alerts for multiple failed logins, logins from new locations, concurrent suspicious sessions.

## Additional Questions (Round 4)
- Generated: 2026-02-25
- Status: Answered

25. Login UI language support?
    - Answer: English + Simplified Chinese (EN + ZH-CN) for Phase 1. Extensible i18n framework for future languages.
26. Technical approach for auth service?
    - Answer: Custom-built with open-source libraries (e.g., Passport.js, Spring Security). No managed IdP.
