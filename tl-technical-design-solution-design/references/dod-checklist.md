# Definition of Done (DoD) Quality Gates Checklist

## Role: Technical Lead (TL) — Technical Design & Solution Design Agent

## DoD Checklist

### A. Document Completeness

| # | Quality Gate | Verification Method | Pass Criteria |
|:--|:--|:--|:--|
| D1 | **All 15 document sections present** | Check technical design document structure | All sections (Front Matter through Glossary) exist and contain content |
| D2 | **Front Matter is complete** | Check version, status, author, date, reviewers | All front matter fields are populated |
| D3 | **Goals and Non-Goals defined** | Check Section 3 | At least 2 goals and 2 non-goals explicitly stated |
| D4 | **Requirements summarized** | Check Section 4 | Both functional and non-functional requirements listed with priorities |
| D5 | **Constraints documented** | Check Section 4.3 | At least 1 technical, 1 business, or 1 organizational constraint listed |

### B. Diagram Quality

| # | Quality Gate | Verification Method | Pass Criteria |
|:--|:--|:--|:--|
| D6 | **C4 Level 1 (Context) diagram present** | Check Section 5.1 | Valid Mermaid C4Context diagram with persons, systems, and relationships |
| D7 | **C4 Level 2 (Container) diagram present** | Check Section 5.2 | Valid Mermaid C4Container diagram showing all major containers |
| D8 | **C4 Level 3 (Component) diagrams present** | Check Section 6 | At least 1 component diagram for the most critical container |
| D9 | **Sequence diagrams present** | Check Section 7 | At least 1 happy path and 1 error path sequence diagram |
| D10 | **ER diagram present** | Check Section 8 | Valid Mermaid ER diagram showing key entities and relationships |
| D11 | **Diagrams use Mermaid syntax** | Check all diagram code blocks | All diagrams are in valid Mermaid (or PlantUML as secondary) |
| D12 | **Diagram consistency** | Cross-reference diagrams | Entities/components in sequence diagrams match those in component/container diagrams |

### C. Design Quality

| # | Quality Gate | Verification Method | Pass Criteria |
|:--|:--|:--|:--|
| D13 | **API specifications defined** | Check Section 9 | At least 1 API endpoint with request/response format and error handling |
| D14 | **Cross-cutting concerns addressed** | Check Section 10 | Security, error handling, logging/observability, and caching addressed |
| D15 | **Deployment architecture defined** | Check Section 11 | Scaling strategy and deployment approach documented |
| D16 | **Alternatives considered (ADR)** | Check Section 12 | At least 1 ADR with options, pros/cons, decision, and consequences |
| D17 | **Risks identified** | Check Section 13 | At least 2 risks with probability, impact, and mitigation strategy |
| D18 | **Testing strategy defined** | Check Section 14 | Unit, integration, and performance testing approaches specified |

### D. Architectural Quality Attributes

| # | Quality Gate | Verification Method | Pass Criteria |
|:--|:--|:--|:--|
| D19 | **Scalability addressed** | Review design for scaling patterns | Design explicitly addresses horizontal/vertical scaling approach |
| D20 | **Resiliency addressed** | Review design for fault tolerance | At least 1 resilience pattern documented (retry, circuit breaker, fallback) |
| D21 | **Modularity verified** | Review component boundaries | Components have clear boundaries, single responsibilities, and loose coupling |
| D22 | **Simplicity verified** | Review overall design complexity | Design uses no more than necessary components; no over-engineering |
| D23 | **Observability addressed** | Review logging/monitoring design | Structured logging, metrics, and tracing strategy documented |

### E. Process Compliance

| # | Quality Gate | Verification Method | Pass Criteria |
|:--|:--|:--|:--|
| D24 | **Conversation log exists** | Check `conversation-log.md` | All user interactions logged question-by-question |
| D25 | **Work log exists** | Check `work-log.md` | All activities logged entry-by-entry on timeline |
| D26 | **Question lists recorded** | Check `question-lists.md` | All questions from each phase recorded |
| D27 | **Research results saved** | Check `research-results.md` | Research process and results documented |
| D28 | **DoD verification report generated** | Check `dod-verification-report.md` | Self-verification results documented |
| D29 | **arc42 structure followed** | Review document structure | Document follows arc42 template conventions |

### F. Implementability

| # | Quality Gate | Verification Method | Pass Criteria |
|:--|:--|:--|:--|
| D30 | **Design is implementable** | Review feasibility | A developer unfamiliar with the project can understand and implement from this document alone |
| D31 | **Technology choices are justified** | Review technology stack section | Each technology choice has a rationale documented |
| D32 | **No contradictions** | Cross-reference all sections | No conflicting statements between sections |
| D33 | **Glossary populated** | Check Section 15 | All domain-specific terms and acronyms defined |

---

## Scoring

- **Total Items**: 33
- **Pass Threshold**: 100% (33/33)
- **Any FAIL item** → must be remediated before submission to Supervisor

## Verification Process

1. Load this checklist
2. For each item, verify against the produced outputs
3. Record PASS/FAIL with evidence (file path, section reference)
4. Generate DoD Verification Report
5. If any item fails → fix and re-verify
6. Repeat until 100% pass rate

## Configuration Notes

- Add new quality gates by appending rows to the appropriate section
- Quality gates can be adjusted per project requirements
- Minimum pass threshold is always 100% — no items can be skipped
