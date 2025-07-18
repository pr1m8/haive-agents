#!/usr/bin/env python3
"""
Example: DynamicReactAgent with Dynamic Tool Discovery

This example demonstrates the DynamicReactAgent's ability to:
1. Start with basic tools
2. Discover and load new tools dynamically
3. Use both discovery agents and RAG-based tool finding
4. Show the "tool that exists to search for other tools" functionality

Run with: poetry run python examples/dynamic_react_agent_example.py
"""

import asyncio

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.tools import tool

from haive.agents.react.dynamic_react_agent import DynamicReactAgent


@tool
def calculator(expression: str) -> float:
    """Calculate mathematical expression."""
    try:
        return eval(expression)
    except:
        return 0.0


@tool
def text_processor(text: str) -> str:
    """Process text by converting to uppercase."""
    return text.upper()


@tool
def word_counter(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def main():
    """Main demonstration of DynamicReactAgent capabilities."""

    print("🚀 DynamicReactAgent Example")
    print("=" * 50)

    # Example 1: Agent with pre-registered tools
    print("\n1️⃣ Creating agent with pre-registered tools...")

    tools = [
        {
            "id": "calc",
            "name": "Calculator",
            "description": "Mathematical calculations",
            "component": calculator,
            "category": "math",
        },
        {
            "id": "text_proc",
            "name": "Text Processor",
            "description": "Text processing operations",
            "component": text_processor,
            "category": "text",
        },
    ]

    agent = DynamicReactAgent.create_with_tools(
        name="demo_agent",
        tools=tools,
        engine=AugLLMConfig(
            system_message="You are a helpful assistant with dynamic tool capabilities."
        ),
    )

    print(f"✅ Agent created: {agent.name}")
    print(f"📁 Initial tools: {len(agent.engine.tools)} tools")

    # Show that the agent has the discovery tool
    discovery_tools = [
        tool
        for tool in agent.engine.tools
        if hasattr(tool, "name") and "discover_and_load_tools" in tool.name
    ]

    if discovery_tools:
        print(f"🔍 Discovery tool available: {discovery_tools[0].name}")
        print("   This tool can search for and load other tools dynamically!")

    # Example 2: Agent with discovery capabilities
    print("\n2️⃣ Creating agent with discovery capabilities...")

    discovery_agent = DynamicReactAgent.create_with_discovery(
        name="discovery_agent", document_path="@haive-tools", engine=AugLLMConfig()
    )

    print(f"✅ Discovery agent created: {discovery_agent.name}")
    print(
        f"📋 Discovery config: {getattr(discovery_agent, '_discovery_config', 'Not set')}"
    )

    # Example 3: Agent with RAG-based tool discovery
    print("\n3️⃣ Creating agent with RAG-based tool discovery...")

    documents = [
        "The calculator tool is useful for mathematical operations like addition, subtraction, multiplication, and division.",
        "Text processing tools can convert text to uppercase, lowercase, or perform other string manipulations.",
        "Word counting tools help analyze text by counting words, characters, or sentences.",
        "Web search tools can find information online and retrieve relevant results.",
        "File processing tools can read, write, and manipulate files in various formats.",
    ]

    rag_agent = DynamicReactAgent.create_with_rag_tooling(
        name="rag_agent", engine=AugLLMConfig(), rag_documents=documents
    )

    print(f"✅ RAG agent created: {rag_agent.name}")
    print(f"📚 RAG documents: {len(documents)} documents")

    # Example 4: Demonstrate tool management
    print("\n4️⃣ Demonstrating tool management...")

    # Create a state for testing
    from haive.agents.react.dynamic_react_agent import DynamicToolState

    state = DynamicToolState()

    # Add some tools to categories
    state.categorize_tool("calculator", "math")
    state.categorize_tool("text_processor", "text")
    state.categorize_tool("word_counter", "text")

    # Track usage
    state.track_tool_usage("calculator")
    state.track_tool_usage("calculator")
    state.track_tool_usage("text_processor")

    print(f"📊 Tool categories: {dict(state.tool_categories)}")
    print(f"📈 Tool usage: {dict(state.tool_usage_stats)}")

    # Get tools by category
    math_tools = state.get_tools_by_category("math")
    text_tools = state.get_tools_by_category("text")

    print(f"🔢 Math tools: {math_tools}")
    print(f"📝 Text tools: {text_tools}")

    # Example 5: Show the dynamic discovery tool in action
    print("\n5️⃣ Testing dynamic tool discovery...")

    # Test the discovery tool functionality
    discovery_tool = discovery_tools[0] if discovery_tools else None
    if discovery_tool:
        print(f"🔍 Testing discovery tool: {discovery_tool.name}")

        # Test discovery for different tasks
        test_queries = [
            "mathematical calculations",
            "text processing",
            "data visualization",
            "web scraping",
        ]

        for query in test_queries:
            try:
                result = discovery_tool.invoke({"task_description": query})
                print(f"   Query: '{query}' -> {result}")
            except Exception as e:
                print(f"   Query: '{query}' -> Error: {e}")

    print("\n🎉 Demo completed!")
    print("\nKey features demonstrated:")
    print("✅ Dynamic tool registration and management")
    print("✅ Multiple factory methods for different use cases")
    print("✅ Tool categorization and usage tracking")
    print("✅ Discovery agent integration")
    print("✅ RAG-based tool discovery")
    print("✅ The 'tool that searches for other tools' functionality")
    print("✅ Recompilation mixin for dynamic updates")
    print("✅ MetaStateSchema integration")


if __name__ == "__main__":
    main()
