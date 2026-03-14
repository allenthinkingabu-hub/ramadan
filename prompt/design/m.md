 AI Agent 长期记忆方案对比
                                                                                                                                                                            
  ┌───────────────────────┬──────────────────────────────────────┬───────────────────────────────────┬──────────────────────────┐                                         
  │         方案          │                 优点                 │               缺点                │         适合场景         │                                           
  ├───────────────────────┼──────────────────────────────────────┼───────────────────────────────────┼──────────────────────────┤                                           
  │ Markdown 文件         │ 人类可读、Git 可追踪、AI 原生友好    │ 无结构化查询、数据量大时检索慢    │ 对话记录、工作日志、报告 │
  ├───────────────────────┼──────────────────────────────────────┼───────────────────────────────────┼──────────────────────────┤
  │ SQLite                │ 结构化查询、轻量无服务、支持复杂检索 │ 人类不可直接阅读、Git diff 不友好 │ 任务状态、关系数据、索引 │
  ├───────────────────────┼──────────────────────────────────────┼───────────────────────────────────┼──────────────────────────┤
  │ JSON 文件             │ 半结构化、可读性尚可                 │ 大文件性能差、并发写不安全        │ 配置、小型结构数据       │
  ├───────────────────────┼──────────────────────────────────────┼───────────────────────────────────┼──────────────────────────┤
  │ 向量数据库 (ChromaDB) │ 语义搜索、相似度匹配                 │ 依赖额外安装、复杂度高            │ 知识检索、经验匹配       │
  └───────────────────────┴──────────────────────────────────────┴───────────────────────────────────┴──────────────────────────┘

  我的建议：混合架构（Markdown + SQLite）

  project-structure-scan/
  ├── memory/
  │   ├── agent_memory.db          ← SQLite: 结构化数据
  │   └── index.md                 ← 记忆索引说明
  ├── logs/
  │   ├── conversation-log.md      ← Markdown: 人类可审查
  │   └── work-log.md              ← Markdown: 人类可审查
  ├── research/                    ← Markdown: 调研成果
  ├── diagrams/                    ← Mermaid/输出产物
  └── config/                      ← Markdown: 配置文件

  分工原则：

  ┌─────────────────────────────────────┬──────────┬──────────────────────────────────────────────────┐
  │              数据类型               │ 存储方式 │                       原因                       │
  ├─────────────────────────────────────┼──────────┼──────────────────────────────────────────────────┤
  │ 对话记录、工作日志、调研报告        │ Markdown │ 人类需要审查、Git 可追踪                         │
  ├─────────────────────────────────────┼──────────┼──────────────────────────────────────────────────┤
  │ 任务状态、执行进度、DoD检查结果     │ SQLite   │ 需要结构化查询（如"哪些DoD项未通过"）            │
  ├─────────────────────────────────────┼──────────┼──────────────────────────────────────────────────┤
  │ 跨 session 记忆（经验、教训、发现） │ SQLite   │ 需要持久化检索（如"上次扫描这个项目发现了什么"） │
  ├─────────────────────────────────────┼──────────┼──────────────────────────────────────────────────┤
  │ 配置文件（RACI、触发器、工具清单）  │ Markdown │ 人类需要编辑维护                                 │
  └─────────────────────────────────────┴──────────┴──────────────────────────────────────────────────┘

  SQLite 表结构示例：

  -- 任务执行记忆
  CREATE TABLE task_memory (
      id INTEGER PRIMARY KEY,
      session_id TEXT,
      task_id TEXT,           -- e.g., 'SA-DISC-001'
      phase TEXT,             -- e.g., 'phase1', 'phase2'
      memory_type TEXT,       -- 'finding', 'decision', 'lesson', 'question'
      content TEXT,
      context TEXT,           -- 关联的项目/模块
      created_at TIMESTAMP,
      updated_at TIMESTAMP
  );

  -- DoD 检查记录
  CREATE TABLE dod_checks (
      id INTEGER PRIMARY KEY,
      session_id TEXT,
      check_item TEXT,
      status TEXT,            -- 'pass', 'fail', 'pending'
      evidence TEXT,
      checked_at TIMESTAMP
  );

  -- 跨 session 知识积累
  CREATE TABLE knowledge_base (
      id INTEGER PRIMARY KEY,
      project_name TEXT,
      category TEXT,          -- 'pattern', 'dependency', 'risk', 'insight'
      key TEXT,
      value TEXT,
      confidence FLOAT,
      source TEXT,
      created_at TIMESTAMP
  );

  这样 AI Agent 下次启动时可以：
  - 查询 SELECT * FROM task_memory WHERE task_id='SA-DISC-001' 获取历史经验
  - 查询 SELECT * FROM dod_checks WHERE status='fail' 知道哪些项还未通过
  - 查询 SELECT * FROM knowledge_base WHERE project_name='xxx' 获取项目积累知识




  新增了完整的 Memory Utilization Protocol 章节，核心内容包括：

  ┌────────────────────────────────────────┬──────────────────────────────────────────────────────────┐
  │                  章节                  │                        解决的问题                        │
  ├────────────────────────────────────────┼──────────────────────────────────────────────────────────┤
  │ Phase 0: Memory-Driven Context Loading │ 启动时自动判断"首次扫描"还是"再次扫描"，走不同路径       │
  ├────────────────────────────────────────┼──────────────────────────────────────────────────────────┤
  │ Phase 1: Memory-Enhanced Understanding │ 复用上次的任务目的理解，只问变化部分                     │
  ├────────────────────────────────────────┼──────────────────────────────────────────────────────────┤
  │ Phase 2: Memory-Accelerated Discovery  │ 预填已知答案（技术栈、框架等），减少 60-80% 重复提问     │
  ├────────────────────────────────────────┼──────────────────────────────────────────────────────────┤
  │ Phase 3: Memory-Informed Research      │ 跳过已有研究，聚焦差异和新风险                           │
  ├────────────────────────────────────────┼──────────────────────────────────────────────────────────┤
  │ Phase 4: Memory-Optimized Execution    │ 增量扫描、模式验证、依赖差异对比                         │
  ├────────────────────────────────────────┼──────────────────────────────────────────────────────────┤
  │ Cross-Project Knowledge Transfer       │ 用历史项目经验加速新项目的首次扫描                       │
  ├────────────────────────────────────────┼──────────────────────────────────────────────────────────┤
  │ Confidence Decay & Validation          │ 90天衰减、矛盾检测、低置信度清理，防止过期记忆误导 Agent │
  └────────────────────────────────────────┴──────────────────────────────────────────────────────────┘

  核心原则：记忆不只是存储，它必须在每个阶段主动改变 Agent 的行为 — 减少重复提问、跳过已知研究、增量扫描而非全量、跨项目知识迁移





  这是一个很实际的问题。当前文件约 400+ 行，包含 17 条要求 + 记忆架构 + 记忆利用协议 + 交互流程，一次性喂给 skill-creator 有两个风险：                     
                                                                                                                                                           
  1. 上下文溢出 — skill-creator 可能遗漏后半部分细节                                                                                                       
  2. 任务过重 — 一次生成 20+ 个文件，质量难以保证                                                                                                          
                                                                                                                                                           
  解决方案：分阶段执行策略                                                                                                                                 
                                                                                                                                                         
  将这个大文件拆成 多个独立的 Prompt 文件，按顺序分批调用 skill-creator：

  SA_IA-INC-001_Project_Structure_Scan_agent_skill_definition.md  ← 当前大文件（作为总纲）
      │
      ├── prompt-01_init-and-config.md        ← 第1批：初始化 + 配置文件（Req 1-6）
      │   产出: SKILL.md骨架, triggers.md, raci.md,
      │         skills-and-knowledge.md, tools.md, mcp-tools.md
      │
      ├── prompt-02_templates-and-sop.md      ← 第2批：输出模板 + SOP + DoD/DoR（Req 7-10）
      │   产出: 6个template文件, sop.md, dod.md, dor.md
      │
      ├── prompt-03_memory-architecture.md    ← 第3批：记忆架构 + 利用协议
      │   产出: memory/index.md, init_memory.py,
      │         memory utilization rules写入SKILL.md
      │
      ├── prompt-04_workflow-and-logging.md   ← 第4批：交互流程 + 日志（Req 11-13, 16-17）
      │   产出: 完善SKILL.md的workflow部分,
      │         conversation-log模板, work-log模板, verify_dod.py
      │
      └── prompt-05_supervisor.md             ← 第5批：监督Agent（Req 14-15）
          产出: 独立的 supervisor skill 完整目录

  每批执行的保障机制

  ┌──────────┬────────────────────────────────────────────────┐
  │   机制   │                      做法                      │
  ├──────────┼────────────────────────────────────────────────┤
  │ 前置检查 │ 每批 prompt 开头引用总纲对应章节，明确本批范围 │
  ├──────────┼────────────────────────────────────────────────┤
  │ 产出校验 │ 每批完成后，对照总纲的 checklist 逐项验证      │
  ├──────────┼────────────────────────────────────────────────┤
  │ 增量累加 │ 后一批在前一批产出基础上追加，不覆盖           │
  ├──────────┼────────────────────────────────────────────────┤
  │ 最终整合 │ 全部完成后，做一次完整性 cross-check           │
  └──────────┴────────────────────────────────────────────────┘

  执行方式

  两种选择：

  选项 A — 手动分批：我把大文件拆成 5 个独立 prompt 文件放到 task/prompts/ 目录，你按顺序每次调用 skill-creator 执行一个

  选项 B — 自动串联：我把大文件拆成 5 个 prompt 文件，然后编写一个总控 prompt，让 skill-creator 按顺序执行每个 prompt，每完成一个自动校验后再进入下一个

  你倾向哪个方案？确认后我开始拆分。




  # Memory
  ## Share Memory
  当前设计的局限
                                                                                                                                                                                        
  现在的 memory 是 skill 内部封闭 的：                                                                                                                                                
                                                                                                                                                                                        
  project-structure-scan/memory/agent_memory.db  ← 只有这个 skill 能访问                                                                                                                

  这意味着：
  - Supervisor 要读 scan agent 的 memory，必须硬编码路径
  - 下游 skill（如 Technology Stack Inventory）无法继承已有的 knowledge_base
  - PM Agent 看不到任何 agent 的执行状态

  需要解决的 3 个场景

  ┌──────────────────────┬─────────────────────────────────────────────────────────────────────────────────┐
  │         场景         │                                      例子                                       │
  ├──────────────────────┼─────────────────────────────────────────────────────────────────────────────────┤
  │ 同 Agent, 跨 Skill   │ IT Architect 先跑 structure scan，再跑 tech stack inventory，后者需要前者的发现 │
  ├──────────────────────┼─────────────────────────────────────────────────────────────────────────────────┤
  │ 跨 Agent, 同 Project │ Supervisor 读取 scan agent 的 dod_checks；PM 读取 scan_history                  │
  ├──────────────────────┼─────────────────────────────────────────────────────────────────────────────────┤
  │ 跨 Agent, 跨 Project │ 新项目扫描时，复用其他项目的 pattern knowledge                                  │
  └──────────────────────┴─────────────────────────────────────────────────────────────────────────────────┘

  几个可行方案

  方案 A：共享 Memory DB（workspace 级别）

  workspace/
  ├── .agent-memory/
  │   └── shared_memory.db        ← 所有 agent/skill 共用
  ├── project-structure-scan/
  ├── tech-stack-inventory/
  └── ...

  - 把 agent_memory.db 提升到 workspace 级别
  - 所有 skill 通过统一的 memory_ops.py 访问同一个 DB
  - 用 task_id 和 skill_name 字段区分来源
  - 优点：简单直接，改动最小
  - 缺点：schema 耦合，所有 skill 必须适配同一张表结构

  方案 B：分层 Memory 架构

  三层记忆模型:

  ┌─────────────────────────────────┐
  │  Team Memory (跨 Agent 共享)     │  ← workspace/.team-memory/
  │  scan_history, knowledge_base   │
  ├─────────────────────────────────┤
  │  Agent Memory (同 Agent 跨 Skill)│  ← workspace/.agent-memory/{agent_id}/
  │  lessons, decisions, context    │
  ├─────────────────────────────────┤
  │  Skill Memory (Skill 内部私有)   │  ← skill/memory/
  │  task_memory, dod_checks        │
  └─────────────────────────────────┘

  - Team Memory：跨 agent 共享的知识（项目技术栈、架构模式、风险列表）
  - Agent Memory：同一 agent 执行不同 skill 时的上下文延续
  - Skill Memory：skill 内部的执行细节（DoD 检查记录等）
  - 优点：职责清晰，隔离性好
  - 缺点：复杂度高，需要定义清楚哪些数据属于哪一层

  方案 C：Memory MCP Server

  所有 Agent/Skill
      ↓ (MCP 协议)
  ┌──────────────────┐
  │ Memory MCP Server │  ← 统一的记忆服务
  │  - read_memory()  │
  │  - write_memory() │
  │  - query()        │
  │  - subscribe()    │
  └──────────────────┘
      ↓
    SQLite / PostgreSQL

  - 用一个 MCP Server 封装所有 memory 操作
  - Agent/Skill 通过 MCP tool 调用读写 memory
  - Server 管理权限、命名空间、版本
  - 优点：最解耦，扩展性最好，可以加权限控制
  - 缺点：需要额外开发 MCP Server，运行时依赖

  方案 D：Memory Export/Handoff 协议

  Skill A 完成 → export_memory() → handoff.json → Skill B 启动 → import_memory()

  - 每个 skill 完成时导出标准化的 memory 摘要
  - 下游 skill 启动时导入上游的 handoff
  - PM Agent 负责编排 handoff 传递
  - 优点：松耦合，不需要共享 DB
  - 缺点：信息可能丢失，需要定义 handoff schema

  我的建议

  短期（改动最小）：方案 A — 把 DB 提到 workspace 级别，加 skill_name 字段区分来源

  中期（架构清晰）：方案 B — 三层 memory，明确数据归属

  长期（最佳扩展）：方案 C — Memory MCP Server，统一 API