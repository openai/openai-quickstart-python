"""Offline regression tests for the assistant function-calling example."""

import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch


class AssistantFunctionsTest(unittest.TestCase):
    def setUp(self):
        path = (
            Path(__file__).resolve().parents[1]
            / "examples"
            / "assistant-functions"
            / "functions.py"
        )
        spec = importlib.util.spec_from_file_location("assistant_functions", path)
        self.example = importlib.util.module_from_spec(spec)
        with patch("openai.OpenAI"):
            spec.loader.exec_module(self.example)

    def tool(self, name, call_id):
        return SimpleNamespace(
            id=call_id,
            function=SimpleNamespace(
                name=name, arguments=json.dumps({"location": "Chicago"})
            ),
        )

    def configure_run(self, tools):
        self.example.client = Mock()
        runs = self.example.client.beta.threads.runs
        runs.retrieve.return_value = SimpleNamespace(
            id="run_test",
            required_action=SimpleNamespace(
                submit_tool_outputs=SimpleNamespace(tool_calls=tools)
            ),
        )
        return runs

    def test_submits_all_required_outputs_in_one_request(self):
        runs = self.configure_run(
            [self.tool("getCurrentWeather", "weather"), self.tool("getNickname", "name")]
        )
        self.example.run_action("thread_test", "run_test")
        runs.submit_tool_outputs.assert_called_once_with(
            thread_id="thread_test",
            run_id="run_test",
            tool_outputs=[
                {"tool_call_id": "weather", "output": "The weather in Chicago is 64 degrees."},
                {"tool_call_id": "name", "output": "The nickname for Chicago is The Windy City."},
            ],
        )

    def test_unsupported_tool_does_not_submit_partial_outputs(self):
        runs = self.configure_run(
            [self.tool("getCurrentWeather", "weather"), self.tool("unknown", "unknown")]
        )
        with self.assertRaisesRegex(Exception, "Unsupported function call"):
            self.example.run_action("thread_test", "run_test")
        runs.submit_tool_outputs.assert_not_called()

    def test_single_tool_still_works(self):
        runs = self.configure_run([self.tool("getNickname", "name")])
        self.example.run_action("thread_test", "run_test")
        runs.submit_tool_outputs.assert_called_once_with(
            thread_id="thread_test",
            run_id="run_test",
            tool_outputs=[
                {"tool_call_id": "name", "output": "The nickname for Chicago is The Windy City."},
            ],
        )


if __name__ == "__main__":
    unittest.main()
