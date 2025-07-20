"""Debug script for ReactAgent → SimpleAgent sequential execution (auto-run version)."""

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
    print("=" * 80 + "\n")

    # Create ReactAgent with calculator tool
    print("📌 STEP 1: Creating ReactAgent with calculator tool")
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
    print(
        f"   - State schema fields: {list(react_agent.state_schema.model_fields.keys())[:10]}..."
    )

    # Create SimpleAgent for structured output
    print("\n📌 STEP 2: Creating SimpleAgent for structured output")
    simple_agent = SimpleAgent(
        name="formatter",
        engine=AugLLMConfig(
            system_message="You are a formatting agent. Take the previous analysis and create a clean, structured summary with: 1) The problem, 2) The calculation performed, 3) The result, 4) A brief conclusion.",
            temperature=0.1,
        ),
    )
    print(f"✅ SimpleAgent created: {simple_agent.name}")
    print(f"   - State schema: {simple_agent.state_schema.__name__}")
    print(
        f"   - State schema fields: {list(simple_agent.state_schema.model_fields.keys())[:10]}..."
    )

    # Create ProperMultiAgent
    print("\n📌 STEP 3: Creating ProperMultiAgent with both agents")
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
    print("\n📌 STEP 4: Analyzing composed state schema")
    schema_fields = set(multi_agent.state_schema.model_fields.keys())
    print(f"   - Total fields in schema: {len(schema_fields)}")

    # Check for MultiAgentState fields
    multi_agent_fields = {
        "agents",
        "agent_states",
        "agent_outputs",
        "active_agent",
        "agent_execution_order",
    }
    has_multi = multi_agent_fields.intersection(schema_fields)
    print(f"   - MultiAgentState fields present: {has_multi}")

    # Check for ReactAgent-specific fields
    react_fields = {
        "reasoning_trace",
        "tool_calls",
        "current_reasoning",
        "final_answer",
    }
    has_react = react_fields.intersection(schema_fields)
    print(f"   - ReactAgent fields present: {has_react}")

    # Check for SimpleAgent fields
    simple_fields = {"messages", "tools", "engines", "token_usage"}
    has_simple = simple_fields.intersection(schema_fields)
    print(f"   - Common fields present: {has_simple}")

    # Show all fields
    print(f"\n   - All schema fields ({len(schema_fields)} total):")
    for field in sorted(schema_fields)[:20]:  # Show first 20
        print(f"     • {field}")
    if len(schema_fields) > 20:
        print(f"     ... and {len(schema_fields) - 20} more fields")

    # Build the graph
    print("\n📌 STEP 5: Building the graph")
    graph = multi_agent.graph
    print("✅ Graph built"t")
    print(f"   - Nodes: {list(graph.nodes.keys())}")

    # Check node details
    print("\n   - Node details:")
    for node_name in graph.nodes.keys():
        # Get edges from this node
        edges = []
        if hasattr(graph, "_graph") and hasattr(graph._graph, "edges"):
            for edge in graph._graph.edges:
                if edge[0] == node_name:
                    edges.append(edge[1])
        print(f"     • {node_name} → {edges if edges else '[END]'}")

    # Prepare test input
    print("\n📌 STEP 6: Preparing test input")
    test_problem = "What is 25 * 37? Please calculate this and explain your reasoning."
    test_input = {"messages": [HumanMessage(content=test_problem)]}
    print(f"📝 Test problem: '{test_problem}'")

    # Execute with debug mode
    print("\n📌 STEP 7: Starting execution")
    print("🚀 Executing multi-agent workflow...\n")
    print("-" * 80)

    try:
        # Execute
        result = await multi_agent.ainvoke(test_input)

        print("-" * 80)
        print("\n📌 STEP 8: Execution completed")
        print("✅ Execution successful!")

        # Inspect result structure
        print("\n📊 Result Analysis:"s:")
        print(f"   - Result type: {type(result)}")
        print(
            f"   - Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}"
        )

        # Check messages
        if isinstance(result, dict) and "messages" in result:
            print("\n📨 Messages Analysis:"s:")
            print(f"   - Total messages: {len(result['messages'])}")

            # Group messages by type
            message_types = {}
            for msg in result["messages"]:
                msg_type = type(msg).__name__
                if msg_type not in message_types:
                    message_types[msg_type] = 0
                message_types[msg_type] += 1

            print(f"   - Message types: {message_types}")

            # Show each message
            print("\n📜 Message Details:"s:")
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
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    print(f"   Tool calls: {len(msg.tool_calls)}")
                    for tc in msg.tool_calls:
                        print(
                            f"     - {tc.get('name', 'unknown')}: {tc.get('args', {})}"
                        )

        # Check agent outputs if available
        if isinstance(result, dict) and "agent_outputs" in result:
            print("\n🤖 Agent Outputs:"s:")
            for agent_name, output in result["agent_outputs"].items():
                print(f"   - {agent_name}:")
                print(f"     Type: {type(output).__name__}")
                if isinstance(output, dict):
                    print(f"     Keys: {list(output.keys())}")

        # Check agent states if available
        if isinstance(result, dict) and "agent_states" in result:
            print("\n📊 Agent States:"s:")
            for agent_name, state in result["agent_states"].items():
                print(f"   - {agent_name}:")
                print(f"     Fields: {len(state)}")
                print(f"     Keys: {list(state.keys())[:5]}...")

        # Check execution order
        if isinstance(result, dict) and "agent_execution_order" in result:
            print(f"\n🔄 Execution Order: {result['agent_execution_order']}")

        # Final state inspection
        print("\n📌 STEP 9: Final state inspection")
        if hasattr(multi_agent, "state") and multi_agent.state:
            state = multi_agent.state
            print(f"   - State type: {type(state).__name__}")
            print(
                f"   - Has display_debug_info: {hasattr(state, 'display_debug_info')}"
            )

            # Try to display debug info
            if hasattr(state, "display_debug_info"):
                print("\n🔍 MultiAgentState Debug Visualization:")
                state.display_debug_info("Final Multi-Agent State")

        return result

    except Exception as e:
        print(f"\n❌ ERROR during execution: {type(e).__name__}: {str(e)}")
        import traceback

        traceback.print_exc()

        # Try to inspect partial state
        print("\n🔍 Attempting to inspect partial state...")
        if hasattr(multi_agent, "state") and multi_agent.state:
            state = multi_agent.state
            print(f"   - State type: {type(state).__name__}")
            print(
                f"   - Last active agent: {getattr(state, 'active_agent', 'Unknown')}"
            )
            if hasattr(state, "agent_outputs"):
                print(f"   - Completed agents: {list(state.agent_outputs.keys())}")
            if hasattr(state, "agent_states"):
                print(f"   - Agent states: {list(state.agent_states.keys())}")

        return None


if __name__ == "__main__":
    print("🚀 Starting ReactAgent → SimpleAgent Sequential Debug (Auto-run)")
    print("This script will run through all steps automatically\n")

    result = asyncio.run(debug_execution())

    if result:
        print("\n✅ Debug execution completed successfully!")

        # Show final answer if available
        if isinstance(result, dict) and "messages" in result and result["messages"]:
            last_msg = result["messages"][-1]
            if hasattr(last_msg, "content"):
                print("\n📝 Final Answer:"r:")
                print(f"{last_msg.content}")
    else:
        print("\n❌ Debug execution failed - check errors above")

    print("\n" + "=" * 80)
    print("Debug session complete")
    print("=" * 80)
