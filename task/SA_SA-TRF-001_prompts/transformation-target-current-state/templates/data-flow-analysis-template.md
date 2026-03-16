# OUT-04: Data Flow & Interface Analysis

**Analysis Session**: {session_id}
**Target**: {target_name}
**Target Path**: {target_path}
**Analysis Date**: {analysis_date}
**Analyst**: SA-TRF-001 Agent

---

## 1. Data Flow Summary

| Flow Category | Count | Notes |
|--------------|-------|-------|
| API / HTTP flows | {api_flow_count} | {api_flow_notes} |
| Event / Message flows | {event_flow_count} | {event_flow_notes} |
| Database read flows | {db_read_count} | {db_read_notes} |
| Database write flows | {db_write_count} | {db_write_notes} |
| External service calls | {ext_service_count} | {ext_service_notes} |
| Shared state reads | {shared_state_read_count} | {shared_state_read_notes} |
| Shared state writes | {shared_state_write_count} | {shared_state_write_notes} |

---

## 2. API / HTTP Interface Flows

| Flow ID | Endpoint / Route | Method | Request Shape | Response Shape | Auth Required | Error Codes |
|---------|-----------------|--------|--------------|----------------|--------------|-------------|
| FL-01 | {endpoint_1} | {method_1} | {request_shape_1} | {response_shape_1} | {auth_1} | {errors_1} |
| FL-02 | {endpoint_2} | {method_2} | {request_shape_2} | {response_shape_2} | {auth_2} | {errors_2} |
| FL-0N | {endpoint_n} | {method_n} | {request_shape_n} | {response_shape_n} | {auth_n} | {errors_n} |

### Data Transformation in API Flows

| Flow ID | Input Type | Transformation Applied | Output Type | Validation Rules |
|---------|-----------|----------------------|-------------|-----------------|
| FL-01 | {input_type_1} | {transformation_1} | {output_type_1} | {validation_1} |
| FL-02 | {input_type_2} | {transformation_2} | {output_type_2} | {validation_2} |

---

## 3. Event / Message Flows

| Flow ID | Topic / Queue | Direction | Message Schema | Producer | Consumer | Ordering Guarantee |
|---------|--------------|-----------|---------------|----------|----------|-------------------|
| EV-01 | {topic_1} | {direction_1} | {schema_1} | {producer_1} | {consumer_1} | {ordering_1} |
| EV-02 | {topic_2} | {direction_2} | {schema_2} | {producer_2} | {consumer_2} | {ordering_2} |

> Direction: `Inbound (consumes)` `Outbound (publishes)` `Bidirectional`
> Note: If no event flows exist, state: "No event or message queue integrations identified in this target."

---

## 4. Database Interactions

### 4.1 Tables / Collections Accessed

| Table / Collection | DB Type | Operations | ORM / Query Method | Source File | Transaction Boundary |
|-------------------|---------|-----------|-------------------|-------------|---------------------|
| {table_1} | {db_type_1} | {operations_1} | {orm_1} | {file_1} | {transaction_1} |
| {table_2} | {db_type_2} | {operations_2} | {orm_2} | {file_2} | {transaction_2} |

> Operations: `SELECT` `INSERT` `UPDATE` `DELETE` `UPSERT` `DDL`

### 4.2 Key Queries

| Query ID | Purpose | SQL / Query | Parameters | Index Used | Performance Notes |
|---------|---------|------------|-----------|-----------|------------------|
| QRY-01 | {purpose_1} | `{query_1}` | {params_1} | {index_1} | {perf_notes_1} |
| QRY-02 | {purpose_2} | `{query_2}` | {params_2} | {index_2} | {perf_notes_2} |

---

## 5. External Service Integrations

| Service | Protocol | Endpoint / Topic | Auth Method | Timeout | Retry Policy | Fallback |
|---------|---------|-----------------|-------------|---------|--------------|---------|
| {service_1} | {protocol_1} | {endpoint_1} | {auth_1} | {timeout_1} | {retry_1} | {fallback_1} |
| {service_2} | {protocol_2} | {endpoint_2} | {auth_2} | {timeout_2} | {retry_2} | {fallback_2} |

---

## 6. Shared State Interactions

| State Item | Storage | Read By | Written By | Consistency Level | Race Condition Risk |
|-----------|---------|---------|-----------|------------------|-------------------|
| {state_1} | {storage_1} | {readers_1} | {writers_1} | {consistency_1} | {race_risk_1} |
| {state_2} | {storage_2} | {readers_2} | {writers_2} | {consistency_2} | {race_risk_2} |

> Consistency levels: `Strong` `Eventual` `None`

---

## 7. Data Validation & Sanitization Points

| Flow ID | Validation Type | Location | Rules Applied | Missing Validation? |
|---------|----------------|----------|--------------|---------------------|
| {flow_id_1} | {validation_type_1} | {location_1} | {rules_1} | {missing_1} |
| {flow_id_2} | {validation_type_2} | {location_2} | {rules_2} | {missing_2} |

---

## 8. Data Flow Risk Assessment

| Risk | Flow(s) Affected | Risk Level | Description | Transformation Impact |
|------|-----------------|------------|-------------|----------------------|
| {risk_1} | {flows_1} | {level_1} | {description_1} | {impact_1} |
| {risk_2} | {flows_2} | {level_2} | {description_2} | {impact_2} |

> Risk levels: `Critical` `High` `Medium` `Low`
