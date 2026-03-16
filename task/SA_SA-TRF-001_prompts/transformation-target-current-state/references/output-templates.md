# Output Templates Index — Transformation Target Current State Analysis (SA-TRF-001)

> Registry of all deliverable templates for the Transformation Target Current State Analysis skill.
> Each output is produced during Step 4 using the corresponding template.

---

## Template Registry

| Output ID | Name | Template File | Description |
|-----------|------|--------------|-------------|
| OUT-01 | Transformation Target Code Structure Map | `templates/code-structure-map-template.md` | Annotated file and directory layout of the target scope: all files involved, their roles, and line counts |
| OUT-02 | Current Responsibility & Behavior Analysis | `templates/responsibility-analysis-template.md` | What the target does today: every responsibility, behavior, side effect, and entry/exit point documented |
| OUT-03 | Dependency Map (Inbound & Outbound) | `templates/dependency-map-template.md` | What the target depends on (outbound) and what depends on the target (inbound), with interface contracts documented |
| OUT-04 | Data Flow & Interface Analysis | `templates/data-flow-analysis-template.md` | All data flows through the target: APIs, events, shared state, database interactions, external integrations |
| OUT-05 | Test Coverage Assessment | `templates/test-coverage-report-template.md` | Existing unit and integration test inventory, coverage percentages, untested paths, and coverage gap analysis |
| OUT-06 | Technical Debt & Risk Register | `templates/tech-debt-risk-register-template.md` | Identified code smells, anti-patterns, known issues, coupling hotspots, and transformation risk areas with severity ratings |
| OUT-07 | Transformation Target Current State Report | `templates/current-state-report-template.md` | Enterprise-level consolidated report covering all findings, hard constraints, soft constraints, risk summary, and recommended follow-ups. User must confirm before any transformation work begins |

---

## Template Usage Rules

1. **All placeholders must be populated.** Templates contain `{placeholder}` fields that must be replaced with actual investigation findings. No placeholder may remain in final output (enforced by DoD-08).

2. **Output file naming convention.** Final outputs are saved to the analysis output directory:
   ```
   outputs/analysis-{YYYYMMDD-HHMMSS}/OUT-0{N}-{kebab-case-name}.md
   ```
   Example: `outputs/analysis-20260315-143000/OUT-07-current-state-report.md`

3. **Template immutability.** Templates in `templates/` are read-only references. Copy content, populate it, write result to output directory. Never modify template files directly.

4. **Minimum content thresholds.**
   - OUT-01 through OUT-06: Must be non-empty (> 0 bytes)
   - OUT-07: Must exceed 1000 bytes to ensure substantive content

5. **User confirmation required.** OUT-07 must be confirmed by the user before the analysis is considered complete (DoD-09).

---

## Cross-References

- **SOP steps:** See `references/sop.md`, Step 4 (sub-steps 4-2 through 4-9)
- **Quality gates:** See `references/dod.md`, Checks DoD-01 through DoD-20
- **Template files:** Located in the `templates/` directory of this skill package
