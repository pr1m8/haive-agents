"""Test if multi-agent execution works despite the warning."""

import asyncio
import os
import sys

sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-agents/src")
sys.path.insert(0, "/home/will/Projects/haive/backend/haive/packages/haive-core/src")

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from rich.console import Console

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent

console = Console()


async def test_simple_execution():
    """Test if execution works despite the warning."""

    console.print("\n[bold blue]Testing Multi-Agent Execution[/bold blue]\n")

    # Create agents
    agent1 = SimpleAgent(
        name="agent1",
        engine=AugLLMConfig(system_message="You are agent 1. Say hello from agent 1."),
    )

    agent2 = SimpleAgent(
        name="agent2",
        engine=AugLLMConfig(
            system_message="You are agent 2. Respond to the previous message."
        ),
    )

    # Create multi-agent
    multi = ProperMultiAgent(
        name="test_multi", agents=[agent1, agent2], execution_mode="sequential"
    )

    console.print(f"Multi-agent created: {multi.name}")
    console.print(f"Agents: {list(multi.agents.keys())}")

    try:
        # Test input
        test_input = {"messages": [HumanMessage(content="Hello!")]}

        # Execute
        console.print("\n[yellow]Starting execution...[/yellow]")
        result = await multi.ainvoke(test_input)

        console.print("\n[bold green]Execution completed![/bold green]")
        console.print(f"Result type: {type(result)}")
        console.print(
            f"Result keys: {list(result.keys()) if isinstance(result, dict) else 'Not a dict'}"
        )

        # Check messages
        if isinstance(result, dict) and "messages" in result:
            console.print(f"Messages count: {len(result['messages'])}")
            if result["messages"]:
                last_message = result["messages"][-1]
                console.print(f"Last message: {last_message.content[:100]}...")

        return True

    except Exception as e:
        console.print(
            f"\n[bold red]Execution failed: {type(e).__name__}: {str(e)}[/bold red]"
        )
        import traceback

        console.print(traceback.format_exc())
        return False


if __name__ == "__main__":
    success = asyncio.run(test_simple_execution())
    if success:
        console.print("\n[bold green]✅ Multi-agent execution working![/bold green]")
    else:
        console.print("\n[bold red]❌ Multi-agent execution failed![/bold red]")
