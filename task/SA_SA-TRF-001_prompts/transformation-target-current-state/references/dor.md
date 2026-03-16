# Definition of Ready (DoR) — Transformation Target Current State Analysis (SA-TRF-001)

> Prerequisites that MUST be satisfied before the agent begins analysis.
> If any mandatory prerequisite fails, halt and report to the user for resolution.

---

## DoR Checklist

| Check ID | Prerequisite | Required | Verification Method | Failure Action |
|----------|-------------|:--------:|---------------------|----------------|
| DoR-01 | Target project repository is cloned and accessible locally | YES | `ls {project_path}` succeeds | Ask user to provide correct local path or clone the repo |
| DoR-02 | Transformation target (method / component / module) is explicitly identified | YES | `target_name` and `target_path` are non-empty; `ls {target_path}` succeeds | Prompt user to specify exact target name and file path |
| DoR-03 | Transformation intent is clearly stated | YES | `transformation_intent` is non-empty and describes a concrete change type | Ask user to clarify what transformation is intended |
| DoR-04 | Analysis scope is defined | YES | `analysis_scope` is one of: `target-only`, `include-direct-dependencies`, `broad` | Present options and ask user to select |
| DoR-05 | Read permissions on target files are available | YES | `cat {target_path}` or `Read {target_path}` succeeds without permission error | Report permission issue to user |
| DoR-06 | Project build system or language ecosystem is known | YES | At least one manifest file exists: `pom.xml`, `package.json`, `build.gradle`, `requirements.txt`, `go.mod`, `Cargo.toml`, `*.csproj` | Run Glob to detect; if none found, ask user to specify language/build system |
| DoR-07 | No active merge conflicts in the target scope files | YES | `grep -r "<<<<<<" {target_path}` returns no matches | Alert user to resolve merge conflicts before analysis |
| DoR-08 | Target Intake Summary has been confirmed by the user | YES | User has explicitly confirmed the intake summary in Step 0 | Do not proceed to Step 1 until user confirms |
| DoR-09 | SQLite memory database is initialized | YES | `memory/agent_memory.db` exists or `scripts/init_memory.py` runs successfully | Run `python scripts/init_memory.py` |
| DoR-10 | Output directory is created | YES | Analysis output directory exists or is created successfully | Create directory: `mkdir -p outputs/analysis-{YYYYMMDD-HHMMSS}/` |

---

## Pre-Analysis Checks Script

Run the following before proceeding past Step 0:

```bash
# DoR-01: Project path
ls {project_path}

# DoR-02: Target file
ls {target_path}

# DoR-05: Read permissions
cat {target_path} | head -5

# DoR-06: Build system
find {project_path} -maxdepth 3 -name "pom.xml" -o -name "package.json" -o -name "build.gradle" -o -name "requirements.txt" -o -name "go.mod" -o -name "Cargo.toml" | head -5

# DoR-07: Merge conflicts
grep -r "<<<<<<" {target_path} 2>/dev/null | head -5
```
