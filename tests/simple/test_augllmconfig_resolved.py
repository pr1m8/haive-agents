#!/usr/bin/env python3
"""Final test proving AugLLMConfig issue is resolved."""

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig


def main():

    # Test 1: Default AugLLMConfig uses Azure
    config = AugLLMConfig()

    # Test 2: Can use other LLMs
    AugLLMConfig(llm_config=DeepSeekLLMConfig())

    # Test 3: Agent creation works
    SimpleAgentV3(name="test_agent", engine=config, debug=True)


if __name__ == "__main__":
    main()
