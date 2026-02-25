# PRD Writer Agent - Research Log

## Research Entry 1
- Timestamp: 2026-02-25
- Tool: web-search
- Query: "JIRA Cloud authentication architecture SSO SAML OIDC best practices 2025 2026"
- Purpose: Understand how Atlassian JIRA Cloud handles authentication (the benchmark product)
- Findings:
  - JIRA supports both SAML 2.0 and OIDC for SSO
  - SAML JIT (Just-in-Time) provisioning for auto user creation
  - Multiple IdP support (mix SSO methods with default login form)
  - SSO handles authentication only; authorization (roles/permissions) managed separately
  - SCIM support for user provisioning lifecycle
  - Best practices: HTTPS for all IdP communication, align NameID attributes, keep SSO components updated
- Source: https://support.atlassian.com/atlassian-cloud/, https://confluence.atlassian.com/enterprise/

## Research Entry 2
- Timestamp: 2026-02-25
- Tool: web-search
- Query: "SaaS multi-tenant authentication system design patterns best practices OAuth2 MFA"
- Purpose: Research industry best practices for multi-tenant auth architecture
- Findings:
  - Core principle: "Authentication is global; authorization is tenant-scoped"
  - Tenant context mandatory everywhere downstream; SSO/MFA policies live on tenants
  - OAuth2 Authorization Code + PKCE recommended; tenant-scoped tokens
  - MFA should be per-tenant configurable with step-up authentication
  - Authorization: Externalize with PDP/PEP; support RBAC/ABAC
  - Data isolation patterns: shared tables with tenant_id, schema-per-tenant, or database-per-tenant
  - Compliance: structured audit logs, regional data residency
  - Strong recommendation against building custom IdP from scratch
- Source: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/, https://workos.com/blog/, https://auth0.com/blog/

## Research Entry 3
- Timestamp: 2026-02-25
- Tool: web-search
- Query: "WeChat OAuth login integration enterprise WeCom authentication best practices"
- Purpose: Research WeChat/WeCom authentication patterns for China market
- Findings:
  - WeChat OAuth 2.0 uses authorization_code flow
  - Two login scenarios: Web (QR code scanning) and Mobile (in-app OAuth)
  - Different OAuth endpoints for Web vs Mobile; may need two separate provider configs
  - WeChat requires developer account from verified organization (300 RMB), AppID and AppSecret
  - WeChat does NOT support login outside WeChat app in other mobile browsers
  - WeCom uses CorpID, Agent ID, and App Secret for authentication
  - WeCom supports OAuth 2.0, QR code login, and enterprise identity binding
  - Domain registration entity must match WeCom entity
  - Best practices: protect AppSecret, test in sandbox, handle account binding
- Source: https://developers.weixin.qq.com/, https://casdoor.org/docs/provider/oauth/Wechat/

## Research Entry 4
- Timestamp: 2026-02-25
- Tool: web-search
- Query: "Microsoft Teams tab SSO authentication integration guide best practices 2025"
- Purpose: Research Microsoft Teams SSO integration patterns
- Findings:
  - Teams SSO uses Microsoft Entra ID (formerly Azure AD) for one-time authentication
  - Flow: User signs in to Teams → Teams requests access token from Entra ID → Token passed to tab app
  - Requires app registration in Microsoft Entra ID with configured scopes
  - Client uses getAuthToken() from Teams JavaScript SDK
  - For Graph API access, server-side token exchange needed (OBO flow)
  - Teams Toolkit simplifies SSO integration
  - iOS considerations: Apple blocks third-party cookies, must use token-based system
  - Best practices: minimize scopes, implement token refresh, handle errors gracefully
  - Consider Nested App Authentication (NAA) for client-side Graph tokens
- Source: https://learn.microsoft.com/en-us/microsoftteams/platform/tabs/how-to/authentication/
