# LLM Evaluation Platform

## Overview
A repeatable evaluation service for measuring model behavior and enforcing regression gates before releases.

The implementation is intentionally runnable without proprietary infrastructure. It demonstrates the control-plane and domain contract first, so real systems can be integrated behind stable interfaces.

## Architecture
```
Client
  |
  v
FastAPI validation
  |
  v
Domain service
  +--> policy checks
  +--> state / metadata
  +--> provider integrations
  |
  v
Structured decision
```

## Repository structure
- `app/main.py` — API boundary
- `app/service.py` — domain behavior
- `tests/test_api.py` — regression tests
- `examples/request.sh` — runnable example
- `Dockerfile` — container image
- `pyproject.toml` — dependencies
- `.github/workflows/ci.yml` — CI

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

Verify:
```bash
curl http://localhost:8000/health
bash examples/request.sh
pytest -q
```

## API contract
### GET /health
Returns:
```json
{"status":"ok"}
```

### POST /v1/run
```json
{"value":"demo request"}
```

Responses are structured JSON so callers can make deterministic decisions without parsing generated prose.

## Production architecture
Typical production components include an API gateway, OIDC/workload identity, durable database, Redis, asynchronous workers, provider adapters, OpenTelemetry, centralized logs, a secrets manager, object storage where needed, and Kubernetes or a managed container platform.

## Reliability
Use deadlines, retries with exponential backoff, circuit breakers, rate limits, idempotency keys, graceful shutdown, queue backpressure, dead-letter handling, dependency health checks, and SLOs.

## Security
Apply least privilege, tenant isolation, audit trails, secret management, PII redaction, input/output validation, dependency scanning, container scanning, and restricted egress. High-impact actions should require explicit authorization or human approval.

## Testing strategy
Unit-test domain decisions, API contract tests, integration-test infrastructure adapters, run load tests for throughput-sensitive paths, and add adversarial/security cases where the system processes untrusted input.

## Deployment
```bash
docker build -t llm-evaluation-platform .
docker run --rm -p 8000:8000 llm-evaluation-platform
```

CI runs automated tests on pushes and pull requests. Production CI/CD should add linting, security scanning, signed images, staging smoke tests, and controlled rollout.

## Design principles
1. Keep policy decisions explicit.
2. Separate detection from action.
3. Make state transitions observable.
4. Keep external providers replaceable.
5. Prefer approval gates for irreversible operations.
6. Treat every agent-generated action as untrusted until validated.

## Roadmap
- Durable state
- Multi-tenancy
- Authentication/RBAC
- Real provider integrations
- OpenTelemetry
- Load/failure testing
- Infrastructure as code
- Kubernetes deployment
- Production dashboards

## Project-specific design
**Core problem:** A repeatable evaluation service for measuring model behavior and enforcing regression gates before releases.

**Production path:** keep the domain service as the policy/control layer and introduce real infrastructure behind adapters.