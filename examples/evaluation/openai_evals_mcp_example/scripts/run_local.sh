#!/bin/bash
# Example script to run the eval locally
export OPENAI_API_KEY=${OPENAI_API_KEY:-"sk-your-key"}

oaieval evals/openai_evals_mcp_example:cats_summary \
  --completion_fn openai_evals_mcp_example.evals.mcp_harness:MCPEval \
  --completion_args server_url=http://localhost:8000
