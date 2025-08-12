#!/usr/bin/env python3
"""Dynamic Branching Agent with State-Based Routing.

This example demonstrates a more sophisticated branching pattern where:
1. Initial analysis determines complexity and requirements
2. Dynamic routing based on analysis results
3. Parallel execution for multi-aspect queries
4. Conditional re-routing based on intermediate results
5. Aggregation and final synthesis

Date: August 7, 2025
"""

import asyncio
from enum import Enum
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Enums and Models
class QueryComplexity(str, Enum):
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"


class RequiredCapability(str, Enum):
    CALCULATION = "calculation"
    RESEARCH = "research"
    ANALYSIS = "analysis"
    CREATIVITY = "creativity"
    PLANNING = "planning"


class QueryAnalysis(BaseModel):
    """Detailed analysis of the query."""

    complexity: QueryComplexity = Field(description="Complexity level of the query")
    required_capabilities: list[RequiredCapability] = Field(
        description="List of capabilities needed"
    )
    needs_tools: bool = Field(description="Whether tools are required")
    needs_research: bool = Field(description="Whether research is required")
    needs_synthesis: bool = Field(description="Whether synthesis is required")
    subtasks: list[str] = Field(
        default_factory=list, description="Breakdown of subtasks if complex"
    )


class IntermediateResult(BaseModel):
    """Result from an intermediate agent."""

    agent_name: str = Field(description="Name of the agent")
    success: bool = Field(description="Whether the task succeeded")
    output: str = Field(description="Agent's output")
    confidence: float = Field(ge=0.0, le=1.0)
    needs_followup: bool = Field(default=False)
    suggested_next_agent: str | None = Field(default=None)


class FinalSynthesis(BaseModel):
    """Final synthesized result."""

    query_complexity: QueryComplexity
    agents_used: list[str]
    execution_path: list[str] = Field(description="Path taken through agents")
    synthesis: str = Field(description="Synthesized final answer")
    confidence: float = Field(ge=0.0, le=1.0)
    key_insights: list[str]


# Tools
@tool
def calculator(expression: str) -> str:
    """Perform calculations."""
    try:
        result = eval(expression)
        return f"Calculation result: {result}"
    except:
        return "Error: Invalid expression"


@tool
def data_analyzer(data: str) -> str:
    """Analyze data patterns."""
    return "Data analysis: Found patterns in the data - trend appears to be increasing"


@tool
def research_tool(topic: str) -> str:
    """Research information on a topic."""
    return (
        f"Research on '{topic}': Found comprehensive information from multiple sources"
    )


@tool
def planner_tool(task: str) -> str:
    """Create a plan for a task."""
    return f"Plan for '{task}': 1) Analyze requirements 2) Design solution 3) Implement 4) Test"


# Agent Creation
def create_dynamic_agents():
    """Create agents for dynamic branching workflow."""
    # Query Analyzer - determines routing
    analyzer = SimpleAgentV3(
        name="query_analyzer",
        engine=AugLLMConfig(
            temperature=0.1,
            system_message="Analyze queries to determine complexity and required capabilities.",
            structured_output_model=QueryAnalysis,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    "Analyze this query and determine routing requirements: {messages}",
                ),
            ]
        ),
    )

    # Simple Handler - for basic queries
    simple_handler = SimpleAgentV3(
        name="simple_handler",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="Handle simple, straightforward queries efficiently.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [("system", "{system_message}"), ("human", "{messages}")]
        ),
    )

    # Calculator Agent - for mathematical tasks
    calc_agent = ReactAgent(
        name="calculator_agent",
        engine=AugLLMConfig(
            temperature=0.1,
            system_message="Perform calculations and mathematical analysis.",
        ),
        tools=[calculator, data_analyzer],
    )

    # Research Agent - for information gathering
    research_agent = ReactAgent(
        name="research_agent",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="Conduct thorough research and fact-finding.",
        ),
        tools=[research_tool],
    )

    # Planning Agent - for complex planning tasks
    planning_agent = ReactAgent(
        name="planning_agent",
        engine=AugLLMConfig(
            temperature=0.5, system_message="Create detailed plans and strategies."
        ),
        tools=[planner_tool],
    )

    # Creative Agent - for creative tasks
    creative_agent = SimpleAgentV3(
        name="creative_agent",
        engine=AugLLMConfig(
            temperature=0.8,
            system_message="Generate creative and innovative solutions.",
        ),
    )

    # Synthesis Agent - combines results
    synthesis_agent = SimpleAgentV3(
        name="synthesis_agent",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="Synthesize multiple inputs into coherent final output.",
            structured_output_model=FinalSynthesis,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                (
                    "human",
                    """Synthesize these results:
            
Query: {original_query}
Analysis: {analysis}
Results: {results}
Execution Path: {execution_path}

Create a final synthesis.""",
                ),
            ]
        ),
    )

    return {
        "analyzer": analyzer,
        "simple": simple_handler,
        "calculator": calc_agent,
        "research": research_agent,
        "planning": planning_agent,
        "creative": creative_agent,
        "synthesis": synthesis_agent,
    }


class DynamicRouter:
    """Handles dynamic routing logic."""

    def __init__(self, agents: dict[str, Any]):
        self.agents = agents
        self.execution_path = []

    async def route_query(self, query: str) -> FinalSynthesis:
        """Route query through appropriate agents."""
        print("🔍 Analyzing query...")

        # Step 1: Analyze the query
        analysis_result = await self.agents["analyzer"].arun(
            {"messages": [HumanMessage(content=query)]}
        )

        if not isinstance(analysis_result, QueryAnalysis):
            raise ValueError("Analysis failed")

        print(f"   Complexity: {analysis_result.complexity}")
        print(f"   Capabilities: {', '.join(analysis_result.required_capabilities)}")

        # Step 2: Route based on complexity
        if analysis_result.complexity == QueryComplexity.SIMPLE:
            return await self._handle_simple(query, analysis_result)
        if analysis_result.complexity == QueryComplexity.MODERATE:
            return await self._handle_moderate(query, analysis_result)
        return await self._handle_complex(query, analysis_result)

    async def _handle_simple(
        self, query: str, analysis: QueryAnalysis
    ) -> FinalSynthesis:
        """Handle simple queries."""
        print("\n📄 Handling as simple query...")

        result = await self.agents["simple"].arun(
            {"messages": [HumanMessage(content=query)]}
        )

        self.execution_path = ["analyzer", "simple"]

        # Create synthesis
        return await self._synthesize(query, analysis, [result], self.execution_path)

    async def _handle_moderate(
        self, query: str, analysis: QueryAnalysis
    ) -> FinalSynthesis:
        """Handle moderate complexity queries."""
        print("\n📊 Handling as moderate query...")

        results = []
        agents_used = []

        # Route to appropriate specialist agents
        for capability in analysis.required_capabilities:
            if capability == RequiredCapability.CALCULATION:
                print("   → Routing to calculator agent...")
                result = await self.agents["calculator"].arun(
                    {"messages": [HumanMessage(content=query)]}
                )
                results.append(result)
                agents_used.append("calculator")

            elif capability == RequiredCapability.RESEARCH:
                print("   → Routing to research agent...")
                result = await self.agents["research"].arun(
                    {"messages": [HumanMessage(content=query)]}
                )
                results.append(result)
                agents_used.append("research")

            elif capability == RequiredCapability.CREATIVITY:
                print("   → Routing to creative agent...")
                result = await self.agents["creative"].arun(
                    {"messages": [HumanMessage(content=query)]}
                )
                results.append(result)
                agents_used.append("creative")

        self.execution_path = ["analyzer"] + agents_used

        return await self._synthesize(query, analysis, results, self.execution_path)

    async def _handle_complex(
        self, query: str, analysis: QueryAnalysis
    ) -> FinalSynthesis:
        """Handle complex queries with parallel execution."""
        print("\n🔧 Handling as complex query...")

        # Break down into subtasks
        if analysis.subtasks:
            print(f"   Subtasks identified: {len(analysis.subtasks)}")

        # Execute required agents in parallel where possible
        tasks = []
        agent_names = []

        capability_agent_map = {
            RequiredCapability.CALCULATION: "calculator",
            RequiredCapability.RESEARCH: "research",
            RequiredCapability.PLANNING: "planning",
            RequiredCapability.CREATIVITY: "creative",
            RequiredCapability.ANALYSIS: "calculator",  # Reuse calculator for analysis
        }

        for capability in analysis.required_capabilities:
            agent_name = capability_agent_map.get(capability)
            if agent_name and agent_name in self.agents:
                print(f"   → Scheduling {agent_name} agent...")
                agent = self.agents[agent_name]
                task = agent.arun({"messages": [HumanMessage(content=query)]})
                tasks.append(task)
                agent_names.append(agent_name)

        # Execute in parallel
        print("\n⚡ Executing agents in parallel...")
        results = await asyncio.gather(*tasks)

        self.execution_path = ["analyzer"] + agent_names

        return await self._synthesize(query, analysis, results, self.execution_path)

    async def _synthesize(
        self,
        query: str,
        analysis: QueryAnalysis,
        results: list[Any],
        execution_path: list[str],
    ) -> FinalSynthesis:
        """Synthesize results from multiple agents."""
        print("\n🎯 Synthesizing final result...")

        # Format results for synthesis
        formatted_results = []
        for i, result in enumerate(results):
            if hasattr(result, "content"):
                formatted_results.append(result.content)
            elif isinstance(result, dict) and "messages" in result:
                messages = result["messages"]
                if messages and hasattr(messages[-1], "content"):
                    formatted_results.append(messages[-1].content)
            else:
                formatted_results.append(str(result))

        synthesis_result = await self.agents["synthesis"].arun(
            {
                "original_query": query,
                "analysis": str(analysis),
                "results": "\n\n".join(formatted_results),
                "execution_path": " → ".join(execution_path),
            }
        )

        return synthesis_result


async def test_dynamic_branching():
    """Test the dynamic branching system."""
    print("🌲 Dynamic Branching Agent System")
    print("=" * 60)

    # Create agents and router
    agents = create_dynamic_agents()
    router = DynamicRouter(agents)

    # Test queries of varying complexity
    test_queries = [
        # Simple
        "What is the capital of France?",
        # Moderate - needs calculation
        "Calculate the compound interest on $10,000 at 5% for 10 years",
        # Complex - needs multiple capabilities
        "Create a comprehensive business plan for a sustainable energy startup, including market analysis, financial projections for 5 years, and creative marketing strategies",
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"\n\n{'='*60}")
        print(f"Test {i}: {query}")
        print("=" * 60)

        try:
            result = await router.route_query(query)

            if isinstance(result, FinalSynthesis):
                print("\n✅ Final Synthesis:")
                print(f"   Complexity: {result.query_complexity}")
                print(f"   Agents Used: {', '.join(result.agents_used)}")
                print(f"   Execution Path: {' → '.join(result.execution_path)}")
                print(f"   Confidence: {result.confidence:.0%}")
                print(f"\n   Synthesis: {result.synthesis[:200]}...")
                print("\n   Key Insights:")
                for insight in result.key_insights[:3]:
                    print(f"   • {insight}")
            else:
                print(f"\n   Result: {result}")

        except Exception as e:
            print(f"\n❌ Error: {e}")


async def main():
    """Run dynamic branching examples."""
    await test_dynamic_branching()

    print("\n\n✅ Dynamic branching examples completed!")
    print("\n💡 Advanced Features Demonstrated:")
    print("1. Dynamic routing based on query analysis")
    print("2. Parallel execution for complex queries")
    print("3. Capability-based agent selection")
    print("4. Progressive complexity handling")
    print("5. Structured synthesis of multi-agent results")


if __name__ == "__main__":
    asyncio.run(main())
