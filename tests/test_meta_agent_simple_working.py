"""Simple working test of MetaAgent using MetaStateSchema directly."""

import asyncio

from haive.agents.simple import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.meta_state import MetaStateSchema


async def main():
    """Test MetaStateSchema with real agents."""
    # Create a simple agent
    simple_agent = SimpleAgent(
        name="worker",
        engine=AugLLMConfig(
            temperature=0.3, system_message="You are a helpful assistant."
        ),
    )

    # Create MetaStateSchema with embedded agent
    meta_state = MetaStateSchema.from_agent(
        agent=simple_agent,
        initial_state={"status": "ready"},
        graph_context={"purpose": "demonstration"},
    )

    # Execute agent through meta state
    try:
        # For SimpleAgent, we just pass the string directly
        result = await meta_state.execute_agent(
            input_data="Hello! What is 2+2?", config={}, update_state=True
        )

        if "output" in result:
            pass

        # Check execution summary
        meta_state.get_execution_summary()

    except Exception:
        import traceback

        traceback.print_exc()

    # Test recompilation tracking

    # Mark for recompilation
    meta_state.mark_for_recompile("Test recompilation")

    # Resolve recompilation
    meta_state.resolve_recompile(success=True)


if __name__ == "__main__":
    asyncio.run(main())
