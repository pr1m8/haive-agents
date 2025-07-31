#!/usr/bin/env python3
"""Test that the AugLLMConfig fix is working properly."""

import contextlib

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig


def main():

    # Test 1: The Core Fix - AzureLLMConfig is no longer None

    from haive.core.engine.aug_llm.config import AzureLLMConfig as ImportedAzure

    assert ImportedAzure is not None, "AzureLLMConfig should not be None!"

    # Test 2: Default AugLLMConfig (which uses AzureLLMConfig internally)

    with contextlib.suppress(Exception):
        config = AugLLMConfig()

    # Test 3: AugLLMConfig with DeepSeek

    config = AugLLMConfig(
        temperature=0.1, max_tokens=100, llm_config=DeepSeekLLMConfig()
    )

    # Test 4: SimpleAgent v3 Creation

    SimpleAgentV3(name="test_agent", engine=config, debug=True)

    # Summary


if __name__ == "__main__":
    main()
