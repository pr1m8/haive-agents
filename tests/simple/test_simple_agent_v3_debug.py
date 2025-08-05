#!/usr/bin/env python3
"""Debug test for SimpleAgent v3 state schema issue."""

import contextlib

from haive.agents.simple.agent_v3 import SimpleAgentV3
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig


def test_debug_state_schema():
    """Debug the state_schema issue."""
    # Create config
    config = AugLLMConfig(temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig())

    # Create agent
    agent = SimpleAgentV3(name="debug_agent", engine=config, debug=True)  # Enable debug

    # Check state

    # Check if compile method exists

    # Try to access the app
    with contextlib.suppress(Exception):
        pass

    return agent


if __name__ == "__main__":
    agent = test_debug_state_schema()
