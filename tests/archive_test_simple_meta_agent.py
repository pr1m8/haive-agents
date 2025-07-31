"""Simple test of generic MetaAgent to show output."""

from haive.agents.meta import MetaAgent
from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


def main():
    """Test basic MetaAgent functionality."""
    # Create a simple agent
    simple = SimpleAgent(
        name="worker",
        engine=AugLLMConfig(
            temperature=0.3, system_message="You are a helpful assistant."
        ),
    )

    # Wrap with MetaAgent
    meta = MetaAgent.wrap(simple, name="meta_worker")

    # Debug wrapped agent
    if meta.wrapped_agent:
        pass
    else:
        pass

    # Build the graph to complete setup
    try:
        # This should trigger full setup
        if hasattr(meta, "_build_initial_graph"):
            meta._build_initial_graph()
    except Exception:
        pass

    # Now check state
    if hasattr(meta, "state"):
        if meta.state.meta_state:
            pass
    else:
        pass

    # Get summary
    try:
        summary = meta.get_summary()
        for _key, value in summary.items():
            if isinstance(value, dict):
                for _k, _v in value.items():
                    pass
            else:
                pass
    except Exception:
        pass

    # Show the key pattern


if __name__ == "__main__":
    main()
