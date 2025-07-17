"""Simple working test of MetaAgent using MetaStateSchema directly."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.prebuilt.meta_state import MetaStateSchema

from haive.agents.simple import SimpleAgent


async def main():
    """Test MetaStateSchema with real agents."""
    print("🧪 Testing Meta-Agent Pattern with MetaStateSchema")
    print("=" * 60)

    # Create a simple agent
    print("\n1. Creating SimpleAgent...")
    simple_agent = SimpleAgent(
        name="worker",
        engine=AugLLMConfig(
            temperature=0.3, system_message="You are a helpful assistant."
        ),
    )
    print(f"   Created: {simple_agent.name}")

    # Create MetaStateSchema with embedded agent
    print("\n2. Creating MetaStateSchema with embedded agent...")
    meta_state = MetaStateSchema.from_agent(
        agent=simple_agent,
        initial_state={"status": "ready"},
        graph_context={"purpose": "demonstration"},
    )

    print(f"   Meta state created")
    print(f"   Agent name: {meta_state.agent_name}")
    print(f"   Agent type: {meta_state.agent_type}")
    print(f"   Execution status: {meta_state.execution_status}")
    print(f"   Needs recompile: {meta_state.needs_recompile}")

    # Execute agent through meta state
    print("\n3. Executing agent through meta state...")
    try:
        # For SimpleAgent, we just pass the string directly
        result = await meta_state.execute_agent(
            input_data="Hello! What is 2+2?", config={}, update_state=True
        )

        print(f"   Execution status: {result['status']}")
        print(f"   Has output: {'output' in result}")
        if "output" in result:
            print(f"   Output type: {type(result['output'])}")

        # Check execution summary
        print("\n4. Getting execution summary...")
        summary = meta_state.get_execution_summary()
        print(f"   Agent: {summary['agent_name']}")
        print(f"   Type: {summary['agent_type']}")
        print(f"   Status: {summary['current_status']}")
        print(f"   Executions: {summary['execution_count']}")
        print(f"   Needs recompilation: {summary['needs_recompilation']}")

    except Exception as e:
        print(f"   Execution error: {e}")
        import traceback

        traceback.print_exc()

    # Test recompilation tracking
    print("\n5. Testing recompilation...")
    print(f"   Current recompile status: {meta_state.get_recompile_status()}")

    # Mark for recompilation
    meta_state.mark_for_recompile("Test recompilation")
    print(f"   After marking: {meta_state.needs_recompile}")
    print(f"   Recompile reason: {meta_state.get_recompile_status()}")

    # Resolve recompilation
    meta_state.resolve_recompile(success=True)
    print(f"   After resolving: {meta_state.needs_recompile}")

    print("\n✅ MetaStateSchema demonstration complete!")

    print("\n📋 Key Points:")
    print("1. MetaStateSchema embeds any agent for graph composition")
    print("2. Agents are executed through meta state with tracking")
    print("3. Recompilation is tracked via RecompileMixin")
    print("4. Execution history and status are maintained")
    print("5. This is the pattern for meta-capable agents!")


if __name__ == "__main__":
    asyncio.run(main())
