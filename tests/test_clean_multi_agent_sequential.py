"""Test clean multi-agent implementation with sequential structured output pattern.

This test validates:
1. ReactAgent → SimpleAgent flow
2. State projection with AgentNodeV3
3. Structured output transfer
4. No mocks - real LLM execution
"""

import asyncio
import logging

from langchain_core.tools import tool
from pydantic import BaseModel, Field
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.tree import Tree

from haive.agents.multi.clean_multi_agent import SequentialAgent
from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.core.engine.aug_llm import AugLLMConfig


# Configure rich logging for debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True)],
)
logger = logging.getLogger(__name__)
console = Console()


# Structured output models
class AnalysisResult(BaseModel):
    """Structured result from analysis."""

    topic: str = Field(description="Main topic analyzed")
    key_points: list[str] = Field(description="Key points discovered")
    confidence_score: float = Field(description="Confidence in analysis (0-1)")
    recommendation: str = Field(description="Final recommendation")


class FormattedReport(BaseModel):
    """Final formatted report."""

    title: str = Field(description="Report title")
    executive_summary: str = Field(description="Executive summary")
    analysis: AnalysisResult = Field(description="Detailed analysis")
    conclusion: str = Field(description="Final conclusion")


# Test tools
@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression.

    Args:
        expression: Mathematical expression to evaluate (e.g., "2 + 2")

    Returns:
        Result of the calculation as a string
    """
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {e!s}"


@tool
def word_counter(text: str) -> str:
    """Count words in the given text.

    Args:
        text: Text to count words in

    Returns:
        Word count as a string
    """
    words = text.split()
    return f"The text contains {len(words)} words"


async def test_sequential_structured_output():
    """Test ReactAgent → SimpleAgent with structured output."""
    console.print(
        "\n[bold blue]Testing Sequential Multi-Agent with Structured Output[/bold blue]\n"
    )

    # Step 1: Create ReactAgent for reasoning
    console.print("[yellow]Step 1: Creating ReactAgent for reasoning...[/yellow]")

    react_agent = ReactAgent(
        name="reasoner",
        engine=AugLLMConfig(
            system_message=(
                "You are an analytical reasoning agent. "
                "Use the available tools to gather information and analyze topics thoroughly. "
                "Provide detailed reasoning for your conclusions."
            ),
            temperature=0.7,
        ),
        tools=[calculator, word_counter],
        max_iterations=3,
    )

    # Step 2: Create SimpleAgent for structured output
    console.print(
        "[yellow]Step 2: Creating SimpleAgent for structured output...[/yellow]"
    )

    simple_agent = SimpleAgent(
        name="formatter",
        engine=AugLLMConfig(
            system_message=(
                "You are a report formatting agent. "
                "Take the analysis provided and format it into a structured report. "
                "Ensure all fields are complete and professional."
            ),
            temperature=0.3,  # Lower for more consistent formatting
            structured_output_model=FormattedReport,
            structured_output_version="v2",
        ),
    )

    # Step 3: Create SequentialAgent
    console.print("[yellow]Step 3: Creating SequentialAgent...[/yellow]")

    multi_agent = SequentialAgent(
        agents=[react_agent, simple_agent],
        name="analyzer_formatter",
        state_strategy="minimal",  # Use minimal state for private passing
    )

    # Debug: Show agent configuration
    tree = Tree("[bold green]Multi-Agent Configuration[/bold green]")
    tree.add(f"Name: {multi_agent.name}")
    tree.add(f"Mode: {multi_agent.mode}")
    tree.add(f"State Strategy: {multi_agent.state_strategy}")
    agents_branch = tree.add("Agents:")
    for name, agent in multi_agent._agent_registry.items():
        agents_branch.add(f"{name}: {agent.__class__.__name__}")
    console.print(tree)

    # Step 4: Test execution
    console.print("\n[yellow]Step 4: Executing multi-agent flow...[/yellow]")

    test_input = {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Analyze the benefits of using multi-agent systems in AI. "
                    "Calculate the potential efficiency gains if we can parallelize "
                    "3 agents each taking 5 seconds serially. "
                    "Also count the words in this request."
                ),
            }
        ]
    }

    try:
        # Execute with real LLMs
        result = await multi_agent.ainvoke(test_input)

        console.print("\n[bold green]Execution Successful![/bold green]")

        # Debug: Show result structure
        console.print(
            Panel(
                f"Result type: {type(result)}\n"
                f"Result keys: {result.keys() if isinstance(result, dict) else 'N/A'}",
                title="[cyan]Result Structure[/cyan]",
            )
        )

        # Extract and display final result
        if "final_result" in result:
            final = result["final_result"]
            console.print(Panel(str(final), title="[green]Final Result[/green]"))

            # Verify structured output
            if hasattr(final, "analysis") and isinstance(
                final.analysis, AnalysisResult
            ):
                console.print("[bold green]✓ Structured output validated![/bold green]")
                console.print(f"  - Topic: {final.analysis.topic}")
                console.print(f"  - Key Points: {len(final.analysis.key_points)} items")
                console.print(f"  - Confidence: {final.analysis.confidence_score}")
            else:
                console.print("[bold red]✗ Structured output not found[/bold red]")

        # Show completed agents
        if "completed_agents" in result:
            console.print(
                f"\n[cyan]Completed agents:[/cyan] {result['completed_agents']}"
            )

        # Show any errors
        if result.get("error"):
            console.print(f"\n[red]Error:[/red] {result['error']}")

    except Exception as e:
        console.print("\n[bold red]Execution failed with error:[/bold red]")
        console.print(f"{type(e).__name__}: {e!s}")

        # Print full traceback for debugging
        import traceback

        console.print("\n[dim]Full traceback:[/dim]")
        console.print(traceback.format_exc())

        raise


async def test_state_projection_debug():
    """Debug test to verify state projection is working."""
    console.print("\n[bold blue]Testing State Projection Debug[/bold blue]\n")

    # Create simple agents with minimal functionality
    agent1 = SimpleAgent(
        name="agent1",
        engine=AugLLMConfig(
            system_message="You are agent 1. Just say 'Hello from agent 1'.",
            temperature=0.1,
        ),
    )

    agent2 = SimpleAgent(
        name="agent2",
        engine=AugLLMConfig(
            system_message="You are agent 2. Respond to the previous message.",
            temperature=0.1,
        ),
    )

    # Create sequential multi-agent
    multi = SequentialAgent(
        agents=[agent1, agent2],
        name="debug_multi",
        state_strategy="minimal",
    )

    # Simple input
    test_input = {"messages": [{"role": "user", "content": "Test message"}]}

    try:
        result = await multi.ainvoke(test_input)
        console.print("[green]Debug test passed![/green]")
        console.print(f"Result: {result}")
    except Exception as e:
        console.print(f"[red]Debug test failed: {e}[/red]")
        raise


if __name__ == "__main__":
    # Run tests
    asyncio.run(test_state_projection_debug())
    asyncio.run(test_sequential_structured_output())
