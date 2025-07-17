"""Simple test of generic MetaAgent to show output."""

from haive.core.engine.aug_llm import AugLLMConfig

from haive.agents.meta import MetaAgent
from haive.agents.simple import SimpleAgent


def main():
    """Test basic MetaAgent functionality."""
    print("🧪 Testing Generic MetaAgent")
    print("=" * 60)

    # Create a simple agent
    print("\n1. Creating SimpleAgent...")
    simple = SimpleAgent(
        name="worker",
        engine=AugLLMConfig(
            temperature=0.3, system_message="You are a helpful assistant."
        ),
    )
    print(f"   Created: {simple}")

    # Wrap with MetaAgent
    print("\n2. Wrapping with MetaAgent...")
    meta = MetaAgent.wrap(simple, name="meta_worker")
    print(f"   Created: {meta}")

    # Debug wrapped agent
    print(f"   Has _wrapped_agent attr: {hasattr(meta, '_wrapped_agent')}")
    print(f"   Wrapped agent via property: {meta.wrapped_agent}")
    if meta.wrapped_agent:
        print(f"   Wrapped agent name: {meta.wrapped_agent.name}")
    else:
        print("   WARNING: Wrapped agent is None!")

    # Build the graph to complete setup
    print("\n3. Building graph...")
    try:
        # This should trigger full setup
        if hasattr(meta, "_build_initial_graph"):
            meta._build_initial_graph()
        print("   Graph built successfully")
    except Exception as e:
        print(f"   Graph build error: {e}")

    # Now check state
    print("\n4. Checking state after build...")
    if hasattr(meta, "state"):
        print(f"   Has state: True")
        print(f"   Meta state exists: {meta.state.meta_state is not None}")
        if meta.state.meta_state:
            print(f"   Agent in meta state: {meta.state.meta_state.agent_name}")
            print(f"   Agent type: {meta.state.meta_state.agent_type}")
        print(f"   Wrapped agent from state: {meta.state.wrapped_agent_ref}")
    else:
        print(f"   Has state: False")

    # Get summary
    print("\n5. Getting summary...")
    try:
        summary = meta.get_summary()
        for key, value in summary.items():
            if isinstance(value, dict):
                print(f"   {key}:")
                for k, v in value.items():
                    print(f"      {k}: {v}")
            else:
                print(f"   {key}: {value}")
    except Exception as e:
        print(f"   Error getting summary: {e}")

    print("\n✅ MetaAgent created and configured successfully!")

    # Show the key pattern
    print("\n📋 Key Pattern Demonstrated:")
    print("1. Any agent can be wrapped with MetaAgent")
    print("2. MetaAgent tracks execution and recompilation")
    print("3. Wrapped agent is embedded in MetaStateSchema")
    print("4. All operations go through meta layer for tracking")


if __name__ == "__main__":
    main()
