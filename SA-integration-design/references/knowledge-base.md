# Integration Design Agent — Knowledge Base Checklist

## Required Knowledge Domains

### 1. Integration Architecture Patterns
- [ ] Enterprise Integration Patterns (EIP) — Gregor Hohpe
- [ ] Microservices integration patterns (API gateway, service mesh, sidecar)
- [ ] Event-driven architecture (EDA) patterns
- [ ] Saga pattern for distributed transactions
- [ ] CQRS and event sourcing patterns
- [ ] Strangler fig pattern for legacy integration

### 2. API Design & Standards
- [ ] OpenAPI 3.x specification
- [ ] AsyncAPI specification
- [ ] GraphQL schema design
- [ ] gRPC / Protocol Buffers
- [ ] REST API best practices (Richardson Maturity Model)
- [ ] API versioning strategies (URL, header, query parameter)
- [ ] HATEOAS principles

### 3. Data Exchange & Formats
- [ ] JSON / JSON Schema
- [ ] XML / XSD
- [ ] Protocol Buffers / Avro / Parquet
- [ ] CSV / flat file formats
- [ ] EDI standards (if applicable)

### 4. Messaging & Event Streaming
- [ ] Apache Kafka architecture and patterns
- [ ] RabbitMQ / AMQP
- [ ] AWS SQS/SNS, Azure Service Bus, GCP Pub/Sub
- [ ] MQTT for IoT integrations
- [ ] WebSocket for real-time communication
- [ ] Server-Sent Events (SSE)

### 5. Security in Integration
- [ ] OAuth 2.0 / OpenID Connect flows
- [ ] Mutual TLS (mTLS)
- [ ] API key management and rotation
- [ ] JWT token validation
- [ ] Data encryption in transit (TLS 1.3)
- [ ] API threat protection (OWASP API Top 10)
- [ ] Zero-trust network architecture for integrations

### 6. Cloud Integration Services
- [ ] AWS: API Gateway, EventBridge, Step Functions, AppSync
- [ ] Azure: API Management, Logic Apps, Event Grid, Service Bus
- [ ] GCP: Apigee, Cloud Functions, Pub/Sub, Cloud Endpoints

### 7. Integration Middleware
- [ ] API gateways (Kong, Apigee, AWS API Gateway)
- [ ] Service mesh (Istio, Linkerd)
- [ ] iPaaS platforms (MuleSoft, Dell Boomi, Workato)
- [ ] ETL/ELT tools (Airflow, dbt, Fivetran)

### 8. Monitoring & Observability
- [ ] Distributed tracing (OpenTelemetry, Jaeger, Zipkin)
- [ ] API monitoring and analytics
- [ ] SLA/SLO measurement
- [ ] Health check patterns
- [ ] Log aggregation for integration flows

### 9. Error Handling & Resilience
- [ ] Circuit breaker pattern (Hystrix, Resilience4j)
- [ ] Retry strategies (exponential backoff, jitter)
- [ ] Dead-letter queues and poison message handling
- [ ] Bulkhead pattern
- [ ] Timeout and fallback strategies
- [ ] Idempotency in integrations

### 10. Industry Standards & Compliance
- [ ] GDPR data transfer requirements
- [ ] PCI-DSS for payment integrations
- [ ] HIPAA for healthcare integrations
- [ ] SOC 2 compliance for third-party integrations

## Configuration Notes

- Check items as the agent acquires or verifies knowledge in each domain.
- Add new domains or items as project requirements evolve.
