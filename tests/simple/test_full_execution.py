#!/usr/bin/env python3
"""Test full execution of SimpleAgent v3 with AugLLMConfig."""

import asyncio

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig, DeepSeekLLMConfig


async def test_with_deepseek():
    """Test execution with DeepSeek LLM."""
    config = AugLLMConfig(temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig())

    agent = SimpleAgentV3(
        name="deepseek_agent",
        engine=config,
        debug=False,  # Less verbose
    )

    try:
        await agent.arun("Say 'SimpleAgent v3 is working!'")
        return True
    except Exception:
        return False


async def test_with_default_azure():
    """Test execution with default Azure LLM."""
    # Create with default (Azure)
    config = AugLLMConfig()  # Should default to Azure

    assert isinstance(config.llm_config, AzureLLMConfig), "Should default to Azure"

    SimpleAgentV3(name="azure_agent", engine=config, debug=False)

    # Note: Actual execution would require Azure credentials
    return True


def test_config_variations():
    """Test various AugLLMConfig configurations."""
    # Test 1: Default config
    AugLLMConfig()

    # Test 2: With temperature
    AugLLMConfig(temperature=0.5)

    # Test 3: With DeepSeek
    AugLLMConfig(llm_config=DeepSeekLLMConfig())

    # Test 4: With max_tokens
    AugLLMConfig(max_tokens=100)

    return True


async def main():
    """Run all tests."""
    # Test configurations
    test_config_variations()

    # Test with default Azure
    await test_with_default_azure()

    # Test with DeepSeek
    await test_with_deepseek()

    # Summary


if __name__ == "__main__":
    asyncio.run(main())
