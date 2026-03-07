# Main Tasks of a Security Engineer

A Security Engineer's core responsibilities throughout the project lifecycle:

---

## 📋 Project Lifecycle Tasks

### 1. Inception Phase
| Task | Description |
|---|---|
| **SE-INC-001 — Security Requirements Gathering** | Identifying security and compliance requirements (OWASP, ISO 27001, SOC 2, NIST) applicable to the project. |
| **SE-INC-002 — Threat Landscape Assessment** | Analyzing potential attack vectors, threat actors, and risk exposure based on the project's business context. |
| **SE-INC-003 — Regulatory & Compliance Mapping** | Mapping applicable regulations (GDPR, HIPAA, PCI-DSS) to technical security controls and obligations. |
| **SE-INC-004 — Security Architecture Review** | Evaluating proposed system architecture for security weaknesses, trust boundaries, and attack surface. |
| **SE-INC-005 — Risk Rating & Prioritization** | Classifying project risk level and determining the depth of security activities required throughout the lifecycle. |

### 2. Requirements Phase
| Task | Description |
|---|---|
| **SE-REQ-001 — Threat Modeling** | Conducting structured threat modeling (STRIDE, DREAD, attack trees) to identify and prioritize security threats. |
| **SE-REQ-002 — Security Controls Design** | Defining authentication, authorization, encryption, input validation, and session management controls. |
| **SE-REQ-003 — Secure Architecture Patterns** | Recommending zero-trust, defense-in-depth, least privilege, and secure-by-default design patterns. |
| **SE-REQ-004 — Data Classification & Protection** | Classifying data sensitivity levels and defining encryption, masking, tokenization, and retention requirements. |
| **SE-REQ-005 — Security Test Planning** | Defining the security testing strategy including SAST, DAST, SCA, penetration testing scope, and timelines. |

### 3. Sprint / Development Phase
| Task | Description |
|---|---|
| **SE-DEV-001 — Secure Code Review** | Reviewing code for security vulnerabilities (injection, XSS, CSRF, insecure deserialization, broken access control). |
| **SE-DEV-002 — SAST & SCA Integration** | Configuring and monitoring static analysis (SonarQube, Checkmarx) and dependency scanning (Snyk, Dependabot) in CI/CD. |
| **SE-DEV-003 — Secrets Management** | Implementing secure secrets handling using vaults (HashiCorp Vault, AWS Secrets Manager) and preventing credential leaks. |
| **SE-DEV-004 — Security Champions Coaching** | Training and mentoring development team security champions on secure coding practices and common vulnerability patterns. |
| **SE-DEV-005 — Security User Story Validation** | Verifying that security-related user stories and abuse cases are implemented correctly with proper controls. |

### 4. QA & UAT Phase
| Task | Description |
|---|---|
| **SE-QA-001 — Dynamic Application Security Testing (DAST)** | Running automated DAST scans (OWASP ZAP, Burp Suite) against deployed environments to detect runtime vulnerabilities. |
| **SE-QA-002 — Penetration Testing** | Conducting or coordinating manual penetration tests covering network, application, and API attack surfaces. |
| **SE-QA-003 — Vulnerability Assessment & Triage** | Consolidating scan results, validating findings, eliminating false positives, and prioritizing remediation. |
| **SE-QA-004 — Security Configuration Review** | Auditing server, container, cloud, and network configurations against CIS benchmarks and hardening guidelines. |
| **SE-QA-005 — Compliance Verification** | Verifying that all regulatory and compliance controls are implemented and generating evidence for audit readiness. |

### 5. Release & Growth Phase
| Task | Description |
|---|---|
| **SE-REL-001 — Pre-Release Security Sign-Off** | Issuing formal security clearance for production deployment based on resolved findings and accepted risks. |
| **SE-REL-002 — Security Monitoring & SIEM** | Configuring security event monitoring, log correlation (Splunk, ELK, Sentinel), and intrusion detection alerts. |
| **SE-REL-003 — Incident Response Readiness** | Establishing incident response playbooks, escalation procedures, and conducting tabletop exercises. |
| **SE-REL-004 — Vulnerability Management** | Continuously monitoring for new CVEs, zero-day threats, and coordinating patch cycles for production systems. |
| **SE-REL-005 — Security Posture Review** | Conducting periodic security assessments, red team exercises, and updating threat models based on evolving risks. |
