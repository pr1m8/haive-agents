"""Working Static Supervisor with Tool Sync - Fixed for Current APIs.

This supervisor has:
1. Active agents registry in supervisor state
2. Automatic sync of agent tools to state (sync_tools_with_agents)
3. SupervisorState with agent registry
4. Dynamic handoff tools creation

Based on static_supervisor_with_sync.py but with working imports.
"""

import asyncio
import logging
import operator
import pickle
from collections.abc import Sequence
from typing import Annotated, Any, Literal, TypedDict

# Import current working APIs
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.tools import BaseTool, tool
from langgraph.graph import END, StateGraph
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

logger = logging.getLogger(__name__)


class AgentEntry(BaseModel):
    """Represents a registered agent in the supervisor state."""

    name: str
    description: str
    agent_instance: bytes  # Pickled agent
    agent_class: str
    active: bool = Field(default=True)

    @classmethod
    def from_agent(cls, name: str, description: str, agent: Any) -> "AgentEntry":
        """Create an AgentEntry from an agent instance."""
        return cls(
            name=name,
            description=description,
            agent_instance=pickle.dumps(agent),
            agent_class=agent.__class__.__name__,
        )

    def get_agent(self) -> Any:
        """Deserialize and return the agent instance."""
        return pickle.loads(self.agent_instance)


def create_handoff_tool(agent_name: str, description: str) -> BaseTool:
    """Create a handoff tool for an agent."""

    @tool
    def handoff_to_agent(task: str) -> str:
        f"""Hand off task to {agent_name}: {description}."""
        return f"HANDOFF_TO_{agent_name.upper()}: {task}"

    # Set proper name and description
    handoff_to_agent.name = f"handoff_to_{agent_name}"
    handoff_to_agent.description = f"Hand off task to {agent_name}: {description}"

    return handoff_to_agent


def create_forward_message_tool() -> BaseTool:
    """Create a message forwarding tool."""

    @tool
    def forward_message(message: str) -> str:
        """Forward a message to the user."""
        return f"FORWARDED: {message}"

    return forward_message


class SupervisorSyncState(TypedDict):
    """State for the supervisor with automatic tool sync."""

    messages: Annotated[Sequence[BaseMessage], operator.add]
    registered_agents: dict[str, AgentEntry]
    handoff_tools: dict[str, BaseTool]
    active_agents: list[str]
    current_agent: str
    last_handoff_result: str


def sync_tools_with_agents(state: SupervisorSyncState) -> SupervisorSyncState:
    """Sync handoff tools with registered agents."""
    print("🔧 Syncing tools with agents...")

    registered_agents = state.get("registered_agents", {})
    handoff_tools = state.get("handoff_tools", {})

    # Add tools for new agents
    for agent_name, agent_entry in registered_agents.items():
        if agent_name not in handoff_tools:
            tool = create_handoff_tool(agent_name, agent_entry.description)
            handoff_tools[agent_name] = tool
            print(f"  ✅ Created handoff tool for {agent_name}")

    # Remove tools for unregistered agents
    tools_to_remove = []
    for tool_name in handoff_tools:
        if tool_name not in registered_agents:
            tools_to_remove.append(tool_name)

    for tool_name in tools_to_remove:
        del handoff_tools[tool_name]
        print(f"  ❌ Removed handoff tool for {tool_name}")

    state["handoff_tools"] = handoff_tools
    return state


# Create test tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b


@tool
def create_plan(task: str) -> str:
    """Create a structured plan for a given task."""
    return f"Plan for {task}:\n1. Analyze requirements\n2. Break down into steps\n3. Execute\n4. Verify"


def create_test_agents() -> dict[str, AgentEntry]:
    """Create test agents for the supervisor."""
    agents = {}

    # Math agent
    math_engine = AugLLMConfig(
        temperature=0.1,
        system_message="You are a math specialist. Use tools for calculations.",
    )
    math_agent = SimpleAgentV3(
        name="math_agent", engine=math_engine, tools=[add, multiply]
    )
    agents["math_agent"] = AgentEntry.from_agent(
        name="math_agent",
        description="Mathematical calculations specialist",
        agent=math_agent,
    )

    # Research agent
    research_engine = AugLLMConfig(
        temperature=0.7,
        system_message="You are a research specialist. Provide detailed analysis.",
    )
    research_agent = SimpleAgentV3(name="research_agent", engine=research_engine)
    agents["research_agent"] = AgentEntry.from_agent(
        name="research_agent",
        description="Research and analysis specialist",
        agent=research_agent,
    )

    # Planning agent
    planning_engine = AugLLMConfig(
        temperature=0.5,
        system_message="You are a planning specialist. Create structured plans.",
    )
    planning_agent = SimpleAgentV3(
        name="planning_agent", engine=planning_engine, tools=[create_plan]
    )
    agents["planning_agent"] = AgentEntry.from_agent(
        name="planning_agent",
        description="Task planning and organization specialist",
        agent=planning_agent,
    )

    return agents


async def supervisor_reasoning_node(state: SupervisorSyncState) -> dict[str, Any]:
    """Supervisor that uses registered agents and synced tools."""
    # Sync tools first
    state = sync_tools_with_agents(state)

    # Get the last user message
    user_message = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            user_message = msg.content
            break

    if not user_message:
        return {"messages": [AIMessage(content="No task provided.")]}

    print(f"\n🤔 Supervisor analyzing: '{user_message}'")

    # Simple routing logic based on task content
    task_lower = user_message.lower()
    registered_agents = state.get("registered_agents", {})

    # Find best agent based on keywords
    selected_agent = None
    reasoning = ""

    if any(
        word in task_lower
        for word in ["calculate", "math", "add", "multiply", "divide"]
    ):
        if "math_agent" in registered_agents:
            selected_agent = "math_agent"
            reasoning = "This task requires mathematical calculations."
    elif any(
        word in task_lower
        for word in ["research", "find", "analyze", "study", "investigate"]
    ):
        if "research_agent" in registered_agents:
            selected_agent = "research_agent"
            reasoning = "This task requires research and analysis."
    elif any(
        word in task_lower
        for word in ["plan", "organize", "strategy", "steps", "structure"]
    ):
        if "planning_agent" in registered_agents:
            selected_agent = "planning_agent"
            reasoning = "This task requires planning and organization."

    if selected_agent:
        print(f"✅ Selected agent: {selected_agent}")
        print(
            f"📋 Available handoff tools: {list(state.get('handoff_tools', {}).keys())}"
        )

        return {
            "messages": [AIMessage(content=f"{reasoning} Using {selected_agent}.")],
            "current_agent": selected_agent,
            "next_agent": selected_agent,
            "agent_task": user_message,
        }

    # No suitable agent found
    available_agents = list(registered_agents.keys())
    return {
        "messages": [
            AIMessage(
                content=f"No suitable agent found for this task. Available agents: {available_agents}"
            )
        ],
        "current_agent": "",
        "next_agent": "",
        "agent_task": "",
    }


async def agent_execution_node(state: SupervisorSyncState) -> dict[str, Any]:
    """Execute the selected agent from registry."""
    agent_name = state.get("next_agent")
    task = state.get("agent_task")

    if not agent_name or not task:
        return {"last_handoff_result": "No agent or task specified"}

    # Get agent from registered agents
    registered_agents = state.get("registered_agents", {})
    agent_entry = registered_agents.get(agent_name)

    if not agent_entry:
        return {"last_handoff_result": f"Agent '{agent_name}' not found in registry"}

    # Get the actual agent
    agent = agent_entry.get_agent()

    try:
        print(f"🚀 Executing {agent_name} with task: '{task}'")

        # Execute agent
        if hasattr(agent, "arun"):
            result = await agent.arun(task)
        elif hasattr(agent, "run"):
            result = agent.run(task)
        else:
            result = f"Agent {agent_name} has no execution method"

        print(f"✅ {agent_name} completed successfully")

        # Return result
        return {
            "last_handoff_result": str(result),
            "messages": [AIMessage(content=f"[{agent_name}]: {str(result)[:300]}...")],
            "current_agent": agent_name,
            "next_agent": "",
            "agent_task": "",
        }

    except Exception as e:
        print(f"❌ Error executing {agent_name}: {e}")
        import traceback

        traceback.print_exc()
        return {
            "last_handoff_result": f"Error executing {agent_name}: {e!s}",
            "messages": [AIMessage(content=f"Error with {agent_name}: {e!s}")],
            "current_agent": "",
            "next_agent": "",
            "agent_task": "",
        }


def route_supervisor(state: SupervisorSyncState) -> Literal["execute", "end"]:
    """Route based on supervisor decision."""
    if state.get("next_agent") and state.get("agent_task"):
        return "execute"
    return "end"


async def test_sync_supervisor():
    """Test the supervisor with automatic tool sync."""
    print("🚀 Starting Supervisor with Tool Sync Test")

    # Create registered agents
    print("\n📋 Creating registered agents...")
    registered_agents = create_test_agents()

    print(f"✅ Created {len(registered_agents)} registered agents:")
    for name, agent_entry in registered_agents.items():
        print(f"  - {name}: {agent_entry.description} ({agent_entry.agent_class})")

    # Build the supervisor graph
    print("\n🏗️ Building supervisor graph...")
    workflow = StateGraph(SupervisorSyncState)

    # Add nodes
    workflow.add_node("supervisor", supervisor_reasoning_node)
    workflow.add_node("execute", agent_execution_node)

    # Set up routing
    workflow.set_entry_point("supervisor")
    workflow.add_conditional_edges(
        "supervisor", route_supervisor, {"execute": "execute", "end": END}
    )
    workflow.add_edge("execute", "supervisor")  # Loop back

    # Compile
    app = workflow.compile()
    print("✅ Graph compiled successfully")

    # Test 1: Math task
    print("\n" + "=" * 60)
    print("🧮 Test 1: Math calculation")
    print("=" * 60)

    state1 = {
        "messages": [HumanMessage(content="Please calculate 15 * 8 + 32")],
        "registered_agents": registered_agents,
        "handoff_tools": {},  # Will be synced automatically
        "active_agents": list(registered_agents.keys()),
        "current_agent": "",
        "last_handoff_result": "",
        "next_agent": "",
        "agent_task": "",
    }

    result1 = await app.ainvoke(state1)
    print(f"📤 Result: {result1.get('last_handoff_result', 'No response')}")
    print(f"🔧 Handoff tools created: {list(result1.get('handoff_tools', {}).keys())}")

    # Test 2: Research task
    print("\n" + "=" * 60)
    print("🔍 Test 2: Research task")
    print("=" * 60)

    state2 = {
        "messages": [HumanMessage(content="Research the benefits of renewable energy")],
        "registered_agents": registered_agents,
        "handoff_tools": result1.get("handoff_tools", {}),  # Keep synced tools
        "active_agents": list(registered_agents.keys()),
        "current_agent": "",
        "last_handoff_result": "",
        "next_agent": "",
        "agent_task": "",
    }

    result2 = await app.ainvoke(state2)
    print(f"📤 Result: {result2.get('last_handoff_result', 'No response')}")

    # Test 3: Planning task
    print("\n" + "=" * 60)
    print("📋 Test 3: Planning task")
    print("=" * 60)

    state3 = {
        "messages": [HumanMessage(content="Create a plan for organizing a conference")],
        "registered_agents": registered_agents,
        "handoff_tools": result2.get("handoff_tools", {}),
        "active_agents": list(registered_agents.keys()),
        "current_agent": "",
        "last_handoff_result": "",
        "next_agent": "",
        "agent_task": "",
    }

    result3 = await app.ainvoke(state3)
    print(f"📤 Result: {result3.get('last_handoff_result', 'No response')}")

    # Test 4: Dynamic agent addition
    print("\n" + "=" * 60)
    print("➕ Test 4: Dynamic agent addition")
    print("=" * 60)

    # Add a new agent dynamically
    writing_engine = AugLLMConfig(
        temperature=0.8,
        system_message="You are a writing specialist. Create engaging content.",
    )
    writing_agent = SimpleAgentV3(name="writing_agent", engine=writing_engine)

    # Add to registered agents
    new_registered_agents = result3.get("registered_agents", {}).copy()
    new_registered_agents["writing_agent"] = AgentEntry.from_agent(
        name="writing_agent",
        description="Content writing and editing specialist",
        agent=writing_agent,
    )

    print("➕ Added writing_agent to registry")

    state4 = {
        "messages": [HumanMessage(content="Write a short story about a robot")],
        "registered_agents": new_registered_agents,  # Updated registry
        "handoff_tools": result3.get("handoff_tools", {}),  # Old tools
        "active_agents": list(new_registered_agents.keys()),
        "current_agent": "",
        "last_handoff_result": "",
        "next_agent": "",
        "agent_task": "",
    }

    result4 = await app.ainvoke(state4)
    print(f"📤 Result: {result4.get('last_handoff_result', 'No response')}")
    print(
        f"🔧 Handoff tools after addition: {list(result4.get('handoff_tools', {}).keys())}"
    )

    # Final summary
    print("\n" + "=" * 60)
    print("📊 FINAL SUMMARY")
    print("=" * 60)

    final_registered = result4.get("registered_agents", {})
    final_tools = result4.get("handoff_tools", {})

    print("🎯 Registry Summary:")
    print(f"  - Total registered agents: {len(final_registered)}")
    print(f"  - Total handoff tools: {len(final_tools)}")
    print(
        f"  - Tool sync working: {'✅' if len(final_registered) == len(final_tools) else '❌'}"
    )

    print("\n📋 Registered Agents:")
    for name, agent_entry in final_registered.items():
        print(f"  - {name}: {agent_entry.description}")

    print("\n🔧 Handoff Tools:")
    for tool_name in final_tools.keys():
        print(f"  - {tool_name}")

    print("\n🎉 Supervisor with Tool Sync Test Complete!")

    return {
        "registered_agents": final_registered,
        "handoff_tools": final_tools,
        "results": [result1, result2, result3, result4],
    }


if __name__ == "__main__":
    asyncio.run(test_sync_supervisor())
