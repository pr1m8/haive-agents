#!/usr/bin/env python3
"""
Dynamic Supervisor Example with Debug Output

This example demonstrates the dynamic supervisor agent in action,
showing how it can dynamically add agents and execute tasks with
full debug visibility.
"""

import asyncio
import logging
from typing import Any, Dict

# Configure logging for debug output
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

from haive.core.engine import AugLLMEngine
from langchain_core.messages import HumanMessage

from haive.agents.experiments.dynamic_supervisor import (
    AgentRegistry,
    DynamicSupervisorAgent,
    create_test_registry,
)
from haive.agents.simple.agent import SimpleAgent


async def create_example_supervisor() -> DynamicSupervisorAgent:
    """Create a supervisor with a real engine for testing."""
    print("🚀 Creating Dynamic Supervisor with Debug Mode")
    print("=" * 60)

    # Create test registry
    registry = create_test_registry()

    # Create supervisor with debug=True
    supervisor = DynamicSupervisorAgent(
        name="Debug Supervisor",
        agent_registry=registry,
        debug=True,  # Enable debug mode
    )

    print(f"✅ Created supervisor: {supervisor.name}")
    print(f"📝 Initial tools count: {len(supervisor.tools)}")

    # List initial tools
    print("\n🔧 Initial Tools:")
    for i, tool in enumerate(supervisor.tools, 1):
        print(f"  {i}. {tool.name}: {tool.description}")

    return supervisor


async def demonstrate_dynamic_agent_addition(supervisor: DynamicSupervisorAgent):
    """Show how agents can be added dynamically."""
    print("\n" + "=" * 60)
    print("🔄 DYNAMIC AGENT ADDITION DEMONSTRATION")
    print("=" * 60)

    initial_count = len(supervisor.tools)
    print(f"📊 Tools before addition: {initial_count}")

    # Add a new agent dynamically
    print("\n➕ Adding 'writing_agent' to registry...")
    supervisor.add_agent_to_registry(
        name="writing_agent",
        description="Specialized in creative writing, editing, and content creation",
        agent_class=SimpleAgent,
        config={
            "name": "Creative Writer",
            "system_message": "You are a creative writing assistant. Help with writing, editing, and content creation.",
        },
    )

    new_count = len(supervisor.tools)
    print(f"📊 Tools after addition: {new_count}")
    print(f"🆕 New tools added: {new_count - initial_count}")

    # Show updated tools
    print("\n🔧 Updated Tools List:")
    for i, tool in enumerate(supervisor.tools, 1):
        is_new = "handoff_to_writing_agent" in tool.name
        prefix = "🆕" if is_new else "  "
        print(f"{prefix} {i}. {tool.name}: {tool.description}")

    return supervisor


async def demonstrate_agent_listing(supervisor: DynamicSupervisorAgent):
    """Show the list_agents tool in action."""
    print("\n" + "=" * 60)
    print("📋 AGENT LISTING DEMONSTRATION")
    print("=" * 60)

    # Find and use the list_agents tool
    list_tool = next(t for t in supervisor.tools if t.name == "list_agents")

    print("🔍 Invoking list_agents tool...")
    result = list_tool.invoke({})

    print("📋 Available Agents:")
    print(result)

    return result


async def demonstrate_handoff_simulation(supervisor: DynamicSupervisorAgent):
    """Simulate a handoff to an agent."""
    print("\n" + "=" * 60)
    print("🤝 AGENT HANDOFF SIMULATION")
    print("=" * 60)

    # Create a mock state for testing
    mock_state = {
        "messages": [HumanMessage(content="Hello, I need help with research.")],
        "agent_registry": supervisor.agent_registry.to_state_format(),
        "current_agent_name": None,
        "current_task": None,
        "execution_history": [],
        "task_complete": False,
        "current_iteration": 0,
    }

    print("📦 Created mock state:")
    print(f"  Messages: {len(mock_state['messages'])}")
    print(f"  Registry entries: {len(mock_state['agent_registry'])}")

    # Find research agent handoff tool
    research_handoff = next(
        t for t in supervisor.tools if t.name == "handoff_to_research_agent"
    )

    print(f"\n🎯 Found handoff tool: {research_handoff.name}")
    print(f"📝 Tool description: {research_handoff.description}")

    # Note: In a real scenario, this would be called by the graph with proper state injection
    print(
        "\n⚠️  Note: In actual usage, state injection happens automatically via LangGraph"
    )
    print("🔄 This simulation shows the tool structure and expected behavior")

    try:
        # This will fail because we're not in a real graph context with state injection
        result = research_handoff.invoke(
            {
                "task": "Research the latest AI developments",
                # State injection would normally happen here automatically
            }
        )
        print(f"✅ Handoff result: {result}")
    except Exception as e:
        print(f"🔴 Expected error (state injection missing): {e}")
        print("   This is normal - state injection happens during graph execution")


async def show_supervisor_state_schema(supervisor: DynamicSupervisorAgent):
    """Show the supervisor's state schema."""
    print("\n" + "=" * 60)
    print("📊 SUPERVISOR STATE SCHEMA")
    print("=" * 60)

    state_schema = supervisor.state_schema
    print(f"🏗️  State Schema Class: {state_schema.__name__}")

    # Create an example state
    example_state = state_schema(
        messages=[HumanMessage(content="Example message")],
        agent_registry=supervisor.agent_registry.to_state_format(),
        current_agent_name="research_agent",
        current_task="Research AI trends",
        execution_history=[
            {
                "agent_name": "research_agent",
                "task": "Research task",
                "result": "Research completed",
                "success": True,
            }
        ],
    )

    print("\n📋 Example State Fields:")
    print(f"  🗨️  messages: {len(example_state.messages)} messages")
    print(f"  🤖 agent_registry: {len(example_state.agent_registry)} agents")
    print(f"  🎯 current_agent_name: {example_state.current_agent_name}")
    print(f"  📝 current_task: {example_state.current_task}")
    print(f"  📚 execution_history: {len(example_state.execution_history)} entries")
    print(f"  ✅ task_complete: {example_state.task_complete}")
    print(f"  🔢 available_agents: {example_state.available_agents}")

    return example_state


async def demonstrate_full_workflow():
    """Complete demonstration of the dynamic supervisor."""
    print("🎭 DYNAMIC SUPERVISOR COMPLETE DEMONSTRATION")
    print("=" * 80)

    # Step 1: Create supervisor
    supervisor = await create_example_supervisor()

    # Step 2: Show initial state
    await show_supervisor_state_schema(supervisor)

    # Step 3: List available agents
    await demonstrate_agent_listing(supervisor)

    # Step 4: Add agent dynamically
    supervisor = await demonstrate_dynamic_agent_addition(supervisor)

    # Step 5: List agents again to show the addition
    print("\n🔄 Listing agents after dynamic addition:")
    await demonstrate_agent_listing(supervisor)

    # Step 6: Simulate handoff
    await demonstrate_handoff_simulation(supervisor)

    # Final summary
    print("\n" + "=" * 80)
    print("🎉 DEMONSTRATION COMPLETE")
    print("=" * 80)
    print(f"✅ Final supervisor state:")
    print(f"   Name: {supervisor.name}")
    print(f"   Tools: {len(supervisor.tools)}")
    print(f"   Agents: {len(supervisor.agent_registry.list_agents())}")
    print(f"   Debug Mode: {getattr(supervisor, 'debug', False)}")

    agent_names = list(supervisor.agent_registry.list_agents().keys())
    print(f"   Available Agents: {', '.join(agent_names)}")

    tool_names = [t.name for t in supervisor.tools]
    handoff_tools = [name for name in tool_names if name.startswith("handoff_to_")]
    print(f"   Handoff Tools: {', '.join(handoff_tools)}")

    print("\n🚀 The supervisor is ready for real execution with debug visibility!")


async def main():
    """Main execution function."""
    try:
        await demonstrate_full_workflow()
    except Exception as e:
        print(f"❌ Error during demonstration: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
