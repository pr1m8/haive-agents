"""Working Dynamic Agent Discovery Supervisor - Fixed for Current APIs.

This supervisor:
1. Has active agents registry
2. Can dynamically discover and add new agents at runtime
3. Manages agent capabilities and specialties
4. Has SupervisorState with agent registry integration
5. Syncs agent tools to state automatically

Based on dynamic_agent_discovery_supervisor.py but with working imports.
"""

import asyncio
import logging
import operator
from collections.abc import Sequence
from enum import Enum
from typing import Annotated, Any, Literal, TypedDict

# Import current working APIs
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.graph import END, StateGraph
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3

logger = logging.getLogger(__name__)


class AgentDiscoveryMode(str, Enum):
    """Agent discovery modes."""

    COMPONENT_DISCOVERY = "component_discovery"
    RAG_DISCOVERY = "rag_discovery"
    MCP_DISCOVERY = "mcp_discovery"
    HYBRID = "hybrid"
    MANUAL = "manual"  # For this demo


class AgentCapability(BaseModel):
    """Description of an agent's capabilities."""

    name: str = Field(..., description="Agent name")
    agent_type: str = Field(..., description="Type of agent")
    description: str = Field(..., description="What this agent can do")
    specialties: list[str] = Field(
        default_factory=list, description="Areas of expertise"
    )
    tools: list[str] = Field(default_factory=list, description="Tools this agent has")
    active: bool = Field(default=True, description="Whether agent is active")


class DynamicAgentDiscoveryState(TypedDict):
    """State for dynamic agent discovery supervisor."""

    messages: Annotated[Sequence[BaseMessage], operator.add]
    agents: dict[str, Any]  # Active agent instances
    agent_capabilities: dict[str, AgentCapability]  # Agent capability registry
    discovered_agents: set[str]  # Names of discovered agents
    available_agent_specs: list[dict[str, Any]]  # Specs for agents that can be created
    current_agent: str
    agent_task: str
    agent_response: str
    discovery_attempts: int


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


@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    return f"Search results for '{query}': Found relevant information about {query}..."


@tool
def analyze_data(data: str) -> str:
    """Analyze data and provide insights."""
    return f"Analysis of '{data}': Key insights and patterns identified..."


@tool
def write_content(topic: str) -> str:
    """Write content on a given topic."""
    return f"Content written about '{topic}': Comprehensive article with analysis and recommendations..."


def create_initial_agents() -> dict[str, Any]:
    """Create initial set of agents."""
    agents = {}

    # Basic assistant
    basic_engine = AugLLMConfig(
        temperature=0.7, system_message="You are a helpful general assistant."
    )
    basic_agent = SimpleAgentV3(name="basic_assistant", engine=basic_engine)
    agents["basic_assistant"] = basic_agent

    return agents


def create_initial_capabilities() -> dict[str, AgentCapability]:
    """Create initial agent capabilities."""
    return {
        "basic_assistant": AgentCapability(
            name="basic_assistant",
            agent_type="SimpleAgentV3",
            description="General purpose assistant for basic tasks",
            specialties=["general", "basic"],
            tools=[],
            active=True,
        )
    }


def create_available_agent_specs() -> list[dict[str, Any]]:
    """Create specs for agents that can be discovered/created."""
    return [
        {
            "name": "math_expert",
            "agent_type": "SimpleAgentV3",
            "description": "Mathematical calculations and problem solving expert",
            "specialties": [
                "math",
                "calculations",
                "arithmetic",
                "algebra",
                "geometry",
            ],
            "tools": ["add", "multiply"],
            "config": {
                "engine": AugLLMConfig(
                    temperature=0.1,
                    system_message="You are a math expert. Use tools for calculations when needed.",
                ),
                "tools": [add, multiply],
            },
        },
        {
            "name": "research_specialist",
            "agent_type": "SimpleAgentV3",
            "description": "Research and information gathering specialist",
            "specialties": [
                "research",
                "analysis",
                "investigation",
                "search",
                "information",
            ],
            "tools": ["search_web", "analyze_data"],
            "config": {
                "engine": AugLLMConfig(
                    temperature=0.5,
                    system_message="You are a research specialist. Use tools to search and analyze information.",
                ),
                "tools": [search_web, analyze_data],
            },
        },
        {
            "name": "planning_agent",
            "agent_type": "SimpleAgentV3",
            "description": "Strategic planning and project management expert",
            "specialties": [
                "planning",
                "strategy",
                "organization",
                "project",
                "management",
                "structure",
            ],
            "tools": ["create_plan"],
            "config": {
                "engine": AugLLMConfig(
                    temperature=0.4,
                    system_message="You are a planning expert. Create detailed plans and organize tasks.",
                ),
                "tools": [create_plan],
            },
        },
        {
            "name": "content_writer",
            "agent_type": "SimpleAgentV3",
            "description": "Content creation and writing specialist",
            "specialties": [
                "writing",
                "content",
                "articles",
                "creative",
                "editing",
                "documentation",
            ],
            "tools": ["write_content"],
            "config": {
                "engine": AugLLMConfig(
                    temperature=0.8,
                    system_message="You are a content writing specialist. Create engaging, well-structured content.",
                ),
                "tools": [write_content],
            },
        },
        {
            "name": "data_analyst",
            "agent_type": "ReactAgent",
            "description": "Data analysis and insights expert with reasoning capabilities",
            "specialties": [
                "data",
                "analytics",
                "statistics",
                "insights",
                "trends",
                "visualization",
            ],
            "tools": ["analyze_data", "search_web"],
            "config": {
                "engine": AugLLMConfig(
                    temperature=0.3,
                    system_message="You are a data analyst. Use reasoning and tools to analyze data and provide insights.",
                ),
                "tools": [analyze_data, search_web],
            },
        },
    ]


def find_matching_agent_specs(
    task: str, available_specs: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Find agent specs that match the task requirements."""
    task_lower = task.lower()
    matches = []

    for spec in available_specs:
        # Check specialties
        for specialty in spec.get("specialties", []):
            if specialty in task_lower:
                matches.append(spec)
                break

        # Check description
        description_words = spec.get("description", "").lower().split()
        if any(word in task_lower for word in description_words):
            if spec not in matches:
                matches.append(spec)

    return matches


def create_agent_from_spec(spec: dict[str, Any]) -> Any:
    """Create an agent instance from a specification."""
    agent_type = spec.get("agent_type", "SimpleAgentV3")
    config = spec.get("config", {})

    if agent_type == "SimpleAgentV3":
        return SimpleAgentV3(name=spec["name"], **config)
    if agent_type == "ReactAgent":
        return ReactAgent(name=spec["name"], **config)
    # Default to SimpleAgentV3
    return SimpleAgentV3(name=spec["name"], **config)


async def supervisor_discovery_node(
    state: DynamicAgentDiscoveryState,
) -> dict[str, Any]:
    """Supervisor node that can discover and add new agents."""
    # Get the last user message
    user_message = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            user_message = msg.content
            break

    if not user_message:
        return {"messages": [AIMessage(content="No task provided.")]}

    print(f"\n🤔 Dynamic Supervisor analyzing: '{user_message}'")

    # Check if we have a suitable active agent
    agents = state.get("agents", {})
    agent_capabilities = state.get("agent_capabilities", {})
    task_lower = user_message.lower()

    # Find suitable active agent
    suitable_agent = None
    for agent_name, capability in agent_capabilities.items():
        if agent_name in agents and capability.active:
            # Check if agent specialties match task
            if any(specialty in task_lower for specialty in capability.specialties):
                suitable_agent = agent_name
                break

    if suitable_agent:
        print(f"✅ Found suitable active agent: {suitable_agent}")
        return {
            "messages": [AIMessage(content=f"Using {suitable_agent} for this task.")],
            "current_agent": suitable_agent,
            "next_agent": suitable_agent,
            "agent_task": user_message,
        }

    # No suitable active agent, try to discover one
    print("🔍 No suitable active agent found, attempting discovery...")

    available_specs = state.get("available_agent_specs", [])
    matching_specs = find_matching_agent_specs(user_message, available_specs)

    if matching_specs:
        # Take the first matching spec
        selected_spec = matching_specs[0]
        agent_name = selected_spec["name"]

        # Check if already discovered
        discovered_agents = state.get("discovered_agents", set())
        if agent_name not in discovered_agents:
            print(f"📋 Discovering and creating agent: {agent_name}")

            try:
                # Create the agent
                new_agent = create_agent_from_spec(selected_spec)

                # Add to active agents
                new_agents = agents.copy()
                new_agents[agent_name] = new_agent

                # Add capability
                new_capabilities = agent_capabilities.copy()
                new_capabilities[agent_name] = AgentCapability(
                    name=selected_spec["name"],
                    agent_type=selected_spec["agent_type"],
                    description=selected_spec["description"],
                    specialties=selected_spec["specialties"],
                    tools=selected_spec.get("tools", []),
                    active=True,
                )

                # Add to discovered
                new_discovered = discovered_agents.copy()
                new_discovered.add(agent_name)

                print(f"✅ Successfully created and added {agent_name}")

                return {
                    "messages": [
                        AIMessage(
                            content=f"Discovered and created {agent_name} specialist for this task."
                        )
                    ],
                    "agents": new_agents,
                    "agent_capabilities": new_capabilities,
                    "discovered_agents": new_discovered,
                    "current_agent": agent_name,
                    "next_agent": agent_name,
                    "agent_task": user_message,
                }

            except Exception as e:
                print(f"❌ Failed to create agent {agent_name}: {e}")
                return {
                    "messages": [
                        AIMessage(content=f"Failed to create specialist agent: {e}")
                    ],
                    "current_agent": "",
                    "next_agent": "",
                    "agent_task": "",
                }
        else:
            # Agent exists but not active
            print(f"🔄 Reactivating existing agent: {agent_name}")
            new_capabilities = agent_capabilities.copy()
            new_capabilities[agent_name].active = True

            return {
                "messages": [
                    AIMessage(content=f"Reactivated {agent_name} for this task.")
                ],
                "agent_capabilities": new_capabilities,
                "current_agent": agent_name,
                "next_agent": agent_name,
                "agent_task": user_message,
            }

    # No matching agent specs found
    available_names = [spec["name"] for spec in available_specs]
    active_agents = [name for name, cap in agent_capabilities.items() if cap.active]

    return {
        "messages": [
            AIMessage(
                content=f"No suitable specialist found for this task. Active agents: {active_agents}. Available for discovery: {available_names}"
            )
        ],
        "current_agent": "",
        "next_agent": "",
        "agent_task": "",
    }


async def agent_execution_node(state: DynamicAgentDiscoveryState) -> dict[str, Any]:
    """Execute the selected/discovered agent."""
    agent_name = state.get("next_agent")
    task = state.get("agent_task")

    if not agent_name or not task:
        return {"agent_response": "No agent or task specified"}

    # Get agent from active agents
    agents = state.get("agents", {})
    agent = agents.get(agent_name)

    if not agent:
        return {"agent_response": f"Agent '{agent_name}' not found in active agents"}

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

        return {
            "agent_response": str(result),
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
            "agent_response": f"Error executing {agent_name}: {e!s}",
            "messages": [AIMessage(content=f"Error with {agent_name}: {e!s}")],
            "current_agent": "",
            "next_agent": "",
            "agent_task": "",
        }


def route_discovery_supervisor(
    state: DynamicAgentDiscoveryState,
) -> Literal["execute", "end"]:
    """Route based on supervisor decision."""
    if state.get("next_agent") and state.get("agent_task"):
        return "execute"
    return "end"


async def test_dynamic_agent_discovery_supervisor():
    """Test the dynamic agent discovery supervisor."""
    print("🚀 Starting Dynamic Agent Discovery Supervisor Test")

    # Create initial setup
    print("\n📋 Setting up initial state...")
    initial_agents = create_initial_agents()
    initial_capabilities = create_initial_capabilities()
    available_specs = create_available_agent_specs()

    print("✅ Initial setup:")
    print(f"  - Active agents: {list(initial_agents.keys())}")
    print(f"  - Available for discovery: {[spec['name'] for spec in available_specs]}")

    # Build the supervisor graph
    print("\n🏗️ Building dynamic supervisor graph...")
    workflow = StateGraph(DynamicAgentDiscoveryState)

    # Add nodes
    workflow.add_node("supervisor", supervisor_discovery_node)
    workflow.add_node("execute", agent_execution_node)

    # Set up routing
    workflow.set_entry_point("supervisor")
    workflow.add_conditional_edges(
        "supervisor", route_discovery_supervisor, {"execute": "execute", "end": END}
    )
    workflow.add_edge("execute", "supervisor")  # Loop back

    # Compile
    app = workflow.compile()
    print("✅ Graph compiled successfully")

    # Test 1: Basic task (use existing agent)
    print("\n" + "=" * 60)
    print("💬 Test 1: Basic conversation (existing agent)")
    print("=" * 60)

    state1 = {
        "messages": [HumanMessage(content="Hello, how are you today?")],
        "agents": initial_agents,
        "agent_capabilities": initial_capabilities,
        "discovered_agents": set(),
        "available_agent_specs": available_specs,
        "current_agent": "",
        "agent_task": "",
        "agent_response": "",
        "next_agent": "",
        "discovery_attempts": 0,
    }

    result1 = await app.ainvoke(state1)
    print(f"📤 Result: {result1.get('agent_response', 'No response')}")
    print(f"🎯 Used agent: {result1.get('current_agent', 'None')}")

    # Test 2: Math task (should discover math_expert)
    print("\n" + "=" * 60)
    print("🧮 Test 2: Math calculation (discover specialist)")
    print("=" * 60)

    state2 = {
        "messages": [
            HumanMessage(content="Please calculate 15 * 23 + 47 and explain the steps")
        ],
        "agents": result1.get("agents", initial_agents),
        "agent_capabilities": result1.get("agent_capabilities", initial_capabilities),
        "discovered_agents": result1.get("discovered_agents", set()),
        "available_agent_specs": available_specs,
        "current_agent": "",
        "agent_task": "",
        "agent_response": "",
        "next_agent": "",
        "discovery_attempts": 0,
    }

    result2 = await app.ainvoke(state2)
    print(f"📤 Result: {result2.get('agent_response', 'No response')}")
    print(f"🎯 Used agent: {result2.get('current_agent', 'None')}")
    print(f"🔍 Discovered agents: {result2.get('discovered_agents', set())}")

    # Test 3: Research task (should discover research_specialist)
    print("\n" + "=" * 60)
    print("🔬 Test 3: Research task (discover specialist)")
    print("=" * 60)

    state3 = {
        "messages": [
            HumanMessage(
                content="Research the latest trends in artificial intelligence"
            )
        ],
        "agents": result2.get("agents", {}),
        "agent_capabilities": result2.get("agent_capabilities", {}),
        "discovered_agents": result2.get("discovered_agents", set()),
        "available_agent_specs": available_specs,
        "current_agent": "",
        "agent_task": "",
        "agent_response": "",
        "next_agent": "",
        "discovery_attempts": 0,
    }

    result3 = await app.ainvoke(state3)
    print(f"📤 Result: {result3.get('agent_response', 'No response')}")
    print(f"🎯 Used agent: {result3.get('current_agent', 'None')}")
    print(f"🔍 Discovered agents: {result3.get('discovered_agents', set())}")

    # Test 4: Planning task (should discover planning_agent)
    print("\n" + "=" * 60)
    print("📋 Test 4: Planning task (discover specialist)")
    print("=" * 60)

    state4 = {
        "messages": [
            HumanMessage(
                content="Create a strategic plan for launching a new mobile app"
            )
        ],
        "agents": result3.get("agents", {}),
        "agent_capabilities": result3.get("agent_capabilities", {}),
        "discovered_agents": result3.get("discovered_agents", set()),
        "available_agent_specs": available_specs,
        "current_agent": "",
        "agent_task": "",
        "agent_response": "",
        "next_agent": "",
        "discovery_attempts": 0,
    }

    result4 = await app.ainvoke(state4)
    print(f"📤 Result: {result4.get('agent_response', 'No response')}")
    print(f"🎯 Used agent: {result4.get('current_agent', 'None')}")
    print(f"🔍 Discovered agents: {result4.get('discovered_agents', set())}")

    # Test 5: Another math task (should reuse existing math_expert)
    print("\n" + "=" * 60)
    print("🧮 Test 5: Another math task (reuse specialist)")
    print("=" * 60)

    state5 = {
        "messages": [HumanMessage(content="What is 89 * 76?")],
        "agents": result4.get("agents", {}),
        "agent_capabilities": result4.get("agent_capabilities", {}),
        "discovered_agents": result4.get("discovered_agents", set()),
        "available_agent_specs": available_specs,
        "current_agent": "",
        "agent_task": "",
        "agent_response": "",
        "next_agent": "",
        "discovery_attempts": 0,
    }

    result5 = await app.ainvoke(state5)
    print(f"📤 Result: {result5.get('agent_response', 'No response')}")
    print(f"🎯 Used agent: {result5.get('current_agent', 'None')}")

    # Final summary
    print("\n" + "=" * 60)
    print("📊 FINAL DYNAMIC DISCOVERY SUMMARY")
    print("=" * 60)

    final_agents = result5.get("agents", {})
    final_capabilities = result5.get("agent_capabilities", {})
    final_discovered = result5.get("discovered_agents", set())

    print("🎯 Discovery Results:")
    print(f"  - Started with: {len(initial_agents)} agents")
    print(f"  - Ended with: {len(final_agents)} agents")
    print(f"  - Total discovered: {len(final_discovered)} agents")
    print(f"  - Available for discovery: {len(available_specs)} specs")

    print("\n🤖 Active Agents:")
    for name, capability in final_capabilities.items():
        if capability.active:
            status = "🆕 Discovered" if name in final_discovered else "🔄 Initial"
            print(f"  - {name}: {capability.description} {status}")

    print("\n🔧 Agent Specialties:")
    for name, capability in final_capabilities.items():
        if capability.active:
            specialties = ", ".join(capability.specialties[:3])  # Show first 3
            print(f"  - {name}: {specialties}")

    print("\n🎉 Dynamic Agent Discovery Supervisor Test Complete!")
    print("✨ Successfully demonstrated dynamic agent discovery and reuse!")

    return {
        "final_agents": final_agents,
        "final_capabilities": final_capabilities,
        "discovered_agents": final_discovered,
        "results": [result1, result2, result3, result4, result5],
    }


if __name__ == "__main__":
    asyncio.run(test_dynamic_agent_discovery_supervisor())
