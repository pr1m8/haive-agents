"""Working Registry-Based Dynamic Supervisor - Fixed for Current APIs.

This creates a supervisor that:
1. Has an AgentRegistry to store inactive agents
2. Can retrieve agents from registry dynamically
3. Manages active vs inactive agents
4. Uses current working APIs
"""

import asyncio
import logging
import operator
from collections.abc import Sequence
from typing import Annotated, Any, Literal, TypedDict

# Import current working APIs
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.graph import END, StateGraph
from pydantic import BaseModel, Field

from haive.agents.simple.agent_v3 import SimpleAgentV3

logger = logging.getLogger(__name__)


class AgentInfo(BaseModel):
    """Information about an agent including the agent instance and metadata."""

    agent: Any = Field(..., description="The actual agent instance", exclude=True)
    name: str = Field(..., description="Agent name")
    description: str = Field(..., description="What the agent is good at")
    capability: str = Field(..., description="Agent capability keywords")
    active: bool = Field(default=False, description="Whether agent is currently active")

    model_config = {"arbitrary_types_allowed": True}

    def get_agent(self) -> Any:
        return self.agent

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False


class AgentRegistry:
    """Registry of available agents that can be added to supervisor."""

    def __init__(self):
        self.available_agents: dict[str, AgentInfo] = {}

    def register_agent(self, agent_info: AgentInfo):
        """Register an agent as available in registry."""
        self.available_agents[agent_info.name] = agent_info
        logger.info(
            f"📝 Registered {agent_info.name} in registry: {agent_info.description}"
        )

    def get_agent(self, agent_name: str) -> AgentInfo | None:
        """Get an agent info from registry."""
        return self.available_agents.get(agent_name)

    def get_available_agents(self) -> dict[str, str]:
        """Get available agents with capabilities."""
        return {name: info.description for name, info in self.available_agents.items()}

    def search_agents_by_capability(self, task_description: str) -> list[str]:
        """Search for agents that might handle the task."""
        task_lower = task_description.lower()
        matches = []

        for agent_name, agent_info in self.available_agents.items():
            capability_lower = agent_info.capability.lower()

            # Simple keyword matching
            if any(word in capability_lower for word in task_lower.split()) or any(
                word in task_lower for word in capability_lower.split()
            ):
                matches.append(agent_name)

        return matches

    def list_all_agents(self) -> dict[str, dict[str, Any]]:
        """List all agents with their status."""
        return {
            name: {
                "description": info.description,
                "capability": info.capability,
                "active": info.is_active(),
            }
            for name, info in self.available_agents.items()
        }


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


class RegistrySupervisorState(TypedDict):
    """State for the registry supervisor."""

    messages: Annotated[Sequence[BaseMessage], operator.add]
    agent_registry: AgentRegistry
    active_agents: dict[str, AgentInfo]
    next_agent: str
    agent_task: str
    agent_response: str


def create_test_agents_registry() -> AgentRegistry:
    """Create a registry with test agents."""
    registry = AgentRegistry()

    # Math agent
    math_engine = AugLLMConfig(
        temperature=0.1,
        system_message="You are a math specialist. Use tools for calculations when needed.",
    )
    math_agent = SimpleAgentV3(
        name="math_agent", engine=math_engine, tools=[add, multiply]
    )
    registry.register_agent(
        AgentInfo(
            agent=math_agent,
            name="math_agent",
            description="Mathematical calculations specialist",
            capability="math calculate addition multiplication numbers arithmetic",
            active=False,
        )
    )

    # Research agent
    research_engine = AugLLMConfig(
        temperature=0.7,
        system_message="You are a research specialist. You provide detailed analysis and information.",
    )
    research_agent = SimpleAgentV3(name="research_agent", engine=research_engine)
    registry.register_agent(
        AgentInfo(
            agent=research_agent,
            name="research_agent",
            description="Research and analysis specialist",
            capability="research search find information analyze study investigate",
            active=False,
        )
    )

    # Planning agent
    planning_engine = AugLLMConfig(
        temperature=0.5,
        system_message="You are a planning specialist. Create structured plans and organize tasks.",
    )
    planning_agent = SimpleAgentV3(
        name="planning_agent", engine=planning_engine, tools=[create_plan]
    )
    registry.register_agent(
        AgentInfo(
            agent=planning_agent,
            name="planning_agent",
            description="Task planning and organization specialist",
            capability="plan organize strategy steps structure workflow project",
            active=False,
        )
    )

    # Writing agent
    writing_engine = AugLLMConfig(
        temperature=0.8,
        system_message="You are a writing specialist. Create clear, engaging content.",
    )
    writing_agent = SimpleAgentV3(name="writing_agent", engine=writing_engine)
    registry.register_agent(
        AgentInfo(
            agent=writing_agent,
            name="writing_agent",
            description="Content writing and editing specialist",
            capability="write content create edit document text article blog",
            active=False,
        )
    )

    return registry


async def supervisor_reasoning_node(state: RegistrySupervisorState) -> dict[str, Any]:
    """Supervisor that can retrieve agents from registry."""
    # Get the last user message
    user_message = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            user_message = msg.content
            break

    if not user_message:
        return {"messages": [AIMessage(content="No task provided.")]}

    print(f"\n🤔 Supervisor analyzing: '{user_message}'")

    # Check if we have active agents that can handle this
    active_agents = state.get("active_agents", {})
    task_lower = user_message.lower()

    # Simple capability matching for active agents
    suitable_active_agent = None
    for agent_name, agent_info in active_agents.items():
        capability_words = agent_info.capability.lower().split()
        if any(word in task_lower for word in capability_words):
            suitable_active_agent = agent_name
            break

    if suitable_active_agent:
        print(f"✅ Found active agent: {suitable_active_agent}")
        return {
            "messages": [
                AIMessage(
                    content=f"Using active agent {suitable_active_agent} for this task."
                )
            ],
            "next_agent": suitable_active_agent,
            "agent_task": user_message,
        }

    # No suitable active agent, search registry
    registry = state["agent_registry"]
    potential_agents = registry.search_agents_by_capability(user_message)

    if potential_agents:
        # Get first matching agent from registry
        agent_name = potential_agents[0]
        agent_info = registry.get_agent(agent_name)

        if agent_info:
            print(f"📋 Retrieved from registry: {agent_name}")
            # Activate the agent
            agent_info.activate()

            return {
                "messages": [
                    AIMessage(
                        content=f"Retrieved and activated {agent_name} from registry for this task."
                    )
                ],
                "next_agent": agent_name,
                "agent_task": user_message,
                "active_agents": {
                    **active_agents,
                    agent_name: agent_info,
                },  # Add to active
            }

    # No suitable agent found anywhere
    available_in_registry = list(registry.get_available_agents().keys())
    return {
        "messages": [
            AIMessage(
                content=f"No suitable agent found. Available in registry: {available_in_registry}"
            )
        ],
        "next_agent": "",
        "agent_task": "",
    }


async def agent_execution_node(state: RegistrySupervisorState) -> dict[str, Any]:
    """Execute the selected agent."""
    agent_name = state.get("next_agent")
    task = state.get("agent_task")

    if not agent_name or not task:
        return {"agent_response": "No agent or task specified"}

    # Get agent from active agents first, then registry
    active_agents = state.get("active_agents", {})
    agent_info = active_agents.get(agent_name)

    if not agent_info:
        registry = state["agent_registry"]
        agent_info = registry.get_agent(agent_name)

    if not agent_info:
        return {"agent_response": f"Agent '{agent_name}' not found"}

    # Get the actual agent
    agent = agent_info.get_agent()

    try:
        print(f"🚀 Executing {agent_name} with task: '{task}'")

        # Execute agent using current API
        if hasattr(agent, "arun"):
            result = await agent.arun(task)
        elif hasattr(agent, "run"):
            result = agent.run(task)
        else:
            result = f"Agent {agent_name} has no execution method"

        print(f"✅ {agent_name} completed successfully")

        # Clear routing and return result
        return {
            "agent_response": str(result),
            "messages": [AIMessage(content=f"[{agent_name}]: {str(result)[:300]}...")],
            "next_agent": "",
            "agent_task": "",
        }

    except Exception as e:
        print(f"❌ Error executing {agent_name}: {e}")
        import traceback

        traceback.print_exc()
        return {
            "agent_response": f"Error executing {agent_name}: {e!s}",
            "messages": [AIMessage(content=f"Error with {agent_name}: {e!s}")],
            "next_agent": "",
            "agent_task": "",
        }


def route_supervisor(state: RegistrySupervisorState) -> Literal["execute", "end"]:
    """Route based on supervisor decision."""
    if state.get("next_agent") and state.get("agent_task"):
        return "execute"
    return "end"


async def test_registry_supervisor():
    """Test the registry-based dynamic supervisor."""
    print("🚀 Starting Registry-Based Dynamic Supervisor Test")

    # Create agent registry with test agents
    print("\n📋 Setting up agent registry...")
    registry = create_test_agents_registry()

    print(f"✅ Registry created with {len(registry.available_agents)} agents:")
    for name, agent_info in registry.available_agents.items():
        status = "🟢 Active" if agent_info.is_active() else "⚪ Inactive"
        print(f"  - {name}: {agent_info.description} {status}")

    # Build the supervisor graph
    print("\n🏗️ Building registry supervisor graph...")
    workflow = StateGraph(RegistrySupervisorState)

    # Add nodes
    workflow.add_node("supervisor", supervisor_reasoning_node)
    workflow.add_node("execute", agent_execution_node)

    # Set up routing
    workflow.set_entry_point("supervisor")
    workflow.add_conditional_edges(
        "supervisor", route_supervisor, {"execute": "execute", "end": END}
    )
    workflow.add_edge("execute", "supervisor")  # Loop back for multi-turn

    # Compile
    app = workflow.compile()
    print("✅ Graph compiled successfully")

    # Test 1: Math task (should retrieve math_agent from registry)
    print("\n" + "=" * 60)
    print("🧮 Test 1: Math calculation (retrieve from registry)")
    print("=" * 60)

    state1 = {
        "messages": [HumanMessage(content="Please calculate 25 * 8 + 15")],
        "agent_registry": registry,
        "active_agents": {},  # No active agents initially
        "next_agent": "",
        "agent_task": "",
        "agent_response": "",
    }

    result1 = await app.ainvoke(state1)
    print(f"📤 Final result: {result1.get('agent_response', 'No response')}")

    # Show registry status
    print(
        f"📊 Active agents after test 1: {list(result1.get('active_agents', {}).keys())}"
    )

    # Test 2: Research task (should retrieve research_agent)
    print("\n" + "=" * 60)
    print("🔍 Test 2: Research task (retrieve from registry)")
    print("=" * 60)

    state2 = {
        "messages": [HumanMessage(content="Research the benefits of renewable energy")],
        "agent_registry": registry,
        "active_agents": result1.get(
            "active_agents", {}
        ),  # Keep previous active agents
        "next_agent": "",
        "agent_task": "",
        "agent_response": "",
    }

    result2 = await app.ainvoke(state2)
    print(f"📤 Final result: {result2.get('agent_response', 'No response')}")

    # Test 3: Planning task (should retrieve planning_agent)
    print("\n" + "=" * 60)
    print("📋 Test 3: Planning task (retrieve from registry)")
    print("=" * 60)

    state3 = {
        "messages": [
            HumanMessage(content="Create a project plan for building a mobile app")
        ],
        "agent_registry": registry,
        "active_agents": result2.get("active_agents", {}),
        "next_agent": "",
        "agent_task": "",
        "agent_response": "",
    }

    result3 = await app.ainvoke(state3)
    print(f"📤 Final result: {result3.get('agent_response', 'No response')}")

    # Test 4: Another math task (should use already active math_agent)
    print("\n" + "=" * 60)
    print("🧮 Test 4: Another math task (use active agent)")
    print("=" * 60)

    state4 = {
        "messages": [HumanMessage(content="What is 100 divided by 5?")],
        "agent_registry": registry,
        "active_agents": result3.get("active_agents", {}),
        "next_agent": "",
        "agent_task": "",
        "agent_response": "",
    }

    result4 = await app.ainvoke(state4)
    print(f"📤 Final result: {result4.get('agent_response', 'No response')}")

    # Final registry status
    print("\n" + "=" * 60)
    print("📊 FINAL REGISTRY STATUS")
    print("=" * 60)

    final_active = result4.get("active_agents", {})
    print(f"🟢 Active agents ({len(final_active)}):")
    for name, agent_info in final_active.items():
        print(f"  - {name}: {agent_info.description}")

    print("\n⚪ Inactive agents in registry:")
    for name, agent_info in registry.available_agents.items():
        if not agent_info.is_active():
            print(f"  - {name}: {agent_info.description}")

    print("\n🎯 Registry Summary:")
    print(f"  - Total agents in registry: {len(registry.available_agents)}")
    print(f"  - Currently active: {len(final_active)}")
    print(
        f"  - Available for activation: {len(registry.available_agents) - len(final_active)}"
    )

    print("\n🎉 Registry-Based Dynamic Supervisor Test Complete!")

    return {
        "registry": registry,
        "final_active_agents": final_active,
        "results": [result1, result2, result3, result4],
    }


if __name__ == "__main__":
    asyncio.run(test_registry_supervisor())
