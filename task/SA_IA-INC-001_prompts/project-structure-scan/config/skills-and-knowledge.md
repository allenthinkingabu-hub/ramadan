# Skills & Knowledge Base — Project Structure Scan Agent

## Skills

Capabilities the agent must possess to execute the Project Structure Scan task:

| # | Skill | Description |
|---|-------|-------------|
| 1 | **Directory structure analysis** | Traverse and annotate directory hierarchies, identify top-level organization patterns |
| 2 | **Build system recognition** | Identify build tools from manifest files: Maven (`pom.xml`), Gradle (`build.gradle`), npm (`package.json`), pip (`requirements.txt`/`pyproject.toml`), Cargo (`Cargo.toml`), Go (`go.mod`), CMake, Bazel |
| 3 | **Module boundary identification** | Detect logical module boundaries from package structure, build modules, and import patterns |
| 4 | **Dependency graph construction** | Build both internal (inter-module) and external (third-party library) dependency graphs |
| 5 | **Architectural pattern recognition** | Identify architecture styles: MVC, MVP, MVVM, DDD, Hexagonal, Clean, Onion, Layered, Microservices, Modular Monolith |
| 6 | **Code convention detection** | Recognize naming patterns, package organization strategies (by-feature vs by-layer), and coding standards |
| 7 | **Configuration analysis** | Analyze env files, config classes, feature flags, property files, and environment-specific configurations |
| 8 | **Multi-language project navigation** | Navigate projects using multiple programming languages and build systems simultaneously |
| 9 | **Monorepo structure recognition** | Identify monorepo patterns (workspace configs, shared packages, independent deployable units) |
| 10 | **Entry-point identification** | Locate application entry points, main classes, route definitions, and API surface areas |
| 11 | **Test structure analysis** | Understand test organization patterns and their relationship to source code |

## Knowledge Base

Domain knowledge the agent must draw from during analysis:

### Software Architecture Patterns

| Pattern | Key Indicators | Directory Signatures |
|---------|---------------|---------------------|
| **MVC** (Model-View-Controller) | Separate model, view, controller directories/packages | `models/`, `views/`, `controllers/` |
| **MVP** (Model-View-Presenter) | Presenter classes mediating between views and models | `presenters/`, `views/`, `models/` |
| **MVVM** (Model-View-ViewModel) | ViewModels with data binding | `viewmodels/`, `views/`, `models/` |
| **Layered Architecture** | Horizontal layers: presentation, business, data | `controller/`, `service/`, `repository/`, `dao/` |
| **Hexagonal (Ports & Adapters)** | Ports (interfaces) and adapters (implementations) | `ports/`, `adapters/`, `domain/`, `application/` |
| **Clean Architecture** | Concentric layers with dependency rule | `entities/`, `usecases/`, `interfaces/`, `frameworks/` |
| **Onion Architecture** | Similar to clean, domain at center | `domain/`, `application/`, `infrastructure/` |
| **DDD** (Domain-Driven Design) | Bounded contexts, aggregates, value objects | `domain/`, `aggregate/`, `valueobject/`, `repository/` |
| **Microservices** | Independent deployable services | Multiple service directories with own build files |
| **Modular Monolith** | Feature modules within single deployment | Feature-based top-level directories, shared kernel |

### Module Decomposition Principles

- **Cohesion**: Functional, sequential, communicational, procedural, temporal, logical, coincidental
- **Coupling**: Content, common, control, stamp, data, message (from tightest to loosest)
- **Separation of Concerns**: Each module addresses a distinct concern
- **Information Hiding**: Internal details are hidden behind well-defined interfaces

### SOLID Principles (Structural Implications)

| Principle | Structural Impact |
|-----------|------------------|
| **Single Responsibility** | Each module/class should have one reason to change |
| **Open/Closed** | Extension points, plugin architectures, strategy patterns |
| **Liskov Substitution** | Interface hierarchies, abstract base classes |
| **Interface Segregation** | Small, focused interfaces rather than monolithic ones |
| **Dependency Inversion** | Dependencies point inward (toward abstractions, toward domain) |

### Package Organization Strategies

- **Package-by-layer**: `controller/`, `service/`, `repository/` — groups by technical concern
- **Package-by-feature**: `user/`, `order/`, `payment/` — groups by business domain
- **Package-by-component**: Hybrid — features contain their own layers internally
- **Screaming Architecture**: Top-level packages reveal business capabilities, not frameworks

### Build Tool Conventions by Ecosystem

| Language | Build Tools | Manifest Files | Dependency Commands |
|----------|-------------|---------------|-------------------|
| Java | Maven, Gradle | `pom.xml`, `build.gradle`, `build.gradle.kts` | `mvn dependency:tree`, `gradle dependencies` |
| JavaScript/TypeScript | npm, yarn, pnpm | `package.json`, `yarn.lock`, `pnpm-lock.yaml` | `npm ls`, `yarn list` |
| Python | pip, poetry, pipenv | `requirements.txt`, `pyproject.toml`, `Pipfile` | `pip list`, `poetry show` |
| Go | go mod | `go.mod`, `go.sum` | `go mod graph` |
| Rust | Cargo | `Cargo.toml`, `Cargo.lock` | `cargo tree` |
| C# | dotnet, NuGet | `*.csproj`, `*.sln`, `packages.config` | `dotnet list package` |
| Ruby | Bundler | `Gemfile`, `Gemfile.lock` | `bundle list` |

### Common Project Structure Conventions by Framework

| Framework | Typical Structure |
|-----------|------------------|
| **Spring Boot** | `src/main/java/{group}/{artifact}/`, with `controller/`, `service/`, `repository/`, `model/`, `config/` |
| **Django** | `{project}/`, `{app}/models.py`, `views.py`, `urls.py`, `templates/`, `static/` |
| **Rails** | `app/models/`, `app/controllers/`, `app/views/`, `db/migrate/`, `config/` |
| **Next.js** | `pages/` or `app/`, `components/`, `lib/`, `public/`, `styles/` |
| **Express.js** | `routes/`, `controllers/`, `middleware/`, `models/`, `config/` |
| **Flutter** | `lib/`, `test/`, `android/`, `ios/`, `pubspec.yaml` |
| **FastAPI** | `app/`, `routers/`, `models/`, `schemas/`, `core/`, `api/` |
