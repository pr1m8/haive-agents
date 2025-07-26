"""Test memory operations with fixed SimpleMemoryAgent."""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.memory_v2.simple_memory_agent import (
    SimpleMemoryAgent,
    TokenAwareMemoryConfig,
)


def test_memory_operations():
    """Test various memory operations."""
    # Create agent with DeepSeek
    agent = SimpleMemoryAgent(
        name="memory_test",
        engine=AugLLMConfig(
            llm_config=DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)
        ),
        memory_config=TokenAwareMemoryConfig(
            max_context_tokens=2000, storage_backend="in_memory"
        ),
    )

    # Test 1: Store memories
    agent.run("Remember that I'm a software engineer working on AI projects")

    agent.run("Remember that I prefer Python and have 10 years of experience")

    agent.run("Remember that I'm interested in multi-agent systems and RAG")

    # Test 2: Retrieve memories
    agent.run("What do you know about my background?")

    # Test 3: Search memories
    agent.run("Search for information about my programming experience")

    # Test 4: Check memory status
    agent.get_memory_status()

    # Test 5: Check if state is correct
    if hasattr(agent, "_app") and agent._app:
        # The graph should be using MemoryStateWithTokens
        agent._app.get_state.__annotations__.get("return", "Unknown")


if __name__ == "__main__":
    test_memory_operations()
