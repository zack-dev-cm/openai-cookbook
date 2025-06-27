import subprocess

subprocess.run([
    "oaieval",
    "evals/openai_evals_mcp_example:cats_summary",
    "--completion_fn",
    "openai_evals_mcp_example.evals.mcp_harness:MCPEval",
    "--completion_args",
    "server_url=http://mcp-server:8000",
], check=True)
