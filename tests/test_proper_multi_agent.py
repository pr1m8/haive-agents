"""Test proper multi-agent following engines dict pattern."""

import asyncio

import pytest
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from rich.console import Console

from haive.agents.multi.proper_base import ProperMultiAgent
from haive.agents.simple.agent import SimpleAgent

console = Console()


@pytest.mark.asyncio
async def test_proper_multi_agent_engines_pattern():
    """Test that agents follow engines dict pattern."""
    console.print(
        "\n[bold blue]Testing Proper Multi-Agent Engines Pattern[/bold blue]\n"
    )

    # Create agents
    agent1 = SimpleAgent(
        name="agent1", engine=AugLLMConfig(system_message="You are agent 1. Say hello.")
    )

    agent2 = SimpleAgent(
        name="agent2",
        engine=AugLLMConfig(system_message="You are agent 2. Respond to previous."),
    )

    # Test list initialization (should be normalized to dict)
    multi = ProperMultiAgent(
        name="test_multi",
        agents=[agent1, agent2],  # List should be converted to dict
        execution_mode="sequential",
    )

    # Check normalization worked
    console.print(f"Agents dict: {list(multi.agents.keys())}")
    console.print(f"State schema: {multi.state_schema}")

    assert isinstance(multi.agents, dict)
    assert "agent1" in multi.agents
    assert "agent2" in multi.agents

    # Test execution
    result = await multi.ainvoke(
        {"messages": [HumanMessage(content="Start conversation")]}
    )

    console.print(f"Result keys: {list(result.keys())}")
    console.print("[green]Test passed![/green]")


@pytest.mark.asyncio
async def test_single_agent_normalization():
    """Test single agent normalization like engines."""
    console.print("\n[bold blue]Testing Single Agent Normalization[/bold blue]\n")

    # Create single agent
    agent = SimpleAgent(
        name="solo_agent", engine=AugLLMConfig(system_message="You are a solo agent.")
    )

    # Test single agent initialization (should go to agents dict)
    multi = ProperMultiAgent(
        name="solo_multi",
        agent=agent,  # Single agent should be normalized to dict
    )

    # Check normalization
    console.print(f"Agents dict: {list(multi.agents.keys())}")

    assert isinstance(multi.agents, dict)
    assert "solo_agent" in multi.agents
    assert multi.agents["solo_agent"] == agent

    console.print("[green]Single agent normalization passed![/green]")


if __name__ == "__main__":
    asyncio.run(test_proper_multi_agent_engines_pattern())
    asyncio.run(test_single_agent_normalization())
