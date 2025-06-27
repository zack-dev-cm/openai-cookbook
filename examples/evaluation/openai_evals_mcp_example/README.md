# OpenAI Evals MCP Example

This example demonstrates running an OpenAI Evals evaluation in CI using `run_ci.py`.

## Manual run

```bash
pip install -r requirements.txt
python run_ci.py
```

The script exits with a non-zero status when accuracy or latency thresholds are not met.
