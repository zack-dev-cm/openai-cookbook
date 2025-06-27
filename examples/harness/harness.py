import openai
import requests


def get_openai_response(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Get a completion from OpenAI."""
    response = openai.ChatCompletion.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]


def get_mcp_response(prompt: str, url: str) -> str:
    """Send a prompt to an MCP endpoint and return the text response."""
    resp = requests.post(url, json={"prompt": prompt}, timeout=10)
    resp.raise_for_status()
    return resp.json()["response"]
