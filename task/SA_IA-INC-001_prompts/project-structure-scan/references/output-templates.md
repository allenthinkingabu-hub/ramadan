# Output Templates Index: Project Structure Scan (SA-DISC-001)

> Registry of all deliverable templates for the Project Structure Scan skill.
> Each output is produced during Phase 4 using the corresponding template.

---

## Template Registry

| Output ID | Name | Template Path | Description |
|-----------|------|---------------|-------------|
| OUT-01 | Project Structure Tree | `templates/structure-tree-template.md` | Annotated directory hierarchy showing the full project layout with descriptions for each significant directory and file grouping. |
| OUT-02 | Module Relationship Diagram | `templates/module-relationship-template.md` | Visual diagram (Mermaid format) showing dependencies and relationships between identified modules. |
| OUT-03 | Layering Pattern Analysis | `templates/layering-analysis-template.md` | Architecture pattern identification and analysis, documenting observed patterns (layered, hexagonal, MVC, etc.) with supporting evidence from the codebase. |
| OUT-04 | Package Dependency Map | `templates/dependency-map-template.md` | Comprehensive map of third-party and internal package dependencies, including version information and circular dependency detection. |
| OUT-05 | Module Responsibility Summary | `templates/module-summary-template.md` | Per-module descriptions covering purpose, responsibilities, key interfaces, and relationships for every identified module. |
| OUT-06 | Project Structure Scan Report | `templates/scan-report-template.md` | Comprehensive final report consolidating all findings, including executive summary, detailed analysis, recommendations, and references to all other outputs. |
| OUT-07 | Transformation Target Current State Report | `templates/transformation-target-template.md` | **Conditional — transformation scans only.** Deep-dive investigation of the transformation target: core logic description, key data structures, draw.io sequence diagrams, dependency analysis, test coverage, constraints, and readiness assessment. |

---

## Template Usage Rules

1. **All placeholders must be populated.** Templates contain `{placeholder}` fields that must be replaced with actual data during Phase 4. No placeholder may remain in the final output (enforced by DoD-07).

2. **Output file naming convention.** Final outputs are saved to the scan output directory using the pattern:
   ```
   outputs/scan-YYYYMMDD-HHMMSS/OUT-{ID}_{kebab-case-name}.md
   ```
   Example: `outputs/scan-20260312-143000/OUT-01_project-structure-tree.md`

3. **Template immutability.** Templates in the `templates/` directory are read-only references. Agents must copy template content, populate it, and write the result to the output directory. Never modify the template files directly.

4. **Minimum content thresholds.**
   - OUT-01 through OUT-05: Must be non-empty (> 0 bytes).
   - OUT-06 (Final Report): Must exceed 500 bytes to ensure substantive content.

5. **draw.io diagram validation.** OUT-02 (`diagrams/module-relationship.drawio`) and OUT-04 (`diagrams/dependency-map.drawio`) must be valid XML with `<mxfile>` as the root element. OUT-07, when produced, must be accompanied by at least one `diagrams/seq-*.drawio` sequence diagram file. All `.drawio` files must pass `xml.etree.ElementTree.parse()` validation (DoD-08, DoD-09, DoD-20).

---

## Cross-References

- **SOP production steps:** See `references/sop.md`, Phase 4 (Steps 4-6 through 4-11) and Phase 5 (Steps 5-14 for OUT-07).
- **Quality gates:** See `references/dod.md`, Checks DoD-01 through DoD-20.
- **Template files:** Located in the `templates/` directory of this skill package.
