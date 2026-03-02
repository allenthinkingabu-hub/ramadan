# Data Flow Diagram — Analytics Aggregation Pipeline

## Description
Shows how raw events from grading, error notebook, and user activity flow through the analytics aggregation pipeline to produce pre-computed dashboard data for students, teachers, parents, and admins.

## Diagram

```mermaid
flowchart TB
    subgraph "Event Sources"
        E1[GradingCompleted\nEvents]
        E2[ReviewSessionCompleted\nEvents]
        E3[MasteryAchieved\nEvents]
        E4[UserActivity\nEvents]
        E5[PaymentCompleted\nEvents]
    end

    subgraph "Message Broker"
        MQ[RabbitMQ\nanalytics.exchange\ntopic exchange]
    end

    subgraph "Analytics Service"
        C1[Event Consumer\nSpring AMQP Listener]
        C2[Event Normalizer\ntimestamp, tenant, user\ncontext enrichment]

        subgraph "Aggregation Engines"
            AG1[Student Aggregator\nper-student daily/weekly/monthly\naccuracy, volume, streaks]
            AG2[Class Aggregator\nper-class averages,\nranking, knowledge gaps]
            AG3[Knowledge Aggregator\nper-knowledge-point\nmastery rates, trends]
            AG4[System Aggregator\nplatform-wide KPIs,\nAI usage, revenue]
        end

        subgraph "CQRS Read Models"
            RM1[(student_dashboard\npre-computed)]
            RM2[(teacher_dashboard\npre-computed)]
            RM3[(parent_report\npre-computed)]
            RM4[(admin_dashboard\npre-computed)]
        end
    end

    subgraph "Data Store"
        PG[(PostgreSQL\nRead Replicas\naggregation tables)]
        REDIS[(Redis\nhot dashboard\ncache, TTL: 5min)]
    end

    subgraph "Dashboard Consumers"
        D1[Student Dashboard\naccuracy trends, streaks,\nknowledge mastery]
        D2[Teacher Dashboard\nclass analytics, student\ncomparison, knowledge gaps]
        D3[Parent Report\nweekly summaries,\nprogress tracking]
        D4[Admin Dashboard\nreal-time KPIs,\nAI usage, system health]
    end

    E1 --> MQ
    E2 --> MQ
    E3 --> MQ
    E4 --> MQ
    E5 --> MQ

    MQ --> C1
    C1 --> C2

    C2 --> AG1
    C2 --> AG2
    C2 --> AG3
    C2 --> AG4

    AG1 --> RM1
    AG2 --> RM2
    AG3 --> RM3
    AG4 --> RM4

    RM1 --> PG
    RM2 --> PG
    RM3 --> PG
    RM4 --> PG

    PG --> REDIS

    REDIS --> D1
    REDIS --> D2
    REDIS --> D3
    REDIS --> D4
```

## Aggregation Schedules

| Aggregator | Trigger | Freshness | Output |
|:---|:---|:---|:---|
| Student Aggregator | On each GradingCompleted/ReviewCompleted event | ≤ 1 min | Daily accuracy, weekly volume, streaks, knowledge mastery % |
| Class Aggregator | Batch every 5 min | ≤ 5 min | Class averages, student ranking, knowledge gap matrix |
| Knowledge Aggregator | Batch every 5 min | ≤ 5 min | Per-knowledge-point mastery rates, error frequency, trend |
| System Aggregator | Batch every 1 min | ≤ 1 min | Active users, AI calls/min, cache hit rate, revenue, error rate |

## Notes
- **CQRS pattern**: Write-side events processed by aggregators; read-side dashboards served from pre-computed tables
- **Data freshness**: Student/admin dashboards ≤ 1 min; teacher/parent dashboards ≤ 5 min (per NFR requirements)
- **Redis caching**: Hot dashboard data cached with 5-minute TTL for high-frequency reads
- **Read replicas**: Aggregation queries run against PostgreSQL read replicas to avoid impacting write workloads
- **Multi-tenant**: All aggregations scoped by tenant_id via Row-Level Security policies
