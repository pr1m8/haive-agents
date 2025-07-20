"""Debug the setup process."""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from rich.console import Console

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent

console = Console()


async def debug_setup():
    """Debug the setup process step by step."""
    console.print("\n[bold blue]Debug Setup Process[/bold blue]\n")

    # Step 1: Create agents
    console.print("[yellow]Step 1: Create agents[/yellow]")
    agent1 = SimpleAgent(
        name="agent1", engine=AugLLMConfig(system_message="You are agent 1.")
    )
    console.print(f"Agent1 created: {agent1.name}")

    # Step 2: Create multi-agent
    console.print("\n[yellow]Step 2: Create multi-agent[/yellow]")
    multi = ProperMultiAgent(
        name="debug_multi",
        agent=agent1,  # Single agent
    )

    # Check normalization
    console.print(f"Agents dict: {list(multi.agents.keys())}")
    console.print(f"State schema: {multi.state_schema}")
    console.print(f"State schema type: {type(multi.state_schema)}")

    # Step 3: Check if MultiAgentState is being used
    if hasattr(multi.state_schema, "__name__"):
        console.print(f"State schema name: {multi.state_schema.__name__}")

    # Step 4: Check engines
    console.print(f"Engines: {list(multi.engines.keys())}")

    console.print("\n[green]Setup debugging complete![/green]")


if __name__ == "__main__":
    asyncio.run(debug_setup())
