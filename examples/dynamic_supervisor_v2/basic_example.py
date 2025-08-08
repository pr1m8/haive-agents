#!/usr/bin/env python3
"""Basic example of Dynamic Supervisor V2.

This example demonstrates:
- Creating a supervisor with predefined agent specs
- Automatic agent creation based on task matching
- Task routing to appropriate agents
- Performance metrics tracking
"""

import asyncio
import logging
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.dynamic_supervisor_v2 import (
    AgentSpec,
    DynamicSupervisor,
    create_dynamic_supervisor,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define tools for agents
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions."""
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating {expression}: {str(e)}"


@tool
def write_content(topic: str, style: str = "informative") -> str:
    """Generate content on a given topic."""
    return f"""# {topic}

This is a {style} piece about {topic}.

## Introduction
{topic} is an important subject that deserves attention.

## Key Points
- First important aspect of {topic}
- Second key consideration
- Third significant element

## Conclusion
In summary, {topic} represents a fascinating area of study.
"""


@tool
def analyze_data(data: str) -> str:
    """Analyze data and provide insights."""
    word_count = len(data.split())
    char_count = len(data)

    return f"""Data Analysis Results:
- Total words: {word_count}
- Total characters: {char_count}
- Average word length: {char_count / word_count if word_count > 0 else 0:.1f}
- Data preview: {data[:100]}...
"""


def create_agent_specs() -> List[AgentSpec]:
    """Create agent specifications for the supervisor."""
    return [
        AgentSpec(
            name="mathematician",
            agent_type="ReactAgent",
            description="Expert in mathematical calculations and problem solving",
            specialties=["math", "calculation", "arithmetic", "algebra"],
            tools=[calculator],
            config={
                "temperature": 0.1,
                "system_message": (
                    "You are a mathematics expert. Use the calculator tool "
                    "for all calculations. Show your work step by step."
                ),
            },
            priority=10,
        ),
        AgentSpec(
            name="content_creator",
            agent_type="ReactAgent",
            description="Creative writer and content generation specialist",
            specialties=["writing", "content", "creative", "documentation"],
            tools=[write_content],
            config={
                "temperature": 0.8,
                "system_message": (
                    "You are a creative content writer. Use the write_content "
                    "tool to generate high-quality content on any topic."
                ),
            },
        ),
        AgentSpec(
            name="data_analyst",
            agent_type="ReactAgent",
            description="Data analysis and insights expert",
            specialties=["data", "analysis", "statistics", "insights"],
            tools=[analyze_data],
            config={
                "temperature": 0.3,
                "system_message": (
                    "You are a data analyst. Use the analyze_data tool to "
                    "extract insights and provide analytical summaries."
                ),
            },
        ),
        AgentSpec(
            name="general_assistant",
            agent_type="SimpleAgentV3",
            description="General purpose assistant for various tasks",
            specialties=["general", "help", "assistant", "question"],
            config={
                "temperature": 0.7,
                "system_message": (
                    "You are a helpful general assistant. Provide clear, "
                    "concise, and accurate responses to any questions."
                ),
            },
            priority=0,  # Lower priority, used as fallback
        ),
    ]


async def main():
    """Run the basic example."""
    print("\n" + "=" * 60)
    print("Dynamic Supervisor V2 - Basic Example")
    print("=" * 60 + "\n")

    # Create agent specifications
    agent_specs = create_agent_specs()
    print(f"Created {len(agent_specs)} agent specifications:")
    for spec in agent_specs:
        print(f"  - {spec.name}: {spec.description}")
    print()

    # Create the supervisor
    supervisor = create_dynamic_supervisor(
        name="task_coordinator",
        agent_specs=agent_specs,
        max_agents=10,
        auto_discover=True,
    )
    print("✅ Dynamic Supervisor created\n")

    # Test tasks for different agents
    test_tasks = [
        "Calculate the compound interest on $1000 at 5% annual rate for 10 years",
        "Write a blog post about artificial intelligence",
        "Analyze this data: 'Sales increased by 25% in Q3 compared to Q2'",
        "What is the capital of France?",
        "Calculate 15 * 23 + 47 / 3",
    ]

    print("Running test tasks...\n")

    for i, task in enumerate(test_tasks, 1):
        print(f"Task {i}: {task}")
        print("-" * 40)

        try:
            result = await supervisor.arun(task)
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")

    # Display metrics
    print("\n" + "=" * 60)
    print("Performance Metrics")
    print("=" * 60 + "\n")

    metrics = supervisor.get_metrics()

    # Supervisor metrics
    sup_metrics = metrics["supervisor"]
    print("Supervisor Statistics:")
    print(f"  Total tasks: {sup_metrics['total_tasks']}")
    print(f"  Success rate: {sup_metrics['success_rate']:.1%}")
    print(f"  Total execution time: {sup_metrics['total_execution_time']:.2f}s")
    print(f"  Agents created: {sup_metrics['agent_creations']}")
    print(f"  Uptime: {sup_metrics['uptime_hours']:.3f} hours\n")

    # Agent metrics
    print("Agent Statistics:")
    for agent_name, stats in metrics["agents"].items():
        print(f"\n  {agent_name}:")
        print(f"    Tasks completed: {stats['task_count']}")
        print(f"    Success rate: {stats['success_rate']:.1%}")
        print(f"    Avg execution time: {stats['avg_execution_time']:.2f}s")
        print(f"    Current state: {stats['state']}")

    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
