# Question Lists

## Phase 3: Research & Requirements Elicitation

---

### Question List #1 — 2026-02-24 16:05

Based on research of JIRA Cloud and multi-platform authentication best practices, the following questions need to be answered:

#### Authentication Methods
1. **Social Login**: Which social login providers do you need to support? (Google, Apple, Microsoft, WeChat)
2. **Enterprise SSO**: Which identity providers are required? (Okta, Azure AD/Entra ID, Google Workspace, custom SAML/OIDC)
3. **Password Policy**: Do you need local password authentication, or will SSO be primary?

#### Multi-Platform Requirements
4. **WeChat Integration**: Is this for Chinese market? (WeChat Official Account vs Enterprise WeChat/WeCom)
5. **Microsoft Teams**: Is this for Microsoft 365 integrated authentication or standalone?
6. **Mobile Apps**: Native iOS/Android apps, or responsive web (PWA)?
7. **API-only Access**: Do you need API key or service account authentication for integrations?

#### Security Requirements
8. **MFA/2FA**: Required for all users, optional, or admin-enforced for enterprise?
9. **Session Management**: Default session timeout? Remember device options?
10. **Password Reset**: Self-service password reset flow needed?

#### User Management
11. **User Invitation**: Can admins invite users via email? Public signup allowed?
12. **User Roles**: What role levels are needed? (Admin, User, Viewer, Custom)
13. **Organization/Tenant**: Multi-tenant support needed (separate organizations)?

#### Integration & Scope
14. **Existing Identity System**: Is there an existing user directory to integrate with?
15. **API Requirements**: Will other systems need to authenticate via API?
16. **Branding**: Custom login page branding required?

---

### Answered Summary #1 — 2026-02-24 16:25

| # | Question | Answer |
|---|----------|--------|
| 1 | Social Login | **All**: Google, Apple, Microsoft, WeChat |
| 2 | Enterprise SSO | **Azure AD, Google Workspace, Custom SAML/OIDC** |
| 3 | WeChat Type | **Both**: WeChat personal (微信) + Enterprise WeChat (企业微信) |
| 4 | MFA/2FA | **User-optional, Enterprise-mandatory** (regular users choose, enterprise users forced) |
| 5 | Mobile Platform | **Flutter** (native iOS/Android) |
| 6 | User Roles | **All**: Super Admin, Org Admin, Regular User, Viewer/Guest |
| 7 | Registration | **Open + Admin Approval** (self-register + admin review) |

---

### Question List #2 — 2026-02-24 16:25 (Additional Clarifications Needed)

1. **Session Timeout**: Default session duration?
2. **Password Requirements**: Password complexity policy?
3. **API Access**: External systems need API key authentication?
4. **Multi-tenant**: Multiple separate organizations needed?
5. **Branding**: Custom login page theming?
6. **Audit Logs**: Login activity audit required?
7. **Account Lockout**: Failed login lockout policy?
8. **Data Residency**: Region-specific requirements?

---

*Additional answers to be recorded after user response*
