"""Debug script for ReactAgent → SimpleAgent sequential execution with breakpoints."""

import asyncio
import sys

# Add paths
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


# Create a simple tool for ReactAgent
@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {str(e)}"


async def debug_execution():
    """Debug ReactAgent → SimpleAgent sequential execution."""

    print("\n" + "=" * 80)
    print("🔍 DEBUG: ReactAgent → SimpleAgent Sequential Execution")
    print("=" * 80 + \n")

    # Create ReactAgent with calculator tool
    print("📌 BREAKPOINT 1: Creating ReactAgent with calculator tool")
    react_agent = ReactAgent(
        name="analyzer",
        engine=AugLLMConfig(
            system_message="You are an analytical agent. Use the calculator tool to solve math problems and provide detailed reasoning.",
            temperature=0.1,  # Low temp for consistency
        ),
        tools=[calculator],
    )
    print(f"✅ ReactAgent created: {react_agent.name}")
    print(f"   - Tools: {[t.name for t in react_agent.tools]}")
    print(f"   - State schema: {react_agent.state_schema.__name__}")
    input("Press Enter to continue...")

    # Create SimpleAgent for structured output
    print("\n📌 BREAKPOINT 2: Creating SimpleAgent for structured output")
    simple_agent = SimpleAgent(
        name="formatter",
        engine=AugLLMConfig(
            system_message="You are a formatting agent. Take the previous analysis and create a clean, structured summary with: 1) The problem, 2) The calculation performed, 3) The result, 4) A brief conclusion.",
            temperature=0.1,
        ),
    )
    print(f"✅ SimpleAgent created: {simple_agent.name}")
    print(f"   - State schema: {simple_agent.state_schema.__name__}")
    input("Press Enter to continue...")

    # Create ProperMultiAgent
    print("\n📌 BREAKPOINT 3: Creating ProperMultiAgent with both agents")
    multi_agent = ProperMultiAgent(
        name="math_analyzer",
        agents=[react_agent, simple_agent],  # Will be converted to dict
        execution_mode="sequential",
    )
    print(f"✅ ProperMultiAgent created: {multi_agent.name}")
    print(f"   - Agents dict: {list(multi_agent.agents.keys())}")
    print(f"   - Execution mode: {multi_agent.execution_mode}")
    print(f"   - State schema: {multi_agent.state_schema.__name__}")

    # Check the composed schema
    print("\n📌 BREAKPOINT 4: Checking composed state schema")
    schema_fields = set(multi_agent.state_schema.model_fields.keys())
    print(f"   - Total fields in schema: {len(schema_fields)}")

    # Check for MultiAgentState fields
    multi_agent_fields = {"agents", "agent_states", "agent_outputs", "active_agent"}
    has_multi = multi_agent_fields.intersection(schema_fields)
    print(f"   - MultiAgentState fields present: {has_multi}")

    # Check for agent-specific fields
    agent_specific_fields = {"reasoning_trace", "tool_calls"}  # ReactAgent fields
    has_specific = agent_specific_fields.intersection(schema_fields)
    print(f"   - Agent-specific fields present: {has_specific}")

    input("Press Enter to continue...")

    # Build the graph
    print("\n📌 BREAKPOINT 5: Building the graph")
    graph = multi_agent.graph
    print("✅ Graph builtt")
    print(f"   - Nodes: {list(graph.nodes.keys())}")

    # Check graph structure
    for node_name, node_fn in graph.nodes.items():
        print(f"   - Node '{node_name}': {type(node_fn).__name__}")

    input("Press Enter to continue...")

    # Prepare test input
    print("\n📌 BREAKPOINT 6: Preparing test input")
    test_problem = "What is 25 * 37? Please calculate this and explain your reasoning."
    test_input = {"messages": [HumanMessage(content=test_problem)]}
    print(f"📝 Test problem: '{test_problem}'")
    input("Press Enter to execute...")

    # Execute with debug mode
    print("\n📌 BREAKPOINT 7: Starting execution")
    print("🚀 Executing multi-agent workflow...\n")

    try:
        # Add debug flag if available
        if hasattr(multi_agent, "debug"):
            multi_agent.debug = True

        # Execute
        result = await multi_agent.ainvoke(test_input)

        print("\n📌 BREAKPOINT 8: Execution completed")
        print("✅ Execution successful!")

        # Inspect result structure
        print(f"\n📊 Result type: {type(result)}")
        print(
            f"📊 Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}"
        )

        # Check messages
        if isinstance(result, dict) and "messages" in result:
            print(f"\n📨 Total messages: {len(result['messages'])}")
            for i, msg in enumerate(result["messages"]):
                print(f"\n   Message {i+1} ({type(msg).__name__}):")
                if hasattr(msg, "content"):
                    content_preview = (
                        msg.content[:200] + "..."
                        if len(msg.content) > 200
                        else msg.content
                    )
                    print(f"   Content: {content_preview}")
                if hasattr(msg, "name"):
                    print(f"   From: {msg.name}")

        # Check agent outputs if available
        if isinstance(result, dict) and "agent_outputs" in result:
            print("\n🤖 Agent outputs:s:")
            for agent_name, output in result["agent_outputs"].items():
                print(f"   - {agent_name}: {type(output).__name__}")

        # Check agent states if available
        if isinstance(result, dict) and "agent_states" in result:
            print("\n📊 Agent states:s:")
            for agent_name, state in result["agent_states"].items():
                print(f"   - {agent_name}: {len(state)} fields")

        input("\nPress Enter to see detailed state inspection...")

        # Detailed state inspection
        print("\n📌 BREAKPOINT 9: Detailed state inspection")
        if hasattr(multi_agent, "state") and multi_agent.state:
            state = multi_agent.state

            # Use MultiAgentState debug visualization if available
            if hasattr(state, "display_debug_info"):
                state.display_debug_info("Final Multi-Agent State")

            # Manual inspection as backup
            print("\n🔍 Manual State Inspection:")
            print(f"   - Active agent: {getattr(state, 'active_agent', 'N/A')}")
            print(
                f"   - Execution order: {getattr(state, 'agent_execution_order', [])}"
            )

            if hasattr(state, "agent_outputs"):
                print("\n   - Agent outputs:")
                for name, output in state.agent_outputs.items():
                    print(f"     • {name}: {type(output).__name__}")

        return result

    except Exception as e:
        print(f"\n❌ ERROR during execution: {type(e).__name__}: {str(e)}")
        import traceback

        traceback.print_exc()

        # Try to inspect partial state
        print("\n🔍 Attempting to inspect partial state...")
        if hasattr(multi_agent, "state") and multi_agent.state:
            state = multi_agent.state
            print(
                f"   - Last active agent: {getattr(state, 'active_agent', 'Unknown')}"
            )
            if hasattr(state, "agent_outputs"):
                print(f"   - Completed agents: {list(state.agent_outputs.keys())}")

        return None


async def inspect_intermediate_states():
    """Additional function to inspect intermediate states during execution."""
    print("\n" + "=" * 80)
    print("🔬 ADVANCED: Inspecting intermediate states")
    print("=" * 80 + \n")

    # This would require modifying the graph nodes to add inspection points
    # For now, we'll use the simpler debug approach above
    pass


if __name__ == "__main__":
    print("🚀 Starting ReactAgent → SimpleAgent Sequential Debug")
    print("This script will pause at various breakpoints for inspection")
    print("Press Ctrl+C at any time to exit\n")

    result = asyncio.run(debug_execution())

    if result:
        print("\n✅ Debug execution completed successfully!")
    else:
        print("\n❌ Debug execution failed - check errors above")

    print("\n" + "=" * 80)
    print("Debug session complete")
    print("=" * 80)
