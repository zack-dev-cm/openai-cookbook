import time
from typing import Any, Optional

import openai
from evals.api import CompletionFn, CompletionResult
from evals.record import record_sampling


class MCPEval(CompletionFn):
    """CompletionFn that routes prompts through an MCP server via the Responses API."""

    def __init__(self, server_url: str, model: str = "gpt-4o", server_label: str = "local-mcp", api_key: Optional[str] = None) -> None:
        self.server_url = server_url
        self.server_label = server_label
        self.model = model
        self.client = openai.Client(api_key=api_key)
        try:
            self.client.mcp_servers.register(url=server_url, label=server_label)
        except Exception:
            pass  # already registered

    def __call__(self, prompt: str, **kwargs: Any) -> CompletionResult:
        start = time.time()
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
            tools=[{"type": "mcp", "server_url": self.server_url, "server_label": self.server_label}],
            **kwargs,
        )
        latency = time.time() - start
        text = getattr(response, "text", "")
        trace_url = f"https://platform.openai.com/trace/{response.id}"
        record_sampling(prompt=prompt, sampled=text, metadata={"latency": latency, "trace_url": trace_url})
        return CompletionResult(text, latency=latency, extra={"trace_url": trace_url})
