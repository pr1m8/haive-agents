"""Working Dynamic Supervisor Test - Fixed for Current APIs

This is a fixed version of the dynamic supervisor that works with current haive-agents APIs.
"""

import asyncio
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


# AgentInfo class - fixed version
class AgentInfo(BaseModel):
    """Information about an agent including the agent instance and metadata."""

    agent: Any = Field(..., description="The actual agent instance", exclude=True)
    name: str = Field(..., description="Agent name")
    description: str = Field(..., description="What the agent is good at or used for")
    active: bool = Field(default=True, description="Whether agent is currently active")
    agent_metadata: dict = Field(
        default_factory=dict, description="Serializable agent metadata"
    )

    model_config = {"arbitrary_types_allowed": True}

    def get_agent(self) -> Any:
        """Get the agent instance."""
        return self.agent

    def is_active(self) -> bool:
        """Check if agent is active."""
        return self.active

    def activate(self):
        """Activate the agent."""
        self.active = True

    def deactivate(self):
        """Deactivate the agent."""
        self.active = False


# Create test tools with current API
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


# Fixed function to create test agents
async def create_test_agents() -> dict[str, AgentInfo]:
    """Create test agents for supervisor testing using current APIs."""

    # Math agent with calculation tools
    math_engine = AugLLMConfig(
        temperature=0.1,
        system_message="You are a math specialist. Use the add and multiply tools for calculations.",
    )

    math_agent = SimpleAgentV3(
        name="math_agent", engine=math_engine, tools=[add, multiply]
    )

    # Search agent (simplified - no external search for now)
    search_engine = AugLLMConfig(
        temperature=0.7,
        system_message="You are a web search specialist. You provide helpful research information.",
    )

    search_agent = SimpleAgentV3(name="search_agent", engine=search_engine)

    # Planning agent
    planning_engine = AugLLMConfig(
        temperature=0.5,
        system_message="You are a planning specialist. Create structured plans for tasks.",
    )

    planning_agent = SimpleAgentV3(
        name="planning_agent", engine=planning_engine, tools=[create_plan]
    )

    # Create agent info dictionary
    agents_dict = {
        "search_agent": AgentInfo(
            agent=search_agent,
            name="search_agent",
            description="Web search and research specialist",
            active=True,
        ),
        "math_agent": AgentInfo(
            agent=math_agent,
            name="math_agent",
            description="Mathematical calculations specialist",
            active=True,
        ),
        "planning_agent": AgentInfo(
            agent=planning_agent,
            name="planning_agent",
            description="Task planning and organization specialist",
            active=False,  # Inactive placeholder
        ),
    }

    return agents_dict


# Define state for LangGraph
class DynamicSupervisorState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    agents: dict[str, AgentInfo]
    active_agents: set
    next_agent: str
    agent_task: str
    agent_response: str
    generated_tools: list


async def supervisor_reasoning_node(state: DynamicSupervisorState) -> dict[str, Any]:
    """Supervisor that reasons about which agent to use."""
    # Get the last user message
    user_message = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            user_message = msg.content
            break

    if not user_message:
        return {"messages": [AIMessage(content="No task provided.")]}

    # Analyze the task
    task_lower = user_message.lower()

    # Simple keyword-based routing (in real implementation, use LLM)
    if any(word in task_lower for word in ["search", "find", "look", "research"]):
        agent_choice = "search_agent"
        reasoning = "This task requires web search capabilities."
    elif any(
        word in task_lower
        for word in ["calculate", "math", "add", "multiply", "divide"]
    ):
        agent_choice = "math_agent"
        reasoning = "This task requires mathematical calculations."
    elif any(word in task_lower for word in ["plan", "organize", "strategy", "steps"]):
        agent_choice = "planning_agent"
        reasoning = "This task requires planning and organization."
    else:
        agent_choice = "search_agent"
        reasoning = "Defaulting to search for general queries."

    # Check if agent is active
    if agent_choice not in state.get("active_agents", set()):
        return {
            "messages": [
                AIMessage(
                    content=f"I would use {agent_choice}, but it's not currently active. Available agents: {state['active_agents']}"
                )
            ]
        }

    # Route to the chosen agent
    return {
        "messages": [AIMessage(content=f"{reasoning} Delegating to {agent_choice}.")],
        "next_agent": agent_choice,
        "agent_task": user_message,
    }


async def agent_execution_node(state: DynamicSupervisorState) -> dict[str, Any]:
    """Execute the selected agent - mirrors tool_node pattern."""
    agent_name = state.get("next_agent")
    task = state.get("agent_task")

    if not agent_name or not task:
        return {"agent_response": "No agent or task specified"}

    # Get agent from state (like tool_node gets tools)
    agent_info = state["agents"].get(agent_name)
    if not agent_info:
        return {"agent_response": f"Agent '{agent_name}' not found"}

    # Check if active
    if not agent_info.is_active():
        return {"agent_response": f"Agent '{agent_name}' is inactive"}

    # Get the actual agent
    agent = agent_info.get_agent()

    try:
        # Execute agent using current API
        if hasattr(agent, "arun"):
            result = await agent.arun(task)
        elif hasattr(agent, "run"):
            result = agent.run(task)
        else:
            result = f"Agent {agent_name} has no execution method"

        # Clear routing and return result
        return {
            "agent_response": str(result),
            "messages": [
                AIMessage(content=f"{agent_name} completed: {str(result)[:200]}...")
            ],
            "next_agent": "",
            "agent_task": "",
        }

    except Exception as e:
        import traceback

        traceback.print_exc()
        return {
            "agent_response": f"Error executing {agent_name}: {e!s}",
            "messages": [AIMessage(content=f"Error with {agent_name}: {e!s}")],
            "next_agent": "",
            "agent_task": "",
        }


def route_supervisor(state: DynamicSupervisorState) -> Literal["execute", "end"]:
    """Route based on supervisor decision."""
    if state.get("next_agent") and state.get("agent_task"):
        return "execute"
    return "end"


async def test_dynamic_supervisor():
    """Test the complete dynamic supervisor."""
    print("🚀 Starting Dynamic Supervisor Test")

    # Create test agents
    print("📋 Creating test agents...")
    agents_dict = await create_test_agents()

    print(f"✅ Created {len(agents_dict)} agents:")
    for name, info in agents_dict.items():
        status = "🟢 Active" if info.is_active() else "🔴 Inactive"
        print(f"  - {name}: {info.description} {status}")

    # Build the supervisor graph
    print("\n🏗️ Building supervisor graph...")
    workflow = StateGraph(DynamicSupervisorState)

    # Add the 3 core nodes
    workflow.add_node("supervisor", supervisor_reasoning_node)
    workflow.add_node("execute", agent_execution_node)

    # Set up routing
    workflow.set_entry_point("supervisor")
    workflow.add_conditional_edges(
        "supervisor", route_supervisor, {"execute": "execute", "end": END}
    )
    workflow.add_edge("execute", END)

    # Compile
    app = workflow.compile()
    print("✅ Graph compiled successfully")

    # Test 1: Math calculation
    print("\n🧮 Test 1: Math calculation")
    state1 = {
        "messages": [HumanMessage(content="Please calculate 25 + 15 for me")],
        "agents": agents_dict,
        "active_agents": {"search_agent", "math_agent"},
        "next_agent": "",
        "agent_task": "",
        "agent_response": "",
        "generated_tools": [],
    }

    result1 = await app.ainvoke(state1)
    print(f"📤 Result: {result1.get('agent_response', 'No response')}")

    # Test 2: Search task
    print("\n🔍 Test 2: Search task")
    state2 = {
        "messages": [
            HumanMessage(content="Search for information about Python decorators")
        ],
        "agents": agents_dict,
        "active_agents": {"search_agent", "math_agent"},
        "next_agent": "",
        "agent_task": "",
        "agent_response": "",
        "generated_tools": [],
    }

    result2 = await app.ainvoke(state2)
    print(f"📤 Result: {result2.get('agent_response', 'No response')}")

    # Test 3: Dynamic agent addition
    print("\n➕ Test 3: Dynamic agent addition")
    # Activate the planning agent
    agents_dict["planning_agent"].activate()
    print("✅ Planning agent activated")

    state3 = {
        "messages": [
            HumanMessage(content="Create a plan for learning machine learning")
        ],
        "agents": agents_dict,
        "active_agents": {
            "search_agent",
            "math_agent",
            "planning_agent",
        },  # Now active!
        "next_agent": "",
        "agent_task": "",
        "agent_response": "",
        "generated_tools": [],
    }

    result3 = await app.ainvoke(state3)
    print(f"📤 Result: {result3.get('agent_response', 'No response')}")

    # Test 4: Inactive agent handling
    print("\n🚫 Test 4: Inactive agent handling")
    state4 = {
        "messages": [HumanMessage(content="Please organize my day")],
        "agents": agents_dict,
        "active_agents": {
            "search_agent",
            "math_agent",
        },  # planning_agent not in active set
        "next_agent": "",
        "agent_task": "",
        "agent_response": "",
        "generated_tools": [],
    }

    result4 = await app.ainvoke(state4)
    print(f"📤 Result: {result4.get('agent_response', 'No response')}")

    print("\n🎉 Dynamic Supervisor Test Complete!")

    return {
        "test1_result": result1,
        "test2_result": result2,
        "test3_result": result3,
        "test4_result": result4,
        "agents": agents_dict,
    }


if __name__ == "__main__":
    asyncio.run(test_dynamic_supervisor())
