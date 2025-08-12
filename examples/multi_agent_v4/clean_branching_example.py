#!/usr/bin/env python3
"""Clean Branching Multi-Agent Example.

Demonstrates conditional routing with automatic structured output extraction.

Date: August 7, 2025
"""

import asyncio
import os
from typing import Literal

from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field

from haive.agents.react.agent import ReactAgent
from haive.agents.simple.agent_v3 import SimpleAgentV3


# Structured output models
class QueryClassification(BaseModel):
    """Classification result."""

    category: Literal["technical", "creative", "research"] = Field(
        description="Category"
    )
    confidence: float = Field(ge=0.0, le=1.0)
    reasoning: str = Field(description="Brief reasoning")


class TechnicalAnswer(BaseModel):
    """Technical response."""

    solution: str = Field(description="Technical solution")
    code_example: str | None = Field(default=None, description="Optional code")
    complexity: Literal["beginner", "intermediate", "advanced"]


class CreativeResponse(BaseModel):
    """Creative response."""

    content: str = Field(description="Creative content")
    style: str = Field(description="Writing style used")
    mood: str = Field(description="Mood or tone")


class ResearchFindings(BaseModel):
    """Research findings."""

    summary: str = Field(description="Research summary")
    key_findings: list[str] = Field(description="Key findings list")
    sources_count: int = Field(ge=0, description="Number of sources")


# Tools
@tool
def python_executor(code: str) -> str:
    """Execute Python code snippets."""
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return f"Code executed successfully. Output: {exec_globals.get('result', 'No result variable')}"
    except Exception as e:
        return f"Error: {e!s}"


@tool
def research_database(query: str) -> str:
    """Search research database."""
    return f"Found 5 peer-reviewed studies on '{query}' from 2023-2024"


async def main():
    """Run clean branching example."""
    # Disable verbose logging
    os.environ["HAIVE_LOG_LEVEL"] = "ERROR"

    print("🌳 Clean Branching Multi-Agent Example")
    print("=" * 50)

    # 1. Create classifier
    classifier = SimpleAgentV3(
        name="classifier",
        engine=AugLLMConfig(
            temperature=0.1,
            system_message="Classify queries as technical, creative, or research.",
            structured_output_model=QueryClassification,  # Auto-extraction!
        ),
        verbose=False,
    )

    # 2. Create specialized agents
    technical = ReactAgent(
        name="technical",
        engine=AugLLMConfig(
            temperature=0.2,
            system_message="Provide technical solutions with code examples.",
            structured_output_model=TechnicalAnswer,  # Auto-extraction!
        ),
        tools=[python_executor],
        verbose=False,
    )

    creative = SimpleAgentV3(
        name="creative",
        engine=AugLLMConfig(
            temperature=0.8,
            system_message="Create engaging creative content.",
            structured_output_model=CreativeResponse,  # Auto-extraction!
        ),
        verbose=False,
    )

    research = ReactAgent(
        name="research",
        engine=AugLLMConfig(
            temperature=0.3,
            system_message="Conduct thorough research.",
            structured_output_model=ResearchFindings,  # Auto-extraction!
        ),
        tools=[research_database],
        verbose=False,
    )

    # Test queries
    queries = [
        "How do I implement quicksort in Python?",
        "Write a haiku about machine learning",
        "What are the cognitive benefits of bilingualism?",
    ]

    for query in queries:
        print(f"\n📋 Query: {query}")
        print("-" * 50)

        # Step 1: Classify
        classification = await classifier.arun(
            {"messages": [HumanMessage(content=query)]}
        )

        # Thanks to automatic extraction, classification is QueryClassification!
        print(
            f"✅ Category: {classification.category} ({classification.confidence:.0%})"
        )
        print(f"   Reasoning: {classification.reasoning}")

        # Step 2: Route to specialist
        print(f"\n🎯 Routing to {classification.category} agent...")

        if classification.category == "technical":
            result = await technical.arun({"messages": [HumanMessage(content=query)]})
            # result is TechnicalAnswer!
            print(f"   Solution: {result.solution[:100]}...")
            if result.code_example:
                print(f"   Code provided: Yes ({result.complexity} level)")

        elif classification.category == "creative":
            result = await creative.arun({"messages": [HumanMessage(content=query)]})
            # result is CreativeResponse!
            print(f"   Content: {result.content}")
            print(f"   Style: {result.style}, Mood: {result.mood}")

        else:  # research
            result = await research.arun({"messages": [HumanMessage(content=query)]})
            # result is ResearchFindings!
            print(f"   Summary: {result.summary[:100]}...")
            print(f"   Key findings: {len(result.key_findings)} items")
            print(f"   Sources: {result.sources_count}")

    print("\n\n✅ Branching complete!")
    print("\n💡 Key Benefits of Automatic Extraction:")
    print("1. No manual extraction needed")
    print("2. Type-safe results (IDE autocomplete works!)")
    print("3. Clean, readable code")
    print("4. Pydantic validation ensures data quality")


if __name__ == "__main__":
    asyncio.run(main())
