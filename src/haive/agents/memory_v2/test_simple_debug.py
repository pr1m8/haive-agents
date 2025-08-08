"""Debug test for SimpleMemoryAgent state issues."""

import traceback

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.memory_v2.simple_memory_agent import (
    SimpleMemoryAgent,
    TokenAwareMemoryConfig,
)


def test_state_schema():
    """Test state schema is properly set."""
    # Create config
    deepseek_config = DeepSeekLLMConfig(model="deepseek-chat", temperature=0.1)

    aug_config = AugLLMConfig(llm_config=deepseek_config)

    memory_config = TokenAwareMemoryConfig(
        max_context_tokens=2000, storage_backend="in_memory"
    )

    # Create agent
    agent = SimpleMemoryAgent(
        name="test_debug", engine=aug_config, memory_config=memory_config
    )

    # Check if graph is built correctly
    if hasattr(agent, "_app") and agent._app:
        pass

    # Try to get initial state
    try:
        if agent.state_schema:
            agent.state_schema()
    except Exception:
        pass

    # Try simple run
    try:
        # Just test the graph building, not full execution
        agent.build_graph()
    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    test_state_schema()
