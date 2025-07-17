"""Test to demonstrate multi-agent type safety issues and solutions."""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.schema.state_schema import StateSchema
from langchain_core.messages import BaseMessage, HumanMessage
from pydantic import Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent


class ReactPlannerState(StateSchema):
    """State for React agent that plans."""

    messages: list[BaseMessage] = Field(default_factory=list)
    plan: str = Field(default="", description="Generated plan")
    reasoning_steps: list[str] = Field(
        default_factory=list, description="Reasoning trace"
    )


class SimpleFormatterState(StateSchema):
    """State for Simple agent that formats output."""

    messages: list[BaseMessage] = Field(default_factory=list)
    formatted_output: str = Field(default="", description="Formatted result")
    format_type: str = Field(default="markdown", description="Output format")


async def test_multi_agent_type_safety():
    """Test that demonstrates the type safety issue with current multi-agent."""

    # Create agents with specific typed state schemas
    react_planner = ReactAgent(
        name="planner",
        engine=AugLLMConfig(
            system_message="You are a planning agent. Create step-by-step plans."
        ),
        state_schema=ReactPlannerState,  # Custom typed state
    )

    simple_formatter = SimpleAgent(
        name="formatter",
        engine=AugLLMConfig(
            system_message="You are a formatting agent. Format results as markdown."
        ),
        state_schema=SimpleFormatterState,  # Custom typed state
    )

    # The problem: How do we compose these agents while preserving their typed states?

    # Option 1: Use proper_list_multi_agent.py (loses type safety)
    from haive.agents.multi.experiments.proper_list_multi_agent import (
        ProperListMultiAgent,
    )

    multi_agent = ProperListMultiAgent("research_pipeline")
    multi_agent.append(react_planner)
    multi_agent.append(simple_formatter)

    # This forces everything through MultiAgentState, losing ReactPlannerState and SimpleFormatterState

    # The issue: Individual agent states are lost
    # - react_planner expects ReactPlannerState with 'plan' and 'reasoning_steps'
    # - simple_formatter expects SimpleFormatterState with 'formatted_output' and 'format_type'
    # - But MultiAgentState doesn't know about these fields!

    # Let's try to run it
    try:
        result = await multi_agent.ainvoke(
            {"messages": [HumanMessage(content="Create a plan for learning Python")]}
        )

        # Can we access typed fields?

    except Exception as e:
        pass

    # What we need: A multi-agent that preserves individual agent state schemas
    # while still allowing coordination and message passing


if __name__ == "__main__":
    asyncio.run(test_multi_agent_type_safety())
