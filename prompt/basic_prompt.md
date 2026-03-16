 以 @brd_writer_agent_skill_definition.md  为模版，给 @system-architect-main-tasks.md 的  IA-INC-001 — Technical Discovery 任务 编写这个任务对应的文档      不要阅读其他文件。文件格式 Role_任务编号_任务名称_agent_skil_definition.md, 写成英文的 。 请先我要你做的任务理解任务，然后理解 ，然后在理解 “IA-INC-001 — Technical Discovery“ 含义，经过我确认了你在写

正确，我的业务： 用户通过手机、电脑、平板电脑上传自己的做得题目，然后系统将图片发送给 AI 大模型去分析做的题，然后将分析的结果返回给用户，AI分析题目的prompt 是可以后台配置的，用户可以选择将做错的题放入错题本。我希望采用前后端分离的云原生技术，采用技术栈必须是开源的、主流的、可以商用的开源框架，后端采用 Java 技术栈，采用主流的开源框架Spring Cloud,Spring AI ，用户是全球用户，可以使用 微信小程序、app,web,H5 访问系统； 系统要有管理控制台。


是不是把我们从第一步聊天内容，到现在都记录起来，然后为 第4天服务。

每一个阶段完成，检查这个阶段是否完成
  



 #任务：，我们来分析 Step 1: Code Archaeology 中的1.1 Project Structure Scan 这个任务，我们的任务是，根据这个1.1 定义，我们编写一个 prompt, 这个prompt ，调用 skill-creator 生成一个能够 1.1 这个任务的 Ai Agent SKill 的，你要参考 @task/brd_writer_agent_skill_definition.md                               
  这个文件。，并且这个新的skill 完成的效果必须是企业级别的，除了指定给你的文件或者目录，或者skil ,不要阅读其他内容       


##
以 @brd_writer_agent_skill_definition.md  为模版，给 @task/architect-sop-new-feature-on-existing-system.md 的 “1.1 Project Structure Scan” 这个任务编写这个任务对应的文档 。不要阅读其他文件。文件格式 Role_任务编号_任务名称_agent_skil_definition.md, 写成英文的 。 请先我要你做的任务理解任务，然后理解 ，然后在理解 “IA-INC-001 — Technical Discovery“ 含义，经过我确认了你在写


##
这个 Ai Agent 拥有了 长期记忆的功能，那怎么保证 Ai Agent 运行这个 ai agent skill 后，充分利用这些长期记忆呢， @task/SA_IA-INC-001_Project_Structure_Scan_agent_skill_definition.md、、、



@SA_IA-INC-001_prompts/SA_IA-INC-001_Project_Structure_Scan_agent_skill_definition.md 中 "”Functional Requirements: Interactive AI Agent Workflow"                                              
我任务少了，在扫描整个项目后，生成整个项目的理解后，还要调查，正对要改造的内容，要让AI Agent 调查这个改造点的现状是什么样的，   



以 @brd_writer_agent_skill_definition.md  为模版，给这个任务这个任务编写这个任务对应的文档 。这个文档是用来 skill-creator 生成skill 的 .不要阅读其他文件。文件格式 Role_任务编号_任务名称_agent_skil_definition.md, 写成英文的 。 请先我要你做的任务理解任务，然后理解 ，然后在理解任务含义，经过我确认了你在写 #任务:“我指定一个项目下某个方法进行改造,但是改造前你要帮我分析这个方法的设计,并编写一个现有设计文档,这个文档必须是企业级的,必须包  2. **Investigate current state**: Using tools (Glob, Grep, Read, Bash), deeply investigate the transformation target's current implementation:
     - Current code structure and file layout within the target scope
     - Current responsibilities and behaviors (what it does today)
     - Current dependencies: what the target depends on (inbound) and what depends on the target (outbound)
     - Current data flows and interfaces (APIs, events, shared state)
     - Current test coverage (unit/integration tests present or absent)
     - Known technical debt, code smells, or anti-patterns within the target
     - Configuration and environment dependencies
  3. **Identify transformation constraints**: Based on the current state investigation, identify:
     - Hard constraints (things that cannot change — public APIs, database schemas, SLAs)
     - Soft constraints (things that should be preserved if possible)
     - Risk areas (high-coupling zones, untested code, shared state)
  4. **Present Current State Summary**: The agent presents a structured **Transformation Target Current State Report** to the user, covering all findings above. The user confirms → proceed to Step 6. The user rejects or requests deeper investigation → the agent refines and repeats until agreed.”