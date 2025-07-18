"""Example demonstrating DynamicToolDiscoverySupervisor capabilities.

This example shows how the supervisor can:
1. Discover tools dynamically from multiple sources
2. Distribute tools to appropriate agents
3. Route tasks based on available tools and agent capabilities
"""

import asyncio
import os
import tempfile
from typing import Any, Dict

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent import SimpleAgent
from haive.agents.supervisor.dynamic_tool_discovery_supervisor import (
    DynamicToolDiscoverySupervisor,
    ToolDiscoveryMode,
)


# Create some sample tools that can be discovered
@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions.

    Args:
        expression: Mathematical expression to evaluate

    Returns:
        Result of the calculation
    """
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def text_analyzer(text: str) -> Dict[str, Any]:
    """Analyze text for various metrics.

    Args:
        text: Text to analyze

    Returns:
        Dictionary with analysis results
    """
    words = text.split()
    return {
        "word_count": len(words),
        "character_count": len(text),
        "average_word_length": (
            sum(len(word) for word in words) / len(words) if words else 0
        ),
        "unique_words": len(set(words)),
    }


@tool
def web_search(query: str) -> str:
    """Simulate web search functionality.

    Args:
        query: Search query

    Returns:
        Simulated search results
    """
    return f"Search results for '{query}': Found 10 relevant articles about {query}"


async def basic_supervisor_example():
    """Basic example of DynamicToolDiscoverySupervisor."""
    print("\n=== Basic Dynamic Tool Discovery Supervisor Example ===\n")

    # Configure LLM
    config = AugLLMConfig(temperature=0.1)

    # Create agents
    agents = {
        "analyzer": SimpleAgent(name="analyzer", engine=config),
        "executor": ReactAgent(name="executor", engine=config, tools=[]),
    }

    # Create supervisor with initial tools
    supervisor = DynamicToolDiscoverySupervisor(
        name="tool_supervisor",
        agents=agents,
        engine=config,
        tools_to_register=[
            {
                "name": "calculator",
                "description": "Calculate mathematical expressions",
                "func": calculator.func,
            }
        ],
    )

    print(f"Supervisor created with agents: {list(agents.keys())}")
    print(f"Initial tools: {supervisor.discovered_tools}")

    # Run task that needs tool discovery
    result = await supervisor.arun(
        "I need to calculate 25 * 4 and analyze the word 'supervisor'"
    )
    print(f"\nResult: {result}")

    # Check discovered tools
    print(f"\nDiscovered tools after execution: {supervisor.discovered_tools}")


async def factory_method_example():
    """Example using factory method with discovery sources."""
    print("\n=== Factory Method with Discovery Sources Example ===\n")

    config = AugLLMConfig(temperature=0.1)

    # Create temporary directory with tool documentation
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create tool documentation
        tool_doc_path = os.path.join(temp_dir, "available_tools.md")
        with open(tool_doc_path, "w") as f:
            f.write(
                """# Available Tools Documentation

## Mathematical Tools

### Calculator
- Function: calculator(expression: str) -> float
- Description: Evaluates mathematical expressions
- Example: calculator("2 + 2") returns 4

### Statistics Calculator
- Function: stats_calc(numbers: List[float]) -> Dict
- Description: Calculate statistics (mean, median, std dev)
- Example: stats_calc([1, 2, 3, 4, 5]) returns statistics

## Text Processing Tools

### Text Analyzer
- Function: text_analyzer(text: str) -> Dict
- Description: Analyzes text for various metrics
- Returns: word count, character count, unique words

### Sentiment Analyzer
- Function: sentiment_analyze(text: str) -> str
- Description: Analyzes sentiment of text
- Returns: positive, negative, or neutral

## Web Tools

### Web Search
- Function: web_search(query: str) -> List[str]
- Description: Search the web for information
- Returns: List of relevant results

### URL Scraper
- Function: scrape_url(url: str) -> str
- Description: Extract content from a URL
- Returns: Cleaned text content
"""
            )

        # Create supervisor with discovery configuration
        supervisor = DynamicToolDiscoverySupervisor.create_with_discovery(
            name="discovery_supervisor",
            agents={
                "researcher": SimpleAgent(name="researcher", engine=config),
                "analyst": ReactAgent(name="analyst", engine=config, tools=[]),
                "reporter": SimpleAgent(name="reporter", engine=config),
            },
            engine=config,
            discovery_mode=ToolDiscoveryMode.HYBRID,
            rag_documents_path=temp_dir,
            component_discovery_config={
                "registry_path": "./components",
                "scan_packages": ["haive.tools"],
            },
        )

        print(f"Supervisor created with discovery mode: {supervisor.discovery_mode}")
        print(f"RAG agent configured: {supervisor.rag_tool_agent is not None}")

        # Run task requiring tool discovery
        result = await supervisor.arun(
            "Research the latest Python features, analyze their impact, and create a summary report"
        )
        print(f"\nResult: {result}")

        # Show tool discovery process
        if supervisor.discovered_tools:
            print(f"\nTools discovered during execution:")
            for tool_name in supervisor.discovered_tools:
                print(f"  - {tool_name}")


async def multi_agent_tool_routing_example():
    """Example showing how supervisor routes based on tool availability."""
    print("\n=== Multi-Agent Tool Routing Example ===\n")

    config = AugLLMConfig(temperature=0.1)

    # Create specialized agents
    agent_configs = [
        {"type": "ReactAgent", "name": "math_specialist", "tools": [calculator]},
        {"type": "ReactAgent", "name": "text_specialist", "tools": [text_analyzer]},
        {"type": "SimpleAgent", "name": "general_assistant"},
    ]

    # Create supervisor with agents and tools
    supervisor = DynamicToolDiscoverySupervisor.create_with_agents_and_tools(
        name="routing_supervisor",
        agent_configs=agent_configs,
        engine=config,
        initial_tools=[web_search],
        discovery_mode=ToolDiscoveryMode.COMPONENT_DISCOVERY,
    )

    print("Supervisor configured with specialized agents:")
    for agent_name, agent in supervisor.agents.items():
        tools = []
        if hasattr(agent, "tools") and agent.tools:
            tools = [t.name for t in agent.tools]
        print(f"  - {agent_name}: {tools}")

    # Test routing for different tasks
    tasks = [
        "Calculate the compound interest on $1000 at 5% for 10 years",
        "Analyze this text: 'The quick brown fox jumps over the lazy dog'",
        "Search for information about quantum computing",
    ]

    for task in tasks:
        print(f"\nTask: {task}")

        # Simulate decision making
        from haive.agents.supervisor.types import SupervisorState

        state = SupervisorState(
            messages=[HumanMessage(content=task)], next_agent="", agent_outputs={}
        )

        decision = await supervisor._make_decision(state)
        print(f"Decision: Route to '{decision.next_agent}' - {decision.reasoning}")
        print(f"Confidence: {decision.confidence}")


async def dynamic_tool_loading_example():
    """Example showing dynamic tool loading during execution."""
    print("\n=== Dynamic Tool Loading Example ===\n")

    config = AugLLMConfig(temperature=0.1)

    # Start with minimal tools
    supervisor = DynamicToolDiscoverySupervisor(
        name="dynamic_loader",
        agents={"worker": ReactAgent(name="worker", engine=config, tools=[])},
        engine=config,
        discovery_mode=ToolDiscoveryMode.HYBRID,
    )

    print(f"Initial tools: {supervisor.discovered_tools}")

    # Simulate tool discovery
    discovery_tool = supervisor.tool_registry.get("discover_and_load_tools")

    # Discover tools for math
    print("\nDiscovering math tools...")
    math_result = discovery_tool.func(
        "I need to perform complex mathematical calculations"
    )
    print(f"Discovery result: {math_result}")

    # Discover tools for text
    print("\nDiscovering text tools...")
    text_result = discovery_tool.func("I need to analyze and process text documents")
    print(f"Discovery result: {text_result}")

    # Show final tool registry
    print(f"\nFinal tool registry: {list(supervisor.tool_registry.keys())}")


async def performance_monitoring_example():
    """Example showing supervisor performance monitoring."""
    print("\n=== Performance Monitoring Example ===\n")

    config = AugLLMConfig(temperature=0.1)

    # Create supervisor with multiple agents
    supervisor = DynamicToolDiscoverySupervisor(
        name="monitoring_supervisor",
        agents={
            "fast_agent": SimpleAgent(name="fast_agent", engine=config),
            "slow_agent": SimpleAgent(name="slow_agent", engine=config),
            "reliable_agent": ReactAgent(
                name="reliable_agent", engine=config, tools=[calculator]
            ),
        },
        engine=config,
        max_discovery_attempts=3,
    )

    print("Running multiple tasks to gather performance data...")

    # Run several tasks
    tasks = [
        "What is 2 + 2?",
        "Calculate 15 * 23",
        "Tell me a fact",
        "What's the weather like?",
        "Compute the factorial of 5",
    ]

    for i, task in enumerate(tasks):
        print(f"\nTask {i+1}: {task}")
        result = await supervisor.arun(task)
        print(f"Completed: {result[:50]}...")

    # Show routing history
    if hasattr(supervisor.state, "routing_history"):
        print("\nRouting History:")
        for route in supervisor.state.get("routing_history", []):
            print(f"  - Routed to: {route}")


async def main():
    """Run all examples."""
    await basic_supervisor_example()
    await factory_method_example()
    await multi_agent_tool_routing_example()
    await dynamic_tool_loading_example()
    await performance_monitoring_example()


if __name__ == "__main__":
    print("Dynamic Tool Discovery Supervisor Examples")
    print("=" * 50)

    # Run examples
    asyncio.run(main())

    print("\n" + "=" * 50)
    print("All examples completed!")
