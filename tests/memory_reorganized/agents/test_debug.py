"""Debug test for SimpleMemoryAgent state issues.
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import DeepSeekLLMConfig

from haive.agents.memory_reorganized.agents.simple import (
    SimpleMemoryAgent,
    TokenAwareMemoryConfig,
)


def test_state_schema():
    """Test state schema is properly set.
    """
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

    print(f"Agent created: {agent.name}")
    print(f"State schema: {agent.state_schema}")
    print(
        f"State schema name: {agent.state_schema.__name__ if agent.state_schema else 'None'}"
    )
    print(f"Use prebuilt base: {agent.use_prebuilt_base}")

    # Check if graph is built correctly
    if hasattr(agent, "_app") and agent._app:
        print(f"\nGraph built: {agent._app}")
        print(
            f"Graph nodes: {list(agent._app.nodes.keys()) if hasattr(agent._app, 'nodes') else 'No nodes'}"
        )

    # Try to get initial state
    try:
        if agent.state_schema:
            initial_state = agent.state_schema()
            print(f"\nInitial state created: {type(initial_state)}")
            print(f"State dict keys: {list(initial_state.model_dump().keys())[:5]}...")
    except Exception as e:
        print(f"\nError creating initial state: {e}")

    # Try simple run
    try:
        # Just test the graph building, not full execution
        agent.build_graph()
        print("\n✅ Graph built successfully!")
    except Exception as e:
        print(f"\n❌ Graph build error: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_state_schema()
