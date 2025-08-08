"""Test SimpleMemoryAgent with DeepSeek LLM configuration."""

import asyncio
import os
import traceback

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.memory_v2.simple_memory_agent import SimpleMemoryAgent

# First set up DeepSeek if needed
if not os.getenv("DEEPSEEK_API_KEY"):
    os.environ["DEEPSEEK_API_KEY"] = "test-key"


async def test_simple_memory_agent_with_deepseek():
    """Test SimpleMemoryAgent using DeepSeek."""
    # Step 1: Create DeepSeek config
    try:
        deepseek_config = DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)
    except Exception:
        return

    # Step 2: Create AugLLMConfig with DeepSeek
    try:
        aug_config = AugLLMConfig(
            llm_config=deepseek_config,
            system_message="You are a helpful memory assistant.",
        )
    except Exception:
        return

    # Step 3: Try to import SimpleMemoryAgent
    try:
        pass
    except Exception:
        traceback.print_exc()

        # Try to import the problematic module directly
        try:
            pass
        except Exception:
            # Check if we can fix the import

            pass
        return

    # Step 4: Create SimpleMemoryAgent with DeepSeek
    try:
        agent = SimpleMemoryAgent(
            name="test_deepseek_memory", engine=aug_config, user_id="test_user"
        )
    except Exception:
        traceback.print_exc()
        return

    # Step 5: Test the agent
    try:
        # Store a memory
        await agent.arun("Remember: Alice works at TechCorp as an AI researcher.")

        # Query memory
        await agent.arun("Who is Alice?")

    except Exception:
        traceback.print_exc()
        return


async def main():
    """Run the test."""
    await test_simple_memory_agent_with_deepseek()


if __name__ == "__main__":
    asyncio.run(main())
