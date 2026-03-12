# Definition of Ready (DoR): Project Structure Scan (SA-DISC-001)

> Prerequisites that must be satisfied before the Project Structure Scan can begin execution.
> All mandatory checks must pass. The agent must not proceed past Phase 0 if any mandatory check fails.

---

## DoR Checklist

| Check ID | Check Item | Verification Method | Pass Criteria | Mandatory |
|----------|-----------|---------------------|---------------|-----------|
| DoR-01 | Project Intake completed | Check that intake summary exists and user confirmation flag is set | Intake summary record exists in memory DB with `confirmed = true` | Yes |
| DoR-02 | Project local path valid | `test -d <path>` and verify directory contains at least one file | Path exists, is a directory, and contains at least one file or subdirectory | Yes |
| DoR-03 | Git repository verified (if applicable) | `git -C <path> status` succeeds | If the project is a git repository, `git status` exits with code 0. Non-git projects skip this check. | No |
| DoR-04 | At least one build/manifest file exists | Glob search for known manifest files | At least one of the following exists in the project root or immediate subdirectories: `pom.xml`, `package.json`, `build.gradle`, `build.gradle.kts`, `requirements.txt`, `setup.py`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `Makefile`, `CMakeLists.txt`, `*.csproj`, `*.sln` | Yes |
| DoR-05 | Read permissions available for project files | Attempt to read a sample of files from the project directory | At least 3 files in the project tree are readable by the agent process | Yes |
| DoR-06 | Scan scope defined | Check intake summary for scope field | Scope is one of: `full`, `partial`, or `exclude-list`. If `partial`, at least one target directory is specified. If `exclude-list`, at least one exclude pattern is specified. | Yes |
| DoR-07 | Directories to exclude specified (if applicable) | Check intake summary for exclude list | If scan scope is `exclude-list` or user indicated exclusions, the exclude list is non-empty and contains valid directory paths or glob patterns | Conditional |
| DoR-08 | Purpose of scan communicated | Check intake summary for purpose field | Purpose string is non-empty and has been confirmed by the user during intake | Yes |
| DoR-09 | Memory database directory is writable | `test -w <memory_dir>` | The directory designated for the SQLite memory database exists and is writable | Yes |
| DoR-10 | Output directory is writable | `test -w <output_parent_dir>` or create it | The parent directory for scan outputs exists and is writable, or can be created | Yes |

---

## Pre-Flight Execution

The DoR check is executed during **Phase 0, Part B, Step 0B-1** (see `references/sop.md`).

### Execution Order

1. Run all mandatory checks (DoR-01 through DoR-06, DoR-08 through DoR-10).
2. Run conditional checks (DoR-07) only if the condition applies.
3. Run optional checks (DoR-03) and record results but do not block on failure.

### On Failure

- **Mandatory check fails:** Halt initialization. Report the failing check(s) to the user with a clear error message and remediation guidance.
- **Conditional check fails:** Halt initialization. Report the failing check and ask the user to provide the missing information.
- **Optional check fails:** Log a warning. Proceed with initialization but note the limitation (e.g., "Git history will not be available for analysis").

### Remediation Guidance

| Check ID | Remediation |
|----------|-------------|
| DoR-01 | Re-run Phase 0 Part A (Project Intake). |
| DoR-02 | Verify the project path. Ensure the directory exists and is not empty. |
| DoR-03 | Initialize a git repository with `git init` or correct the path. |
| DoR-04 | Confirm this is a software project. If no manifest file exists, create one or proceed with reduced analysis capabilities. |
| DoR-05 | Check file permissions. Ensure the agent has read access to the project directory. |
| DoR-06 | Specify the scan scope during intake: full, partial, or exclude-list. |
| DoR-07 | Provide at least one directory or pattern to exclude. |
| DoR-08 | Provide the purpose of the scan during intake. |
| DoR-09 | Ensure the memory directory exists and has write permissions. Create it if necessary. |
| DoR-10 | Ensure the output parent directory exists and has write permissions. Create it if necessary. |
