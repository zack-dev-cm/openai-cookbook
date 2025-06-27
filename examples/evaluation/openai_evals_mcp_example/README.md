# MCP Evaluation Example

This directory demonstrates running [OpenAI Evals](https://github.com/openai/evals) against a local MCP server using the `Responses` API. The `MCPEval` harness defined in `evals/mcp_harness.py` registers an MCP server and sends prompts using `client.responses.create`.

## Setup

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Start an MCP server on `http://localhost:8000`.

3. Run the eval

```bash
bash scripts/run_local.sh
```

## Files

- `evals/mcp_harness.py` – custom completion function.
- `evals/specs/cats_summary.jsonl` – example evaluation data.
- `evals/prompts/answer.jinja` – prompt template.
- `scripts/run_local.sh` – quick start script.
- `scripts/run_ci.py` – CI entry point used by the Dockerfile.
