"""Minimal test to debug state issue."""

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

    print(f"Agent state schema: {agent.state_schema}")
    print(f"Use prebuilt: {agent.use_prebuilt_base}")

    # Check the app
    if hasattr(agent, "_app") and agent._app:
        print(
            f"\nApp state schema: {getattr(agent._app, 'state_schema', 'No state_schema')}"
        )

    # Try to prepare input
    try:
        # Test with a simple message
        test_input = {"messages": [HumanMessage(content="Hello")]}
        print(f"\nTest input: {test_input}")

        # Try to invoke
        result = agent._app.invoke(test_input)
        print(f"Result: {result}")

    except Exception as e:
        print(f"\nError during invoke: {e}")
        print(f"Error type: {type(e)}")

        # Try with string input
        try:
            print("\nTrying with string input...")
            result = agent.run("Hello")
            print(f"Result: {result}")
        except Exception as e2:
            print(f"String input error: {e2}")


if __name__ == "__main__":
    test_minimal()
