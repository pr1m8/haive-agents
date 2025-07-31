"""Test SimpleMemoryAgent after fixing imports."""

import asyncio
import traceback

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

        # Test basic memory operation
        agent.run("Remember that I like Python programming")

        # Get memory status
        agent.get_memory_status()

        return True

    except Exception:

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
    await agent.arun("Remember that async works!")


if __name__ == "__main__":

    # Test sync version
    success = test_simple_memory_agent_with_deepseek()

    if success:

        # Test async version
        asyncio.run(test_async_memory_agent())
    else:
        pass
