#!/usr/bin/env python3
"""Simple demonstration of Supervisor Agent.

This example shows the core functionality:
- Creating a supervisor with agent specs
- Automatic agent creation and routing
- Basic task execution
"""

import asyncio

from langchain_core.tools import tool

from haive.agents.supervisor import (
    AgentSpec,
    create_dynamic_supervisor,
)


# Simple tools
@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b


async def main():
    """Run simple demo."""
    print("\nSupervisor Agent - Simple Demo\n")

    # Define two simple agent specs
    specs = [
        AgentSpec(
            name="calculator",
            agent_type="ReactAgent",
            description="Handles mathematical calculations",
            specialties=["math", "calculate", "numbers"],
            tools=[add_numbers, multiply_numbers],
            config={
                "temperature": 0.1,
                "system_message": "You are a calculator. Use tools for all calculations.",
            },
        ),
        AgentSpec(
            name="assistant",
            agent_type="SimpleAgentV3",
            description="General helpful assistant",
            specialties=["general", "help", "explain"],
            config={
                "temperature": 0.7,
                "system_message": "You are a helpful assistant.",
            },
        ),
    ]

    # Create supervisor
    supervisor = create_dynamic_supervisor(name="demo_supervisor", agent_specs=specs)

    print("✅ Supervisor created with 2 agent specifications\n")

    # Test different tasks
    tasks = [
        "Calculate 25 plus 17",
        "What is the capital of France?",
        "Multiply 8 by 9",
    ]

    for task in tasks:
        print(f"Task: {task}")
        result = await supervisor.arun(task)
        print(f"Result: {result}\n")

    # Show metrics
    metrics = supervisor.get_metrics()
    print("\nMetrics:")
    print(f"Total tasks: {metrics['supervisor']['total_tasks']}")
    print(f"Agents created: {metrics['supervisor']['agent_creations']}")

    print("\nActive agents:")
    for name, stats in metrics["agents"].items():
        print(f"  - {name}: {stats['task_count']} tasks")


if __name__ == "__main__":
    asyncio.run(main())
