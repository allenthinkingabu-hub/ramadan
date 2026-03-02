# Research Log - AI Smart Grader PRD

> Records all research activities (tool, query, findings, sources).

---

## Research Entry 1
- Timestamp: 2026-02-28
- Tool: web-search
- Query: "AI homework grading app features 2025 2026 Photomath Gauth competitors"
- Purpose: Understand competitive landscape and feature benchmarks for AI grading apps
- Findings:
  - AI education market projected $223.2B by 2034
  - Gauth (ByteDance): #2 iOS education, 1.39M DAU, powered by GPT-4V/Claude 3/Gemini, 95% solve rate for K-12 STEM, multi-subject, includes human tutors
  - Photomath (Google): Math only, strong pedagogical animations, $9.99/mo
  - MathGPT Pro: 17% higher accuracy than Photomath/Mathway
  - Key gap: None focus on error notebook + spaced repetition as core value
- Sources: bbntimes.com, skywork.ai, setapp.com, cybernews.com

## Research Entry 2
- Timestamp: 2026-02-28
- Tool: web-search
- Query: "intelligent error notebook 错题本 AI education app features spaced repetition"
- Purpose: Research existing error notebook implementations and spaced repetition in education
- Findings:
  - 错题本 is a deeply embedded Chinese study practice
  - Squirrel AI and Xueersi integrate AI-powered error tracking with knowledge graphs
  - Xueersi uses knowledge graphs for personalized homework recommendations and automatic correction
  - Spaced repetition shows 88% vs 78% test scores compared to traditional methods
  - 80% recall accuracy with spaced repetition vs 60% for cramming
  - No single app combines AI grading + intelligent error notebook + spaced repetition as primary value proposition
- Sources: technologyreview.com, 100tal.com, en.people.cn, npr.org

## Research Entry 3
- Timestamp: 2026-02-28
- Tool: web-search
- Query: "AI grading accuracy multimodal LLM handwriting recognition education 2025"
- Purpose: Understand current state of AI grading accuracy and handwriting recognition
- Findings:
  - Late-2025 models made end-to-end handwritten exam grading practically viable for first time
  - GPT-4o consistently outperforms other models in handwriting recognition + grading accuracy
  - Error propagation from imperfect handwriting recognition remains key challenge
  - Multi-stage pipeline needed: format check → ensemble graders → supervisor aggregation → validation
  - >80% text correctly converted at >200dpi scanning quality
  - Mathematical notation (superscripts, vectors, differentiation) still problematic
  - Pedagogical feedback can be useful even when grading accuracy is imperfect
- Sources: arxiv.org (2601.00730v1, 2506.04822v2), emerald.com, ijcai.org

## Research Entry 4
- Timestamp: 2026-02-28
- Tool: web-search
- Query: "EdTech freemium subscription conversion rate best practices 2025"
- Purpose: Benchmark conversion rates and monetization best practices for EdTech
- Findings:
  - EdTech freemium conversion rates: 2-8% range
  - Free trial conversion: up to 22%
  - Opt-out trials convert 48.8% vs opt-in 18.2%
  - Hybrid pricing models grow revenue 2.4x faster than single-model
  - 92% of teachers discover tech through free trials
  - Best practices: balance free/premium features, personalized onboarding, contextual upsells at peak engagement, social proof, gamification
  - Canva converts 6% of free users; Slack achieves 30%
- Sources: pathmonk.com, getmonetizely.com, userpilot.com, fastercapital.com
