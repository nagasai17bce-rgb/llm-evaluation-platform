# LLM Evaluation Platform

A small evaluation service demonstrating sample scoring and a regression gate. The deterministic evaluator is intentionally easy to replace with task-specific judges.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Production extensions
Add golden datasets, LLM-as-judge evaluators, factuality and safety metrics, trace capture, statistical aggregation, experiment comparison, and CI release gates.
