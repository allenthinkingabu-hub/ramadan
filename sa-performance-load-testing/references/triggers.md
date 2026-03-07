# Trigger Mechanisms Configuration -- sa-performance-load-testing

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests performance test planning or load testing strategy |
| TRG-002 | PM Agent assigns task | PM Agent | IA-QA-001 task assigned via RACI matrix |
| TRG-003 | Architecture design completion | SA Agent | Architecture Design (IA-REQ-001) completed, NFR validation needed |
| TRG-004 | Pre-release NFR validation | QA Process | Release candidate requires performance certification |
| TRG-005 | Performance regression detected | Monitoring | Performance degradation triggers re-validation |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 1
- **Upstream**: Architecture Design outputs, NFR mapping, SLA/SLO targets
- **Downstream**: TL-QA-001..004 (Technical Lead QA tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "performance testing"
- "load testing"
- "stress testing"
- "benchmark"
- "NFR validation"
- "latency target"
- "throughput testing"
- "concurrency testing"
- "soak test"
- "spike test"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The system or service to performance test |
| scope | No | Specific performance aspects to focus on (default: full NFR validation) |
| output_dir | No | Directory for outputs (default: `./performance-load-testing/`) |
| nfr_mapping_ref | No | Path to NFR mapping document |
| architecture_ref | No | Path to architecture design outputs |
