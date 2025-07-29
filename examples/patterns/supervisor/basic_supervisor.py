#!/usr/bin/env python3
"""Basic Dynamic Supervisor Example.

This example demonstrates how to create a simple dynamic supervisor
that can route tasks to different specialized agents.

Run with:
    poetry run python examples/patterns/supervisor/basic_supervisor.py
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig
from langchain_core.tools import tool

from haive.agents.simple import SimpleAgent
from haive.agents.supervisor import (
    DynamicSupervisor,
    create_with_agents,
)


@tool
def calculate(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e!s}"


async def main():
    """Run the basic supervisor example."""
    # Create specialized agents

    # Math agent
    math_engine = AugLLMConfig(
        name="math_engine",
        llm_config=AzureLLMConfig(model="gpt-4o"),
        tools=[calculate],
        system_message="You are a math expert. Use the calculate tool for mathematical operations.",
    )
    math_agent = SimpleAgent(name="math_agent", engine=math_engine)

    # General assistant agent
    general_engine = AugLLMConfig(
        name="general_engine",
        llm_config=AzureLLMConfig(model="gpt-4o"),
        system_message="You are a helpful general assistant. Answer questions clearly.",
    )
    general_agent = SimpleAgent(name="general_agent", engine=general_engine)

    # Create supervisor with agents
    supervisor = create_with_agents(
        name="task_supervisor",
        agents=[math_agent, general_agent],
        engine=AugLLMConfig(
            llm_config=AzureLLMConfig(model="gpt-4o"),
            temperature=0.0,
            system_message="You are a supervisor that routes tasks to specialized agents. Choose the most appropriate agent for each task.",
        ),
    )

    # Test 1: Math task
    print("Test 1: Math task")
    result1 = await supervisor.arun("Calculate the result of 15 * 23 + 7")
    print(f"Result: {result1}")
    print()

    # Test 2: General task
    print("Test 2: General task")
    result2 = await supervisor.arun("What is the capital of France?")
    print(f"Result: {result2}")
    print()

    # Test 3: Task requiring reasoning about which agent to use
    print("Test 3: Complex task")
    result3 = await supervisor.arun(
        "I need help with both math and general knowledge. First, calculate 100 / 4, then tell me what that number represents in terms of a perfect score."
    )
    print(f"Result: {result3}")
    print()


if __name__ == "__main__":
    asyncio.run(main())
