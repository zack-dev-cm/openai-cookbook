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

## GitHub Actions

A workflow named **MCP Eval** runs automatically on every pull request. You can
also trigger it manually from GitHub:

1. Push your branch and open the **Actions** tab.
2. Choose **MCP Eval** from the list of workflows.
3. Click **Run workflow**, select the branch, and start the job.

The workflow installs the dependencies listed in `requirements.txt`, executes
`scripts/run_ci.py`, and fails if the evaluation's accuracy or latency thresholds
are not met.
