#!/usr/bin/env python3
"""Basic Agent Test - Test individual agents with structured output."""

import asyncio
from typing import List

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models
class AnalysisResult(BaseModel):
    """Structured analysis output."""

    topic: str = Field(description="Topic analyzed")
    key_points: List[str] = Field(description="Key points identified")
    summary: str = Field(description="Brief summary")
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score")


async def test_simple_agent_v3():
    """Test SimpleAgentV3 with structured output."""
    print("\n=== Testing SimpleAgentV3 ===\n")

    # Create agent with structured output
    agent = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="You are an expert analyst. Provide structured analysis.",
            structured_output_model=AnalysisResult,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("human", "Analyze this topic: {topic}\nContext: {context}"),
            ]
        ),
        debug=True,
    )

    print(f"Agent created: {agent.name}")
    print(f"Engine type: {type(agent.engine)}")
    print(f"Has structured output: {agent.engine.structured_output_model is not None}")

    # Test execution
    try:
        result = await agent.arun(
            {
                "topic": "The impact of AI on software development",
                "context": "Focus on productivity, code quality, and developer experience",
                "messages": [{"role": "user", "content": "Analyze this topic"}],
            }
        )

        print("\n--- Results ---")
        print(f"Result type: {type(result)}")

        if isinstance(result, dict):
            print("Result is a dictionary:")
            for key, value in result.items():
                print(f"  {key}: {value}")
        elif isinstance(result, AnalysisResult):
            print("Result is AnalysisResult model:")
            print(f"  Topic: {result.topic}")
            print(f"  Key Points: {result.key_points}")
            print(f"  Summary: {result.summary}")
            print(f"  Confidence: {result.confidence}")
        else:
            print(f"Result: {result}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


async def test_react_agent():
    """Test ReactAgent with tools."""
    print("\n\n=== Testing ReactAgent ===\n")

    # Create tools
    @tool
    def calculate(expression: str) -> str:
        """Calculate mathematical expressions."""
        try:
            result = eval(expression)
            return f"The result of {expression} is {result}"
        except:
            return f"Could not calculate {expression}"

    @tool
    def get_info(topic: str) -> str:
        """Get information about a topic."""
        info_db = {
            "python": "Python is a high-level programming language known for simplicity.",
            "ai": "AI refers to machines performing tasks that require human intelligence.",
            "react": "React is a JavaScript library for building user interfaces.",
        }
        return info_db.get(topic.lower(), f"No information found about {topic}")

    # Create ReactAgent
    agent = ReactAgent(
        name="assistant",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message="You are a helpful assistant. Use tools to answer questions.",
            tools=[calculate, get_info],
        ),
    )

    print(f"Agent created: {agent.name}")
    print(f"Tools available: {[t.name for t in agent.engine.tools]}")

    # Test execution
    try:
        # Test 1: Math calculation
        print("\nTest 1: Math calculation")
        result = await agent.arun("What is 25 * 4 + 10?")
        print(f"Result: {result}")

        # Test 2: Information retrieval
        print("\nTest 2: Information retrieval")
        result = await agent.arun("Tell me about Python")
        print(f"Result: {result}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


async def test_sequential_manual():
    """Test sequential execution manually (without MultiAgent)."""
    print("\n\n=== Testing Manual Sequential Execution ===\n")

    # Agent 1: Analyzer
    analyzer = SimpleAgentV3(
        name="analyzer",
        engine=AugLLMConfig(
            temperature=0.4,
            system_message="You are an analyzer. Break down problems into components.",
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("human", "Analyze this problem: {problem}"),
            ]
        ),
    )

    # Agent 2: Solution Designer with structured output
    class Solution(BaseModel):
        approach: str = Field(description="Solution approach")
        steps: List[str] = Field(description="Implementation steps")
        benefits: List[str] = Field(description="Expected benefits")

    designer = SimpleAgentV3(
        name="designer",
        engine=AugLLMConfig(
            temperature=0.5,
            system_message="You are a solution designer. Create practical solutions.",
            structured_output_model=Solution,
        ),
        prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system", "{system_message}"),
                ("human", "Based on this analysis:\n{analysis}\n\nDesign a solution."),
            ]
        ),
    )

    # Execute sequentially
    try:
        problem = "How to improve code review efficiency in large teams"
        print(f"Problem: {problem}\n")

        # Step 1: Analyze
        print("Step 1: Analysis")
        analysis_result = await analyzer.arun(
            {"problem": problem, "messages": [{"role": "user", "content": problem}]}
        )
        print(f"Analysis: {analysis_result}\n")

        # Step 2: Design solution
        print("Step 2: Solution Design")
        solution_result = await designer.arun(
            {
                "analysis": str(analysis_result),
                "messages": [{"role": "user", "content": "Design solution"}],
            }
        )

        print("Solution:")
        if isinstance(solution_result, dict):
            print(f"  Approach: {solution_result.get('approach', 'N/A')}")
            print(f"  Steps: {solution_result.get('steps', [])}")
            print(f"  Benefits: {solution_result.get('benefits', [])}")
        else:
            print(f"  {solution_result}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()


async def main():
    """Run all tests."""
    print("=" * 60)
    print("BASIC AGENT TESTS")
    print("Testing SimpleAgentV3 and ReactAgent individually")
    print("=" * 60)

    await test_simple_agent_v3()
    await test_react_agent()
    await test_sequential_manual()

    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
