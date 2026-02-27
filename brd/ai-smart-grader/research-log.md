# Research Log — AI Smart Grader BRD

## Research #1 — 2026-02-27 20:36
- **Tool**: WebSearch
- **Query**: "AI homework grading app photo scanning error notebook 错题本 智能判卷 products 2025 2026"
- **Purpose**: Identify existing products and market landscape for AI homework grading and error notebook platforms
- **Key Findings**:
  1. Gauth AI (ByteDance) held #1 US education app downloads in Q3 2025; AI education market reached $7.05B in 2025
  2. Chinese EdTech (作业帮, 小猿搜题, 学而思) upgraded from "answer retrieval" to "process explanation" with LLM integration
  3. Error notebooks (错题本) + AI can boost processing efficiency by over 80%, enabling knowledge gap discovery
  4. AI grading accuracy hovers around 50-55% with rubrics, 33% without — accuracy remains a key challenge
  5. 85% of teachers used AI tools in 2025; 17% specifically for quick feedback on student work
- **Sources**:
  - https://ucstrategies.com/news/gauth-ai-review-can-this-tool-really-help-you-study-like-a-real-teacher/
  - https://www.cnblogs.com/miketwais/p/18914316/ai_agent
  - https://www.qbitai.com/2020/09/18209.html
  - https://www.tshanywhere.org/post/top-ai-graders-teachers

## Research #2 — 2026-02-27 20:36
- **Tool**: WebSearch
- **Query**: "Spring AI Spring Cloud education platform architecture best practices 2025"
- **Purpose**: Understand technology architecture best practices for Java/Spring-based education platforms
- **Key Findings**:
  1. Spring AI 1.0 GA released May 2025; supports ChatModel, Prompts, RAG, ChatMemory, Tools, MCP
  2. Spring AI Alibaba 1.0 GA released — strong support for Chinese LLM ecosystem
  3. Recommended patterns: microservices (Spring Cloud), RAG pipelines for personalized learning, agentic AI patterns
  4. Key Spring Cloud components: Eureka (discovery), Resilience4J (fault tolerance), Sleuth+Zipkin (tracing), ELK (logging)
  5. Cloud-native deployment with Docker/Kubernetes recommended for scalability
- **Sources**:
  - https://spring.io/projects/spring-ai/
  - https://github.com/spring-projects/spring-ai
  - https://www.alibabacloud.com/blog/spring-ai-alibaba-1-0-ga-officially-released-marking-the-advent-of-a-new-era-in-java-agent-development_602299
  - https://www.javaguides.net/2025/12/spring-boot-microservices-roadmap-2026.html

## Research #3 — 2026-02-27 20:36
- **Tool**: WebSearch
- **Query**: "AI批改作业 拍照判题 错题本 产品 竞品分析 2025 2026"
- **Purpose**: Chinese market competitor analysis for AI grading and error notebook products
- **Key Findings**:
  1. Major Chinese competitors: 作业帮(快对AI), 猿辅导(小猿AI), 学而思; International: Photomath, Socratic
  2. Industry shifting from "photo search" to "AI tutoring" — from giving answers to explaining knowledge points
  3. Core competitive dimensions: photo recognition → AI explanation, error notebook → learning analytics, auto-grading → full-process automation
  4. Technical architecture: Data collection layer (RPA/OCR) + Analysis layer (LLM for both objective and subjective grading)
  5. Key differentiator: precise identification of knowledge weak points + personalized exercise recommendations
- **Sources**:
  - https://www.qbitai.com/2026/01/374770.html
  - http://www.ai-indeed.com/encyclopedia/12917.html
  - https://c.m.163.com/news/a/KLJ7MET405386T63.html

## Research #4 — 2026-02-27 20:50
- **Tool**: WebSearch
- **Query**: "AI education app DAU growth trajectory startup user scale first year 2025"
- **Purpose**: Establish realistic DAU projections for AI education app startup
- **Key Findings**:
  1. AI education market: $7.05B (2025) → $136.79B (2035), CAGR 34.52%
  2. Student AI usage surged from 66% (2024) to 92% (2025)
  3. Grok scaled from 0 to 9.5M DAU in one year (general AI, not education-specific)
  4. 60% of educators surveyed used AI tools in classrooms (Forbes Advisor Oct 2025)
  5. AI tutoring systems enhance student engagement by up to 30%
- **Sources**:
  - https://www.precedenceresearch.com/ai-in-education-market
  - https://a16z.com/state-of-consumer-ai-2025-product-hits-misses-and-whats-next/
  - https://www.enrollify.org/blog/ai-in-education-statistics

## Research #5 — 2026-02-27 20:50
- **Tool**: WebSearch
- **Query**: "LLM multimodal image analysis response time latency benchmark GPT Claude vision API 2025"
- **Purpose**: Determine realistic AI response time expectations for image analysis
- **Key Findings**:
  1. GPT-5.2: first-token 0.60s, 187 tok/s; Claude 4.5 Sonnet: first-token 2s, 77 tok/s
  2. GPT-4o: 320ms response time for text/audio/visuals
  3. Gemini 2.5 Flash: 372 tok/s (fastest reasoning model)
  4. Chat agents tolerate up to 2 seconds before users notice
  5. Best practice: intelligent model routing (speed model for user-facing, quality model for critical decisions)
- **Sources**:
  - https://research.aimultiple.com/llm-latency-benchmark/
  - https://artificialanalysis.ai/leaderboards/models
  - https://www.digitalapplied.com/blog/llm-comparison-guide-december-2025
