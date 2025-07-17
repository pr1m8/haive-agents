"""Test multi-agent incrementally with real components.

Start simple and build up complexity.
"""

import asyncio
import logging

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field
from rich.console import Console
from rich.logging import RichHandler

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True)],
)
logger = logging.getLogger(__name__)
console = Console()


# Test 1: Basic two agents working independently
async def test_individual_agents():
    """Test that our agents work individually first."""
    console.print("\n[bold blue]Test 1: Individual Agents[/bold blue]\n")

    # Create SimpleAgent
    simple_agent = SimpleAgent(
        name="simple_test",
        engine=AugLLMConfig(
            system_message="You are a helpful assistant. Keep responses brief.",
            temperature=0.3,
        ),
    )

    # Test SimpleAgent
    console.print("[yellow]Testing SimpleAgent...[/yellow]")
    result = await simple_agent.ainvoke(
        {"messages": [HumanMessage(content="Say hello in 5 words or less")]}
    )
    console.print(f"SimpleAgent result: {result}")

    # Create ReactAgent with a tool
    @tool
    def calculator(expression: str) -> str:
        """Calculate a math expression."""
        try:
            result = eval(expression)
            return f"Result: {result}"
        except Exception as e:
            return f"Error: {e!s}"

    react_agent = ReactAgent(
        name="react_test",
        engine=AugLLMConfig(
            system_message="You are a math assistant. Use the calculator tool.",
            temperature=0.3,
        ),
        tools=[calculator],
        max_iterations=2,
    )

    # Test ReactAgent
    console.print("\n[yellow]Testing ReactAgent...[/yellow]")
    result = await react_agent.ainvoke(
        {"messages": [HumanMessage(content="Calculate 15 * 7")]}
    )
    console.print(f"ReactAgent result: {result}")

    return simple_agent, react_agent


# Test 2: Manual sequential execution
async def test_manual_sequential(simple_agent, react_agent):
    """Test passing output from one agent to another manually."""
    console.print("\n[bold blue]Test 2: Manual Sequential Execution[/bold blue]\n")

    # First agent generates a math problem
    console.print("[yellow]Step 1: SimpleAgent generates problem...[/yellow]")
    result1 = await simple_agent.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content="Generate a simple multiplication problem with two numbers between 10 and 20"
                )
            ]
        }
    )
    console.print(f"Problem generated: {result1}")

    # Extract the response
    if result1.get("messages"):
        problem = result1["messages"][-1].content

        # Second agent solves it
        console.print(f"\n[yellow]Step 2: ReactAgent solves: {problem}[/yellow]")
        result2 = await react_agent.ainvoke(
            {"messages": [HumanMessage(content=f"Solve this problem: {problem}")]}
        )
        console.print(f"Solution: {result2}")


# Test 3: Structured output flow
async def test_structured_output():
    """Test SimpleAgent with structured output."""
    console.print("\n[bold blue]Test 3: Structured Output[/bold blue]\n")

    # Define structured output
    class MathProblem(BaseModel):
        """A math problem with solution."""

        problem: str = Field(description="The math problem")
        solution: int = Field(description="The solution")
        explanation: str = Field(description="How to solve it")

    # Create agent with structured output
    structured_agent = SimpleAgent(
        name="structured_test",
        engine=AugLLMConfig(
            system_message="Generate math problems with solutions.",
            temperature=0.3,
            structured_output_model=MathProblem,
            structured_output_version="v2",
        ),
    )

    # Test it
    result = await structured_agent.ainvoke(
        {"messages": [HumanMessage(content="Create a multiplication problem")]}
    )
    console.print(f"Structured result: {result}")

    # Check if we got structured output
    if "parsed_output" in result:
        console.print(f"\n[green]Parsed output:[/green] {result['parsed_output']}")
    elif "content" in result:
        console.print(f"\n[green]Content:[/green] {result['content']}")


# Test 4: Check MultiAgentState
async def test_multi_agent_state():
    """Test using MultiAgentState directly."""
    console.print("\n[bold blue]Test 4: MultiAgentState[/bold blue]\n")

    from haive.core.schema.prebuilt.multi_agent_state import MultiAgentState

    # Create agents
    agent1 = SimpleAgent(name="agent1", engine=AugLLMConfig())
    agent2 = SimpleAgent(name="agent2", engine=AugLLMConfig())

    # Create state with agents
    state = MultiAgentState(agents=[agent1, agent2])

    console.print(f"Agents in state: {list(state.agents.keys())}")
    console.print(f"Agent states: {state.agent_states}")
    console.print(f"Has messages field: {hasattr(state, 'messages')}")
    console.print(f"Has tools field: {hasattr(state, 'tools')}")

    # Update agent state
    state.update_agent_state("agent1", {"status": "ready"})
    console.print(f"\nAfter update: {state.agent_states}")

    # Set active agent
    state.set_active_agent("agent1")
    console.print(f"Active agent: {state.active_agent}")


async def main():
    """Run all tests incrementally."""
    try:
        # Test 1: Individual agents
        simple_agent, react_agent = await test_individual_agents()

        # Test 2: Manual sequential
        await test_manual_sequential(simple_agent, react_agent)

        # Test 3: Structured output
        await test_structured_output()

        # Test 4: MultiAgentState
        await test_multi_agent_state()

        console.print("\n[bold green]All tests completed![/bold green]")

    except Exception as e:
        console.print(f"\n[bold red]Error: {type(e).__name__}: {e!s}[/bold red]")
        import traceback

        console.print(traceback.format_exc())


if __name__ == "__main__":
    asyncio.run(main())
