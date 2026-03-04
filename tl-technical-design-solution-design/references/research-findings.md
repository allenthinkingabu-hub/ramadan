# Research Findings — Skill Creation Phase

## Research Session: Industry Best Practices for Technical Design & Solution Design
- **Date**: 2026-03-03
- **Phase**: Skill Creation — Step 3

### Sources Consulted

| # | Source | Key Finding |
|:--|:--|:--|
| 1 | IEEE 1016-2009 Standard | Formal SDD standard; view/viewpoint/stakeholder model; medium-agnostic |
| 2 | arc42 Template (Starke & Hruschka) | 12-section open-source template; flexible, tool-agnostic, order-flexible |
| 3 | C4 Model (Simon Brown) | 4 hierarchical zoom levels; 5 basic elements; notation-agnostic |
| 4 | ISO/IEC/IEEE 42010:2022 | Architecture description framework for regulated industries |
| 5 | 4+1 View Model | 5 concurrent views for large enterprise; Logical, Development, Process, Physical, Scenarios |
| 6 | Pragmatic Engineer (RFC Process) | RFC is dominant design review process; used at Google, Spotify, Uber |
| 7 | Spotify Engineering (ADRs) | ADRs embedded in culture; stored in code repos alongside code |
| 8 | CMU SEI (ATAM) | Architecture Tradeoff Analysis Method for critical systems |
| 9 | GitHub Well-Architected | Quality attributes: scalability, resiliency, efficiency, modularity, simplicity, observability, interoperability |
| 10 | Mermaid vs PlantUML comparisons | Mermaid: GitHub-native, LLM-friendly, growing adoption; PlantUML: more features, Java dependency |
| 11 | C4 Model practical tips | L1+L2 provide most value; L3 selectively; L4 auto-generate; don't model external system internals |
| 12 | Sequence diagram best practices | 70-80% key interactions; use combined fragments; chronological order; descriptive naming |

### Key Decisions Made

| Decision | Choice | Rationale |
|:--|:--|:--|
| Document Framework | arc42 + C4 | Most widely adopted hybrid; flexible, extensible |
| Primary Diagram Tool | Mermaid | GitHub-native, LLM-friendly, no runtime dependency |
| Secondary Diagram Tool | PlantUML | Advanced C4 support, complex layouts |
| Document Sections | 15 sections | Comprehensive coverage from cross-referencing IEEE 1016, arc42, Google Design Docs |
| Quality Review Model | DoD + Architectural Quality Attributes | Comprehensive quality assurance |
| Interaction Style | Phased (understand → research → design → validate) | Matches spec's Step 1-4 flow |
| Output Language | English | Consistent with project conventions |

### Anti-Patterns Identified (to Avoid)

1. Big Design Up Front (BDUF) — avoid excessive upfront design without feedback
2. Golden Hammer — avoid applying favorite tech to every problem
3. Over-Engineering — avoid excessive patterns for simple problems
4. Missing ADR integration — always document the "why" behind decisions
5. No diagram legends — every diagram must include context
6. Write-Once-Read-Never — design documents must be living artifacts
7. Showing internal details of external systems — focus on boundaries
8. Mixing decision process with architecture outcomes in diagrams
