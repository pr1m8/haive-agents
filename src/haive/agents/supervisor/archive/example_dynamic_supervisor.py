#!/usr/bin/env python
"""Example of using DynamicMultiAgent with real haive agents.

This example shows how to create a dynamic supervisor system that can:
1. Start with a few agents
2. Add specialized agents on demand
3. Route requests intelligently
4. Track performance
"""

import asyncio
import logging

import langchain_core.messages
from langchain_core.tools import tool

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_dynamic_supervisor_system():
    """Create a dynamic supervisor system with real agents."""
    # Import required components
    try:
        from haive.core.engine.aug_llm import AugLLMConfig

        from haive.agents.react.agent import ReactAgent
        from haive.agents.simple.agent import SimpleAgent
        from haive.agents.supervisor.dynamic_multi_agent import DynamicMultiAgent
    except ImportError:
        logger.warning("Failed to import required components")
        return None, None

    # Create engines for different agents

    # Research engine - good at finding information
    research_engine = AugLLMConfig(
        name="research_engine",
        system_message="You are a research specialist. Find and summarize information on any topic. Be thorough and cite sources when possible.",
        temperature=0.3,  # Lower temperature for factual research
    )

    # Writing engine - good at content creation
    writing_engine = AugLLMConfig(
        name="writing_engine",
        system_message="You are a professional writer. Create engaging, well-structured content. Adapt your style to the audience and purpose.",
        temperature=0.7,  # Higher temperature for creativity
    )

    # Analysis engine - good at data analysis
    analysis_engine = AugLLMConfig(
        name="analysis_engine",
        system_message="You are a data analyst. Analyze information, identify patterns, and provide insights. Be precise and data-driven.",
        temperature=0.4,
    )

    # Create initial agents

    # Simple agents for basic tasks
    research_agent = SimpleAgent(name="research_specialist", engine=research_engine)
    research_agent.capability = (
        "research, information gathering, fact-finding, web search"
    )

    writing_agent = SimpleAgent(name="content_writer", engine=writing_engine)
    writing_agent.capability = "writing, content creation, documentation, storytelling"

    # Create dynamic multi-agent system

    supervisor = DynamicMultiAgent(
        name="dynamic_supervisor",
        agents=[research_agent, writing_agent],
        enable_capability_routing=True,
        track_performance=True,
        separation_strategy="smart",  # Smart field separation
    )

    return supervisor, analysis_engine


async def demonstrate_dynamic_capabilities(supervisor, analysis_engine):
    """Demonstrate the dynamic capabilities of the system."""
    # Test 1: Research request

    result1 = await supervisor.ainvoke(
        {
            "messages": [
                langchain_core.messages.HumanMessage(
                    content="Research the latest developments in quantum computing"
                )
            ]
        }
    )

    result1.get("messages", [])[-1]

    # Test 2: Writing request

    await supervisor.ainvoke(
        {
            "messages": [
                langchain_core.messages.HumanMessage(
                    content="Write a blog post introduction about the future of AI"
                )
            ]
        }
    )

    # Test 3: Analysis request (no analyst yet)

    await supervisor.ainvoke(
        {
            "messages": [
                langchain_core.messages.HumanMessage(
                    content="Analyze the trends in the research findings"
                )
            ]
        }
    )

    # Add analysis agent dynamically

    analysis_agent = SimpleAgent(name="data_analyst", engine=analysis_engine)
    analysis_agent.capability = (
        "analysis, data processing, pattern recognition, insights"
    )

    # Register the new agent
    supervisor.register_agent_dynamically(
        analysis_agent, capability="data analysis and insights generation"
    )

    # Test 4: Analysis request with analyst

    await supervisor.ainvoke(
        {
            "messages": [
                langchain_core.messages.HumanMessage(
                    content="Analyze the market trends for AI adoption"
                )
            ]
        }
    )

    # Show performance metrics

    for agent_name in supervisor.agents:
        supervisor.get_agent_performance(agent_name)


async def demonstrate_complex_workflow(supervisor):
    """Demonstrate a complex multi-step workflow."""
    # Initialize conversation
    messages = [
        langchain_core.messages.SystemMessage(
            content="You are part of a research project team."
        ),
        langchain_core.messages.HumanMessage(
            content="Let's research and write about the impact of AI on healthcare"
        ),
    ]

    # Step 1: Research
    result1 = await supervisor.ainvoke({"messages": messages})
    messages = result1.get("messages", messages)

    # Step 2: Analysis
    messages.append(
        langchain_core.messages.HumanMessage(
            content="Now analyze the key findings and identify the main trends"
        )
    )
    result2 = await supervisor.ainvoke({"messages": messages})
    messages = result2.get("messages", messages)

    # Step 3: Writing
    messages.append(
        langchain_core.messages.HumanMessage(
            content="Write a comprehensive report based on the research and analysis"
        )
    )
    result3 = await supervisor.ainvoke({"messages": messages})
    messages = result3.get("messages", messages)

    # Show conversation flow

    # Execution history
    history = supervisor.get_execution_history(limit=5)
    for _i, _entry in enumerate(history):
        pass


async def demonstrate_react_agent_integration(supervisor):
    """Show how to add a ReactAgent with tools."""

    # Create simple tools for demo
    @tool
    def calculator(expression: str) -> str:
        """Perform basic math calculations.

        Args:
            expression: A mathematical expression to evaluate (e.g., '2 + 2', '10 * 5')

        Returns:
            The result of the calculation as a string
        """
        try:
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error calculating: {e!s}"

    @tool
    def web_search(query: str) -> str:
        """Simulate web search functionality.

        Args:
            query: The search query

        Returns:
            Simulated search results
        """
        return f"Search results for '{query}': [Result 1: Example content], [Result 2: More content]"

    # Create engine for ReactAgent
    react_engine = AugLLMConfig(
        name="react_engine",
        system_message="You are a helpful assistant with access to tools. Use them to solve problems step by step.",
        temperature=0.3,
    )

    # Create ReactAgent
    react_agent = ReactAgent(
        name="tool_specialist", engine=react_engine, tools=[calculator, web_search]
    )
    react_agent.capability = "tool usage, calculations, web search, problem solving"

    # Add to supervisor

    supervisor.register_agent_dynamically(
        react_agent, capability="specialized tool usage and problem solving"
    )

    # Test tool usage

    await supervisor.ainvoke(
        {
            "messages": [
                langchain_core.messages.HumanMessage(
                    content="Calculate the compound interest on $10,000 at 5% for 10 years"
                )
            ]
        }
    )

    # Note: In real usage, the ReactAgent would use the calculator tool


async def main():
    """Main example flow."""
    # Create the system
    supervisor, analysis_engine = await create_dynamic_supervisor_system()

    if not supervisor:
        return

    # Demonstrate capabilities
    await demonstrate_dynamic_capabilities(supervisor, analysis_engine)

    # Complex workflow
    await demonstrate_complex_workflow(supervisor)

    # ReactAgent integration
    await demonstrate_react_agent_integration(supervisor)

    # Final summary

    for _agent, _capability in supervisor.get_agent_capabilities().items():
        pass


if __name__ == "__main__":
    asyncio.run(main())
