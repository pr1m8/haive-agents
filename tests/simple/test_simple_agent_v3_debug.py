#!/usr/bin/env python3
"""Debug test for SimpleAgent v3 state schema issue."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.simple.agent_v3 import SimpleAgentV3


def test_debug_state_schema():
    """Debug the state_schema issue."""
    print("\n" + "=" * 60)
    print("DEBUG: SimpleAgent v3 State Schema Issue")
    print("=" * 60)

    # Create config
    config = AugLLMConfig(
        temperature=0.1, max_tokens=50, llm_config=DeepSeekLLMConfig()
    )

    # Create agent
    agent = SimpleAgentV3(name="debug_agent", engine=config, debug=True)  # Enable debug

    # Check state
    print(f"\n✅ Agent created: {agent.name}")
    print(f"Engine: {type(agent.engine).__name__}")
    print(f"Engines dict: {list(agent.engines.keys())}")
    print(f"State schema: {agent.state_schema}")
    print(f"Set schema flag: {agent.set_schema}")
    print(f"Graph built: {agent._graph_built}")
    print(f"Setup complete: {agent._setup_complete}")
    print(f"Is compiled: {agent._is_compiled}")

    # Check if compile method exists
    print(f"\nHas compile method: {hasattr(agent, 'compile')}")
    print(f"Has build_graph method: {hasattr(agent, 'build_graph')}")
    print(f"Has setup_agent method: {hasattr(agent, 'setup_agent')}")

    # Try to access the app
    try:
        app = agent.app
        print(f"\nApp type: {type(app).__name__ if app else 'None'}")
    except Exception as e:
        print(f"\n❌ Error accessing app: {e}")

    return agent


if __name__ == "__main__":
    agent = test_debug_state_schema()
