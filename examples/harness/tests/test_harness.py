from pathlib import Path
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import harness


@patch("harness.openai.ChatCompletion.create")
def test_get_openai_response(mock_create):
    mock_create.return_value = {"choices": [{"message": {"content": "hi"}}]}
    assert harness.get_openai_response("hello") == "hi"
    mock_create.assert_called_once()


@patch("harness.requests.post")
def test_get_mcp_response(mock_post):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"response": "mcp"}
    mock_resp.raise_for_status.return_value = None
    mock_post.return_value = mock_resp

    assert harness.get_mcp_response("hi", "http://mcp") == "mcp"
    mock_post.assert_called_once_with("http://mcp", json={"prompt": "hi"}, timeout=10)
