# Architecture Patterns & Best Practices Research
# Java Spring Cloud Microservices on Kubernetes (2025-2026)

**Research Date:** 2026-03-01
**Context:** AI Smart Grader — IA-REQ-001 Architecture Design
**Covers:** 7 key architecture domains for a 10-microservice education platform

---

## Table of Contents

1. [Spring Cloud Gateway Patterns](#1-spring-cloud-gateway-patterns)
2. [Spring AI Multi-LLM Integration Patterns](#2-spring-ai-multi-llm-integration-patterns)
3. [Nacos Configuration Hot-Reload](#3-nacos-configuration-hot-reload)
4. [Event-Driven Patterns with RabbitMQ](#4-event-driven-patterns-with-rabbitmq)
5. [Multi-Tenant Data Isolation with PostgreSQL](#5-multi-tenant-data-isolation-with-postgresql)
6. [RBAC Implementation with Spring Security](#6-rbac-implementation-with-spring-security)
7. [Redis Caching Strategies](#7-redis-caching-strategies)

---

## 1. Spring Cloud Gateway Patterns

### 1.1 Rate Limiting

**Pattern Name:** Token Bucket Rate Limiting (Redis-backed)

**Implementation Approach:**
Spring Cloud Gateway's built-in `RequestRateLimiter` filter uses Redis. For a 10-service architecture, apply tiered rate limiting: a global gateway-level limit plus per-route limits for expensive operations (e.g., AI grading).

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: ai-grading-service
          uri: lb://grading-service
          predicates:
            - Path=/api/v1/grading/**
          filters:
            - name: RequestRateLimiter
              args:
                redis-rate-limiter.replenishRate: 10    # 10 requests/second steady state
                redis-rate-limiter.burstCapacity: 20     # allow burst to 20
                redis-rate-limiter.requestedTokens: 1
                key-resolver: "#{@userKeyResolver}"      # rate limit per user
```

```java
@Configuration
public class RateLimiterConfig {
    @Bean
    public KeyResolver userKeyResolver() {
        return exchange -> Mono.justOrEmpty(
            exchange.getRequest().getHeaders().getFirst("X-User-Id"))
            .defaultIfEmpty("anonymous");
    }

    @Bean
    public KeyResolver apiKeyResolver() {
        return exchange -> Mono.just(
            exchange.getRequest().getPath().value());
    }
}
```

**For a 10-microservice architecture, apply layered rate limiting:**

| Layer | Scope | Tool | Purpose |
|:------|:------|:-----|:--------|
| Gateway global | All routes | Redis `RequestRateLimiter` | Protect against DDoS |
| Per-route | Expensive routes (AI grading) | Redis `RequestRateLimiter` with lower limits | Protect LLM API costs |
| Per-service | Service-level | Resilience4j `@RateLimiter` | Prevent single-service overload |
| Per-user tier | Free vs. paid users | Custom `KeyResolver` + Lua script | Enforce subscription quotas |

**Trade-offs:**
- Redis-backed: accurate across gateway replicas, adds Redis dependency and ~1ms latency per request
- In-memory (Resilience4j at service level): no network call, but per-instance only (inaccurate with multiple replicas)
- Recommendation: Use Redis at gateway for global/per-user limits; use Resilience4j at service for circuit-level protection

### 1.2 Circuit Breaker (Resilience4j)

**Pattern Name:** Circuit Breaker with Fallback + Bulkhead Isolation

**Implementation Approach:**
Use Spring Cloud CircuitBreaker with Resilience4j 2.2.0+. Each downstream service route gets its own circuit breaker instance.

```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: grading-service
          uri: lb://grading-service
          predicates:
            - Path=/api/v1/grading/**
          filters:
            - name: CircuitBreaker
              args:
                name: gradingServiceCB
                fallbackUri: forward:/fallback/grading

resilience4j:
  circuitbreaker:
    instances:
      gradingServiceCB:
        slidingWindowSize: 10
        slidingWindowType: COUNT_BASED
        minimumNumberOfCalls: 5
        failureRateThreshold: 50
        waitDurationInOpenState: 30s
        permittedNumberOfCallsInHalfOpenState: 3
        automaticTransitionFromOpenToHalfOpenEnabled: true
        registerHealthIndicator: true       # Exposes to K8s health probes
      userServiceCB:
        slidingWindowSize: 20
        failureRateThreshold: 40
        waitDurationInOpenState: 15s
  timelimiter:
    instances:
      gradingServiceCB:
        timeoutDuration: 30s               # AI grading may take longer
      userServiceCB:
        timeoutDuration: 5s
  bulkhead:
    instances:
      gradingServiceCB:
        maxConcurrentCalls: 50             # Limit concurrent AI calls
        maxWaitDuration: 500ms
```

```java
@RestController
public class FallbackController {
    @GetMapping("/fallback/grading")
    public Mono<ResponseEntity<ApiResponse>> gradingFallback() {
        return Mono.just(ResponseEntity
            .status(HttpStatus.SERVICE_UNAVAILABLE)
            .body(ApiResponse.error("GRADING_SERVICE_UNAVAILABLE",
                "Grading service is temporarily unavailable. Your request has been queued.")));
    }
}
```

**Best practice for 10 microservices:** Define a circuit breaker per downstream service with tuned thresholds. AI-dependent services (grading-service) need longer timeouts (30s) and lower concurrency limits. CRUD services (user-service) need shorter timeouts (5s) and higher concurrency.

**Critical rule:** Never use retry without circuit breaker. Retries without a circuit breaker can cause cascading failures and retry storms.

**Trade-offs:**
- COUNT_BASED sliding window: simpler, but bursts can open circuit prematurely
- TIME_BASED sliding window: better for variable-throughput services, more memory
- Bulkhead: prevents one slow service from consuming all gateway threads, but requires careful sizing

### 1.3 Request/Response Transformation

**Pattern Name:** Gateway Claim Injection (JWT Decomposition)

**Implementation Approach:**
Validate JWT at the gateway, extract claims, and inject them as headers for downstream services. This eliminates the need for each microservice to parse JWT.

```java
@Component
@Order(1)
public class JwtClaimInjectionFilter implements GlobalFilter {

    private final JwtDecoder jwtDecoder;

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        String authHeader = exchange.getRequest().getHeaders().getFirst("Authorization");
        if (authHeader != null && authHeader.startsWith("Bearer ")) {
            String token = authHeader.substring(7);
            try {
                Jwt jwt = jwtDecoder.decode(token);
                ServerHttpRequest mutatedRequest = exchange.getRequest().mutate()
                    .header("X-User-Id", jwt.getSubject())
                    .header("X-Tenant-Id", jwt.getClaimAsString("tenant_id"))
                    .header("X-User-Role", jwt.getClaimAsString("role"))
                    .header("X-School-Id", jwt.getClaimAsString("school_id"))
                    .build();
                return chain.filter(exchange.mutate().request(mutatedRequest).build());
            } catch (JwtException e) {
                exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
                return exchange.getResponse().setComplete();
            }
        }
        return chain.filter(exchange);
    }
}
```

**Downstream services then simply read headers:**
```java
@GetMapping("/students")
public List<StudentDTO> getStudents(
        @RequestHeader("X-User-Id") String userId,
        @RequestHeader("X-Tenant-Id") String tenantId,
        @RequestHeader("X-User-Role") String role) {
    // No JWT parsing needed here
}
```

**Trade-offs:**
- Pro: Eliminates redundant JWT parsing in every microservice, centralizes security
- Con: Downstream services must trust the gateway (internal network must be secured); if a service is called directly (bypassing gateway), headers are missing
- Mitigation: Use Kubernetes NetworkPolicy to ensure services are only reachable through the gateway

### 1.4 Authentication Filters

**Pattern Name:** Gateway as OAuth2 Resource Server + Route-Level Authorization

**Implementation Approach:**
Configure the gateway as an OAuth2 Resource Server that validates JWTs. Define public routes (login, registration) and protected routes with role requirements.

```java
@Configuration
@EnableWebFluxSecurity
public class GatewaySecurityConfig {

    @Bean
    public SecurityWebFilterChain securityFilterChain(ServerHttpSecurity http) {
        return http
            .csrf(ServerHttpSecurity.CsrfSpec::disable)
            .authorizeExchange(exchange -> exchange
                .pathMatchers("/api/v1/auth/**").permitAll()
                .pathMatchers("/api/v1/admin/**").hasRole("ADMIN")
                .pathMatchers("/api/v1/teacher/**").hasAnyRole("TEACHER", "ADMIN")
                .pathMatchers("/api/v1/parent/**").hasAnyRole("PARENT", "ADMIN")
                .pathMatchers("/api/v1/student/**").hasAnyRole("STUDENT", "PARENT", "TEACHER", "ADMIN")
                .anyExchange().authenticated()
            )
            .oauth2ResourceServer(oauth2 -> oauth2
                .jwt(jwt -> jwt.jwtAuthenticationConverter(jwtAuthConverter()))
            )
            .build();
    }

    @Bean
    public ReactiveJwtAuthenticationConverter jwtAuthConverter() {
        var converter = new ReactiveJwtAuthenticationConverter();
        converter.setJwtGrantedAuthoritiesConverter(jwt -> {
            List<String> roles = jwt.getClaimAsStringList("roles");
            return Flux.fromIterable(roles)
                .map(role -> new SimpleGrantedAuthority("ROLE_" + role));
        });
        return converter;
    }
}
```

**Trade-offs:**
- Gateway-level auth: Centralized, consistent; but coarse-grained (can only check roles, not data-level permissions)
- Service-level auth: Fine-grained (data-level); but duplicated across services
- Recommendation: Use both. Gateway enforces role-based route access; individual services enforce data-level access (e.g., "teacher sees own classes only")

### 1.5 WebSocket / SSE Proxying

**Pattern Name:** Protocol-Aware Gateway Routing

**WebSocket Configuration:**
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: websocket_route
          uri: lb:ws://notification-service
          predicates:
            - Path=/ws/notifications/**
        - id: sse_grading_route
          uri: lb://grading-service
          predicates:
            - Path=/api/v1/grading/stream/**
          metadata:
            response-timeout: 300000    # 5 min for long-running AI streams
            connect-timeout: 5000
```

**SSE Proxying Challenges and Mitigations:**

SSE proxying through Spring Cloud Gateway has known issues with response buffering. The gateway may batch SSE events rather than flushing them immediately. Mitigations:

1. Use the reactive (WebFlux-based) Spring Cloud Gateway, not the MVC variant
2. Set explicit streaming response headers
3. Consider disabling response buffering for SSE routes

```java
@Component
public class SseFlushFilter implements GlobalFilter, Ordered {
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        if (exchange.getRequest().getPath().value().contains("/stream/")) {
            exchange.getResponse().getHeaders()
                .set("X-Accel-Buffering", "no");           // Disable NGINX buffering
            exchange.getResponse().getHeaders()
                .set("Cache-Control", "no-cache");
        }
        return chain.filter(exchange);
    }

    @Override
    public int getOrder() { return -2; }
}
```

**For WeChat Mini Program (which does not support SSE natively):**
- Option A: Use `wx.request` with `enableChunked: true` for chunked transfer encoding
- Option B: Use WebSocket as a unified streaming transport for Mini Program
- Option C: Long-polling fallback with progressive result delivery

**Trade-offs:**
- SSE: Simpler, auto-reconnect, HTTP/2 multiplexing; but known buffering issues through gateway, not supported in WeChat Mini Program
- WebSocket: Full duplex, works everywhere; more complex, requires sticky sessions or external session store
- Recommendation: SSE for web/mobile app (through gateway with flush fix), WebSocket fallback for Mini Program

### 1.6 Gateway Configuration Best Practices for 10-Microservice Architecture

```yaml
spring:
  cloud:
    gateway:
      default-filters:
        - DedupeResponseHeader=Access-Control-Allow-Origin Access-Control-Allow-Credentials
        - AddResponseHeader=X-Response-Time, ${responseTime}
      globalcors:
        cors-configurations:
          '[/**]':
            allowedOrigins: "${CORS_ORIGINS}"
            allowedMethods: "*"
            allowedHeaders: "*"
            allowCredentials: true
      httpclient:
        connect-timeout: 5000
        response-timeout: 30s
        pool:
          type: ELASTIC
          max-idle-time: 15s
          max-connections: 500
```

**Filter execution order for a typical request:**
1. CORS filter (framework)
2. Rate limiter (global)
3. JWT validation + claim injection (custom global filter, order=1)
4. Route-specific circuit breaker
5. Load balancer
6. Request/response logging (custom, order=last)

---

## 2. Spring AI Multi-LLM Integration Patterns

### 2.1 Multi-Provider Architecture

**Pattern Name:** Provider-Agnostic ChatClient with Model Registry

**Implementation Approach:**
Spring AI 1.0+ (GA May 2025) and 1.1 (GA November 2025) provide a portable `ChatClient` API that abstracts LLM providers. Each provider is a separate starter dependency.

**Dependencies:**
```xml
<!-- OpenAI (GPT-4o for English subjects) -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-model-openai</artifactId>
</dependency>
<!-- Anthropic (Claude for complex reasoning) -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-model-anthropic</artifactId>
</dependency>
<!-- ZhiPu AI (GLM-4 for Chinese subjects) -->
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-model-zhipuai</artifactId>
</dependency>
```

**Configuration (Nacos-managed for hot-reload):**
```yaml
spring:
  ai:
    openai:
      api-key: ${OPENAI_API_KEY}
      chat:
        options:
          model: gpt-4o
          temperature: 0.3
    anthropic:
      api-key: ${ANTHROPIC_API_KEY}
      chat:
        options:
          model: claude-sonnet-4-20250514
          temperature: 0.3
    zhipuai:
      api-key: ${ZHIPUAI_API_KEY}
      chat:
        options:
          model: glm-4-air
          temperature: 0.3
```

**Model Registry and Router:**
```java
@Service
public class ModelRouter {

    private final Map<String, ChatModel> modelRegistry;

    public ModelRouter(
            @Qualifier("openAiChatModel") ChatModel openAi,
            @Qualifier("anthropicChatModel") ChatModel anthropic,
            @Qualifier("zhiPuAiChatModel") ChatModel zhiPu) {
        this.modelRegistry = Map.of(
            "openai", openAi,
            "anthropic", anthropic,
            "zhipuai", zhiPu
        );
    }

    public ChatModel route(GradingRequest request) {
        // Route by subject language affinity
        if (request.isChineseSubject()) {
            return modelRegistry.get("zhipuai");    // GLM excels at Chinese content
        }
        // Route by complexity
        if (request.estimatedComplexity() == Complexity.HIGH) {
            return modelRegistry.get("anthropic");   // Claude for complex reasoning
        }
        return modelRegistry.get("openai");          // Default: GPT-4o
    }

    public ChatModel fallback(String failedProvider) {
        // Fallback chain: zhipuai -> openai -> anthropic
        return switch (failedProvider) {
            case "zhipuai" -> modelRegistry.get("openai");
            case "openai" -> modelRegistry.get("anthropic");
            case "anthropic" -> modelRegistry.get("openai");
            default -> modelRegistry.get("openai");
        };
    }
}
```

### 2.2 Streaming SSE Responses with WebFlux

**Pattern Name:** Reactive SSE Streaming with Token Metadata

**Implementation Approach:**
Use `ChatClient.stream()` with `Flux<ChatResponse>` to stream AI responses and capture token usage metadata.

```java
@RestController
@RequestMapping("/api/v1/grading")
public class GradingController {

    private final ModelRouter modelRouter;
    private final TokenUsageTracker tokenTracker;

    @PostMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<GradingChunk>> streamGrading(
            @RequestBody GradingRequest request,
            @RequestHeader("X-User-Id") String userId,
            @RequestHeader("X-Tenant-Id") String tenantId) {

        ChatModel model = modelRouter.route(request);
        ChatClient client = ChatClient.builder(model).build();

        return client.prompt()
            .system(buildSystemPrompt(request.subject(), request.gradeLevel()))
            .user(buildUserPrompt(request))
            .stream()
            .chatResponse()
            .index()
            .map(tuple -> {
                long index = tuple.getT1();
                ChatResponse response = tuple.getT2();

                // Track token usage from the last chunk (which contains totals)
                if (response.getMetadata() != null && response.getMetadata().getUsage() != null) {
                    tokenTracker.record(userId, tenantId, model.getClass().getSimpleName(),
                        response.getMetadata().getUsage());
                }

                String content = response.getResult().getOutput().getText();
                return ServerSentEvent.<GradingChunk>builder()
                    .id(String.valueOf(index))
                    .event("grading-chunk")
                    .data(new GradingChunk(content, index == 0))
                    .build();
            })
            .onErrorResume(e -> {
                // Fallback to another provider on error
                ChatModel fallbackModel = modelRouter.fallback(
                    model.getClass().getSimpleName());
                return retryWithFallback(fallbackModel, request, userId, tenantId);
            })
            .concatWith(Mono.just(
                ServerSentEvent.<GradingChunk>builder()
                    .event("complete")
                    .data(new GradingChunk("[DONE]", false))
                    .build()
            ));
    }
}
```

### 2.3 Model Routing and Fallback Patterns

**Pattern Name:** Subject-Aware Model Routing with Cascading Fallback

**Routing Matrix:**

| Subject Type | Primary Model | Fallback 1 | Fallback 2 | Rationale |
|:-------------|:--------------|:-----------|:-----------|:----------|
| Chinese Language / Literature | ZhiPu GLM-4 | Qwen (via OpenAI-compatible API) | GPT-4o | Best Chinese language understanding |
| Math (elementary) | GPT-4o | ZhiPu GLM-4 | Claude | Good at structured reasoning |
| Math (advanced) | Claude | GPT-4o | ZhiPu GLM-4 | Best at complex multi-step reasoning |
| English | GPT-4o | Claude | ZhiPu GLM-4 | Native English proficiency |
| Science | Claude | GPT-4o | ZhiPu GLM-4 | Strong analytical reasoning |

**Fallback implementation with Resilience4j:**
```java
@Service
public class ResilientGradingService {

    @CircuitBreaker(name = "primaryModel", fallbackMethod = "gradeFallback")
    @Retry(name = "primaryModel", fallbackMethod = "gradeFallback")
    public Flux<ChatResponse> grade(GradingRequest request) {
        ChatModel primary = modelRouter.route(request);
        return ChatClient.builder(primary).build()
            .prompt()
            .system(buildPrompt(request))
            .user(request.content())
            .stream()
            .chatResponse();
    }

    public Flux<ChatResponse> gradeFallback(GradingRequest request, Throwable t) {
        log.warn("Primary model failed, using fallback: {}", t.getMessage());
        ChatModel fallback = modelRouter.fallback(request);
        return ChatClient.builder(fallback).build()
            .prompt()
            .system(buildPrompt(request))
            .user(request.content())
            .stream()
            .chatResponse();
    }
}
```

### 2.4 Token Usage Tracking

**Pattern Name:** AOP-Based Token Metering with Micrometer

**Implementation Approach:**
Spring AI 1.0+ exposes token usage via `ChatResponse.getMetadata().getUsage()`. Track input/output tokens per request, per tenant, per model.

```java
@Component
public class TokenUsageTracker {

    private final MeterRegistry meterRegistry;
    private final TokenUsageRepository tokenUsageRepo;

    public void record(String userId, String tenantId, String modelName, Usage usage) {
        // Micrometer metrics for real-time dashboards
        meterRegistry.counter("ai.tokens.prompt",
            "model", modelName, "tenant", tenantId)
            .increment(usage.getPromptTokens());
        meterRegistry.counter("ai.tokens.completion",
            "model", modelName, "tenant", tenantId)
            .increment(usage.getCompletionTokens());

        // Persist for billing and analytics
        tokenUsageRepo.save(TokenUsageRecord.builder()
            .userId(userId)
            .tenantId(tenantId)
            .model(modelName)
            .promptTokens(usage.getPromptTokens())
            .completionTokens(usage.getCompletionTokens())
            .totalTokens(usage.getTotalTokens())
            .estimatedCost(calculateCost(modelName, usage))
            .timestamp(Instant.now())
            .build());
    }

    private BigDecimal calculateCost(String modelName, Usage usage) {
        // Per-model pricing (configurable via Nacos)
        return switch (modelName) {
            case "OpenAiChatModel" -> usage.getPromptTokens()
                .multiply(new BigDecimal("0.000005"))
                .add(usage.getCompletionTokens()
                    .multiply(new BigDecimal("0.000015")));
            case "ZhiPuAiChatModel" -> usage.getPromptTokens()
                .multiply(new BigDecimal("0.000001"))
                .add(usage.getCompletionTokens()
                    .multiply(new BigDecimal("0.0000032")));
            // ... other models
            default -> BigDecimal.ZERO;
        };
    }
}
```

**Spring AI 1.1 enhancements for token tracking:**
- `prompt_tokens_details` tracking added for ZhiPuAI
- Usage field added to `ChatCompletionChunk` for streaming operations
- Prompt caching support for Anthropic Claude (up to 90% cost reduction)
- Dynamic tool discovery (34-64% token reduction)

**Trade-offs:**
- Per-request DB persistence: accurate billing, but adds write latency; mitigate with async writes or batch inserts
- Micrometer-only: low overhead, real-time; but no persistence for billing audits
- Recommendation: Both. Micrometer for dashboards, async DB writes for billing

### 2.5 Qwen Integration via OpenAI-Compatible API

Qwen (Alibaba) and many Chinese LLMs expose OpenAI-compatible APIs. Use Spring AI's OpenAI starter with a custom base URL:

```yaml
# Second OpenAI-compatible client for Qwen
qwen:
  api:
    base-url: https://dashscope.aliyuncs.com/compatible-mode/v1
    api-key: ${QWEN_API_KEY}
    model: qwen-plus
```

```java
@Configuration
public class QwenConfig {
    @Bean("qwenChatModel")
    public OpenAiChatModel qwenChatModel(
            @Value("${qwen.api.base-url}") String baseUrl,
            @Value("${qwen.api.api-key}") String apiKey,
            @Value("${qwen.api.model}") String model) {
        var api = new OpenAiApi(baseUrl, apiKey);
        var options = OpenAiChatOptions.builder().model(model).temperature(0.3).build();
        return new OpenAiChatModel(api, options);
    }
}
```

---

## 3. Nacos Configuration Hot-Reload

### 3.1 Namespace/Group Strategy for Multi-Tenant Configuration

**Pattern Name:** Environment-Namespace + Module-Group + Service-DataId

**Namespace Strategy (for environment isolation):**

| Namespace | Purpose | ID Pattern |
|:----------|:--------|:-----------|
| `dev` | Development environment | `ns-dev-xxxxx` |
| `test` | QA/Testing environment | `ns-test-xxxxx` |
| `staging` | Pre-production | `ns-staging-xxxxx` |
| `prod` | Production | `ns-prod-xxxxx` |

**Group Strategy (for module grouping within each namespace):**

| Group | Services | Example DataIds |
|:------|:---------|:----------------|
| `GATEWAY_GROUP` | gateway-service | `gateway-service.yml` |
| `AI_GROUP` | grading-service, error-notebook-service | `grading-service.yml`, `ai-model-config.yml` |
| `USER_GROUP` | user-service, auth-service | `user-service.yml`, `auth-config.yml` |
| `BUSINESS_GROUP` | subscription-service, payment-service, notification-service | `subscription-service.yml` |
| `COMMON_GROUP` | Shared configs | `common-redis.yml`, `common-rabbitmq.yml`, `common-datasource.yml` |

**Configuration:**
```yaml
# bootstrap.yml (or spring.config.import for newer versions)
spring:
  application:
    name: grading-service
  cloud:
    nacos:
      config:
        server-addr: ${NACOS_SERVER:localhost:8848}
        namespace: ${NACOS_NAMESPACE:ns-dev-xxxxx}
        group: AI_GROUP
        file-extension: yml
        # Shared configs loaded first, service-specific overrides
        shared-configs:
          - data-id: common-redis.yml
            group: COMMON_GROUP
            refresh: true
          - data-id: common-rabbitmq.yml
            group: COMMON_GROUP
            refresh: true
          - data-id: common-datasource.yml
            group: COMMON_GROUP
            refresh: true
        extension-configs:
          - data-id: ai-model-config.yml
            group: AI_GROUP
            refresh: true
```

**For Spring Cloud 2025.x**, use `spring.config.import` instead of bootstrap:
```yaml
spring:
  config:
    import:
      - optional:nacos:grading-service.yml?group=AI_GROUP&refreshEnabled=true
      - optional:nacos:common-redis.yml?group=COMMON_GROUP&refreshEnabled=true
      - optional:nacos:ai-model-config.yml?group=AI_GROUP&refreshEnabled=true
```

### 3.2 Managing 40+ Configurable Parameters

**Pattern Name:** Layered Configuration with Typed Config Beans

Organize 40+ parameters across multiple DataIds by domain:

| DataId | Group | Parameters | Example |
|:-------|:------|:-----------|:--------|
| `ai-model-config.yml` | AI_GROUP | Model selection, temperature, max tokens, pricing | `ai.grading.primary-model: glm-4-air` |
| `ai-prompt-templates.yml` | AI_GROUP | Prompt templates per subject/grade | `ai.prompts.math.elementary: "..."` |
| `grading-limits.yml` | AI_GROUP | Rate limits, tier quotas, timeout | `grading.free-tier.daily-limit: 20` |
| `subscription-tiers.yml` | BUSINESS_GROUP | Tier definitions, pricing, feature flags | `tiers.premium.error-notebook-limit: 5000` |
| `notification-config.yml` | BUSINESS_GROUP | Channel settings, templates, throttles | `notification.sms.daily-limit: 5` |
| `common-redis.yml` | COMMON_GROUP | Redis connection, pool, TTL defaults | `spring.data.redis.host: ...` |
| `common-rabbitmq.yml` | COMMON_GROUP | RabbitMQ connection, exchange config | `spring.rabbitmq.host: ...` |
| `feature-flags.yml` | COMMON_GROUP | Feature toggles for canary/A-B testing | `feature.new-grading-ui: false` |

**Hot-Reload with `@RefreshScope` and `@NacosConfig`:**

```java
// Traditional approach - @RefreshScope
@RefreshScope
@Component
@ConfigurationProperties(prefix = "ai.grading")
@Data
public class GradingConfig {
    private String primaryModel = "glm-4-air";
    private String fallbackModel = "gpt-4o";
    private double temperature = 0.3;
    private int maxTokens = 4096;
    private int freeTierDailyLimit = 20;
    private int premiumTierDailyLimit = 200;
    private Duration requestTimeout = Duration.ofSeconds(30);
}

// Newer approach - @NacosConfig (Spring Cloud Alibaba 2023.x+)
@Component
public class AiModelConfigListener {

    @NacosConfigListener(dataId = "ai-model-config.yml", group = "AI_GROUP")
    public void onConfigChange(String newConfig) {
        log.info("AI model config changed, reloading: {}", newConfig);
        // Custom handling: clear model caches, re-initialize clients, etc.
    }
}
```

### 3.3 Config Versioning and Rollback

**Pattern Name:** Nacos Built-in History + GitOps Sync

Nacos Server provides built-in configuration versioning:
- Every config change is stored with a version history (up to 30 days by default)
- Rollback to any previous version via Nacos Console
- Each version stores: content, MD5 hash, modification timestamp, operator

**Best practice: GitOps for config management:**
1. Store canonical configurations in Git repository
2. Use CI pipeline to push config changes to Nacos via Nacos Open API
3. Nacos stores runtime config + history
4. Git provides long-term audit trail; Nacos provides runtime delivery

```bash
# Push config to Nacos via API (in CI pipeline)
curl -X POST "http://nacos:8848/nacos/v1/cs/configs" \
  -d "dataId=grading-service.yml" \
  -d "group=AI_GROUP" \
  -d "tenant=ns-prod-xxxxx" \
  -d "content=$(cat configs/prod/grading-service.yml)" \
  -d "type=yaml"
```

**Nacos diagnostic logs to monitor:**

| Log Event | Meaning |
|:----------|:--------|
| `data-received` | App received push notification from Nacos |
| `notify-listener` | Nacos sent updated config to Spring listener |
| `notify-ok` | Listener callback completed successfully |
| `notify-error` | Listener callback threw exception |

**Trade-offs:**
- Nacos-only versioning: simple, built-in; but limited history (30 days), no merge/diff tooling
- Git + Nacos sync: full audit trail, review process; but adds complexity, potential drift between Git and Nacos
- Recommendation: Git as source of truth for config definitions; Nacos for runtime delivery and hot-reload

---

## 4. Event-Driven Patterns with RabbitMQ

### 4.1 Spring Cloud Stream Functional Model

**Pattern Name:** Functional Binding with Spring Cloud Stream

Spring Cloud Stream uses `Supplier`, `Function`, and `Consumer` beans as message handlers, with automatic binding generation.

```java
@Configuration
public class EventBindings {

    // Grading result event -> multiple consumers
    @Bean
    public Function<GradingCompletedEvent, ErrorNotebookEntryEvent> processGradingResult() {
        return event -> {
            if (event.hasErrors()) {
                return new ErrorNotebookEntryEvent(
                    event.userId(), event.errors(), event.subject(), event.knowledgePoints());
            }
            return null; // No errors, no downstream event
        };
    }

    // Error notebook entry -> notification trigger
    @Bean
    public Consumer<ErrorNotebookEntryEvent> triggerNotification() {
        return event -> {
            notificationService.sendErrorCollectedNotification(
                event.userId(), event.subject(), event.errorCount());
        };
    }
}
```

**Binding configuration:**
```yaml
spring:
  cloud:
    stream:
      function:
        definition: processGradingResult;triggerNotification
      bindings:
        processGradingResult-in-0:
          destination: grading-completed
          group: error-notebook-processor
        processGradingResult-out-0:
          destination: error-notebook-entry
        triggerNotification-in-0:
          destination: error-notebook-entry
          group: notification-trigger
      rabbit:
        bindings:
          processGradingResult-in-0:
            consumer:
              autoBindDlq: true
              republishToDlq: true
              maxAttempts: 3
              backOffInitialInterval: 1000
              backOffMaxInterval: 10000
              backOffMultiplier: 2.0
```

### 4.2 Event Flow: Grading -> Error Notebook -> Notification

**Pattern Name:** Event Notification Chain with DLQ Safety Net

**Event flow for AI Smart Grader:**

```
[grading-service]
    |
    | publishes: GradingCompletedEvent
    v
[grading-completed exchange] (topic)
    |
    +---> [error-notebook-service] Consumer
    |         |
    |         | publishes: ErrorNotebookEntryEvent (if errors found)
    |         v
    |     [error-notebook-entry exchange]
    |         |
    |         +---> [notification-service] Consumer
    |         |         |
    |         |         | publishes: NotificationRequestEvent
    |         |         v
    |         |     [notification-request exchange]
    |         |         |
    |         |         +---> [sms-worker]
    |         |         +---> [push-worker]
    |         |         +---> [email-worker]
    |         |
    |         +---> [analytics-service] Consumer (for real-time dashboards)
    |
    +---> [analytics-service] Consumer (for grading stats)
```

**Event DTOs:**
```java
public record GradingCompletedEvent(
    String gradingId,
    String userId,
    String tenantId,
    String subject,
    String gradeLevel,
    List<QuestionResult> results,
    boolean hasErrors,
    List<ErrorDetail> errors,
    TokenUsageSummary tokenUsage,
    Instant timestamp
) {}

public record ErrorNotebookEntryEvent(
    String userId,
    String tenantId,
    List<ErrorDetail> errors,
    String subject,
    List<String> knowledgePoints,
    Instant timestamp
) {}

public record NotificationRequestEvent(
    String userId,
    String tenantId,
    String notificationType,     // ERROR_COLLECTED, REVIEW_REMINDER, MASTERY_ACHIEVED
    Map<String, String> params,
    List<String> channels,       // IN_APP, PUSH, SMS, EMAIL
    Instant timestamp
) {}
```

### 4.3 Dead Letter Queue (DLQ) and Retry Strategy

**Pattern Name:** DLQ with Parking Lot Escalation

**Configuration for grading event processing:**
```yaml
spring:
  cloud:
    stream:
      rabbit:
        bindings:
          processGradingResult-in-0:
            consumer:
              autoBindDlq: true              # Auto-create .dlq queue
              republishToDlq: true           # Add exception details to DLQ message headers
              dlqTtl: 30000                  # Messages stay in DLQ for 30s before retry
              dlqDeadLetterExchange: ""       # Route expired DLQ messages back to original queue
              maxAttempts: 3                  # 3 binder-level retries first
              backOffInitialInterval: 1000
              backOffMaxInterval: 10000
              backOffMultiplier: 2.0
```

**DLQ-based async retry with parking lot:**
```java
@Component
public class DlqProcessor {

    private static final int MAX_DLQ_RETRIES = 3;

    @RabbitListener(queues = "grading-completed.error-notebook-processor.dlq")
    public void processDlq(Message failedMessage) {
        int retryCount = getRetryCount(failedMessage);

        if (retryCount >= MAX_DLQ_RETRIES) {
            // Move to parking lot for manual inspection
            rabbitTemplate.send("parking-lot-exchange", "grading-failed",
                failedMessage);
            log.error("Message moved to parking lot after {} retries: {}",
                retryCount, failedMessage.getMessageProperties().getMessageId());
            alertService.notifyOps("Grading event stuck in DLQ", failedMessage);
            return;
        }

        // Retry: republish to original queue with incremented retry count
        failedMessage.getMessageProperties().getHeaders()
            .put("x-retry-count", retryCount + 1);
        rabbitTemplate.send("grading-completed", "", failedMessage);
    }

    private int getRetryCount(Message message) {
        Object count = message.getMessageProperties().getHeaders().get("x-retry-count");
        return count == null ? 0 : (int) count;
    }
}
```

### 4.4 Saga Pattern for Multi-Step Grading Workflow

**Pattern Name:** Choreography-Based Saga with Compensating Events

For the AI grading workflow, use choreography (event-driven) saga rather than orchestration, since the flow is mostly linear:

```
1. ImageUploadedEvent
   -> grading-service: validate image, start grading
      -> (compensation: mark grading as FAILED if any step fails)

2. GradingCompletedEvent
   -> error-notebook-service: collect errors
      -> (compensation: remove error entries if grading result is invalidated)

3. ErrorNotebookEntryEvent
   -> notification-service: send notification
      -> (compensation: none needed, notifications are fire-and-forget)

4. GradingCompletedEvent
   -> subscription-service: decrement usage quota
      -> (compensation: increment quota back if grading is invalidated)

5. GradingCompletedEvent
   -> analytics-service: update statistics
      -> (compensation: recalculate statistics)
```

**Compensating event:**
```java
public record GradingInvalidatedEvent(
    String gradingId,
    String userId,
    String tenantId,
    String reason,    // DUPLICATE_SUBMISSION, CONTENT_MODERATION_FAILED, USER_CANCELLED
    Instant timestamp
) {}
```

### 4.5 Event Sourcing vs. Event Notification: Decision

**For AI Smart Grader, use Event Notification (not Event Sourcing):**

| Criteria | Event Notification | Event Sourcing |
|:---------|:-------------------|:---------------|
| Complexity | Lower | Higher (requires event store, replay, snapshots) |
| Audit trail | Via application logging + DB records | Complete event log as source of truth |
| Replay | Not supported | Full replay capability |
| Fit for this system | Grading results are immutable facts; no need for event replay | Overkill for a grading workflow |

**Exception:** Consider event sourcing for the analytics pipeline (grading stats, knowledge mastery tracking) where replaying events to rebuild read models is valuable. Use CQRS with a dedicated analytics read model updated by consuming `GradingCompletedEvent` messages.

**Trade-offs:**
- Event notification + DLQ: Simple, fits the grading workflow well; loses events if both queue and DLQ fail (mitigate with Transactional Outbox pattern)
- Event sourcing + CQRS: Complete audit trail, replay; adds significant complexity (event store, projectors, snapshots)
- Recommendation: Event notification for the main flow; CQRS read models for analytics only

---

## 5. Multi-Tenant Data Isolation with PostgreSQL

### 5.1 Strategy Selection: Row-Level Security (RLS)

**Pattern Name:** Shared Database + Row-Level Security with Session Variables

**For AI Smart Grader, use RLS (Row-Level Security) for the following reasons:**

| Strategy | Isolation | Ops Cost | Scale Limit | Query Complexity | Recommendation |
|:---------|:---------|:---------|:------------|:----------------|:---------------|
| Row-level (`tenant_id` column) | Medium | Low | High (thousands of tenants) | Low (auto-filtered) | Best for SaaS education platform |
| Schema-per-tenant | High | Medium | Medium (hundreds) | Medium | Better for enterprise with strict data requirements |
| Database-per-tenant | Highest | High | Low (dozens) | Low | Enterprise on-prem deployments only |

**Rationale for RLS:**
- Education platform may scale to thousands of schools (tenants)
- Shared indexes across all tenants (15 tables x 1 set of indexes vs. 15 x N)
- Schema migrations run once, not per-tenant
- Connection pooling works normally (no `SET search_path` switching)

### 5.2 PostgreSQL RLS Implementation

**Database setup:**
```sql
-- Enable RLS on all tenant-scoped tables
ALTER TABLE grading_results ENABLE ROW LEVEL SECURITY;
ALTER TABLE grading_results FORCE ROW LEVEL SECURITY;  -- Even table owner is filtered

-- Create RLS policy
CREATE POLICY tenant_isolation ON grading_results
    USING (tenant_id = current_setting('app.tenant_id')::uuid);

-- Apply to all tenant tables
DO $$
DECLARE
    t text;
BEGIN
    FOR t IN
        SELECT tablename FROM pg_tables
        WHERE schemaname = 'public' AND tablename IN (
            'users', 'students', 'classes', 'grading_results',
            'error_notebook_entries', 'subscriptions', 'knowledge_points',
            'notifications', 'analytics_snapshots'
        )
    LOOP
        EXECUTE format('ALTER TABLE %I ENABLE ROW LEVEL SECURITY', t);
        EXECUTE format('ALTER TABLE %I FORCE ROW LEVEL SECURITY', t);
        EXECUTE format(
            'CREATE POLICY tenant_isolation ON %I USING (tenant_id = current_setting(''app.tenant_id'')::uuid)',
            t
        );
    END LOOP;
END $$;
```

### 5.3 Spring Data JPA Integration

**Pattern Name:** Hibernate Filter + AOP + ThreadLocal Tenant Context

**TenantContext (ThreadLocal):**
```java
public class TenantContext {
    private static final InheritableThreadLocal<String> TENANT_ID =
        new InheritableThreadLocal<>();

    public static void setTenantId(String tenantId) {
        TENANT_ID.set(tenantId);
    }

    public static String getTenantId() {
        return TENANT_ID.get();
    }

    public static void clear() {
        TENANT_ID.remove();
    }
}
```

**HTTP Interceptor (extracts tenant from JWT via gateway header):**
```java
@Component
public class TenantInterceptor implements HandlerInterceptor {

    @Override
    public boolean preHandle(HttpServletRequest request,
                             HttpServletResponse response,
                             Object handler) {
        String tenantId = request.getHeader("X-Tenant-Id");
        if (tenantId == null || tenantId.isBlank()) {
            response.setStatus(HttpStatus.BAD_REQUEST.value());
            return false;
        }
        TenantContext.setTenantId(tenantId);
        return true;
    }

    @Override
    public void afterCompletion(HttpServletRequest request,
                                HttpServletResponse response,
                                Object handler, Exception ex) {
        TenantContext.clear(); // CRITICAL: always clear to prevent leakage in connection pool
    }
}
```

**Connection-level tenant setting (for RLS):**
```java
@Component
public class TenantConnectionCustomizer implements ConnectionCustomizer {

    @Aspect
    @Component
    public static class TenantDataSourceAspect {

        @Autowired
        private DataSource dataSource;

        @Before("execution(* org.springframework.data.jpa.repository.JpaRepository+.*(..))")
        public void setTenantBeforeQuery(JoinPoint jp) {
            String tenantId = TenantContext.getTenantId();
            if (tenantId != null) {
                try (var conn = DataSourceUtils.getConnection(dataSource);
                     var stmt = conn.createStatement()) {
                    stmt.execute("SET app.tenant_id = '" + tenantId + "'");
                } catch (SQLException e) {
                    throw new TenantConfigurationException("Failed to set tenant context", e);
                }
            }
        }
    }
}
```

**Alternative: Hibernate @Filter approach (application-level filtering, works without PostgreSQL RLS):**
```java
@Entity
@Table(name = "grading_results")
@FilterDef(name = "tenantFilter",
    parameters = @ParamDef(name = "tenantId", type = String.class))
@Filter(name = "tenantFilter", condition = "tenant_id = :tenantId")
public class GradingResult {
    @Id
    private UUID id;

    @Column(name = "tenant_id", nullable = false)
    private UUID tenantId;

    // ... other fields
}

@Aspect
@Component
public class TenantFilterAspect {

    @PersistenceContext
    private EntityManager entityManager;

    @Before("execution(* com.smartgrader.*.repository.*.*(..))")
    public void enableTenantFilter() {
        Session session = entityManager.unwrap(Session.class);
        session.enableFilter("tenantFilter")
            .setParameter("tenantId", TenantContext.getTenantId());
    }
}
```

### 5.4 Connection Pooling Strategy

**Pattern Name:** HikariCP with Tenant-Aware Connection Initialization

```yaml
spring:
  datasource:
    hikari:
      maximum-pool-size: 20           # Per-service pool
      minimum-idle: 5
      connection-init-sql: "SET app.tenant_id = ''"  # Initialize with empty tenant
      connection-timeout: 30000
      idle-timeout: 600000
      max-lifetime: 1800000
```

**Critical rule:** Always reset `app.tenant_id` after each request in a `finally` block or interceptor `afterCompletion`. Failure to do so will serve the wrong tenant's data to the next request using the pooled connection.

**Trade-offs:**
- PostgreSQL RLS + session variables: strongest isolation (database-enforced), works with raw SQL and JPA; but requires careful connection pool management
- Hibernate @Filter only: application-level, easier setup; but can be bypassed by native queries, less secure
- Both together (defense in depth): Hibernate filter for JPA queries + PostgreSQL RLS for native queries and direct DB access; adds slight overhead but provides strongest guarantee
- Recommendation: Use both for defense-in-depth. Hibernate filter handles JPA; PostgreSQL RLS catches everything else.

---

## 6. RBAC Implementation with Spring Security

### 6.1 Three-Layer Access Control Architecture

**Pattern Name:** API-Level + Menu-Level + Data-Level RBAC

| Layer | Enforcement Point | Mechanism | Example |
|:------|:-----------------|:----------|:--------|
| API-Level | Gateway + Controller | `@PreAuthorize`, route-level security | Only TEACHER can access `/api/v1/grading/batch` |
| Menu-Level | Frontend (informed by backend) | Permissions in JWT / permissions API | Teacher sees "Class Management" menu; Parent does not |
| Data-Level | Service/Repository | JPA Specifications, Hibernate Filters | Teacher sees only their assigned classes' students |

### 6.2 JWT Claims Structure

**Pattern Name:** Role + Permission + Scope JWT Claims

```json
{
  "sub": "user-uuid-12345",
  "iss": "smartgrader-auth",
  "iat": 1709251200,
  "exp": 1709337600,
  "tenant_id": "school-uuid-67890",
  "roles": ["TEACHER"],
  "permissions": [
    "grading:submit",
    "grading:view",
    "class:view",
    "class:manage",
    "student:view",
    "error-notebook:view",
    "analytics:class-view",
    "notification:send"
  ],
  "scope": {
    "school_id": "school-uuid-67890",
    "class_ids": ["class-a-uuid", "class-b-uuid"],
    "subject_ids": ["math", "chinese"]
  }
}
```

**Role-to-permission mapping:**

| Role | Permissions | Data Scope |
|:-----|:-----------|:-----------|
| SUPER_ADMIN | `*` (all) | All tenants |
| SCHOOL_ADMIN | `user:manage`, `class:manage`, `analytics:school-view`, `subscription:manage` | Own school only |
| TEACHER | `grading:submit`, `grading:view`, `class:view`, `student:view`, `error-notebook:view`, `analytics:class-view` | Own assigned classes + subjects only |
| PARENT | `grading:view`, `error-notebook:view`, `student:view`, `subscription:view` | Own children only |
| STUDENT | `grading:submit`, `grading:view`, `error-notebook:view` | Own data only |

### 6.3 API-Level Access Control

**Implementation with `@PreAuthorize`:**
```java
@RestController
@RequestMapping("/api/v1/grading")
public class GradingController {

    @PostMapping("/submit")
    @PreAuthorize("hasAnyRole('TEACHER', 'STUDENT', 'PARENT')")
    public Mono<GradingResponse> submitGrading(@RequestBody GradingRequest request) {
        // ...
    }

    @GetMapping("/batch-report")
    @PreAuthorize("hasRole('TEACHER') and hasAuthority('analytics:class-view')")
    public Mono<BatchReport> getBatchReport(@RequestParam String classId) {
        // Data-level check happens in service layer
    }

    @DeleteMapping("/results/{id}")
    @PreAuthorize("hasRole('SCHOOL_ADMIN') or hasRole('SUPER_ADMIN')")
    public Mono<Void> deleteResult(@PathVariable String id) {
        // ...
    }
}
```

### 6.4 Data-Level Access Control: "Teacher Sees Own Classes Only"

**Pattern Name:** JPA Specification + Security Context Filtering

```java
@Service
public class StudentService {

    private final StudentRepository studentRepo;

    public Page<StudentDTO> getStudents(String classId, Pageable pageable) {
        SecurityUser currentUser = SecurityContextHolder.getContext()
            .getAuthentication().getPrincipal();

        return switch (currentUser.getRole()) {
            case SUPER_ADMIN, SCHOOL_ADMIN ->
                studentRepo.findByTenantId(currentUser.getTenantId(), pageable);
            case TEACHER -> {
                // Verify teacher is assigned to this class
                if (!currentUser.getClassIds().contains(classId)) {
                    throw new AccessDeniedException("Not assigned to class: " + classId);
                }
                yield studentRepo.findByClassId(classId, pageable);
            }
            case PARENT ->
                studentRepo.findByParentId(currentUser.getUserId(), pageable);
            case STUDENT ->
                studentRepo.findById(currentUser.getUserId())
                    .map(s -> new PageImpl<>(List.of(s)))
                    .orElseThrow();
        };
    }
}
```

**Generic Specification approach for reusable data filtering:**
```java
public class DataScopeSpecification<T> implements Specification<T> {

    private final SecurityUser user;

    @Override
    public Predicate toPredicate(Root<T> root, CriteriaQuery<?> query,
                                  CriteriaBuilder cb) {
        List<Predicate> predicates = new ArrayList<>();

        // Tenant isolation (always applied)
        predicates.add(cb.equal(root.get("tenantId"), user.getTenantId()));

        // Role-based data scoping
        switch (user.getRole()) {
            case TEACHER -> {
                if (root.getModel().getAttributes().stream()
                        .anyMatch(a -> a.getName().equals("classId"))) {
                    predicates.add(root.get("classId").in(user.getClassIds()));
                }
            }
            case PARENT -> {
                if (root.getModel().getAttributes().stream()
                        .anyMatch(a -> a.getName().equals("studentId"))) {
                    predicates.add(root.get("studentId").in(user.getChildStudentIds()));
                }
            }
            case STUDENT -> {
                predicates.add(cb.equal(root.get("userId"), user.getUserId()));
            }
            // ADMIN roles: tenant filter only
        }

        return cb.and(predicates.toArray(new Predicate[0]));
    }
}
```

### 6.5 Menu-Level Access Control

**Pattern Name:** Permission-Based UI Rendering via API

The backend provides the user's menu permissions. The frontend renders menus accordingly.

```java
@GetMapping("/api/v1/auth/menu-permissions")
public MenuPermissions getMenuPermissions() {
    SecurityUser user = getCurrentUser();
    return MenuPermissions.builder()
        .menus(menuService.getVisibleMenus(user.getPermissions()))
        .buttons(buttonService.getVisibleButtons(user.getPermissions()))
        .build();
}
```

**Menu permission mapping (stored in database or config):**

| Menu Item | Required Permission | Visible To |
|:----------|:-------------------|:-----------|
| Dashboard | `dashboard:view` | All |
| Class Management | `class:manage` | ADMIN, TEACHER |
| AI Grading | `grading:submit` | TEACHER, STUDENT, PARENT |
| Error Notebook | `error-notebook:view` | TEACHER, STUDENT, PARENT |
| User Management | `user:manage` | ADMIN |
| Subscription & Billing | `subscription:manage` | ADMIN |
| Analytics - School | `analytics:school-view` | ADMIN |
| Analytics - Class | `analytics:class-view` | TEACHER |
| System Config | `system:config` | SUPER_ADMIN |

**Trade-offs:**
- JWT-embedded permissions: No DB lookup needed, fast; but JWT grows large with many permissions, hard to revoke mid-session
- Permission API + Redis cache: Permissions can change in real-time; but requires API call or cache lookup
- Recommendation: Embed roles + core permissions in JWT (kept small); fetch detailed menu/button permissions from API (cached in Redis with 5-min TTL)

---

## 7. Redis Caching Strategies

### 7.1 Cache-Aside for AI Grading Results

**Pattern Name:** Cache-Aside with Image Hash Key

**Implementation:**
```java
@Service
public class GradingCacheService {

    private final StringRedisTemplate redisTemplate;
    private final ObjectMapper objectMapper;
    private static final Duration GRADING_CACHE_TTL = Duration.ofHours(24);

    // Key format: grading:{tenant_id}:{image_hash}:{subject}
    private String cacheKey(String tenantId, String imageHash, String subject) {
        return String.format("grading:%s:%s:%s", tenantId, imageHash, subject);
    }

    public Optional<GradingResult> getCachedResult(String tenantId,
                                                     String imageHash,
                                                     String subject) {
        String key = cacheKey(tenantId, imageHash, subject);
        String cached = redisTemplate.opsForValue().get(key);
        if (cached != null) {
            return Optional.of(objectMapper.readValue(cached, GradingResult.class));
        }
        return Optional.empty();
    }

    public void cacheResult(String tenantId, String imageHash,
                            String subject, GradingResult result) {
        String key = cacheKey(tenantId, imageHash, subject);
        redisTemplate.opsForValue().set(key,
            objectMapper.writeValueAsString(result),
            GRADING_CACHE_TTL);
    }
}
```

**Why cache-aside (not write-through) for grading results:**
- Grading results are immutable once created (AI output does not change for the same input)
- Not all results need to be cached (only frequently accessed recent results)
- Cache miss cost is high (LLM API call), so even low hit rates provide value
- Write-through would cache every result, wasting Redis memory on rarely accessed old results

### 7.2 Image Hash-Based Deduplication

**Pattern Name:** Perceptual Hash + Exact Hash Dual Strategy

```java
@Service
public class ImageDeduplicationService {

    private final StringRedisTemplate redisTemplate;
    private static final Duration DEDUP_TTL = Duration.ofHours(1);

    /**
     * Two-level deduplication:
     * Level 1: Exact hash (SHA-256) - catches identical re-uploads
     * Level 2: Perceptual hash (pHash) - catches re-photographed same page
     */
    public DeduplicationResult checkDuplicate(String tenantId, byte[] imageBytes) {
        // Level 1: Exact hash
        String exactHash = DigestUtils.sha256Hex(imageBytes);
        String exactKey = String.format("dedup:exact:%s:%s", tenantId, exactHash);

        String existingGradingId = redisTemplate.opsForValue().get(exactKey);
        if (existingGradingId != null) {
            return DeduplicationResult.exactMatch(existingGradingId);
        }

        // Level 2: Perceptual hash (using a library like JImageHash)
        String pHash = perceptualHash(imageBytes);
        String pHashKey = String.format("dedup:phash:%s:%s", tenantId, pHash);

        existingGradingId = redisTemplate.opsForValue().get(pHashKey);
        if (existingGradingId != null) {
            return DeduplicationResult.perceptualMatch(existingGradingId);
        }

        return DeduplicationResult.noMatch();
    }

    public void registerImage(String tenantId, byte[] imageBytes, String gradingId) {
        String exactHash = DigestUtils.sha256Hex(imageBytes);
        String pHash = perceptualHash(imageBytes);

        redisTemplate.opsForValue().set(
            String.format("dedup:exact:%s:%s", tenantId, exactHash),
            gradingId, DEDUP_TTL);
        redisTemplate.opsForValue().set(
            String.format("dedup:phash:%s:%s", tenantId, pHash),
            gradingId, DEDUP_TTL);
    }

    private String perceptualHash(byte[] imageBytes) {
        // Use JImageHash library for perceptual hashing
        BufferedImage img = ImageIO.read(new ByteArrayInputStream(imageBytes));
        HashingAlgorithm hasher = new PerceptiveHash(64);
        return hasher.hash(img).toHexString();
    }
}
```

**Trade-offs:**
- Exact hash only: simple, fast; misses re-photographed pages
- Perceptual hash only: catches similar images; more expensive to compute, may produce false positives
- Both (recommended): dual check maximizes dedup rate; 2x Redis storage, perceptual hash computation adds ~50ms

### 7.3 Session Management

**Pattern Name:** Redis-Backed Spring Session with Tenant Isolation

```yaml
spring:
  session:
    store-type: redis
    timeout: 1800                    # 30 minutes
    redis:
      namespace: smartgrader:session  # Isolate session keys
```

For a stateless JWT-based architecture, Spring Session is primarily used for:
- Storing refresh tokens securely (not in client storage)
- Rate limiting state
- Temporary workflow state (e.g., multi-step grading upload)

**Recommendation for AI Smart Grader:** Use stateless JWT for authentication (no server-side session). Use Redis only for refresh token storage and temporary state.

```java
@Service
public class RefreshTokenService {

    private final StringRedisTemplate redisTemplate;
    private static final Duration REFRESH_TOKEN_TTL = Duration.ofDays(7);

    public void storeRefreshToken(String userId, String refreshToken) {
        String key = "refresh:" + userId;
        redisTemplate.opsForValue().set(key, refreshToken, REFRESH_TOKEN_TTL);
    }

    public boolean validateRefreshToken(String userId, String refreshToken) {
        String stored = redisTemplate.opsForValue().get("refresh:" + userId);
        return refreshToken.equals(stored);
    }

    public void revokeRefreshToken(String userId) {
        redisTemplate.delete("refresh:" + userId);
    }
}
```

### 7.4 Rate Limiting with Redis

**Pattern Name:** Sliding Window Rate Limiter with Lua Script

```java
@Service
public class RedisRateLimiter {

    private final StringRedisTemplate redisTemplate;

    private static final String RATE_LIMIT_SCRIPT = """
        local key = KEYS[1]
        local limit = tonumber(ARGV[1])
        local window = tonumber(ARGV[2])
        local now = tonumber(ARGV[3])

        -- Remove old entries outside the window
        redis.call('ZREMRANGEBYSCORE', key, 0, now - window)

        -- Count current entries
        local count = redis.call('ZCARD', key)

        if count < limit then
            -- Add current request
            redis.call('ZADD', key, now, now .. '-' .. math.random(100000))
            redis.call('EXPIRE', key, window)
            return 1  -- allowed
        else
            return 0  -- rejected
        end
        """;

    /**
     * Check if request is within rate limit.
     * Uses sorted set with timestamp scores for sliding window.
     */
    public boolean isAllowed(String userId, String action, int limit, Duration window) {
        String key = String.format("ratelimit:%s:%s", userId, action);
        long now = Instant.now().toEpochMilli();

        DefaultRedisScript<Long> script = new DefaultRedisScript<>(RATE_LIMIT_SCRIPT, Long.class);
        Long result = redisTemplate.execute(script,
            List.of(key),
            String.valueOf(limit),
            String.valueOf(window.toMillis()),
            String.valueOf(now));

        return result != null && result == 1;
    }
}
```

**Rate limit tiers for AI Smart Grader:**

| Action | Free Tier | Premium Tier | Implementation |
|:-------|:----------|:-------------|:---------------|
| AI grading submissions | 20/day | 200/day | Sliding window (24h) |
| Image uploads | 5/minute | 20/minute | Sliding window (60s) |
| API calls (general) | 100/minute | 1000/minute | Gateway Redis rate limiter |
| Error notebook exports | 5/day | Unlimited | Sliding window (24h) |

### 7.5 Distributed Locking with Redisson

**Pattern Name:** Redisson RLock for Concurrent Grading Prevention

```java
@Service
public class GradingLockService {

    private final RedissonClient redissonClient;

    /**
     * Prevent duplicate grading of the same image by the same user.
     * Uses distributed lock to ensure only one grading process runs per image.
     */
    public <T> T executeWithLock(String lockKey, Duration waitTime,
                                  Duration leaseTime, Supplier<T> action) {
        RLock lock = redissonClient.getLock("lock:grading:" + lockKey);
        boolean acquired = false;

        try {
            acquired = lock.tryLock(waitTime.toMillis(), leaseTime.toMillis(),
                TimeUnit.MILLISECONDS);
            if (!acquired) {
                throw new ConcurrentGradingException(
                    "Another grading process is running for this image");
            }
            return action.get();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new GradingException("Lock acquisition interrupted", e);
        } finally {
            if (acquired && lock.isHeldByCurrentThread()) {
                lock.unlock();
            }
        }
    }
}

// Usage in grading service:
@Service
public class GradingService {

    @Autowired
    private GradingLockService lockService;

    public GradingResult gradeImage(String userId, String imageHash, byte[] image) {
        String lockKey = userId + ":" + imageHash;

        return lockService.executeWithLock(lockKey,
            Duration.ofSeconds(5),     // Wait up to 5s for lock
            Duration.ofSeconds(60),    // Lock auto-expires after 60s (safety)
            () -> {
                // Check cache first
                // If miss, call LLM
                // Cache result
                // Publish event
                return performGrading(userId, imageHash, image);
            });
    }
}
```

**Redisson vs. Spring Data Redis locks:**
- Redisson RLock: automatic renewal (watchdog), fair locks, read/write locks, Pub/Sub notification on release (no polling)
- Spring Data Redis `RedisCacheWriter` lock: simpler, built-in; but cache-level locking only, no fine-grained control
- Recommendation: Use Redisson for application-level distributed locks (grading dedup, quota updates); use Spring Data Redis for cache operations

### 7.6 Redis Key Namespace Strategy

**All Redis keys should follow a consistent naming convention:**

| Prefix | Purpose | Example | TTL |
|:-------|:--------|:--------|:----|
| `grading:{tenant}:{hash}:{subject}` | Grading result cache | `grading:school1:abc123:math` | 24h |
| `dedup:exact:{tenant}:{hash}` | Exact image dedup | `dedup:exact:school1:sha256hash` | 1h |
| `dedup:phash:{tenant}:{hash}` | Perceptual image dedup | `dedup:phash:school1:phash64` | 1h |
| `ratelimit:{user}:{action}` | Rate limiting | `ratelimit:user1:grading` | Window size |
| `lock:grading:{key}` | Distributed lock | `lock:grading:user1:abc123` | 60s |
| `refresh:{user}` | Refresh token | `refresh:user1` | 7d |
| `menu-perm:{user}` | Menu permissions cache | `menu-perm:user1` | 5min |
| `token-usage:{tenant}:{date}` | Daily token usage counter | `token-usage:school1:2026-03-01` | 48h |
| `session:{id}` | Spring Session (if used) | `session:abc-def-123` | 30min |

---

## Cross-Cutting Concerns Summary

### Pattern Interaction Map

```
[Client Request]
    |
    v
[Spring Cloud Gateway]
    |- JWT validation (Section 1.4)
    |- Rate limiting via Redis (Section 7.4)
    |- Circuit breaker (Section 1.2)
    |- Claim injection to headers (Section 1.3)
    |
    v
[Microservice]
    |- Tenant context from header (Section 5.3)
    |- RBAC check via @PreAuthorize (Section 6.3)
    |- Data-level filtering via JPA Spec (Section 6.4)
    |- PostgreSQL RLS enforced (Section 5.2)
    |- Redis cache check (Section 7.1)
    |- Distributed lock (Section 7.5)
    |- AI model routing (Section 2.3)
    |- SSE streaming response (Section 2.2)
    |
    v
[Event Publication via RabbitMQ]
    |- GradingCompletedEvent (Section 4.2)
    |- DLQ + retry (Section 4.3)
    |- Saga compensation (Section 4.4)
    |
    v
[Nacos Hot-Reload]
    |- Model config changes (Section 3.2)
    |- Rate limit tuning (Section 3.2)
    |- Feature flags (Section 3.2)
```

### Technology Version Matrix (2025-2026)

| Component | Recommended Version | Notes |
|:----------|:-------------------|:------|
| Spring Boot | 3.5.x | Latest stable for Spring Cloud 2025 |
| Spring Cloud | 2025.1.x | Compatible with Boot 3.5 |
| Spring AI | 1.1.x | GA November 2025, ZhiPu + Anthropic support |
| Spring Cloud Alibaba | 2025.0.0.x | For Nacos integration |
| Resilience4j | 2.2.0+ | Spring Boot 3 compatible |
| Nacos Server | 2.4.x or 3.x | 3.x adds MCP/A2A support |
| Redisson | 3.35.0+ | Spring Boot 3 starter |
| PostgreSQL | 16+ | RLS improvements |
| RabbitMQ | 4.x | Quorum queues, streams |
| Kubernetes | 1.30+ | 2025 stable |

---

## Sources

### Spring Cloud Gateway & Resilience4j
- [Spring Cloud Gateway Workshop - Resilience Lab](https://andifalk.gitbook.io/spring-cloud-gateway-workshop/hands-on-labs/lab2)
- [Resilience4j Circuit Breakers in Spring Boot 3](https://www.javacodegeeks.com/2025/06/resilience4j-circuit-breakers-in-spring-boot-3.html)
- [Building Resilient Systems: Circuit Breakers and Retry Patterns (2026)](https://dasroot.net/posts/2026/01/building-resilient-systems-circuit-breakers-retry-patterns/)
- [How to Build Circuit Breaker with Resilience4j (2026)](https://oneuptime.com/blog/post/2026-01-30-spring-resilience4j-circuit-breaker/view)
- [Spring Cloud Gateway Workshop - JWT Authentication](https://andifalk.gitbook.io/spring-cloud-gateway-workshop/hands-on-labs/lab3)
- [Spring Cloud Gateway JWT Security](https://medium.com/@rajithgama/spring-cloud-gateway-security-with-jwt-23045ba59b8a)
- [Gateway SSE Issue #1550](https://github.com/spring-cloud/spring-cloud-gateway/issues/1550)
- [Gateway SSE Issue #3833](https://github.com/spring-cloud/spring-cloud-gateway/issues/3833)

### Spring AI
- [Spring AI 1.1 GA Release](https://spring.io/blog/2025/11/12/spring-ai-1-1-GA-released/)
- [Spring AI 1.0 GA Release](https://spring.io/blog/2025/05/20/spring-ai-1-0-GA-released/)
- [ZhiPu AI Chat - Spring AI Reference](https://docs.spring.io/spring-ai/reference/api/chat/zhipuai-chat.html)
- [Spring AI ChatClient API Reference](https://docs.spring.io/spring-ai/reference/api/chatclient.html)
- [Streaming Chat Response in Spring AI (Baeldung)](https://www.baeldung.com/spring-ai-chatclient-stream-response)
- [Spring AI Streaming Response Guide (BootcampToProd)](https://bootcamptoprod.com/spring-ai-streaming-response-guide/)
- [Spring AI Tool Search - 34-64% Token Savings](https://spring.io/blog/2025/12/11/spring-ai-tool-search-tools-tzolov/)
- [Spring AI Agentic Patterns - A2A Protocol](https://spring.io/blog/2026/01/29/spring-ai-agentic-patterns-a2a-integration/)

### Nacos Configuration
- [Nacos Config Best Practices with Spring Cloud and KMS](https://www.alibabacloud.com/blog/best-practices-for-dynamic-configuration-with-spring-cloud-nacos-and-kms_601998)
- [Nacos Config - Spring Cloud Alibaba Wiki](https://github.com/alibaba/spring-cloud-alibaba/wiki/Nacos-config-en)
- [Nacos Configuration Center Advanced Guide](https://sca.aliyun.com/en/docs/2023/user-guide/nacos/advanced-guide/)
- [Nacos Config Annotations for Spring Cloud](https://www.alibabacloud.com/blog/annotations-for-nacos-configuration-center-in-spring-cloud-applications_602093)
- [Multi-Configuration Pulling with Nacos in Spring Boot](https://www.oreateai.com/blog/a-complete-practical-guide-to-implementing-multiconfiguration-pulling-with-nacos-in-spring-boot-projects/408405cd46036b89ed0a9e84415dd20b)

### Event-Driven / RabbitMQ
- [Spring Cloud Stream DLQ Processing](https://docs.spring.io/spring-cloud-stream/reference/rabbit/rabbit_dlq.html)
- [Spring Cloud Stream RabbitMQ Retry](https://docs.spring.io/spring-cloud-stream/reference/rabbit/rabbit_overview/rabbitmq-retry.html)
- [Spring Cloud Stream - Event-Driven Microservices (2026)](https://oneuptime.com/blog/post/2026-01-25-event-driven-microservices-spring-cloud-stream/view)
- [Spring Cloud Stream for Real-Time Event-Driven Systems](https://foojay.io/today/spring-cloud-stream-event-driven-architecture-part-1/)
- [Event Architecture with Spring Cloud Stream](https://dev.to/lucasnscr/event-architecture-with-spring-cloud-stream-k9l)
- [Spring Cloud Stream Functional + Reactive](https://spring.io/blog/2019/10/17/spring-cloud-stream-functional-and-reactive/)

### Multi-Tenancy / PostgreSQL
- [AWS - Multi-Tenant Data Isolation with PostgreSQL RLS](https://aws.amazon.com/blogs/database/multi-tenant-data-isolation-with-postgresql-row-level-security/)
- [Spring Boot Multi-Tenancy with PostgreSQL RLS](https://www.bytefish.de/blog/spring_boot_multitenancy_using_rls.html)
- [PostgreSQL RLS with Spring Boot 3 (Medium)](https://medium.com/@priyaranjanpatraa/multi-tenant-the-safe-way-postgresql-row-level-security-rls-with-spring-boot-3-4132a4d142fa)
- [Crunchy Data - RLS for Tenants in Postgres](https://www.crunchydata.com/blog/row-level-security-for-tenants-in-postgres)
- [Multitenancy with Spring Data JPA (Baeldung)](https://www.baeldung.com/multitenancy-with-spring-data-jpa)
- [Hibernate Filters + Spring Aspects for Data Isolation (2025)](https://rajind.dev/2025/07/09/hibernate-filters-coupled-with-spring-aspects-for-data-isolation/)
- [Callista Enterprise - Multi-Tenancy with Hibernate Filters](https://callistaenterprise.se/blogg/teknik/2020/10/17/multi-tenancy-with-spring-boot-part5/)

### RBAC / Spring Security
- [Role-Based Access Control in Spring Boot 3](https://blog.tericcabrel.com/role-base-access-control-spring-boot/)
- [JWT Authentication & RBAC - Clean Architecture (2025)](https://medium.com/@ahraval11/jwt-authentication-rbac-in-spring-boot-a-clean-architecture-with-real-request-flow-88adfb3aa846)
- [Spring Security - Role and Permission Based Access Control](https://www.geeksforgeeks.org/java/spring-security-role-based-and-permission-based-access-control/)
- [Auth0 - Spring Boot RBAC Code Sample](https://developer.auth0.com/resources/code-samples/api/spring/basic-role-based-access-control)

### Redis
- [Redis Distributed Caching in Spring Boot](https://positivethinking.tech/insights/distributed-caching-using-redis-in-spring-boot-applications/)
- [Spring Boot Caching with Redis (2025)](https://www.codingshuttle.com/blogs/spring-boot-caching-with-redis-boost-performance-with-fast-operations-2025-1/)
- [Redis Caching Strategies Guide](https://www.meerako.com/blogs/redis-caching-strategies-performance-boost-guide)
- [Distributed Lock with Redisson in Spring Boot](https://medium.com/@melihhtasci/distributed-lock-in-spring-boot-by-redisson-1c812e23dc66)
- [Redisson Spring Integration Reference](https://redisson.pro/docs/integration-with-spring/)
- [Redis Distributed Locks Official Docs](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/)
- [Distributed Locks Best Practices (Developer Playground)](https://developer-playground.com/blog/software-engineer/list/distributed-lock/)
