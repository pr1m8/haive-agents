"""Test SimpleMemoryAgent after fixing imports."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.memory_v2.simple_memory_agent import (
    SimpleMemoryAgent,
    TokenAwareMemoryConfig,
)


def test_simple_memory_agent_with_deepseek():
    """Test SimpleMemoryAgent with DeepSeek configuration."""

    # Create DeepSeek config
    deepseek_config = DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)

    # Create AugLLM config with DeepSeek
    aug_config = AugLLMConfig(
        llm_config=deepseek_config, system_message="You are a helpful memory assistant."
    )

    # Create memory config
    memory_config = TokenAwareMemoryConfig(
        max_context_tokens=2000,
        warning_threshold=0.7,
        critical_threshold=0.85,
        storage_backend="in_memory",
    )

    try:
        # Create SimpleMemoryAgent
        agent = SimpleMemoryAgent(
            name="test_memory", engine=aug_config, memory_config=memory_config
        )

        print("✅ SimpleMemoryAgent created successfully!")
        print(f"Agent name: {agent.name}")
        print(f"Memory config: {memory_config}")
        print(f"Graph enabled: {agent.graph_enabled}")

        # Test basic memory operation
        result = agent.run("Remember that I like Python programming")
        print(f"\n✅ Memory operation successful!")
        print(f"Result: {result}")

        # Get memory status
        status = agent.get_memory_status()
        print(f"\n✅ Memory status retrieved!")
        print(f"Token status: {status.get('token_status', {})}")

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()
        return False


async def test_async_memory_agent():
    """Test async execution of SimpleMemoryAgent."""

    # Create DeepSeek config
    deepseek_config = DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)

    aug_config = AugLLMConfig(
        llm_config=deepseek_config, system_message="You are a helpful memory assistant."
    )

    memory_config = TokenAwareMemoryConfig(
        max_context_tokens=2000, storage_backend="in_memory"
    )

    agent = SimpleMemoryAgent(
        name="test_async", engine=aug_config, memory_config=memory_config
    )

    # Test async operation
    result = await agent.arun("Remember that async works!")
    print(f"\n✅ Async operation successful!")
    print(f"Result: {result}")


if __name__ == "__main__":
    print("Testing SimpleMemoryAgent with fixed imports...\n")

    # Test sync version
    success = test_simple_memory_agent_with_deepseek()

    if success:
        print("\n✅ All sync tests passed!")

        # Test async version
        print("\nTesting async version...")
        asyncio.run(test_async_memory_agent())
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Tests failed!")
