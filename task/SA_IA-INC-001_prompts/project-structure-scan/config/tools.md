# Tools — Project Structure Scan Agent

## Core Tools

| # | Tool | Purpose | Usage Examples |
|---|------|---------|----------------|
| 1 | **Glob** | File pattern matching for directory and file discovery | `**/*.java`, `**/pom.xml`, `src/**/*.ts`, `**/{Controller,Service,Repository}*` |
| 2 | **Grep** | Content search for pattern identification — imports, annotations, decorators, keywords | `import\s+.*from`, `@RestController`, `@Entity`, `module.exports`, `func main()` |
| 3 | **Read** | File reading for build files, config files, entry points, key source files | Read `pom.xml`, `package.json`, `README.md`, main entry files |
| 4 | **Bash** (system) | System commands for structure analysis and metrics | `tree -L 4 -d`, `wc -l`, `find . -type f -name '*.py' \| wc -l`, `du -sh` |
| 5 | **Bash** (git) | Git commands for repository analysis | `git log --oneline -20`, `git branch -a`, `git remote -v`, `git diff --stat` |

## Language-Specific Dependency Analysis Tools

| Language | Command | Purpose |
|----------|---------|---------|
| Java (Maven) | `mvn dependency:tree -DoutputType=text` | Full dependency tree with transitive deps |
| Java (Gradle) | `gradle dependencies --configuration compileClasspath` | Compile-time dependency tree |
| JavaScript (npm) | `npm ls --depth=1` | Direct dependencies with immediate children |
| JavaScript (yarn) | `yarn list --depth=1` | Direct dependencies |
| Python (pip) | `pip list --format=columns` | Installed packages with versions |
| Python (poetry) | `poetry show --tree` | Dependency tree |
| Go | `go mod graph` | Module dependency graph |
| Rust | `cargo tree --depth=1` | Dependency tree |
| C# | `dotnet list package` | NuGet package list |
| Ruby | `bundle list` | Gem list with versions |

## Tool Usage Strategy

### Phase 2 (Understand Target Project)
1. **Glob** `**/{pom.xml,package.json,build.gradle,requirements.txt,go.mod,Cargo.toml}` → identify build system
2. **Read** manifest file → identify tech stack and dependencies
3. **Bash** `tree -L 2 -d {path}` → get directory overview
4. **Bash** `find {path} -name '*.{ext}' -not -path '*/node_modules/*' | wc -l` → count source files

### Phase 4 (Execute Scan)
1. **Bash** `tree -L 4 -d {path}` → deep directory structure
2. **Glob** `{path}/**/*` → complete file listing
3. **Grep** import/require statements → build dependency graph
4. **Grep** annotations/decorators → identify architecture patterns
5. **Read** key files (entry points, configs, interfaces) → understand module responsibilities
6. **Bash** language-specific dependency command → full dependency analysis
