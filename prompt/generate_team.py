#!/usr/bin/env python3
"""
OpenClaw Team Generator — Creates all files for PM, IPM, and SA agents.
Generates ~1100+ files across ~119 directories.
Run from the workspace root: python3 prompt/generate_team.py
"""

import json
import os
from pathlib import Path
from datetime import date

WORKSPACE = Path("/Users/allenwang/build/ai/workspace/ramadan")
TODAY = date.today().isoformat()

# ═══════════════════════════════════════════════════════════════
# DATA DEFINITIONS
# ═══════════════════════════════════════════════════════════════

PM_TASKS = [
    # Inception Phase
    {"task_id": "PM-INC-001", "name": "Project Charter Development", "phase": "Inception", "wave": 1, "step": 1,
     "skill_dir": "pm-project-charter-development",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Drafting the project charter defining objectives, scope, stakeholders, constraints, and success criteria."},
    {"task_id": "PM-INC-002", "name": "Stakeholder Analysis", "phase": "Inception", "wave": 1, "step": 2,
     "skill_dir": "pm-stakeholder-analysis",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Identifying stakeholders, assessing their influence and interest, and developing a stakeholder engagement plan."},
    {"task_id": "PM-INC-003", "name": "Resource Planning", "phase": "Inception", "wave": 1, "step": 3,
     "skill_dir": "pm-resource-planning",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Estimating team composition, skillsets, and resource availability needed for project execution."},
    {"task_id": "PM-INC-004", "name": "Budget Estimation", "phase": "Inception", "wave": 1, "step": 4,
     "skill_dir": "pm-budget-estimation",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Developing initial cost estimates covering personnel, infrastructure, licensing, and contingency reserves."},
    {"task_id": "PM-INC-005", "name": "Risk Register Initialization", "phase": "Inception", "wave": 1, "step": 5,
     "skill_dir": "pm-risk-register-initialization",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Identifying early project risks, assessing probability and impact, and defining initial mitigation strategies."},
    # Requirements Phase
    {"task_id": "PM-REQ-001", "name": "Project Plan & WBS", "phase": "Requirements", "wave": 1, "step": 1,
     "skill_dir": "pm-project-plan-wbs",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Creating the detailed project plan with Work Breakdown Structure, milestones, and critical path analysis."},
    {"task_id": "PM-REQ-002", "name": "Schedule Development", "phase": "Requirements", "wave": 1, "step": 2,
     "skill_dir": "pm-schedule-development",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Building project timelines using Gantt charts, defining dependencies, and setting baseline schedules."},
    {"task_id": "PM-REQ-003", "name": "RACI Matrix Definition", "phase": "Requirements", "wave": 1, "step": 3,
     "skill_dir": "pm-raci-matrix-definition",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Establishing clear roles and responsibilities across all workstreams using RACI (Responsible, Accountable, Consulted, Informed)."},
    {"task_id": "PM-REQ-004", "name": "Communication Plan", "phase": "Requirements", "wave": 1, "step": 4,
     "skill_dir": "pm-communication-plan",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Defining reporting cadence, meeting schedules, escalation paths, and communication channels for all stakeholders."},
    {"task_id": "PM-REQ-005", "name": "Vendor & Procurement Management", "phase": "Requirements", "wave": 1, "step": 5,
     "skill_dir": "pm-vendor-procurement-management",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Coordinating vendor selection, contract negotiation, SOWs, and third-party onboarding when applicable."},
    # Development Phase
    {"task_id": "PM-DEV-001", "name": "Progress Tracking & Reporting", "phase": "Development", "wave": 1, "step": 1,
     "skill_dir": "pm-progress-tracking-reporting",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Monitoring project health through status reports, dashboards, earned value metrics, and milestone tracking."},
    {"task_id": "PM-DEV-002", "name": "Risk & Issue Management", "phase": "Development", "wave": 1, "step": 2,
     "skill_dir": "pm-risk-issue-management",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Continuously updating the risk register, managing issue logs, and driving resolution of escalated blockers."},
    {"task_id": "PM-DEV-003", "name": "Scope Management", "phase": "Development", "wave": 1, "step": 3,
     "skill_dir": "pm-scope-management",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Controlling scope through formal change request processes, impact assessments, and change control board decisions."},
    {"task_id": "PM-DEV-004", "name": "Resource Management", "phase": "Development", "wave": 1, "step": 4,
     "skill_dir": "pm-resource-management",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Balancing team workloads, resolving resource conflicts, and adjusting allocations based on project needs."},
    {"task_id": "PM-DEV-005", "name": "Stakeholder Communication", "phase": "Development", "wave": 1, "step": 5,
     "skill_dir": "pm-stakeholder-communication",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Conducting regular status meetings, steering committee updates, and executive briefings to maintain alignment."},
    # QA Phase
    {"task_id": "PM-QA-001", "name": "UAT Coordination", "phase": "QA", "wave": 1, "step": 1,
     "skill_dir": "pm-uat-coordination",
     "next": ["IPM-QA-001", "IPM-QA-002", "IPM-QA-003"],
     "description": "Planning UAT timelines, coordinating business user participation, and ensuring environment readiness."},
    {"task_id": "PM-QA-002", "name": "Go/No-Go Decision Facilitation", "phase": "QA", "wave": 1, "step": 2,
     "skill_dir": "pm-go-no-go-decision-facilitation",
     "next": ["IPM-QA-001", "IPM-QA-002", "IPM-QA-003"],
     "description": "Organizing go/no-go review meetings with key stakeholders based on quality metrics and risk assessment."},
    {"task_id": "PM-QA-003", "name": "Release Planning", "phase": "QA", "wave": 1, "step": 3,
     "skill_dir": "pm-release-planning",
     "next": ["IPM-QA-001", "IPM-QA-002", "IPM-QA-003"],
     "description": "Coordinating release schedules, deployment windows, and rollback contingencies with all involved teams."},
    {"task_id": "PM-QA-004", "name": "Compliance & Audit Readiness", "phase": "QA", "wave": 1, "step": 4,
     "skill_dir": "pm-compliance-audit-readiness",
     "next": ["IPM-QA-001", "IPM-QA-002", "IPM-QA-003"],
     "description": "Ensuring all project documentation, approvals, and sign-offs are complete for governance and audit requirements."},
    # Release Phase
    {"task_id": "PM-REL-001", "name": "Go-Live Coordination", "phase": "Release", "wave": 1, "step": 1,
     "skill_dir": "pm-go-live-coordination",
     "next": ["IPM-REL-001", "IPM-REL-002", "IPM-REL-003", "IPM-REL-004"],
     "description": "Orchestrating the production launch across development, operations, support, and business teams."},
    {"task_id": "PM-REL-002", "name": "Hypercare Management", "phase": "Release", "wave": 1, "step": 2,
     "skill_dir": "pm-hypercare-management",
     "next": ["IPM-REL-001", "IPM-REL-002", "IPM-REL-003", "IPM-REL-004"],
     "description": "Managing the post-launch support period with dedicated resources, escalation procedures, and rapid response."},
    {"task_id": "PM-REL-003", "name": "Project Closure", "phase": "Release", "wave": 1, "step": 3,
     "skill_dir": "pm-project-closure",
     "next": [],
     "description": "Conducting formal project closure including final sign-offs, budget reconciliation, and contract closeouts."},
    {"task_id": "PM-REL-004", "name": "Lessons Learned & Retrospective", "phase": "Release", "wave": 1, "step": 4,
     "skill_dir": "pm-lessons-learned-retrospective",
     "next": [],
     "description": "Facilitating post-project retrospectives to capture successes, challenges, and improvement recommendations."},
    {"task_id": "PM-REL-005", "name": "Benefits Handover", "phase": "Release", "wave": 1, "step": 5,
     "skill_dir": "pm-benefits-handover",
     "next": [],
     "description": "Transitioning project deliverables to operations and business owners with documented support and maintenance plans."},
]

IPM_TASKS = [
    # Inception Phase
    {"task_id": "IPM-INC-001", "name": "Requirement Gathering", "phase": "Inception", "wave": 2, "step": 1,
     "skill_dir": "ipm-requirement-gathering",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "In-depth interviews with stakeholders/customers to collect raw requirements."},
    {"task_id": "IPM-INC-002", "name": "Market Research", "phase": "Inception", "wave": 2, "step": 2,
     "skill_dir": "ipm-market-research",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "Analyzing competitors, industry trends, and user pain points."},
    {"task_id": "IPM-INC-003", "name": "BRD Writing", "phase": "Inception", "wave": 2, "step": 3,
     "skill_dir": "ipm-brd-writing",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "Creating the Business Requirement Document to define commercial value and goals."},
    {"task_id": "IPM-INC-004", "name": "Feasibility Assessment", "phase": "Inception", "wave": 2, "step": 4,
     "skill_dir": "ipm-feasibility-assessment",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "Collaborating with technical teams to evaluate technical viability."},
    {"task_id": "IPM-INC-005", "name": "Alignment", "phase": "Inception", "wave": 2, "step": 5,
     "skill_dir": "ipm-alignment",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "Achieving consensus among business, technical, and design stakeholders."},
    # Requirements Phase
    {"task_id": "IPM-REQ-001", "name": "PRD Writing", "phase": "Requirements", "wave": 2, "step": 1,
     "skill_dir": "ipm-prd-writing",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Creating the Product Requirement Document with detailed logic, boundaries, and interactions."},
    {"task_id": "IPM-REQ-002", "name": "User Story Decomposition", "phase": "Requirements", "wave": 2, "step": 2,
     "skill_dir": "ipm-user-story-decomposition",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Breaking down large requirements into deliverable User Stories (Definition of Ready - DoR)."},
    {"task_id": "IPM-REQ-003", "name": "Prioritization", "phase": "Requirements", "wave": 2, "step": 3,
     "skill_dir": "ipm-prioritization",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Ranking requirements using frameworks like MoSCoW or RICE."},
    {"task_id": "IPM-REQ-004", "name": "Prototype Review", "phase": "Requirements", "wave": 2, "step": 4,
     "skill_dir": "ipm-prototype-review",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Collaborating with designers to finalize UI/UX solutions."},
    {"task_id": "IPM-REQ-005", "name": "Refinement Meetings", "phase": "Requirements", "wave": 2, "step": 5,
     "skill_dir": "ipm-refinement-meetings",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Organizing requirement reviews to ensure shared understanding across teams."},
    # Development Phase
    {"task_id": "IPM-DEV-001", "name": "Requirement Clarification", "phase": "Development", "wave": 2, "step": 1,
     "skill_dir": "ipm-requirement-clarification",
     "next": ["SM-DEV-001", "SM-DEV-002", "SM-DEV-003", "SM-DEV-004"],
     "description": "Responding to developer and tester queries in real-time."},
    {"task_id": "IPM-DEV-002", "name": "Acceptance Criteria", "phase": "Development", "wave": 2, "step": 2,
     "skill_dir": "ipm-acceptance-criteria",
     "next": ["SM-DEV-001", "SM-DEV-002", "SM-DEV-003", "SM-DEV-004"],
     "description": "Defining the specific conditions that must be met for each feature."},
    {"task_id": "IPM-DEV-003", "name": "PRD Change Management", "phase": "Development", "wave": 2, "step": 3,
     "skill_dir": "ipm-prd-change-management",
     "next": ["SM-DEV-001", "SM-DEV-002", "SM-DEV-003", "SM-DEV-004"],
     "description": "Managing requirement changes and assessing their impact."},
    {"task_id": "IPM-DEV-004", "name": "Progress Tracking", "phase": "Development", "wave": 2, "step": 4,
     "skill_dir": "ipm-progress-tracking",
     "next": ["SM-DEV-001", "SM-DEV-002", "SM-DEV-003", "SM-DEV-004"],
     "description": "Monitoring delivery timelines and identifying risks early."},
    # QA Phase
    {"task_id": "IPM-QA-001", "name": "UAT Organization", "phase": "QA", "wave": 2, "step": 1,
     "skill_dir": "ipm-uat-organization",
     "next": ["SM-QA-001", "SM-QA-002", "SM-QA-003"],
     "description": "Coordinating User Acceptance Testing with users/business owners."},
    {"task_id": "IPM-QA-002", "name": "Bug Prioritization", "phase": "QA", "wave": 2, "step": 2,
     "skill_dir": "ipm-bug-prioritization",
     "next": ["SM-QA-001", "SM-QA-002", "SM-QA-003"],
     "description": "Deciding which bugs are critical and whether they block release."},
    {"task_id": "IPM-QA-003", "name": "Launch Checklist", "phase": "QA", "wave": 2, "step": 3,
     "skill_dir": "ipm-launch-checklist",
     "next": ["SM-QA-001", "SM-QA-002", "SM-QA-003"],
     "description": "Confirming release standards (Definition of Done - DoD)."},
    # Release Phase
    {"task_id": "IPM-REL-001", "name": "Release Coordination", "phase": "Release", "wave": 2, "step": 1,
     "skill_dir": "ipm-release-coordination",
     "next": ["SM-REL-001", "SM-REL-002", "SM-REL-003", "SM-REL-004"],
     "description": "Planning release schedules, canary deployments, and rollback strategies."},
    {"task_id": "IPM-REL-002", "name": "Data Analysis", "phase": "Release", "wave": 2, "step": 2,
     "skill_dir": "ipm-data-analysis",
     "next": ["SM-REL-001", "SM-REL-002", "SM-REL-003", "SM-REL-004"],
     "description": "Analyzing KPIs after launch to verify if objectives were met."},
    {"task_id": "IPM-REL-003", "name": "User Feedback", "phase": "Release", "wave": 2, "step": 3,
     "skill_dir": "ipm-user-feedback",
     "next": ["SM-REL-001", "SM-REL-002", "SM-REL-003", "SM-REL-004"],
     "description": "Collecting continuous feedback for the next iteration cycle."},
    {"task_id": "IPM-REL-004", "name": "Retrospectives", "phase": "Release", "wave": 2, "step": 4,
     "skill_dir": "ipm-retrospectives",
     "next": [],
     "description": "Organizing project/sprint retrospectives to optimize collaboration."},
]

# SA tasks that need new skill files (empty dirs exist)
SA_INCOMPLETE_TASKS = [
    {"task_id": "IA-INC-007", "name": "Compliance & Privacy Scan", "phase": "Inception", "wave": 10, "step": 7,
     "skill_dir": "sa-compliance-privacy-scan",
     "next": ["TL-INC-001", "TL-INC-002", "TL-INC-003", "TL-INC-004", "TL-INC-005"],
     "description": "Highlighting regulatory or policy constraints (PII/PHI, data residency, industry standards) that shape solution boundaries."},
    {"task_id": "IA-INC-008", "name": "Third-Party/Vendor Strategy", "phase": "Inception", "wave": 10, "step": 8,
     "skill_dir": "sa-third-party-vendor-strategy",
     "next": ["TL-INC-001", "TL-INC-002", "TL-INC-003", "TL-INC-004", "TL-INC-005"],
     "description": "Assessing SaaS/Cloud vendors, integration fit, contractual constraints, and exit/mitigation options."},
    {"task_id": "IA-REQ-008", "name": "Vendor & Third-Party Controls", "phase": "Requirements", "wave": 10, "step": 8,
     "skill_dir": "sa-vendor-third-party-controls",
     "next": ["TL-REQ-001", "TL-REQ-002", "TL-REQ-003", "TL-REQ-004", "TL-REQ-005"],
     "description": "Specifying integration safeguards, SLAs, and operational models for external services and suppliers."},
    {"task_id": "IA-REQ-009", "name": "Requirements Traceability & Compliance Mapping", "phase": "Requirements", "wave": 10, "step": 9,
     "skill_dir": "sa-requirements-traceability",
     "next": ["TL-REQ-001", "TL-REQ-002", "TL-REQ-003", "TL-REQ-004", "TL-REQ-005"],
     "description": "Maintaining bidirectional traceability from business/NFR items to design, tests, and runbooks, including privacy and regulatory clauses."},
    {"task_id": "IA-DEV-005", "name": "Architecture Decision Records (ADRs)", "phase": "Development", "wave": 10, "step": 5,
     "skill_dir": "sa-adr",
     "next": ["TL-DEV-001", "TL-DEV-002", "TL-DEV-003", "TL-DEV-004", "TL-DEV-005"],
     "description": "Documenting key technical decisions, rationale, and trade-offs for future reference."},
    {"task_id": "IA-DEV-006", "name": "IaC & Environment Baseline", "phase": "Development", "wave": 10, "step": 6,
     "skill_dir": "sa-iac-environment-baseline",
     "next": ["TL-DEV-001", "TL-DEV-002", "TL-DEV-003", "TL-DEV-004", "TL-DEV-005"],
     "description": "Establishing reproducible environments (IaC, configuration management) and enforcing drift controls across dev/test/stage/prod."},
    {"task_id": "IA-QA-003", "name": "Infrastructure Validation", "phase": "QA", "wave": 10, "step": 3,
     "skill_dir": "sa-infrastructure-validation",
     "next": ["TL-QA-001", "TL-QA-002", "TL-QA-003", "TL-QA-004"],
     "description": "Verifying that deployment environments match the designed architecture specifications."},
    {"task_id": "IA-QA-004", "name": "Integration Testing Support", "phase": "QA", "wave": 10, "step": 4,
     "skill_dir": "sa-integration-testing-support",
     "next": ["TL-QA-001", "TL-QA-002", "TL-QA-003", "TL-QA-004"],
     "description": "Ensuring end-to-end integration points function correctly across system boundaries."},
    {"task_id": "IA-QA-005", "name": "Compliance Validation", "phase": "QA", "wave": 10, "step": 5,
     "skill_dir": "sa-compliance-validation",
     "next": ["TL-QA-001", "TL-QA-002", "TL-QA-003", "TL-QA-004"],
     "description": "Verifying regulatory, privacy, and policy requirements through targeted test cases and evidence collection."},
    {"task_id": "IA-REL-001", "name": "Deployment Architecture", "phase": "Release", "wave": 10, "step": 1,
     "skill_dir": "sa-deployment-architecture",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Designing CI/CD pipelines, blue-green/canary deployment strategies, and rollback mechanisms."},
    {"task_id": "IA-REL-002", "name": "Monitoring & Observability", "phase": "Release", "wave": 10, "step": 2,
     "skill_dir": "sa-monitoring-observability",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Setting up logging, metrics, alerting, and distributed tracing for production systems."},
    {"task_id": "IA-REL-003", "name": "Capacity Planning", "phase": "Release", "wave": 10, "step": 3,
     "skill_dir": "sa-capacity-planning",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Analyzing production data to forecast scaling needs and optimize resource utilization."},
    {"task_id": "IA-REL-004", "name": "Post-Mortem Analysis", "phase": "Release", "wave": 10, "step": 4,
     "skill_dir": "sa-post-mortem-analysis",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Leading technical root-cause analysis for production incidents and outages."},
    {"task_id": "IA-REL-005", "name": "Architecture Evolution", "phase": "Release", "wave": 10, "step": 5,
     "skill_dir": "sa-architecture-evolution",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Refining the architecture based on real-world performance data and emerging requirements."},
    {"task_id": "IA-REL-006", "name": "Runbooks & Knowledge Transfer", "phase": "Release", "wave": 10, "step": 6,
     "skill_dir": "sa-runbooks-knowledge-transfer",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Delivering operational runbooks, onboarding material, and handover sessions for support/ops teams."},
    {"task_id": "IA-REL-007", "name": "FinOps & Cost Guardrails", "phase": "Release", "wave": 10, "step": 7,
     "skill_dir": "sa-finops-cost-guardrails",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Establishing cost baselines, alerts, and optimization playbooks tied to usage trends."},
    {"task_id": "IA-REL-008", "name": "Resilience/Chaos Testing", "phase": "Release", "wave": 10, "step": 8,
     "skill_dir": "sa-resilience-chaos-testing",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Designing and running chaos or game-day exercises to validate failure modes and recovery paths."},
    {"task_id": "IA-REL-009", "name": "Architecture Governance & Change Control", "phase": "Release", "wave": 10, "step": 9,
     "skill_dir": "sa-architecture-governance-change-control",
     "next": ["TL-REL-001", "TL-REL-002", "TL-REL-003", "TL-REL-004", "TL-REL-005"],
     "description": "Setting review cadences, change-control workflows, and ADR audits to keep the architecture baseline governed and current."},
]

# SA supervisors that need to be created (main exists but supervisor is empty)
SA_MISSING_SUPERVISORS = ["sa-dr-bcp-architecture", "sa-technical-debt-management"]

PHASE_CODE_MAP = {"Inception": "INC", "Requirements": "REQ", "Development": "DEV", "QA": "QA", "Release": "REL"}

# ═══════════════════════════════════════════════════════════════
# TEMPLATE GENERATORS
# ═══════════════════════════════════════════════════════════════

def gen_skill_md(task, role_name, role_code, workspace_code):
    """Generate SKILL.md content for a main skill."""
    t = task
    skill_name = t["skill_dir"]
    title_parts = t["name"]
    next_str = ", ".join(t["next"]) if t["next"] else "None (terminal task)"

    # Build upstream description based on role and phase
    if role_code == "PM":
        upstream = "- **User / Organization**: Project initiation request and strategic objectives"
        if t["phase"] != "Inception":
            upstream += f"\n- **Previous PM phase outputs**: Completed {t['phase']} prerequisites"
        downstream_role = "IPM (IT Product Manager)"
    elif role_code == "IPM":
        upstream = "- **PM Agent**: Project Charter, Stakeholder Analysis, Resource Plan from Wave 1"
        if t["phase"] != "Inception":
            upstream += f"\n- **Previous IPM phase outputs**: Completed {t['phase']} prerequisites"
        downstream_role = "SM (Scrum Master)"
    else:  # SA
        upstream = "- **Solutions Architect outputs**: SAD, Integration Architecture, NFR Mapping, Technology Blueprint"
        if t["phase"] != "Inception":
            upstream += f"\n- **Previous SA phase outputs**: Completed {t['phase']} prerequisites"
        downstream_role = "TL (Technical Lead)"

    return f"""---
name: {skill_name}
description: "{role_name} skill for {t['description'].rstrip('.')}. Use when: (1) PM assigns task {t['task_id']} via TaskTriggered event, (2) {t['phase']} phase {t['name'].lower()} activities are needed, (3) orchestrating {t['name'].lower()} deliverables for downstream team tasks."
---

# {role_code} {title_parts}

Role: {role_name} | Task ID: {t['task_id']} | Wave: {t['wave']}, Step: {t['step']}

## Objective

{t['description']}

## Upstream Inputs

{upstream}

## Downstream Triggers

On TaskCompleted (after supervisor 100% pass):
- {next_str}

## Workflow (Phase 0-5)

### Phase 0: Initialization

1. Create output directory: `~/.openclaw/workspace-{workspace_code}/outputs/{t['task_id']}/`
2. Initialize logs: `conversation-log.md`, `work-log.md`, `question-lists.md`, `research-log.md`
3. Log: `[{{timestamp}}] Phase 0: Initialization — Status: completed`
4. Before proceeding, read `references/dor.md` to verify all prerequisites
5. Check DoR items — if required items missing, request from PM via event

### Phase 1: Understand Task Purpose

1. Receive the task context from user or upstream task artifacts
2. Analyze and summarize understanding of the **task purpose** (why {t['name'].lower()} is needed)
3. Present understanding to user and ask for confirmation
4. If user disagrees → re-analyze and present again
5. If user agrees → record confirmation in conversation log, proceed to Phase 2

### Phase 2: Understand the Topic

1. Analyze the topic in depth (who, what, why, when, where, how)
2. Incorporate findings from upstream task artifacts
3. Present topic understanding to user
4. Ask user for confirmation
5. If user disagrees → refine and present again
6. If user agrees → record confirmation, proceed to Phase 3

### Phase 3: Research & Question Generation

1. Research the topic using web search and authoritative knowledge bases
2. **Save all research to `research-log.md`** (tool, query, findings, sources)
3. Analyze industry best practices, benchmarks, and relevant standards
4. Present industry findings to user
5. Generate structured question list based on research gaps
6. **Save question list to `question-lists.md`**
7. Conduct interactive Q&A with user — one question at a time or small groups
8. Iterate until all critical information is gathered
9. **Save each round's questions and answered summaries to `question-lists.md`**
10. Consolidate into validated requirements list
11. Present requirements list to user for final confirmation

### Phase 4: Execute & Produce Deliverables

1. Read `references/output-templates.md` — follow the output template strictly
2. Read `references/dod.md` — ensure all quality gates are addressed
3. Research additional details as needed — **log all research to `research-log.md`**
4. Draft all deliverable sections following the template structure
5. Self-review against DoD checklist
6. Fix any issues found in self-review
7. Save deliverables to output directory

### Phase 5: Completion & Handoff

1. Read `references/dod.md` and verify every criterion
2. Check completeness, deliverable quality, process quality
3. If any critical/high items fail → return to Phase 4 to fix
4. Repeat until all checks pass
5. Save final deliverables
6. Present completion summary to user
7. Invoke supervisor: send SupervisorTriggered event to `{skill_name}-supervisor`
8. If supervisor returns issues → remediate and re-invoke supervisor
9. Once supervisor approves (100% pass) → send TaskCompleted to PM with:
   - Deliverable file path and filename
   - RACI matrix (for triggering downstream tasks)
   - Final inspection report

## Resources

Load these reference files at the indicated times:

- **Before Phase 1**: Read `references/dor.md` to verify all prerequisites
- **During Phase 3**: Read `references/raci.md` for stakeholder roles during elicitation
- **Before Phase 4**: Read `references/output-templates.md` for deliverable structure
- **Before Phase 4**: Read `references/dod.md` to understand quality gates while drafting
- **During Phase 4**: Read `references/sop.md` for detailed step-by-step procedure
- **After Phase 4**: Read `references/dod.md` to run self-check
- **Phase 5**: Run `scripts/verify_dod.py` for automated DoD verification
- **Trigger config**: See `references/triggers.md` for activation conditions

## Logging

Maintain four logs in the output directory throughout execution:

### conversation-log.md
```
### Question #1 — {{timestamp}}
**Agent**: {{question asked}}
**User**: {{user response}}
```

### work-log.md
```
- [{{timestamp}}] {{action_description}} — Status: {{completed/in-progress/failed}}
```

### question-lists.md
```
## Phase {{N}}: {{phase_name}} — {{timestamp}}
### Question List #{{seq}}
1. {{question}}
### Answered Summary
- Q1: {{answer_summary}}
```

### research-log.md
```
## Research #{{seq}} — {{timestamp}}
- **Tool**: {{web_search / context7 / web_fetch / ...}}
- **Query/URL**: {{search_query_or_url}}
- **Purpose**: {{why this research was needed}}
- **Key Findings**:
  1. {{finding}}
- **Source**: {{url_or_reference}}
```
"""


def gen_supervisor_md(task, role_name, role_code):
    """Generate supervisor SKILL.md content."""
    t = task
    skill_name = t["skill_dir"]

    return f"""---
name: {skill_name}-supervisor
description: "Supervisor inspection skill for {skill_name}. Use when: (1) {role_code} agent completes self-check for task {t['task_id']}, (2) SupervisorTriggered event received from {skill_name} skill, (3) quality gate verification needed before TaskCompleted is sent to PM."
---

# {role_code} {t['name']} — Supervisor

Role: {role_name} Supervisor | Task ID: {t['task_id']} | Inspection Agent

## Inspection Scope

Independent quality review of the {t['name']} output for task {t['task_id']}. This supervisor:
- Operates independently from the {role_code} {t['name']} agent
- Reviews only — never modifies deliverables directly
- Must achieve 100% pass rate before TaskCompleted can be sent to PM

## Trigger

Activated when the {role_code} {t['name']} agent sends SupervisorTriggered event with:
- Deliverable file path
- Output directory (containing conversation-log.md, work-log.md, question-lists.md, research-log.md)
- Skill directory path (containing references/)

## Inspection Checklist

### Infrastructure Checks (INS-01 through INS-08)

| ID | Check Item | Severity |
|----|-----------|----------|
| INS-01 | references/triggers.md exists and properly structured | Critical |
| INS-02 | references/raci.md exists with roles AND task assignments | Critical |
| INS-03 | references/output-templates.md exists with deliverable template | Critical |
| INS-04 | references/sop.md exists with complete Phase 0-5 workflow | Critical |
| INS-05 | references/dod.md exists with quality gate definitions | Critical |
| INS-06 | references/dor.md exists with prerequisite definitions | Critical |
| INS-07 | conversation-log.md exists with numbered user interactions | Critical |
| INS-08 | work-log.md exists with timestamped agent actions | Critical |

### Process Checks (INS-09 through INS-12)

| ID | Check Item | Severity |
|----|-----------|----------|
| INS-09 | DoD verification was performed and all critical/high items passed | Critical |
| INS-10 | question-lists.md exists with phase-labeled sections and answered summaries | Critical |
| INS-11 | research-log.md exists with tool, query, findings, source for each entry | Critical |
| INS-12 | User confirmation obtained for task purpose and topic understanding | Critical |

### Deliverable Quality Checks (INS-DQ-01 through INS-DQ-05)

| ID | Check Item | Severity |
|----|-----------|----------|
| INS-DQ-01 | All required deliverable sections present and populated | Critical |
| INS-DQ-02 | No TBD, TODO, or placeholder text in final deliverable | Critical |
| INS-DQ-03 | Deliverable follows output template structure | High |
| INS-DQ-04 | All acceptance criteria are testable and measurable | High |
| INS-DQ-05 | Upstream traceability — inputs referenced and decisions traceable | High |

## Inspection Process

```
[Trigger] {role_code} {t['name']} agent sends SupervisorTriggered
     |
     v
[Load] Read references/inspection-criteria.md for detailed verification rules
     |
     v
[Check] Inspect each item INS-01 through INS-12 + INS-DQ-01 through INS-DQ-05
     |
     v
[Report] Generate inspection report (format below)
     |
     v
[Decide] Pass rate = 100%?
     |-- No  -> Return report to {role_code} agent for remediation
     |          Agent fixes and re-sends SupervisorTriggered
     |          Repeat until 100% pass
     |-- Yes -> Notify PM Agent with completion package
```

## Inspection Report Format

```markdown
# {role_code} {t['name']} Supervisor Inspection Report

- Inspection Time: {{timestamp}}
- Inspection Round: #{{N}}
- Deliverable File Path: {{file_path}}

## Inspection Results

| Check Item | Status | Notes |
|:-----------|:------:|:------|
| INS-01: Triggers Config | PASS/FAIL | {{notes}} |
| INS-02: RACI Matrix | PASS/FAIL | {{notes}} |
| INS-03: Output Template | PASS/FAIL | {{notes}} |
| INS-04: SOP Process | PASS/FAIL | {{notes}} |
| INS-05: DoD Checklist | PASS/FAIL | {{notes}} |
| INS-06: DoR Checklist | PASS/FAIL | {{notes}} |
| INS-07: Conversation Log | PASS/FAIL | {{notes}} |
| INS-08: Work Log | PASS/FAIL | {{notes}} |
| INS-09: DoD Verification Passed | PASS/FAIL | {{notes}} |
| INS-10: Question Lists Log | PASS/FAIL | {{notes}} |
| INS-11: Research Log | PASS/FAIL | {{notes}} |
| INS-12: User Confirmation | PASS/FAIL | {{notes}} |
| INS-DQ-01: Deliverable Complete | PASS/FAIL | {{notes}} |
| INS-DQ-02: No Unresolved TBDs | PASS/FAIL | {{notes}} |
| INS-DQ-03: Template Followed | PASS/FAIL | {{notes}} |
| INS-DQ-04: Acceptance Criteria | PASS/FAIL | {{notes}} |
| INS-DQ-05: Upstream Traceability | PASS/FAIL | {{notes}} |

## Overall Pass Rate: {{X}}% ({{M}}/17 items passed)

## Issues Requiring Remediation
1. {{issue_description}} — Suggested fix: {{suggestion}}

## Conclusion: [FAIL -> Return to {role_code} Agent | PASS -> Notify PM Agent]
```

## On 100% Pass

1. Generate final report marked "ALL PASSED"
2. Notify **PM Agent** with:
   - Deliverable file path
   - RACI matrix configuration (for triggering downstream tasks)
   - Final inspection report

## Resources

- Inspection criteria details: see `references/inspection-criteria.md`
"""


def gen_dor(task, role_name, workspace_code):
    """Generate Definition of Ready."""
    t = task
    return f"""# Definition of Ready (DoR) — {t['task_id']} {t['name']}

Prerequisites that must be satisfied before starting {t['name']}.
Items marked **required** MUST be available; others are recommended.

| ID | Check | Required | Source | Fallback |
|----|-------|----------|--------|----------|
| DOR-001 | Task context / business problem provided | Yes | User input or upstream | — |
| DOR-002 | Upstream task artifacts available | Yes | Upstream task output | Request from PM |
| DOR-003 | Project Charter exists (PM deliverable) | No | PM Agent | Proceed with user as sponsor |
| DOR-004 | Stakeholder information available | No | User input or org context | Ask user during elicitation |
| DOR-005 | Business context available | No | User input, docs, or web research | Research and confirm with user |
| DOR-006 | Initial scope indication | No | User input | Collaboratively define during elicitation |
| DOR-007 | Relevant prior documents | No | User-provided files | Proceed without if unavailable |
| DOR-008 | Industry / domain context identifiable | Yes | Inferred from topic or explicit | — |
| DOR-009 | Output location defined | Yes | User input or default | Default: `~/.openclaw/workspace-{workspace_code}/outputs/{t['task_id']}/` |
| DOR-010 | Language preference | No | User input | Default: English |
"""


def gen_dod(task, role_name):
    """Generate Definition of Done."""
    t = task
    return f"""# Definition of Done (DoD) — {t['task_id']} {t['name']}

Quality gates that must ALL pass for {t['name']} deliverables to be considered complete.

## Completeness Checks

| ID | Check | Severity |
|----|-------|----------|
| DOD-C01 | All required deliverable sections present and populated with meaningful content | Critical |
| DOD-C02 | Objectives traceable to at least one requirement or stakeholder need | Critical |
| DOD-C03 | Every deliverable item has defined, testable acceptance criteria | Critical |
| DOD-C04 | In-scope and out-of-scope items explicitly listed where applicable | Critical |
| DOD-C05 | All stakeholders documented with roles and responsibilities | High |
| DOD-C06 | All assumptions explicitly stated | High |
| DOD-C07 | Constraints (budget, time, technology, regulatory) listed | High |
| DOD-C08 | Dependencies identified | High |
| DOD-C09 | Risk assessment populated with probability, impact, and mitigation | High |
| DOD-C10 | KPIs defined, measurable, and tied to objectives | Critical |

## Deliverable Quality

| ID | Check | Severity |
|----|-------|----------|
| DOD-D01 | Clear, concise language accessible to target audience | High |
| DOD-D02 | Objectives in SMART format where applicable | High |
| DOD-D03 | No spelling, grammar, or formatting errors | Medium |
| DOD-D04 | Version number, date, author, and change log complete | High |
| DOD-D05 | Zero TBD/TODO placeholders in final version | Critical |

## Process Quality

| ID | Check | Severity |
|----|-------|----------|
| DOD-P01 | User confirmation obtained for task purpose and topic understanding | Critical |
| DOD-P02 | Industry research conducted and applied | High |
| DOD-P03 | Interactive Q&A completed with structured question lists | High |
| DOD-P04 | conversation-log.md recorded with all user interactions | High |
| DOD-P05 | work-log.md recorded with timestamps for all actions | High |
| DOD-P06 | question-lists.md recorded with phase context and answered summaries | High |
| DOD-P07 | research-log.md recorded with tool, query, findings, source | High |
"""


def gen_raci(task, role_name, role_code):
    """Generate RACI matrix."""
    t = task
    return f"""# RACI Matrix — {t['task_id']} {t['name']}

R = Responsible, A = Accountable, C = Consulted, I = Informed

## Roles

| ID | Role | Description |
|----|------|-------------|
| {role_code} | {role_name} | Primary executor; produces and delivers {t['name']} outputs |
| PM | Project Manager | Oversees process, ensures timeline adherence, coordinates stakeholders |
| SPONSOR | Project Sponsor | Provides strategic direction, funding authority, final approval |
| SME | Subject Matter Expert | Provides domain-specific knowledge and validates deliverables |
| END_USER | End User / Business Stakeholder | Provides actual needs, validates from user perspective |
| ARCHITECT | Solution Architect / Tech Lead | Validates technical feasibility, consults on technical aspects |
| QA | QA Lead | Consults on testability and quality standards |

## Task-Level RACI Assignments

| ID | Task | {role_code} | PM | SPONSOR | SME | END_USER | ARCHITECT | QA |
|----|------|-----|-----|---------|-----|----------|-----------|-----|
| RACI-01 | Identify stakeholders | R | A | C | I | I | I | I |
| RACI-02 | Plan elicitation approach | R | A | I | C | I | I | I |
| RACI-03 | Conduct research & analysis | R | I | I | C | C | C | I |
| RACI-04 | Analyze current state | R | I | I | C | C | C | I |
| RACI-05 | Define deliverable structure | R | I | C | C | C | C | I |
| RACI-06 | Draft deliverables | R | I | I | C | I | I | I |
| RACI-07 | Peer review | C | R | I | C | I | C | C |
| RACI-08 | Stakeholder validation | C | C | C | C | C | C | C |
| RACI-09 | Approve / sign-off | I | I | A | I | I | I | I |
| RACI-10 | Baseline & distribute | R | A | I | I | I | I | I |
"""


def gen_sop(task, role_name, workspace_code):
    """Generate Standard Operating Procedure."""
    t = task
    return f"""# Standard Operating Procedure (SOP) — {t['task_id']} {t['name']}

## Overview

Step-by-step process from receiving the {t['name']} task to delivering complete, supervisor-approved deliverables. Each phase must complete before the next begins.

---

## Phase 0: Initialization

| Step | Action | Output |
|------|--------|--------|
| 0.1 | Create output directory `~/.openclaw/workspace-{workspace_code}/outputs/{t['task_id']}/` | Directory created |
| 0.2 | Initialize `conversation-log.md`, `work-log.md`, `question-lists.md`, `research-log.md` | Logs initialized |
| 0.3 | Check DoR prerequisites (read `references/dor.md`) | DoR status |
| 0.4 | If required items missing → request from PM | Missing items requested |
| 0.5 | Load upstream artifacts | Artifacts loaded |

---

## Phase 1: Understand Task Purpose

| Step | Action | Output |
|------|--------|--------|
| 1.1 | Receive topic/context from user or upstream artifacts | Raw topic recorded |
| 1.2 | Analyze and summarize understanding of **task purpose** | Task purpose summary |
| 1.3 | Present understanding to user and ask for confirmation | User confirmation |
| 1.4 | If user disagrees → return to 1.2 and re-analyze | Revised understanding |
| 1.5 | If user agrees → proceed to Phase 2 | Confirmed task purpose |

**Log**: Record all exchanges in conversation-log.md.

---

## Phase 2: Understand the Topic

| Step | Action | Output |
|------|--------|--------|
| 2.1 | Analyze topic in depth (who, what, why, when, where, how) | Topic analysis |
| 2.2 | Incorporate upstream findings and context | Enriched analysis |
| 2.3 | Present topic understanding to user | Topic summary |
| 2.4 | Ask user for confirmation | User confirmation |
| 2.5 | If user disagrees → return to 2.1, refine | Revised analysis |
| 2.6 | If user agrees → proceed to Phase 3 | Confirmed topic |

**Log**: Record all exchanges in conversation-log.md.

---

## Phase 3: Research & Question Generation

| Step | Action | Output |
|------|--------|--------|
| 3.1 | Research topic on internet and authoritative knowledge bases | Research findings |
| 3.2 | **Save research to `research-log.md`** (tool, query, findings, sources) | Research log entry |
| 3.3 | Analyze industry best practices, benchmarks, standards | Industry analysis |
| 3.4 | Generate structured question list based on research gaps | Question list |
| 3.5 | **Save question list to `question-lists.md`** | Question list logged |
| 3.6 | Present industry findings and questions to user | Presented findings |
| 3.7 | Conduct interactive Q&A (one at a time or small groups) | Q&A responses |
| 3.8 | Iterate until all critical information gathered | Complete Q&A |
| 3.9 | **Save each round's Q&A to `question-lists.md`** | Updated log |
| 3.10 | Consolidate into validated requirements list | Requirements list |
| 3.11 | Present requirements list to user for confirmation | User confirmation |

**Log**: Record Q&A in conversation-log.md. Record research in research-log.md.

---

## Phase 4: Execute & Produce Deliverables

| Step | Action | Output |
|------|--------|--------|
| 4.1 | Read `references/output-templates.md` | Template loaded |
| 4.2 | Read `references/dod.md` | DoD loaded |
| 4.3 | Research additional details as needed — **log to `research-log.md`** | Supplemental research |
| 4.4 | Draft all deliverable sections following template structure | Draft v0.1 |
| 4.5 | Self-review against DoD checklist | Self-review notes |
| 4.6 | Fix any issues found | Draft v1.0 |
| 4.7 | Save deliverables to output directory | Saved deliverables |

**Log**: Record all actions in work-log.md with timestamps.

---

## Phase 5: Completion & Handoff

| Step | Action | Output |
|------|--------|--------|
| 5.1 | Run DoD verification (check every criterion) | DoD report |
| 5.2 | If critical/high items fail → return to Phase 4 | Fixes applied |
| 5.3 | Repeat 5.1-5.2 until all checks pass | All checks passed |
| 5.4 | Save final deliverables | Final output |
| 5.5 | Generate completion summary | Summary |
| 5.6 | Send SupervisorTriggered to {t['skill_dir']}-supervisor | Signal sent |
| 5.7 | If supervisor returns issues → fix and re-submit | Fixes applied |
| 5.8 | Once supervisor approves (100%) → send TaskCompleted to PM | PM notified |
| 5.9 | Include deliverable path, RACI matrix, final report in payload | Handoff package |

**Log**: Record handoff actions in work-log.md.
"""


def gen_triggers(task, role_code, skill_name):
    """Generate trigger configuration."""
    t = task
    return f"""# Trigger Configuration — {t['task_id']} {t['name']}

## Primary Triggers (any one activates)

| ID | Type | Description |
|----|------|-------------|
| T-001 | TaskTriggered event | PM dispatches {t['task_id']} via event bus |
| T-002 | Upstream completion | Upstream prerequisite tasks completed |
| T-003 | User invocation | User explicitly requests {t['name'].lower()} for the project |

## Context Conditions (must be satisfied)

| ID | Description | Required |
|----|-------------|----------|
| C-001 | Task context or business problem is provided | Yes |
| C-002 | DoR prerequisites available or can be gathered interactively | Yes |
| C-003 | Upstream artifacts accessible | Yes |

## Output Signals (emitted on completion)

| ID | Target | Signal | Description |
|----|--------|--------|-------------|
| S-001 | {skill_name}-supervisor | SupervisorTriggered | Triggers supervisor review of output |
| S-002 | PM Agent | TaskCompleted | Notifies PM that {t['name']} is finalized (after supervisor approval) |

### S-002 Payload
- `deliverable_path`: Path to the final deliverable
- `raci_matrix`: RACI configuration for downstream task activation
- `final_inspection_report`: Supervisor inspection results
"""


def gen_output_templates(task, role_name):
    """Generate output templates."""
    t = task
    return f"""# Output Template — {t['task_id']} {t['name']}

Use this template as the strict structure for all {t['name']} deliverables. Every section must be populated with meaningful content. No section may be empty or contain placeholder text in the final output.

---

## Document Control

| Field | Value |
|-------|-------|
| Document Title | {{{{project_name}}}} — {t['name']} Document |
| Version | {{{{version_number}}}} |
| Date | {{{{date}}}} |
| Author | {role_name} AI Agent |
| Status | Draft / In Review / Approved |
| Reviewer(s) | {{{{reviewer_names}}}} |

### Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1 | {{{{date}}}} | {role_name} AI Agent | Initial draft |

---

## 1. Executive Summary

{{{{One-paragraph overview of the deliverable purpose, key findings, and recommendations. Write this section LAST after all other sections are complete.}}}}

---

## 2. Objectives & Scope

### 2.1 Objectives
{{{{List objectives in SMART format: Specific, Measurable, Achievable, Relevant, Time-bound.}}}}

| ID | Objective | Success Metric | Target | Timeline |
|----|-----------|---------------|--------|----------|
| OBJ-01 | {{{{objective}}}} | {{{{metric}}}} | {{{{target_value}}}} | {{{{deadline}}}} |

### 2.2 In Scope
{{{{Bulleted list of items explicitly included.}}}}

### 2.3 Out of Scope
{{{{Bulleted list of items explicitly excluded.}}}}

---

## 3. Background & Context

### 3.1 Current State
{{{{Describe existing situation and pain points.}}}}

### 3.2 Future State
{{{{Describe desired outcome.}}}}

---

## 4. Stakeholders

| ID | Name / Role | Department | Interest Level | Influence Level | RACI |
|----|------------|------------|---------------|-----------------|------|
| SH-01 | {{{{name/role}}}} | {{{{dept}}}} | High/Medium/Low | High/Medium/Low | R/A/C/I |

---

## 5. Detailed Analysis / Requirements

{{{{Core content specific to {t['name']}. Structure according to the deliverable type.}}}}

---

## 6. Assumptions

| ID | Assumption | Impact if Invalid |
|----|-----------|-------------------|
| AS-01 | {{{{assumption}}}} | {{{{impact}}}} |

---

## 7. Constraints

| ID | Type | Constraint | Impact |
|----|------|-----------|--------|
| CN-01 | Budget/Time/Technology/Regulatory | {{{{constraint}}}} | {{{{impact}}}} |

---

## 8. Dependencies

| ID | Dependency | Type | Owner | Status |
|----|-----------|------|-------|--------|
| DP-01 | {{{{dependency}}}} | Internal/External | {{{{owner}}}} | Open/Resolved |

---

## 9. Risks & Mitigation

| ID | Risk | Probability | Impact | Mitigation Strategy | Owner |
|----|------|------------|--------|---------------------|-------|
| RK-01 | {{{{risk}}}} | High/Medium/Low | High/Medium/Low | {{{{mitigation}}}} | {{{{owner}}}} |

---

## 10. Recommendations

{{{{Key recommendations based on analysis.}}}}

---

## 11. Appendices

### Appendix A: Supporting Documents
{{{{List and link any supporting documents.}}}}

---

## 12. Approval Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Sponsor | {{{{name}}}} | _________ | {{{{date}}}} |
| Project Manager | {{{{name}}}} | _________ | {{{{date}}}} |
| {role_name} | AI Agent | _________ | {{{{date}}}} |
"""


def gen_verify_dod(task):
    """Generate DoD verification script."""
    t = task
    return f'''#!/usr/bin/env python3
"""DoD Verification Script for {t['task_id']} {t['name']}.

Checks the output directory against the Definition of Done criteria.
Usage: python3 verify_dod.py <output_dir>

Exit code 0 = all critical/high checks pass, 1 = failures found.
"""

import os
import sys
import re
from pathlib import Path


def check_file_exists(path, name):
    """Check if a file exists and is non-empty."""
    if not os.path.isfile(path):
        return False, f"{{name}}: File not found at {{path}}"
    if os.path.getsize(path) == 0:
        return False, f"{{name}}: File is empty at {{path}}"
    return True, f"{{name}}: OK"


def check_no_todos(path, name):
    """Check that file has no unresolved TBD/TODO placeholders."""
    if not os.path.isfile(path):
        return False, f"{{name}}: File not found"
    content = Path(path).read_text(encoding="utf-8")
    todos = re.findall(r'\\b(TBD|TODO|FIXME|XXX)\\b', content, re.IGNORECASE)
    if todos:
        return False, f"{{name}}: Found {{len(todos)}} unresolved placeholders: {{todos[:5]}}"
    return True, f"{{name}}: No unresolved placeholders"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify_dod.py <output_dir>")
        sys.exit(1)

    output_dir = sys.argv[1]
    if not os.path.isdir(output_dir):
        print(f"Error: Output directory not found: {{output_dir}}")
        sys.exit(1)

    results = []
    failures = 0

    # Process quality: Check required logs exist
    logs = [
        ("conversation-log.md", "DOD-P04"),
        ("work-log.md", "DOD-P05"),
        ("question-lists.md", "DOD-P06"),
        ("research-log.md", "DOD-P07"),
    ]
    for log_file, dod_id in logs:
        passed, msg = check_file_exists(os.path.join(output_dir, log_file), f"{{dod_id}} {{log_file}}")
        results.append((dod_id, "High", passed, msg))
        if not passed:
            failures += 1

    # Find deliverable files
    log_names = {{l[0] for l in logs}}
    deliverable_files = [
        f for f in os.listdir(output_dir)
        if f.endswith(".md") and f not in log_names
    ]

    if not deliverable_files:
        results.append(("DOD-C01", "Critical", False, "No deliverable found in output directory"))
        failures += 1
    else:
        deliverable_path = os.path.join(output_dir, deliverable_files[0])

        # Document quality: No unresolved TBDs
        passed, msg = check_no_todos(deliverable_path, "DOD-D05")
        results.append(("DOD-D05", "Critical", passed, msg))
        if not passed:
            failures += 1

    # Print results
    print("=" * 60)
    print("DoD Verification Report — {t['task_id']} {t['name']}")
    print("=" * 60)
    print(f"Output directory: {{output_dir}}")
    print()
    print(f"{{\\'ID\\':<10}} {{\\'Severity\\':<10}} {{\\'Status\\':<8}} {{\\'Details\\'}}")
    print("-" * 60)
    for dod_id, severity, passed, msg in results:
        status = "PASS" if passed else "FAIL"
        print(f"{{dod_id:<10}} {{severity:<10}} {{status:<8}} {{msg}}")

    print()
    total = len(results)
    passed_count = total - failures
    print(f"Result: {{passed_count}}/{{total}} checks passed ({{failures}} failures)")

    if failures > 0:
        print("\\nSTATUS: FAIL — Fix the above issues and re-run verification.")
        sys.exit(1)
    else:
        print("\\nSTATUS: PASS — All automated DoD checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
'''


def gen_inspection_criteria(task, role_name, role_code):
    """Generate inspection criteria for supervisor."""
    t = task
    return f"""# Inspection Criteria — {t['task_id']} {t['name']} Supervisor

Detailed verification rules for each inspection item. The supervisor must check every item below.

---

## Infrastructure Checks

### INS-01: Triggers Configuration
- **Verify**: `references/triggers.md` exists in the skill directory
- **Content**: Contains primary triggers, context conditions, and output signals
- **Severity**: Critical

### INS-02: RACI Matrix Configuration
- **Verify**: `references/raci.md` exists with role definitions AND task-level RACI assignments
- **Content**: At least 7 roles defined, at least 10 task assignments with R/A/C/I values
- **Severity**: Critical

### INS-03: Output Template
- **Verify**: `references/output-templates.md` exists with deliverable template
- **Content**: Document Control, Executive Summary, Objectives, Stakeholders, and core sections present
- **Severity**: Critical

### INS-04: SOP Process
- **Verify**: `references/sop.md` exists with Phase 0 through Phase 5 defined
- **Content**: Each phase has step-by-step actions with expected outputs
- **Severity**: Critical

### INS-05: DoD Checklist
- **Verify**: `references/dod.md` exists with completeness, deliverable quality, process quality categories
- **Content**: At least 20 check items with severity levels
- **Severity**: Critical

### INS-06: DoR Checklist
- **Verify**: `references/dor.md` exists with prerequisite entries
- **Content**: Each entry has required/optional flag and fallback strategy
- **Severity**: Critical

---

## Process Checks

### INS-07: Conversation Log
- **Verify**: `conversation-log.md` exists in output directory
- **Content**: Entries are numbered, each has timestamp and agent/user labels
- **Format**: `### Question #N — {{timestamp}}` followed by `**Agent**:` and `**User**:` lines
- **Severity**: Critical

### INS-08: Work Log
- **Verify**: `work-log.md` exists in output directory
- **Content**: Entries have timestamps and status indicators (completed/in-progress/failed)
- **Format**: `- [{{timestamp}}] {{action}} — Status: {{status}}`
- **Severity**: Critical

### INS-09: DoD Verification Passed
- **Verify**: Evidence that DoD self-check was performed
- **Content**: All critical severity items show as passed; high severity items show as passed
- **Severity**: Critical

### INS-10: Question Lists Log
- **Verify**: `question-lists.md` exists in output directory
- **Content**: Phase-labeled sections, numbered question entries, answered summaries
- **Format**: `## Phase {{N}}: {{name}} — {{timestamp}}` + `### Question List #{{seq}}` + `### Answered Summary`
- **Severity**: Critical

### INS-11: Research Log
- **Verify**: `research-log.md` exists in output directory
- **Content**: Sequentially numbered entries, each with Tool, Query/URL, Purpose, Key Findings, Source
- **Format**: `## Research #{{seq}} — {{timestamp}}` with structured fields
- **Severity**: Critical

### INS-12: User Confirmation
- **Verify**: Conversation log shows explicit user confirmation for:
  1. Task purpose understanding (Phase 1)
  2. Topic understanding (Phase 2)
  3. Requirements/deliverable validation (Phase 3)
- **Severity**: Critical

---

## Deliverable Quality Checks

### INS-DQ-01: Deliverable Complete
- **Verify**: All required sections from output template are present and populated
- **Content**: No empty sections or placeholder-only content
- **Severity**: Critical

### INS-DQ-02: No Unresolved TBDs
- **Verify**: Search entire deliverable for TBD, TODO, FIXME, XXX markers
- **Content**: Zero matches found
- **Severity**: Critical

### INS-DQ-03: Template Followed
- **Verify**: Deliverable structure matches output-templates.md format
- **Content**: All required sections in correct order
- **Severity**: High

### INS-DQ-04: Acceptance Criteria
- **Verify**: All requirements/deliverables have testable acceptance criteria
- **Content**: Criteria are measurable and specific
- **Severity**: High

### INS-DQ-05: Upstream Traceability
- **Verify**: Upstream inputs are referenced and decisions traceable to requirements
- **Content**: Clear linkage between inputs and outputs
- **Severity**: High
"""


# ═══════════════════════════════════════════════════════════════
# FILE CREATION FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def write_file(path, content):
    """Write content to a file, creating directories as needed."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def create_skill(task, role_name, role_code, workspace_code, base_dir, skip_existing=False):
    """Create a complete skill directory with all files."""
    skill_dir = base_dir / task["skill_dir"]
    sup_dir = base_dir / f"{task['skill_dir']}-supervisor"

    if skip_existing and (skill_dir / "SKILL.md").exists():
        return 0

    count = 0

    # Main skill
    write_file(skill_dir / "SKILL.md", gen_skill_md(task, role_name, role_code, workspace_code))
    count += 1
    write_file(skill_dir / "references" / "dor.md", gen_dor(task, role_name, workspace_code))
    count += 1
    write_file(skill_dir / "references" / "dod.md", gen_dod(task, role_name))
    count += 1
    write_file(skill_dir / "references" / "raci.md", gen_raci(task, role_name, role_code))
    count += 1
    write_file(skill_dir / "references" / "sop.md", gen_sop(task, role_name, workspace_code))
    count += 1
    write_file(skill_dir / "references" / "triggers.md", gen_triggers(task, role_code, task["skill_dir"]))
    count += 1
    write_file(skill_dir / "references" / "output-templates.md", gen_output_templates(task, role_name))
    count += 1
    write_file(skill_dir / "scripts" / "verify_dod.py", gen_verify_dod(task))
    count += 1

    # Supervisor
    write_file(sup_dir / "SKILL.md", gen_supervisor_md(task, role_name, role_code))
    count += 1
    write_file(sup_dir / "references" / "inspection-criteria.md", gen_inspection_criteria(task, role_name, role_code))
    count += 1

    return count


def create_tasks_index(tasks, role_name, agent_name):
    """Generate tasks-index.json content."""
    task_entries = []
    for t in tasks:
        entry = {
            "task_id": t["task_id"],
            "name": t["name"],
            "phase": t["phase"],
            "wave": t["wave"],
            "step": t["step"],
            "next": t["next"],
            "skill_dir": t["skill_dir"],
            "supervisor_dir": f"{t['skill_dir']}-supervisor",
            "description": t["description"]
        }
        task_entries.append(entry)

    return json.dumps({
        "metadata": {
            "role": role_name,
            "agent": agent_name,
            "source": "task/delivery_playbook.md",
            "generated_at": TODAY
        },
        "tasks": task_entries
    }, indent=2)


def create_state_json():
    """Generate initial state.json."""
    return json.dumps({"tasks": {}, "last_updated": TODAY}, indent=2)


def create_agent_bootstrap(role_name, role_code, emoji):
    """Generate bootstrap files for an agent workspace."""
    agents_md = f"""# AGENTS.md — {role_name} Agent Workspace

## Agent Identity

| Field | Value |
|:---|:---|
| Role | {role_name} |
| Type | {"Orchestrator" if role_code == "PM" else "Role Agent"} |
| Status | Active |

## Operating Instructions

1. Listen for TaskTriggered events from PM Agent
2. Check DoR prerequisites before starting
3. Execute skill Phase 0-5 in strict order
4. Self-check against DoD criteria
5. Invoke supervisor for independent quality review
6. Report TaskCompleted to PM Agent (only after supervisor 100% pass)

## Mandatory Rules

- No phase may be skipped
- All DoD quality gates must pass
- Supervisor must achieve 100% pass rate
- All actions logged in work-log.md and conversation-log.md
"""

    soul_md = f"""# SOUL.md — {role_name} Agent Persona

You are a {role_name} agent in an OpenClaw multi-agent team.

## Boundaries

- PM is your sole orchestrator. Only act on TaskTriggered events from PM.
- Follow your skill instructions exactly. No phase skipping.
- Always run self-check and supervisor before reporting TaskCompleted.
- Maintain professional, precise communication.
- Document all decisions with rationale.
- When uncertain, research first, then ask the user.

## Communication Style

- Clear, structured, and actionable
- Use tables and lists for clarity
- Cite sources for all research findings
- Present options with trade-offs when multiple approaches exist
"""

    identity_md = f"""# IDENTITY.md — {role_name} Agent

- **Name**: {role_name} Agent
- **Emoji**: {emoji}
- **Role**: {role_name}
- **Team**: OpenClaw AI Agent Team
"""

    user_md = f"""# USER.md — Team Context

## Team Structure

- **PM Agent**: Project Manager (Orchestrator)
- **IPM Agent**: IT Product Manager (Role Agent)
- **SA Agent**: System Architect (Role Agent)
- **TL Agent**: Technical Lead (Role Agent)

## Communication Protocol

- All task assignments flow from PM Agent
- All task completions report to PM Agent
- Supervisor reviews are independent quality gates
"""

    tools_md = f"""# TOOLS.md — Tool Usage Conventions

## File Operations

- Use Read tool for file access (not cat/head/tail)
- Use Edit tool for modifications (not sed/awk)
- Use Write tool for new files (not echo/cat heredoc)
- Use Glob for file search (not find/ls)
- Use Grep for content search (not grep/rg)

## Git Conventions

- Commit after each completed phase
- Use descriptive commit messages referencing task ID
- Never force push or amend published commits

## External APIs

- Log all external API calls in research-log.md
- Cache research results to avoid redundant calls
- Cite sources for all findings
"""

    return agents_md, soul_md, identity_md, user_md, tools_md


# ═══════════════════════════════════════════════════════════════
# PHASE 0: SHARED INFRASTRUCTURE
# ═══════════════════════════════════════════════════════════════

def create_phase0():
    """Create shared workspace infrastructure."""
    print("\n=== PHASE 0: Shared Workspace Infrastructure ===\n")
    count = 0
    config_dir = WORKSPACE / "config"

    # agents-registry.json
    registry = {
        "metadata": {"version": "1.0", "generated_at": TODAY},
        "agents": [
            {
                "role_code": "PM",
                "role_full_name": "IT Project Manager",
                "description": "Sole orchestrator; broadcasts tasks, collects completions, re-broadcasts for supervisor QA",
                "type": "Orchestrator",
                "task_prefix": "PM",
                "agent_id": "pm-agent",
                "workspace": "~/.openclaw/workspace-pm",
                "skill_dirs": [t["skill_dir"] for t in PM_TASKS],
                "playbook_role": "Project Manager",
                "model": "claude-opus-4-6",
                "status": "active",
                "instances": 1,
                "created_at": TODAY,
                "updated_at": TODAY
            },
            {
                "role_code": "IPM",
                "role_full_name": "IT Product Manager",
                "description": "Manages product requirements, BRDs, PRDs, and product lifecycle across all phases",
                "type": "Role Agent",
                "task_prefix": "IPM",
                "agent_id": "ipm-agent",
                "workspace": "~/.openclaw/workspace-ipm",
                "skill_dirs": [t["skill_dir"] for t in IPM_TASKS],
                "playbook_role": "IT Product Manager",
                "model": "claude-opus-4-6",
                "status": "active",
                "instances": 1,
                "created_at": TODAY,
                "updated_at": TODAY
            },
            {
                "role_code": "SA",
                "role_full_name": "System Architect",
                "description": "Executes system architecture tasks across Inception, Requirements, Development, QA, Release phases",
                "type": "Role Agent",
                "task_prefix": "IA",
                "agent_id": "sa-agent",
                "workspace": "~/.openclaw/workspace-sa",
                "skill_dirs": [t["skill_dir"] for t in SA_INCOMPLETE_TASKS],  # will merge with existing
                "playbook_role": "IT Architect",
                "model": "claude-opus-4-6",
                "status": "active",
                "instances": 1,
                "created_at": TODAY,
                "updated_at": TODAY
            },
            {
                "role_code": "TL",
                "role_full_name": "Technical Lead",
                "description": "Executes technical leadership tasks across all phases (to be completed separately)",
                "type": "Role Agent",
                "task_prefix": "TL",
                "agent_id": "tl-agent",
                "workspace": "~/.openclaw/workspace-tl",
                "skill_dirs": [],
                "playbook_role": "Technical Lead",
                "model": "claude-opus-4-6",
                "status": "active",
                "instances": 1,
                "created_at": TODAY,
                "updated_at": TODAY
            }
        ]
    }
    write_file(config_dir / "agents-registry.json", json.dumps(registry, indent=2))
    count += 1
    print(f"  Created config/agents-registry.json")

    # openclaw.json
    all_skill_entries = {}
    for t in PM_TASKS + IPM_TASKS:
        all_skill_entries[t["skill_dir"]] = {"enabled": True}
        all_skill_entries[f"{t['skill_dir']}-supervisor"] = {"enabled": True}
    # SA skills (all from tasks-index)
    for t in SA_INCOMPLETE_TASKS:
        all_skill_entries[t["skill_dir"]] = {"enabled": True}
        all_skill_entries[f"{t['skill_dir']}-supervisor"] = {"enabled": True}

    openclaw = {
        "agents": {
            "defaults": {
                "workspace": "~/.openclaw/workspace",
                "model": "claude-opus-4-6"
            },
            "list": [
                {
                    "id": "pm-agent",
                    "workspace": "~/.openclaw/workspace-pm",
                    "model": "claude-opus-4-6",
                    "tools": {"profile": "full"}
                },
                {
                    "id": "ipm-agent",
                    "workspace": "~/.openclaw/workspace-ipm",
                    "model": "claude-opus-4-6",
                    "tools": {"profile": "coding", "allow": ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]}
                },
                {
                    "id": "sa-agent",
                    "workspace": "~/.openclaw/workspace-sa",
                    "model": "claude-opus-4-6",
                    "tools": {"profile": "coding", "allow": ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]}
                },
                {
                    "id": "tl-agent",
                    "workspace": "~/.openclaw/workspace-tl",
                    "model": "claude-opus-4-6",
                    "tools": {"profile": "coding", "allow": ["Read", "Write", "Edit", "Glob", "Grep", "Bash"]}
                }
            ]
        },
        "skills": {
            "load": {
                "extraDirs": ["~/.openclaw/workspace/skills"],
                "watch": True
            },
            "entries": all_skill_entries
        },
        "bindings": [
            {"agentId": "pm-agent", "match": {"channel": "event-bus", "topic": "orchestrator"}},
            {"agentId": "ipm-agent", "match": {"channel": "event-bus", "topic": "pm-ipm"}},
            {"agentId": "sa-agent", "match": {"channel": "event-bus", "topic": "pm-sa"}},
            {"agentId": "tl-agent", "match": {"channel": "event-bus", "topic": "pm-tl"}}
        ]
    }
    write_file(config_dir / "openclaw.json", json.dumps(openclaw, indent=2))
    count += 1
    print(f"  Created config/openclaw.json")

    # event-bus.json
    event_bus = {
        "metadata": {"version": "1.0", "generated_at": TODAY},
        "routes": [
            {"event": "TaskTriggered", "from": "pm-agent", "to": ["ipm-agent", "sa-agent", "tl-agent"], "description": "PM broadcasts task assignments to role agents"},
            {"event": "TaskCompleted", "from": ["ipm-agent", "sa-agent", "tl-agent"], "to": "pm-agent", "description": "Role agents report task completion to PM"},
            {"event": "SupervisorTriggered", "from": ["ipm-agent", "sa-agent", "tl-agent"], "to": "supervisor", "description": "Role agents invoke their supervisors"},
            {"event": "SupervisorCompleted", "from": "supervisor", "to": ["ipm-agent", "sa-agent", "tl-agent"], "description": "Supervisors return inspection results"}
        ],
        "rules": [
            {"name": "wave-ordering", "description": "Complete all tasks in Wave N before triggering Wave N+1"},
            {"name": "parallel-fanout", "description": "Tasks within same wave can execute in parallel"},
            {"name": "supervisor-gate", "description": "TaskCompleted requires 100% supervisor pass rate"}
        ]
    }
    write_file(config_dir / "event-bus.json", json.dumps(event_bus, indent=2))
    count += 1
    print(f"  Created config/event-bus.json")

    # Bootstrap files
    soul_md = """# SOUL.md — OpenClaw Team Persona

## Team Identity

This is an OpenClaw multi-agent team for IT project delivery. Each agent has a specific role and follows strict quality processes.

## Boundaries

- PM is the sole orchestrator. No role agent may bypass PM.
- Every task follows Phase 0-5 workflow. No phases may be skipped.
- Self-check + supervisor must both pass before TaskCompleted.
- All decisions documented with rationale.
- Research-backed recommendations only.

## Communication Style

- Professional, structured, and actionable
- Use tables and lists for clarity
- Cite sources for research findings
- Present options with trade-offs
"""
    write_file(WORKSPACE / "SOUL.md", soul_md)
    count += 1
    print(f"  Created SOUL.md")

    identity_md = """# IDENTITY.md — OpenClaw Team

- **Team Name**: OpenClaw AI Agent Team
- **Purpose**: End-to-end IT project delivery through specialized AI agents
- **Agents**:
  - PM Agent — Project Manager (Orchestrator)
  - IPM Agent — IT Product Manager (Role Agent)
  - SA Agent — System Architect (Role Agent)
  - TL Agent — Technical Lead (Role Agent)
"""
    write_file(WORKSPACE / "IDENTITY.md", identity_md)
    count += 1
    print(f"  Created IDENTITY.md")

    user_md = """# USER.md — User Context

## Team Operator

The user acts as the team operator, providing:
- Project context and business requirements
- Stakeholder information
- Decision inputs when agents need clarification
- Approval for key deliverables

## Interaction Protocol

- Agents ask targeted questions through structured Q&A
- User confirms understanding at Phase 1 and Phase 2
- User validates requirements at Phase 3
- User reviews final deliverables at Phase 5
"""
    write_file(WORKSPACE / "USER.md", user_md)
    count += 1
    print(f"  Created USER.md")

    tools_md = """# TOOLS.md — Tool Usage Conventions

## File Operations

- Use Read tool for file access (not cat/head/tail)
- Use Edit tool for modifications (not sed/awk)
- Use Write tool for new files (not echo/cat heredoc)
- Use Glob for file search (not find/ls)
- Use Grep for content search (not grep/rg)

## Git Conventions

- Commit after each completed skill batch
- Use descriptive commit messages referencing task IDs
- Never force push or amend published commits

## Research Tools

- WebSearch for current information
- WebFetch for specific URLs
- Context7 for library documentation
- Log all research in research-log.md
"""
    write_file(WORKSPACE / "TOOLS.md", tools_md)
    count += 1
    print(f"  Created TOOLS.md")

    print(f"\n  Phase 0 complete: {count} files created")
    return count


# ═══════════════════════════════════════════════════════════════
# PHASE 1: PM AGENT
# ═══════════════════════════════════════════════════════════════

def create_phase1():
    """Create PM Agent skills."""
    print("\n=== PHASE 1: PM Agent — 24 skills + 24 supervisors ===\n")
    count = 0
    pm_ws = Path.home() / ".openclaw" / "workspace-pm"

    # Agent config
    write_file(pm_ws / "config" / "tasks-index.json", create_tasks_index(PM_TASKS, "IT Project Manager", "PM Agent"))
    count += 1
    print(f"  Created workspace-pm/config/tasks-index.json")

    write_file(pm_ws / "config" / "state.json", create_state_json())
    count += 1
    print(f"  Created workspace-pm/config/state.json")

    # Bootstrap files
    agents_md, soul_md, identity_md, user_md, tools_md = create_agent_bootstrap(
        "IT Project Manager", "PM", "📊"
    )
    write_file(pm_ws / "AGENTS.md", agents_md)
    write_file(pm_ws / "SOUL.md", soul_md)
    write_file(pm_ws / "IDENTITY.md", identity_md)
    write_file(pm_ws / "USER.md", user_md)
    write_file(pm_ws / "TOOLS.md", tools_md)
    count += 5
    print(f"  Created PM bootstrap files (AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md)")

    # Skills
    for i, task in enumerate(PM_TASKS):
        n = create_skill(task, "IT Project Manager", "PM", "pm", WORKSPACE)
        count += n
        print(f"  [{i+1}/{len(PM_TASKS)}] Created {task['skill_dir']} + supervisor ({n} files)")

    print(f"\n  Phase 1 complete: {count} files created")
    return count


# ═══════════════════════════════════════════════════════════════
# PHASE 2: IPM AGENT
# ═══════════════════════════════════════════════════════════════

def create_phase2():
    """Create IPM Agent skills (skip ipm-brd-writing which already exists)."""
    print("\n=== PHASE 2: IPM Agent — 20 new skills + supervisors ===\n")
    count = 0
    ipm_ws = Path.home() / ".openclaw" / "workspace-ipm"

    # Agent config
    write_file(ipm_ws / "config" / "tasks-index.json", create_tasks_index(IPM_TASKS, "IT Product Manager", "IPM Agent"))
    count += 1
    print(f"  Created workspace-ipm/config/tasks-index.json")

    write_file(ipm_ws / "config" / "state.json", create_state_json())
    count += 1
    print(f"  Created workspace-ipm/config/state.json")

    # Bootstrap files
    agents_md, soul_md, identity_md, user_md, tools_md = create_agent_bootstrap(
        "IT Product Manager", "IPM", "📋"
    )
    write_file(ipm_ws / "AGENTS.md", agents_md)
    write_file(ipm_ws / "SOUL.md", soul_md)
    write_file(ipm_ws / "IDENTITY.md", identity_md)
    write_file(ipm_ws / "USER.md", user_md)
    write_file(ipm_ws / "TOOLS.md", tools_md)
    count += 5
    print(f"  Created IPM bootstrap files")

    # Skills (skip ipm-brd-writing which already exists)
    for i, task in enumerate(IPM_TASKS):
        n = create_skill(task, "IT Product Manager", "IPM", "ipm", WORKSPACE, skip_existing=True)
        count += n
        if n > 0:
            print(f"  [{i+1}/{len(IPM_TASKS)}] Created {task['skill_dir']} + supervisor ({n} files)")
        else:
            print(f"  [{i+1}/{len(IPM_TASKS)}] Skipped {task['skill_dir']} (already exists)")

    print(f"\n  Phase 2 complete: {count} files created")
    return count


# ═══════════════════════════════════════════════════════════════
# PHASE 3: SA AGENT COMPLETION
# ═══════════════════════════════════════════════════════════════

def create_phase3():
    """Complete SA Agent missing skills."""
    print("\n=== PHASE 3: SA Agent — Complete missing skills + supervisors ===\n")
    count = 0
    sa_ws = Path.home() / ".openclaw" / "workspace-sa"

    # Bootstrap files for SA workspace (if not exists)
    if not (sa_ws / "AGENTS.md").exists():
        agents_md, soul_md, identity_md, user_md, tools_md = create_agent_bootstrap(
            "System Architect", "SA", "🏗️"
        )
        write_file(sa_ws / "AGENTS.md", agents_md)
        write_file(sa_ws / "SOUL.md", soul_md)
        write_file(sa_ws / "IDENTITY.md", identity_md)
        write_file(sa_ws / "USER.md", user_md)
        write_file(sa_ws / "TOOLS.md", tools_md)
        count += 5
        print(f"  Created SA bootstrap files")

    # Complete incomplete skills
    for i, task in enumerate(SA_INCOMPLETE_TASKS):
        skill_dir = WORKSPACE / task["skill_dir"]
        # Check if SKILL.md exists (it shouldn't for incomplete skills)
        if (skill_dir / "SKILL.md").exists():
            print(f"  [{i+1}/{len(SA_INCOMPLETE_TASKS)}] Skipped {task['skill_dir']} (already complete)")
            continue
        n = create_skill(task, "System Architect", "SA", "sa", WORKSPACE)
        count += n
        print(f"  [{i+1}/{len(SA_INCOMPLETE_TASKS)}] Created {task['skill_dir']} + supervisor ({n} files)")

    # Missing supervisors (main exists, supervisor empty)
    for skill_name in SA_MISSING_SUPERVISORS:
        sup_dir = WORKSPACE / f"{skill_name}-supervisor"
        if (sup_dir / "SKILL.md").exists():
            print(f"  Skipped {skill_name}-supervisor (already exists)")
            continue
        # Find matching task from SA tasks-index
        matching = [t for t in SA_INCOMPLETE_TASKS if t["skill_dir"] == skill_name]
        if not matching:
            # Need to look in existing tasks (dr-bcp-architecture = IA-REQ-007, technical-debt = IA-DEV-004)
            if skill_name == "sa-dr-bcp-architecture":
                task = {"task_id": "IA-REQ-007", "name": "DR/BCP Architecture", "phase": "Requirements", "wave": 10, "step": 7,
                        "skill_dir": "sa-dr-bcp-architecture", "next": ["TL-REQ-001", "TL-REQ-002", "TL-REQ-003", "TL-REQ-004", "TL-REQ-005"],
                        "description": "Designing disaster recovery and business continuity posture (RPO/RTO targets, failover topology)."}
            else:
                task = {"task_id": "IA-DEV-004", "name": "Technical Debt Management", "phase": "Development", "wave": 10, "step": 4,
                        "skill_dir": "sa-technical-debt-management", "next": ["TL-DEV-001", "TL-DEV-002", "TL-DEV-003", "TL-DEV-004", "TL-DEV-005"],
                        "description": "Tracking and prioritizing technical debt; proposing remediation strategies."}
        else:
            task = matching[0]

        write_file(sup_dir / "SKILL.md", gen_supervisor_md(task, "System Architect", "SA"))
        write_file(sup_dir / "references" / "inspection-criteria.md", gen_inspection_criteria(task, "System Architect", "SA"))
        count += 2
        print(f"  Created {skill_name}-supervisor (2 files)")

    print(f"\n  Phase 3 complete: {count} files created")
    return count


# ═══════════════════════════════════════════════════════════════
# PHASE 4: UPDATE AGENTS.MD
# ═══════════════════════════════════════════════════════════════

def update_agents_md():
    """Update AGENTS.md to include IPM row."""
    agents_path = WORKSPACE / "AGENTS.md"
    content = agents_path.read_text(encoding="utf-8")

    # Check if IPM is already in the file
    if "IPM Agent" in content:
        print("  AGENTS.md already contains IPM row")
        return 0

    # Add IPM row after SA row
    old = "| SA Agent | IT Architect | Role Agent | Executes system architecture tasks across Inception, Requirements, Development, QA, Release phases |"
    new = old + "\n| IPM Agent | IT Product Manager | Role Agent | Manages product requirements, BRDs, PRDs, and product lifecycle across Inception, Requirements, Development, QA, Release phases |"

    content = content.replace(old, new)
    agents_path.write_text(content, encoding="utf-8")
    print("  Updated AGENTS.md with IPM row")
    return 1


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    print("=" * 70)
    print("  OpenClaw Team Generator")
    print("=" * 70)

    total = 0

    total += create_phase0()
    update_agents_md()
    total += create_phase1()
    total += create_phase2()
    total += create_phase3()

    print("\n" + "=" * 70)
    print(f"  TOTAL FILES CREATED: {total}")
    print("=" * 70)

    # Summary
    print("\n  Next steps:")
    print("  1. Run quick_validate.py on each skill directory")
    print("  2. Update config/agents-registry.json with final SA skill_dirs")
    print("  3. Verify all tasks-index.json next references")
    print("  4. Git commit")


if __name__ == "__main__":
    main()
