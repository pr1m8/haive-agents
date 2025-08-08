"""Minimal test to debug state issue."""

import contextlib

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig
from langchain_core.messages import HumanMessage

from haive.agents.memory_v2.simple_memory_agent import (
    SimpleMemoryAgent,
    TokenAwareMemoryConfig,
)


def test_minimal():
    """Minimal test to find the issue."""
    # Create agent with minimal config
    agent = SimpleMemoryAgent(
        name="test_minimal",
        engine=AugLLMConfig(llm_config=DeepSeekLLMConfig(model="deepseek-chat")),
        memory_config=TokenAwareMemoryConfig(
            max_context_tokens=2000, storage_backend="in_memory"
        ),
        graph_enabled=False,  # Disable graph to simplify
    )

    # Check the app
    if hasattr(agent, "_app") and agent._app:
        pass

    # Try to prepare input
    try:
        # Test with a simple message
        test_input = {"messages": [HumanMessage(content="Hello")]}

        # Try to invoke
        agent._app.invoke(test_input)

    except Exception:
        # Try with string input
        with contextlib.suppress(Exception):
            agent.run("Hello")


if __name__ == "__main__":
    test_minimal()
