<p align="center">
  <a href="README.md">English</a> |
  <strong>中文</strong> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.de.md">Deutsch</a>
</p>

# Ramadan AI 交付平台

**通过专业化、编排式 AI 智能体实现端到端 IT 项目自动化交付。**

Ramadan AI 将软件交付生命周期转化为一套可组合的 AI 智能体技能体系。项目生命周期中的每项任务——从项目章程制定到发布后复盘——均被编码为结构化技能，配备独立的 SOP、准入条件（DoR）、完成条件（DoD）、RACI 责任矩阵及工具引用。多智能体团队在编排引擎的协调下执行这些技能，在每个阶段产出可审计、经质量门禁把控的交付物。

---

## 目录

- [项目动机](#项目动机)
- [核心概念](#核心概念)
- [智能体团队](#智能体团队)
- [技能结构解析](#技能结构解析)
- [交付手册](#交付手册)
- [执行模型](#执行模型)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [深入解析：项目结构扫描与智能体记忆系统](#深入解析项目结构扫描与智能体记忆系统)
- [参与贡献](#参与贡献)
- [许可证](#许可证)

---

## 项目动机

企业 IT 项目遵循成熟的生命周期阶段——启动、需求、开发、测试、发布——然而每项任务的操作知识往往散落在各类 Wiki、口口相传的经验或临时拼凑的检查清单中。Ramadan AI 通过以下方式解决这一问题：

1. **将交付生命周期分解**为覆盖所有阶段的离散、定义明确的任务。
2. **将每项任务编码为 AI 智能体技能**，具备完整的质量维度（SOP、DoR、DoD、RACI、工具链）。
3. **编排技能执行**，通过事件驱动的多智能体架构与内置的督导质量门禁实现。

最终成果是一套由 AI 智能体驱动的、可复现、可审查、可持续改进的交付体系。

---

## 核心概念

### 一任务一技能模型

软件交付生命周期中的每项任务恰好映射到一个 AI 智能体技能。技能不是泛化的提示词——而是包含以下维度的结构化执行单元：

| 维度 | 用途 | 示例 |
|:---|:---|:---|
| **SOP** | 分步操作规程（Phase 0–5） | 如何开展技术发现评估 |
| **DoR** | 执行前必须满足的前置条件 | 范围已定义、干系人已识别、工具已就绪 |
| **DoD** | 任务标记完成前必须通过的质量检查清单 | 涵盖交付物、流程和文档的 19 项检查 |
| **RACI** | 全部干系人的责任分配 | SA = 执行者，PM = 负责人，TL = 被咨询方 |
| **工具** | 工具引用及使用指南 | WebSearch、文件操作、图表生成器 |
| **触发条件** | 激活该技能的条件 | 上游任务完成、项目经理指令 |
| **输出模板** | 标准化交付物格式 | 报告结构、决策日志格式 |

### 督导质量门禁

每个主技能都配有一个**督导技能**，执行独立的质量检查。只有当督导对所有检查项达到 100% 通过率时，任务才视为完成。未通过的项目会触发自动整改与复检。

### 事件驱动编排

智能体之间通过结构化事件协议进行通信：

```
PM 广播 TaskTriggered → 角色智能体执行技能 → 自检 DoD
  → 督导检查 → 100% 通过 → 向 PM 报告 TaskCompleted
  → PM 触发下游任务
```

---

## 智能体团队

Ramadan AI 以四智能体团队运作，每个智能体拥有明确的角色定位和技能组合：

| 智能体 | 角色 | 类型 | 技能数 | 覆盖领域 |
|:---|:---|:---|:---:|:---|
| **PM Agent** | 项目经理 | 编排者 | 24 | 项目章程、干系人分析、资源规划、风险管理、发布协调、项目收尾 |
| **IPM Agent** | IT 产品经理 | 角色智能体 | 21 | 需求采集、BRD/PRD 编写、用户故事、验收标准、UAT、上线协调 |
| **SA Agent** | 系统架构师 | 角色智能体 | 37 | 技术发现、架构设计、NFR 定义、集成设计、安全评审、部署架构 |
| **TL Agent** | 技术负责人 | 角色智能体 | 24 | 技术愿景、方案设计、代码评审管理、开发规范、技术风险评估 |

每个主技能均配有对应的督导技能，总计 **212 个技能目录**（106 个主技能 + 106 个督导技能）。

---

## 技能结构解析

每个技能遵循标准化的目录结构：

```
{role}-{skill-name}/
├── SKILL.md                        # 技能定义，包含 Phase 0-5 工作流
└── references/
    ├── sop.md                      # 标准操作规程
    ├── dor.md                      # 准入条件
    ├── dod.md                      # 完成条件
    ├── raci.md                     # RACI 责任矩阵
    ├── tools.md                    # 工具使用参考
    ├── triggers.md                 # 触发条件
    ├── output-templates.md         # 交付物模板
    └── skills-and-knowledge.md     # 所需能力要求
```

督导技能额外包含 `inspection-criteria.md` 文件和 `scripts/verify_dod.py` 自动化验证脚本。

### 通用 Phase 0–5 工作流

所有技能执行统一的六阶段工作流以确保一致性：

| 阶段 | 名称 | 目的 |
|:---:|:---|:---|
| 0 | 初始化 | 创建输出目录、初始化日志、验证 DoR |
| 1 | 理解任务目标 | 通过对话澄清目标，获取用户确认 |
| 2 | 理解主题领域 | 深入领域上下文，收集背景信息 |
| 3 | 调研与问答 | 行业调研、迭代式问题生成、专家咨询 |
| 4 | 执行与交付 | 使用模板产出交付物，依据 DoD 自检 |
| 5 | 完成与交接 | 调用督导、整改缺陷、向 PM 汇报 |

---

## 交付手册

[`delivery_playbook.md`](task/delivery_playbook.md) 定义了五个项目阶段中所有任务的完整执行顺序，按顺序波次组织：

### 阶段与任务分布

| 阶段 | 说明 | 关键活动 |
|:---|:---|:---|
| **启动阶段** | 项目立项与可行性评估 | 章程制定、干系人分析、需求采集、技术选型、风险识别 |
| **需求阶段** | 详细规格说明与设计 | 架构设计、NFR 定义、集成设计、数据架构、PRD 编写、技术规范 |
| **开发阶段** | 实施与技术指导 | 代码/设计评审、技术探针/PoC 主导、技术债务管理、ADR 编写 |
| **测试阶段** | 验证与合规检查 | 性能测试、安全评审、合规验证、基础设施验证、UAT 协调 |
| **发布阶段** | 部署与运行稳定 | 部署架构、监控体系搭建、容量规划、上线协调、超级保障期、复盘 |

### 波次执行模型

同一波次内的任务并行执行。第 N 波次的所有任务必须全部完成后，第 N+1 波次方可启动。这种机制在遵循任务依赖关系的前提下实现了最大并行度。

---

## 执行模型

### 事件协议

| 事件 | 方向 | 载荷 |
|:---|:---|:---|
| `TaskTriggered` | PM → 角色智能体 | `{ task_id, skill_dir, inputs, context }` |
| `TaskCompleted` | 角色智能体 → PM | `{ task_id, status, artifacts, supervisor_report }` |
| `SupervisorTriggered` | 角色智能体 → 督导 | `{ task_id, output_dir }` |
| `SupervisorCompleted` | 督导 → 角色智能体 | `{ task_id, pass_rate, report, remediation_items }` |

### 质量保障流程

```
角色智能体完成技能执行
       │
       ▼
自检：验证全部 19 项 DoD 检查项
       │
       ├── 未通过 → 自动整改，重新验证
       │
       ▼
调用配对督导技能
       │
       ├── 未通过 → 接收整改报告，修复后重新调用督导
       │
       ▼
达到 100% 通过率 → 向 PM 报告 TaskCompleted
```

### 幂等性

所有任务执行均具备幂等性。系统跟踪任务状态（`PENDING`、`IN_PROGRESS`、`DONE`、`FAILED`），并根据状态自动恢复或跳过，避免重复工作，确保可靠的故障恢复能力。

---

## 项目结构

```
ramadan/
├── IDENTITY.md                     # 团队身份定义
├── SOUL.md                         # 团队人格与运行边界
├── AGENTS.md                       # 智能体注册表与事件协议
├── USER.md                         # 用户交互模型
├── TOOLS.md                        # 工具使用规范
│
├── config/
│   ├── agents-registry.json        # 智能体定义与元数据
│   ├── openclaw.json               # 技能绑定、工具配置、事件总线配置
│   └── event-bus.json              # 事件路由规则
│
├── pm-*/                           # 24 个 PM 技能 + 24 个督导技能
├── ipm-*/                          # 21 个 IPM 技能 + 21 个督导技能
├── sa-*/                           # 37 个 SA 技能 + 37 个督导技能
├── tl-*/                           # TL 技能 + 督导技能
│
├── task/
│   ├── delivery_playbook.md        # 完整任务执行序列
│   └── *_agent_skill_definition.md # 任务级技能规格说明
│
├── prompt/
│   ├── generate_team.py            # 团队脚手架生成器
│   └── openclaw-skill-creator-prompt.md  # 技能创建指南
│
├── openclaw-team/                  # 可部署团队包
│   ├── skills/                     # 所有技能汇总
│   ├── workspaces/                 # 智能体工作区模板
│   ├── scripts/
│   │   ├── install_team.py         # 一键安装器
│   │   ├── quick_validate.py       # 结构验证器
│   │   ├── init_skill.py           # 新技能脚手架工具
│   │   └── package_skill.py        # 技能打包器
│   └── config/                     # 部署配置
│
└── scripts/
    ├── install_team.py             # 团队部署脚本
    ├── bootstrap_workspaces.py     # 工作区初始化脚本
    └── package_team.py             # 分发打包器
```

---

## 快速开始

### 前置条件

- Python 3.8+
- Claude Code CLI，需具备 Claude Opus 4.6 模型访问权限
- Git

### 安装步骤

1. **克隆仓库**
   ```bash
   git clone <repository-url>
   cd ramadan
   ```

2. **安装团队包**
   ```bash
   python scripts/install_team.py
   ```

3. **初始化智能体工作区**
   ```bash
   python scripts/bootstrap_workspaces.py
   ```

4. **验证技能结构**
   ```bash
   python openclaw-team/scripts/quick_validate.py
   ```

### 创建新技能

使用技能脚手架工具生成包含所有必要引用文件的新技能：

```bash
python openclaw-team/scripts/init_skill.py --role sa --name my-new-skill
```

该命令将创建完整的目录结构，包含 SOP、DoR、DoD、RACI、工具、触发条件和输出模板的模板文件。

---

## 深入解析：项目结构扫描与智能体记忆系统

**项目结构扫描**技能（`project-structure-scan`）是 Ramadan AI 中架构最为先进的技能，也是一项关键能力的参考实现——大多数 AI 智能体技能所缺乏的能力：**跨会话持久化的结构化记忆，能够在项目间传递知识**。

### 问题：无状态的 AI 智能体

默认情况下，AI 智能体是无状态的。每次对话都从零开始。当智能体今天扫描了一个代码库，用户下周再次扫描同一项目时，智能体对之前的发现毫无记忆，无法感知变更，也无法跳过重复工作。这导致了以下问题：

- 对未变更代码的重复分析
- 重复询问用户已回答过的问题
- 无法追踪项目的演进过程
- 缺乏跨项目学习能力（项目 A 的洞见无法惠及项目 B）

项目结构扫描技能通过**基于 SQLite 的记忆系统**解决了这一问题，使智能体在每次调用后逐步变得更加智能。

### 记忆架构

记忆系统使用本地 SQLite 数据库（`memory/agent_memory.db`），包含四张专用数据表：

```
┌─────────────────────────────────────────────────────────────┐
│                    agent_memory.db                           │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ task_memory  │  │ knowledge    │  │   scan_history    │  │
│  │             │  │ _base        │  │                   │  │
│  │ findings    │  │              │  │ session tracking  │  │
│  │ decisions   │  │ patterns     │  │ scope & status    │  │
│  │ lessons     │  │ dependencies │  │ deliverables path │  │
│  │ questions   │  │ tech_stack   │  │ timestamps        │  │
│  │ risks       │  │ conventions  │  │                   │  │
│  │             │  │ insights     │  │                   │  │
│  │ (per phase, │  │              │  │                   │  │
│  │  per session)│  │ (confidence  │  │                   │  │
│  │             │  │  scored,     │  │                   │  │
│  │             │  │  cross-      │  │                   │  │
│  │             │  │  project)    │  │                   │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
│                                                             │
│  ┌─────────────┐                                            │
│  │ dod_checks  │    Supplementary Files:                    │
│  │             │    ├── logs/conversation-log.md             │
│  │ per-round   │    ├── logs/work-log.md                    │
│  │ pass/fail   │    ├── research/{topic}.md                 │
│  │ evidence    │    └── phase{N}-questions.md                │
│  └─────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
```

| 数据表 | 用途 | 关键字段 |
|:---|:---|:---|
| `task_memory` | 单次会话的发现、决策、经验教训、问答及风险 | `session_id`, `phase`, `memory_type`, `content`, `tags` |
| `knowledge_base` | 跨会话可复用知识，带置信度评分 | `category`, `key`, `value`, `confidence` (0.0–1.0) |
| `scan_history` | 每次扫描执行的审计追踪 | `project_name`, `scan_scope`, `status`, `deliverables_path` |
| `dod_checks` | 按轮次记录的质量门禁验证结果 | `check_round`, `check_item`, `status`, `evidence` |

### 记忆系统如何融入各工作流阶段

记忆系统并非外挂功能——它深度织入技能执行的每个阶段：

**Phase 0 — 记忆驱动的初始化**

启动时，智能体查询 `scan_history` 以判断该项目是否曾被扫描过。这一查询决定了整个执行路径：

```
load_project_history(project_name)
  │
  ├── 发现历史扫描记录 → 重新扫描模式
  │   └── generate_memory_summary() → 向用户呈现
  │       └── 用户选择：增量扫描 / 全量重新扫描 / 查看历史结果
  │
  ├── 无历史记录，但存在相似项目 → 假设推导模式
  │   └── get_similar_projects(tech_stack_tags)
  │       └── "项目 X 使用了 DDD + 六边形架构，是否检查类似模式？"
  │
  └── 无历史记录，无相似项目 → 全新扫描模式
```

在开始任何工作之前，智能体还会执行维护操作：`apply_confidence_decay()` 对 90 天内未更新的知识条目降低置信度评分，`prune_low_confidence()` 清除置信度低于 0.3 阈值的条目。

**Phase 1 — 记忆增强的目标理解**

智能体不再每次都从头询问"你为什么需要这次扫描？"，而是查询历史目标记录：

```python
load_lessons_learned(task_id='SA-DISC-001', project_name=...) # filtered by phase='phase1'
```

如果存在记录，智能体会提示：*"上次扫描该项目时，目标是：{previous_purpose}。这次目标是否相同？"*——将原本 5 分钟的对话缩短为一次确认。

**Phase 2 — 记忆加速的发现过程**

智能体查询 `knowledge_base` 中已记录的技术栈、模式和约定：

```python
load_project_knowledge(project_name)  # returns entries sorted by confidence DESC
```

已知答案会被预填充。只有增量问题——未知或可能已变更的内容——才会被提出。在重新扫描时，这可以减少 60%–80% 的问题量。

**Phase 3 — 记忆引导的调研**

加载之前的调研文件和风险记录。智能体跳过重复调研，聚焦于空白领域，并主动复查已知风险：*"上次我识别了以下风险：{list}。是否需要验证这些风险是否已解决？"*

**Phase 4 — 记忆优化的执行**

对于增量扫描，智能体加载之前的 `OUT-01`（项目结构树），与当前目录结构进行差异对比，仅对变更区域进行深度扫描。之前的 `OUT-04`（依赖关系图）与当前清单文件对比，生成仅包含变更内容的依赖报告。这使得重新扫描的执行时间减少 40%–70%。

### 跨项目知识迁移

最强大的记忆功能可跨项目边界运作。当智能体遇到新项目时，会在知识库中搜索具有相似技术栈的项目：

```python
get_similar_projects(db_path, tech_stack_tags=["spring-boot", "postgresql", "redis"])
# Returns: [{"project_name": "ProjectX", "matching_tags": [...], "match_count": 3}]
```

来自相似项目的高置信度模式成为新项目的假设。如果智能体曾识别到三个 Spring Boot 项目都使用六边形架构模式，它可以主动询问：*"我的记录中相似项目使用了六边形架构，是否需要在此项目中查找该模式？"*——使首次扫描分析效率提升约 30%。

### 置信度衰减与矛盾检测

知识并非永远有效。记忆系统实现了两种机制以维护数据完整性：

1. **置信度衰减**：每隔 90 天，未更新的条目会损失 0.2 置信度分值（最低为 0.0）。一个初始置信度为 0.8 的条目，若从未被重新确认，将在连续周期内衰减至 0.6 → 0.4 → 0.2 → 0.0。低于 0.3 的条目将被清除并向用户报告。

2. **矛盾检测**：在写入新知识条目之前，智能体会检查是否存在冲突：

   ```python
   contradiction = detect_contradictions(db_path, project_name, category, key, new_value)
   # Returns existing vs. new value if they differ
   ```

   当发现矛盾时（例如，架构模式之前记录为"MVC"，但新证据表明是"Hexagonal"），智能体会标记冲突并请用户裁决——而非静默覆盖。

### 记忆操作 API

所有记忆操作在 `scripts/memory_ops.py` 中实现为纯函数，使用显式数据库路径参数：

| 操作 | 函数 | 使用场景 |
|:---|:---|:---|
| 加载扫描历史 | `load_project_history()` | Phase 0 — 确定扫描模式 |
| 加载知识 | `load_project_knowledge()` | Phase 1–4 — 预填充已知答案 |
| 加载经验教训 | `load_lessons_learned()` | Phase 1–3 — 跳过重复工作 |
| 查找相似项目 | `get_similar_projects()` | Phase 0 — 跨项目知识迁移 |
| 生成摘要 | `generate_memory_summary()` | Phase 0 — 向用户呈现历史 |
| 记录发现 | `record_finding()` | Phase 4 — 持久化扫描结果 |
| 记录决策 | `record_decision()` | Phase 1–3 — 持久化确认的决策 |
| 记录风险 | `record_risk()` | Phase 3–4 — 持久化已识别的风险 |
| 记录知识 | `record_knowledge()` | 所有阶段 — UPSERT 至知识库 |
| 记录经验教训 | `record_lesson()` | Phase 5 — 沉淀会话洞见 |
| 开始/完成扫描 | `start_scan()` / `complete_scan()` | Phase 0/5 — 扫描生命周期管理 |
| 记录 DoD 检查 | `record_dod_check()` | Phase 4 — 质量门禁结果 |
| 执行衰减 | `apply_confidence_decay()` | Phase 0 — 维护数据时效性 |
| 检测矛盾 | `detect_contradictions()` | 每次知识写入前 |
| 清除低置信度 | `prune_low_confidence()` | Phase 0 — 移除过期条目 |

### 技能目录结构

项目结构扫描技能在标准技能结构基础上扩展了记忆、调研和模板目录：

```
project-structure-scan/
├── SKILL.md                          # 技能定义（记忆增强的 Phase 0-5）
├── memory/
│   ├── index.md                      # 记忆架构文档
│   └── agent_memory.db               # SQLite 数据库（运行时创建）
├── config/
│   ├── triggers.md                   # 项目准入检查清单（7 项）
│   ├── raci.md                       # RACI 矩阵及下游触发关系
│   ├── tools.md                      # 工具使用参考
│   ├── mcp-tools.md                  # MCP 工具配置
│   └── skills-and-knowledge.md       # 智能体所需能力
├── references/
│   ├── sop.md                        # 标准操作规程
│   ├── dor.md                        # 准入条件
│   ├── dod.md                        # 完成条件
│   └── output-templates.md           # 模板索引
├── templates/
│   ├── structure-tree-template.md    # OUT-01 模板
│   ├── module-relationship-template.md # OUT-02 模板
│   ├── layering-analysis-template.md # OUT-03 模板
│   ├── dependency-map-template.md    # OUT-04 模板
│   ├── module-summary-template.md    # OUT-05 模板
│   └── scan-report-template.md       # OUT-06 模板
├── scripts/
│   ├── init_memory.py                # 数据库模式初始化
│   ├── memory_ops.py                 # 记忆 CRUD 操作库
│   └── verify_dod.py                 # 自动化 DoD 验证
├── research/                         # 调研产物（运行时填充）
├── logs/                             # 执行日志（运行时填充）
└── diagrams/                         # 生成的图表（运行时填充）
```

### 设计原则

记忆架构遵循以下设计理念：

1. **SQLite 优先于云存储**：记忆数据本地化、可移植，且无需基础设施依赖。数据库文件可提交至代码仓库或在团队成员间共享。

2. **置信度评分优先于二元判定**：知识不是简单的"已知"或"未知"——它携带置信度评分并随时间衰减，反映了软件项目持续演进、昨日之真理未必适用于今日的客观现实。

3. **UPSERT 语义**：`record_knowledge()` 执行 UPSERT 操作——如果相同的 `(project_name, category, key)` 元组已存在，则更新值和置信度，而非创建重复条目。

4. **任务记忆与知识库分离**：`task_memory` 作用域为单次会话，记录原始问答、决策和发现。`knowledge_base` 作用域为项目级别，存储经提炼的、可跨会话复用的知识。

5. **WAL 日志模式**：数据库采用预写式日志（Write-Ahead Logging）以提升并发性能，允许在写入期间进行读取操作而不产生阻塞。

---

## 参与贡献

### 添加技能

1. 在 `task/` 中以智能体技能定义文档的形式定义任务。
2. 在交付手册中将任务映射到对应的交付阶段和波次。
3. 使用 `init_skill.py` 搭建技能脚手架。
4. 填充所有引用文件（SOP、DoR、DoD、RACI、工具、触发条件、输出模板）。
5. 创建配对的督导技能及检查标准。
6. 在 `config/openclaw.json` 中注册技能。
7. 使用 `quick_validate.py` 进行验证。

### 技能质量标准

每个技能必须包含：
- 完整的 Phase 0–5 SOP，不可跳过任何阶段
- 包含可验证前置条件的 DoR 检查清单
- 包含 19 项质量门禁检查项的 DoD 检查清单
- 分配所有相关干系人的 RACI 矩阵
- 所有交付物的输出模板
- 配对的督导技能及检查标准

---

## 许可证

本项目为专有软件，保留所有权利。
